# Lab 09 — First MCP Connection

## Objective

Connect to one trusted remote MCP server, inspect its tools, and perform one bounded read.

This lab uses the official OpenAI developer-documentation MCP endpoint:

```text
https://developers.openai.com/mcp
```

Verify the endpoint from the current OpenAI developer docs before use.

It is chosen because the course needs a low-consequence documentation lookup rather than access to personal/business data.

---

## Option A — Your MCP-compatible AI client

If your AI client supports remote MCP servers:

1. read its current official instructions for adding a remote HTTP MCP server;
2. add a server named something clear such as `openai_docs`;
3. use the verified endpoint above;
4. connect;
5. inspect the available tools;
6. ask the client to use the documentation server to answer:

> What categories of tools does the current OpenAI API documentation describe?

Require the answer to identify its MCP/tool evidence.

Do not add credentials if the official docs server does not require them.

---

## Option B — MCP Inspector CLI

If you have a compatible current Node.js environment, use the official MCP Inspector.

First verify the Inspector's current requirements/docs.

Then list tools from the remote server using the current Streamable HTTP syntax documented by the Inspector.

Conceptually:

```text
MCP Inspector
→ OpenAI Docs MCP
→ tools/list
```

Do not memorize this course's command if current Inspector syntax has changed—check the live Inspector docs.

---

## What to inspect

Record:

```text
Server:
Transport:
Authentication:
Tool names:
Which tool looks relevant?
Read/write consequence:
```

Then call one documentation search/read tool.

---

## Security reflection

Why is this a suitable first server?

- trusted identifiable operator;
- documentation use case;
- no business write;
- no private client/customer data required.

Now imagine replacing it with an unknown server that asks for your email token.

List at least five questions you would ask before connecting.

---

## MCP vs direct web/API reflection

Could you search OpenAI docs without MCP?

Yes.

Then why use MCP here?

The learning objective is to understand:

- standardized discovery;
- model-callable tools;
- reusable connection;
- how a compatible client can use the same server without custom per-tool HTTP code.

MCP must earn its place in real projects.

---

## Completion artifact

Create:

```text
work/09-first-mcp-result.md
```

Include:

- verified server owner;
- endpoint source;
- transport;
- tools discovered;
- tool called;
- arguments;
- result summary;
- why the server was trusted;
- why this MCP connection was or was not more useful than a direct lookup.

## Pass condition

You can explain the entire path:

```text
user request
→ AI host/client
→ MCP tool discovery
→ selected tool
→ MCP server
→ authoritative documentation
→ tool result
→ model response
```
