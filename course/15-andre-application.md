# André Application — Module 15: When Multi-Agent Actually Helps

This file personalizes the canonical [Module 15](15-multi-agent-systems.md) for André.

## Use a crew analogy carefully

A complex technical job may involve:

- one technician doing the whole diagnosis;
- separate hydraulic/electrical/software specialists;
- an independent inspector;
- a vendor engineer.

You do not call four specialists for every minor fault.

The same applies to agents.

## One-agent baseline

For a maintenance case, start with:

```text
one technical evidence agent
→ manuals
→ maintenance history
→ structured reasoning
→ verified handover
```

If this works reliably, keep it.

## A justified split

A later system might earn:

```text
manager
├── hydraulic evidence specialist
├── software/log specialist
└── documentation/history specialist
        ↓
evidence join
        ↓
manager synthesis
        ↓
human technical decision
```

This split is only justified if the workstreams are genuinely independent or require different context/tools.

## Independent verifier

Another useful pattern:

```text
diagnostic summary agent
→ evidence verifier
→ accept / repair
```

Use it when the consequence/quality requirement earns an independent check.

## Exercise

For each proposed specialist ask:

1. What exact job does it own?
2. What different instructions/tools/authority does it need?
3. Could the main agent do this just as well?
4. Can it run independently?
5. How are conflicting results merged?
6. What happens if it fails?
7. What is the measurable advantage?

If you cannot answer these, collapse it back into one agent.
