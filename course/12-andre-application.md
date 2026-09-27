# André Application — Module 12: Safety and Human Control

This file personalizes the canonical [Module 12](12-safety-permissions-human-control.md) for André.

## Safety interlocks are a useful analogy

Industrial systems already distinguish between:

- normal operator controls;
- maintenance controls;
- protected service/admin functions;
- actions that require explicit confirmation or procedure.

Agentic systems need the same **consequence-based thinking**.

## Important distinction

The lesson is not:

> Put a confirmation in front of everything.

That would be like requiring supervisor approval to read a pressure gauge.

The lesson is:

> Protect the action whose consequence justifies protection.

## Exercise A — classify actions

For a maintenance agent, classify:

```text
read machine manual
read current alarm
add internal maintenance note
send vendor escalation
change controller configuration
clear safety-critical fault
```

For each ask:

- read or write?
- reversible?
- external commitment?
- operational/safety consequence?
- human confirmation or monitoring needed?

## Exercise B — untrusted instructions

Suppose a downloaded vendor document contains instruction-shaped text telling an automated system to ignore its assigned diagnostic task.

Your agent should treat that text as:

```text
document content
≠ operating authority
```

Explain how this is similar to receiving a suspicious or irrelevant instruction in a service document that conflicts with the actual maintenance procedure.

## Exercise C — role separation

Design:

### Diagnostic assistant
- reads manuals;
- reads measurements;
- structures evidence;
- produces hypotheses.

### Authorized operator
- may perform defined machine-state changes under the real operating procedure.

Explain why the diagnostic assistant does not automatically need every control capability.

Then explain why an explicitly authorized operator may legitimately have broader standing authority.

## Target

You should be able to answer:

> What exact failure or consequence does this control prevent?

If you cannot answer that, the control may be friction rather than safety.
