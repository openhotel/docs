# app/shared: core and utils as one project (phase 2)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: core, utils, pathfinding, openhotel and every service
- Discussion: none

## Summary
Part of [restructuring](restructuring.md). `@oh/core` and `@oh/utils` merge into one project, `app/shared`, inside [the monorepo](monorepo.md). Facts: [utils](../../projects/utils.md), [core](../../projects/core.md).

## Proposal
One project, two entry points so browser code never pulls Deno APIs:

| Entry | Holds | Runs in |
|---|---|---|
| `shared` (root / `./core`) | types, consts, validators, pure helpers (Point/Size/Direction, random, version compare, dates, base64, HttpStatusCode, RequestMethod), hotel/game event types (USER_JOIN, USER_READY, USER_LEAVE) | browser + server |
| `shared/server` | api, db, S3, tokens/encryption, config, migrations, workers/process workers, updater, yaml, OS helpers, login flow, log system | server only |

- One toolchain (core has both Jest+Babel and deno test today), tests in CI, README with exported API.
- Published to JSR (name open, see [questions](questions.md)) for game-utils, game-template, battleship.
- core and utils repos archived after the import.

## pathfinding
Only `Grid` is used, in hotel rooms. Inline the ~445 lines under `app/server/src/shared/pathfinding/`, close [pathfinding#26](https://github.com/openhotel/pathfinding/issues/26) / [pathfinding#27](https://github.com/openhotel/pathfinding/pull/27), archive the repo.

## Hotel
- Updater fix for stale client JS ([utils#92](https://github.com/openhotel/utils/issues/92)) lands in `shared/server`.
- Root deno.json pin to utils 1.3.25 disappears with the workspace.
