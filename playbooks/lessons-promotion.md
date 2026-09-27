# Playbook — Promote a Lesson Into Future Behaviour

## Objective

Turn a material failure or success into a durable improvement without creating learning bureaucracy.

## Loop

```text
observe
→ reproduce
→ identify changed assumption
→ extract reusable rule
→ choose smallest correct owner
→ implement
→ verify old failure is harder to repeat
→ stop
```

## Is it material?

Promote only if the learning is likely to matter again.

Do not capture every typo or one-off mistake.

## Is it actually new?

Check whether an existing:

- AGENTS.md rule;
- Skill;
- tool schema;
- test/eval;
- playbook;
- source model;

already owns the principle.

Deepen the existing owner when possible.

## Choose owner

```text
reusable HOW
→ Skill

project invariant
→ AGENTS.md

tool contract problem
→ tool schema/implementation

regression
→ eval/test

state ownership mistake
→ architecture/source-of-truth model

one-time task detail
→ do not promote
```

## Preserve evidence proportionally

Keep enough evidence to understand why the rule exists.

Do not paste the entire incident into every instruction file.

## Verify

Rerun the failed/representative case.

If the change does not alter future behaviour, learning has not been implemented.

## Stop

Do not manufacture a separate lesson object if the real owner has already been corrected.
