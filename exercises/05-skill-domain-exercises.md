# Skill Exercises — André's Technical Domains

These exercises use domains you already understand.

The point is not to test your audio, DJ or maintenance expertise.

The point is to test whether you can convert expertise into a reusable AI operating procedure.

Choose at least **two** exercises.

---

# Exercise A — Audio Session Preflight

## Repeated job

Prepare a live or studio session before the technical work starts.

## Candidate input

- event/session brief;
- venue information;
- input/channel list;
- known equipment;
- timing;
- performer/client requirements.

## Candidate outcome

A concise technical preflight showing:

- what is confirmed;
- what is missing;
- what must be checked;
- what may block the session;
- what should happen before sound check.

## Your job

Design a Skill that does **not** invent missing technical information.

### Discovery tests

Should trigger:

> Prepare a technical preflight for tomorrow's live sound session from this input list and venue brief.

Should probably not trigger:

> Explain the difference between dynamic and condenser microphones.

### Failure to watch for

AI invents:

- equipment availability;
- power specifications;
- patching;
- channel assignments;
- venue capabilities.

Your Skill should distinguish **known**, **missing** and **recommended**.

---

# Exercise B — DJ Set Preparation

## Repeated job

Turn an event brief plus a track pool into a structured set-preparation plan.

## Candidate input

- event type;
- audience;
- expected duration;
- track list;
- BPM/key/energy metadata where available;
- restrictions or must-play tracks.

## Candidate outcome

A preparation plan with:

- event constraints;
- track pools;
- energy progression;
- transition considerations;
- metadata gaps;
- rehearsal checks.

## Important boundary

The Skill should not pretend there is one mathematically perfect set order.

The agent should retain judgement.

### Discovery tests

Should trigger:

> Help me prepare this track pool for a four-hour corporate DJ set.

Should not automatically trigger:

> Who produced this song?

### Failure to watch for

Over-automation.

If the Skill becomes a deterministic "sort by BPM and call it a set," it has removed the creative judgement that makes the work valuable.

---

# Exercise C — Maintenance Vendor Handover

## Repeated job

Turn raw machine fault observations into a clean escalation for the manufacturer or service vendor.

## Candidate input

- symptoms;
- timestamps;
- alarms;
- measurements;
- sequence of events;
- interventions already tried;
- photos/log references;
- unresolved questions.

## Candidate outcome

A vendor-ready technical handover that separates:

```text
OBSERVATION
MEASUREMENT
ACTION TAKEN
RESULT
HYPOTHESIS
MISSING EVIDENCE
QUESTION FOR VENDOR
```

## Discovery tests

Should trigger:

> Prepare these machine-fault notes for the manufacturer's technical team.

Should not automatically trigger:

> Write a preventive maintenance calendar.

### Failure to watch for

The AI converts a hypothesis into a fact.

Your Skill should make that difficult.

---

# Exercise D — Hydraulic Fault Diagnostic Intake

## Repeated job

Structure the first diagnostic pass for a hydraulic fault.

This is **not** a Skill that should autonomously declare the machine safe, diagnose beyond the evidence, or instruct unqualified people to perform hazardous interventions.

Its purpose is **structured evidence and troubleshooting intake**.

## Candidate input

- symptoms;
- pressure readings;
- temperature;
- alarms;
- actuator behaviour;
- operating state;
- recent maintenance;
- known changes.

## Candidate outcome

A structured diagnostic record with:

- observed symptoms;
- exact measured values;
- missing measurements;
- relevant recent changes;
- possible subsystem categories;
- next evidence to collect;
- escalation notes.

## Discovery tests

Should trigger:

> Structure these readings and symptoms into a hydraulic fault diagnostic intake.

Should not automatically trigger:

> Tell me how to bypass this safety interlock.

### Failure to watch for

The AI jumps from symptom to confident root cause.

The Skill should preserve uncertainty and evidence boundaries.

---

# Comparative exercise

After building two Skills, compare them.

Create:

```text
work/05-skill-comparison.md
```

Answer:

1. Which rules are truly domain-specific?
2. Which rules are generic agent behaviour and should be removed?
3. Did either Skill need a reference file?
4. Did either Skill need deterministic code?
5. Which Skill had a clearer trigger?
6. Which was easier to test?
7. Which one would save you the most repeated explanation in real life?

## Advanced challenge

Ask your AI:

> Try to merge these two Skills into one generic technical-assistant Skill.

Then evaluate the result.

In many cases the merged Skill becomes less discoverable and less precise.

Explain why.
