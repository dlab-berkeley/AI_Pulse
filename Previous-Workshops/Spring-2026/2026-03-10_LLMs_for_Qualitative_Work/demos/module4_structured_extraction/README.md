# Module 4: Structured Extraction (LangExtract)

## Overview

This module demonstrates how to use large language models (LLMs) for structured extraction from qualitative text. We use survey responses about food insecurity on campus to extract and classify key information using a predefined schema and codebook.

Structured extraction helps researchers move from raw qualitative data to organized, analyzable information while preserving nuance and reducing manual coding effort.

## Anchor Paper

**Addressing Food Insecurity in Higher Education: A Qualitative Study of Student Experiences and Institutional Barriers**
(Example reference: Similar to research published in the Journal of College Student Psychotherapy, PMC-indexed studies on food insecurity)

This module uses synthesized survey data inspired by real food insecurity research in higher education. The extraction schema and codebook reflect established qualitative research frameworks from multilevel analysis and barrier frameworks in public health.

## Files

- **survey_responses.txt** — 15 synthetic open-ended responses to "What barriers have you faced in accessing food on campus this semester?" Responses vary in length, sentiment, and barrier types; includes 2-3 ambiguous/sarcastic responses.

- **extraction_schema.txt** — Formal schema defining what to extract: Barrier Type, Level (intrapersonal/interpersonal/institutional), Sentiment, Resources Mentioned, Key Entities, Urgency.

- **codebook.txt** — Coding framework with 6 themes (Cost, Time/Schedule, Dietary/Cultural, Location, Stigma/Awareness, Institutional Support Gaps). Each theme includes definition, indicators, and examples.

- **prompts.txt** — Two extraction approaches:
  - **Version A**: Plain Gemini chat prompt for non-coders
  - **Version B**: Python script for Google Colab using Gemini API

- **README.md** — This file.

## Demo Instructions

### Option 1: Gemini Chat (Non-coder friendly)

1. Open [Google Gemini](https://gemini.google.com)
2. Copy the **Version A prompt** from `prompts.txt`
3. Paste it into Gemini, including the codebook, schema, and survey responses
4. Gemini will return a table of extracted and classified information
5. Copy the table into a spreadsheet for further analysis

**Expected output:** A table with columns for Response ID, Barrier Type, Level, Sentiment, Resources Mentioned, Key Entities, and Urgency.

**Discussion point:** How consistent are the model's extractions? Where does sarcasm (R4) or ambiguity (R11, R14) affect coding?

### Option 2: Python Script for Google Colab (Programmers)

1. Open [Google Colab](https://colab.research.google.com)
2. Create a new notebook and copy the **Version B script** from `prompts.txt`
3. Set your Gemini API key:
   ```python
   import os
   os.environ["GEMINI_API_KEY"] = "your-api-key-here"
   ```
4. Run the script cell by cell:
   - First cell: Install dependencies (`pip install google-generativeai pandas`)
   - Second cell: Define responses and initialize the model
   - Third cell: Run extraction loop
   - Fourth cell: View results and export CSV
5. Results are saved to `campus_food_access_extracted.csv`

**Expected output:** CSV file with extracted and classified data, ready for further analysis or comparison with human-coded data.

**Discussion point:** How do programmatic extractions compare to manual coding? What biases might the model introduce?

## Key Concepts

### Structured Extraction vs. Manual Coding
- **Traditional approach:** Researchers read all responses, manually apply codes, discuss disagreements
- **LLM approach:** Define extraction schema, prompt LLM, review and adjust as needed
- **Hybrid approach:** Use LLM for initial extraction, then have researchers review and correct

### Codebook Design
The codebook in this module uses a **thematic approach** with a defined hierarchy for ambiguous cases:
- **Stigma/Awareness** → **Cost** → **Time** → **Location** → **Dietary** → **Institutional**

This reflects the assumption that awareness/stigma issues are often foundational (students don't know resources exist, so cost is secondary). In your own research, establish this hierarchy based on theory or initial interviews.

### Handling Ambiguity and Sarcasm
- **R4** uses sarcasm to critique cost barriers but is coded as Cost Barriers (not Stigma)
- **R11** mentions both awareness gaps and cost; coded as Stigma/Awareness (per hierarchy)
- **R14** blends cost and stigma; coded as Stigma (person had access but couldn't overcome shame)

LLMs generally handle sarcasm well when the context is clear, but always review ambiguous cases.

### Multilevel Framework
Barriers are classified by the level at which they operate:
- **Intrapersonal:** Individual knowledge, beliefs, emotions (e.g., shame, lack of awareness)
- **Interpersonal:** Social dynamics, discrimination (e.g., rude dining workers)
- **Institutional:** System-level policies, resource design (e.g., grad student exclusion from meal plans)

This framework helps identify where interventions are most needed.

## Discussion Points

1. **Accuracy and Bias:** How well does the LLM handle nuance? Where might it misclassify? Compare LLM output to human coding on a subset (R4, R11, R14 are good test cases).

2. **Schema Design:** Is this schema capturing what matters for your research question? What barriers are missing? How would you adjust barrier types for your own data?

3. **Scale and Reproducibility:** What are the advantages of programmatic extraction over manual coding? What is lost? When would you choose one approach over the other?

4. **Transparency and Justification:** Should you report which responses were extracted by LLM vs. manual coding? What disclosure is ethically required in published research?

## Explore Further

- **spacy-llm:** Combine spaCy's NLP pipeline with LLM extraction for hybrid approaches. See: https://spacy.io/usage/large-language-models

- **LangChain:** Build more complex extraction workflows with retries, validation, and chaining. See: https://python.langchain.com/docs/modules/data_connection/document_loaders/

- **Instructor Library:** Use Pydantic for type-safe, validated extraction. Ensures output conforms to your schema automatically. See: https://github.com/jxnl/instructor

- **Human-in-the-Loop Workflows:** Implement active learning to iteratively improve extraction by having researchers label uncertain cases.

## Technical Requirements

- **Google Gemini API key** (free tier available with rate limits)
- **Python 3.8+** (for script version)
- **Pandas** and **google-generativeai** libraries (installed via pip)

## Citation

If using this module or adapted data in published research, cite the underlying food insecurity research and acknowledge the use of LLM-assisted extraction.
