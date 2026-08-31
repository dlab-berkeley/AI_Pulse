# Module 2 Demo: Dialogical Qualitative Coding with Gemini

## Overview

This module demonstrates **dialogical qualitative coding**—using a large language model (Gemini) as a thinking partner in thematic analysis. The demo uses a realistic synthetic interview about food insecurity at UC Berkeley to teach how AI can help organize, extract, and classify qualitative data while maintaining human judgment and interpretive authority.

**Key Learning Goal:** Students will see that AI-assisted coding is not about replacing human expertise. Rather, it's about making research decisions transparent, iterative, and dialogical. The AI surfaces patterns and ambiguities; the researcher makes meaning.

---

## Anchor Paper

**Citation:**  
Maroto, M. E., Snelling, A., & Linck, H. M. (2015). Navigating Hidden Hunger: Lived Experience of Food Insecurity among College Students. *Journal of Contemporary Ethnography*, 45(5), 540–569.  
**Open Access:** Available via PubMed Central (PMC)

This empirical study uses qualitative interviews with college students to analyze food insecurity as a lived experience, not just a metric. It identifies themes including stigma, coping, social isolation, and systemic barriers. Our codebook is loosely inspired by this paper's analytic structure.

---

## Research Question

**How do college students experience, respond to, and make meaning of food insecurity? And how can qualitative AI tools help us identify and organize these experiences systematically?**

---

## Files in This Directory

### 1. **interview_transcript.txt** (~2,000 words)
A realistic, de-identified interview with "Maya," a Berkeley junior.

**Content includes:**
- How she first realized she was food insecure (textbook vs. food trade-off)
- Coping strategies (free campus food, eating at friends' places, working, meal-prepping)
- Discovery of the UC Berkeley Food Pantry and emotional responses (shame, relief, anger)
- Work-study balance and academic impact
- Social dynamics and hiding food insecurity
- Institutional critique (meal plan costs, inadequate financial aid)
- Turning point: a professor's intervention and connection to a student organization
- Shift from individual coping to collective advocacy

**Design notes:**
- Written to feel natural and realistic (includes pauses, incomplete thoughts, tangential stories)
- Contains genuinely ambiguous passages suitable for discussion (e.g., "not wanting to burden anyone")
- Appropriate for teaching qualitative analysis (rich, detailed, emotionally complex)

### 2. **codebook.txt**
Pre-defined codebook with 8 codes designed for analyzing food insecurity experiences.

**Codes:**
1. **Financial Strain** – Lack of money and trade-offs between necessities
2. **Coping Strategies** – Concrete, active behaviors to manage food insecurity
3. **Stigma and Shame** – Negative emotions, fear of judgment, internalized blame
4. **Institutional Barriers** – University policies and structural constraints
5. **Social Support** – Relationships and community that provide food, encouragement, or belonging
6. **Academic Impact** – Effects on learning, engagement, and grades
7. **Food Access Resources** – Specific programs and channels for accessing food
8. **Agency and Advocacy** – Active resistance, systemic thinking, participation in organizing

**Each code includes:**
- Name and 2-3 sentence definition
- Inclusion criteria (what qualifies as this code)
- Exclusion criteria (what does not belong)
- Concrete example from the transcript

**Design notes:**
- Codes reflect both individual experiences (Stigma, Coping) and structural factors (Institutional Barriers, Food Access Resources)
- Codes allow for growth and change (Agency and Advocacy)
- Codes are designed to overlap intentionally—showing that real data is messy

### 3. **human_coded_excerpts.txt**
Three key passages with "ground truth" human coding and justification.

**Excerpts:**
1. **Complex Overlap** – The restaurant encounter (shame, coping, social support all present)
2. **Ambiguous Framing** – Food pantry discovery (can be coded multiple ways depending on theoretical frame)
3. **Debatable Interpretation** – Work-study trade-off (financial strain vs. academic impact as primary)

**Each excerpt includes:**
- The text (100–200 words)
- Primary and secondary codes
- Detailed justification explaining the coding choice
- Notes on why the passage is ambiguous or overlapping
- Discussion of how different research questions might yield different codes

**Design notes:**
- Ground truth is presented with reasoning, not as dogma
- Ambiguity is acknowledged, not hidden
- These excerpts prepare students for the interactive Gemini demo

### 4. **prompts.txt**
Exact prompts to paste into Gemini, designed for a 50-minute workshop session.

**Steps (in order):**
1. **Role-Set Prompt** (5 min) – Establish Gemini as a coding assistant
2. **Passage Extraction** (8 min) – Have Gemini identify all COPING STRATEGIES passages
3. **Classification** (10 min) – Code three straightforward passages
4. **Iterative Justification** (10 min) – Discuss a passage with overlapping codes; explore ambiguity
5. **Re-Coding from Different Frame** (8 min) – Code the same passage from a critical pedagogy perspective
6. **Bonus: Identify Ambiguity** (5 min, optional) – Have Gemini surface genuinely hard-to-code passages

**Design notes:**
- Prompts are ready to copy-paste—no preparation required
- Each step includes "EXPECTED OUTPUT" and "WORKSHOP FACILITATION NOTES"
- Prompts move from simple (straight extraction) to complex (theoretical re-framing)
- Ambiguity is introduced gradually, building to the key insight: coding is interpretation

---

## How to Run the Demo

### Before Class
1. Read through this README and the codebook to understand the codes
2. (Optional) Code one passage yourself to build familiarity
3. Have Gemini open (gemini.google.com) and these files available
4. Test the prompts once to ensure Gemini responds as expected

### During Class (50 minutes)
1. **Introduce the context** (5 min): Anchor paper, research question, why we code
2. **Walk through the codebook** (5 min): Quick overview of the 8 codes
3. **Step 1: Role-Set** (5 min): Paste the role-set prompt; let students see Gemini confirm it understands
4. **Step 2: Extract Passages** (8 min): Paste the COPING STRATEGIES prompt; ask: "Did we miss any? Would you code anything differently?"
5. **Step 3: Classify** (10 min): Paste three passages; celebrate agreement with codebook
6. **Step 4: Discuss Ambiguity** (10 min): Paste the complex passage; ask follow-up questions about where emphasis lies
7. **Step 5: Re-Code** (8 min): Code the same passage from a critical pedagogy perspective; discuss how theory changes analysis
8. **Wrap-up** (4 min): Key takeaway: coding is dialogical and interpretive, not mechanical

### After Class
- Ask students to code one new passage on their own
- Have them write a short reflection: "Where did you make a coding choice? What factors influenced it?"
- Optional follow-up: assign a "theoretical lens" and have them re-code their passage from that perspective

---

## Key Teaching Points

### 1. **AI as a Thinking Partner, Not an Authority**
Gemini is good at:
- Systematically extracting passages
- Organizing data
- Asking clarifying questions

Gemini is not good at:
- Understanding nuance without guidance
- Making decisions about what matters in your research
- Interpreting ambiguity without human direction

### 2. **Coding Is Interpretation**
- There is no "objective" code floating in the data
- Coding reflects your research question, theory, and priorities
- The same passage can be validly coded multiple ways
- Acknowledging this is scientific rigor, not weakness

### 3. **Ambiguity Is Information**
If a passage is hard to code, that's not a failure:
- It might mean your codebook needs refinement
- It might mean your research question needs sharpening
- It might reveal where themes overlap in meaningful ways

### 4. **Dialogical Coding Is Iterative**
- Ask follow-up questions ("Why did you choose that code?")
- Disagree with the AI
- Test alternative frames
- Refine your understanding as you go

---

## Discussing Results with Gemini

When Gemini codes a passage, ask:

- **"Do you agree with this coding? Why or why not?"**
- **"Could this passage be coded differently? How?"**
- **"What would change if we were focused on [different research question]?"**
- **"Where does this passage seem ambiguous to you?"**
- **"Which code do you think is primary, and why?"**

These questions model qualitative thinking: you're not accepting Gemini's coding as truth; you're using it as a starting point for reflection.

---

## Common Questions

### Q: Isn't this just getting AI to do my coding work for me?
**A:** No. Gemini extracts and organizes; you interpret. The AI helps you see patterns and test ideas, but you decide what matters. The demo explicitly shows how the same passage can be coded multiple ways—forcing students to engage in interpretation, not just categorization.

### Q: What if Gemini makes mistakes in coding?
**A:** That's perfect for teaching. If Gemini codes something you'd code differently, stop and ask why. Disagreement is a learning opportunity. It forces you to articulate your reasoning.

### Q: Can I use this codebook for my own research?
**A:** It's designed for this specific demo. Feel free to adapt it for your own work, but understand that every codebook should be tailored to your data and research question. This one is specifically for teaching how to code qualitatively.

### Q: What if I want to use a different theoretical frame?
**A:** The prompts include a re-coding example from critical pedagogy. You can adapt Step 5 to any theory: feminist, phenomenological, discourse analysis, etc. Different theories highlight different aspects of the data.

---

## Technical Notes

- **Transcript length:** ~2,000 words (fits comfortably in Gemini's context window)
- **Token estimate:** The full prompt + transcript should use ~3,000–4,000 tokens, well within limits
- **Gemini model:** Works with Gemini 1.5 and later; tested on Gemini 2.0
- **Time to run each step:** 30 seconds to 2 minutes depending on complexity
- **Reproducibility:** Results should be fairly consistent, though Gemini may phrase explanations differently each time

---

## Extensions and Adaptations

### For shorter sessions (30 min):
- Skip Step 5 (re-coding from different frame)
- Combine Steps 2 and 3
- Focus on discussing ambiguity in Step 4

### For longer sessions (90 min):
- Have students code passages in pairs before Step 3, then compare with Gemini
- Add Step 5 and then ask students to develop their own coding from a different frame
- Introduce a second, conflicting passage and discuss how to handle disagreement

### For writing-heavy classes:
- Have students write a brief memo: "How would you code this differently, and why?"
- Ask them to design their own codebook for a different research question
- Assign a reflection on how their coding choices reflect their theoretical assumptions

### For other research contexts:
- The structure works with any qualitative data: interviews, focus groups, open-ended surveys, ethnographic notes
- You can adapt the prompts to different domains (mental health, workplace dynamics, organizational change, etc.)
- The key insight (coding is interpretation) transfers to any qualitative analysis

---

## References and Further Reading

### On Qualitative Coding:
- Braun, V., & Clarke, V. (2019). *Reflecting on reflexive thematic analysis*. *Qualitative Research in Sport, Exercise and Health*, 11(4), 589–597.
- Saldaña, J. (2016). *The coding manual for qualitative researchers* (3rd ed.). SAGE.

### On Food Insecurity in Higher Education:
- Maroto, M. E., Snelling, A., & Linck, H. M. (2015). Navigating hidden hunger. *Journal of Contemporary Ethnography*, 45(5), 540–569.
- Goldrick-Rab, S., Broton, K., & Gates, C. (2013). Hungry and homeless in college. *Wisconsin HOPE Lab*.

### On AI and Qualitative Research:
- Gough, N. (2020). AI and qualitative research: Collaborating with artificial intelligence. *QSR NVivo*.
- Gusenbauer, M., & Haddaway, N. R. (2020). Which academic search systems are suitable for systematic reviews or meta-analyses? *Evaluating retrieval qualities of Google Scholar, PubMed, and 26 other resources*. *Research Synthesis Methods*, 11(2), 181–217.

---

## Attribution and Disclaimers

**Synthetic Data:** The interview transcript is a realistic synthetic composition created for teaching purposes. All identifying information has been removed or altered. This is not actual research data.

**Codebook Design:** The codebook draws inspiration from Maroto et al. (2015) but is adapted for this specific demo. It should not be used for actual research without validation and refinement.

**Demo Purpose:** This demo is designed to teach the mechanics and ethics of dialogical coding with AI. It is not intended to train students as food insecurity researchers; it is intended to teach qualitative method.

---

**Last updated:** February 2025  
**Created for:** D-Lab Workshop Series, Spring 2026  
**Module:** LLMs for Qualitative Work, Session 2

