# Module 14 — Capstone: Build a Real Agentic System

## Objective

Build one useful end-to-end agentic system that solves a real problem.

The capstone is not a feature checklist.

It proves that you can combine the course's operating methods into one coherent system.

---

## Required ingredients

Your capstone must include:

- clear outcome and acceptance evidence;
- repository/workspace;
- root project instructions;
- at least one reusable Skill where justified;
- Git history;
- coding-agent/Codex involvement where code is needed;
- existing tool/API/MCP capability where useful;
- explicit source-of-truth/state design;
- representative evals;
- fault diagnosis;
- appropriate permission/safety boundaries;
- architecture proof;
- deployment/operating plan appropriate to its scope.

A component may be omitted if you can explain why it is unnecessary.

---

## Capstone tracks

Choose a real domain.

### Track A — Business Operations Agent

Examples:

- customer/account brief;
- sales follow-up preparation;
- recruitment screening workflow;
- finance/admin review;
- support triage.

### Track B — Research / Knowledge Agent

Examples:

- evidence-backed research brief;
- policy/market monitoring;
- internal knowledge retrieval;
- source comparison.

### Track C — Creative / Production Agent

Examples:

- content production preflight;
- audio/video project organizer;
- publishing workflow;
- media asset validation.

### Track D — Technical / Engineering Agent

Examples:

- maintenance evidence assistant;
- incident/fault handover;
- technical diagnostic intake;
- software release assistant.

### Track E — Software / Builder Agent

Examples:

- repository maintenance agent;
- issue-to-change workflow;
- code review assistant;
- release verification agent.

### Track F — Personal Operating Agent

Examples:

- knowledge/project system;
- recurring planning/review;
- personal research workflow.

---

## Capstone build sequence

### 1. Real problem

Write:

```text
USER
PROBLEM
CURRENT PROCESS
DESIRED OUTCOME
WHY IT MATTERS
```

### 2. Acceptance

Define observable proof.

### 3. Source of truth

List each mutable meaning and its owner.

### 4. Smallest architecture

Use Module 13.

Do not begin with multi-agent.

### 5. Project instructions

Create/review root `AGENTS.md`.

### 6. Skill

Create or reuse a Skill only for repeated HOW.

### 7. Tools

Reuse native/dedicated capabilities before building integrations.

### 8. Code

Use a coding agent to build only what remains missing.

Inspect the diff and tests.

### 9. Eval set

Include:

- happy path;
- missing information;
- edge/neighbor case;
- known failure;
- untrusted input where relevant.

### 10. Failure drill

Deliberately break one layer and diagnose it.

### 11. Safety / authority

Map real consequences.

### 12. Production plan

Define what must be true for real use.

### 13. Architecture explanation

Explain the system to another person without AI assistance.

---

## Evidence folder

Keep a capstone evidence folder:

```text
outputs/capstone/
├── architecture.md
├── acceptance.md
├── eval-results.md
├── failure-drill.md
├── operating-notes.md
└── demo-evidence/
```

Do not duplicate source-system state into this folder.

Keep only proof and derived artifacts.

---

## Demonstration

Your final demonstration should show:

```text
real input
→ agent reasoning/tool use
→ authoritative data interaction
→ output/action
→ verification
```

Avoid a slide-only demo.

Show the system working.

## Verification

Use [Capstone Verification Rubric](../rubrics/capstone-verification-rubric.md).

## Pass condition

The capstone solves a real problem, survives representative tests, has understandable architecture, and can be operated/debugged by the learner rather than only by the AI that built it.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [15. Multi-agent systems](15-multi-agent-systems.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
