# Module 5 — Skills

## Objective

Learn how to turn a repeated way of working into a small reusable capability that another AI can discover and execute.

A Skill is not "a very long prompt."

A useful Skill is closer to a **technical operating procedure for an AI**, packaged so the relevant instructions and resources can be loaded when the job appears.

---

## 1. The problem Skills solve

Imagine telling an AI the same thing repeatedly:

> When preparing a live sound session, first inspect the venue requirements, then check the input list, flag missing technical information, produce a preflight checklist and never invent equipment specifications.

If you repeat that across many conversations, you have discovered reusable behaviour.

That behaviour may deserve a Skill.

Without a Skill:

```text
new chat
→ re-explain procedure
→ hope nothing is forgotten
→ repeat next time
```

With a Skill:

```text
matching request
→ Skill discovered
→ compact procedure loaded
→ relevant references/tools loaded only if needed
→ job performed consistently
```

---

## 2. When NOT to create a Skill

Do not create a Skill because:

- a task happened once;
- you like the idea of having many Skills;
- one paragraph of project instructions already solves the problem;
- the host tool already does it natively;
- the Skill would just copy public documentation that changes frequently.

A Skill should earn its existence through reuse or meaningful consistency.

---

## 3. Skill mental model

A good Skill has three layers:

```text
DISCOVERY
name + description
"Should this Skill trigger?"

CONTROL PLANE
SKILL.md
"What is the smallest complete way to do the job?"

CONDITIONAL DEPTH
references / scripts / assets
"What extra material is needed only in some cases?"
```

This is progressive loading.

You do not put the entire manual into the first page.

---

## 4. The description is important

The description helps the agent decide when the Skill applies.

Weak:

```yaml
description: Helps with audio.
```

Better:

```yaml
description: Prepare and review live sound session preflight plans from venue, input-list and equipment information. Use when a user asks to prepare a technical sound-check checklist, identify missing session information, or standardise a live-audio preflight.
```

The body is loaded **after** the Skill is selected.

Therefore important trigger wording belongs in the description, not hidden deep in the body.

---

## 5. Minimal Skill structure

The reusable core usually starts with:

```text
my-skill/
├── SKILL.md
├── references/     optional
├── scripts/        optional
└── assets/         optional
```

For a ChatGPT-packaged Skill, current platform packaging also includes:

```text
agents/
└── openai.yaml
```

Do not create folders you do not need.

### What belongs where?

**SKILL.md**
- trigger/ownership;
- core decision flow;
- non-obvious rules;
- acceptance;
- links to optional resources.

**references/**
- deeper domain guidance;
- schemas;
- detailed procedures;
- stable knowledge the Skill needs.

**scripts/**
- repeated deterministic mechanics;
- exact transformations;
- fragile calculations;
- operations where code is more reliable than prose.

**assets/**
- templates;
- images;
- boilerplate artifacts used in output.

---

## 6. Smart-agent-first design

Do not write 200 lines telling a capable agent how to perform obvious reasoning.

Write only the reusable information that materially improves execution.

Example:

Bad:

```text
Step 1: Read the user's message carefully.
Step 2: Think about what they want.
Step 3: Be accurate.
Step 4: Be helpful.
...
```

These are generic model behaviours.

Better:

```text
If venue power information is missing, mark POWER DATA MISSING.
Do not infer amplifier draw from brand/model unless a verified specification is provided or retrieved from an authoritative source.
```

That is specific, reusable and valuable.

---

## 7. Course convention: Fast Links + Execution Spine

In this course, Skills should make their normal path visible near the top.

Example:

```markdown
**Fast links:** `references/input-checklist.md` · `references/output-format.md`

**Execution spine:** request → inspect inputs → identify missing evidence → build checklist → verify against inputs → output
```

These are useful design conventions from the FolderDesk/TBHRC ecosystem.

They are not a substitute for the actual Skill body.

---

## 8. Durable knowledge vs live knowledge

Before copying information into a Skill, ask:

> Will this remain true?

Good durable Skill content:

- a company workflow;
- a stable checklist;
- decision logic;
- output rules;
- internal naming conventions;
- acceptance criteria.

Poor candidate for copying into a general Skill:

- today's model prices;
- today's software plan limits;
- current product feature table;
- live regulations that can change.

For volatile public facts, point to the authoritative live source and instruct the agent to verify at runtime.

---

## 9. Agent judgement vs scripts

Use agent reasoning for:

- ambiguous interpretation;
- diagnosis;
- choosing between valid options;
- reviewing human language;
- exception handling.

Consider a script when:

- the same exact mechanical work repeats;
- a transformation must be deterministic;
- a calculation must be exact;
- repeated manual tool work is slow or fragile.

Do not replace a capable agent's judgement with code just because you can write code.

---

## 10. A Skill build loop

Use:

```text
real repeated outcome
→ define trigger
→ identify reusable decisions
→ create smallest SKILL.md
→ add only necessary resources
→ test one representative case
→ observe failure
→ make smallest correction
→ test again
```

Do not start by designing ten theoretical edge cases.

Test reality.

---

## 11. Example: maintenance handover Skill

Suppose the repeated job is:

> Turn machine fault notes into a clear technical vendor handover.

Potential Skill:

```yaml
---
name: maintenance-vendor-handover
description: Convert industrial equipment fault observations, measurements and attempted interventions into a structured vendor/escalation handover. Use when preparing a manufacturer support case, maintenance escalation, or fault summary from technician notes.
---
```

Core rules may include:

- distinguish observation from inference;
- preserve measured values exactly;
- show sequence of events;
- list interventions already attempted;
- mark missing evidence rather than guessing;
- produce a concise vendor-ready summary.

No Python required.

The value is the procedure and discipline.

---

## 12. Test discovery separately from execution

Two questions:

### Discovery test

> Does the Skill trigger for the right request?

Example matching request:

> Prepare these hydraulic fault notes for manufacturer escalation.

Example neighboring request:

> Explain generally how hydraulic accumulators work.

The first may need the handover Skill.

The second probably does not.

### Execution test

Once triggered:

> Does the Skill actually produce the intended result?

Both matter.

---

## Practical work

Complete:

1. [Skill Anatomy](../knowledge/skill-anatomy.md)
2. [First Skill Workshop](../workshops/05-first-skill-workshop.md)
3. [Technical-domain Skill exercises](../exercises/05-skill-domain-exercises.md)
4. [Skill testing and debugging](../playbooks/skill-testing-debugging.md)
5. [Skill graduation exercise](05-skill-graduation.md)

## Pass condition

You can identify a repeated behaviour worth packaging, create a minimal Skill, explain why every file exists, and demonstrate that it works on at least one realistic case.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [6. Codex fundamentals](06-codex-fundamentals.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
