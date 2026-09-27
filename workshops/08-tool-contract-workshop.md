# Workshop 08 — Design Your First Tool Contract

## Objective

Design one bounded model-callable tool from a real task.

Do not build it until the contract is clear.

## Step 1 — Choose an action

Examples:

- look up a customer by email;
- create a maintenance ticket;
- search a repository;
- get a public weather observation;
- retrieve an invoice status;
- list files in a known folder.

## Step 2 — Identify the owner

Write:

```text
Authoritative system:
Existing dedicated integration:
If none, API owner:
```

If a dedicated authorised tool already exists, explain why a new tool is or is not still justified.

## Step 3 — Define consequence

Choose:

```text
READ
WRITE
DESTRUCTIVE / HIGH-CONSEQUENCE
```

State what real-world state could change.

## Step 4 — Design schema

Example:

```json
{
  "name": "find_customer",
  "arguments": {
    "email": "string"
  }
}
```

Then challenge it:

- Is email really required?
- Should arbitrary query strings be allowed?
- Is tenant/account context required?
- What should happen on no match?
- What should happen on multiple matches?

## Step 5 — Define errors

List expected error categories:

- invalid input;
- unauthorized;
- forbidden;
- not found;
- conflict;
- rate limit;
- upstream failure.

## Step 6 — Define verification

For reads:

> What evidence proves the returned record is the intended one?

For writes:

> What authoritative target do you inspect after the call?

## Step 7 — Retry/idempotency

Ask:

> If the call times out after the server processed it, what happens if we retry?

If duplicate action matters, design a strategy before implementation.

## Step 8 — KISSS review

Could the task be solved by:

- an existing tool?
- a smaller API wrapper?
- one less argument?
- a read-only operation?

## Completion artifact

Create:

```text
work/08-tool-contract.md
```

Include the final tool contract and one paragraph explaining why its scope is not broader than necessary.
