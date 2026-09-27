# Module 6 — Codex Fundamentals: Supervise the Coding Agent

## Objective

Learn to supervise a coding agent working directly on a repository.

The goal is **not**:

> Make Codex write code for me.

The goal is:

> Give a capable coding agent a bounded engineering outcome, enough project context, and a verification contract—then inspect what it actually does.

This module uses Codex because it is a strong current coding-agent environment. The operating method should transfer to other capable coding agents.

For current product details, see [Codex current sources](../knowledge/codex-current-sources.md) and verify live.

---

## 1. A coding agent is not autocomplete

Autocomplete suggests code near your cursor.

An agent can operate across a repository:

- inspect files;
- understand instructions;
- search code;
- plan changes;
- edit multiple files;
- run commands;
- run tests;
- inspect errors;
- revise its work;
- review diffs;
- explain what changed.

That makes the quality of the **environment and supervision** important.

---

## 2. The coding-agent contract

Use the Agent Brief you already learned:

```text
OUTCOME
CONTEXT
INPUTS
CONSTRAINTS
TOOLS
ACCEPTANCE
STOP
```

For repository work, add:

```text
SCOPE
Which repository/files/components are actually in scope?

BASELINE
What currently works or fails before the change?

VERIFY
Which tests/checks prove the requested outcome?
```

Example:

> In this repository, implement support for marking a task complete. Read AGENTS.md and inspect the existing task model and tests before changing anything. Preserve existing JSON fields and public function names unless the current code proves a change is necessary. First tell me the smallest file set you expect to touch and how you will verify the change. Then implement it, run the relevant tests, show me the diff, and stop. Do not refactor unrelated code.

This is much stronger than:

> Add complete task support.

---

## 3. Inspect before changing

A coding agent should usually inspect enough of the repository to answer:

- What is the project?
- What instructions govern this area?
- Where is the relevant code?
- What is the current behaviour?
- What tests already exist?
- What should remain unchanged?

Useful first request:

> Read the root AGENTS.md and the smallest relevant code/test surface. Explain the current behaviour, the likely owner files, and the verification path. Do not edit yet.

Why this matters:

A coding agent can produce technically valid code in the wrong architectural location.

Inspection protects placement and intent.

---

## 4. Scope the change

Strong scope:

```text
one user-visible outcome
+ smallest relevant files
+ explicit non-goals
+ acceptance evidence
```

Weak scope:

> Clean up this project and add the feature.

That mixes:
- feature work;
- refactoring;
- architecture;
- style cleanup;
- unknown acceptance.

Use KISSS:

```text
DIRECT
→ smallest useful change
→ broader refactor only if the real change proves it necessary
```

---

## 5. Ask for the verification path before implementation

Before the agent changes code, ask:

> What exact test/check will prove this works?

Possible evidence:

- an existing unit test;
- a new targeted unit test;
- type check;
- linter;
- build;
- CLI example;
- API response;
- rendered UI;
- integration test.

Do not accept:

> I will test it.

Ask what will be tested.

---

## 6. Let the agent work—but keep evidence visible

A practical loop:

```text
inspect
→ explain
→ change
→ run checks
→ inspect errors
→ revise
→ show diff
→ verify
→ stop
```

Do not interrupt every line-level edit.

Do interrupt when:
- scope expands;
- the agent wants to change architecture without evidence;
- it removes a public interface unexpectedly;
- it proposes a destructive command;
- tests fail for unclear reasons;
- it declares success without proof.

Supervision is not micromanagement.

---

## 7. Read the diff before trusting the summary

Agent summary:

> Added validation and updated tests.

Diff:

```text
3 files changed
+ validation
+ test update
- public function
- compatibility path
+ unrelated refactor
```

The summary is not enough.

Review:

1. Which files changed?
2. What was added?
3. What was removed?
4. Did scope expand?
5. Did the agent change an interface?
6. Did the tests meaningfully test the outcome?
7. Is any change unrelated?

Use [Prompt 04 — Git Change Review](../prompts/04-git-change-review.md).

---

## 8. Tests are evidence, not magic

A green test suite proves only what the tests cover.

Ask:

- Which test proves my requested behaviour?
- Was that test already present?
- If a new test was added, does it test the real outcome or merely the implementation?
- Could the code still fail outside the test's assumptions?

Useful hierarchy:

```text
no test
< test runs
< targeted test passes
< regression suite passes
< representative real behaviour verified
```

Do not require every layer for every task.

Use the smallest decisive proof.

---

## 9. Failure is diagnostic evidence

When a command/test fails, do not tell the agent only:

> Fix it.

Ask:

> Explain the failing layer and the evidence. Is this caused by the code change, an existing baseline failure, a dependency/environment problem, a test assumption, or an unrelated repository issue?

Possible failure layers:

```text
requirement
instruction
code logic
test
dependency
environment
permissions
network
tooling
data
```

Change one material cause at a time when possible.

---

## 10. Rollback thinking

You should be able to answer:

> If this change is wrong, how do I get back?

Good habits:

- inspect Git status before work;
- work on a branch/worktree for materially isolated work;
- commit meaningful stable checkpoints;
- avoid destructive Git commands you do not understand;
- prefer corrective commits over rewriting history while learning.

Do not ask an AI to “undo everything” without inspecting what “everything” includes.

---

## 11. AGENTS.md and repository instructions

Codex and other coding agents benefit from project instructions.

Your root instructions should not contain every coding detail.

They should route to:
- project purpose;
- key directories;
- coding/testing conventions that materially matter;
- relevant Skills;
- verification expectations;
- important boundaries.

Current Codex tooling can help scaffold project instructions in some clients, but you must still understand and review the resulting instructions.

Do not outsource the meaning of your repository to an initialization command.

---

## 12. When to use a branch or isolated worktree

Direct work on the main line may be fine for tiny personal exercises.

Use isolation when:
- the change is material;
- multiple agents/people may work concurrently;
- experimentation may be discarded;
- you want a clean review surface;
- the main branch must remain stable.

Isolation should reduce collision risk.

It should not become ceremony for every one-line edit.

---

## 13. Parallel agents come later

Modern Codex surfaces can support parallel work.

That does not mean you should begin with multiple agents.

First prove:

```text
one task
→ one coding agent
→ clean scope
→ inspectable diff
→ reliable verification
```

Then parallelize only independent work whose merge/review cost does not erase the benefit.

This course introduces broader multi-agent orchestration later.

---

## 14. A reusable Codex task shape

Use:

```text
Read:
- AGENTS.md
- <smallest relevant files/tests>

Outcome:
- <one observable result>

Preserve:
- <interfaces/data/behaviour that must remain>

Non-goals:
- <what not to refactor/change>

Before editing:
- explain current behaviour
- identify smallest file set
- state verification path

Then:
- implement smallest complete change
- run targeted verification
- inspect failure if any
- show diff
- map evidence to acceptance criteria
- stop
```

---

## Practical work

Complete:

1. [Lab 06 — Supervise a Coding Agent](../labs/06-codex-supervision-lab.md)
2. [Codex supervision playbook](../playbooks/codex-supervision.md)
3. [Prompt — Codex Task Brief](../prompts/06-codex-task-brief.md)

## Teach-back

Explain without notes:

1. Why inspect before edit?
2. Why is an agent summary weaker than a diff?
3. Why can a green test still be insufficient?
4. When should you isolate work on a branch/worktree?
5. What is the difference between supervising and micromanaging a coding agent?
6. Why does the course teach one coding agent before parallel agents?

## Pass condition

You can give a coding agent a bounded repository task, review its actual change, identify the evidence supporting success, and reject unnecessary scope expansion.
