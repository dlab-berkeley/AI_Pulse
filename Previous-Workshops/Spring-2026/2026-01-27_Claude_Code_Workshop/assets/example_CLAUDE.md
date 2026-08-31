# Example CLAUDE.md File

This file shows what a CLAUDE.md might look like for a research project.

---

# Project: Survey Analysis Pipeline

## Overview
This project processes and analyzes longitudinal survey data from the National Health Study (2020-2024). The goal is to identify trends in health behaviors across demographic groups.

## Project Structure
```
├── data/
│   ├── raw/          # Original survey files (DO NOT MODIFY)
│   └── processed/    # Cleaned datasets
├── src/
│   ├── cleaning/     # Data cleaning scripts
│   ├── analysis/     # Statistical analysis
│   └── viz/          # Visualization code
├── results/          # Output figures and tables
└── docs/             # Documentation
```

## Coding Conventions
- Use Python 3.10+
- Follow PEP 8 style guidelines
- All functions must have docstrings with parameter descriptions
- Use type hints for function signatures
- Numerical operations: prefer numpy over pandas where possible
- Statistical tests: use scipy.stats or statsmodels

## Data Notes
- Raw data contains PII - never commit to git
- Missing values coded as -99 in original data
- Date format: YYYY-MM-DD
- Income is in 2020 dollars (adjusted)

## Common Tasks
- Data cleaning: `python src/cleaning/process_raw.py`
- Run analysis: `python src/analysis/main.py`
- Generate figures: `python src/viz/create_plots.py`

## Important Considerations
- All analyses must be reproducible (set random seeds)
- Save intermediate results to enable checkpointing
- Log all data transformations
