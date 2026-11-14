# One monorepo: openhotel/openhotel (phases 1 and 4)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: openhotel, auth, onet, web, asset-editor, static, core, utils, web-components, pathfinding
- Discussion: none

## Summary
Part of [restructuring](restructuring.md). The monorepo is the existing `openhotel/openhotel`; everything lives under `app/`. Facts: [architecture](../../org/architecture.md), [openhotel](../../projects/openhotel.md).

## Proposal: layout
```
app/
  client/        game client (already here)
  server/        hotel server (already here), pathfinding inside
  auth/          server/ + client/
  onet/          server only
  web/           server/ + client/
  asset-editor/  server/ + client/
  static/        server/ + client/
  shared/        @oh/core + @oh/utils merged, see shared.md
  ui/            was web-components, Tailwind (+ Tailwind preset)
```
- Keeping `openhotel/openhotel` keeps its stars, 103 issues, releases and history; game paths do not move.
- One Deno 2 workspace (servers + shared), one yarn 4 workspace (clients + ui), one CI.
- Apps import `app/shared` from the workspace: no more version drift (7 utils versions today).
- Import the other repos with git history (subtree / filter-repo into `app/<name>`).
- All open issues move here too: see [issues](issues.md).

## Dedupe inside the monorepo
- Login flow against auth (copied in web, static, asset-editor) -> one helper in `app/shared`.
- ~20 duplicated static/asset-editor server files.
- One log system replacing [openhotel#1029](https://github.com/openhotel/openhotel/issues/1029), [auth#432](https://github.com/openhotel/auth/issues/432), [auth#58](https://github.com/openhotel/auth/issues/58), [onet#46](https://github.com/openhotel/onet/issues/46), [web#9](https://github.com/openhotel/web/issues/9), [utils#90](https://github.com/openhotel/utils/issues/90).
- Endpoint naming ([auth#177](https://github.com/openhotel/auth/issues/177)).

## Tailwind (phase 4)
Preset in `app/ui`, then the ui components (~1,970 scss lines), then web (~70), static (~230), asset-editor (~470), auth (~730). The game client uses Pixi, not affected.
