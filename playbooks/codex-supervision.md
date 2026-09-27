# Playbook — Supervise a Coding Agent

Use this for Codex or another capable repository coding agent.

## 1. Freeze the outcome

Write one observable result.

Avoid mixing:
- feature;
- refactor;
- cleanup;
- migration;
- documentation rewrite;

unless they are genuinely one outcome.

## 2. Establish baseline

Before editing:

- inspect Git status;
- read root project instructions;
- find the smallest relevant code/tests;
- run a baseline test when the current state matters.

## 3. Ask the agent to explain before mutation

Prompt:

> Inspect the relevant repository surface. Explain current behaviour, likely owner files, constraints and verification path. Do not edit yet.

If the agent cannot explain the current behaviour, it is not ready to change it.

## 4. Review scope

Challenge:

- too many files;
- architecture changes before evidence;
- new frameworks;
- new dependencies;
- duplicate helpers;
- unrelated cleanup.

Apply:

```text
DELETE → COLLAPSE → REUSE → DIRECT → only then ADD
```

## 5. Implement the smallest complete change

Give the agent authority to work within the agreed scope.

Do not dictate every line unless the implementation method itself is load-bearing.

Specify:
- outcome;
- invariants;
- acceptance;
- real boundaries.

## 6. Run targeted checks

Start with the smallest useful verification:

```text
targeted test
→ related regression tests
→ wider build/check only if material
```

Do not run the whole world merely because tests exist.

## 7. Diagnose failures

Classify before changing more code:

```text
new code?
existing baseline?
test?
dependency?
environment?
permissions?
network?
data?
```

Do not mask baseline failures as feature failures.

## 8. Inspect the diff

Ask:

- what changed;
- what was removed;
- why each file changed;
- whether public interfaces moved;
- whether tests prove behaviour;
- whether unrelated cleanup slipped in.

## 9. Correct or rollback

If the change is poor:

- correct the smallest cause; or
- discard the isolated experiment.

Avoid compounding bad work by layering patches over an unvalidated premise.

## 10. Verify once and stop

Map evidence to acceptance criteria.

Then stop.

Do not keep “improving” the repository after the requested outcome is proven.
