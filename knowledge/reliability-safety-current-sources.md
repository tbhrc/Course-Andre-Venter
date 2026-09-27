# Reliability, Evals and Agent Safety — Current Sources

This page is a **live-source map**, not a copied product manual.

## OpenAI reliability / eval sources

- Evals learning hub: https://developers.openai.com/learn/evals
- Evaluation best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- Getting started with datasets/evaluation: https://developers.openai.com/api/docs/guides/evaluation-getting-started
- Working with evals: https://developers.openai.com/api/docs/guides/evals

## OpenAI agent-safety sources

- Safety in building agents: https://developers.openai.com/api/docs/guides/agent-builder-safety
- Understanding prompt injections: https://openai.com/safety/prompt-injections/
- Designing agents to resist prompt injection: https://openai.com/index/designing-agents-to-resist-prompt-injection/

## Durable concepts

Learn these regardless of product surface:

```text
reliability
= explicit expected behaviour + representative cases + evidence

eval
= structured test of behaviour against criteria

regression
= behaviour that used to work but no longer does

prompt injection
= untrusted content attempts to manipulate the agent's instructions/actions

human control
= place human confirmation/oversight where consequence justifies it

source of truth
= the authoritative owner of mutable state
```

## Current-product rule

OpenAI's evaluation products and safety tooling evolve. Verify the current recommended surface before implementation.

Do not hard-code the course to one dashboard, API object name, grader product or dated Agent Builder workflow.

The durable method is:

```text
define expected behaviour
→ build representative cases
→ run
→ inspect failures
→ change smallest cause
→ rerun old failures + neighboring cases
→ preserve useful regression evidence
```

## Safety rule

Prompt injection is not solved by one filter.

Use layered design:

- distinguish trusted instructions from untrusted content;
- minimize unnecessary access;
- constrain data flow where practical;
- use structured outputs/contracts;
- isolate risky execution;
- verify tool arguments/results;
- place approvals at real consequential boundaries and obey provider-required approvals;
- test adversarial/untrusted cases;
- monitor and improve from observed failures.

A standard protocol, trusted model or connected tool does not eliminate the need for system design.
