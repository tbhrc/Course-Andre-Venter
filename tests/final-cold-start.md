# Final Cold-Start Test

## Purpose

Verify that a fresh capable agent can enter this repository with no prior conversation and correctly operate the course.

## Fresh-agent prompt

> Open this repository. Read the root AGENTS.md first. Do not assume prior conversation context. Tell me: (1) the purpose of the repository, (2) the first learning file a new learner should open, (3) the teaching loop, (4) the core architecture doctrine, (5) where reusable HOW belongs, (6) how current volatile provider facts should be handled, and (7) what proves course graduation. Do not edit anything.

## Expected evidence

The fresh agent should identify:

- practical Agentic AI builder course;
- `course/00-start-here.md`;
- explain → show → learner does → inspect → debug → verify → teach-back → keep artifact;
- one capable agent / smallest architecture before orchestration;
- reusable HOW in Skills;
- volatile public/product facts verified from live authoritative sources;
- graduation through independent build/verification/explanation, not reading completion.

## Failure conditions

Fail if the agent:

- starts at an arbitrary module;
- treats the repository as André-specific;
- recommends multi-agent first;
- says chat memory is authoritative state;
- treats every task as requiring an Issue/PR;
- copies volatile product facts instead of live verification;
- cannot locate graduation criteria.

## Repair rule

If the cold-start test fails:

1. identify the smallest routing/instruction gap;
2. fix only that gap;
3. rerun the same test once;
4. stop when the expected route is recovered.
