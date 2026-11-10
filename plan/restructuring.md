# Restructuring: decisions

Decided by Pablo on 2026-10-22. Source doc: https://claude.ai/artifact/6otaGWpMUBXBk99ZUp2Ky8. Status: planned, nothing executed yet.

| Repo | Fate | What happens |
|---|---|---|
| openhotel | stays | Drops `@oh/utils`, inlines pathfinding, new socket |
| auth, onet, web, asset-editor, static | merged | One services monorepo, clients to Tailwind |
| web-components | merged | Becomes `packages/ui`, Tailwind |
| utils | killed | Split into core / packages/server / openhotel / game-utils, archived |
| core | stays, love | Single shared isomorphic lib |
| game-utils | stays, love | Real game shell |
| game-template | stays, love | Built on game-utils + pixi-components + new socket |
| battleship | stays, love | Rebuilt on the same base |
| pixi-components | stays, love | Version, license, consumer cleanup |
| aseprite-scripts | stays, love | Not reachable yet |
| pathfinding | killed | Inlined into openhotel, archived |
| auth-example, captcha, at | killed | Archived |
| devkit | reworked | Runs openhotel + monorepo |
| @da/socket | rewritten | New binary socket lib in the org |
| queue, openhotel.github.io | undecided | |

End state: ~8 active repos instead of ~20.

## Monorepo layout (proposed)
```
apps/      auth, onet (server only), web, asset-editor, static
packages/  ui (was web-components), server (from utils),
           auth-client (shared login flow), config (Tailwind preset, tsconfig, prettier)
```
One Deno 2 workspace (servers) + one yarn 4 workspace (clients), one CI. Import repos with git history.

## Tailwind order
Preset in packages/config -> packages/ui -> web (~70 scss lines) -> static (~230) -> asset-editor (~470) -> auth (~730).

Next: [phases](phases.md).
