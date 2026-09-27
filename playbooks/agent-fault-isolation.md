# Playbook — Agent Fault Isolation

## 1. Freeze the symptom

Write exactly what happened.

Prefer:

> For input X, the agent created a duplicate record before checking the authoritative system.

over:

> The agent is bad.

## 2. Establish expected behaviour

What should have happened?

What evidence would prove it?

## 3. Classify the layer

```text
objective
instruction
context
source
model reasoning
tool
permission
data
environment
verification
```

## 4. Inspect evidence

Open only evidence relevant to the suspected layer:

- instruction;
- retrieved record;
- tool arguments/result;
- error;
- diff;
- log;
- source-system state.

## 5. Form one hypothesis

Example:

> The duplicate happened because the workflow did not verify the existing external ID before create.

Not:

> AI is unreliable.

## 6. Make the smallest correction

Change only the layer supported by evidence.

## 7. Rerun

Run:

- original failed case;
- one similar case;
- one neighboring case;
- relevant regressions.

## 8. Promote learning if reusable

If the failure reveals a durable rule, change its smallest correct owner:

- AGENTS.md;
- Skill;
- tool schema;
- test/eval;
- source model;
- permission configuration.

## 9. Stop

Once evidence proves the failure is addressed, stop expanding scope.
