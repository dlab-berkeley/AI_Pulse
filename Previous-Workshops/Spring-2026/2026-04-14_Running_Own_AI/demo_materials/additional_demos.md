# Additional Demo Conversations: Running Your Own AI

These are bonus pre-run demos beyond the core 4 demos in `demo_conversations.md`.
Use them as options if time permits, if a core demo fails, or to deepen
discussion in a particular area.

---

## Demo Q: Quantization Live Demo (Ollama)

**Context given to students:** We've talked about quantization in the slides —
now let's see it in practice. We'll look at how much smaller a quantized model
is, how fast it runs, and whether the quality holds up for academic writing.

### Part 1: Model Sizes

```bash
# Pull the same model at different quantization levels
$ ollama pull llama3.2:3b
# (already pulled)

# Check how much disk space it uses
$ ls -lh ~/.ollama/models/blobs/ | grep sha256
-rw-------  1 user user  2.0G Mar 25 14:22 sha256-...  # 4-bit quantized (Q4_K_M)

# For comparison, the full-precision (FP16) version would be:
# 3B parameters × 2 bytes (FP16) = ~6 GB
# But we're running the 4-bit version = ~2 GB
# That's a 3x compression with minimal quality loss
```

**Instructor talking point:** "The model went from 6 GB to 2 GB — it fits
on a laptop with room to spare. A 7B model quantized to 4-bit is about
4 GB. Even a 13B model fits in 8 GB of RAM at 4-bit."

### Part 2: Speed Comparison

```bash
# Time a generation
$ time ollama run llama3.2:3b "Write one sentence about superconductivity." --verbose

# Output:
# Superconductivity is a quantum mechanical phenomenon in which certain
# materials exhibit zero electrical resistance below a critical temperature.
#
# total duration:       2.847s
# load duration:        0.012s
# prompt eval count:    14 tokens
# prompt eval duration: 0.285s
# eval count:           24 tokens
# eval duration:        2.543s
# eval rate:            9.43 tokens/s
```

**Instructor talking point:** "About 10 tokens per second on CPU — that's
readable but not fast. On a MacBook with Apple Silicon, you'd see 20-30
tokens/sec. On a GPU, 50-100+. For a writing assistant where you're
reading the output anyway, 10 tok/s is perfectly usable."

### Part 3: Quality Check — Does Quantization Hurt?

USER:

We quantized the model from 16-bit to 4-bit. Let's test if it can still
handle a technical prompt.

Write the first sentence of an abstract about Berry phase effects in
twisted bilayer graphene.

ASSISTANT (llama3.2:3b, 4-bit quantized):

The discovery of correlated insulating states and unconventional
superconductivity in magic-angle twisted bilayer graphene has motivated
intense theoretical investigation of the role of Berry phase and
non-trivial band topology in the flat bands formed by the moiré
superlattice potential.

**Instructor talking point:** "That's a perfectly serviceable opening
sentence. The 4-bit quantization didn't lose the physics knowledge — it
mainly affects the model's ability to handle very long, nuanced
reasoning chains. For paragraph-level writing tasks, 4-bit is fine."

### Part 4: The Quantization Spectrum (Slide Reference)

| Format | Bits per weight | 3B model size | 7B model size | Quality loss |
|--------|----------------|---------------|---------------|-------------|
| FP32   | 32             | ~12 GB        | ~28 GB        | None (reference) |
| FP16   | 16             | ~6 GB         | ~14 GB        | Negligible |
| Q8_0   | 8              | ~3 GB         | ~7 GB         | Very small |
| Q4_K_M | 4              | ~2 GB         | ~4 GB         | Small, acceptable |
| Q2_K   | 2              | ~1 GB         | ~2.5 GB       | Noticeable |

**Instructor talking point:** "Ollama defaults to Q4_K_M, which is the
sweet spot. You lose maybe 1-2% on benchmarks but save 75% of the
memory. Below 4-bit, you start seeing real degradation."

---

## Demo 5: System Prompts — Creating a Research Persona (Ollama)

**Context given to students:** Ollama lets you create custom models with
system prompts baked in. This is lighter than fine-tuning — you're giving
the model instructions, not changing its weights. Think of it as giving
a general-purpose assistant a detailed job description.

### Part 1: Creating a Custom Modelfile

```bash
# Create a Modelfile for a physics paper reviewer
$ cat > Modelfile.reviewer << 'EOF'
FROM llama3.2:3b

SYSTEM """You are a critical but constructive reviewer for Physical Review B.
You specialize in topological materials and strongly correlated electron systems.

When reviewing text:
- Flag any claims not supported by the methods described
- Check notation consistency (hat operators, bold vectors, etc.)
- Note if the writing is too informal for a physics journal
- Suggest specific improvements, not vague criticism
- Use the standards of PRB, not Nature or Science

When asked about conventions, draw on standard practices in the
cond-mat.str-el and cond-mat.mes-hall communities."""
EOF

# Create the model (instant — it just wraps the base model)
$ ollama create prb-reviewer -f Modelfile.reviewer
# transferring model data
# using llama3.2:3b as base
# setting system prompt
# success

# Now run it
$ ollama run prb-reviewer
```

### Part 2: Testing the Reviewer Persona

USER:

Review this paragraph from my draft:

"We computed the band structure using DFT and found that the system is a
topological insulator. The gap is pretty big, around 0.3 eV. We think this
could be useful for devices."

ASSISTANT (prb-reviewer):

Several issues need to be addressed before this paragraph is suitable for PRB:

1. **Missing methodological specifics.** "Using DFT" is insufficient. You need
   to specify: which exchange-correlation functional (PBE, HSE06?), the
   pseudopotential type (PAW, ultrasoft?), the code used (VASP, Quantum
   ESPRESSO?), and whether spin-orbit coupling was included (critical for a
   topological insulator claim). PRB requires reproducibility.

2. **Informal language.** "Pretty big" is not appropriate for a journal paper.
   Replace with: "a sizable topological gap of 0.3 eV" or "a topological gap
   of approximately 0.3 eV, comparable to room-temperature thermal energy."

3. **Unsupported topological classification.** Stating the system "is a
   topological insulator" requires you to report the topological invariant
   you computed (Z2 invariant, spin Chern number, etc.) and how you computed
   it (Wilson loop, parity analysis at TRIM points, etc.). Simply observing a
   gap in DFT does not establish topological character.

4. **Vague application claim.** "Could be useful for devices" is too vague for
   PRB. Either specify what kind of devices (spintronic, thermoelectric) and
   why your gap value matters for them, or omit the applications sentence and
   let the fundamental physics stand on its own.

5. **"We think" should be replaced.** In PRB papers, use "We propose," "Our
   results suggest," or "These findings indicate" instead of "We think."

### Part 3: A Second Persona — The Writing Coach

```bash
$ cat > Modelfile.coach << 'EOF'
FROM llama3.2:3b

SYSTEM """You are an academic writing coach specializing in STEM papers.
You help researchers improve their writing clarity and structure without
changing the technical content.

Your approach:
- Focus on sentence-level clarity and paragraph flow
- Identify passive voice overuse and suggest active alternatives
- Check that each paragraph has a clear topic sentence
- Ensure transitions between paragraphs are logical
- Keep feedback practical and specific: quote the sentence, then suggest a fix
- Do NOT comment on the science itself — only the writing."""
EOF

$ ollama create writing-coach -f Modelfile.coach
```

USER:

Help me improve this methods paragraph:

"The calculations were performed using the Vienna Ab initio Simulation
Package (VASP). The projector augmented wave method was used. A plane-wave
energy cutoff of 400 eV was employed. The Brillouin zone was sampled using
a 12×12×1 Gamma-centered k-mesh. Spin-orbit coupling was included."

ASSISTANT (writing-coach):

This paragraph is a common pattern in physics papers — a list of settings
disguised as prose. Every sentence follows the same "X was used/employed"
structure, creating a monotonous reading experience. Here's how to fix it:

**Problem 1: Repetitive passive constructions.** Five sentences in a row
use passive voice with nearly identical structure. This reads like a
bullet list with periods.

**Suggested revision:**

"We performed first-principles calculations within the projector augmented
wave (PAW) framework as implemented in the Vienna Ab initio Simulation
Package (VASP). The plane-wave basis was truncated at a kinetic energy
cutoff of 400 eV, and the Brillouin zone was sampled with a 12×12×1
Γ-centered k-mesh. Spin-orbit coupling was included throughout."

**What changed:**
- Merged the first two sentences to reduce repetition
- Used active voice for the first sentence ("We performed")
- Combined the cutoff and k-mesh into one sentence since they're related
  (both are convergence parameters)
- Kept the SOC sentence short and final — it's a separate physical
  ingredient, not a convergence parameter
- Three sentences instead of five, same information

### Instructor Notes

**Key pedagogical point:** System prompts are the "80/20 solution." They
don't change the model's weights, so the physics knowledge is the same as
the base model — but they dramatically change the *behavior*. For many
use cases (especially editing and review), a good system prompt is all
you need. Fine-tuning is for when you need the model to write *like* a
domain expert, not just *about* the domain.

**Timing:** 5-7 min for both personas. The reviewer persona is the more
impressive one; the writing coach is a practical "you can do this today"
takeaway.

---

## Demo 6: Local API Integration (Python + Ollama REST API)

**Context given to students:** Ollama isn't just a chatbot — it runs a
local API server. This means you can call it from Python scripts, Jupyter
notebooks, or any tool that speaks HTTP. No API keys, no cloud, no cost.

### Part 1: The Simplest API Call

```python
# ollama_api_demo.py — Batch-process abstracts with a local LLM

import requests
import json

def ask_ollama(prompt, model="llama3.2:3b"):
    """Send a prompt to the local Ollama server and get a response."""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
        }
    )
    return response.json()["response"]

# Test it
result = ask_ollama("What is the Berry phase? One sentence.")
print(result)
```

Output:
```
The Berry phase is a geometric phase acquired by a quantum system's wave
function when it is adiabatically transported around a closed loop in
parameter space.
```

### Part 2: Batch Processing — Check 5 Abstracts for Informal Language

```python
# Imagine you have a folder of draft abstracts to review
abstracts = [
    "We show that the system exhibits a pretty large gap of 0.5 eV...",
    "Our calculations demonstrate that spin-orbit coupling plays a crucial role...",
    "Basically, we found three distinct phases in the phase diagram...",
    "The results indicate a topological phase transition at critical strain...",
    "We think the Chern number changes from 1 to 0 at the transition...",
]

REVIEW_PROMPT = """You are a journal editor. Check this abstract sentence for
informality or vague language inappropriate for Physical Review B. If it's
fine, say "OK". If not, quote the problematic phrase and suggest a replacement.
Be concise (1-2 sentences max).

Sentence: {sentence}"""

print("Abstract Quality Check")
print("=" * 60)
for i, abstract in enumerate(abstracts, 1):
    result = ask_ollama(REVIEW_PROMPT.format(sentence=abstract))
    status = "✓" if "OK" in result[:10] else "✗"
    print(f"\n[{status}] Sentence {i}:")
    print(f"    Input:  {abstract[:70]}...")
    print(f"    Review: {result.strip()}")
```

Output:
```
Abstract Quality Check
============================================================

[✗] Sentence 1:
    Input:  We show that the system exhibits a pretty large gap of 0.5 eV...
    Review: "Pretty large" is informal. Replace with "sizable" or
            "substantial": "...exhibits a substantial gap of 0.5 eV."

[✓] Sentence 2:
    Input:  Our calculations demonstrate that spin-orbit coupling plays a cru...
    Review: OK. This follows standard PRB conventions.

[✗] Sentence 3:
    Input:  Basically, we found three distinct phases in the phase diagram...
    Review: "Basically" is conversational filler — remove it entirely.
            "We identify three distinct phases" is stronger than "we found."

[✓] Sentence 4:
    Input:  The results indicate a topological phase transition at critical s...
    Review: OK. Clear and appropriately formal.

[✗] Sentence 5:
    Input:  We think the Chern number changes from 1 to 0 at the transition...
    Review: "We think" is too tentative for a results statement. Use "We find"
            or "Our calculations show" instead.
```

### Part 3: Integration with Existing Workflows

```python
# You can also use the official ollama Python package
# pip install ollama

import ollama

# Chat-style API (maintains conversation context)
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {"role": "system", "content": "You are a condensed matter physics writing assistant."},
        {"role": "user", "content": "Is 'Hamiltonian' capitalized in physics papers?"},
    ]
)
print(response["message"]["content"])
```

Output:
```
Yes, "Hamiltonian" is capitalized in physics papers because it is a proper
noun — it derives from the name of William Rowan Hamilton. This is
consistent across condensed matter, high-energy physics, and mathematical
physics literature. Similarly, "Lagrangian" (from Lagrange), "Hermitian"
(from Hermite), and "Dirac" (as in Dirac fermion) are always capitalized.
```

### Instructor Notes

**Key pedagogical point:** The local API is what makes local LLMs practical
for research workflows. You're not limited to chatting — you can build tools:
batch abstract checkers, reference formatters, notation validators, or even
pipelines that process an entire paper section by section.

**Timing:** 5 min. Show Part 1 live if Ollama is running; show Parts 2-3
from pre-run output if time is short.

---

## Demo 7: Model Comparison — Same Task, Different 3B Models

**Context given to students:** There are many open-source models in the
3B parameter range. How do you choose? Let's compare three models on the
same physics writing task and see how they differ.

### Setup

```bash
# Pull three different 3B-class models
$ ollama pull llama3.2:3b       # Meta's Llama 3.2 (3B)
$ ollama pull qwen2.5:3b        # Alibaba's Qwen 2.5 (3B)
$ ollama pull phi3:3.8b          # Microsoft's Phi-3 Mini (3.8B)
```

### The Prompt (identical for all three)

Write the opening paragraph (3-4 sentences) for a condensed matter theory
paper about frustrated magnetism on the kagome lattice. The paper uses
exact diagonalization and DMRG to study the spin-1/2 Heisenberg model.
Use a formal academic tone appropriate for Physical Review B.

### Llama 3.2 (3B) Response

The spin-1/2 Heisenberg antiferromagnet on the kagome lattice has long
served as a paradigmatic model for geometrically frustrated magnetism,
hosting an extensive ground-state degeneracy that has resisted definitive
characterization for decades. Despite intensive theoretical and
experimental efforts, the nature of the ground state — whether it realizes
a quantum spin liquid, a valence-bond crystal, or some other exotic phase
— remains the subject of active debate. In this work, we employ a
combination of exact diagonalization on clusters of up to N=36 sites and
density-matrix renormalization group (DMRG) calculations on cylindrical
geometries to revisit this question with improved numerical precision.

### Qwen 2.5 (3B) Response

Geometrically frustrated quantum magnets represent a frontier of condensed
matter physics, with the kagome lattice Heisenberg antiferromagnet
occupying a central position as the most intensively studied frustrated
spin system. The ground state of the spin-1/2 nearest-neighbor model on
this lattice continues to elude consensus, with competing proposals
ranging from gapped Z2 spin liquids to gapless U(1) Dirac spin liquids
and various symmetry-broken states. Here we present a comprehensive
numerical study combining exact diagonalization (ED) and the density
matrix renormalization group (DMRG) to systematically investigate the
phase diagram and its sensitivity to next-nearest-neighbor exchange
interactions.

### Phi-3 Mini (3.8B) Response

The kagome lattice is a geometrically frustrated magnetic structure that
has attracted significant attention due to its potential to host novel
quantum phases of matter. The nearest-neighbor Heisenberg model on this
lattice is particularly interesting because the triangular arrangement of
spins leads to competing interactions that prevent conventional magnetic
ordering. We study this model using two complementary numerical methods:
exact diagonalization, which provides exact results for small clusters,
and the density matrix renormalization group (DMRG), which can handle
larger systems. Our goal is to clarify the nature of the ground state and
determine whether a spin liquid phase is realized.

### Side-by-Side Analysis

| Feature | Llama 3.2 | Qwen 2.5 | Phi-3 Mini |
|---------|-----------|----------|------------|
| Tone | Formal, strong | Very formal, dense | Slightly pedagogical |
| Specificity | Good (N=36 sites) | Very good (Z2, U(1) liquids) | Moderate |
| Structure | Classic intro pattern | Literature-heavy opening | Definition-first |
| Jargon level | Standard PRB | Advanced (assumes reader knows the field) | Accessible |
| Best for | General physics writing | Specialist cond-mat | Cross-disciplinary papers |

### Instructor Notes

**Key pedagogical point:** Different models have different "personalities"
even at the same parameter count. Qwen tends to be more technically
detailed; Phi-3 is more explanatory; Llama strikes a middle ground. The
right choice depends on your audience and use case. Try 2-3 models before
committing to one for your workflow.

**Timing:** 5 min. Show outputs side by side on screen. Ask students which
they'd prefer for their own subfield.

---

## Demo 8: Privacy-Sensitive Qualitative Coding (Local LLMs for IRB Data)

**Context given to students:** A major advantage of running models locally
is that no data leaves your machine. This matters enormously for
research involving human subjects — interview transcripts, survey
responses, medical records. Let's see how a local LLM can assist with
qualitative coding while keeping your IRB compliance intact.

### Scenario

You're a social scientist who conducted interviews about graduate student
experiences with AI tools. Your IRB protocol says data cannot be uploaded
to third-party services. Here's an anonymized transcript excerpt:

### The Data (saved locally as `interview_excerpt.txt`)

```
INTERVIEWER: Can you tell me about a time you used an AI tool for your
research?

PARTICIPANT 7: Yeah, so last semester I was working on my qualifying exam
paper and I was really struggling with the literature review. There's just
so much out there on [topic redacted]. I tried using ChatGPT to help me
organize the papers I'd already read, like "here are my 30 papers, help me
group them by theme." And it actually did a decent job at first, but then
I noticed it was making up citations. Like, it would say "as shown by
Smith et al. (2019)" and that paper didn't exist. After that I didn't
trust it for anything bibliography-related.

INTERVIEWER: How did that change your approach?

PARTICIPANT 7: I still use it, but differently. Now I only use it for
things where I can verify the output immediately. Like, I'll paste a
paragraph I wrote and ask "is this argument logically coherent" or "what
am I missing." But I won't ask it to find papers or state facts anymore.
I guess I learned that it's better as a thinking partner than an
information source.
```

### Conversation

USER:

I'm doing qualitative coding on interview transcripts about graduate
student AI use. This is IRB-protected data — I cannot upload it to any
cloud service. I'm using you (running locally via Ollama) to help with
initial coding.

Here's an excerpt. Please suggest relevant codes from a grounded theory
perspective. For each code, quote the specific text that supports it.

[paste of transcript above]

ASSISTANT (llama3.2:3b, running locally):

Here are suggested codes with supporting evidence:

**1. Trust calibration through experience**
"After that I didn't trust it for anything bibliography-related"
→ The participant's trust in AI tools shifted after a negative experience,
leading to a more nuanced understanding of the tool's capabilities.

**2. Hallucination awareness**
"it was making up citations... 'as shown by Smith et al. (2019)' and that
paper didn't exist"
→ Direct experience with AI confabulation as a turning point in the
participant's relationship with the tool.

**3. Task-specific trust boundaries**
"I still use it, but differently. Now I only use it for things where I
can verify the output immediately"
→ The participant developed a personal framework for appropriate vs.
inappropriate AI use cases, centered on verifiability.

**4. AI as thinking partner vs. information source**
"it's better as a thinking partner than an information source"
→ This is a rich in-vivo code — the participant's own language captures
a distinction that may be analytically productive across your dataset.

**5. Verification-dependent adoption**
"I'll paste a paragraph I wrote and ask 'is this argument logically
coherent'"
→ Continued use is conditional on the ability to immediately verify
outputs — a pattern of "trust but verify."

**Suggested axial coding connections:**
- Codes 1, 3, and 5 may connect through a category like "Adaptive trust
  management" — the process by which users calibrate their reliance on
  AI tools through experience.
- Code 4 is potentially a core category if other participants express
  similar distinctions.

### Follow-up

USER:

Good. Now compare this participant's response to the codes we've
already established from earlier interviews. Our existing codebook has:

- INITIAL_ENTHUSIASM: Positive first experience with AI tools
- DISILLUSIONMENT: Negative experience leading to reduced use
- STRATEGIC_USE: Deliberate, bounded deployment of AI

Does Participant 7 fit these existing codes, or do we need new ones?

ASSISTANT:

Participant 7 partially fits the existing codes but suggests the codebook
needs refinement:

**INITIAL_ENTHUSIASM** — Partial fit. P7 says "it actually did a decent
job at first," indicating initial positive experience, but the enthusiasm
is more measured than what this code typically captures.

**DISILLUSIONMENT** — Poor fit. P7 did not reduce use — they *redirected*
it. "I still use it, but differently" is explicitly not disillusionment.
Your current code implies reduced use, but P7's trajectory is adaptation,
not withdrawal.

**STRATEGIC_USE** — Good fit. "I only use it for things where I can
verify the output immediately" is a clear instance of bounded deployment.

**Suggested new code:**
- **ADAPTIVE_RECALIBRATION**: The process of shifting AI use patterns
  after a negative experience *without abandoning the tool*. This is
  distinct from DISILLUSIONMENT (which implies reduced use) and
  STRATEGIC_USE (which doesn't require a precipitating negative
  experience). P7's trajectory is: enthusiasm → hallucination encounter
  → recalibration → continued but modified use.

This new code may apply to other participants who had negative experiences
but continued using AI tools in different ways.

### Instructor Notes

**Key pedagogical point:** This is the single most compelling use case
for local LLMs in the social sciences. The model never sees the data
unless it's running on your machine. No API calls, no logging, no
third-party data processing agreements needed. For IRB-protected data,
this is the difference between "I can use AI to help" and "I can't touch
AI at all."

**Secondary point:** The model is surprisingly good at qualitative coding
tasks — identifying themes, suggesting codes, comparing against existing
codebooks. It's not replacing the researcher's judgment, but it's a
useful first pass that can speed up the most tedious part of qualitative
analysis.

**Timing:** 7 min. This demo tends to generate the most discussion,
especially from social science and public health students. Budget extra
time for Q&A.

---

## Demo 9: Temperature and Sampling — How Randomness Affects Output

**Context given to students:** When you generate text with an LLM, the
"temperature" parameter controls how creative vs. deterministic the output
is. This matters for academic writing — you usually want consistency, not
creativity. Let's see the difference.

### Setup

We ask the same model the same prompt at three different temperatures.

### Prompt (identical each time)

Write one sentence describing the ground state of the spin-1/2 kagome
Heisenberg antiferromagnet.

### Temperature 0.0 (Deterministic)

```bash
$ ollama run llama3.2:3b --temperature 0.0 "Write one sentence describing
the ground state of the spin-1/2 kagome Heisenberg antiferromagnet."
```

**Run 1:**
The ground state of the spin-1/2 kagome Heisenberg antiferromagnet is
believed to be a quantum spin liquid, characterized by long-range quantum
entanglement and the absence of conventional magnetic order.

**Run 2 (identical prompt, same temperature):**
The ground state of the spin-1/2 kagome Heisenberg antiferromagnet is
believed to be a quantum spin liquid, characterized by long-range quantum
entanglement and the absence of conventional magnetic order.

→ *Identical outputs.* At temperature 0, the model always picks the most
probable next token. This is deterministic and reproducible.

### Temperature 0.7 (Default — Balanced)

```bash
$ ollama run llama3.2:3b --temperature 0.7 "Write one sentence..."
```

**Run 1:**
The nature of the ground state of the spin-1/2 Heisenberg antiferromagnet
on the kagome lattice remains one of the most debated questions in
frustrated magnetism, with strong numerical evidence pointing toward a
gapped Z2 spin liquid phase.

**Run 2:**
The spin-1/2 kagome Heisenberg antiferromagnet is widely believed to
realize a quantum spin liquid ground state, though whether the spin liquid
is gapped or gapless continues to be debated.

→ *Different but both good.* Temperature 0.7 gives variety while staying
on-topic. Good for brainstorming multiple phrasings.

### Temperature 1.5 (High — Creative/Unpredictable)

```bash
$ ollama run llama3.2:3b --temperature 1.5 "Write one sentence..."
```

**Run 1:**
Interestingly, unlike typical Néel-ordered systems the kagome
antiferromagnet's enigmatic ground manifold resists simple symmetry-broken
characterization, instead weaving together resonating valence bond
fluctuations into what various groups have termed a topological
spin-liquid — a deeply entangled quantum soup.

**Run 2:**
The spin-half kagomé Heisenberg problem continues to frustrate (pun
perhaps intended by nature) theorists who've thrown DMRG, variational
Monte Carlo, and even tensor networks at it without reaching full consensus.

→ *Unpredictable and sometimes inappropriate.* "Quantum soup" and jokes
about frustration are not PRB-appropriate. High temperature introduces
randomness that can produce creative metaphors but also nonsense.

### Summary Table

| Temperature | Reproducible? | Tone | Best for |
|------------|--------------|------|----------|
| 0.0 | Yes (deterministic) | Conservative, safe | Final drafts, consistency checks |
| 0.3 | Mostly | Formal, slight variety | Polishing, minor rephrasing |
| 0.7 | No | Balanced, natural | First drafts, brainstorming options |
| 1.0 | No | More varied, occasional tangents | Creative writing, exploring ideas |
| 1.5+ | No | Unpredictable, sometimes weird | Not recommended for academic work |

### Instructor Notes

**Key pedagogical point:** For academic writing, you almost always want
temperature 0.0-0.7. Higher temperatures are for brainstorming, not for
final output. This is one of the most practical takeaways — students can
immediately apply this to get more consistent results from any LLM.

**Practical tip for students:** "If you're asking the model to check your
notation or review your logic, use temperature 0. If you're asking it to
suggest 5 different opening sentences, use temperature 0.7. Never use
temperature above 1.0 for anything going into a paper."

**Timing:** 4 min. The contrast between temperature 0 (identical outputs)
and temperature 1.5 ("quantum soup") is funny and memorable.

---

## Updated Instructor Notes for All Demos

### Full Demo Menu (pick based on time and audience)

| Demo | Time | Topic | Best for |
|------|------|-------|----------|
| Demo 1: Ping-Pong | 5 min | Iterative prompting workflow | Everyone |
| Demo 2: Full Paper | 7 min | Context window + privacy | Physics/STEM students |
| Demo 3a: Base vs FT | 5 min | Fine-tuning impact | Everyone |
| Demo 3b: Field Questions | 4 min | Domain knowledge | Physics students |
| Demo 4: HuggingFace | 4 min | Sharing & collaboration | Everyone |
| Demo Q: Quantization | 5 min | Size/speed/quality | Technical audience |
| Demo 5: System Prompts | 6 min | Custom personas | Everyone |
| Demo 6: Local API | 5 min | Python integration | Coders |
| Demo 7: Model Comparison | 5 min | Choosing a model | Everyone |
| Demo 8: Privacy/Qual | 7 min | IRB-safe qualitative coding | Social scientists |
| Demo 9: Temperature | 4 min | Sampling parameters | Everyone |

### Recommended Sets by Audience

**Mixed D-Lab audience (50 min total):**
Core: Demos 1, 2, 3a, 3b, 4 (25 min demos + 25 min discussion)

**Physics-heavy audience:**
Core + Demo Q + Demo 7 (swap Demo 8 for Demo Q)

**Social science audience:**
Core + Demo 8 + Demo 5 (swap Demo 3b for Demo 8, add Demo 5)

**Technical/CS audience:**
Core + Demo 6 + Demo 9 (swap Demo 2 for Demo 6)
