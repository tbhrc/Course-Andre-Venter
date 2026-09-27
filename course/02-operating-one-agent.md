# Module 2 — Operating One Agent Well

## Objective

Learn to control one capable agent before adding more agents, automation or code.

## The Agent Brief

Use this structure:

```text
OUTCOME
What must be true when the task is finished?

CONTEXT
What does the agent need to know?

INPUTS
What material does it have?

CONSTRAINTS
What boundaries must it respect?

TOOLS
What can it use?

ACCEPTANCE
What evidence proves success?

STOP
When should it stop rather than expanding the task?
```

## Example — weak request

> Help me organise my DJ music.

Problems:
- no clear outcome;
- no source/location;
- no definition of organised;
- no acceptance check;
- no boundary on what may be changed.

## Example — controlled task

> Inspect the sample track list in `work/dj-library-sample.csv`. Propose a folder/tagging scheme that preserves the original files, supports fast filtering by BPM, energy and event type, and does not invent missing metadata. Create the proposal in `outputs/dj-library-organisation.md`. Success means every sample track can be routed by the scheme and all unknown metadata is clearly marked rather than guessed. Do not rename or delete source files.

That is much closer to an executable engineering task.

## The operating loop

```text
BRIEF
→ AGENT PLANS
→ AGENT ACTS
→ INSPECT
→ VERIFY
→ CORRECT
→ STOP
```

## Exercise 1 — rewrite vague tasks

Create `work/02-agent-briefs.md`.

Rewrite these as controlled Agent Briefs:

1. “Fix my audio workflow.”
2. “Research this hydraulic fault.”
3. “Make my video files easier to manage.”
4. One real task of your own.

Each must contain:
- outcome;
- context;
- inputs;
- constraints;
- tools;
- acceptance;
- stop condition.

## Exercise 2 — run one brief

Pick the smallest safe brief.

Before the agent acts, ask:

> Restate the acceptance criteria and tell me exactly how you will verify them. Do not start work yet.

Only then let it execute.

Afterwards ask:

> Show me the evidence for each acceptance criterion. Separate verified facts from assumptions.

## Fault-isolation lesson

When an agent fails, do not immediately change the model.

Ask which layer failed:

```text
Outcome unclear?
Instructions wrong?
Context missing?
Wrong source?
Tool failed?
Permission failed?
Environment failed?
Agent reasoning failed?
Verification missing?
```

This fault tree will become important later.

## Pass condition

You can turn an ambiguous request into an Agent Brief that another capable agent could execute without guessing the definition of success.
