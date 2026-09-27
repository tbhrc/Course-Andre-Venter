# Course Roadmap — Practical AI & Agentic AI for André Venter

## Outcome

By the end of this course, André should be able to build and operate a useful AI system rather than merely use a chatbot.

The course is intentionally **builder-first**. Coding theory, APIs and orchestration are introduced when a real project needs them.

## Phase 1 — Control one agent

### Module 0 — Start here
**Goal:** establish the learning environment and baseline.

You will:
- give this repository to an AI;
- verify that the AI reads `AGENTS.md`;
- create your learner workspace;
- choose an initial real problem;
- establish a simple build/verify/reflection loop.

**Artifact:** `work/00-baseline.md`

### Module 1 — AI mental models
**Goal:** understand the components without unnecessary mathematics.

Learn:
- model vs assistant vs agent;
- instruction vs prompt vs context;
- tool use;
- files and external knowledge;
- deterministic software vs probabilistic reasoning;
- hallucination and uncertainty;
- why verification matters.

**Artifact:** your own system diagram and explanations.

### Module 2 — Operating one agent well
**Goal:** move from casual prompting to controlled execution.

Learn:
- outcome definition;
- constraints;
- inputs;
- acceptance criteria;
- role and operating boundaries;
- context management;
- plan → act → inspect → verify.

**Artifact:** a reusable Agent Brief.

### Module 3 — Project instructions and `AGENTS.md`
**Goal:** make behaviour survive beyond one chat.

Learn:
- project-level instructions;
- repository routers;
- stable rules vs task-specific instructions;
- progressive context loading;
- how bad instructions cause agent drift;
- how to test an instruction file.

**Artifact:** André writes and tests his first `AGENTS.md`.

---

## Phase 2 — Durable project work

### [Module 4 — Markdown, files, Git and GitHub](course/04-markdown-git-github.md)
**Goal:** make AI work durable, inspectable and reversible.

Learn:
- files/folders as agent context;
- Markdown;
- repository anatomy;
- commits;
- diffs;
- branches;
- issues;
- pull requests;
- source of truth;
- why Git is valuable even when AI writes the code.

**Build:** complete the [Git/GitHub lab](labs/04-git-github-lab.md), make deliberate changes and inspect the diff.

### [Module 5 — Skills](course/05-skills.md)
**Goal:** turn proven repeated behaviour into reusable capability.

Learn:
- what a Skill is;
- trigger conditions;
- minimal instruction design;
- references/resources;
- progressive loading;
- testing a Skill on representative work;
- when not to create a Skill.

**Build:** complete the [first Skill workshop](workshops/05-first-skill-workshop.md), test it using the [Skill testing playbook](playbooks/skill-testing-debugging.md), then complete the [Skill graduation exercise](course/05-skill-graduation.md).

Suggested starting domains:
- audio session preparation;
- DJ set preparation;
- technical fault-isolation checklist;
- hydraulic machine troubleshooting handover.

---

## Phase 3 — Codex as a technical worker

### [Module 6 — Codex fundamentals](course/06-codex-fundamentals.md)
**Goal:** supervise an agent working directly on a repository.

Learn:
- giving Codex a bounded objective;
- asking Codex to inspect before changing;
- reading plans and diffs;
- creating/editing files;
- running commands;
- tests;
- debugging;
- review;
- rollback;
- repository instructions.

**Build:** complete the [Codex supervision lab](labs/06-codex-supervision-lab.md), then apply it to André's [technical Codex exercise](course/06-andre-application.md).

### [Module 7 — Coding literacy for AI builders](course/07-coding-literacy.md)
**Goal:** learn enough code to supervise, debug and extend AI-built systems.

Focus:
- variables and data types;
- functions;
- conditions and loops;
- files;
- JSON;
- HTTP;
- errors and logs;
- packages/dependencies;
- environment variables;
- Python and/or TypeScript as practical implementation languages.

This is **not** a traditional programming course. Every coding concept must connect to a real agent/build task.

**Build:** complete the [coding literacy lab](labs/07-coding-literacy-lab.md), [diff/debug/rollback lab](labs/07-diff-debug-rollback.md), and André's [systems-to-code application](course/07-andre-application.md).

---

## Phase 4 — Tools and connected agents

### [Module 8 — APIs and tool calling](course/08-apis-and-tool-calling.md)
**Goal:** understand how an agent moves from reasoning to action.

Learn:
- API basics;
- request/response;
- authentication concepts;
- JSON payloads;
- tool schemas;
- permissions;
- retries;
- failure handling;
- idempotency.

**Build:** complete the [first API lab](labs/08-first-api-lab.md), [tool-contract workshop](workshops/08-tool-contract-workshop.md), [authentication/secrets practical](labs/08-auth-secrets-practical.md), and André's [technical API/tool application](course/08-andre-application.md).

### [Module 9 — MCP](course/09-mcp.md)
**Goal:** understand reusable agent-to-system connectivity.

Learn:
- MCP mental model;
- tools vs resources;
- client/server relationship;
- discovery;
- permission boundaries;
- why MCP reduces custom integration work;
- when a direct API is simpler.

**Build:** complete the [first MCP connection lab](labs/09-first-mcp-connection.md), then André's [MCP systems application](course/09-andre-application.md).

---

## Phase 5 — Reliability

### [Module 10 — Context, memory, state and data](course/10-context-memory-state-data.md)
**Goal:** understand what persists and where truth lives.

Learn:
- conversation context;
- project files;
- durable memory;
- database state;
- external source-of-truth systems;
- stale context;
- provenance;
- retrieval;
- avoiding duplicated truth.

**Build:** complete the [source-of-truth/state-design workshop](workshops/10-source-of-truth-state-design.md), then André's [machine-state application](course/10-andre-application.md).

### [Module 11 — Debugging and evaluation](course/11-debugging-and-evals.md)
**Goal:** troubleshoot agents the way André already troubleshoots technical systems.

Learn:
- reproduce the failure;
- isolate the layer;
- distinguish model failure from instruction failure, tool failure, data failure and environment failure;
- logs and traces;
- representative tests;
- eval cases;
- regressions;
- changing one variable at a time.

**Build:** complete the [failure/regression lab](labs/11-deliberate-failure-regression.md), [representative eval exercise](labs/11-representative-eval.md), and André's [fault-isolation application](course/11-andre-application.md).

### [Module 12 — Safety, permissions and human control](course/12-safety-permissions-human-control.md)
**Goal:** make useful systems without hiding risk.

Learn:
- secrets;
- least necessary access;
- reversible vs irreversible actions;
- approvals at consequential boundaries;
- untrusted input;
- prompt injection;
- audit evidence where it adds value;
- human-in-the-loop design.

**Build:** complete the [prompt-injection/untrusted-input lab](labs/12-prompt-injection-untrusted-input.md), [permission/human-control lab](labs/12-permission-boundaries.md), and André's [technical safety application](course/12-andre-application.md).

---

## Phase 6 — Build a real agent

### Module 13 — Architecture the smallest useful system
**Goal:** choose the minimum architecture that solves a real problem.

Default order:

```text
capable model
→ clear instructions
→ useful files/context
→ reusable Skill
→ existing tool/API/MCP
→ small adapter/code only if needed
→ database/state only if needed
→ orchestration only if needed
```

**Artifact:** architecture diagram + proof plan.

### Module 14 — Capstone build
Choose one real project.

Strong candidates for André:

1. **Studio / Audio Session Assistant**
   - session intake;
   - checklist;
   - file/track organisation;
   - issue detection;
   - handover notes.

2. **DJ Set Preparation Agent**
   - track metadata;
   - energy/BPM/key planning;
   - crate organisation;
   - event brief;
   - set review.

3. **Industrial Maintenance Knowledge Agent**
   - maintenance procedure library;
   - fault symptoms;
   - evidence capture;
   - troubleshooting tree;
   - vendor handover preparation.

4. **Hydraulic System Diagnostic Assistant**
   - symptoms → likely subsystem;
   - inspection sequence;
   - measured values;
   - maintenance history;
   - escalation packet.

The capstone must solve a real problem and include:
- repository instructions;
- at least one Skill;
- Git history;
- Codex involvement;
- at least one tool/API/MCP where genuinely useful;
- explicit state/source-of-truth design;
- representative verification;
- a short architecture explanation André can give without AI assistance.

---

## Phase 7 — Advanced only after the foundation

### Module 15 — Multi-agent systems
Only now introduce:
- specialist agents;
- handoffs;
- supervisor/router patterns;
- parallel work;
- shared state;
- conflict resolution;
- observability.

The key question is not “How many agents can I create?”

It is:

> Does separating this job into multiple agents produce a clearer, more reliable system than one well-instructed agent with the right tools?

### Module 16 — Production thinking
Learn:
- deployment;
- monitoring;
- cost;
- latency;
- rate limits;
- failure recovery;
- versions;
- backups;
- testing before releases;
- user experience.

---

# Graduation test

André receives a new practical problem.

Without being given the architecture, he must be able to:

1. clarify the outcome;
2. identify the source of truth;
3. create the repository/workspace;
4. write the controlling instructions;
5. organise context;
6. decide whether a Skill is justified;
7. use Codex to build what is missing;
8. connect required tools;
9. identify real permissions and risks;
10. test representative cases;
11. diagnose at least one failure;
12. explain the system clearly.

That is the graduation standard.
