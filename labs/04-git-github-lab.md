# Lab 04 — Git and GitHub

## Objective

Create a small repository change from start to finish and prove that you understand the history.

Use either this repository in a local clone or a separate practice repository.

If you are unsure whether a command is safe, ask your AI to explain the command **before** running it.

---

# Part A — Inspect

Run:

```bash
git status
git log --oneline -5
```

Write down:

- current branch;
- whether there are uncommitted changes;
- the latest commit message.

Do not continue until you understand the output.

---

# Part B — Create a practice file

Create:

```text
work/git-practice.md
```

Add:

```markdown
# Git Practice

My first version.

## What I think Git does

Write your answer here.
```

Run:

```bash
git status
git diff
```

Question:

Why might `git diff` not show a brand-new untracked file in the same way it shows changes to a tracked file?

Ask your AI if needed, but explain the answer back yourself.

---

# Part C — Stage and inspect

Run:

```bash
git add work/git-practice.md
git status
git diff --staged
```

Explain:

- what changed after `git add`;
- what "staged" means;
- what `git diff --staged` is showing.

---

# Part D — Commit

Commit:

```bash
git commit -m "Add Git practice notes"
```

Then:

```bash
git log --oneline -3
git status
```

Verify your commit appears.

---

# Part E — Change and compare

Edit the file.

Add:

```markdown
## Why Git matters with AI

Write three reasons.
```

Run:

```bash
git diff
```

Do not commit yet.

Ask your AI:

> Review this diff only. Tell me whether the change is limited to the requested section. Do not edit anything.

Compare its review with what you see.

Now commit the change.

---

# Part F — Branch

Create:

```bash
git switch -c experiment/better-git-notes
```

Change one section.

Run:

```bash
git status
git diff
```

Commit it.

Now inspect:

```bash
git log --oneline --decorate -5
```

Explain:

- what branch you are on;
- where the experimental commit lives;
- why `main` and the branch can now differ.

---

# Part G — GitHub Issue

Create one Issue in your practice repository:

**Title:**
`Improve Git practice explanation`

Body:

```markdown
## Outcome

Improve the Git practice notes so a future version of me can explain status, diff and commit without AI.

## Acceptance

- I can explain status.
- I can explain diff.
- I can explain commit.
- I can inspect a real change before accepting it.
```

Then explain:

Why is the Issue useful here, and when would it be unnecessary?

---

# Part H — Pull Request

Push the experimental branch to GitHub if your environment is configured to do so.

Create a PR from:

```text
experiment/better-git-notes
→ main
```

Before merging:

1. inspect the PR diff;
2. confirm no unrelated files changed;
3. read the commit history;
4. explain what the merge will do.

If you are not ready to push/merge, you may stop after inspecting the local branch difference. The learning objective is understanding, not blindly performing a remote write.

---

# Final verification

Create:

```text
work/04-git-lab-result.md
```

Answer:

1. What is the difference between working tree, staged changes and committed history?
2. What does a diff prove?
3. When would you use a branch?
4. When is an Issue useful?
5. When is a PR useful?
6. Why should you inspect AI changes before committing?
7. Which Git operation still feels unclear?

## Pass condition

Your AI coach should only mark this lab complete if your explanations match the actual repository state.
