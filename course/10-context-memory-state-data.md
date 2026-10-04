# Module 10 — Context, Memory, State and Data

## Objective

Understand what the agent can see now, what persists, and which system actually owns truth.

## Context

Context is information available to the model for the current decision:

- current request;
- project instructions;
- conversation;
- retrieved files;
- tool results;
- selected memory;
- live state fetched from a system.

Context is temporary input to reasoning.

More context is not automatically better. It can be stale, duplicated, contradictory, irrelevant or untrusted.

## Memory

Memory is retained information that may influence future work.

Memory supports continuity, but it is **not automatically current truth**.

Example:

```text
memory:
"Customer was considering Plan A last month."

CRM:
"Customer signed Plan B yesterday."
```

The CRM wins for current commercial state.

## State

State is the current value of something in a system.

Examples:

- task status;
- selected configuration;
- current branch;
- workflow stage;
- opportunity stage;
- machine alarm state.

State normally belongs to the system whose transactional purpose owns it.

## Data

Data is material a system stores or processes:

- documents;
- messages;
- database rows;
- measurements;
- logs;
- API responses;
- transcripts.

Data has provenance. Ask:

> Where did this come from, when, and who owns the authoritative version?

## Source of truth

A source of truth is the authoritative owner for a specific piece of mutable meaning.

```text
Git → repository history
CRM → customer/opportunity state
calendar → scheduled event state
email service → sent/received message state
database → application records
machine controller → current machine state
```

Do not create another database merely because an agent wants convenient memory.

## One meaning, one owner

Avoid:

```text
customer status in CRM
+ copied customer status in memory
+ copied customer status in Markdown
+ copied customer status in spreadsheet
```

Prefer:

```text
CRM owns current customer status
→ agent retrieves it when needed
→ other artifacts reference or summarize it
```

A summary is not a competing system of record.

## Derived memory

Derived memory can preserve:

- prior observations;
- stable preferences;
- useful summaries;
- lessons;
- routing hints.

Treat it as:

```text
useful continuity
≠ guaranteed live state
```

When current truth matters, retrieve the owner.

## Provenance

For material data, preserve enough provenance to identify:

- source;
- timestamp/period;
- record/document identity;
- transformation;
- uncertainty where relevant.

## Retrieval

Retrieve the smallest relevant truth:

```text
request
→ identify owner
→ retrieve relevant record/file
→ reason
→ verify against owner when material
```

## Staleness

Ask:

> Could this have changed since it was stored?

High-staleness examples:

- current account/task state;
- prices;
- schedules;
- regulations;
- software capabilities.

Lower-staleness examples:

- historical decision;
- immutable source document;
- stable procedure.

## Context window is not a database

A model context window is working memory for a reasoning episode.

If state must survive and be authoritative, store it in the system that owns that state.

## Files vs database

Use files when human-readable/versioned project knowledge is primary and concurrency/volume is modest.

Use a database when records mutate frequently, structured querying/concurrency/transactions materially matter, or the application itself owns changing state.

Let the requirement earn the database.

## State transitions

Define:

```text
current state
→ allowed transition
→ action
→ resulting state
→ verification
```

## Design rule

```text
meaning
→ canonical owner
→ retrieval path
→ permitted mutation path
→ verification path
→ derived memory only if useful
```

## Practical work

Complete [State and Source-of-Truth Workshop](../workshops/10-source-of-truth-state-design.md).

## Pass condition

You can distinguish context, memory, state and data, assign one authoritative owner to material mutable truth, and explain when the agent must retrieve live state rather than trust remembered context.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [11. Debugging and evaluations](11-debugging-and-evals.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
