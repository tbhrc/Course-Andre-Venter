# André Application — Module 10: State, Memory and Source of Truth

This file personalizes the canonical [Module 10](10-context-memory-state-data.md) for André.

## Machine-state analogy

You already work with systems where the **current machine state** matters more than what someone remembers from yesterday.

Use this mapping:

| Agent concept | Technical-system analogy |
|---|---|
| context | what is visible on the panel right now |
| memory | prior maintenance notes / remembered history |
| authoritative state | live controller / actual machine condition |
| reference data | manual / specification |
| derived summary | technician handover |
| stale context | yesterday's pressure reading |
| provenance | which sensor/log/manual produced the value |

The central rule:

> A note saying the machine was at 110 bar yesterday does not override the live instrument reading today.

The same applies to agents.

## Exercise A — current truth

Scenario:

- a previous note says machine status = `RUNNING`;
- live controller now reports `FAULT`;
- an old handover says `FAULT CLEARED`.

Which one owns current state?

Explain why.

## Exercise B — duplicate truth

Imagine maintenance status exists in:

- technician notebook;
- shared spreadsheet;
- machine controller;
- vendor email.

For each, classify:

```text
AUTHORITATIVE CURRENT STATE
REFERENCE
DERIVED NOTE
COMMUNICATION EVIDENCE
```

Then decide whether any duplicate should be removed or demoted to reference-only.

## Exercise C — agent design

Design a diagnostic assistant where:

```text
manual
= reference knowledge

maintenance history
= historical data

live readings
= current state

agent memory
= continuity only

final vendor handover
= derived output
```

Explain what the agent must retrieve live before making a current-status claim.

## Target

You should be able to say:

> Memory helps me continue the work, but the system that actually owns the changing state wins.
