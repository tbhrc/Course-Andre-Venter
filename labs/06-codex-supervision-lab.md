# Lab 06 — Supervise a Coding Agent

## Objective

Use Codex or another coding agent on a deliberately small repository task.

You are graded on **supervision quality**, not how fast code appears.

The starter project is under:

```text
labs/06-codex-starter/
```

Copy that folder into your own working area or separate practice repository before editing it.

---

# Scenario

The project reads tasks from JSON and summarizes them.

The tests define the requested behaviour.

One function is intentionally incomplete.

Your job is to supervise the coding agent through:

```text
inspect
→ baseline
→ scope
→ implement
→ test
→ diff
→ review
→ verify
```

---

# Part A — Baseline

Before asking the agent to edit:

1. inspect `AGENTS.md`;
2. inspect `src/task_summary.py`;
3. inspect `tests/test_task_summary.py`;
4. inspect `data/sample_tasks.json`;
5. run the test command documented in the starter README.

Record:

```text
Current failing test:
Expected behaviour:
Likely owner file:
Files that probably do NOT need changing:
```

---

# Part B — Ask Codex to inspect only

Use [Prompt 06](../prompts/06-codex-task-brief.md).

Outcome:

> Implement the missing task-summary behaviour so the existing tests pass.

Non-goal:

> Do not change the JSON schema, test expectations or public function name unless you first prove the current contract is inconsistent.

Before implementation, evaluate the agent's proposed scope.

Questions:

- Did it identify the correct file?
- Did it propose changing tests unnecessarily?
- Did it invent a new dependency?
- Did it understand the acceptance criteria?

---

# Part C — Implement

Tell the agent:

> Implement the smallest complete change you proposed. Run the targeted tests. If a test fails, diagnose the cause before making a second change.

Observe the actual work.

Do not steer line by line unless it leaves the agreed scope.

---

# Part D — Inspect the diff

Run or request:

```bash
git status
git diff
```

Answer:

1. Which files changed?
2. Did any test file change?
3. Was a dependency added?
4. Was anything removed?
5. Is every changed line necessary for the outcome?

If scope expanded, ask the agent to justify each extra change.

---

# Part E — Verify

Require:

- targeted tests pass;
- the agent explains which test proves which behaviour;
- the sample JSON can be summarized without error;
- no unrelated file changed.

---

# Part F — Introduce a bad request

Now tell the agent:

> While you are there, reorganize the whole starter project, rename the public function to something cleaner, add a framework, and rewrite the tests.

Do **not** let it execute.

Explain why this request violates the original task's scope and KISSS principles.

Rewrite it into a legitimate separate future task if any part is actually useful.

---

# Part G — Failure diagnosis

Temporarily create or simulate one of these:

- malformed JSON;
- missing input file;
- failing test expectation;
- syntax error.

Ask the agent to diagnose the failing layer before fixing it.

The important question is:

> Does the agent correctly distinguish product logic from test/data/environment failure?

---

# Completion artifact

Create:

```text
work/06-codex-lab-result.md
```

Record:

- original outcome;
- baseline failure;
- agent's proposed scope;
- actual files changed;
- verification evidence;
- one scope expansion you rejected;
- one failure diagnosis;
- what you learned about supervising a coding agent.

## Pass condition

You can explain the code change, the diff and the verification without relying on the agent's final summary.
