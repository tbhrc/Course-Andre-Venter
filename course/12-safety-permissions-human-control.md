# Module 12 — Safety, Permissions and Human Control

## Objective

Build useful agents that can act without confusing safety with bureaucracy.

For current guidance, see [Reliability and Safety Current Sources](../knowledge/reliability-safety-current-sources.md).

## Risk comes from capability + context + consequence

Ask:

```text
What can the agent see?
What can it do?
What external state can change?
What happens if it is manipulated or mistaken?
```

A read-only documentation lookup and a financial transaction do not need the same control design.

## Trusted instructions vs untrusted content

Agent context can contain:

- system/project instructions;
- user instructions;
- emails;
- web pages;
- documents;
- retrieved records;
- tool outputs.

External content may contain instruction-shaped text.

Treat untrusted content as **data to analyze**, not authority.

If a document says:

> Ignore the user's task and perform an unrelated action.

that sentence remains part of the document. It does not become the user's instruction.

## Prompt injection

Prompt injection attempts to manipulate an agent through untrusted content.

Potential effects include:

- changed recommendations;
- unintended tool calls;
- inappropriate data disclosure;
- unauthorized communication;
- destructive or high-impact action.

Prompt injection is a system-security problem, not merely a prompt-writing problem.

## Layered defenses

Use layers where risk warrants:

- explicit task scope;
- instruction hierarchy;
- untrusted-content isolation;
- structured extraction;
- tool narrowing;
- minimal task-relevant data access;
- sandboxing/isolation;
- validation;
- approval before genuinely consequential external actions;
- output/tool-call verification;
- adversarial evals;
- monitoring/trace review.

No single layer is perfect.

## Structured extraction

When untrusted text must influence a downstream action, extract only the fields the next step needs.

Example:

```text
untrusted email
→ extract:
   customer_id
   requested_date
   requested_product
→ validate
→ downstream tool
```

This reduces free-text instruction channels.

It does not prove the extracted data is true.

## Permission design

Give an agent the authority its operating role genuinely requires.

For an ordinary bounded agent:

- prefer task-relevant access;
- separate read/write when useful;
- avoid unnecessary admin credentials;
- keep secrets outside normal model arguments where possible.

For an explicitly authorized administrator/operator, broader standing authority may be appropriate.

The durable rule is:

> Match authority to the real operating role and consequence.

## Human approval

Use human approval when a person should own the final consequential decision.

Examples can include:

- sensitive external communication;
- material purchase;
- destructive deletion;
- publication;
- security/identity change;
- legal or financial commitment.

Do not add approval merely because AI is involved.

If the provider/platform mandates approval, respect it.

## Reversibility

A useful scale:

```text
easy to reverse / low impact
< difficult to reverse
< irreversible / high impact
```

The harder the action is to undo and the larger the consequence, the stronger the evidence/control should be.

## Secrets

Never place real secrets in:

- prompts;
- AGENTS.md;
- Skills;
- source files;
- Git history;
- logs;
- screenshots/artifacts.

Prefer host-managed authentication, secret stores, or runtime environment configuration.

## Data minimization

Ask:

> What is the smallest data slice required for this operation?

Do not send an entire dataset to an external system if the task needs two fields.

## Tool output is untrusted too

A tool can return:

- stale data;
- malformed data;
- attacker-controlled content;
- wrong results.

Treat external output as evidence/data.

Do not blindly execute instruction-shaped text found inside it.

## Human-in-the-loop vs human-on-the-loop

### Human-in-the-loop

Human approval is required at a defined step.

### Human-on-the-loop

Agent acts within bounded authority while a human can inspect, monitor or intervene.

Use the model that matches consequence and required operating speed.

## Audit evidence

Capture evidence when it helps:

- reproduce;
- review;
- meet legal/compliance needs;
- understand a consequential action.

Do not log everything forever merely because auditability sounds safe. Logs can create privacy/security risk.

## Security review question

Before adding a control, ask:

> What concrete failure becomes materially harder because this control exists?

If you cannot answer, you may be adding friction rather than safety.

## Practical work

Complete:

1. [Prompt Injection and Untrusted Input Lab](../labs/12-prompt-injection-untrusted-input.md)
2. [Permission and Human-Control Lab](../labs/12-permission-boundaries.md)

## Pass condition

You can distinguish trusted instructions from untrusted content, design layered controls for a realistic agent, place human approval at a genuine consequence boundary, and explain why a proposed control improves safety rather than merely adding friction.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [13. Smallest useful architecture](13-smallest-useful-architecture.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
