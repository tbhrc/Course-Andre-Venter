# Module 1 — AI Mental Models

## Objective

Build a practical mental model of modern AI without starting with neural-network mathematics.

## 1. Model, assistant and agent

A useful distinction:

```text
MODEL
reasoning/generation engine

ASSISTANT
model + instructions + conversation interface + some capabilities

AGENT
model + goal + instructions + context + tools + state + execution loop + verification
```

These are not perfect universal definitions, but they are useful engineering models.

### Sound-engineering analogy

A model is not the whole PA system.

It is closer to a powerful processing component inside the chain.

The useful system includes routing, sources, controls, outputs, feedback and an operator. Agentic AI is similar: the model matters, but the surrounding system determines what the model can see, do, remember and verify.

## 2. Probabilistic reasoning vs deterministic software

Traditional code often follows explicit rules.

A model predicts/reasons probabilistically. That makes it powerful for ambiguous work, but it can also:
- infer the wrong intent;
- fabricate missing information;
- choose a poor path;
- produce an answer that sounds correct without evidence.

Good agent engineering combines model reasoning with deterministic components where exactness matters.

## 3. Instructions

Instructions define stable behaviour.

Examples:
- what the agent's job is;
- where truth lives;
- what files it should read;
- what it is allowed to change;
- what must be verified;
- when it should stop.

A one-off task prompt is not the same as durable project instructions.

## 4. Context

Context is what the model can use for the current decision.

Possible context:
- your current message;
- previous conversation;
- project instructions;
- files;
- retrieved documents;
- tool results;
- database records.

More context is not automatically better. Wrong, stale or duplicated context can make the system worse.

## 5. Tools

A model can reason about sending an email.

A tool is what actually allows the agent to send it.

Common tools:
- filesystem;
- terminal;
- browser;
- email;
- calendar;
- GitHub;
- database;
- APIs;
- MCP servers.

## 6. State

State is information that survives beyond a single reasoning step.

Examples:
- files;
- a Git commit;
- a database row;
- an issue status;
- a saved configuration;
- a durable memory record.

A chat response is not automatically durable state.

## 7. Hallucination and evidence

Treat fluent output as a proposal until the result is verified.

A useful reliability hierarchy:

```text
agent says it happened
< agent shows generated output
< agent inspects the actual target
< independent check proves the target state
```

## Practical exercise — map a familiar system

Create `work/01-system-map.md`.

Choose either:
- an audio signal chain;
- your hydraulic system;
- a video-editing workflow.

Map it using:

- inputs;
- processing/reasoning;
- instructions/settings;
- tools/actuators;
- state;
- output;
- feedback/verification;
- failure points.

Then create the equivalent map for an AI agent.

## Teach-back

Without looking at this lesson, explain:

1. Why is a model not automatically an agent?
2. What is context?
3. What is state?
4. What makes a tool different from an instruction?
5. Why can a confident AI answer still require verification?

## Pass condition

Your AI should challenge unclear answers rather than simply congratulating you.
