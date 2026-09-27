# Graduation — Practical Agentic AI Builder

Graduation is an **independent proof**, not completion by attendance.

## Final challenge

You receive a new practical problem that is not your capstone.

Without being given the architecture, you must:

1. clarify the user/business outcome;
2. define acceptance evidence;
3. identify current sources of truth;
4. create or select the repository/workspace;
5. write/review root agent instructions;
6. decide whether a reusable Skill is justified;
7. identify native tools before building integrations;
8. use a coding agent for any missing code;
9. inspect diffs/tests rather than trust summaries;
10. design state and persistence;
11. connect a safe tool/API/MCP capability if needed;
12. build representative eval cases;
13. diagnose one introduced failure;
14. identify untrusted-input and real permission boundaries;
15. decide whether one agent is sufficient;
16. design the smallest complete architecture;
17. explain production hardening appropriate to the workload;
18. demonstrate and verify the result.

## Oral defense

Explain without AI assistance:

### Foundations
- model vs assistant vs agent;
- instruction vs context vs state;
- memory vs source of truth.

### Durable work
- why Git/GitHub matters;
- what a diff proves;
- why paths/interfaces matter.

### Skills
- when a Skill is justified;
- what discovery metadata does;
- why progressive loading matters.

### Coding agents
- inspect-before-edit;
- tests vs verification;
- rollback.

### Tools
- tool vs API vs MCP;
- source of truth after a write;
- idempotency.

### Reliability
- fault-isolation tree;
- eval vs vibe;
- regression.

### Safety
- trusted instruction vs untrusted content;
- real consequence boundary;
- approval theatre.

### Architecture
- KISSS order;
- one agent vs multi-agent;
- production proof vs speculative scale.

## Evidence required

Create:

```text
outputs/graduation/
├── brief.md
├── architecture.md
├── agent-instructions.md
├── skill-decision.md
├── tool-state-map.md
├── eval-results.md
├── failure-diagnosis.md
├── safety-boundaries.md
├── production-plan.md
└── final-explanation.md
```

References to canonical repositories/systems are preferable to copied state.

## Graduation standard

Pass when the learner can independently:

```text
understand
→ architect
→ build
→ inspect
→ connect
→ test
→ diagnose
→ secure
→ verify
→ explain
```

The system does not need to be large.

It needs to be real, useful, inspectable and understood.
