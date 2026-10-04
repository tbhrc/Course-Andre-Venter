# Module 15 — Multi-Agent Systems

## Objective

Learn when multiple agents improve a system—and when they are merely theatre.

The default remains:

> One capable agent with the right instructions, context and tools.

Split only when the added boundary solves a real problem.

For current framework details, see [Architecture and Production Current Sources](../knowledge/architecture-production-current-sources.md). For hands-on harness practice, also use [Current Practice Harnesses](../knowledge/current-practice-harnesses.md).

---

## 1. One loop before a graph

A single agent can already:

- reason;
- use multiple tools;
- retrieve different sources;
- execute several steps;
- iterate until a stop condition.

Do not split one coherent loop into multiple agents just because the workflow has several steps.

---

## 2. Reasons to add another agent

A split may be justified by:

### Specialist instructions/tools

The specialist genuinely needs a different job and context.

### Authority boundary

Different work requires meaningfully different permissions.

### Independent verification

A reviewer should inspect output without inheriting all producer assumptions.

### Parallelism

Independent workstreams can run concurrently and later join.

### Branch ownership

A specialist should take over a distinct conversation/workflow branch.

### Isolation/recovery

A failure should be contained or retried independently.

---

## 3. Two common orchestration patterns

### Handoff

```text
router/agent
→ specialist takes ownership
→ specialist produces the next branch/result
```

Use when the specialist should own that branch.

### Agent as tool / manager pattern

```text
manager agent
├── calls specialist A
├── calls specialist B
└── synthesizes final result
```

Use when one manager should remain responsible for the final answer.

Current OpenAI SDKs support both concepts; verify exact implementation syntax live.

---

## 4. Not every node should be an agent

A graph node may be:

- model agent;
- deterministic function;
- tool;
- validator;
- human checkpoint;
- external event;
- nested workflow.

Use code when the decision is stable and deterministic.

Use a model when semantic judgement is required.

---

## 5. State contract

Shared state should be minimal.

For each field define:

```text
name
owner
type/shape
who may read
who may write
merge rule
durability
```

Avoid passing whole conversation histories between every agent.

Pass references to canonical artifacts/state where practical.

---

## 6. Edges and routing

For every transition define:

- source;
- destination;
- trigger;
- who decides: code/model/human;
- data passed;
- timeout/budget;
- failure path.

Stable routing rules often belong in code.

Semantic routing may belong with the model.

---

## 7. Cycles must be bounded

A retry/repair loop needs:

- success condition;
- max retries/iterations;
- time/token/cost bound where material;
- checkpoint;
- terminal failure/escalation.

Never rely on:

> The agents will know when to stop.

---

## 8. Parallel work

Parallelize only genuinely independent tasks.

Bad:

```text
agent A edits file X
agent B edits same file X
agent C also edits file X
```

Good:

```text
agent A researches source family A
agent B researches source family B
→ join evidence
→ one owner synthesizes
```

Define the join:

- all;
- quorum;
- first success;
- merge;
- best score;
- human choice;
- timeout.

---

## 9. Independent verification

A useful pattern:

```text
producer
→ verifier
→ accept
   or
→ repair
   or
→ terminal failure / human
```

Independent review is useful when the consequence/quality requirement earns it.

Do not add a verifier to every trivial task.

---

## 10. Observability

Trace enough to answer:

```text
which agent/node ran?
what input/reference did it receive?
which tools did it call?
why did routing occur?
what state changed?
where did failure originate?
what terminal evidence exists?
```

Use existing runtime tracing before building another observability platform.

---

## 11. KISSS collapse

After drawing the graph:

```text
DELETE unnecessary nodes
COLLAPSE same-owner/same-authority nodes
REUSE native orchestration/tools
DIRECT unnecessary hops
ADD only surviving complexity
```

---

## Practical work

Complete [One Agent vs Multi-Agent Lab](../labs/15-one-vs-multi-agent.md), then use the [Pi + DeepSeek Harness Playground](../labs/15-harness-playground.md) to compare the same principles in current real harnesses.

## Pass condition

You can explain exactly why each additional agent exists, define its contract/state/authority, bound every loop, and show why the multi-agent version is materially better than one well-engineered agent.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [16. Production thinking](16-production-thinking.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
