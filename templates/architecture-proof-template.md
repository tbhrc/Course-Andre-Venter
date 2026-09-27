# Architecture Proof Template

## Problem

<one sentence>

## Observable outcome

<what must become true>

## Users / actors

- ...

## Existing reusable capability

- ...

## Recommended smallest architecture

```text
<input>
→ ...
→ <verified outcome>
```

## Component contracts

| Component | Responsibility | Input | Output | Authority/tools | State owner |
|---|---|---|---|---|---|

## Systems of record

| Meaning | Authoritative owner | Read path | Write path | Verification |
|---|---|---|---|---|

## Control decisions

| Decision | Owner: code/model/human | Why |
|---|---|---|

## Failure and recovery

| Failure | Detection | Recovery / terminal path |
|---|---|---|

## Real boundaries

- secrets:
- privacy:
- consequential actions:
- irreversible actions:

## Phase 0 — proof

<smallest vertical slice>

## Phase 1 — production

<only hardening required for real use>

## Phase 2 — scale

<optional, triggered by observed need>

## Acceptance evidence

- [ ] ...
- [ ] ...

## KISSS pass

- DELETE:
- COLLAPSE:
- REUSE:
- DIRECT:
- ADD only if earned:

## Architecture explanation

Explain the system in fewer than 150 words without naming unnecessary implementation detail.
