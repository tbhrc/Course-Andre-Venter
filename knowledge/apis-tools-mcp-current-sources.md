# APIs, Tools and MCP — Current Authoritative Sources

This page is a **source map**, not a copied vendor manual.

Verify current implementation details live before teaching or building against them.

## OpenAI tool sources

- Tools overview: https://developers.openai.com/learn/tools
- Using tools: https://developers.openai.com/api/docs/guides/tools
- MCP servers: https://developers.openai.com/api/docs/guides/tools-connectors-mcp
- Agents API MCP connections: https://developers.openai.com/api/docs/guides/agents-api/tools/mcp
- OpenAI Docs MCP: https://developers.openai.com/learn/docs-mcp
- OpenAI developer docs MCP endpoint: https://developers.openai.com/mcp

## MCP sources

- MCP TypeScript SDK: https://ts.sdk.modelcontextprotocol.io/v2/
- MCP Inspector: https://github.com/modelcontextprotocol/inspector
- MCP specification / documentation: https://modelcontextprotocol.io/

## Stable concepts

Learn these as durable architecture:

```text
API
= software interface exposed by a system

TOOL
= model-callable capability with a clear contract

FUNCTION/CUSTOM TOOL
= your application exposes a structured callable function

MCP
= standard client/server protocol for discovering and using tools/resources/prompts

CONNECTOR / NATIVE INTEGRATION
= prebuilt service-specific integration owned by a platform/provider
```

## Current OpenAI implementation notes

As of the current docs:

- OpenAI supports built-in tools, custom/function tools and MCP tools.
- Remote MCP servers can be connected to supported OpenAI APIs.
- Private/local MCP servers can be reached through supported environment/tunnel mechanisms.
- Tool lists can be narrowed with allowed-tool controls.
- Approval requirements can be configured for MCP actions.
- MCP tools may involve credentials/OAuth depending on the server.
- OpenAI provides an official developer-documentation MCP endpoint.

Treat exact model compatibility, field names, connector status, client UI and product limits as volatile.

## MCP implementation notes

Current MCP SDK/docs support:

- tools;
- resources;
- prompts;
- client/server discovery;
- stdio for local process integrations;
- HTTP transports for remote integrations;
- authorization/security mechanisms.

The protocol evolves. Do not hard-code the course to one dated protocol revision.

## Course rule

Teach:

```text
capability need
→ existing native/dedicated tool?
→ direct API/custom tool?
→ MCP when standard reusable discovery/connection adds value
→ smallest authorised surface
→ verify real result
```

Do not build another connector merely because MCP exists.
