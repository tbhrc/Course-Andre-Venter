# Current Practice Harnesses — September 2026

**Status:** current-tool practice layer  
**Last verified:** 27 September 2026

The course fundamentals are deliberately durable. This page is deliberately **not**.

Agent harnesses change quickly, so use current tools to practise the principles while treating exact commands, package names, modes and feature sets as volatile.

## Why practise in a harness?

A harness is the operating environment around the model:

```text
model
+ instructions
+ context
+ tools
+ Skills
+ state/session handling
+ execution loop
+ sandbox/runtime
+ observability
= working agent environment
```

The best way to understand that layer is to operate one, strip it down, extend it, and compare what changes.

## Pi

Official site: https://pi.dev/

Pi currently positions itself as a **minimal agent harness** that can be adapted through extensions, Skills, prompt templates, themes and packages.

That makes Pi useful for learning because the harness does not hide every architectural choice behind a large platform.

At the time of verification, Pi intentionally keeps the core small and does not treat features such as sub-agents or plan mode as mandatory built-ins; those capabilities can be added through the extension/package model when they actually help.

### What to learn with Pi

Use Pi to practise:

1. one capable agent with a small tool surface;
2. project instructions and Skills;
3. session/context behaviour;
4. extending the harness only when a real gap appears;
5. comparing one-agent work with an added specialist/sub-agent extension;
6. inspecting whether the extra orchestration actually improves the result.

The lesson is not that Pi is permanently the best harness. The lesson is that a small harness makes the architecture visible enough to understand.

## DeepSeek Harness

Official developer preview: https://www.deepseek.com/harness/en/

Source: https://github.com/deepseek-ai/deepseek-harness

DeepSeek Harness currently describes itself as a composable agent harness where capabilities are mounted as plugins.

At the time of verification, its plugin surface includes models, tools, Skills, sessions, sandboxes, storage, loops, scheduling and UI.

Its current modes include:

- **Standard** — full coding-agent capability;
- **Code** — lets the model orchestrate tool use through code;
- **Minimal** — deliberately reduced tool surface;
- **Creator** — runtime inspection and plugin/preset experimentation.

### Why this is useful for learning

DeepSeek Harness exposes a different lesson from Pi:

> What happens when the harness itself becomes a composable plugin system?

Use it to compare minimal vs full tool surfaces, agent-loop design, plugins/modules vs hard-coded features, state/session ownership, sandbox boundaries, reusable Skills, custom presets/modes, and useful vs decorative complexity.

## Current quick starts

Verify the official pages before running these because the commands may change.

### Pi

Official installation options are published at https://pi.dev/.

### DeepSeek Harness

Current official developer-preview quick start:

```bash
npx @deepseek-ai/dsh web
```

Source install:

```bash
git clone https://github.com/deepseek-ai/deepseek-harness
```

## Maintenance contract

Before teaching or using these specific harnesses:

1. open the official source;
2. confirm the project is still active;
3. confirm current install/launch instructions;
4. confirm the current extension/plugin model;
5. update this file only when the practical learning path materially changes.

Do not rewrite the stable course doctrine merely because a harness changes.

```text
durable principle
→ current tool used to practise it
→ tool changes
→ update practice layer
→ principle remains unless evidence changes it
```
