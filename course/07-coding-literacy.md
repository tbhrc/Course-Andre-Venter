# Module 7 — Coding Literacy for AI Builders

## Objective

Learn enough code to **read, supervise, debug and extend AI-built systems**.

This is not a traditional programming course.

You do not need to memorize an entire language before using coding agents.

You do need enough literacy to answer:

- What is this code doing?
- Where does data enter?
- Where does it change?
- What can fail?
- What is returned?
- What is external?
- What is secret?
- What changed in the diff?
- Does the code actually implement the requirement?

---

## 1. Read code as data flow

Before syntax, ask:

```text
INPUT
→ TRANSFORM
→ DECISION
→ SIDE EFFECT
→ OUTPUT
```

Example:

```python
def open_tasks(tasks):
    return [task["title"] for task in tasks if not task["completed"]]
```

Read it as:

```text
input: list of task objects
→ inspect each task
→ keep tasks where completed is false
→ take each title
→ output list of titles
```

You do not need to know every Python detail to understand the behaviour.

---

## 2. Variables and values

Python:

```python
name = "Pump inspection"
completed = False
attempts = 3
```

TypeScript:

```typescript
const name = "Pump inspection";
const completed = false;
const attempts = 3;
```

A variable gives a value a name.

When reviewing code, ask:

- where was this value created?
- can it change?
- is the type what I expect?
- did it come from a trusted source?

---

## 3. Core data shapes

### String

```text
"Call supplier"
```

### Number

```text
42
12.5
```

### Boolean

```text
true / false
```

### List / array

Python:

```python
["one", "two", "three"]
```

TypeScript:

```typescript
["one", "two", "three"]
```

### Object / dictionary

Python:

```python
{"title": "Inspect pump", "completed": False}
```

TypeScript:

```typescript
{ title: "Inspect pump", completed: false }
```

Most agent/application work is moving structured values between these shapes.

---

## 4. Functions

A function packages behaviour.

Python:

```python
def add(a, b):
    return a + b
```

TypeScript:

```typescript
function add(a: number, b: number): number {
  return a + b;
}
```

Read a function by asking:

1. What enters?
2. What assumptions does it make?
3. What does it change?
4. What does it return?
5. What errors can it produce?

---

## 5. Conditions

Python:

```python
if pressure > limit:
    alert = True
else:
    alert = False
```

TypeScript:

```typescript
if (pressure > limit) {
  alert = true;
} else {
  alert = false;
}
```

Conditions create branches.

When debugging, ask:

> Which branch did the program actually take, and why?

---

## 6. Loops

Python:

```python
for task in tasks:
    print(task["title"])
```

TypeScript:

```typescript
for (const task of tasks) {
  console.log(task.title);
}
```

A loop repeats behaviour over items.

Common bugs:

- wrong collection;
- wrong filter condition;
- modifying the collection while looping;
- assuming every item has the same shape.

---

## 7. JSON

JSON is one of the most important data formats in agentic systems.

Example:

```json
{
  "title": "Inspect pump",
  "completed": false,
  "priority": 2
}
```

JSON is data, not executable code.

Key points:

- keys are strings;
- strings use double quotes;
- booleans are `true` / `false`;
- arrays use `[]`;
- objects use `{}`;
- no comments in standard JSON.

You will see JSON in:

- APIs;
- tool arguments;
- configuration;
- logs;
- databases;
- agent state;
- MCP/tool schemas.

---

## 8. Files

Programs often read and write files.

Python:

```python
from pathlib import Path

text = Path("notes.txt").read_text()
```

TypeScript / Node:

```typescript
import { readFile } from "node:fs/promises";

const text = await readFile("notes.txt", "utf8");
```

Questions:

- Which path is being used?
- Is it relative or absolute?
- What happens if the file is missing?
- Could the code overwrite source evidence?
- Is encoding handled?

Remember the lesson:

> Paths can become interfaces.

Changing a path may affect more than one file.

---

## 9. HTTP mental model

HTTP is how many programs communicate with external services.

A basic request has:

```text
METHOD
URL
HEADERS
BODY
```

A response has:

```text
STATUS
HEADERS
BODY
```

Common methods:

- `GET` — retrieve;
- `POST` — create/action;
- `PUT/PATCH` — update;
- `DELETE` — delete.

Common status families:

- `2xx` — success;
- `4xx` — request/client problem;
- `5xx` — server problem.

Do not memorize every code.

Learn to inspect the actual response.

Actual API work comes in Module 8.

---

## 10. Environment variables

Secrets and environment-specific configuration should not be hard-coded into source files.

Python:

```python
import os

api_key = os.environ.get("API_KEY")
```

TypeScript:

```typescript
const apiKey = process.env.API_KEY;
```

Do not commit:

```text
API_KEY=real-secret-value
```

A repository may contain:

```text
.env.example
```

with placeholder variable names, but not secret values.

---

## 11. Errors and exceptions

Python:

```python
try:
    value = data["title"]
except KeyError:
    raise ValueError("title is required")
```

TypeScript:

```typescript
if (!data.title) {
  throw new Error("title is required");
}
```

An error message is evidence.

Do not immediately ask the AI to “fix it.”

Read:

- error type;
- message;
- file;
- line;
- call stack;
- preceding log/output.

Then classify the layer.

---

## 12. Logs

Logs expose what a running program observed or did.

Useful log:

```text
INFO loaded_tasks count=12
ERROR task_validation missing_field=title index=4
```

Weak log:

```text
Something went wrong
```

Logging should help diagnose behaviour without exposing secrets.

Never log:

- API keys;
- passwords;
- access tokens;
- unnecessary private data.

---

## 13. Dependencies

A dependency is external code your project imports/installs.

Examples:

Python:
```text
requirements.txt
pyproject.toml
```

Node/TypeScript:
```text
package.json
package-lock.json
```

Before adding a dependency, ask:

> Does the platform/language already do this simply enough?

New dependencies add:
- install work;
- versioning;
- security surface;
- compatibility risk.

Implement-before-inventing also means reuse mature native capability before writing a custom framework.

But do not add a third-party package for a five-line standard-library task.

---

## 14. Types

Types describe what shape a value should have.

TypeScript makes them explicit:

```typescript
type Task = {
  title: string;
  completed: boolean;
};
```

Python can also use hints:

```python
def count_open(tasks: list[dict]) -> int:
    ...
```

Types help agents and humans understand contracts.

They do not replace runtime validation when external/untrusted data enters the system.

---

## 15. Read the call path

When a feature fails, trace:

```text
entrypoint
→ function call
→ data transformation
→ external dependency
→ output
```

Ask Codex:

> Trace the call path for this behaviour. Name the files/functions in order and distinguish application logic from external dependencies. Do not edit anything.

This is often more useful than asking:

> Where is the bug?

---

## 16. Learn to predict before running

Before executing a small code block, predict:

- output;
- changed files;
- returned value;
- expected error.

Then run it.

Prediction forces understanding.

When prediction differs from reality, that gap is valuable learning.

---

## 17. Translation is a learning tool

Ask your coding agent:

> Show this Python function and the TypeScript equivalent side by side. Explain the behavioural equivalence rather than every punctuation difference.

The goal is to recognize concepts across languages.

Not to memorize syntax trivia.

---

## 18. AI-written code still creates maintenance obligations

If the agent writes 500 lines you cannot reason about, you have acquired a system you cannot supervise.

You do not need to author every line.

You do need to understand:

- responsibility boundaries;
- contracts;
- data flow;
- failure paths;
- verification;
- dependencies;
- state changes.

The coding agent can explain details on demand.

Your job is to retain architectural understanding.

---

## Practical work

Complete:

1. [Coding literacy cheat sheet](../knowledge/coding-literacy-cheatsheet.md)
2. [Lab 07 — Coding Literacy](../labs/07-coding-literacy-lab.md)
3. [Lab — Diff, Debug and Rollback](../labs/07-diff-debug-rollback.md)
4. [Prompt — Explain This Code](../prompts/07-explain-code.md)

## Teach-back

Explain:

1. What is a function?
2. What is JSON?
3. Why use environment variables?
4. What is the difference between an error and a log?
5. What is a dependency?
6. How would you trace a failing feature?
7. Why is understanding data flow more valuable than memorizing syntax?

## Pass condition

You can read a small unfamiliar program, explain its data flow, identify likely failure points, interpret a basic error, and review a coding agent's change without treating the code as a black box.
