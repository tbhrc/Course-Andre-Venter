# Coding Literacy Cheat Sheet

Use this while supervising AI-built code.

## Read any function

Ask:

```text
INPUT?
ASSUMPTIONS?
DECISIONS?
SIDE EFFECTS?
OUTPUT?
FAILURES?
```

## Read any file

Ask:

```text
Why does this file exist?
Who calls/imports it?
What contract does it expose?
What source/state does it touch?
What breaks if its path/name changes?
```

## Read any diff

Ask:

```text
What was added?
What was removed?
What public behaviour changed?
What data contract changed?
What dependency changed?
What test proves the outcome?
What change is unrelated?
```

## Read any error

Ask:

```text
ERROR TYPE
MESSAGE
FILE
LINE
CALL STACK
INPUT
BASELINE OR NEW?
```

## Read any API call

Ask:

```text
METHOD
URL
AUTH
REQUEST BODY
RESPONSE STATUS
RESPONSE BODY
TIMEOUT/RETRY
SIDE EFFECT
```

## Read configuration

Ask:

```text
What is fixed in code?
What belongs in configuration?
What belongs in environment variables?
Are any secrets committed?
```

## Python ↔ TypeScript concepts

| Concept | Python | TypeScript |
|---|---|---|
| Variable | `name = "x"` | `const name = "x";` |
| Function | `def f(x):` | `function f(x) {}` |
| Boolean | `True / False` | `true / false` |
| List/array | `[1, 2]` | `[1, 2]` |
| Dictionary/object | `{"a": 1}` | `{ a: 1 }` |
| Missing value | `None` | `null / undefined` |
| Print/log | `print(x)` | `console.log(x)` |
| Throw error | `raise ValueError()` | `throw new Error()` |
| Environment | `os.environ.get()` | `process.env.X` |

## Common red flags

- hard-coded secrets;
- `except: pass` / swallowed errors;
- broad unrelated refactor;
- new dependency for trivial work;
- tests changed to accept broken behaviour;
- duplicate source of truth;
- path rename without reference search;
- network call without timeout/error handling;
- logs containing secrets;
- comments explaining obsolete behaviour;
- generated code nobody can explain.

## Core rule

You do not need to know every syntax rule.

You need to understand enough of the system to **challenge the agent intelligently and verify the outcome**.
