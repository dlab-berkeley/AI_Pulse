#!/usr/bin/env python3
"""
nrp_merge_and_serve.py
======================
Merge a LoRA adapter into the base model and save the merged model.

This is a fallback for when vLLM's dynamic LoRA serving has issues.
The merged model can be served directly as a standard vLLM deployment
(without --enable-lora).

Usage:
    python nrp_merge_and_serve.py \
        --base-model meta-llama/Llama-3.2-3B-Instruct \
        --adapter-dir ./output/physics-adapter \
        --merged-dir ./output/physics-merged
"""

import argparse
import os

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def main():
    parser = argparse.ArgumentParser(
        description="Merge a LoRA adapter into the base model."
    )
    parser.add_argument(
        "--base-model", default="meta-llama/Llama-3.2-3B-Instruct",
        help="HuggingFace model ID for the base model.",
    )
    parser.add_argument(
        "--adapter-dir", required=True,
        help="Path to the saved LoRA adapter directory.",
    )
    parser.add_argument(
        "--merged-dir", required=True,
        help="Where to save the merged model.",
    )
    args = parser.parse_args()

    # Load base model in fp16
    print(f"Loading base model: {args.base_model}")
    model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        torch_dtype=torch.float16,
        device_map="cpu",  # merge on CPU to avoid VRAM issues
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.base_model, trust_remote_code=True)

    # Load and merge the LoRA adapter
    print(f"Loading adapter from: {args.adapter_dir}")
    model = PeftModel.from_pretrained(model, args.adapter_dir)

    print("Merging adapter into base model...")
    model = model.merge_and_unload()

    # Save the merged model
    print(f"Saving merged model to: {args.merged_dir}")
    os.makedirs(args.merged_dir, exist_ok=True)
    model.save_pretrained(args.merged_dir)
    tokenizer.save_pretrained(args.merged_dir)

    merged_size_gb = sum(
        os.path.getsize(os.path.join(args.merged_dir, f))
        for f in os.listdir(args.merged_dir)
        if f.endswith((".safetensors", ".bin"))
    ) / (1024 ** 3)

    print()
    print("=" * 60)
    print("Merge complete!")
    print("=" * 60)
    print(f"  Merged model: {args.merged_dir}")
    print(f"  Size: {merged_size_gb:.1f} GB")
    print()
    print("To serve with vLLM (no --enable-lora needed):")
    print(f'  vllm serve {args.merged_dir} --port 5000')


if __name__ == "__main__":
    main()
