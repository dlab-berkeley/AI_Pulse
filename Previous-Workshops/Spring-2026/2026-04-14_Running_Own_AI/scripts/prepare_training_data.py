#!/usr/bin/env python3
"""
prepare_training_data.py
========================
Converts arXiv paper metadata (JSONL) into a chat-formatted training dataset
for fine-tuning a language model to write physics paper abstracts.

Input:  JSONL file with fields: id, title, abstract, authors, categories, published
Output: train.jsonl and val.jsonl in chat/instruction format

Usage:
    python prepare_training_data.py --input arxiv_papers.jsonl --output-dir ./data
"""

import argparse
import json
import random
from pathlib import Path


# ---------------------------------------------------------------------------
# Chat template
# ---------------------------------------------------------------------------
# We use a simple chat template compatible with Llama-3 instruction format.
# Each training example is a single turn: system sets the persona, user gives
# the paper title, and the assistant writes the abstract.

SYSTEM_PROMPT = (
    "You are an expert academic writer specializing in condensed matter physics. "
    "You write in the style of published research papers in this field."
)


def format_example(title: str, abstract: str) -> str:
    """Wrap a (title, abstract) pair in the chat template."""
    return (
        f"<|system|>{SYSTEM_PROMPT}<|end|>\n"
        f'<|user|>Write an abstract for a paper titled: "{title}"<|end|>\n'
        f"<|assistant|>{abstract}<|end|>"
    )


# ---------------------------------------------------------------------------
# Data loading and cleaning
# ---------------------------------------------------------------------------

def load_papers(input_path: str) -> list[dict]:
    """Read the arXiv JSONL file and return a list of paper dicts."""
    papers = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            paper = json.loads(line)
            papers.append(paper)
    return papers


def clean_abstract(abstract: str) -> str:
    """Light cleaning: collapse whitespace and strip leading/trailing space."""
    return " ".join(abstract.split())


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Prepare arXiv abstracts for LLM fine-tuning."
    )
    parser.add_argument(
        "--input", required=True,
        help="Path to the arXiv JSONL file."
    )
    parser.add_argument(
        "--output-dir", default="./data",
        help="Directory to write train.jsonl and val.jsonl (default: ./data)."
    )
    parser.add_argument(
        "--val-fraction", type=float, default=0.10,
        help="Fraction of data reserved for validation (default: 0.10)."
    )
    parser.add_argument(
        "--seed", type=int, default=42,
        help="Random seed for reproducibility (default: 42)."
    )
    args = parser.parse_args()

    # -- Load raw papers -------------------------------------------------------
    papers = load_papers(args.input)
    print(f"Loaded {len(papers)} papers from {args.input}")

    # -- Format each paper as a training example --------------------------------
    examples = []
    abstract_lengths = []

    for paper in papers:
        title = paper["title"].strip()
        abstract = clean_abstract(paper["abstract"])

        # Skip entries with missing data
        if not title or not abstract:
            continue

        text = format_example(title, abstract)
        examples.append({"text": text})
        abstract_lengths.append(len(abstract))

    print(f"Formatted {len(examples)} valid examples (skipped {len(papers) - len(examples)})")

    # -- Shuffle and split into train / validation ------------------------------
    random.seed(args.seed)
    random.shuffle(examples)

    val_size = int(len(examples) * args.val_fraction)
    val_examples = examples[:val_size]
    train_examples = examples[val_size:]

    # -- Save to disk -----------------------------------------------------------
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    train_path = output_dir / "train.jsonl"
    val_path = output_dir / "val.jsonl"

    for path, data in [(train_path, train_examples), (val_path, val_examples)]:
        with open(path, "w", encoding="utf-8") as f:
            for entry in data:
                f.write(json.dumps(entry) + "\n")

    # -- Print summary statistics -----------------------------------------------
    avg_len = sum(abstract_lengths) / len(abstract_lengths) if abstract_lengths else 0

    print()
    print("=== Dataset Statistics ===")
    print(f"  Total examples : {len(examples)}")
    print(f"  Training set   : {len(train_examples)}")
    print(f"  Validation set : {len(val_examples)}")
    print(f"  Avg abstract   : {avg_len:.0f} characters")
    print()
    print(f"  Saved: {train_path}")
    print(f"  Saved: {val_path}")


if __name__ == "__main__":
    main()
