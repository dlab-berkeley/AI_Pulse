# Module 1: Document Analysis with NotebookLM

## Overview

This module demonstrates how to use **NotebookLM** (Google's AI research notebook tool) for grounded qualitative analysis of multiple documents. We use the UC Berkeley student housing crisis as a case study to show how different stakeholders frame problems and solutions.

### Key Learning Objectives

- Upload diverse documents to NotebookLM to create an AI-powered research notebook
- Ask targeted questions across multiple sources to identify framings and disagreements
- Use AI to surface contradictions and complementary perspectives
- Understand when LLMs are useful for qualitative work (document synthesis, pattern finding) vs. when human interpretation is essential

---

## The Research Question

**How do different stakeholders frame the causes of and solutions to Berkeley's student housing crisis?**

### Why This Question?

Housing is a politically contentious issue where:
- **Universities** emphasize capacity constraints and need for new construction
- **Cities** focus on affordability, community impacts, and development concerns
- **Researchers** analyze market failures, policy design, and equity dimensions
- **Students** experience the consequences directly

Using NotebookLM to analyze documents from these different perspectives teaches students how AI tools can help identify framings that might be invisible within any single document.

---

## Documents for NotebookLM

Download the following documents (see `SOURCE.md` for detailed download instructions):

### 1. **Anchor Paper: Jiang-Brittan (2025)**
- **Title:** *Crisis by Design: Student Housing and the Hidden Cost of Higher Education*
- **Type:** Academic paper
- **Length:** ~20-30 pages (typical for journal article)
- **Role:** Provides theoretical framework; explicitly discusses framing of the housing crisis
- **File:** `Jiang-Brittan_2025_Crisis_by_Design.pdf`

### 2. **Chancellor's Housing Initiative**
- **Type:** Official university statement
- **Length:** ~3-5 pages
- **Role:** University administration's public framing of the problem and solutions
- **File:** `Chancellor_Housing_Initiative.pdf` or `.html`

### 3. **UC Berkeley Housing Task Force**
- **Type:** Institutional policy document
- **Length:** ~5-10 pages (may include links to longer reports)
- **Role:** University's internal deliberation on housing; may reveal constraints acknowledged internally
- **File:** `Housing_Task_Force.pdf` or `.html`

### 4. **Policy Review @ Berkeley Housing Analysis**
- **Type:** Student-run policy analysis (independent perspective)
- **Length:** ~5-10 pages
- **Role:** Critical, data-driven analysis; represents student/academic perspective on solutions
- **File:** `PRB_Housing_Analysis.pdf` or `.html`

---

## Demo Workflow

### Step 1: Create NotebookLM Notebook

1. Go to **[notebooklm.google.com](https://notebooklm.google.com)**
2. Sign in with a Google account
3. Create a new notebook
4. Upload all 4 documents (see above)
5. Wait for NotebookLM to process (2-3 minutes)

### Step 2: Ask Targeted Questions

Use the following prompts to explore different aspects of the housing crisis framing:

#### **Question 1: How does each document frame the causes?**

> "How does each document frame the causes of the student housing crisis? Is it presented as a supply problem, a policy failure, a market design issue, or something else? What evidence does each document cite?"

**What this reveals:**
- Different stakeholders emphasize different root causes
- Some documents may prioritize "facts" while others emphasize values/priorities
- Academic vs. advocacy framings

**Student discussion prompt:**
> "Which framing seems most persuasive to you? Why might someone from each organization believe their framing?"

---

#### **Question 2: What solutions does each document propose?**

> "What solutions does each document propose for the student housing crisis? Who would benefit from each proposed solution, and who might oppose it? Are there solutions mentioned by only one document?"

**What this reveals:**
- Solutions map directly to framings (if it's a supply problem → build more; if it's affordability → price controls/subsidies)
- Stakeholder interests become visible in which solutions are prioritized
- Documents may disagree on feasibility or desirability of solutions

**Student discussion prompt:**
> "If you had to choose one solution, which would you recommend? What values are you prioritizing?"

---

#### **Question 3: University vs. City disagreement**

> "Where do the university and the city disagree on housing responsibility? What does the university say the city should do? What does city-level analysis suggest the university should do? Are there solutions neither party mentions?"

**What this reveals:**
- Institutional boundaries affect problem framing
- Some solutions require coordination that documents don't acknowledge
- Hidden assumptions about who should pay/act

**Student discussion prompt:**
> "Is this a coordination problem, a values conflict, or both?"

---

### Step 3: Create Audio Overview (Optional)

NotebookLM can create an auto-generated podcast-style discussion of your documents:

1. In your notebook, click **"Audio Overview"** or **"Notebook Guide"** button
2. Review the generated summary
3. Note how the AI prioritizes and synthesizes across documents
4. **Critically discuss:** What did it emphasize? What was left out?

---

### Step 4: Guided Notes (Optional)

Use NotebookLM's **guided notes** feature to:
- Generate a reading guide
- Create flashcards from key concepts
- Produce an outline structure

**Reflection:** Compare the AI-generated outline to the questions you asked. What structure emerges?

---

## Demo Prompts & Discussion Questions

### For Instructors/Facilitators

Use these talking points to highlight what NotebookLM does well and its limitations:

**Strengths:**
- ✓ Quickly synthesizes information across multiple documents
- ✓ Can identify contradictions and different framings at scale
- ✓ Useful for finding specific information ("What does each document say about affordability?")
- ✓ Can generate learning guides and overviews that save reading time

**Limitations:**
- ✗ May miss nuance, tone, or implicit framings
- ✗ Could reinforce biases in source documents without flagging them
- ✗ Requires human interpretation of why disagreements exist
- ✗ Should not replace close reading for research papers
- ✗ Can hallucinate details if documents are ambiguous

**Discussion Prompts:**
1. "Did NotebookLM's synthesis match your reading? What did it miss?"
2. "How would you use this tool in your own research? What kinds of documents would it be useful for?"
3. "What risks do you see in relying on AI summaries for academic work?"

---

## Explore Further

After the demo, students can explore:

### 1. **Claude Projects**
- Create a Claude project on housing policy
- Upload documents to a project
- Use Claude to build a structured research notebook
- Compare Claude's approach to NotebookLM

### 2. **Google Gemini with Drive**
- Upload documents to Google Drive
- Use Gemini to analyze files from Drive
- Try asking questions across 10+ documents
- Explore Gemini's image/diagram analysis for institutional org charts

### 3. **ChatGPT File Analysis**
- Upload PDFs directly to ChatGPT
- Compare how different LLMs handle the same documents
- Test which LLM best identifies framing differences

### 4. **Research Extensions**
- Apply this workflow to your own documents (policy briefs, interview transcripts, news articles)
- Combine with qualitative coding (Module 2) to categorize framing elements
- Use AI output as starting point for manual analysis, not final answer

---

## Technical Notes

### Document Format Compatibility

NotebookLM accepts:
- ✓ PDF files (most reliable)
- ✓ Google Docs
- ✓ Google Drive links
- ✓ Web links (sometimes)

### File Size & Processing
- Maximum file size: ~50MB per document
- Processing time: 1-3 minutes for typical academic papers
- Best results: documents with clear structure (headings, sections)

### Privacy Considerations
- Documents uploaded to NotebookLM are processed by Google
- Do not upload confidential or proprietary documents
- Google may use content for model training (check terms)
- For sensitive research, consider local alternatives (Claude, Ollama)

---

## Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| NotebookLM won't upload PDFs | Convert to Google Docs first, or try uploading via Google Drive link |
| Prompts give generic answers | Be specific: "According to [Document Name]..." |
| Different tool gives different answer | Expected! Models may notice different details |
| I want offline analysis | Try Claude Projects or Ollama (Module 6) |

---

## Files in This Folder

```
module1_document_analysis/
├── README.md                                    ← You are here
├── SOURCE.md                                    ← Download instructions for all documents
├── Jiang-Brittan_2025_Crisis_by_Design.pdf     ← Anchor paper (download from URL)
├── Chancellor_Housing_Initiative.pdf            ← University statement
├── Housing_Task_Force.pdf                       ← Task force report
└── PRB_Housing_Analysis.pdf                     ← Policy analysis
```

---

## Workshop Integration

- **Session:** LLMs for Qualitative Work
- **Module:** 1 (Document Analysis)
- **Duration:** ~20 minutes (demo) + 10 minutes (discussion)
- **Next Module:** Module 2 - Qualitative Coding with AI
- **Skills Practiced:**
  - Using AI for literature synthesis
  - Identifying assumptions & framings in documents
  - Critical evaluation of AI outputs
  - Building research questions

---

## References & Further Reading

If students want to learn more about:

- **AI for qualitative research:** Search "LLMs qualitative methodology" in educational databases
- **UC Berkeley housing:** The anchor paper (Jiang-Brittan) has comprehensive references
- **NotebookLM:** Google's AI Overviews blog and help documentation
- **Policy framing:** See political science literature on "frame analysis"

---

**Last Updated:** February 2026

**Created for:** AI-Pulse Workshop Series, UC Berkeley D-Lab

**Questions?** Contact D-Lab or your workshop facilitator.
