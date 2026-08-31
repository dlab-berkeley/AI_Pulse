"""
download_arxiv.py — Download arXiv abstracts for LLM fine-tuning data.

Fetches paper metadata (title, abstract, authors, etc.) from a given arXiv
category and saves the results as individual text files and a single JSONL file.

Usage:
    pip install arxiv tqdm
    python download_arxiv.py --category "cond-mat.str-el" --max-results 500

The JSONL output is ready to use as training data for fine-tuning an LLM
on academic writing style.
"""

import argparse
import json
import os
import time
from pathlib import Path

import arxiv
from tqdm import tqdm


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download arXiv abstracts for LLM fine-tuning."
    )
    parser.add_argument(
        "--category",
        type=str,
        default="cond-mat.str-el",
        help='arXiv category to query (default: "cond-mat.str-el").',
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=2000,
        help="Maximum number of papers to download (default: 2000).",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="./arxiv_data",
        help='Directory to save output files (default: "./arxiv_data").',
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Helper: sanitise a string for use as a filename
# ---------------------------------------------------------------------------

def sanitize_filename(name: str, max_length: int = 80) -> str:
    """Remove or replace characters that are unsafe in filenames."""
    # Replace common problematic characters with underscores
    for ch in r'\/:*?"<>|':
        name = name.replace(ch, "_")
    # Collapse runs of whitespace / underscores
    name = "_".join(name.split())
    return name[:max_length]


# ---------------------------------------------------------------------------
# Core download logic
# ---------------------------------------------------------------------------

def download_abstracts(category: str, max_results: int, output_dir: str):
    """
    Query arXiv for papers in *category*, then save:
      1. One .txt file per abstract  (in <output_dir>/abstracts/)
      2. One JSONL file with all metadata  (<output_dir>/abstracts.jsonl)
    """

    # --- Set up output directories -------------------------------------------
    output_path = Path(output_dir)
    abstracts_dir = output_path / "abstracts"
    abstracts_dir.mkdir(parents=True, exist_ok=True)

    jsonl_path = output_path / "abstracts.jsonl"

    print(f"Category  : {category}")
    print(f"Max papers: {max_results}")
    print(f"Output    : {output_path.resolve()}")
    print()

    # --- Build the arXiv API query -------------------------------------------
    # The arxiv package wraps the arXiv API.  We search by category using the
    # query syntax "cat:<category>" and sort by submission date (newest first).
    client = arxiv.Client(
        page_size=100,          # results per API call (max 100)
        delay_seconds=3.0,      # polite delay between API pages
        num_retries=5,          # retry on transient errors
    )

    search = arxiv.Search(
        query=f"cat:{category}",
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )

    # --- Iterate through results and save ------------------------------------
    saved_count = 0

    with open(jsonl_path, "w", encoding="utf-8") as jsonl_file:
        # tqdm wraps the iterator so we get a live progress bar
        for result in tqdm(
            client.results(search),
            total=max_results,
            desc="Downloading",
            unit="paper",
        ):
            # Extract the fields we care about
            arxiv_id = result.entry_id.split("/")[-1]  # e.g. "2401.12345v1"
            title = result.title.replace("\n", " ")
            abstract = result.summary.replace("\n", " ")
            authors = [author.name for author in result.authors]
            categories = result.categories
            published = result.published.isoformat()

            # -- Save individual text file ------------------------------------
            filename = f"{arxiv_id}_{sanitize_filename(title)}.txt"
            txt_path = abstracts_dir / filename
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n")
                f.write(f"arXiv ID: {arxiv_id}\n")
                f.write(f"Authors: {', '.join(authors)}\n")
                f.write(f"Published: {published}\n")
                f.write(f"Categories: {', '.join(categories)}\n\n")
                f.write(abstract + "\n")

            # -- Append to JSONL file -----------------------------------------
            record = {
                "id": arxiv_id,
                "title": title,
                "abstract": abstract,
                "authors": authors,
                "categories": categories,
                "published": published,
            }
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")

            saved_count += 1

            # Small extra delay between individual results to be respectful.
            # The client already adds delay_seconds between *pages*, but this
            # adds a tiny pause so we never hammer the API.
            time.sleep(0.05)

    print()
    print(f"Done! Saved {saved_count} abstracts.")
    print(f"  Text files : {abstracts_dir.resolve()}")
    print(f"  JSONL file : {jsonl_path.resolve()}")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    args = parse_args()
    download_abstracts(
        category=args.category,
        max_results=args.max_results,
        output_dir=args.output_dir,
    )

    # ----- Example usage (for the workshop) -----
    # Download 500 condensed-matter (strongly correlated electrons) abstracts:
    #   python download_arxiv.py --category "cond-mat.str-el" --max-results 500
    #
    # Download 1000 machine-learning papers:
    #   python download_arxiv.py --category "cs.LG" --max-results 1000
    #
    # The resulting abstracts.jsonl file can be used directly for fine-tuning
    # with tools like Ollama, LM Studio, or the OpenAI fine-tuning API.
