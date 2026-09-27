# André Application — Module 7: Coding Literacy

This file personalizes the canonical [Module 7](07-coding-literacy.md) for André.

## Your advantage

You already understand systems, dependencies, fault paths and physical consequences.

Coding literacy is largely learning the vocabulary used to express those same relationships in software.

You do **not** need to become a traditional programmer before Codex becomes useful.

You need to understand enough to supervise what Codex builds.

## Mapping software to systems you already know

| Software concept | Technical analogy |
|---|---|
| variable | current setting / measured value |
| function | repeatable operation |
| condition | control rule / interlock logic |
| loop | repeated cycle over components/items |
| object / JSON | structured equipment/fault record |
| function input | sensor/operator/source input |
| return value | produced result |
| exception | explicit fault condition |
| log | machine/event history |
| environment variable | runtime configuration stored outside source |
| dependency | external component/library the system relies on |
| test | controlled functional verification |
| call stack | sequence of operations leading to failure |
| Git commit | known recorded system state |
| diff | exact change since previous state |

## Exercise A — Read code like a control diagram

When looking at a function, ignore unfamiliar punctuation first.

Trace:

```text
WHAT ENTERS?
→ WHAT GETS CHECKED?
→ WHICH BRANCH IS TAKEN?
→ WHAT CHANGES?
→ WHAT LEAVES?
→ WHAT CAN FAIL?
```

This is very similar to following signal flow or hydraulic flow.

## Exercise B — Predict before run

Before running any small code example:

1. predict the output;
2. predict the likely failure;
3. run it;
4. compare reality with your prediction.

The gap is the lesson.

## Exercise C — Fault trace

Take a Python error and ask Codex to explain:

```text
symptom
→ exact failing line
→ wrong assumption
→ upstream input
→ smallest repair
→ verification
```

Do not accept a fix until you understand the wrong assumption.

## Exercise D — Code review using maintenance judgement

When reviewing a diff, ask the same questions you would ask after technical maintenance:

- Was only the intended component changed?
- Did the change affect another interface?
- Was a safety/validation check removed?
- Did someone hide the fault instead of fixing it?
- Did the change add unnecessary equipment/dependencies?
- What proves the system now operates correctly?

## Your target

By the end of Module 7 you should be able to say:

> I may not have written this system from scratch, but I understand the data flow, the key contracts, the dependencies, the failure path, the change that was made and the evidence that proves it works.

That is enough coding literacy to become highly effective with coding agents and to keep learning quickly.
