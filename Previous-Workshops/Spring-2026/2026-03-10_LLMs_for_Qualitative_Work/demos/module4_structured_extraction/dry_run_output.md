# Module 4: Structured Extraction from Text Data — Dry Run Output

**Fallback output for Gemini API demo (workshop date: 2026-02-25)**

---

## Extraction Prompt

> You are a qualitative research assistant analyzing campus food access barriers.
>
> For each response below, extract and structure the following information:
> - **Barrier Type**: Classify the primary barrier (Cost Barriers, Time and Schedule Barriers, Dietary and Cultural Barriers, Location and Access Barriers, Stigma and Awareness Barriers, Institutional Support Gaps)
> - **Socioecological Level**: Intrapersonal, Interpersonal, or Institutional
> - **Sentiment**: Positive/Neutral, Negative, or Mixed
> - **Resources Mentioned**: Any food access resources referenced (dining plan, food pantry, meal plan, resources, meal times, etc.) — list explicitly or "None"
> - **Key Entities**: Important mentions (jobs, commute, roles, medical conditions, etc.)
> - **Urgency**: Low, Medium, or High based on tone and constraint severity
>
> Format output as a structured table. Mark any response that is unclear, sarcastic, or off-topic in the Sentiment column.

---

## Structured Extraction Results

| Response ID | Barrier Type | Level | Sentiment | Resources Mentioned | Key Entities | Urgency |
|---|---|---|---|---|---|---|
| R1 | Cost Barriers | Intrapersonal | Negative | None | Ramen, PB sandwiches, affordability | High |
| R2 | Time and Schedule Barriers | Institutional | Negative | Dining hall, convenience store | Library work shift, late-night food access | High |
| R3 | Dietary and Cultural Barriers | Institutional | Negative | None | Kosher dietary needs, home cooking | Medium |
| R4 | Location and Access Barriers | Institutional | Mixed | Vending machines | Dwinelle building, late-night hours (11pm) | Low |
| R5 | Stigma and Awareness Barriers | Interpersonal | Negative | Food pantry | Junior year discovery, stigma awareness | High |
| R6 | Cost Barriers + Time and Schedule Barriers | Institutional | Negative | Meal costs, commute time | Oakland commute, meal skipping | High |
| R7 | Institutional Support Gaps | Institutional | Positive/Neutral | Meal plan, family care packages | Friend networks, resource awareness | Low |
| R8 | Dietary and Cultural Barriers | Interpersonal | Negative | Dining options (limited) | Halal dietary needs, worker attitude, hunger | High |
| R9 | Dietary and Cultural Barriers | Intrapersonal | Negative | Ingredient lists (unavailable) | Diabetes, medical condition, food safety | High |
| R10 | Time and Schedule Barriers | Intrapersonal | Negative | Meal times | Three jobs, exhaustion, schedule conflict | High |
| R11 | Stigma and Awareness Barriers | Interpersonal | Negative | Food resources, peer mentor support | Informal peer referral, cost concerns | Medium |
| R12 | Cost Barriers | Intrapersonal | Negative | Dining hall | Meal plan cost, affordability perception | Medium |
| R13 | Institutional Support Gaps | Institutional | Negative | Meal plan (undergrad only, unavailable) | Grad student status, policy exclusion | High |
| R14 | Stigma and Awareness Barriers | Intrapersonal | Negative | Food resources (underutilized) | Food-insecure background, help-seeking shame | High |
| R15 | Location and Access Barriers | Positive/Neutral | Positive/Neutral | Crossroads (late-night options) | Late-night dining, variety preference | Low |

---

## Summary Analysis

**Barrier Prevalence & Patterns:**
This dataset reveals cost and time-based barriers as the most prevalent issues, affecting 8 out of 15 respondents directly (Cost Barriers: R1, R6, R12; Time and Schedule: R2, R6, R10; Institutional Gaps: R7, R13). Notably, **stigma and awareness barriers** form a secondary cluster (R5, R11, R14) where students lack information about existing resources or feel shame accessing them—a key finding for institutional communication strategy. Dietary and cultural barriers (R3, R8, R9) reflect both institutional inflexibility and interpersonal dynamics (e.g., worker attitude in R8).

**Socioecological Distribution:**
Nearly half the responses (7/15) point to **institutional-level barriers** (inadequate hours, limited menu options, policy exclusions for grad students), suggesting systemic intervention potential. Interpersonal barriers (5/15) emerge around stigma, informal information sharing, and worker interactions, while intrapersonal factors (3/15) reflect medical conditions and individual financial constraints. This distribution indicates that addressing food access requires institutional policy changes, not just awareness campaigns.

**Urgency & Sentiment:**
High-urgency responses (10/15) cluster among cost, time, and medical constraint cases, many marked Negative sentiment. Importantly, R7 (Positive) and R15 (Positive/Neutral) provide satisfaction baselines—students with adequate resources or after-hours options report low urgency, suggesting infrastructure solutions exist and can be scaled. Only R4 was coded Mixed (sarcasm/venting about convenient gaps) and may require follow-up clarification.

**Actionable Insights:**
- **Cost**: Expand subsidized plans and pantry reach (addresses 8 cases)
- **Timing**: Extend hours and add late-night kiosks modeled on Crossroads success (R15)
- **Dietary Accommodation**: Audit menus for cultural/medical inclusion; improve ingredient transparency (R3, R8, R9)
- **Stigma & Awareness**: Formalize peer mentor referral (R11 model) and de-stigmatize pantry access (R5, R14)
- **Policy**: Extend dining privileges to grad students; clarify resource eligibility (R13)

---

## Notes for Instructor

This dry-run output was generated as a fallback demonstration. In the live workshop, you will:
1. Copy the 15 survey responses into Gemini (or use the clipboard feature)
2. Paste this extraction prompt
3. Request that Gemini format output as a markdown table
4. Optionally ask Gemini to provide the summary analysis

**Expected Live Differences:**
- Gemini may slightly reword barrier type labels or sentiment assessments
- The summary analysis order and emphasis may vary based on Gemini's synthesis
- Response formatting (capitalization, punctuation) may differ slightly

If Gemini fails during the workshop, display this file to show what structured extraction looks like. Then discuss the codebook choices and analysis implications with students.
