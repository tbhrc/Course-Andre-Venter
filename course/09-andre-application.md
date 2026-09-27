# André Application — Module 9: MCP as a Standard Connection Layer

This file personalizes the canonical [Module 9](09-mcp.md) for André.

## Think of MCP as a standardized equipment interface

You already understand the value of standard connectors and protocols.

Without a standard:

```text
controller A needs custom wiring
controller B needs different custom wiring
controller C needs another custom interface
```

With a standard interface:

```text
one equipment interface
→ multiple compatible controllers
```

MCP applies that idea to AI clients and tool/data systems.

## Mapping

| MCP concept | Technical analogy |
|---|---|
| MCP host/client | control system / operator console |
| MCP server | equipment interface/controller |
| tool | command/function |
| resource | readable sensor/reference data |
| prompt | reusable guided operating template |
| discovery | querying what capabilities are available |
| schema | command parameter contract |
| transport | physical/network communication channel |
| authentication | authorized service/operator identity |

## Important boundary

Standardized connection does **not** mean standardized trust.

A physically compatible part can still be unsafe or wrong for the machine.

Likewise:

> An MCP server being connectable does not mean it should receive your data or credentials.

Always inspect the operator, authority, tools and data boundary.

## Exercise A — decide whether MCP is justified

For each case choose:

```text
native tool
direct API/custom tool
MCP
```

### Case 1

One small script needs to read one public status endpoint once.

### Case 2

Multiple AI clients need access to the same maintenance knowledge system with:
- search manuals;
- retrieve fault procedures;
- create vendor handover;
- inspect equipment history.

### Case 3

Your AI already has an official Google Drive connector that performs the exact required file operation.

### Case 4

You have one Python function that converts BPM to beat duration.

Explain your choice.

## Exercise B — design a future maintenance MCP

Do not build it yet.

Sketch:

```text
maintenance-mcp
├── search_fault_history
├── get_machine_manual
├── get_work_order
└── create_vendor_handover
```

Then challenge it:

- Does every function really belong?
- Which are read-only?
- Which system owns the data?
- Does an existing vendor API already solve this?
- Should create_vendor_handover be a Skill instead of a tool?
- Which capability is reusable across multiple AI clients?

## Exercise C — Skill vs MCP

Use this split:

```text
Skill
= HOW to troubleshoot/escalate

MCP
= ACCESS to fault history, manual, work orders, vendor system
```

This distinction is important.

Do not encode the entire troubleshooting method inside an MCP server if it belongs in a reusable Skill.

Do not expect a Skill to access live machine history without an actual tool/data connection.

## Your target

You should be able to explain:

> MCP is useful when I want a reusable standard capability surface for AI clients. It does not replace the underlying API, source system, Skill, security model or business procedure.
