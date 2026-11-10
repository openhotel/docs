# onet

Repo: github.com/openhotel/onet · last tag v0.4.2 · no license file · active.

**OpenHotel Messaging Protocol (OHMP)**: the network that links hotels. Server only, no client.

## What it does
- Hotels connect as WebSocket clients (`@da/socket`), protocols `[hotelId, licenseToken]`; onet validates with auth. Events today: `welcome` (hotel side also handles connected, disconnected, reconnecting).
- HTTP `/api/v1`: `version`, `auth/check`, `auth/collections`, `collections` (list, manifest, files), `teleports` (get, link).
- **Collections**: furniture/asset packs with signatures (`system/collections/signature.ts`), types from `@oh/core`.
- **Teleports**: link a teleport in one hotel to another hotel.
- Storage: Deno KV (`--unstable-kv`), cron jobs (`--unstable-cron`), migrations.

## Layout
Root `mod.ts` + `src/modules/{api/v1, system/{hotels,collections,teleports,auth,api,server-socket}, migrations}` + `src/shared`.

## Run
`deno task start` (port 9400 in devkit). `deno task build` makes binaries for 4 targets.

## Plan
Merged into the services monorepo (server only). Moves to the new binary socket. See [restructuring](../plan/restructuring.md).
