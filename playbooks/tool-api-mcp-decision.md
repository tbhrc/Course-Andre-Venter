# Playbook — Native Tool vs Direct API vs MCP

## Objective

Choose the smallest connection architecture that solves the real problem.

## Decision path

```text
NEED
→ dedicated authorised/native tool already exists?
   YES
   → use it directly
   → verify result
   → stop

   NO
   → one bounded stable API/function enough?
      YES
      → use/build the smallest direct wrapper
      → verify
      → stop

      NO
      → multiple clients/agents need reusable discovery?
      → many related tools/resources belong behind one capability?
      → standardized connection materially reduces custom glue?
         YES
         → consider MCP
         → expose only necessary capabilities
         → verify discovery + real call
         → stop
```

## Prefer native/dedicated integration when

- the service is already connected;
- auth is already managed;
- the exact operation exists;
- it is the authoritative supported route.

## Prefer direct API/custom tool when

- one or a few operations are needed;
- the contract is stable and simple;
- only one application owns the integration;
- MCP would add packaging/transport/discovery work without reuse value.

## Prefer MCP when

- multiple agent clients should discover the same capability;
- a coherent system exposes several tools/resources;
- portable standardized discovery is useful;
- an existing authoritative MCP server already exists;
- the service integration would otherwise be repeatedly rebuilt.

## Do not choose MCP because

- it sounds more agentic;
- every function must become a server;
- you want another control plane;
- a dedicated integration already solves the job.

## Real-boundary questions

Before action:

- What data leaves the current system?
- Which identity/credential is used?
- Is this read, write or destructive?
- Is there spend?
- Is the external processor appropriate for this data?
- What authoritative state changes?
- Can the result be verified?

## KISSS

```text
dedicated tool
→ direct API/tool
→ MCP only when standardization/reuse earns it
```
