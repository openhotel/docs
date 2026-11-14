# One monorepo for client, services and shared libs (phases 1 and 4)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: openhotel, auth, onet, web, asset-editor, static, core, utils, web-components, pathfinding
- Discussion: none

## Summary
Part of [restructuring](restructuring.md). One repo, name open ([questions](questions.md)). Facts: [architecture](../../org/architecture.md).

## Proposal: layout
```
apps/
  client/        was openhotel (hotel server + game client), pathfinding inside
  auth/
  onet/          server only
  web/
  asset-editor/
  static/
packages/
  core/          @oh/core: isomorphic types, consts, validators
  utils/         @oh/utils: server runtime (api, db, S3, config, workers, updater)
  ui/            was web-components, Tailwind
  config/        Tailwind preset, tsconfig, prettier
```
- One Deno 2 workspace (servers + core/utils), one yarn 4 workspace (clients + ui), one CI, one lockfile each.
- Apps import `@oh/core` / `@oh/utils` from the workspace: no more version drift (7 utils versions today).
- core and utils keep publishing to JSR from the monorepo, for games outside it.
- Import repos with git history; transfer open issues before archiving the old repos.

## Dedupe inside the monorepo
- Login flow against auth (copied in web, static, asset-editor) -> one helper in `packages/utils`.
- ~20 duplicated static/asset-editor server files.
- One log system replacing [openhotel#1029](https://github.com/openhotel/openhotel/issues/1029), [auth#432](https://github.com/openhotel/auth/issues/432), [auth#58](https://github.com/openhotel/auth/issues/58), [onet#46](https://github.com/openhotel/onet/issues/46), [web#9](https://github.com/openhotel/web/issues/9), [utils#90](https://github.com/openhotel/utils/issues/90).
- Endpoint naming ([auth#177](https://github.com/openhotel/auth/issues/177)).

## Tailwind (phase 4)
Preset in `packages/config`, then `packages/ui` (~1,970 scss lines), then web (~70), static (~230), asset-editor (~470), auth (~730). `apps/client` uses Pixi, not affected. Re-file the 7 [web-components issues](https://github.com/openhotel/web-components/issues) that still apply.
