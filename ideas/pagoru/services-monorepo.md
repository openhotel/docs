# Services monorepo + Tailwind (phases 2 and 5)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-10
- Part of: [restructuring](restructuring.md). Facts: [architecture](../../org/architecture.md)

## Members
auth, onet, web, asset-editor, static, web-components. Name undecided ([questions](questions.md)).

## Layout
```
apps/      auth, onet (server only), web, asset-editor, static
packages/  ui (was web-components), server (from utils),
           auth-client (shared login flow), config (Tailwind preset, tsconfig, prettier)
```
- One Deno 2 workspace (servers), one yarn 4 workspace (clients), one CI.
- Import repos with git history; transfer open issues before archiving.

## packages
- **server**: api, db, S3, tokens, config, migrations from utils; one log system replacing [auth#432](https://github.com/openhotel/auth/issues/432), [auth#58](https://github.com/openhotel/auth/issues/58), [onet#46](https://github.com/openhotel/onet/issues/46), [web#9](https://github.com/openhotel/web/issues/9), [utils#90](https://github.com/openhotel/utils/issues/90); atomic db, useApi, migration traces.
- **auth-client**: one login flow for web, static, asset-editor.
- **ui**: re-file the 7 [web-components issues](https://github.com/openhotel/web-components/issues) that still apply.
- Cleanup: ~20 duplicated static/asset-editor server files, endpoint naming ([auth#177](https://github.com/openhotel/auth/issues/177)).

## Tailwind order (phase 5)
Preset in packages/config, then packages/ui, then web (~70 scss lines), static (~230), asset-editor (~470), auth (~730).
