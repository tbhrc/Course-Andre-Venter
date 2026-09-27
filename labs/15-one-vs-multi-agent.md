# Lab 15 — One Agent vs Multi-Agent

## Objective

Prove whether a problem actually earns multi-agent architecture.

## Scenario

Build a research brief from three independent source families.

### Option A

One research agent:
- searches all source families;
- compares evidence;
- produces final brief.

### Option B

Manager:
- specialist A researches source family A;
- specialist B researches source family B;
- specialist C researches source family C;
- manager joins evidence and produces final brief.

## Step 1 — Define acceptance

Use the same acceptance criteria for both options.

Include:

- factual support;
- source provenance;
- contradiction handling;
- completion time;
- token/cost if measurable;
- debugging clarity.

## Step 2 — Design one-agent baseline

Do not skip this.

Write the one-agent contract first.

## Step 3 — Identify the claimed multi-agent advantage

Choose a real reason:

- parallelism;
- context separation;
- specialist tools;
- independent verification.

If the reason is merely:

> Multi-agent is more advanced

stop.

## Step 4 — Define specialist contracts

For each specialist:

- job;
- input;
- output;
- tool access;
- state read/write;
- stop condition.

## Step 5 — Define join

How are results combined?

Who owns conflicting evidence?

## Step 6 — Failure paths

What happens if one specialist:

- times out;
- returns weak evidence;
- duplicates another specialist;
- fails completely?

## Step 7 — Compare

Run or simulate both versions.

Record:

| Dimension | One agent | Multi-agent |
|---|---|---|
| quality | | |
| latency | | |
| cost/tokens | | |
| complexity | | |
| failure isolation | | |
| observability | | |

## Step 8 — Decision

Choose the simpler architecture unless the multi-agent version shows material value.

## Completion artifact

Create `work/15-one-vs-multi-agent.md`.

## Pass condition

Your decision is based on evidence/architecture fit rather than preference for a more complex system.
