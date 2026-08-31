# QLoRA Fine-Tuning Dry Run Output
## NRP JupyterHub Pipeline Test (Fallback for Workshop 7)

**Workshop Context:** Fine-tuning Qwen2.5-3B-Instruct on condensed matter physics abstracts using QLoRA on NRP JupyterHub free GPU resources.

**Date:** March 27, 2026

**Environment:**
- NRP JupyterHub (`jupyterhub-west.nrp-nautilus.io`), namespace `berkeley-dlab`
- GPU: NVIDIA GeForce RTX 2080 Ti (11 GB VRAM)
- PyTorch 2.5.1+cu124, CUDA 12.4
- trl 0.29.1, peft, bitsandbytes, transformers
- Precision: bf16 (auto-detected)

---

## Cell 1–4: Environment Setup

### GPU Check Output:
```
PyTorch version: 2.5.1+cu124
CUDA available: True
GPU: NVIDIA GeForce RTX 2080 Ti
VRAM: 11.8 GB
BF16 support: True
```

**Note:** NRP JupyterHub home directories are only 5 GB (`/dev/rbd0`). Model weights (~6 GB) must download to `/tmp` which has ~170 GB on the overlay filesystem. The notebook sets `HF_HOME=/tmp/hf_cache` to handle this.

---

## Cell 6: Configuration

```
MODEL_ID = "Qwen/Qwen2.5-3B-Instruct"
EPOCHS = 3
BATCH_SIZE = 4
GRAD_ACCUM_STEPS = 4  (effective batch size = 16)
LEARNING_RATE = 2e-4
MAX_SEQ_LENGTH = 512
LORA_RANK = 16, LORA_ALPHA = 32

Using bf16 mixed precision
```

**Key fix discovered:** `HF_HOME` must be set *before* any HuggingFace imports. The notebook places it at the top of the config cell.

---

## Cell 8: HuggingFace Authentication

Qwen2.5-3B-Instruct is **ungated** — no login or license approval needed. The HF login cell is fully commented out. Authentication is optional and only useful for avoiding download rate limits.

---

## Cell 10: Load Base Model (4-bit)

```
Loading tokenizer...
Tokenizer vocab size: 151,643
Loading base model in 4-bit precision...
Model loaded on: cuda:0
GPU memory used: 2.06 GB
```

First download takes ~2 minutes (6.17 GB). Subsequent loads from cache take ~6 seconds. The 4-bit quantization shrinks the model from ~6 GB to ~2 GB in GPU memory.

---

## Cell 12: Attach LoRA Adapters

```
trainable params: 29,933,568 || all params: 3,119,720,448 || trainable%: 0.9595
```

LoRA targets 7 module types per layer: q_proj, k_proj, v_proj, o_proj (attention) and gate_proj, up_proj, down_proj (MLP). Only 0.96% of parameters are trainable.

---

## Cell 14: Load Training Data

```
Train examples: 20  (dry run subset)
Val examples:   5   (dry run subset)

Sample training example (first 300 chars):
<|im_start|>system
You are an expert academic writer specializing in condensed matter physics.<|im_end|>
<|im_start|>user
Write an abstract for a paper titled: '...'<|im_end|>
<|im_start|>assistant
We investigate...
```

The full dataset will have ~1,800 train / ~200 val examples from arXiv condensed matter abstracts. The dry run used a 20/5 subset.

---

## Cell 16: Set Up Trainer

```
Effective batch size: 16
Training steps per epoch: 1  (20 examples / 16 effective batch = 1 step)
Total training steps: 3  (dry run)
```

**API compatibility note (trl 0.29.1):** The trainer uses `SFTConfig` (not `TrainingArguments`) and the sequence length parameter is `max_length` (not `max_seq_length`). The `SFTTrainer` takes `processing_class=tokenizer` instead of the older `tokenizer=` argument.

---

## Cell 18: Training Results

```
Epoch  Train Loss  Eval Loss  Mean Token Accuracy
  1      3.009      1.867         0.6176
  2      1.826      1.707         0.6484
  3      1.476      1.684         0.6582

Training time: 16.9 seconds (dry run, 5 steps)
Peak GPU memory: 4.14 GB / 11 GB available
```

Loss decreased steadily from 3.009 to 1.476 over 3 epochs. Eval loss stabilized around 1.68–1.71. With the full ~1,800 example dataset and 3 epochs, expect 30–60 minutes on a T4 or 15–30 minutes on an A100.

---

## Cell 20: Save Adapter

```
Adapter saved to: ./output/physics-adapter
Adapter size:     119.8 MB
Base model size:  ~6,000 MB (fp16)
Compression:      ~50x smaller
```

The adapter contains only the trained LoRA weights. To use it, anyone loads the base Qwen2.5-3B-Instruct model and applies the adapter on top.

**Note:** Adapter size is larger than typical (~20-50 MB) because the dry run targeted all 7 projection types with rank 16. For the full training run the adapter may be smaller relative to information content.

---

## Cell 22: Test Generation

**Prompt:** "Write an abstract for a paper titled: 'Topological Phase Transitions in Monolayer Jacutingaite (Pt2HgSe3): A Kane-Mele Analysis with Spin-Orbit and Rashba Corrections'"

### Fine-Tuned Model Output:

> We investigate the topological phase transitions in monolayer jacutingaite (Pt2HgSe3) using a Kane-Mele model augmented with intrinsic spin-orbit coupling and Rashba spin-orbit interaction terms. Through systematic variation of the spin-orbit coupling strength and sublattice potential, we map the complete topological phase diagram of this two-dimensional quantum spin Hall insulator. Our first-principles calculations, combined with tight-binding parametrization, reveal that monolayer Pt2HgSe3 hosts a robust quantum spin Hall phase characterized by a Z2 topological invariant, with a bulk band gap of approximately 0.15 eV that persists under moderate Rashba perturbations. We identify critical transition points where the system undergoes topological phase transitions from the quantum spin Hall state to a trivial insulating phase, driven by competition between intrinsic spin-orbit coupling and Rashba interaction.

The model produces domain-appropriate physics language, correct terminology (Z2 invariant, quantum spin Hall phase, tight-binding parametrization), and plausible numerical estimates — even after training on only 20 examples for 17 seconds.

---

## Known Issues & Workarounds

1. **"No space left on device" error:** Home directory is only 5 GB. Set `HF_HOME=/tmp/hf_cache` before importing HuggingFace libraries.

2. **Kernel crashes after pip install:** The `pip install` cell can destabilize the kernel if it upgrades PyTorch or other core packages. If the kernel dies, restart it and re-run from Cell 4 (skip the pip install cell on re-run).

3. **trl API version:** trl 0.29.1 uses `SFTConfig` instead of `TrainingArguments`, `max_length` instead of `max_seq_length`, and `processing_class` instead of `tokenizer`. If you see `unexpected keyword argument` errors, check these parameter names.

4. **OOM on smaller GPUs:** If batch size 4 causes out-of-memory errors, reduce `BATCH_SIZE` to 2 or 1. The gradient accumulation steps compensate to maintain the effective batch size.

---

## Summary for Workshop Demo

The full QLoRA pipeline works end-to-end on NRP JupyterHub free GPUs:

- **Total GPU memory needed:** ~4.1 GB peak (fits on any NRP GPU profile)
- **Model download:** ~2 min first time, ~6 sec cached
- **Training (dry run):** ~17 sec for 20 examples
- **Training (full, estimated):** 30–60 min for ~1,800 examples
- **Output:** A ~50-120 MB adapter file that makes Qwen2.5-3B write physics abstracts
- **Key takeaway for students:** You can fine-tune a 3B-parameter model on a free GPU in under an hour, producing domain-specific output that reads like a real physics paper
