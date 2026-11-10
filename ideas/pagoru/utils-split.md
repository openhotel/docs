# Kill @oh/utils, grow core (phases 1 and 3)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-10
- Part of: [restructuring](restructuring.md). Facts: [utils](../../projects/utils.md), [core](../../projects/core.md)

## Proposed split
| utils part | Goes to |
|---|---|
| Point/Size/Direction, random, version compare, dates, base64, HttpStatusCode, RequestMethod | core |
| api, db, S3, tokens/encryption, config, migrations | monorepo `packages/server` |
| updater, parent side of process worker, OS helpers, yaml, copyDirectory | openhotel |
| child side of process worker, readYaml, getDb for games | game-utils |

## core (phase 1)
- Rule: no Deno APIs, runs in browser and server.
- Also owns hotel/game event types (USER_JOIN, USER_READY, USER_LEAVE) so openhotel and game-utils share one contract.
- README with exported API, one toolchain (drop Jest+Babel or deno test), tests in CI.

## openhotel (phase 3)
- Replace utils imports with core + local modules (root deno.json still pins utils 1.3.25).
- Own updater; fix stale client JS there ([utils#92](https://github.com/openhotel/utils/issues/92)).
- Game logging ([openhotel#1029](https://github.com/openhotel/openhotel/issues/1029)).
- Inline pathfinding (`Grid`, ~445 lines) under `app/server/src/shared/pathfinding/`.

## Issues absorbed
All 9 [utils issues](https://github.com/openhotel/utils/issues) move to packages/server or openhotel, or close with the archive.
