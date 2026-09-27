# Lab — Representative Eval

## Objective

Run a small deterministic grader over structured agent outputs.

Starter:

```text
labs/11-eval-starter/
```

## Step 1 — Inspect cases

Read `eval_cases.json`.

Each case defines:

- input;
- expected fact terms;
- expected hypothesis terms;
- expected missing terms;
- terms forbidden as fact.

## Step 2 — Produce results

For each case, ask your agent for strict JSON:

```json
{
  "id": "case-1",
  "facts": [],
  "hypotheses": [],
  "missing": []
}
```

Save all outputs to `results.json`.

## Step 3 — Grade

Run:

```bash
python3 grade_results.py results.json
```

## Step 4 — Inspect failure

For every failed criterion ask:

- bad instruction?
- bad reasoning?
- ambiguous case?
- bad expected criterion?
- output-format failure?

The eval itself can be wrong.

## Step 5 — Fix and rerun

Change the smallest responsible layer.

Then rerun:
- failed case;
- full small set.

## Step 6 — Add one real case

Add a case from your own domain.

Do not add a synthetic case merely to increase case count.

## Pass condition

You can explain every grader criterion and why the eval set is representative enough for this learning objective.
