# Lab 13 — KISSS Architecture

## Objective

Take an intentionally over-engineered proposal and reduce it to the smallest architecture that still proves the outcome.

## Scenario

Outcome:

> Turn incoming customer requests into a verified draft response using the current CRM record and company response rules.

Proposed architecture:

```text
email webhook
→ queue
→ intake microservice
→ classification agent
→ customer lookup service
→ copied customer database
→ research agent
→ policy agent
→ draft agent
→ reviewer agent
→ workflow database
→ analytics database
→ custom dashboard
→ response API
→ CRM adapter
→ CRM
```

## Step 1 — Freeze the outcome

What must actually happen?

List only observable acceptance evidence.

## Step 2 — DELETE

Which components do not help prove the outcome?

Do not preserve them because they sound useful later.

## Step 3 — COLLAPSE

Which components share:

- owner;
- instructions;
- authority;
- state;
- execution loop?

Could one capable agent perform them?

## Step 4 — REUSE

Assume:

- the CRM already owns customer state;
- a native CRM connector exists;
- email is already connected;
- response policy exists as a project Skill.

What custom infrastructure disappears?

## Step 5 — DIRECT

Draw the shortest viable flow.

A possible result:

```text
incoming request
→ one response agent
   ↳ response-policy Skill
   ↳ CRM read tool
→ draft response
→ verification
→ human/user decides whether to send
```

Your answer may differ, but every additional component must earn its existence.

## Step 6 — Decide state

What state needs to persist?

Do not add a new workflow database unless the workflow actually needs one.

## Step 7 — Failure design

Handle:

- CRM lookup fails;
- customer not found;
- policy missing;
- draft fails acceptance;
- external tool unavailable.

## Step 8 — Proof

Define one representative end-to-end case.

## Completion artifact

Create `work/13-architecture.md` with:

- original architecture;
- deletions;
- collapses;
- reused capability;
- direct final architecture;
- state ownership;
- failure/recovery;
- proof case;
- KISSS verdict.

## Pass condition

You can defend every remaining component with a concrete requirement.
