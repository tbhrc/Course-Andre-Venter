# Playbook — Inspect an MCP Server Before Using It

## 1. Identify the owner

Before connection:

- who operates the server?
- what system does it represent?
- is there an official/authoritative server?

## 2. Inspect current documentation

Verify:

- endpoint/launch command;
- transport;
- authentication;
- capability purpose;
- current security notes.

Do not rely on a copied endpoint from an old tutorial.

## 3. Connect with smallest authority

Prefer:

- read-only first;
- no credential when the trusted server supports anonymous read access;
- narrowly scoped credential when auth is required.

## 4. Discover capabilities

Inspect:

- server identity;
- tool list;
- resource list if relevant;
- prompts if relevant.

Do not call tools yet.

## 5. Review tool contracts

For each tool you may call:

- name;
- description;
- input schema;
- output/side effect;
- read/write consequence.

## 6. Narrow

If the client supports allowed-tool filtering, expose/import only the subset needed for the task.

## 7. Call one bounded tool

Start with one low-consequence read.

Inspect:

- exact arguments;
- returned data;
- errors;
- provenance.

## 8. Verify result

Transport success is not enough.

Ask:

> Did the tool return useful/correct data from the intended authoritative source?

## 9. Stop

Do not add more servers or write privileges merely because the first connection worked.
