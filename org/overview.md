# Org overview

GitHub org `openhotel`. Goal: an open, self-hostable virtual hotel / social game where anyone can run a hotel, credits come from mini-games, nothing is pay-to-win. Snapshot 2026-11-10. Last tag in brackets.

| Repo | Kind | Status | Role |
|---|---|---|---|
| openhotel [v0.8.6] | service | active | The game: hotel server (Deno) + client (React + Pixi). See [openhotel](../projects/openhotel.md) |
| auth [v0.11.1] | service | active | Accounts, sessions, hotel licenses, OHAP. See [auth](../projects/auth.md) |
| onet [v0.4.2] | service | active | Inter-hotel network (OHMP). See [onet](../projects/onet.md) |
| web [v0.3.2] | service | idle since 2025-10, live | Public site. See [web](../projects/web.md) |
| static [v0.0.10] | service | active | S3 file host. See [static](../projects/static.md) |
| asset-editor [v0.1.5] | service | active | Furniture/collection editor. See [asset-editor](../projects/asset-editor.md) |
| core | lib (JSR `@oh/core`) | new, Oct 2026 | Shared isomorphic types. See [core](../projects/core.md) |
| utils | lib (JSR `@oh/utils`) | active, to kill | Server helpers. See [utils](../projects/utils.md) |
| pixi-components | lib (npm) | active | Pixi + React game UI. See [ui-libs](../projects/ui-libs.md) |
| web-components | lib (npm) | active | React + Sass web UI. See [ui-libs](../projects/ui-libs.md) |
| game-utils | lib (JSR `@oh/game-utils`) | no consumers | Game shell. See [games](../projects/games.md) |
| pathfinding | lib (JSR `@oh/pathfinding`) | stale 2024 | Jump-point pathfinding. See [small-libs](../projects/small-libs.md) |
| queue | lib (JSR `@oh/queue`, named `@tu/queue` inside) | stale 2024 | Ticker/queue. See [small-libs](../projects/small-libs.md) |
| game-template | template | active | Base for mini-games. See [games](../projects/games.md) |
| battleship | game | 2026-05 | First game on the template. See [games](../projects/games.md) |
| devkit | tool | new, Oct 2026 | Docker local stack. See [devkit](../projects/devkit.md) |
| docs | docs | new | This repo |
| .github | meta | | Org profile + CONTRIBUTING. See [misc](../projects/misc.md) |
| auth-example, at, openhotel.github.io | dead | | See [misc](../projects/misc.md) |
| aseprite-scripts, captcha, art | unreachable | | Linked from profile, not clonable. See [misc](../projects/misc.md) |

## Relationship in one picture

```
            players (browser)
                 |
   web ----> auth <---- every service checks tokens here
                 |  ^
   hotel client  |  | license-token / connection-token
        |  ws    |  |
   openhotel server ---ws/http---> onet (network of hotels)
        |  spawns
   games (game-template based)

   asset-editor, static: content tooling, both log in via auth
   libs: core, utils, queue, pathfinding, @da/socket, pixi/web-components
```

Details: [architecture](architecture.md), [dependencies](dependencies.md).
