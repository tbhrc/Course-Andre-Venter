# Module 9 — Model Context Protocol (MCP)

## Objective

Understand why MCP exists, how clients and servers interact, what an MCP server exposes, and when MCP is the right integration layer.

MCP is not “agents talking to agents.”

A useful mental model is:

```text
AI HOST / CLIENT
→ discovers capabilities
→ MCP SERVER
→ tools / resources / prompts
→ underlying system
```

For current implementation details, see [APIs, Tools and MCP — Current Sources](../knowledge/apis-tools-mcp-current-sources.md).

---

## 1. The integration problem

Without a common protocol, every AI client may need custom integration code for every system.

```text
client A → custom GitHub adapter
client B → different GitHub adapter
client C → another GitHub adapter
```

MCP can provide:

```text
GitHub MCP server
→ standard discoverable capability surface
→ multiple MCP-compatible clients
```

This does not automatically make MCP the best choice.

It makes standard reuse possible.

---

## 2. Client, host and server

### Host / AI application

The environment the user interacts with.

Examples may include coding agents, IDEs, AI applications or your own agent runtime.

### MCP client

The protocol component inside the host that connects to an MCP server.

### MCP server

A service/process exposing capabilities through MCP.

The server may be:

- local;
- remote;
- public;
- private;
- authenticated;
- read-only;
- action-capable.

---

## 3. Tools

Tools are callable operations.

Examples:

```text
search_issues(query)
create_issue(title, body)
get_customer(email)
send_message(channel, text)
```

A tool usually has:

- name;
- description;
- input schema;
- optional output schema;
- implementation.

The model uses tool metadata to decide whether/how to call it.

---

## 4. Resources

Resources are readable content/data exposed through MCP.

Examples:

- documents;
- files;
- schemas;
- reference records.

Think:

> read this content through a standard protocol.

A resource is not the same thing as a tool action.

---

## 5. Prompts

MCP servers can expose reusable prompt templates.

This is distinct from model tools.

Do not turn every piece of instructional content into an MCP prompt.

Use the primitive that matches the job.

---

## 6. Discovery

One important MCP advantage is that clients can discover the capabilities a server exposes.

Conceptually:

```text
connect
→ discover supported capabilities
→ list relevant tools/resources
→ choose/call
→ receive result
```

This reduces hard-coded client-specific integration logic.

---

## 7. Transport

Common MCP deployment shapes include:

### Local process

```text
AI client
→ stdio
→ local MCP server process
```

Useful when the server runs on the same machine/environment.

### Remote HTTP

```text
AI client
→ HTTP
→ remote MCP server
```

Useful for shared/network services.

Exact protocol versions/transports evolve. Verify current docs rather than memorizing a dated matrix.

---

## 8. Authentication

Remote MCP may require:

- OAuth;
- bearer tokens;
- other trusted headers/identity mechanisms.

The MCP server should receive only the authority needed for its job.

Never put real credentials into:

- `SKILL.md`;
- AGENTS.md;
- repository examples;
- logs;
- chat.

---

## 9. Tool narrowing

If a server exposes 100 tools but the agent needs 3, importing all 100 may:

- increase context;
- increase ambiguity;
- increase unintended action surface.

Use host/server filtering/narrowing mechanisms when available.

Expose the smallest useful capability surface.

---

## 10. Approval controls

Read vs write matters more than “MCP vs non-MCP.”

An MCP tool that deletes a record is still consequential.

An MCP tool that searches public docs is low consequence.

Where the host supports approval controls, align them with real action consequence.

Do not require human confirmation for every harmless lookup merely because MCP is involved.

---

## 11. MCP security mindset

A remote MCP server is an external capability boundary.

Ask:

- Do I trust the server/operator?
- What data enters its tools?
- What authority does it have?
- Could tool descriptions/content be malicious or misleading?
- Are tool outputs treated as untrusted external input?
- Is the server allowed to make writes?
- Are credentials scoped appropriately?

A protocol standard does not make a server trustworthy.

---

## 12. MCP vs API

MCP frequently sits **on top of APIs**.

Example:

```text
AI client
→ MCP tool: create_issue(...)
→ MCP server
→ GitHub API
→ GitHub
```

MCP does not replace the underlying service API.

It standardizes how AI clients discover and call the integration.

---

## 13. MCP vs Skill

A Skill teaches reusable **HOW**.

MCP provides executable **CAPABILITY / DATA ACCESS**.

Example:

```text
Skill:
how we triage customer complaints

MCP tools:
search_customer
read_order
create_support_case
```

The Skill decides the operating procedure.

The tools execute the allowed operations.

Do not confuse instruction with capability.

---

## 14. First MCP architecture

A good beginner architecture:

```text
learner
→ one MCP-compatible client
→ one trusted MCP server
→ one or two read-only tools
→ inspect tool list
→ call one tool
→ inspect result
```

Do not begin with:

- five servers;
- write access everywhere;
- OAuth for multiple services;
- a custom gateway;
- multi-agent routing.

Prove the basic connection first.

---

## 15. When to build an MCP server

Build/operate one when:

- the capability should be reusable across MCP clients;
- a coherent system has several related tools/resources;
- discovery provides real value;
- an authoritative MCP server does not already exist;
- direct API wrappers would otherwise be repeatedly reimplemented.

Do not build one when:

- one tiny local function is enough;
- a dedicated native integration already exists;
- there is no reuse;
- it becomes a second source of truth.

---

## Practical work

Complete:

1. [Lab 09 — First MCP Connection](../labs/09-first-mcp-connection.md)
2. [MCP inspection playbook](../playbooks/mcp-inspection.md)
3. Revisit [Tool/API/MCP Decision](../playbooks/tool-api-mcp-decision.md)

## Teach-back

Explain without notes:

1. MCP client vs server?
2. Tool vs resource?
3. MCP vs direct API?
4. MCP vs Skill?
5. Why is discovery valuable?
6. Why does an MCP server still need trust/security review?
7. When is MCP unnecessary?

## Pass condition

You can connect to one trusted MCP server, inspect its exposed capability surface, call one read-only tool, explain the result, and decide whether MCP materially improves the integration.

## Your next step

Once the practical work and teach-back for this module are complete, record the evidence and exact next action in your own `work/progress.md`. If something still needs practice, continue that step before advancing.

**Next:** [10. Context, memory, state and data](10-context-memory-state-data.md) · **[Full curriculum and estimated study plan](../COURSE.md)**
