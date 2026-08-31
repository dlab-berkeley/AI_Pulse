# Module 5: Simulating Participants (Gemini)

## Overview

This module demonstrates how to use LLMs to generate synthetic qualitative data by simulating research participants. Rather than recruiting human participants for a survey, you can prompt an LLM to adopt detailed personas and respond to open-ended questions as those personas would.

This approach offers:
- **Speed:** Generate diverse responses in minutes instead of weeks
- **Feasibility:** Pilot your survey questions without recruiting participants
- **Iteration:** Test question clarity and prompt refinement quickly
- **Exploration:** Generate diverse perspectives to inform study design

However, simulated data introduces important limitations and risks that must be carefully considered and disclosed.

## Anchor Papers

1. **Park et al. (2024)** — "Generative Agents: Interactive Simulacra of Human Behavior"
   Demonstrated generating behavior from 1,052 simulated agents. Showed LLMs can sustain consistent personas over multiple interactions.

2. **Stanford Human AI Research Institute (HAI)** — "Measuring Correlation Between LLM-Generated Data and Real-World Outcomes"
   Found 0.85 correlation between predictions from LLM-simulated survey responses and outcomes from 476 real randomized controlled trials. Suggests LLMs capture some real patterns but not all.

3. **Wang et al. (2025)** — "Silicon Samples: The Problem of Variance Compression in LLM-Generated Data"
   Demonstrated that LLM-generated data tends to have lower variance than real data and may overrepresent modal (average) responses. Real humans are more diverse, extreme, and contradictory than LLMs generate.

## Files

- **participant_profiles.txt** — Three detailed personas: Jordan (skeptical PhD student), Dr. Patricia Okafor (critical senior professor), and Sam (peer support advocate). Each includes demographics, background, values, mental health history, and ideals.

- **survey_questions.txt** — Five open-ended survey questions about campus mental health services, formatted as a real survey instrument. Questions explore access, barriers, university improvements, cultural identity, and ideal systems.

- **prompts.txt** — Five prompts for Gemini/Claude:
  - Prompts 1-3: Persona-specific prompts to generate responses for each participant
  - Prompt 4: Comparative analysis of the three sets of responses
  - Prompt 5: Critical reflection on simulation limitations and biases

- **README.md** — This file.

## Demo Instructions

### Step 1: Generate Individual Responses

1. Open [Google Gemini](https://gemini.google.com) or Claude
2. Copy **Prompt 1** from `prompts.txt` (the Jordan persona prompt)
3. Paste into the LLM and run
4. Copy the generated responses into a Google Doc or spreadsheet
5. Repeat for **Prompt 2** (Dr. Okafor) and **Prompt 3** (Sam)

**Expected output:** Three sets of open-ended responses, each about 1-2 paragraphs per survey question, written in each person's voice.

**Duration:** ~5 minutes per persona

### Step 2: Analyze Patterns and Divergences

1. Copy all three sets of responses into a comparison document (spreadsheet or shared doc)
2. Use **Prompt 4** (comparative analysis) to analyze patterns:
   - Where do the three personas agree?
   - Where do they diverge?
   - What does this tell us about different perspectives on campus mental health?
3. The LLM will generate insights about how different social positions lead to different experiences

**Expected output:** Structured analysis identifying patterns, divergences, and implications.

**Discussion point:** Do the differences reflect genuine structural positions (grad vs. faculty, worker vs. student, critical theorist vs. pragmatist) or are they artifacts of the LLM's training data?

### Step 3: Reflect on Limitations

1. After reviewing the three responses, run **Prompt 5** (critical reflection)
2. The LLM will meta-analyze its own simulation:
   - What limitations did it face?
   - Where might it have reinforced stereotypes?
   - What disclosures should accompany this data if used in research?

**Expected output:** Thoughtful reflection on validity, bias, and ethical implications.

**Discussion point:** This is the most important step. Simulated data can be useful for exploration and iteration, but publishing it as if it were real human data is misleading.

## Key Concepts

### Why Simulate Participants?

**Exploratory Research:**
- Test whether your survey questions are clear and generative
- Identify patterns you might want to look for in real data
- Pilot your theoretical framework

**Educational Purposes:**
- Demonstrate how different social positions lead to different experiences
- Show how identity shapes access to resources
- Illustrate qualitative analysis methods

**Not for Real Data:**
- Do not publish simulated responses as if they were human data
- Do not use simulated data in a study design if you could recruit real participants
- Do not ignore the limits of LLM-generated variation

### The Variance Compression Problem

Wang et al. (2025) documented a critical limitation: **LLM-generated data has lower variance than real human data.**

Why?
- LLMs are trained on aggregate patterns, so they default to modal (average) responses
- Humans are inconsistent, contradictory, extreme, and surprising
- Real people hold contradictory beliefs (e.g., "I think therapy is useless but also I need it")
- LLMs smooth over these contradictions

**Implication:** If you use simulated data to design interventions, you may miss edge cases, extreme needs, and contradictory perspectives that real people have. Real qualitative research remains essential.

### Stereotype Amplification

LLMs can inadvertently amplify stereotypes when generating personas:
- "Asian students are pragmatic and skeptical of therapy" ← stereotyped
- "Black professors are systemic critics" ← flattened
- "Queer people are trauma survivors" ← essentialized

The model may generate responses that are consistent with stereotypes rather than authentic human variation.

**Mitigation:**
- Provide rich, detailed personas (not caricatures)
- Run Prompt 5 to reflect critically on what the model generated
- Compare simulated responses to small samples of real data to calibrate
- Disclose the use of simulation explicitly

### Silicon Samples vs. Real Samples

Use this framework to decide when simulated data is appropriate:

| Use Case | Appropriate? | Why |
|----------|------------|-----|
| Piloting survey questions | YES | Quick iteration, low stakes |
| Demonstrating qualitative methods | YES | Educational value, no claims about real experiences |
| Designing interventions for real people | NO | May miss real variance and needs |
| Publishing as qualitative research | NO | Misrepresents data source |
| Generating training data for another model | MAYBE | Risks amplifying biases; use with caution |
| Supplementing real data with simulated voices | MAYBE | Only if clearly disclosed; not recommended |

## Discussion Points

1. **Accuracy:** Do these simulated responses feel authentic? Where do they ring true? Where do they fall flat? What would make them more realistic?

2. **Bias and Stereotypes:** Do the three personas reinforce stereotypes (e.g., "efficient Asian student," "critical Black professor," "traumatized queer person")? How could you make them more complex and less stereotyped?

3. **Variation:** Real survey respondents would likely include people who contradict these profiles (a skeptical Asian student who loves therapy, a Black professor who is apolitical, etc.). How would you generate more diverse and less predictable responses?

4. **Ethical Use:** If you were writing a paper and used simulated data, what would you need to disclose? Would it be okay to include it as supplementary material? Could you use it to inform your survey design without disclosing it?

5. **Practical Application:** For what research questions or stages of your project would simulation be most useful? Where would it be insufficient?

## Explore Further

- **Stanford Generative Agents:** Multi-agent simulation where agents remember past interactions and plan autonomously. More sophisticated than single-prompt simulation. See: https://arxiv.org/abs/2304.03442

- **Broska et al. (2024) — Prediction-Powered Inference:** Combine small amounts of ground-truth human data with large amounts of LLM predictions to make inferences while accounting for model bias. See: https://prediction-powered-inference.github.io/

- **Prompt Engineering for Personas:** Techniques for writing more detailed and consistent persona prompts. See: https://www.deeplearning.ai/short-courses/prompt-engineering-for-developers/

- **Validation Against Real Data:** Methods for comparing simulated and real data distributions to estimate where the simulation breaks down.

## Technical Requirements

- Google Gemini account (free, or paid for higher rate limits)
- Google Doc or spreadsheet (for comparing responses)
- No coding required for basic demo

## Citation and Disclosure

If you use this module or adapt it for your own research:

1. **Cite the anchor papers** that document simulation benefits and limitations.

2. **Disclose explicitly** if you used simulated data in any publication:
   - "To pilot our survey questions, we generated synthetic responses using the Gemini API, adopting detailed participant personas. These simulated responses should not be interpreted as data from real participants."

3. **Distinguish use cases:**
   - If exploratory: "Simulated responses informed our survey design"
   - If illustrative: "Personas are fictional and designed to illustrate different perspectives"
   - If methodological: "We acknowledge the limitations documented by Wang et al. (2025) regarding variance compression"

4. **Never represent simulated data as real human data.**

## Limitations and Risks

- **Variance compression:** Simulated data may underestimate real human diversity
- **Stereotype amplification:** Detailed personas can inadvertently flatten identities
- **Representativeness:** No guarantee that LLM-generated responses match real population distributions
- **Model drift:** Different model versions or training periods may generate different responses
- **Ethical concerns:** Using simulated data to inform real decisions affecting real people requires careful validation

## Further Resources

- Park et al. (2024): https://arxiv.org/abs/2304.03442 (Stanford Generative Agents)
- Wang et al. (2025): Silicon Samples paper (check arXiv or your institution's library)
- Stanford HAI reports on LLM correlation with RCTs: https://hai.stanford.edu/
- Prompt engineering best practices: https://platform.openai.com/docs/guides/prompt-engineering
