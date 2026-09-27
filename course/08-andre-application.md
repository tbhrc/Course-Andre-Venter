# André Application — Module 8: APIs and Tool Calling

This file personalizes the canonical [Module 8](08-apis-and-tool-calling.md) for André.

## Why this maps well to your technical background

You already work with systems where one controller talks to another machine or subsystem through a defined interface.

An API is similar:

```text
controller
→ defined command/request
→ system
→ defined response/state
```

The useful question is not:

> How many APIs can I connect?

It is:

> Which system owns the real state, and what is the smallest safe operation I need?

## Hydraulic / industrial analogy

| Software integration | Industrial analogy |
|---|---|
| API endpoint | defined machine interface |
| request body | command/settings sent to controller |
| response | machine/controller reply |
| schema | expected signal/field contract |
| authentication | authorized operator/service identity |
| write call | changing machine state |
| read call | reading sensor/system state |
| 400 error | invalid command/input |
| 401/403 | identity/authority problem |
| 404 | requested object not found |
| 5xx | remote system fault |
| idempotency | repeat command without unintended duplicate action |

## Exercise A — tool design from maintenance work

Imagine the factory maintenance system has an API.

Design three possible model tools:

```text
find_work_order(work_order_id)
create_maintenance_note(work_order_id, note)
close_work_order(work_order_id)
```

Classify each as:

- read;
- write;
- high-consequence if applicable.

Then answer:

1. Which one should you test first?
2. Which one changes authoritative state?
3. Which one may need stronger confirmation or acceptance checks?
4. Which one should not expose arbitrary API access?

## Exercise B — separate judgement from mechanics

Suppose the agent sees:

```text
pressure low
temperature normal
alarm X17
```

The AI may reason about what information to retrieve.

A deterministic tool should perform the exact retrieval:

```text
get_alarm_history(machine_id, alarm_code)
```

Do not build:

```text
run_any_database_query(sql)
```

unless that broad access is genuinely required and safely owned.

## Exercise C — audio/video analogy

For a media workflow:

```text
list_project_assets(project_id)
get_export_status(export_id)
create_render_job(project_id, preset)
```

Again separate:

- read;
- write;
- expensive operation;
- source of truth;
- verification.

A render API returning “job accepted” does not prove the final export succeeded.

## Your target

By the end of Module 8, you should instinctively ask:

```text
What system owns the truth?
What exact operation do I need?
Can an existing tool already do it?
What authority is required?
What changes?
How do I verify the result?
```
