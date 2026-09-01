# D-Lab AI Pulse

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

AI Pulse is UC Berkeley D-Lab's bi-weekly online workshop series on AI tools for research and academia. Sessions run 50 minutes and alternate between **wide-view sessions** on where AI actually stands and **hands-on sessions** that walk through specific tools, with discussion running throughout rather than saved for the end.

No prior experience with AI tools required! Check out D-Lab's [Workshop Catalog](https://dlab-berkeley.github.io/dlab-workshops/) to browse all workshops.

---

## Fall 2026

Bi-weekly on Tuesdays, opening 1 September 2026. Slides and materials are published here after each session runs.

### Session 1 (September 1, 2026): The State of AI

**Wide-view** | [Materials](Workshops/Fall-2026/2026-09-01_State_of_AI/)

In this workshop we will discuss how AI arrived at where it stands today, and where it has been used effectively — and where it hasn't. We start with the many ways of interacting with AI, from chats to agentic workflows, then turn to practical concerns such as which model tier is appropriate for each task. Participants should leave with a map of the current tools, applications and buzzwords, and a sense of where to start.

### Session 2 (September 15, 2026): The Major AI Ecosystems — Anthropic and OpenAI

**Hands-on** | *Materials to follow.*

As AI subscriptions become a real expense rather than a token one, one of the first questions after deciding to get hands-on is which environment to sign up for. In this workshop we will compare the two largest, Anthropic's and OpenAI's, looking at what they have in common and where they genuinely differ, along with the practical details: what each plan costs, what comes for free, what each company is building beyond the chat window, and what they do with your data. Participants should leave knowing which ecosystem best fits their own work and budget, and how to get started.

### Session 3 (September 29, 2026): AI in the News

**Wide-view** | *Materials to follow.*

In just a few years, AI went from a novelty you tried online to a fixture in the news. In this workshop we will go through a handful of the most consequential AI stories of the past year, from stand-offs with defence agencies to models breaking containment, unpacking the technical terms and following each one through to how it actually ended. For each we will propose a set of open questions, ethical, social and political, and open the floor. Participants should leave with a clear picture of stories they may only have half-followed, and with a range of views on what those stories mean, gathered from across the campus community.

*More sessions to be announced.*

---

## How this repository is organised

Each workshop is a self-contained folder:

```
Workshops/<Season-Year>/<YYYY-MM-DD>_<Workshop_Name>/
├── README.md                   # what the session covered
├── slides/
│   ├── workshop_slides.tex     # LaTeX Beamer source
│   └── workshop_slides.pdf     # compiled slides
├── demos/                      # data, scripts, prompts and codebooks used live
├── dry_run_output.md           # pre-generated demo output, in case a live demo fails
└── SOURCE.md                   # where to get external data not tracked here
```

Not every session has every file. Wide-view sessions carry no `demos/`, and only some sessions publish their LaTeX source.

Slides are built with `pdflatex workshop_slides.tex` from inside a session's `slides/` directory.

---

## Past seasons

- **[Spring 2026](Previous-Workshops/Spring-2026/)** — the first season. Eight sessions from January to April 2026, covering coding assistants, specialised research tools, teaching and learning, qualitative work, science case studies, running models locally, and a year-in-review.

---

## Resources

- [D-Lab](https://dlab.berkeley.edu/)
- [Gemini](https://gemini.google.com/) (Free for Berkeley accounts!)

---

## About the UC Berkeley D-Lab

D-Lab works with Berkeley faculty, research staff, and students to advance data-intensive social science and humanities research. Our goal at D-Lab is to provide practical training, staff support, resources, and space to enable you to use AI tools for your own research applications.

Visit the [D-Lab homepage](https://dlab.berkeley.edu/) to learn more about us.

## Contributors

* Bruno Cittolin Smaniotto
* Tom van Nuenen
