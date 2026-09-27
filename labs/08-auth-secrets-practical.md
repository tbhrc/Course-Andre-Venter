# Lab — Authentication, Secrets and Permission Boundaries

## Objective

Practise identifying where credentials belong, what authority a tool actually needs, and how to avoid leaking secrets into agent context or repositories.

This lab uses placeholders only. **Never paste a real secret into the course repository.**

---

## Scenario

You need an agent tool that can read maintenance tickets from an external service and optionally create a new ticket.

The external API uses a bearer token.

## Part A — Bad design review

Review:

```python
API_TOKEN = "real-token-value"

def create_ticket(title):
    ...
```

List every problem.

At minimum consider:

- secret committed in source;
- secret visible to anyone reading the repository;
- possible logging/chat exposure;
- unclear scope;
- read and write authority bundled together.

---

## Part B — Environment boundary

Design:

```text
source code
→ reads environment variable name
→ runtime provides secret
→ secret never enters Git
```

Repository may contain:

```text
.env.example
```

with:

```text
MAINTENANCE_API_TOKEN=<set-at-runtime>
```

but not the real value.

---

## Part C — Permission split

You currently have one broad token that can:

- read tickets;
- create tickets;
- delete tickets;
- administer users.

The agent only needs to search tickets.

Question:

> What is the smallest useful authority?

Answer in terms of real capability, not slogans.

Then consider a second tool that creates tickets.

Should the read and write functions use the same permission surface if the service supports narrower identities/scopes?

Explain.

---

## Part D — Tool descriptions and secrets

Bad tool argument:

```json
{
  "token": "string",
  "query": "string"
}
```

Why is asking the model to supply the token a weak design?

Prefer a trusted runtime/integration layer that supplies credentials outside the model's normal arguments when the platform supports it.

---

## Part E — Logs

Classify:

Safe:

```text
INFO ticket_search query_id=abc result_count=4
```

Unsafe:

```text
DEBUG Authorization=Bearer real-secret-value
```

Potentially sensitive:

```text
INFO ticket_body="Employee medical issue..."
```

Explain why credential safety and data privacy are different concerns.

---

## Part F — Approval boundary

Consider:

1. search tickets;
2. create draft ticket;
3. send/escalate ticket externally;
4. delete ticket.

Rank them by consequence **for this workflow**.

Do not assume every write always requires human approval.

State the actual consequence that would justify an approval step.

---

## Completion artifact

Create:

```text
work/08-auth-secrets-result.md
```

Include:

- where the secret lives;
- what code knows;
- what the model sees;
- read vs write permission split;
- safe logging rule;
- one real approval boundary;
- one example of unnecessary approval theatre.
