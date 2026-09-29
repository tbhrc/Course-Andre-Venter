# André Capstone Tracks

Use this alongside the canonical [Module 14 — Capstone](14-capstone.md).

Choose **one real problem**. Do not build all tracks.

Based on [André's learner profile](../LEARNER-PROFILE.md), **Track A is the strongest default starting point** because it combines his demonstrated industrial, troubleshooting, procedural and vendor-handover strengths while forcing him to learn the new AI/Git/data/tooling layers. Track B is a strong alternative when a real hydraulic problem is available. The coach should still choose the problem with André, not for him.

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

## Track C — Maintenance Risk / HIRA Evidence Assistant

### Outcome

Turn maintenance/change observations into a structured risk-evidence package for an authorised human review.

### Possible flow

```text
work/change brief
→ evidence + hazard extraction
→ existing-control lookup
→ missing-evidence questions
→ consequence/likelihood support
→ proposed controls
→ authorised human review
→ verified final record in the real owner system
```

### Important boundary

The agent does not certify a machine/process as safe and does not replace the employer's real HIRA/SHE process. It improves evidence quality, completeness and traceability.

### Proof

Include:
- one low-risk case where no extra control is justified;
- one case with missing evidence;
- one contradictory-input case;
- one untrusted-instruction case;
- one consequential action that clearly belongs to an authorised human/operator.

---

## Track D — Studio / Audio Session Agent

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

## Track E — DJ Set Preparation Agent

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
