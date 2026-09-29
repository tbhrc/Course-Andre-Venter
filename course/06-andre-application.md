# André Application — Module 6: Codex as a Technical Co-Worker

This file personalizes the canonical [Module 6](06-codex-fundamentals.md) for André.

## Why this should fit you quickly

You already supervise complex systems where:

- software controls physical behaviour;
- one incorrect setting can produce a downstream fault;
- vendor support needs precise evidence;
- a machine has a current known-good operating state;
- maintenance changes must be isolated and tested;
- a symptom does not automatically reveal the real cause.

That is extremely close to good coding-agent supervision.

Your training portfolio also gives a more specific bridge: lift-truck and crane assessments explicitly separate **pre-start checks, start/operational checks, practical operation and close-down checks**. Treat repository work the same way:

```text
PRE-START
inspect repository + instructions + current tests

OPERATION
make the bounded change

FUNCTIONAL CHECK
run the relevant test / inspect output

CLOSE-DOWN
review diff + confirm no unrelated change + preserve known-good state
```

Use this mental mapping:

| Industrial / hydraulic work | Coding-agent work |
|---|---|
| machine baseline | repository baseline |
| control logic | application code |
| sensor/input values | runtime data |
| alarm / fault code | error / test failure |
| service procedure | AGENTS.md / Skill / playbook |
| changed component/setting | code diff |
| functional test | unit/integration test |
| known-good setup | known-good commit |
| vendor escalation evidence | bug report / Issue |
| rollback setting/part | revert/correct Git change |

## Exercise A — Explain before touching

Take the included Codex starter repository.

Pretend it is a machine you have never serviced.

Before allowing Codex to edit, require it to explain:

1. What is the system supposed to do?
2. Which file is the likely control point?
3. What evidence says the current system is broken?
4. Which files should probably remain untouched?
5. What exact test would prove the repair?

Treat an agent that cannot answer these as a technician who wants to replace parts before diagnosing the fault.

## Exercise B — Maintenance discipline

When the test fails, do not say:

> Fix the code.

Use:

> Tell me whether this is a logic fault, test fault, environment fault, dependency fault or data fault. Show me the evidence before changing anything else.

This is the coding equivalent of isolating hydraulic, electrical, sensor and control-system causes before replacing equipment.

## Exercise C — Your own project

After the starter lab, create a tiny repository for one familiar problem.

Choose one:

### Hydraulic maintenance
A small program that reads structured fault observations and validates that required evidence fields exist.

### Audio
A small program that validates an audio-session input list and reports missing required fields.

### Video
A small script that checks whether a folder contains the expected project/source/export structure.

### DJ
A small program that validates track metadata such as title/BPM/key when supplied.

The project does not need to be commercially useful yet.

Its job is to teach you:

```text
requirements
→ repository
→ AGENTS.md
→ code
→ test
→ diff
→ fault
→ diagnosis
→ repair
→ verification
```

## Pass condition

You should be able to supervise Codex the same way you would supervise a technical intervention:

- establish current state;
- define the intended state;
- change the smallest thing;
- observe evidence;
- reject unjustified changes;
- verify operation;
- know how to return to a known-good state.
