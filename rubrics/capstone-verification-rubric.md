# Capstone Verification Rubric

This is a **pass/fail evidence rubric**, not a beauty contest.

## A. Outcome

- [ ] real problem is clear;
- [ ] observable acceptance exists;
- [ ] demo proves the intended outcome.

## B. Architecture

- [ ] smallest complete architecture;
- [ ] every component has a reason;
- [ ] one source of truth per mutable meaning;
- [ ] data/control flow is explainable;
- [ ] recovery path exists for material failures.

## C. Agent control

- [ ] root instructions are durable and tested;
- [ ] repeated HOW is in a Skill only when justified;
- [ ] agent stop/verification behaviour is clear.

## D. Durable engineering

- [ ] Git history is meaningful;
- [ ] coding-agent changes were inspected;
- [ ] tests/checks support the code change;
- [ ] rollback/recovery is understood.

## E. Tools and state

- [ ] existing dedicated tools reused where possible;
- [ ] APIs/MCP are justified rather than decorative;
- [ ] tool authority matches real need;
- [ ] current external state is verified from its owner.

## F. Reliability

- [ ] representative eval set exists;
- [ ] at least one prior/created failure is a regression case;
- [ ] learner can identify failing layers;
- [ ] evidence is stronger than agent self-report.

## G. Safety

- [ ] secrets are not exposed;
- [ ] untrusted content is treated as data;
- [ ] consequential actions have appropriate control;
- [ ] unnecessary approval friction is absent.

## H. Operability

- [ ] learner can explain the architecture unaided;
- [ ] learner can locate relevant instructions/code/state;
- [ ] learner can diagnose a failure;
- [ ] learner can identify what would need production hardening.

## Result

Pass only when all material criteria for the chosen capstone are evidenced.

Mark genuinely irrelevant criteria as:

```text
N/A — <reason>
```

Do not invent work merely to eliminate an N/A.
