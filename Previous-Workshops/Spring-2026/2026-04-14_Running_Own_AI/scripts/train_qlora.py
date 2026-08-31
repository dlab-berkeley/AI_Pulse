#!/usr/bin/env python3
"""
train_qlora.py
==============
Fine-tune Llama 3.2 3B on physics paper abstracts using QLoRA.

QLoRA (Quantized Low-Rank Adaptation) lets us fine-tune a large model on a
single consumer GPU by:
  1. Loading the base model in 4-bit precision  (~1.5 GB instead of ~6 GB)
  2. Attaching tiny trainable "adapter" matrices (LoRA) to each layer
  3. Training only those adapters — everything else stays frozen

The result is a small adapter file (~20-50 MB) that can be merged with the
base model at inference time.

Usage:
    python train_qlora.py \
        --train-data ./data/train.jsonl \
        --val-data   ./data/val.jsonl \
        --output-dir ./output/physics-adapter
"""

import argparse
import os

import torch
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
)
from trl import SFTTrainer


# ---------------------------------------------------------------------------
# 1. Argument parsing
# ---------------------------------------------------------------------------

def parse_args():
    parser = argparse.ArgumentParser(
        description="QLoRA fine-tuning of Llama 3.2 3B on arXiv abstracts."
    )
    parser.add_argument(
        "--model", default="meta-llama/Llama-3.2-3B-Instruct",
        help="HuggingFace model ID or local path (default: Llama-3.2-3B-Instruct)."
    )
    parser.add_argument("--train-data", required=True, help="Path to train.jsonl.")
    parser.add_argument("--val-data", required=True, help="Path to val.jsonl.")
    parser.add_argument("--output-dir", default="./output/physics-adapter",
                        help="Where to save the LoRA adapter.")
    parser.add_argument("--epochs", type=int, default=3, help="Training epochs (default: 3).")
    parser.add_argument("--batch-size", type=int, default=4, help="Per-device batch size (default: 4).")
    parser.add_argument("--lr", type=float, default=2e-4, help="Learning rate (default: 2e-4).")
    parser.add_argument("--max-seq-length", type=int, default=512,
                        help="Maximum sequence length for training examples (default: 512).")
    parser.add_argument("--bf16", action="store_true",
                        help="Use bf16 instead of fp16 (recommended for A100/H200 GPUs).")
    parser.add_argument("--save-total-limit", type=int, default=2,
                        help="Keep only the N best checkpoints to save disk space (default: 2).")
    return parser.parse_args()


# ---------------------------------------------------------------------------
# 2. Quantization config  (this is the "Q" in QLoRA)
# ---------------------------------------------------------------------------
# We load the base model in 4-bit NormalFloat (nf4) precision.  Double
# quantization further compresses the quantization constants themselves,
# saving a bit more memory.

def make_bnb_config():
    return BitsAndBytesConfig(
        load_in_4bit=True,                  # use 4-bit precision for base model
        bnb_4bit_quant_type="nf4",          # NormalFloat4 — optimal for normally-distributed weights
        bnb_4bit_use_double_quant=True,     # quantize the quantization constants too
        bnb_4bit_compute_dtype=torch.float16,  # compute in fp16 for speed
    )


# ---------------------------------------------------------------------------
# 3. LoRA config  (this is the "LoRA" in QLoRA)
# ---------------------------------------------------------------------------
# LoRA freezes the original weight matrices and injects small trainable
# rank-decomposition matrices alongside them.
#
#   r      = rank of the decomposition (higher = more capacity, more VRAM)
#   alpha  = scaling factor (usually 2*r works well)
#   target_modules = which linear layers get adapters
#
# We target all the attention projections (q, k, v, o) and the MLP
# projections (gate, up, down) in every transformer block.

def make_lora_config():
    return LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",  # attention
            "gate_proj", "up_proj", "down_proj",       # MLP
        ],
    )


# ---------------------------------------------------------------------------
# 4. Main training loop
# ---------------------------------------------------------------------------

def main():
    args = parse_args()

    print("=" * 60)
    print("QLoRA Fine-Tuning")
    print("=" * 60)
    print(f"  Base model   : {args.model}")
    print(f"  Train data   : {args.train_data}")
    print(f"  Val data     : {args.val_data}")
    print(f"  Output dir   : {args.output_dir}")
    print(f"  Epochs       : {args.epochs}")
    print(f"  Batch size   : {args.batch_size}")
    print(f"  Learning rate: {args.lr}")
    print()

    # -- Load tokenizer --------------------------------------------------------
    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)

    # Llama models may not have a pad token — use eos_token as a fallback
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # -- Load base model in 4-bit ----------------------------------------------
    print("Loading base model in 4-bit precision (this may take a minute)...")
    bnb_config = make_bnb_config()

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        quantization_config=bnb_config,
        device_map="auto",            # automatically place layers on GPU/CPU
        trust_remote_code=True,
    )

    # Prepare the quantized model for LoRA training (freezes base, enables
    # gradient checkpointing for memory efficiency)
    model = prepare_model_for_kbit_training(model)

    # -- Attach LoRA adapters --------------------------------------------------
    print("Attaching LoRA adapters...")
    lora_config = make_lora_config()
    model = get_peft_model(model, lora_config)

    # Show how few parameters we're actually training
    model.print_trainable_parameters()
    # Typical output: "trainable params: 27,262,976 || all params: 3,240,000,000 || trainable%: 0.84%"

    # -- Load datasets ---------------------------------------------------------
    print("Loading datasets...")
    dataset_train = load_dataset("json", data_files=args.train_data, split="train")
    dataset_val = load_dataset("json", data_files=args.val_data, split="train")
    print(f"  Train examples: {len(dataset_train)}")
    print(f"  Val examples  : {len(dataset_val)}")

    # -- Training arguments ----------------------------------------------------
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch_size,
        per_device_eval_batch_size=args.batch_size,
        gradient_accumulation_steps=4,       # effective batch size = 4 * 4 = 16
        learning_rate=args.lr,
        warmup_ratio=0.1,                    # 10% of steps for LR warmup
        fp16=not args.bf16,                  # mixed-precision training
        bf16=args.bf16,                      # use bf16 on A100/H200 GPUs
        logging_steps=10,                    # log loss every 10 steps
        eval_strategy="epoch",               # evaluate at the end of each epoch
        save_strategy="epoch",               # checkpoint at the end of each epoch
        save_total_limit=args.save_total_limit,  # limit checkpoints to save disk
        load_best_model_at_end=True,         # reload best checkpoint when done
        report_to="none",                    # disable wandb / tensorboard for simplicity
        optim="paged_adamw_8bit",            # memory-efficient optimizer from bitsandbytes
    )

    # -- Create the trainer ----------------------------------------------------
    # SFTTrainer (from trl) handles tokenization of the "text" field for us.
    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=dataset_train,
        eval_dataset=dataset_val,
        processing_class=tokenizer,
        max_seq_length=args.max_seq_length,
    )

    # -- Train! ----------------------------------------------------------------
    print()
    print("Starting training...")
    print("-" * 60)
    trainer.train()

    # -- Save the LoRA adapter (NOT the full 3B model) -------------------------
    print()
    print("Saving LoRA adapter...")
    trainer.model.save_pretrained(args.output_dir)
    tokenizer.save_pretrained(args.output_dir)

    # -- Report adapter size ---------------------------------------------------
    adapter_size_bytes = sum(
        os.path.getsize(os.path.join(args.output_dir, f))
        for f in os.listdir(args.output_dir)
        if f.endswith((".safetensors", ".bin"))
    )
    adapter_size_mb = adapter_size_bytes / (1024 * 1024)

    print()
    print("=" * 60)
    print("Training complete!")
    print("=" * 60)
    print(f"  Adapter saved to : {args.output_dir}")
    print(f"  Adapter size     : {adapter_size_mb:.1f} MB")
    print(f"  Base model size  : ~6,000 MB (fp16)")
    print(f"  Compression ratio: ~{6000 / max(adapter_size_mb, 0.1):.0f}x smaller")
    print()
    print("To use this adapter, load the base model and apply the adapter with PEFT.")
    print("See upload_to_huggingface.py to share it on the Hub.")


if __name__ == "__main__":
    main()
