# Lab — Diff, Debug and Rollback

## Objective

Practise what to do when an AI-generated code change is wrong.

Use a small practice repository.

---

## Part 1 — Establish clean state

Run:

```bash
git status
git log --oneline -3
```

Confirm what the last known-good state is.

---

## Part 2 — Ask for a bounded change

Choose a tiny feature.

Require the coding agent to:

- inspect first;
- make the change;
- run a targeted test;
- stop before committing.

---

## Part 3 — Inspect the diff

Run:

```bash
git diff
```

Find one line or file you do not understand.

Ask:

> Explain why this exact change is necessary for the requested outcome. Do not edit yet.

If the explanation is weak, challenge the change.

---

## Part 4 — Deliberately introduce an error

Examples:

- invert a condition;
- change a field name;
- remove a required return;
- alter a path.

Run the relevant check.

Before asking for a fix, predict:
- what should fail;
- where;
- why.

---

## Part 5 — Diagnose before repair

Ask the coding agent:

> Classify the failure. Show evidence for the cause. Do not fix it yet.

Compare its diagnosis with yours.

Then make the smallest repair.

---

## Part 6 — Rollback exercise

On a practice branch, make a disposable bad change.

Use Git to return to the known-good content.

While learning, prefer a method you understand and can inspect.

Do not use destructive history-rewriting commands merely because the AI suggests them.

Ask the agent to explain:
- what state will change;
- what work could be lost;
- whether a safer corrective approach exists.

---

## Part 7 — Commit the proven result

Only after:
- diff reviewed;
- targeted check passes;
- acceptance criteria mapped to evidence.

Create one meaningful commit.

---

## Reflection

Create `work/07-diff-debug-rollback-result.md`.

Answer:

1. How did you identify the last known-good state?
2. What did the diff reveal that the agent summary did not?
3. Which failure layer was responsible?
4. What was the smallest repair?
5. How did you know rollback would not destroy unrelated work?
6. Why is reversibility part of agentic engineering?
