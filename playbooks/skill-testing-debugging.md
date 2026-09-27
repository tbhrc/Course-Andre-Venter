# Playbook — Test and Debug a Skill

## Objective

Do not judge a Skill by how good its `SKILL.md` looks.

Judge it by induced behaviour.

Use this sequence:

```text
DISCOVERY
→ EXECUTION
→ OUTPUT
→ FAILURE
→ SMALLEST FIX
→ RETEST
```

---

# 1. Discovery test

Test at least:

### Positive request

A realistic request that clearly belongs to the Skill.

### Alternate positive request

Same job, different wording.

### Neighbor request

Related domain, different job.

### Unrelated request

Clearly outside scope.

Ask:

- Did the Skill trigger when it should?
- Is the description too vague?
- Is it stealing work from another capability?

If discovery is wrong, fix the **name/description** before bloating the body.

---

# 2. Execution test

Use one representative real input.

Do not create an artificial easy case designed around your Skill wording.

Observe:

- Did it follow the intended sequence?
- Did it load relevant references only when needed?
- Did it preserve source evidence?
- Did it invent missing facts?
- Did it stop when the job was complete?
- Did it produce the right natural output?

---

# 3. Acceptance test

Write acceptance conditions before judging the result.

Example:

```text
- all supplied pressure readings preserved exactly;
- hypotheses labelled as hypotheses;
- attempted interventions listed in chronological order;
- missing evidence explicit;
- no invented component specifications.
```

Then inspect the actual output against each condition.

---

# 4. Diagnose the failing layer

Do not respond to every failure by adding more instructions.

Use this fault tree:

```text
Skill did not trigger
→ description/discovery problem

Skill triggered but wrong job
→ ownership/scope problem

Skill understood job but missed rule
→ control-plane instruction problem

Skill needs detailed stable knowledge
→ reference problem

Skill repeatedly fails exact mechanical step
→ possible script/helper problem

Skill has correct procedure but source is wrong/stale
→ data/source problem

Skill follows rules but result still poor
→ reasoning/model/example problem

Skill works only when you tell it expected answer
→ test design / overfitting problem
```

---

# 5. Change one material thing

Bad debugging:

```text
Rewrite the description
+ add 30 rules
+ add a script
+ add 4 reference files
+ change the output
```

Now you do not know what fixed the problem.

Better:

```text
Observed failure:
The Skill treated suspected pump cavitation as confirmed.

Smallest fix:
Add rule: "Separate observation, inference and confirmed cause."

Retest:
Use the same case plus one different case.
```

---

# 6. Test the output, not just the process

A Skill can follow every step and still produce a poor result.

Inspect the artifact itself.

For a vendor handover:

- Is it concise enough to send?
- Are measurements legible?
- Can the vendor see what has already been tried?
- Are open questions obvious?

For a DJ preparation Skill:

- Does it help the actual preparation?
- Has it preserved creative judgement?
- Is missing metadata visible?

For an audio preflight:

- Could it prevent a real setup surprise?

---

# 7. Avoid overfitting

If you keep adding rules only to pass one exact example, your Skill may become a brittle test answer.

After a fix, run:

- the original failed case;
- one similar but different case;
- one neighbor request.

---

# 8. Minimality review

After the Skill works, ask:

> Which instruction can be deleted without reducing reliability?

Also ask:

> Which repeated mechanical step, if any, genuinely earns a script?

Do not confuse "more files" with "more mature."

---

# 9. Final Skill evidence

Keep a small test note:

```markdown
# Skill test

## Representative request
...

## Expected outcome
...

## Failure observed
...

## Change made
...

## Retest evidence
...

## Neighbor request
...
```

This is learning evidence, not a permanent enterprise testing framework.

---

# Debug prompt

Use:

> Test this Skill as induced behaviour, not prose. First evaluate discovery using a realistic positive request and a neighboring non-trigger request. Then run one representative execution. Compare the actual result against explicit acceptance criteria. If something fails, identify the failing layer and recommend the smallest correction. Do not redesign the Skill unless the observed failure requires it.
