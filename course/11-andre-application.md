# André Application — Module 11: Fault Isolation and Evals

This file personalizes the canonical [Module 11](11-debugging-and-evals.md) for André.

## This is already your natural operating style

When a hydraulic system fails, you do not normally replace every component simultaneously.

You isolate:

```text
symptom
→ subsystem
→ evidence
→ suspected cause
→ targeted intervention
→ retest
```

Agent debugging is the same discipline.

## Mapping

| Technical troubleshooting | Agent debugging |
|---|---|
| symptom | bad output/action |
| wiring/control logic | instructions |
| sensor input | context/data |
| wrong manual/spec | wrong source |
| actuator/tool | API/tool |
| access lockout | permission |
| machine environment | runtime/dependency |
| functional test | eval/regression |
| known recurring fault | regression case |

## Exercise A — classify before repair

Given:

> The agent says a machine fault is confirmed, but the source note says it is only suspected.

Possible failing layers:

- source retrieval;
- instruction;
- reasoning;
- output contract.

Choose the primary layer and explain the evidence.

Do not immediately change the model.

## Exercise B — regression mindset

A recurring machine fault becomes useful maintenance knowledge when the next technician can detect it faster.

An agent failure becomes useful engineering knowledge when it creates:

- a corrected Skill/instruction/tool;
- a regression case;
- a better source model;
- a better permission boundary.

Write one example from your own maintenance experience and translate it into an AI regression test.

## Exercise C — neighboring case

If you teach the agent:

> suspected pump wear must remain a hypothesis

also test:

> inspection confirmed pump wear

The correction must not force every future mention of pump wear to remain hypothetical.

That is the equivalent of fixing one machine condition without breaking normal operation elsewhere.

## Target

You should be able to debug an agent using the same discipline you use on technical systems:

```text
reproduce
→ isolate
→ change one thing
→ retest
→ preserve regression evidence
```
