#!/usr/bin/env python3
"""
upload_to_huggingface.py
========================
Upload a trained LoRA adapter to the HuggingFace Hub so others can use it.

This creates a model repository with:
  - The adapter weights (adapter_model.safetensors)
  - The adapter config (adapter_config.json)
  - A model card (README.md) explaining what the adapter is and how to use it

Usage:
    python upload_to_huggingface.py \
        --adapter-dir ./output/physics-adapter \
        --repo-name your-username/physics-abstract-writer \
        --private
"""

import argparse
from pathlib import Path

from huggingface_hub import HfApi, create_repo


# ---------------------------------------------------------------------------
# Model card template
# ---------------------------------------------------------------------------
# This README.md is automatically placed in the HuggingFace repo.
# It tells users what the adapter is and how to load it.

MODEL_CARD_TEMPLATE = """\
---
library_name: peft
base_model: {base_model}
tags:
  - qlora
  - lora
  - llama
  - physics
  - arxiv
  - condensed-matter
license: mit
---

# Physics Abstract Writer (LoRA Adapter)

This is a **QLoRA adapter** for [{base_model}](https://huggingface.co/{base_model})
fine-tuned on condensed matter physics paper abstracts from arXiv.

Given a paper title, the model generates an abstract in the style of published
research papers.

## Training Details

| Parameter | Value |
|-----------|-------|
| Base model | `{base_model}` |
| Method | QLoRA (4-bit NF4 quantization + LoRA) |
| LoRA rank | 16 |
| LoRA alpha | 32 |
| Epochs | {epochs} |
| Learning rate | {lr} |
| Training examples | arXiv abstracts (condensed matter physics) |

## How to Use

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "{base_model}",
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("{base_model}")

# Load the LoRA adapter on top
model = PeftModel.from_pretrained(base_model, "{repo_name}")

# Generate an abstract
prompt = (
    '<|system|>You are an expert academic writer specializing in '
    'condensed matter physics.<|end|>\\n'
    '<|user|>Write an abstract for a paper titled: '
    '"Topological Phase Transitions in Twisted Bilayer Graphene"<|end|>\\n'
    '<|assistant|>'
)

inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=256, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Created With

Fine-tuned as part of UC Berkeley D-Lab's AI-Pulse workshop series
using the QLoRA technique on a single GPU.
"""


# ---------------------------------------------------------------------------
# Upload logic
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Upload a LoRA adapter to HuggingFace Hub."
    )
    parser.add_argument(
        "--adapter-dir", required=True,
        help="Path to the saved adapter directory."
    )
    parser.add_argument(
        "--repo-name", required=True,
        help="HuggingFace repo name, e.g. 'your-username/physics-abstract-writer'."
    )
    parser.add_argument(
        "--private", action="store_true",
        help="Make the repository private (default: public)."
    )
    parser.add_argument(
        "--base-model", default="meta-llama/Llama-3.2-3B-Instruct",
        help="Base model ID (for the model card)."
    )
    parser.add_argument(
        "--epochs", type=int, default=3,
        help="Number of training epochs (for the model card)."
    )
    parser.add_argument(
        "--lr", type=float, default=2e-4,
        help="Learning rate used (for the model card)."
    )
    args = parser.parse_args()

    adapter_dir = Path(args.adapter_dir)
    if not adapter_dir.exists():
        print(f"Error: adapter directory not found: {adapter_dir}")
        return

    # -- Create the repository on HuggingFace ----------------------------------
    print(f"Creating repository: {args.repo_name} (private={args.private})")
    create_repo(
        repo_id=args.repo_name,
        repo_type="model",
        private=args.private,
        exist_ok=True,  # don't error if it already exists
    )

    # -- Write the model card --------------------------------------------------
    model_card_path = adapter_dir / "README.md"
    model_card = MODEL_CARD_TEMPLATE.format(
        base_model=args.base_model,
        repo_name=args.repo_name,
        epochs=args.epochs,
        lr=args.lr,
    )
    model_card_path.write_text(model_card, encoding="utf-8")
    print(f"Generated model card: {model_card_path}")

    # -- Upload all files in the adapter directory ------------------------------
    print("Uploading adapter files...")
    api = HfApi()
    api.upload_folder(
        folder_path=str(adapter_dir),
        repo_id=args.repo_name,
        repo_type="model",
    )

    # -- Print the result ------------------------------------------------------
    url = f"https://huggingface.co/{args.repo_name}"
    print()
    print("=" * 60)
    print("Upload complete!")
    print("=" * 60)
    print(f"  Repository URL: {url}")
    print()
    print("Anyone can now load your adapter with:")
    print(f'  PeftModel.from_pretrained(base_model, "{args.repo_name}")')


if __name__ == "__main__":
    main()
