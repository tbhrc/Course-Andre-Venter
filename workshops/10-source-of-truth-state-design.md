# Workshop 10 — Source of Truth and State Design

## Objective

Design the state model for one small agentic workflow.

## Step 1 — Choose a workflow

Examples:

- candidate screening;
- sales follow-up;
- maintenance case;
- content publishing;
- support ticket;
- research brief;
- code-change workflow.

## Step 2 — List meanings, not tools

Create a table:

| Meaning | Changes? | Current owner | Desired owner |
|---|---:|---|---|
| customer email | yes | email service | email service |
| opportunity stage | yes | CRM | CRM |
| reusable sales method | rarely | unclear | Skill |
| working analysis | temporary | local work | work/ |

Do not begin by choosing a database.

## Step 3 — Classify

For each item choose:

```text
CONTEXT
MEMORY
AUTHORITATIVE STATE
REFERENCE DATA
WORKING DATA
DERIVED OUTPUT
```

## Step 4 — Resolve duplicates

Find any meaning stored in more than one place.

Ask:

- which copy can change?
- which owner should win?
- can the duplicate become a link/reference/derived summary instead?

## Step 5 — Define retrieval

For every live-state question:

```text
question
→ owner
→ retrieval method
→ freshness requirement
```

## Step 6 — Define mutation

For every write:

```text
intended change
→ authoritative owner
→ tool/API
→ permission
→ verification
```

## Step 7 — Derived memory

Identify anything worth remembering for continuity.

Then state explicitly:

> This memory is advisory/derived and does not override the source of truth.

## Step 8 — Diagram

```text
user/agent
   ↓
context
   ↓
reasoning
   ↓
retrieve source truth
   ↓
tool/action
   ↓
authoritative state
   ↓
verification
   ↓
derived summary/memory if useful
```

## Completion artifact

Create `work/10-state-design.md`.

## Pass condition

Every material mutable meaning has exactly one authoritative owner or an explicitly unresolved owner that must be decided.
