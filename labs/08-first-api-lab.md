# Lab 08 — First API

## Objective

Call a safe local HTTP API, inspect request/response behaviour, and diagnose errors without needing any external account or secret.

The lab server is:

```text
labs/08-api-starter/server.py
```

It uses only the Python standard library.

---

## Part A — Start the API

From the starter folder:

```bash
python3 server.py
```

It listens on:

```text
http://127.0.0.1:8766
```

This is intentionally loopback-only.

---

## Part B — Read

In another terminal:

```bash
curl -i http://127.0.0.1:8766/tasks
```

Identify:

- method;
- URL;
- status;
- content type;
- response body.

Question:

> Which side owns the task state: curl, the AI, or the API server?

---

## Part C — Create

Run:

```bash
curl -i \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{"title":"Inspect pump"}' \
  http://127.0.0.1:8766/tasks
```

Identify:

- status code;
- new ID;
- authoritative new state.

Then call `GET /tasks` again.

---

## Part D — Invalid request

Run:

```bash
curl -i \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{}' \
  http://127.0.0.1:8766/tasks
```

Do not retry.

Explain why the response is evidence of an input/schema problem rather than a temporary network problem.

---

## Part E — Not found

Run:

```bash
curl -i http://127.0.0.1:8766/tasks/999
```

Explain why `404` is not fixed by retrying the same ID ten times.

---

## Part F — Turn one endpoint into a tool design

Design a model tool for:

```text
create_task(title)
```

Do not expose arbitrary HTTP calls to the model.

Define:

- tool name;
- description;
- argument schema;
- output;
- write consequence;
- error handling;
- verification.

---

## Part G — Optional public read-only API

If internet access is available, call one documented public read-only endpoint chosen by your coach.

Requirements:

- no credential;
- no write;
- authoritative public source;
- inspect the live docs first;
- do not hard-code the endpoint into course doctrine.

Compare:

```text
local controlled API
vs
external API dependency
```

## Completion

Create `work/08-api-lab-result.md` with:

- one GET request;
- one POST request;
- one validation error;
- one not-found error;
- one tool contract;
- source-of-truth explanation;
- retry/idempotency reflection.
