# Module 3 — Project Instructions and AGENTS.md

## Objective

Move the agent's operating behaviour out of one chat and into the project.

## Why project instructions matter

If you repeatedly type:

- always verify changes;
- put finished work in this folder;
- never delete source files;
- use this naming convention;
- read this reference first;

then the project is carrying important operational knowledge only in your head or chat history.

A durable instruction file turns those rules into part of the working environment.

## Think of AGENTS.md as the operating panel

It is not the current job ticket.

It defines how the agent should operate inside the project.

A good root `AGENTS.md` usually answers:

1. What is this repository?
2. What outcome does it serve?
3. Where does different material belong?
4. Which instructions or Skills own recurring jobs?
5. What important rules must survive every session?
6. What constitutes proof?
7. When should the agent stop?

## Stable rule vs task instruction

Stable project rule:

> Never alter original source audio. Work on copies under `work/`.

Task instruction:

> Analyse the four tracks uploaded today and produce mix notes.

The first belongs in durable project instructions. The second belongs in the task.

## Progressive loading

Do not put the entire world in `AGENTS.md`.

Use it as a router:

```text
AGENTS.md
→ identify the kind of work
→ load the relevant Skill/file
→ perform the task
→ verify
```

This keeps context smaller and clearer.

## Exercise — build a clean-room agent project

Create this under `work/first-agent-project/`:

```text
first-agent-project/
├── README.md
├── AGENTS.md
├── knowledge/
├── work/
└── outputs/
```

Pick one familiar domain:
- audio;
- DJ preparation;
- video editing;
- machine maintenance;
- hydraulic troubleshooting.

Write a root `AGENTS.md` from scratch.

Do not copy this repository's file word for word.

## Test your instructions

Start a fresh AI session or fresh agent context against only your new project.

Give it three tests:

### Test A — placement
> I have a reusable fault-code reference. Where should it go?

### Test B — execution
> I need to investigate a new fault. What is your first step?

### Test C — boundary
> Delete all old source evidence so the folder is clean.

The responses should reflect your project rules.

If they do not, improve the smallest instruction that caused the failure.

## Pass condition

A fresh agent can enter the project, understand the operating shape and make correct first-hop decisions without relying on your previous chat.
