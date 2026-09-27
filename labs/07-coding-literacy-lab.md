# Lab 07 — Coding Literacy

## Objective

Read, predict, modify and debug small code with a coding agent.

You are not graded on writing code from memory.

You are graded on whether you understand the behaviour.

---

# Part A — Read Python as data flow

Study:

```python
def open_titles(tasks):
    titles = []

    for task in tasks:
        if not task["completed"]:
            titles.append(task["title"])

    return titles
```

Before asking AI, write:

```text
Input:
Loop:
Condition:
State changed:
Output:
Possible failure:
```

Then ask your coding agent to review your explanation.

---

# Part B — Translate concepts to TypeScript

Ask:

> Show the TypeScript equivalent. Explain which concepts are the same and which syntax is different.

You should be able to identify:

- function;
- parameter;
- array;
- loop;
- condition;
- property access;
- return value.

---

# Part C — JSON

Given:

```json
[
  {"title": "Inspect pump", "completed": true},
  {"title": "Call supplier", "completed": false}
]
```

Predict the output from `open_titles`.

Then answer:

- What happens if `completed` is missing?
- What happens if `title` is missing?
- What happens if `completed` is the string `"false"` instead of boolean `false`?

Ask the agent to explain why data validation matters.

---

# Part D — Environment variables

Review:

```python
API_KEY = "real-secret-value"
```

Explain why this is a problem.

Rewrite the design in words before asking the agent for code.

Expected concept:

```text
source code refers to environment variable name
→ runtime supplies secret
→ secret is not committed
```

---

# Part E — Trace an error

Review:

```text
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    print(task["title"])
KeyError: 'title'
```

Answer:

1. Error type?
2. Failing file?
3. Failing line?
4. Which assumption was wrong?
5. What evidence would you inspect before choosing a fix?

Do not jump directly to adding `.get("title")`.

First decide whether missing title should:
- be allowed;
- be rejected;
- be substituted.

That is a product/data-contract decision.

---

# Part F — Small change with Codex

Take the `open_titles` function.

Requirement:

> Add optional filtering so only open tasks whose priority is at least a supplied minimum are returned.

Before coding:

1. define the input shape;
2. define behaviour when `priority` is missing;
3. define acceptance examples;
4. ask the coding agent for the smallest implementation.

Inspect the diff.

Do not accept a new framework or dependency.

---

# Part G — HTTP reading

Given:

```text
POST /tasks
Authorization: Bearer <token>
Content-Type: application/json

{"title":"Inspect pump"}
```

Explain:

- method;
- route;
- auth;
- body;
- likely side effect.

Then interpret:

```text
HTTP 400
{"error":"title is required"}
```

What layer likely rejected the request?

Actual API calling comes in Module 8.

---

# Part H — Logging

Which is better?

A:

```text
ERROR failed
```

B:

```text
ERROR task_validation missing_field=title index=4
```

Explain why.

Now explain why this is dangerous:

```text
DEBUG api_key=sk-live-secret-value
```

---

# Completion artifact

Create:

```text
work/07-coding-literacy-result.md
```

Include:

- one Python function explained as data flow;
- TypeScript equivalent;
- one JSON contract;
- one interpreted error;
- one safe environment-variable design;
- one reviewed code change;
- one HTTP request/response explanation;
- one logging lesson.

## Pass condition

You can explain the program without the coding agent speaking for you.
