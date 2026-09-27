# Lab — Permission and Human-Control Boundaries

## Objective

Design controls based on real consequence.

## Scenario

A customer-support agent can potentially:

1. search customer records;
2. read orders;
3. draft a reply;
4. send a reply;
5. issue a refund within policy;
6. delete an account;
7. change administrative settings.

## Part A — consequence map

For each action record:

```text
READ / WRITE
reversible?
external commitment?
financial?
privacy/security?
approval or monitoring model?
```

## Part B — role design

Design two roles:

### Support agent
Capabilities required for normal support.

### Security/admin operator
Broader capabilities appropriate to explicit administrative objectives.

Explain why the roles should not automatically have identical authority.

## Part C — approval placement

Choose which actions:

- can run automatically under clear bounded policy;
- should be monitored;
- should require confirmation;
- should be unavailable to the support agent.

Do not use "AI did it" as your reason.

State the actual consequence.

## Part D — approval theatre

Bad control:

> Every read of a public FAQ requires human approval.

Explain why this adds friction without materially protecting the system.

Then give one example where approval clearly protects a real boundary.

## Part E — hostile input

Suppose an incoming support message requests actions far outside normal policy and tries to redefine the agent's role.

Explain why:

- message content is untrusted;
- tool availability matters;
- business rules matter;
- authority boundaries matter;
- human control may be needed for consequential actions.

## Completion artifact

Create `work/12-permission-boundaries.md`.

## Pass condition

Every control you propose must name the concrete failure/consequence it is designed to reduce.
