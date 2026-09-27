# Module 8 — APIs and Tool Calling

## Objective

Understand how an agent moves from **reasoning** to **action**.

By the end of this module you should understand:

- what an API is;
- what a model tool is;
- request/response;
- schemas;
- authentication;
- secrets;
- errors;
- retries;
- idempotency;
- side effects;
- why a callable endpoint is not automatically an appropriate tool.

For current product details, use [APIs, Tools and MCP — Current Sources](../knowledge/apis-tools-mcp-current-sources.md).

---

## 1. API mental model

An API is an interface another program can use.

Think:

```text
consumer
→ defined request
→ system
→ defined response
```

Example:

```text
GET /tasks/42
→ task service
→ 200 + task data
```

The API contract may define:

- method;
- path;
- parameters;
- authentication;
- request body;
- response body;
- error responses;
- rate/spend limits.

---

## 2. Tool mental model

A tool is a capability the model can choose to call.

A useful tool definition tells the model:

```text
NAME
what capability is this?

DESCRIPTION
when should it be used?

INPUT SCHEMA
what arguments are valid?

OUTPUT
what comes back?

SIDE EFFECT
does it read, create, update, delete or spend?
```

The model reasons about **whether and how** to call the tool.

Your application/tool implementation performs the actual deterministic operation.

This matches the principle:

> AI chooses meaning; deterministic tools do the mechanics.

---

## 3. API is not the same as tool

You can call an API directly from ordinary code without any AI.

You can also wrap an API operation as a model-callable tool.

Example:

```text
CRM API:
POST /contacts

Model tool:
create_contact(name, email, company)
```

The tool may:

- validate inputs;
- enforce permissions;
- translate the model's arguments to the API;
- normalize the API response;
- hide irrelevant API complexity.

Do not expose the entire raw API to the model unless the real task needs it.

---

## 4. Tool contract design

Weak tool:

```text
name: do_crm_thing
arguments: anything
```

Strong tool:

```text
name: create_contact
description: Create a CRM contact after identity fields are confirmed.
arguments:
  name: string
  email: string
  company: optional string
```

Good schemas reduce ambiguity.

Do not confuse schema detail with business judgement.

The schema can require `email` to be a string.

It cannot determine whether creating the contact is the right business action unless that decision is encoded elsewhere.

---

## 5. Read vs write tools

Classify tools by consequence.

### Read

Examples:

- search files;
- retrieve CRM contact;
- read calendar;
- inspect repository.

### Write

Examples:

- create contact;
- update opportunity;
- send email;
- create event.

### Destructive / high consequence

Examples:

- delete record;
- transfer ownership;
- publish;
- send money;
- revoke credentials.

The approval/control level should follow the **real consequence**, not the fact that AI is involved.

---

## 6. Authentication

Common concepts:

### API key

A secret credential identifying an application/account.

### Bearer token

A token sent in an authorization header.

### OAuth

A delegated authorization flow allowing a user/app to grant scoped access.

### Session / service identity

An authenticated runtime identity managed by the host/system.

Never teach secrets by pasting real secrets into:

- chat;
- source code;
- GitHub;
- logs;
- screenshots;
- course artifacts.

Use placeholders:

```text
Authorization: Bearer <access-token>
```

---

## 7. Environment variables

Keep runtime configuration and secrets outside reusable source.

Example:

```bash
export DEMO_API_TOKEN="..."
```

Code reads the environment variable.

Repository stores:

```text
DEMO_API_TOKEN=<set-at-runtime>
```

not the real credential.

---

## 8. Request/response

Request:

```text
POST /tasks
Content-Type: application/json

{
  "title": "Inspect pump"
}
```

Response:

```text
201 Created

{
  "id": 42,
  "title": "Inspect pump"
}
```

Ask:

- What does the method imply?
- What changed?
- Which ID became canonical?
- What should the agent keep as evidence?

---

## 9. Errors are part of the contract

Examples:

```text
400
invalid request

401
not authenticated

403
authenticated but not allowed

404
not found

409
state conflict

429
rate limited

5xx
server-side failure
```

Do not memorize the entire HTTP standard.

Learn to inspect:

```text
status
→ error body
→ request
→ actual system state
```

Do not blind-retry every failure.

---

## 10. Retry discipline

Retry only when the failure mode makes a retry sensible.

Potentially retryable:

- temporary network failure;
- timeout;
- some rate-limit/server failures.

Usually not fixed by blind retry:

- invalid schema;
- missing permission;
- wrong identifier;
- rejected business rule.

Before retrying a write, ask:

> Could the first request actually have succeeded?

This leads to idempotency.

---

## 11. Idempotency

Idempotency is about making repeated requests safe or predictable.

Example problem:

```text
create invoice
→ timeout
→ caller cannot tell whether invoice was created
→ retry
→ duplicate invoice
```

An idempotency key or deterministic external identifier can let the server recognize the repeated intent.

You do not need to implement idempotency in every beginner project.

You do need to recognize when duplicate writes would matter.

---

## 12. Source of truth

If the CRM creates contact ID `123`, the CRM owns that contact state.

The agent's chat message:

> Created contact 123.

is evidence/reporting—not the system of record.

Always know:

```text
tool call
→ authoritative external state
→ verification
→ concise evidence returned to agent/user
```

---

## 13. Dedicated tool first

Use this decision order:

```text
capability needed
→ existing dedicated authorised integration?
   YES → use it
   NO  → is a direct API/custom tool small and stable?
          YES → use/build that
          NO / reusable multi-client integration needed
              → consider MCP
```

Do not route Gmail through a generic scraper if an authenticated Gmail integration already exists.

Do not build an MCP server for one trivial local function simply because MCP is fashionable.

---

## 14. Build the smallest tool

Suppose the task is:

> Check whether a maintenance ticket exists.

Do not expose:

```text
run_arbitrary_sql(query)
```

if the real need is:

```text
find_ticket(ticket_id)
```

Smaller tools:

- are easier to describe;
- are easier to authorize;
- reduce ambiguity;
- reduce blast radius;
- simplify verification.

---

## 15. Tool result verification

Transport success is not outcome success.

Example:

```text
tool HTTP call = 200
but result = []
```

This does not prove the requested customer exists.

Verify the provider/business result.

For writes, inspect the authoritative target when material.

---

## Practical work

Complete:

1. [Lab 08 — First API](../labs/08-first-api-lab.md)
2. [Tool contract workshop](../workshops/08-tool-contract-workshop.md)
3. [Tool/API/MCP decision playbook](../playbooks/tool-api-mcp-decision.md)
4. [Prompt — Design a Tool Contract](../prompts/08-design-tool-contract.md)

## Pass condition

You can explain an API request/response, design a bounded tool schema, keep secrets out of source, classify read/write consequence, diagnose basic errors, and decide whether an existing tool or direct API is sufficient.
