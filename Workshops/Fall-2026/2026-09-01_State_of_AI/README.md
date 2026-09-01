# Session 1 (Fall 2026): The State of AI

**D-Lab AI Pulse, Fall 2026** — the opening session of the Fall series, and a wide-view
session rather than a hands-on one. 1 September 2026.

## The session

A map of where AI actually stands, for people being brought into it rather than people
already working in it. No prior experience assumed, and nothing in the session requires a
paid account.

It opens with what changed and what now exists, moves to what agents do and whether any of
it holds up when somebody measures, and closes on what all of this asks of the person doing
the work.

## Structure

**Part 1 — Where things stand.** How we got here, from the 2017 transformer paper to the
first AI-produced proof of a major open problem in May 2026. The ladder from chats to
agents. One power user's working day, and then everybody else: adoption across workplaces,
classrooms and peer review. A catalogue of what exists, what the plans cost, what a token
costs, and why the best option is usually not the best model.

**Part 2 — What agents do, and whether it works.** What separates an agent from a chat, what
one can reach, and what lies beyond the main apps for repeated work at scale. Tools built for
science. Then the turn: a randomised trial that found nothing, the failure mode that leaves
no trace, and why accuracy and safety are different measurements.

**Part 3 — How your role changes.** Whether this replaces workers or replaces work.
Kasparov's centaurs, and the same pattern arriving in mathematics twenty-one years later.
What that leaves you doing, and a rule for what to hand over.

## Contents

```
slides/workshop_slides.tex    # LaTeX Beamer source
slides/workshop_slides.pdf    # Compiled slides
```

Compile with `pdflatex workshop_slides.tex` from inside `slides/`, twice, so the page
counter in the footer is correct.

The source carries a status legend above `\begin{document}`, and a source comment on every
factual claim recording where it came from, when it was verified, and what undercuts it.

## Status

Complete, 31 slides.

**Perishable content.** Anything about model versions, prices, leaderboards or vendor
offerings dates fast. Re-check before re-delivering: the tool catalogue, the subscription
prices, the per-token price table, and the LMArena standings. Each is flagged in the source.

**Image provenance.** `slides/drafting_room.jpg` has no established source, photographer or
licence, so it is excluded from this repository and the `\includegraphics` call is guarded
with `\IfFileExists`. The source therefore compiles without it, showing a placeholder note
in its place. Note that the compiled PDF here still embeds the photograph.
