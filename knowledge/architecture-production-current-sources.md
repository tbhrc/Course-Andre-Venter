# Architecture, Multi-Agent and Production — Current Sources

This page is a **live-source map**, not a copied framework manual.

## OpenAI architecture sources

- Agents SDK overview: https://developers.openai.com/api/docs/guides/agents/sdk
- Define agents: https://developers.openai.com/api/docs/guides/agents/define-agents
- Run agents: https://developers.openai.com/api/docs/guides/agents/running-agents
- Orchestration and handoffs: https://developers.openai.com/api/docs/guides/agents/orchestration
- Integrations and observability: https://developers.openai.com/api/docs/guides/agents/integrations-observability
- API deployment checklist: https://developers.openai.com/api/docs/guides/deployment-checklist
- Production best practices: https://developers.openai.com/api/docs/guides/production-best-practices

## Current hands-on harness sources

- Pi: https://pi.dev/
- DeepSeek Harness developer preview: https://www.deepseek.com/harness/en/
- DeepSeek Harness source: https://github.com/deepseek-ai/deepseek-harness

These are practice environments, not permanent course dependencies. See [Current Practice Harnesses](current-practice-harnesses.md).

## Durable concepts

Learn these regardless of current SDK/API details:

```text
one agent first
→ explicit outcome/state/tool boundaries
→ prove a vertical slice
→ split only when ownership, authority, parallelism or independent verification earns it
→ observe runs
→ test representative behaviour
→ harden only proven failure surfaces
```

## Current multi-agent concepts

Current OpenAI guidance distinguishes two useful patterns:

```text
HANDOFF
specialist takes ownership of the next branch

AGENT AS TOOL
manager remains responsible for the final result
and calls specialists as bounded capabilities
```

Exact SDK method names and beta product features can change. Verify them live.

## Course rule

Do not teach multi-agent as a maturity badge.

Teach:

> What specific limitation of one well-engineered agent is solved by adding this agent/node/graph edge?

If the answer is unclear, keep one agent.

## Production rule

Production readiness is not one checklist item.

It includes, where material:

- correctness/evals;
- observability/tracing;
- security and secret handling;
- state/source-of-truth integrity;
- idempotency and recovery;
- rate limits;
- latency;
- cost;
- model/tool/version changes;
- backups/checkpoints;
- user experience;
- rollback/fallback;
- support/ownership.

Verify current provider-specific requirements from current official docs.
