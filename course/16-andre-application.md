# André Application — Module 16: Production Thinking

This file personalizes the canonical [Module 16](16-production-thinking.md) for André.

## Prototype vs operational system

You already understand the difference between:

> It worked once during a test.

and:

> We can rely on this during real operation.

That is the core production mindset.

## Maintenance-agent production questions

If your capstone is technical/industrial, ask:

### Reliability
- does it preserve measurements exactly?
- does it separate hypotheses from facts?
- do regression cases cover known mistakes?

### Source truth
- where do live machine readings come from?
- where does maintenance history live?
- how stale can data be before retrieval is mandatory?

### Safety
- does the agent only advise/structure evidence, or can it change machine state?
- what real action requires an authorized operator?
- what happens when evidence conflicts?

### Availability
- what if the manual/history source is unavailable?
- can the workflow continue in a degraded read-only mode?
- does it clearly say what cannot be verified?

### Observability
- can you see which source was used?
- which tool call failed?
- which assumption produced the recommendation?

### Cost/latency
- does a technical answer arrive quickly enough to be useful?
- are expensive model/tool calls actually improving the outcome?

## Audio/video production questions

- what if an asset is missing?
- can processing be safely retried?
- what is the authoritative project folder?
- how do you prevent overwriting source media?
- what proves an export completed correctly?

## Your target

Production thinking should feel familiar:

```text
commission
→ observe
→ fault-test
→ document
→ recover
→ maintain
→ improve from actual failures
```

Do not build enterprise infrastructure for a personal prototype. Harden only the risks that the real use case earns.
