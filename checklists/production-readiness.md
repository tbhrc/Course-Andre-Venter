# Production Readiness Checklist

Use only the sections relevant to the real system.

## Outcome

- [ ] user/problem owner identified;
- [ ] measurable useful outcome;
- [ ] production acceptance defined.

## Reliability

- [ ] representative evals;
- [ ] known regressions;
- [ ] material failures have defined paths;
- [ ] verification is not agent self-report only.

## State

- [ ] authoritative owners defined;
- [ ] writes are verifiable;
- [ ] retry/replay duplication considered;
- [ ] backup/checkpoint/restore considered where needed.

## Security

- [ ] secrets outside source/prompts;
- [ ] authentication/roles appropriate;
- [ ] untrusted content handled;
- [ ] consequential actions controlled;
- [ ] privacy/external processors understood.

## Observability

- [ ] run can be traced;
- [ ] errors/tool calls visible;
- [ ] enough evidence exists to diagnose;
- [ ] no unnecessary sensitive logging.

## Performance

- [ ] latency measured if it affects UX;
- [ ] rate/concurrency limits understood;
- [ ] cost per useful outcome understood where material.

## Deployment

- [ ] runtime/deployment owner;
- [ ] configuration path;
- [ ] launch verification;
- [ ] rollback/recovery path;
- [ ] version/change process proportional to risk.

## User experience

- [ ] useful success state;
- [ ] useful error state;
- [ ] approvals understandable;
- [ ] recovery path understandable.

## Support

- [ ] owner for incidents;
- [ ] feedback path;
- [ ] next improvement driven by observed use.

## KISSS

Remove any checklist item that is genuinely irrelevant to the system.

Do not build infrastructure merely to tick a box.
