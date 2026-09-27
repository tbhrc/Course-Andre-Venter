# Lab 15 — Harness Playground: Pi + DeepSeek Harness

## Objective

Use two current harnesses to make the **harness layer itself** visible.

This lab complements [Module 15 — Multi-Agent Systems](../course/15-multi-agent-systems.md).

Read [Current Practice Harnesses](../knowledge/current-practice-harnesses.md) and verify the official tool documentation before installation.

Use only a disposable practice repository. Do not use real client data, production credentials or consequential write access.

## Part A — One-agent baseline in Pi

Choose one small repository task.

Example:

> Read a small JSON file, identify incomplete records, produce a Markdown summary, and verify the output.

Before extending Pi:

1. run the task with one agent;
2. record the instructions/context it received;
3. inspect its available tools;
4. note session/state behaviour;
5. inspect the actual files changed;
6. verify the result.

Record:

```text
Outcome:
Tool surface:
Instructions:
State/session behavior:
Evidence:
Failure points:
```

This is your baseline.

## Part B — Extend Pi deliberately

Add **one** useful extension to the learning environment.

Examples:

- one Skill;
- one prompt template;
- one reviewed extension/package;
- one specialist/sub-agent capability if the task genuinely benefits.

Before adding it, write:

> What exact limitation of the one-agent baseline is this extension intended to solve?

Then rerun the same or a directly comparable task.

Compare quality, latency, token/cost if visible, complexity, debugging clarity and failure isolation.

If the extension adds complexity without material value, remove it.

## Part C — Explore DeepSeek Harness modes

Use the current official DeepSeek Harness developer preview.

Run the same bounded task in two materially different modes when available.

A useful comparison is `Minimal` vs `Standard`, or `Standard` vs `Creator`.

Inspect exposed tools, plugins, session/state behaviour, sandbox/runtime boundary, Skill support, loop behaviour, observability, and how easy it is to add or remove capability.

Do not merely record which mode felt smarter. Record what architectural change produced the difference.

## Part D — Multi-agent experiment

Only after the one-agent baseline exists, design one small split.

Example:

```text
manager
├── evidence specialist
└── verifier
```

or:

```text
research specialist A
research specialist B
→ manager join
```

Use whichever harness currently makes that experiment practical.

Do not force both harnesses into identical orchestration APIs.

The comparison is conceptual: how is the specialist defined, how is context passed, who owns final output, where is shared state, how is failure surfaced, and what did the extra agent improve?

## Part E — Harness comparison

Create `work/15-harness-comparison.md`.

| Dimension | Pi | DeepSeek Harness |
|---|---|---|
| Core philosophy | | |
| Default tool surface | | |
| Skills / reusable instructions | | |
| Extensions / plugins | | |
| Sessions / state | | |
| Sandbox/runtime | | |
| Multi-agent path | | |
| Observability | | |
| Ease of modification | | |
| Best learning use | | |

Then answer:

1. Which harness made the agent loop easier to understand?
2. Which made extension/composition easier to understand?
3. Which extra capability actually improved the task?
4. Which addition should be removed under KISSS?
5. What principle transferred cleanly between both harnesses?

## Pass condition

You can explain the difference between **the model** and **the harness**, show what changed when the harness changed, and justify any multi-agent capability with evidence rather than novelty.
