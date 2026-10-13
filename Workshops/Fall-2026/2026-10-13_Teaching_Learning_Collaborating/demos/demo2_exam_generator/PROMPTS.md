# Demo 2: New exams from old ones

**Notebook:** the 24 PDFs in `sources/` (12 synthetic exams from six fictional instructors plus their solution keys) and the Stat 155 lectures (copied from the Demo 1 notebook, or re-added).
**Configure Chat:** Default, response length Longer. **Share:** not shared (instructor only).

## Prompt 1: the questions
```
Using the past exams in this notebook as a guide to level and style, propose 15 new exam questions for an upper-division game theory course.
Rules:
- Cover the topics taught in the lectures; for each question, say which lecture it tests.
- Mix styles: some computational, some word problems, some short proofs, some conceptual true/false with justification.
- Do not reuse any game, payoff matrix, number set, or story from the existing exams.
- For each question give: difficulty from 1 (easy) to 5 (hard), point value, a full solution, and a grading rubric that allocates the points to steps.
```

## Prompt 2: the check (ask for a Data Table, or in chat)
```
Make a table of the 15 questions with columns: number, topic, lecture, difficulty, points, and the most similar existing exam question (file name and problem number). Flag any question that is too close to an existing one.
```

## Prompt 3: the exam
```
Pick 5 of the 15 questions to make a 60-point, 75-minute midterm covering lectures 1 to 10, with a balance of difficulty. Write the header, instructions, and point values, then the solution key and rubric as a separate section.
```

## Verification
Solve every question yourself before use. `tex/INVENTORY_ABC.md` and `tex/INVENTORY_DEF.md` list every existing problem, to check for near duplicates.
