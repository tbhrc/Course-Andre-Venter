# Module 4 — Markdown, Files, Git and GitHub

## Objective

Learn enough Markdown, Git and GitHub to make AI work **durable, inspectable, reversible and understandable**.

You are not learning Git because every AI builder must become a software engineer.

You are learning Git because agentic work becomes safer and more useful when you can answer:

- What changed?
- Who or what changed it?
- What did the file look like before?
- Can I compare versions?
- Can I undo a bad change?
- Can another agent enter the project and understand the current state?

For an AI builder, Git is one of the best forms of technical memory.

---

## 1. Files are part of the agent system

A chat message disappears into conversation history.

A file can become part of the project.

A useful mental model is:

```text
conversation
= temporary working context

project file
= durable project context

Git commit
= durable versioned project context
```

An agent that writes good files into the right repository is leaving behind useful system state for the next agent.

---

## 2. Markdown

Markdown is plain text with lightweight structure.

You are already reading it throughout this course.

### Core syntax

```markdown
# Heading 1
## Heading 2

Normal paragraph.

- bullet
- bullet

1. numbered item
2. numbered item

**bold**
`inline code`

[Link text](https://example.com)

```text
code or diagram block
```
```

### Why Markdown matters for agents

Markdown is:

- easy for humans to read;
- easy for AI to read;
- easy to diff;
- easy to version;
- portable across GitHub, editors and AI tools;
- ideal for project instructions, knowledge, Skills and playbooks.

Do not use complex formats when plain structured text solves the job better.

---

## 3. Repository mental model

A Git repository is a folder with version history.

Example:

```text
my-agent-project/
├── README.md
├── AGENTS.md
├── knowledge/
├── work/
├── outputs/
└── .git/
```

The hidden `.git/` directory contains the version-control machinery.

### Important distinction

Git and GitHub are not the same thing.

- **Git** = the version-control system.
- **GitHub** = a service that hosts Git repositories and adds collaboration features such as Issues and Pull Requests.

You can use Git without GitHub.

You can also use GitHub as the shared remote home for your Git repository.

---

## 4. The six Git operations to understand first

Do not begin by memorising dozens of commands.

Understand these six operations:

### 1. Inspect

```bash
git status
```

Question answered:

> What is different from the last recorded version?

### 2. Compare

```bash
git diff
```

Question answered:

> Exactly what changed?

### 3. Stage

```bash
git add <file>
```

Meaning:

> Include this change in the next recorded change-set.

### 4. Commit

```bash
git commit -m "Describe the meaningful change"
```

Meaning:

> Record this state in project history.

### 5. Inspect history

```bash
git log --oneline
```

Question answered:

> What meaningful changes happened before?

### 6. Create a branch

```bash
git switch -c <branch-name>
```

Meaning:

> Create an isolated line of work so I can change things without immediately changing the main line.

---

## 5. The AI builder's Git loop

Use this loop:

```text
inspect status
→ understand task
→ make a small meaningful change
→ inspect diff
→ verify result
→ commit
```

The important part is **inspect the diff before trusting the change**.

An AI saying "I updated the file" is not the same as you seeing what it changed.

---

## 6. Diff thinking

A diff is the exact change between versions.

Example:

```diff
- Never edit source files.
+ Never edit original source audio files. Create working copies under work/.
```

A diff tells you more than "the file was updated."

It tells you:

- what disappeared;
- what appeared;
- whether the change was broader than requested;
- whether important information was accidentally removed.

### Exercise

Ask your AI to make a tiny controlled change to a practice Markdown file.

Before committing, inspect the diff yourself.

Answer:

1. Did it change only what you requested?
2. Did it silently rewrite anything else?
3. Is the new wording actually better?
4. Would you be comfortable recording this version permanently?

---

## 7. Commit thinking

A good commit represents one meaningful change.

Weak commit:

```text
updates
```

Better:

```text
Add fault-isolation checklist for hydraulic startup failures
```

A future human or agent should understand why the commit exists.

### Rule

Do not make one giant commit covering five unrelated experiments if they can be separated cleanly.

The goal is not bureaucracy.

The goal is recoverable meaning.

---

## 8. Branches

A branch is useful when:

- the work is experimental;
- you want review before changing `main`;
- the change may fail;
- another person/agent is working separately;
- you want a clean comparison between proposed and current state.

For simple personal work, you do not need a branch for every tiny edit.

Use branches when isolation provides real value.

---

## 9. Issues

An Issue is durable work/decision continuity.

Good uses:

- a substantial piece of work that spans multiple sessions;
- a bug;
- a future feature;
- a design decision needing discussion;
- work another person/agent must pick up later.

Bad use:

- creating an Issue for every five-minute task;
- treating an Issue as permission to work;
- copying the entire chat into the Issue.

A good Issue preserves:

```text
objective
current state
important constraints
material decisions
next action
```

This course itself is controlled by one GitHub Issue because the build spans multiple passes.

---

## 10. Pull Requests

A Pull Request (PR) proposes changing one branch into another.

Think:

```text
current main
+
proposed branch
=
reviewable change
```

PRs are especially useful when:

- another person should review;
- an AI made a material change;
- tests need to run before merge;
- the diff needs a clean discussion surface.

Do not use PRs just because "professional developers use PRs."

Use them when review/isolation earns the extra step.

---

## 11. Reversibility

One reason Git is powerful with agents is that mistakes become less frightening.

If an agent makes a poor edit, you can inspect earlier history and restore known-good content.

Before using destructive Git commands, understand exactly what they affect.

During this course, prefer:

- inspecting;
- comparing;
- making new corrective commits;

over destructive history rewriting.

---

## 12. GitHub as an agent workspace

A repository can hold:

- instructions;
- knowledge;
- working files;
- source code;
- Skills;
- Issues;
- tests;
- outputs;
- architecture decisions.

That makes GitHub a useful home for agentic projects.

But GitHub should not become a dumping ground for every secret or private file.

Do not commit:

- API keys;
- passwords;
- access tokens;
- private credentials;
- secret environment values.

---

## Practical exercise

Complete [Lab 04 — Git and GitHub](../labs/04-git-github-lab.md).

Do not continue to Module 5 until you can:

- make a Markdown change;
- inspect `git status`;
- inspect a diff;
- commit intentionally;
- create a branch;
- explain what an Issue is for;
- explain what a PR is for;
- describe why Git is useful when an AI is doing the editing.

## Teach-back

Explain this without notes:

> Why is Git more than "a place to store code" for an AI builder?

## Pass condition

You can independently inspect an AI-made change and determine what actually changed before accepting it.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [5. Reusable Skills](05-skills.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
