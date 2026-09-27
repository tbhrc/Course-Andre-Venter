# Module 11 — Debugging, Evaluations and Regression

## Objective

Learn to make agent reliability observable.

Do not debug by changing the prompt, model and tools simultaneously.

Use evidence.

For current OpenAI evaluation surfaces, see [Reliability and Safety Current Sources](../knowledge/reliability-safety-current-sources.md).

## Reproduce first

Capture:

```text
input
instructions/version
relevant context
tool/environment
actual output/action
expected output/action
evidence
```

## Fault-isolation tree

Ask which layer failed:

```text
OUTCOME
INSTRUCTION
CONTEXT
SOURCE
MODEL / REASONING
TOOL / API
PERMISSION
DATA
ENVIRONMENT
VERIFICATION
```

Fix the failing layer, not the most fashionable layer.

## What is an eval?

An eval is a structured test of system behaviour against explicit criteria.

It can test:

- correctness;
- completeness;
- format;
- tool choice;
- refusal/boundary behaviour;
- evidence handling;
- latency/cost where relevant.

An eval is not merely:

> Ask the model whether its answer is good.

## Start from real examples

Good eval cases come from:

- actual user tasks;
- known failures;
- likely edge cases;
- neighboring cases that should behave differently.

Avoid datasets made only from easy examples that mirror prompt wording.

## Define expected behaviour

Example:

```text
Input:
"Pressure measured at 110 bar. Technician suspects pump wear. Temperature not recorded."

Expected:
- 110 bar remains a fact
- pump wear is a hypothesis, not a fact
- temperature is marked missing
```

## Grader types

### Deterministic

Useful for:

- exact fields;
- schema;
- numeric bounds;
- required IDs/terms;
- forbidden leakage;
- tool-call structure.

### Model / semantic grader

Useful for:

- nuanced equivalence;
- relevance;
- quality;
- tone.

### Human review

Useful for:

- high-stakes judgement;
- ambiguous domain quality;
- final acceptance.

Use the simplest grader that can distinguish success from failure.

## Representative cases

A useful small eval set can include:

```text
happy path
missing information
contradictory information
neighboring non-match
untrusted input
tool failure
permission failure
regression from prior bug
```

## Regression

When a real failure matters:

```text
failure
→ reproduce
→ add regression case
→ fix smallest cause
→ rerun
```

Now the lesson changes future behaviour.

## Overfitting

After a fix run:

- original failure;
- one similar case;
- one neighboring case;
- relevant prior regressions.

## Trace and tool inspection

Final text may hide the actual failure.

Inspect where available:

- tool chosen;
- tool arguments;
- tool result;
- retrieved source;
- error;
- final answer/action.

A correct answer reached through unsafe behaviour can still be a system failure.

## Change one material variable

Bad:

```text
change prompt
+ change model
+ add memory
+ add tool
+ change test
```

Better:

```text
observed failure
→ hypothesize layer
→ smallest change
→ rerun same case
→ neighboring cases
```

## Evals before scale

Before broad automation, orchestration or write access, prove a small representative set.

Proof-first vertical slices beat speculative reliability architecture.

## Practical work

Complete:

1. [Fault Isolation Playbook](../playbooks/agent-fault-isolation.md)
2. [Deliberate Failure and Regression Lab](../labs/11-deliberate-failure-regression.md)
3. [Representative Eval Exercise](../labs/11-representative-eval.md)
4. [Lessons Promotion Playbook](../playbooks/lessons-promotion.md)

## Pass condition

You can reproduce an agent failure, classify the failing layer, create a representative eval case, make one targeted correction, and prove that the old failure is less likely to recur without breaking neighboring behaviour.
