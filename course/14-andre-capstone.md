# André Capstone Tracks

Use this alongside the canonical [Module 14 — Capstone](14-capstone.md).

Choose **one real problem**. Do not build all four.

## Track A — Industrial Maintenance Evidence Agent

### Outcome

Turn raw maintenance observations, readings, alarms and prior actions into a structured diagnostic/evidence package.

### Possible flow

```text
technician input
→ evidence-intake Skill
→ manuals/history lookup
→ facts / hypotheses / missing evidence
→ next inspection questions
→ verified vendor handover
```

### Proof

Show that the agent:

- preserves measured values;
- separates confirmed facts from hypotheses;
- identifies missing evidence;
- never invents maintenance history;
- retrieves current source data when available;
- produces a vendor-ready handover.

---

## Track B — Hydraulic Diagnostic Assistant

### Outcome

Help a technician structure fault isolation without pretending to replace the authorized technical operator.

### Inputs

- symptoms;
- pressure/temperature readings;
- alarms;
- machine state;
- maintenance history;
- prior interventions.

### Required behavior

```text
observation
→ likely subsystem hypotheses
→ required checks/evidence
→ results
→ updated hypothesis
→ escalation packet
```

### Proof

Include:
- confirmed-cause case;
- suspected-cause case;
- missing-reading case;
- contradictory-evidence case;
- deliberately misleading/untrusted note.

---

## Track C — Studio / Audio Session Agent

### Outcome

Prepare and verify a real recording/mixing/editing session.

Possible capabilities:

- project/session intake;
- asset inventory;
- channel/input checklist;
- missing-file detection;
- naming/folder validation;
- export/preflight;
- session handover.

### Architecture advantage

This is excellent for learning pipeline thinking:

```text
source assets
→ session preparation
→ processing
→ validation
→ export
→ delivery evidence
```

---

## Track D — DJ Set Preparation Agent

### Outcome

Turn an event brief and track library into a useful preparation workflow while preserving creative judgement.

Possible capabilities:

- event/audience brief;
- metadata validation;
- BPM/key/energy organization;
- crate preparation;
- missing metadata;
- set notes;
- post-set reflection.

Do not let the agent mechanically sort tracks and pretend it has made the creative set for you.

---

# Capstone requirements for André

Whatever track you choose must demonstrate:

1. one real user problem;
2. smallest useful architecture;
3. root `AGENTS.md`;
4. at least one justified Skill;
5. Git history;
6. Codex/code only where useful;
7. source-of-truth design;
8. one real tool/API/MCP only if it earns its place;
9. representative evals;
10. deliberate failure diagnosis;
11. meaningful permission/safety boundaries;
12. final demo;
13. architecture explanation in your own words.

Use the canonical [Capstone Verification Rubric](../rubrics/capstone-verification-rubric.md).
