# Lab 11 — Deliberate Failure and Regression

## Objective

Break a small agent workflow deliberately, diagnose the real layer, and turn the failure into a regression test.

## Scenario

An agent converts notes into:

```json
{
  "facts": [],
  "hypotheses": [],
  "missing": []
}
```

Rule:

- measured/explicit statements → facts;
- suspected/explanatory possibilities → hypotheses;
- explicitly absent required evidence → missing.

## Failure

Input:

> Pressure measured at 110 bar. Technician suspects pump wear. Temperature was not recorded.

Bad output:

```json
{
  "facts": ["Pressure 110 bar", "Pump wear"],
  "hypotheses": [],
  "missing": ["Temperature"]
}
```

## Step 1 — classify

What failed?

Possible layers:

- source;
- data;
- instruction;
- reasoning;
- output schema;
- tool.

Choose one primary failing layer and explain why.

## Step 2 — smallest correction

Possible correction:

> Preserve suspected/possible causes as hypotheses, never facts, unless confirmed by source evidence.

Do not rewrite the entire system.

## Step 3 — regression case

Add this case to your eval set.

It should fail if "pump wear" appears as a fact.

## Step 4 — neighboring cases

### Confirmed cause

> Inspection confirmed pump wear. Pressure measured at 110 bar.

Expected:
- pump wear may be fact.

### No hypothesis

> Pressure measured at 110 bar. Temperature was not recorded.

Expected:
- no invented hypothesis.

## Step 5 — reflection

Create `work/11-regression-result.md`.

Record:

- failing layer;
- evidence;
- smallest correction;
- regression criterion;
- neighboring cases;
- whether the correction generalized.
