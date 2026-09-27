# Workshop 05 — Build Your First Skill

## Objective

Build one small Skill from a job you already understand well.

Do **not** choose a topic you are still learning.

Your existing expertise should let you judge whether the AI procedure is actually good.

---

# Step 1 — Choose a repeated job

Choose one:

### Audio
Prepare a live/studio session preflight.

### DJ
Prepare a set from an event brief and track list.

### Industrial maintenance
Convert fault notes into a manufacturer/vendor escalation.

### Hydraulics
Turn symptoms and measurements into a structured diagnostic intake.

Or choose another job you perform repeatedly.

Write:

```text
The repeated job:
The input:
The useful output:
Why doing it consistently matters:
```

---

# Step 2 — Test the task without a Skill

Give your AI one representative example.

Use a normal prompt.

Observe:

- What did it do well?
- What did it guess?
- What did it omit?
- Which instructions did you have to add?
- Which corrections would you probably repeat next time?

Create:

```text
work/05-first-skill-observations.md
```

Capture only material observations.

---

# Step 3 — Extract reusable rules

From your observations, identify 3–8 rules that should survive future sessions.

Examples:

```text
- Never invent missing equipment specifications.
- Preserve measured pressure values exactly.
- Separate observed symptom from suspected cause.
- Always show unresolved information before recommendations.
```

If you have 40 rules on your first attempt, stop.

You are probably writing a manual, not a small Skill.

---

# Step 4 — Define the trigger

Write three requests that **should** trigger the Skill.

Example:

```text
1. Turn these machine fault notes into a manufacturer escalation.
2. Prepare a technical handover for this hydraulic fault.
3. Summarise our troubleshooting evidence for vendor support.
```

Now write two requests that should **not** trigger it.

Example:

```text
1. Explain how a hydraulic pump works.
2. Write a general preventive-maintenance schedule.
```

This is your first discovery test.

---

# Step 5 — Name the Skill

Choose a lower-case hyphenated name.

Good:

```text
maintenance-vendor-handover
```

Bad:

```text
andre-machine-ai-helper
```

---

# Step 6 — Create the folder

Under your course working area create:

```text
work/my-first-skill/
└── SKILL.md
```

Start small.

Add `references/`, `scripts/`, `assets/` only if the real job proves they are needed.

---

# Step 7 — Write frontmatter

Use:

```yaml
---
name: <your-name>
description: <what it owns + realistic trigger wording>
---
```

Challenge the description:

> Would an AI know from this description when to select the Skill?

---

# Step 8 — Write the control plane

Use this starter:

```markdown
# <Human-readable name>

**Execution spine:** request → inspect evidence → <core decisions> → verify → output

## Rules

- ...

## Output

Describe only the parts of the output that must be consistent.

## Acceptance

- ...
```

If a reference is actually needed, add a **Fast links** line and create the smallest reference.

---

# Step 9 — Test representative execution

Use the same representative input from Step 2.

Do not tell the AI what improvement you expect.

Observe the result.

Compare:

```text
WITHOUT SKILL
vs
WITH SKILL
```

Did the Skill materially improve consistency or correctness?

If not, do not add more pages immediately.

Find the smallest missing rule.

---

# Step 10 — Test a neighboring request

Give the AI one of your "should not trigger" requests.

Ask:

> Would you use my Skill for this request? Explain why or why not before answering the request.

If the Skill is too broad, improve the description.

---

# Step 11 — Failure-driven revision

Choose one real weakness from the test.

Modify only what is needed.

Examples:

- description too broad → fix description;
- agent invents evidence → add explicit evidence rule;
- output inconsistent → define output shape;
- large domain table needed → move it to a reference;
- exact repeated calculation fails → consider a script.

Do not redesign the whole Skill because one case failed.

---

# Step 12 — Commit the Skill

Before committing:

```bash
git status
git diff
```

Inspect what changed.

Then commit with a meaningful message.

Example:

```text
Build first maintenance vendor handover Skill
```

---

# Workshop completion

Create:

```text
work/05-first-skill-result.md
```

Answer:

1. What repeated job does your Skill own?
2. What requests trigger it?
3. Which requests should not trigger it?
4. Which part of the Skill produced the biggest improvement?
5. What did you deliberately leave out?
6. Does it need a script? Why or why not?
7. What failure did you observe and correct?
8. What evidence proves the Skill is better than the original one-off prompt?

Your first Skill does not need to be impressive.

It needs to be **useful, understandable and proven**.
