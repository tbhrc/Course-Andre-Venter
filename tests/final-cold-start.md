# Course Startup and Continuation Acceptance Cases

## Purpose

Verify the real learner-facing opening for André’s personalized track with Course-Agentic-AI as the general curriculum owner: curriculum first, teaching next, existing evidence reused.

## Case 1 — New learner, supplied background, no baseline file

Start a fresh course session using:

> Read AGENTS.md, COURSE.md and LEARNER-PROFILE.md first. Act as David AI Coach. I have supplied my background. Show me what I will learn, the roadmap, how long to allow and what we do next. Start teaching; do not give me an intake questionnaire.

Expected opening:

- Introduces **David AI Coach** as an AI tutor.
- Links [COURSE.md](../COURSE.md), shows the ordered modules and their outcomes/practical results.
- Explains the **50–75 active-hour** planning estimate and **10–15 weeks at 5 hours/week**, with adaptable pacing.
- Shows current module, today's outcome, session estimate, expected output and next lesson.
- Reuses supplied background and begins Module 1 with an explanation and worked example before one exercise.
- Does not require `work/00-baseline.md` or ask eight questions, together or sequentially, before teaching.

## Case 2 — Learner already answered the old eight questions

Supply the existing answers, then ask:

> I already answered your questions. Where is my course and what should I learn next?

Expected: preserves those answers as evidence, shows the roadmap and next lesson, and starts teaching. No repeated interview or requirement to recreate the baseline.

## Case 3 — Returning learner with practical progress

Supply `work/progress.md` and relevant artifacts showing the current module and unfinished step, then ask:

> Continue my course from where I stopped.

Expected: resumes the evidenced step, shows today's outcome and next lesson, and revises the remaining estimate. Does not restart Module 0 or infer mastery solely from a CV or questionnaire answers.

## Case 4 — Repository access unavailable

Expected: states the access limitation and asks for only the instructions/roadmap/current lesson needed. Does not invent file access, saved progress, a curriculum or completion.

## Failure and repair

Fail an opening that withholds the curriculum, starts with a baseline questionnaire, requires a baseline file, repeats supplied CV/background, invents mastery, or presents the study estimate as a guaranteed duration.

Repair the smallest conflicting instruction, then repeat the failed case. These are behavioral acceptance cases; document inspection alone is not proof of a live learner-session pass.
