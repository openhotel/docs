# Shared packages: core and utils inside the monorepo (phase 2)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: core, utils, pathfinding, openhotel and every service
- Discussion: none

## Summary
Part of [restructuring](restructuring.md). `@oh/core` and `@oh/utils` both live in [the monorepo](monorepo.md) as workspace packages. utils is no longer killed. Facts: [utils](../../projects/utils.md), [core](../../projects/core.md).

## Proposal
| Package | Holds | Rule |
|---|---|---|
| `packages/core` | types, consts, validators, pure helpers (Point/Size/Direction, random, version compare, dates, base64, HttpStatusCode, RequestMethod), hotel/game event types (USER_JOIN, USER_READY, USER_LEAVE) | no Deno APIs: browser + server |
| `packages/utils` | api, db, S3, tokens/encryption, config, migrations, workers/process workers, updater, yaml, OS helpers, shared login flow, log system | server only |

- Pure parts currently in utils move to core; utils imports them from core.
- One toolchain per package (core has both Jest+Babel and deno test today), tests in CI, README with exported API.
- Keep publishing both to JSR for game-utils, game-template, battleship.

## pathfinding
Only `Grid` is used, in client rooms. Inline the ~445 lines under `apps/client/app/server/src/shared/pathfinding/`, close [pathfinding#26](https://github.com/openhotel/pathfinding/issues/26) / [pathfinding#27](https://github.com/openhotel/pathfinding/pull/27), archive the repo.

## Client
- Updater fix for stale client JS ([utils#92](https://github.com/openhotel/utils/issues/92)) lands in `packages/utils`.
- Root deno.json pin to utils 1.3.25 disappears with the workspace.

## Issues absorbed
All 9 [utils issues](https://github.com/openhotel/utils/issues) and the [core issues](https://github.com/openhotel/core/issues) transfer to the monorepo.
