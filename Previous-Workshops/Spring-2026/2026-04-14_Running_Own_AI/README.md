# Local LLMs: From Download to Deployment

D-Lab AI Pulse Workshop — Session 7, April 14, 2026

## Workshop Arc

1. **Run it** — Install Ollama, pull a model, chat locally in three commands
2. **Use it for writing** — Ping-pong iterative approach: human ideas, AI phrasing, human judgment
3. **Fit your paper in it** — Context windows (up to 128K tokens) and quantization (Q4/Q8)
4. **Make it yours** — LoRA/QLoRA fine-tuning on NRP (National Research Platform) using ~2,000 arXiv abstracts
5. **Share it** — Upload the adapter to HuggingFace; collaborators load it in two commands

## Key Files

- `slides/` — LaTeX Beamer source and compiled PDF (33 slides)
- `scripts/` — Demo scripts and NRP deployment configs:
  - `nrp_hosted_llm_demo.ipynb` — Jupyter notebook: use NRP's hosted LLMs via API
  - `nrp_finetune_notebook.ipynb` — Jupyter notebook: QLoRA fine-tuning on NRP JupyterHub
  - `nrp_training_job.yaml` — Kubernetes Job for batch fine-tuning on NRP
  - `nrp_vllm_deployment.yaml` + `nrp_vllm_service.yaml` — Deploy fine-tuned model on NRP
  - `train_qlora.py` — Core training script (platform-agnostic)
  - `download_arxiv.py`, `prepare_training_data.py` — Data pipeline
  - `upload_to_huggingface.py` — Share adapter on HuggingFace Hub
  - `nrp_merge_and_serve.py` — Merge LoRA adapter into base model (fallback for serving)
  - `dry_run_output.md` — Full output from NRP JupyterHub QLoRA dry run
- `demo_materials/` — Pre-recorded demo conversations and real model outputs

## Format

~37 min presentation (all demos are pre-run screenshots/logs) + ~13 min discussion.

## D-Lab

https://dlab.berkeley.edu/
