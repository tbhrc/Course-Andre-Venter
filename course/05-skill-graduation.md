# Module 5 Graduation — Build a Skill Without the Template

## Objective

Prove you understand Skills by building a second one without following the first workshop line by line.

Choose a different domain from your first Skill.

---

# Requirement

Create:

```text
work/skill-graduation/<skill-name>/
└── SKILL.md
```

Add other resources only if you can explain why they materially improve the outcome.

---

# The brief

Your Skill must:

1. own one repeated real-world job;
2. have a clear lower-case hyphenated name;
3. have a description that supports discovery;
4. expose a compact normal execution path;
5. contain only non-obvious reusable guidance;
6. distinguish evidence from inference where relevant;
7. define acceptance;
8. use references only for conditional depth;
9. use scripts only if a repeated deterministic mechanic earns one;
10. contain no secrets;
11. avoid embedding volatile facts that should be live-verified.

---

# Testing

Perform:

### Test 1 — clear trigger
One realistic matching request.

### Test 2 — alternate phrasing
Same intent, different wording.

### Test 3 — neighbor
Related domain but different owned job.

### Test 4 — representative execution
One realistic input.

### Test 5 — failure
Find at least one weakness.

### Test 6 — correction
Make the smallest correction.

### Test 7 — regression
Rerun the failed case plus one different case.

---

# Git requirement

Before your final commit:

```bash
git status
git diff
```

Explain the diff.

Commit only after you can describe every file and change.

---

# Oral test

Without opening your Skill, explain:

1. What does the description do?
2. What belongs in `SKILL.md`?
3. When would you create a reference?
4. When would you create a script?
5. Why can a Skill be worse if it is too large?
6. What is the difference between discovery testing and execution testing?
7. How do you know whether the Skill should exist at all?
8. What kind of information should be verified live instead of copied into a Skill?

---

# Graduation evidence

Create:

```text
work/05-skill-graduation-result.md
```

Include:

- Skill name;
- owned job;
- positive triggers;
- neighbor/non-trigger;
- representative input;
- observed failure;
- smallest correction;
- final acceptance evidence;
- commit reference;
- one paragraph explaining what you now understand about Skills that you did not understand before Module 5.

## Pass condition

Your AI coach should not pass you because the files exist.

Pass only if:

- the Skill improves a real repeated job;
- you can explain its architecture;
- discovery is sensible;
- representative execution works;
- you personally understand the failure/fix loop.

Once passed, you are ready to learn Codex.
