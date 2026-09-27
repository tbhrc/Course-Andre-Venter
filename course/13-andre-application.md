# André Application — Module 13: Smallest Useful Architecture

This file personalizes the canonical [Module 13](13-smallest-useful-architecture.md) for André.

## Use the same discipline you use on a technical system

When diagnosing or modifying an industrial system, you already ask:

- what is the actual fault/outcome?
- which subsystem owns the behaviour?
- what is already installed?
- what is the smallest intervention?
- what evidence proves the result?
- what must not be disturbed?

Use the same architecture discipline for AI systems.

## Mapping

| Agent architecture | Technical system |
|---|---|
| model/agent | intelligent controller/operator |
| Skill | repeatable operating procedure |
| tool/API | machine/system interface |
| source of truth | live controller/system state |
| adapter/code | interface conversion/control logic |
| database | durable operational state |
| eval | functional verification |
| multi-agent | multiple specialist controllers/operators |

## Exercise — hydraulic diagnostic assistant

Start with this overbuilt idea:

```text
sensor database
→ ingestion service
→ classification agent
→ hydraulic agent
→ electrical agent
→ machine-learning fault model
→ maintenance database
→ vendor agent
→ report agent
→ dashboard
```

Now apply:

```text
DELETE
→ COLLAPSE
→ REUSE
→ DIRECT
→ ADD only if earned
```

A first proof may be much smaller:

```text
technician observations/readings
→ one diagnostic-intake agent
   ↳ troubleshooting Skill
   ↳ machine manual/reference
   ↳ maintenance-history lookup if available
→ structured evidence + hypotheses + missing checks
→ technician verification
```

Only add more architecture after this real loop exposes a limitation.

## Your target

You should be able to explain every component the way you would explain every component added to a machine:

> It exists because this exact requirement cannot be satisfied cleanly by the simpler system.
