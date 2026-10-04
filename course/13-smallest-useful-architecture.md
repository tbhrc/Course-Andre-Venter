# Module 13 — Architect the Smallest Useful Agentic System

## Objective

Turn a real problem into the **smallest complete architecture that proves value**.

Architecture is not the art of adding components.

It is the discipline of deciding what must exist, who owns truth, how control/data flow, what can fail, and what evidence proves the system works.

---

## 1. Freeze the outcome

Start with:

```text
USER / BUSINESS OUTCOME
What becomes observably better?

ACCEPTANCE
What evidence proves it?
```

Bad:

> Build an advanced AI platform.

Better:

> Given a customer request, retrieve the current account record, produce a compliant response draft, and save the draft to the existing CRM without changing customer state.

The second statement can be architected.

---

## 2. Default architecture order

Use this default:

```text
capable model
→ clear project instructions
→ relevant context/files
→ reusable Skill
→ existing native/dedicated tool
→ direct API / MCP only when needed
→ small adapter/code only when needed
→ durable state/database only when needed
→ multi-agent/graph only when needed
```

This is a search order, not a mandatory stack.

At every step ask:

> Can the existing layer already solve this cleanly?

---

## 3. Reuse before adding

Before proposing a component, inspect:

- existing system of record;
- existing connector/native integration;
- existing Skill;
- existing API;
- existing repository/runtime;
- existing platform capability;
- existing auth/identity;
- existing observability.

Infrastructure already operating reliably is reusable capital.

---

## 4. One owner for each durable truth

For every material state:

```text
meaning
→ owner
→ read path
→ write path
→ verification
```

Avoid architecture diagrams that show "database" without saying what it owns.

---

## 5. Separate reasoning from mechanics

A useful architecture often has:

```text
AI
→ semantic judgement / interpretation / planning

deterministic code
→ exact transformation / validation / protocol mechanics

source system
→ authoritative mutable state
```

Do not force semantic judgement into brittle code.

Do not ask a model to perform exact deterministic mechanics that code can do better.

---

## 6. Proof-first vertical slice

Do not build every future layer first.

Prove:

```text
one real input
→ one agent
→ required source/tool
→ useful output/action
→ verification
```

Then harden what the proof reveals.

---

## 7. Architecture components

For each component record:

- responsibility;
- owner;
- input;
- output;
- tools;
- authority;
- state read/write;
- failure surface;
- verification.

If two components have the same owner, same state, same authority and same job, ask whether they should be collapsed.

---

## 8. Data flow

Trace:

```text
input
→ retrieval
→ reasoning
→ tool/action
→ authoritative state
→ output
→ verification
```

Do not leave hidden copies of mutable state along the path.

---

## 9. Control flow

Identify who chooses each transition:

```text
code?
model?
human?
external event?
```

Stable policy/routing often belongs in deterministic logic.

Open-ended semantic decisions often belong with the model.

Consequential final decisions may belong with a human.

---

## 10. Failure and recovery

For every material step ask:

- what can fail?
- can it be retried?
- could retry duplicate an external action?
- what is the known-good state?
- can the workflow resume?
- what evidence tells us it failed?

Architecture without recovery thinking is incomplete for production work.

---

## 11. KISSS architecture pass

Apply:

```text
DELETE
→ COLLAPSE
→ REUSE
→ DIRECT
→ only then ADD
```

Examples:

### DELETE
Remove a dashboard no one needs.

### COLLAPSE
One agent can own two steps that share the same instructions, state and authority.

### REUSE
Use the existing CRM connector instead of building another customer database adapter.

### DIRECT
Call the authoritative API directly rather than through three internal hops.

### ADD
Add a new service only when the requirement survives all earlier tests.

---

## 12. When code is earned

Add code when you need:

- exact repeated transformation;
- API/tool integration;
- validation;
- durable application logic;
- runtime/service;
- measurable performance.

Do not add code merely to make a workflow feel engineered.

---

## 13. When a database is earned

Add/use durable database state when:

- mutable records need a transactional owner;
- multiple users/processes share state;
- structured querying matters;
- concurrency/integrity matters;
- application state must persist authoritatively.

Do not use agent memory as a transactional database.

---

## 14. When multi-agent is earned

Keep one agent when one owner, one authority boundary and one coherent loop can finish reliably.

Split when there is a material reason such as:

- distinct specialist instructions/tools;
- distinct authority boundary;
- independent verification;
- genuinely independent parallel work;
- branch-specific ownership;
- isolation/recovery requirements.

Multi-agent comes in Module 15.

---

## 15. Proof criteria

Architecture should define terminal evidence.

Example:

```text
SUCCESS
- correct source record retrieved
- required output created
- authoritative system updated if intended
- representative eval passed
- no unrelated state changed

FAILURE
- exact failed step identified
- no ambiguous partial write
- recoverable state preserved
```

---

## Practical work

Complete:

1. [KISSS Architecture Lab](../labs/13-kisss-architecture-lab.md)
2. [Architecture Proof Template](../templates/architecture-proof-template.md)

## Pass condition

You can design a complete architecture, explain why each component exists, name every authoritative owner, show the data/control flow, and remove any component that does not materially improve the proof.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [14. Capstone build](14-capstone.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
