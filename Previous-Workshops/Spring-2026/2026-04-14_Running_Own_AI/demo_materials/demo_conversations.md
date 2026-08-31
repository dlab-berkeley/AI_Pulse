# Demo Conversations: Running Your Own AI for Academic Writing

These are pre-run conversations used during the live workshop demos. Each
demo is shown as a pasted transcript so we don't depend on live inference.

---

## Demo 1: Ping-Pong Writing (Ollama + Llama 3)

**Context given to students:** We're drafting a paragraph for the
introduction of our condensed matter paper. Instead of asking the model to
write the whole thing, we work iteratively: bullet points, then openings,
then refinement. This keeps us in the driver's seat.

### Round 1: Bullet Points to Opening Sentences

USER:

I'm writing the introduction to a condensed matter physics paper about
topological phase transitions in monolayer jacutingaite (Pt2HgSe3). I
need a paragraph that covers these points:

- Kane-Mele model predicts QSH effect on honeycomb lattice
- Graphene's SOC too small to observe it
- Jacutingaite has large SOC from heavy atoms (Pt, Hg)
- Recent exfoliation experiments make this timely

Give me 5 different opening sentences for this paragraph. Just the
opening sentence, nothing else.

ASSISTANT:

Here are five options:

1. "The Kane-Mele model, which predicts the quantum spin Hall effect on
the honeycomb lattice, has motivated an extensive search for materials
with sufficiently large spin-orbit coupling to realize this topological
phase."

2. "Since its proposal in 2005, the Kane-Mele model has served as the
paradigmatic framework for understanding topological insulating behavior
on the honeycomb lattice."

3. "The experimental observation of the quantum spin Hall effect in
honeycomb materials has remained elusive due to the vanishingly small
spin-orbit coupling in graphene."

4. "A central challenge in topological quantum materials research has
been identifying honeycomb systems where the Kane-Mele mechanism produces
a measurably large topological gap."

5. "Monolayer jacutingaite (Pt2HgSe3) has recently emerged as a
compelling candidate for realizing the quantum spin Hall effect predicted
by the Kane-Mele model."

### Round 2: Pick and Modify

USER:

I like #4 best, but it's a bit too broad. I want it to immediately
signal that this paper is about jacutingaite, not a general review. Can
you keep the "central challenge" framing but bring in the material
earlier? Also, #5 was too abrupt — it jumped straight to the material
without motivation.

ASSISTANT:

How about these revised versions:

A) "A central challenge in realizing the Kane-Mele quantum spin Hall
effect has been the vanishingly small spin-orbit coupling in graphene, a
limitation that monolayer jacutingaite (Pt2HgSe3), with its heavy
Pt and Hg atoms, may overcome."

B) "Identifying honeycomb materials where the Kane-Mele mechanism
produces an observable topological gap has remained a central challenge
— one that monolayer jacutingaite (Pt2HgSe3) is uniquely positioned
to address."

C) "The Kane-Mele quantum spin Hall effect requires substantial
spin-orbit coupling on a honeycomb lattice, a condition that has proven
difficult to satisfy in practice until the recent identification of
monolayer jacutingaite (Pt2HgSe3) as a candidate topological insulator."

Option A keeps your "central challenge" framing and introduces
jacutingaite as the solution in the same sentence. Option B is more
compact. Option C has a slightly different structure that emphasizes the
requirement-solution relationship.

### Round 3: Full Paragraph

USER:

Go with version A. Now write the full paragraph using that opening.
Cover all four bullet points I gave you. Keep it to about 5 sentences,
formal physics style.

ASSISTANT:

A central challenge in realizing the Kane-Mele quantum spin Hall effect
has been the vanishingly small spin-orbit coupling in graphene, a
limitation that monolayer jacutingaite (Pt2HgSe3), with its heavy Pt and
Hg atoms, may overcome. The Kane-Mele model predicts that intrinsic
spin-orbit coupling on a honeycomb lattice opens a topological gap at the
Dirac points, giving rise to helical edge states protected by
time-reversal symmetry. However, in graphene the intrinsic spin-orbit
coupling is of order 1 microeV, rendering the quantum spin Hall effect
unobservable at any accessible temperature. Monolayer jacutingaite, in
which Hg atoms occupy the honeycomb sites and experience strong spin-orbit
interactions mediated by neighboring Pt atoms, has been predicted to host
a topological gap exceeding 0.15 eV — more than five orders of magnitude
larger than that of graphene. The recent successful exfoliation of
jacutingaite crystals to the monolayer limit brings the experimental
verification of these predictions within reach and motivates a detailed
theoretical investigation of the phase diagram under realistic
perturbations.

---

## Demo 2: Full Paper in Context (Ollama + Llama 3, 8K context)

**Context given to students:** Now we load the whole draft paper into the
model's context window. This is where running locally matters — you might
not want to upload an unpublished manuscript to a cloud API. We'll ask
the model to play the role of a critical reader.

*[In the live demo, the instructor pastes the full contents of
`sample_paper.txt` into the prompt. It is not reproduced here.]*

### Conversation

USER:

I've pasted my draft paper above. I'd like you to help me review it
before submission. Let's start with the big picture.

Summarize the main argument of this paper in 2 sentences.

ASSISTANT:

The paper maps out the topological phase diagram of monolayer jacutingaite
(Pt2HgSe3) using an extended Kane-Mele model parameterized by
first-principles DFT calculations, identifying how biaxial strain and
Rashba spin-orbit coupling control the transition between a quantum spin
Hall insulator and a trivial band insulator. The central finding is that
the phase boundary traces a funnel-shaped curve in the strain-Rashba
parameter space, with the QSH phase surviving up to moderate Rashba
coupling strengths (~0.06 eV) and closing at a critical strain of ~5.2%,
values that are within experimental reach.

USER:

Good. Now check: is the notation consistent throughout the paper?

ASSISTANT:

I found one notation inconsistency. In Section 2 (Model and Methods),
the full Hamiltonian is introduced with the notation "$\hat{H}$"
(H-hat), using the hat operator notation:

  "$\hat{H}$ = H_0 + H_SOC + H_R + H_Delta"

However, in the final paragraph of Section 4 (Discussion and Conclusion),
the Hamiltonian is referred to using a different notation,
"$\mathcal{H}$" (calligraphic H):

  "The $\mathcal{H}$ exhibits rich phase behavior..."

These should be made consistent. Since $\hat{H}$ (operator hat notation)
is more standard for the Hamiltonian in condensed matter physics, I'd
recommend using $\hat{H}$ throughout and changing the instance in the
conclusion.

I should also note that the individual terms (H_0, H_SOC, H_R, H_Delta)
are written without the hat, which is fine as long as it's intentional —
some authors put hats on all operators, others only on the full
Hamiltonian. But the $\hat{H}$ vs $\mathcal{H}$ discrepancy should
definitely be fixed.

USER:

Good catch. Next: does the conclusion follow logically from the results?
Are there any claims in the conclusion that aren't supported by what's
in the Results section?

ASSISTANT:

Yes, I found two issues:

**1. Optical conductivity claim (unsupported).** The conclusion states:

  "An important implication of our work is the prediction that the optical
  conductivity should exhibit a characteristic step-like feature at the
  topological transition, arising from the van Hove singularity associated
  with the gap closure."

However, the Results section (Section 3) does not present any optical
conductivity calculations. There is no mention of optical response, the
joint density of states, or van Hove singularities anywhere in the
results. This claim appears to come out of nowhere. You should either:
- Add optical conductivity calculations to the Results section, or
- Soften the language to frame it as a prediction or future direction
  rather than an "implication of our work," or
- Remove it.

**2. Disorder analysis (weakly supported).** The conclusion also
discusses:

  "our analysis of the disorder-averaged topological invariant
  demonstrates that the QSH phase remains stable against Anderson
  disorder up to a critical disorder strength of W_c = 0.8 eV"

This result is also not presented in Section 3. There are no figures,
tables, or detailed discussion of disorder calculations in the Results.
The specific value W_c = 0.8 eV is stated as a quantitative result but
has no supporting analysis.

The claims about strain and Rashba coupling effects are well supported
by the Results section. It's the optical conductivity and disorder claims
that need either supporting results or reframing.

USER:

Last thing: find any sentences in the paper that are too informal for a
physics journal.

ASSISTANT:

I found one sentence that stands out. In the abstract, the final
sentence reads:

  "These findings suggest that monolayer jacutingaite offers a robust and
  experimentally tunable platform for studying topological phase
  transitions, which makes it a pretty interesting system for potential
  spintronic applications."

The phrase "a pretty interesting system" is too informal for a journal
paper. In a Physical Review or Nature Physics manuscript, you'd want
something like:

- "...establishing it as a promising candidate for spintronic
  applications."
- "...highlighting its potential for spintronic device applications."
- "...making it an attractive platform for spintronic applications."

The rest of the paper maintains an appropriate academic tone. The
abstract sentence is the only place where the register slips. It reads
like something from a talk or a first draft where the author was
thinking out loud.

---

## Demo 3a: Base Model vs Fine-Tuned Model (Side by Side)

**Context given to students:** We're comparing two models running locally
in Ollama: a general-purpose base model (Qwen2.5 3B) and the same model
after QLoRA fine-tuning on ~2,000 condensed matter abstracts from arXiv. Same
prompt, same hardware, very different outputs.

### Prompt (given to both models)

Write an abstract for a paper about spin-orbit coupling effects on the
topological phase diagram of a Kane-Mele model with next-nearest-neighbor
interactions.

### Base Model Response (Qwen2.5-3B-Instruct, unmodified)

ASSISTANT (base model):

In this paper, we study the effects of spin-orbit coupling on the
topological phase diagram of the Kane-Mele model. The Kane-Mele model is
an important model in condensed matter physics that describes the behavior
of electrons on a honeycomb lattice. We add next-nearest-neighbor
interactions to the standard model and investigate how spin-orbit coupling
changes the different phases. Using numerical calculations, we compute the
phase diagram as a function of the spin-orbit coupling strength and the
next-nearest-neighbor hopping parameter. We find that spin-orbit coupling
can induce transitions between different topological phases, including
topologically trivial and non-trivial phases. Our results show that the
next-nearest-neighbor interactions have a significant impact on the phase
boundaries and can either stabilize or destabilize the topological phases
depending on their strength. These findings contribute to our
understanding of topological materials and could have implications for the
design of new electronic devices.

### Fine-Tuned Model Response (Qwen2.5-3B-Instruct + cond-mat QLoRA)

ASSISTANT (fine-tuned):

We investigate the topological phase diagram of the Kane-Mele model on
the honeycomb lattice in the presence of intrinsic spin-orbit coupling
(SOC), Rashba SOC, and next-nearest-neighbor (NNN) hopping interactions.
By computing the Z2 invariant and spin Chern number across the
multi-dimensional parameter space, we identify several competing phases:
a quantum spin Hall (QSH) insulator, a trivial band insulator, and a
Chern insulator phase that emerges at finite NNN coupling. We show that
NNN interactions break particle-hole symmetry and introduce an asymmetry
between the K and K' valleys, shifting the topological phase boundaries
in a manner that depends sensitively on the sign of the NNN hopping
integral t'. For t' > 0, the QSH phase is stabilized against Rashba
perturbations, whereas for t' < 0, a direct transition to the Chern
insulator phase preempts the Rashba-driven gap closure. We construct the
full phase diagram in the (lambda_SOC, lambda_R, t') parameter space
and derive analytical expressions for the phase boundaries in limiting
cases. Our results demonstrate that NNN interactions constitute a
relevant perturbation to the Kane-Mele model that qualitatively modifies
the topological phase structure and may be important for the
interpretation of experiments on candidate QSH materials with non-
negligible longer-range hopping.

### Instructor Notes (shown on slide, not read aloud)

Key differences to point out:
- The base model says "topologically trivial and non-trivial" -- the
  fine-tuned model uses the field-standard terms (QSH insulator, Chern
  insulator, Z2 invariant, spin Chern number)
- The base model's last sentence is a generic "implications for devices"
  conclusion; the fine-tuned model connects to specific experimental
  concerns
- The fine-tuned model follows abstract conventions: no citations, states
  the method early, gives specific parameter names, ends with broader
  significance
- The base model reads like a student summary; the fine-tuned model reads
  like an arXiv posting

---

## Demo 3b: Field-Specific Questions (Fine-Tuned Model)

**Context given to students:** Beyond writing, a fine-tuned model can
answer field-specific style and convention questions that a general model
handles poorly. Let's try a few.

### Question 1: Word choice conventions

USER:

In condensed matter physics papers, is "we demonstrate" or "we show" more
commonly used in abstracts? Does it matter?

ASSISTANT (fine-tuned):

Both are common, but they tend to be used in slightly different contexts
in cond-mat abstracts:

- "We show" is more frequent overall and is the safer default. It's used
  for both analytical and numerical results: "We show that the gap closes
  at a critical strain of 5%."

- "We demonstrate" is typically reserved for cases where the result is
  more surprising or where you're establishing something for the first
  time: "We demonstrate the existence of a previously unidentified Chern
  insulator phase." It carries a slightly stronger connotation of proof
  or novelty.

- "We find" is used for results that emerged from the calculation rather
  than being the stated goal: "We find that the phase boundary is
  insensitive to disorder."

- "We predict" is used when the result hasn't been experimentally
  verified: "We predict a topological transition at 4% strain."

In practice, many abstracts use "show" and "find" multiple times and
"demonstrate" once or not at all. Using "demonstrate" for every result
would read as slightly over-claiming.

### Question 2: Notation standards

USER:

What's the standard notation for the Berry phase in condensed matter
papers? I've seen gamma, phi, and Phi_B used in different references.

ASSISTANT (fine-tuned):

The most common notations in the condensed matter literature are:

- gamma (lowercase Greek gamma) — This is the most standard for the
  geometric/Berry phase itself, following Berry's original paper. You'll
  see gamma_n for band n, or just gamma for the total Berry phase.

- gamma = oint A(k) . dk — where A(k) is the Berry connection (also
  called the Berry potential). The Berry connection is almost universally
  written as A or A_n(k).

- Phi_B is less common for the Berry phase itself; it's more often used
  for the magnetic flux in Aharonov-Bohm contexts, which can cause
  confusion. I'd avoid it unless you're specifically discussing the
  Aharonov-Bohm effect.

- The Berry curvature is almost always Omega or Omega_n(k) = nabla_k x
  A_n(k).

For your jacutingaite paper, I'd recommend gamma for the Berry phase,
A_n(k) for the connection, and Omega_n(k) for the curvature. This is the
most widely recognized convention in the topological insulator literature
and consistent with the notation used in review articles like Hasan and
Kane (2010).

I should note that some authors in the quantum chemistry community use
different conventions, so if you're writing for a cross-disciplinary
audience, it's worth defining your notation explicitly.

### Question 3: Abstract structure

USER:

Here's my abstract:

"We investigate the topological phase diagram of monolayer Pt2HgSe3
using an extended Kane-Mele model. We find three distinct phases and
map out the full strain-Rashba parameter space. The topological gap can
be tuned by strain. Rashba coupling shifts the critical strain."

Does this follow the conventional structure for cond-mat abstracts?

ASSISTANT (fine-tuned):

The content is there, but the structure needs work. A conventional
condensed matter abstract follows this implicit template:

1. **Motivation/Context** (1 sentence): What system, what question
2. **Method** (1 sentence): How you did it
3. **Key results** (2-3 sentences): What you found, with numbers
4. **Significance** (1 sentence): Why it matters

Your abstract is missing the motivation and significance sentences, and
the results lack quantitative specifics. Here's how the structure maps:

- Sentence 1: Method (OK, but no motivation before it)
- Sentence 2: Result (too vague — which three phases?)
- Sentence 3: Result (no numbers — tuned by how much strain?)
- Sentence 4: Result (no numbers — shifted by how much?)

A stronger version would look like:

"Monolayer jacutingaite (Pt2HgSe3) has emerged as a promising quantum
spin Hall insulator with a sizable topological gap. [MOTIVATION] We
investigate its topological phase diagram using an extended Kane-Mele
model parametrized by first-principles calculations. [METHOD] We
identify three distinct phases — a quantum spin Hall insulator, a trivial
band insulator, and a metallic regime — and show that the topological gap
can be tuned from 0.15 eV to closure by biaxial strain of 4-6%.
[RESULT 1] Rashba spin-orbit coupling, arising from substrate
interactions, shifts the critical strain and produces a funnel-shaped
phase boundary in the strain-Rashba parameter space. [RESULT 2] These
results provide quantitative targets for experimental realization of
tunable topological phase transitions in this material. [SIGNIFICANCE]"

The key differences: specific numbers, named phases, and bookend
sentences that frame the work.

---

## Demo 4: Sharing via HuggingFace (Terminal Commands + Conversation)

**Context given to students:** You've fine-tuned a model and it's useful.
Now your collaborator wants to use it. Here's how to share a LoRA adapter
(not the full model — just the small set of modified weights) through
HuggingFace.

### Part 1: Uploading the Adapter

```bash
# Step 1: Install the HuggingFace CLI (one time)
pip install huggingface_hub

# Step 2: Log in (opens browser for token)
huggingface-cli login

# Step 3: Create a new model repository
huggingface-cli repo create condmat-qwen25-qlora \
  --type model \
  --organization dlab-berkeley

# Step 4: Upload the adapter files
# The adapter is small — usually 50-200 MB for a 3B model
cd ~/lora-output/condmat-adapter/
huggingface-cli upload dlab-berkeley/condmat-qwen25-qlora . . \
  --repo-type model

# Step 5: Verify it's up
# Visit: https://huggingface.co/dlab-berkeley/condmat-qwen25-qlora
```

Output:
```
Upload successful.
Repository: https://huggingface.co/dlab-berkeley/condmat-qwen25-qlora
Files uploaded: adapter_model.safetensors (148 MB), adapter_config.json,
  tokenizer_config.json, special_tokens_map.json
```

### Part 2: Collaborator Downloads and Uses It

```bash
# Step 1: Make sure you have the base model already
ollama pull qwen2.5:3b

# Step 2: Download the adapter from HuggingFace
pip install huggingface_hub
huggingface-cli download dlab-berkeley/condmat-qwen25-qlora \
  --local-dir ./condmat-adapter

# Step 3: Create a Modelfile that applies the adapter
cat > Modelfile << 'EOF'
FROM qwen2.5:3b
ADAPTER ./condmat-adapter

PARAMETER temperature 0.7
PARAMETER top_p 0.9

SYSTEM """You are a helpful assistant specializing in condensed matter
physics. You are familiar with standard conventions, notation, and
writing style used in condensed matter journal articles."""
EOF

# Step 4: Create the Ollama model from the Modelfile
ollama create condmat-assistant -f Modelfile

# Step 5: Run it
ollama run condmat-assistant
```

Output:
```
transferring model data...
creating model layer from adapter...
using qwen2.5:3b as base
created successfully: condmat-assistant
```

### Part 3: Collaborator Tests Their Own Draft

USER:

I'm testing the fine-tuned condensed matter model my colleague shared.
Here's the opening of my abstract — can you check if it follows
cond-mat conventions?

"The interplay between topology and strong correlations remains one
of the great open problems in condensed matter physics. In this work,
we use DMFT combined with a topological Hamiltonian approach to study
the Haldane-Hubbard model at half filling."

ASSISTANT (fine-tuned):

Your opening is solid and follows conventions well. A few specific
comments:

1. The first sentence works as a motivation statement. "One of the great
   open problems" is a common framing in PRL and PRB abstracts. Some
   referees find it slightly grandiose for anything below Nature Physics,
   but it's within the accepted range.

2. "In this work, we use..." is the standard transition to the method
   statement. Good.

3. "DMFT" — you should define this on first use in the abstract:
   "dynamical mean-field theory (DMFT)." Even though most cond-mat readers
   will know the acronym, standard practice is to spell it out once.

4. "Haldane-Hubbard model at half filling" is specific and tells the
   reader exactly what system you're studying. This is what reviewers want
   to see.

5. Minor style point: "combined with" is fine, but "in conjunction with"
   or "supplemented by" are also common. Some subfields prefer one over
   the other, but this isn't something a referee would flag.

Overall this reads like a real cond-mat abstract opening. The main
suggestion is to expand the DMFT acronym. Otherwise you're following
conventions correctly.

---

## Instructor Notes

### Timing

| Demo | Estimated time | Slide reference |
|------|---------------|-----------------|
| Demo 1 (Ping-Pong) | 5 min | Slides 8-10 |
| Demo 2 (Full Paper) | 7 min | Slides 11-14 |
| Demo 3a (Base vs Fine-Tuned) | 5 min | Slides 18-19 |
| Demo 3b (Field Questions) | 4 min | Slides 20-21 |
| Demo 4 (HuggingFace) | 4 min | Slides 23-25 |

### Fallback Plan

If Ollama is slow or unavailable during the workshop:
- All conversations above are pre-run and can be shown as slides
- The sample paper is saved as `sample_paper.txt` in this directory
- Screenshots of terminal output are in `dry_run_results/` (if available)

### Key Pedagogical Points

1. **Demo 1** teaches the workflow, not the technology. The ping-pong
   pattern works with any LLM. The point is that iterative prompting
   gives you better output than a single large prompt.

2. **Demo 2** shows the privacy advantage of local models. Emphasize:
   "Your unpublished manuscript never leaves your laptop."

3. **Demo 3** is the core argument for fine-tuning. The side-by-side
   comparison should make the difference visceral. Ask students: "Which
   one would you trust more for your own writing?"

4. **Demo 4** normalizes sharing. The adapter is small, the process is
   simple, and the scientific community benefits. Connect this to the
   open-science ethos.

### Additional Demos

See `additional_demos.md` for 6 more pre-run demos:
- **Demo Q:** Quantization live demo (size/speed/quality tradeoffs)
- **Demo 5:** System prompts for research personas (PRB reviewer, writing coach)
- **Demo 6:** Local API integration (Python + Ollama REST for batch processing)
- **Demo 7:** Model comparison (Llama 3.2 vs Qwen 2.5 vs Phi-3 on same task)
- **Demo 8:** Privacy-sensitive qualitative coding (IRB-safe with local LLMs)
- **Demo 9:** Temperature/sampling effects on academic writing
