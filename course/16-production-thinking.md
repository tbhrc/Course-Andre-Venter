# Module 16 — Production Thinking

## Objective

Understand what changes when an agent moves from a successful demo to repeated real use.

Production does not mean:

> Add Kubernetes, dashboards and enterprise architecture.

Production means the system can be operated reliably enough for its real users and consequences.

For current provider guidance, see [Architecture and Production Current Sources](../knowledge/architecture-production-current-sources.md).

---

## 1. Start with actual usage

Ask:

- who uses it?
- how often?
- what volume?
- what consequence?
- what uptime matters?
- what latency is acceptable?
- what cost is acceptable?
- who supports it?

Do not design for imaginary scale.

---

## 2. Reliability

Production needs:

- representative evals;
- regression cases;
- known failure behavior;
- clear terminal failure;
- fallback/recovery where needed.

A demo that works once is not enough.

---

## 3. Observability

You should be able to locate:

- request/run;
- model calls;
- tool calls;
- routing/handoffs;
- errors;
- state changes;
- final outcome.

Use current platform/runtime tracing where it already provides this.

Do not build a second telemetry stack without a gap.

---

## 4. Security

Production review includes:

- secrets;
- identity/authentication;
- role/authority;
- privacy;
- untrusted input;
- external tool/data processors;
- consequential writes;
- dependency/supply-chain risk.

Match controls to the actual role.

---

## 5. State and durability

Know:

- what must persist;
- where it persists;
- backups/checkpoints;
- restore/recovery;
- idempotency/replay risks;
- migration/versioning.

---

## 6. Rate limits and quotas

External systems have limits.

Production workflows should understand:

- provider rate limits;
- concurrency;
- retry behavior;
- backoff;
- quota exhaustion;
- user-visible fallback.

Do not blind-retry writes.

---

## 7. Latency

Measure end-to-end user value.

Possible contributors:

- model reasoning;
- tool/API latency;
- sequential dependencies;
- unnecessary context;
- slow external systems;
- avoidable orchestration.

Optimize measured bottlenecks.

---

## 8. Cost

Track cost per useful outcome where it matters.

Potential costs:

- model tokens;
- tool/API calls;
- external data;
- infrastructure;
- human review;
- failure/rework.

Cheapest model is not always lowest cost per successful task.

---

## 9. Model/version changes

Models and providers change.

Before switching:

- run representative evals;
- compare quality;
- compare tool behavior;
- compare latency/cost;
- inspect regressions.

Do not upgrade solely because a model is newer.

---

## 10. Deployment and rollback

Define:

```text
what is deployed?
where?
how is config supplied?
how do we verify launch?
how do we roll back?
what state survives rollback?
```

Use the simplest deployment that meets the real workload.

---

## 11. Failure recovery

Examples:

- external API unavailable;
- model request fails;
- tool partially writes;
- state becomes inconsistent;
- worker restarts;
- quota exhausted.

Decide which require:

- retry;
- resume;
- repair;
- fallback;
- human intervention;
- terminal failure.

---

## 12. User experience

A technically correct system can still be poor.

Users need:

- clear state;
- useful errors;
- predictable waiting;
- understandable approvals;
- recovery path;
- trust in what was actually done.

---

## 13. Ownership

Someone must own:

- business outcome;
- application/runtime;
- source systems;
- incidents;
- changes;
- user feedback.

"AI owns it" is not an operating model.

---

## 14. Production hardening order

Use:

```text
real proof
→ representative users
→ observe failures
→ harden actual failure surfaces
→ measure
→ scale only when needed
```

Avoid front-loading speculative infrastructure.

---

## Practical work

Use [Production Readiness Checklist](../checklists/production-readiness.md) against your capstone.

## Pass condition

You can distinguish demo proof from production requirements and identify the smallest additional hardening needed for your actual capstone workload.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [Final graduation challenge](../GRADUATION-ANDRE.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
