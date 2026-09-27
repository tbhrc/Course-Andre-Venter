# Skill Anatomy

Use this as a reference while building your first Skills.

---

# 1. Required idea: one owned reusable job

Before creating files, finish this sentence:

> This Skill exists to ______ when ______.

Example:

> This Skill exists to prepare a live-audio technical preflight when a user provides venue/session requirements and needs a sound-check readiness plan.

If you cannot write that clearly, the Skill is probably not ready to exist.

---

# 2. Name

Use a short lower-case hyphenated name.

Examples:

- `audio-session-preflight`
- `dj-set-preparation`
- `maintenance-vendor-handover`
- `hydraulic-fault-triage`

Avoid:

- `andre-awesome-ai-skill`
- `do-everything`
- `general-helper`

The name should describe the reusable operating object.

---

# 3. Description

The description is discovery metadata.

It should answer:

- What does the Skill do?
- Which user requests should trigger it?
- What kind of object/outcome does it own?

Example:

```yaml
---
name: audio-session-preflight
description: Build live-audio session preflight plans from venue requirements, input lists and available equipment information. Use for technical sound-check preparation, missing-information checks and repeatable pre-show readiness reviews.
---
```

Do not hide trigger logic only inside the body.

---

# 4. SKILL.md body

A strong body can often fit into:

```markdown
# Audio Session Preflight

**Fast links:** [Input rules](references/inputs.md)

**Execution spine:** request → inspect source evidence → identify gaps → build preflight → verify → stop

## Rules

- Preserve supplied channel names.
- Do not invent missing equipment.
- Mark missing power/patch/input data explicitly.
- Separate required checks from optional improvements.

## Output

<required shape>

## Acceptance

- Every supplied input is accounted for.
- Missing data is explicit.
- No unverified equipment facts are presented as certain.
```

That may be enough.

Do not add sections because a template has space for them.

---

# 5. references/

Create a reference when detailed stable knowledge is needed sometimes, but not every time.

Example:

```text
references/
├── input-checklist.md
└── vendor-handover-format.md
```

Keep references easy to reach directly from `SKILL.md`.

Avoid deep chains such as:

```text
SKILL.md
→ reference A
→ reference B
→ reference C
```

The agent should not need a treasure hunt.

---

# 6. scripts/

Use a script only when it earns its maintenance.

Strong uses:

- parse a repeated CSV format;
- calculate exact values;
- transform file names deterministically;
- validate a strict machine schema.

Weak uses:

- summarise normal prose;
- choose the best explanation;
- interpret ambiguous notes;
- generate ordinary text.

The model already handles semantic work well.

---

# 7. assets/

Assets are output ingredients.

Examples:

- a report template;
- company logo;
- standard worksheet;
- fixed diagram base;
- boilerplate configuration.

Do not use `assets/` as a second reference library.

---

# 8. ChatGPT packaging metadata

For a Skill intended to be packaged for ChatGPT, current Skill packaging uses:

```text
agents/
└── openai.yaml
```

This contains user-interface metadata such as display name and short description.

The core Skill logic still belongs in `SKILL.md`.

---

# 9. What a Skill should NOT contain

Avoid:

- generic advice the model already knows;
- enormous copied documentation;
- secrets;
- passwords/API keys;
- today's volatile prices/plans unless the Skill is explicitly a dated snapshot;
- unrelated capabilities;
- duplicate procedures owned by another Skill;
- scripts that add no reliability or speed advantage.

---

# 10. Acceptance checklist

Before calling a Skill ready:

- [ ] The owned job is clear.
- [ ] The name is specific.
- [ ] The description clearly triggers on realistic requests.
- [ ] The body is the smallest complete decision map.
- [ ] Optional depth is moved to references.
- [ ] Scripts exist only for proven deterministic leverage.
- [ ] No secrets exist in the Skill.
- [ ] Volatile public facts are runtime-verified instead of copied blindly.
- [ ] One realistic case has been tested.
- [ ] At least one likely neighboring/non-trigger request has been considered.
- [ ] The result itself has been inspected.

A Skill is complete when it reliably improves the real job, not when every possible folder exists.
