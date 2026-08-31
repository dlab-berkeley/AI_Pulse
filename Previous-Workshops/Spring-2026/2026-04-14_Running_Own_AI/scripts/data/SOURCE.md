# Training Data

Two pipelines are provided. The **full-papers pipeline** is the one that produced the released fine-tuned adapter ([`brunosmaniotto/condmat-qwen25-qlora-fullpapers`](https://huggingface.co/brunosmaniotto/condmat-qwen25-qlora-fullpapers)) demoed in the workshop. The abstracts-only pipeline is kept for reference and as a lighter-weight starting point.

---

## Full-papers pipeline (used for the workshop adapter)

Downloads the full LaTeX source of 100 recent papers from arXiv category `cond-mat.str-el` (strongly correlated electrons) and builds four kinds of training examples per paper:

1. `title -> abstract` — what should this paper emphasize?
2. `intro paragraph -> continuation` — flow and coherence
3. `section heading + context -> section body` — structure and argument
4. `body -> abstract` — summarization in the field's voice

This yields roughly **2,282 training + 254 validation examples** from 100 papers (~25 examples per paper after filtering).

### Regenerating

```bash
pip install arxiv tqdm
python download_full_papers.py \
    --category "cond-mat.str-el" \
    --max-results 100 \
    --output-dir ./arxiv_fullpapers
python prepare_training_data_full.py \
    --manifest ./arxiv_fullpapers/papers_manifest.jsonl \
    --papers-root ./arxiv_fullpapers \
    --output-dir ./data
```

### Outputs

- `arxiv_fullpapers/papers/<arxiv_id>_<title>/` — extracted `.tex` files per paper
- `arxiv_fullpapers/papers_manifest.jsonl` — one JSON record per paper (id, title, abstract, authors, tex files)
- `data/train.jsonl`, `data/val.jsonl` — chat-formatted training/validation splits (90/10)

Note: downloading LaTeX source bundles is slower and more bandwidth-intensive than fetching abstracts. The script pauses 3 s between papers by default to be polite to arXiv.

---

## Abstracts-only pipeline (lighter alternative)

If you just want to teach a model the style of abstracts (shorter runs, smaller data), use the simpler pipeline:

```bash
pip install arxiv tqdm
python download_arxiv.py --category "cond-mat.str-el" --max-results 2000
python prepare_training_data.py
```

This produces:

- `abstracts/` — individual abstract text files
- `abstracts.jsonl` — all abstracts as a single JSONL file
- `train.jsonl` + `val.jsonl` — formatted training/validation splits (1,800/200)

Only uses `title -> abstract` pairs. Faster to collect and train on, but the fine-tuned model will only learn abstract-style conventions, not the broader structure of a paper.
