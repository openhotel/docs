# Dependency map

Server imports (deno.json), snapshot 2026-11-10.

| Consumer | @oh/utils | @oh/core | @oh/queue | @da/socket | other |
|---|---|---|---|---|---|
| openhotel | 1.5.24 (root pins 1.3.25) | 0.1.0 | 1.1.1 | 2.3.0 | @oh/pathfinding 2.0.3, @da/worker |
| auth | 1.5.32 | | 1.1.1 | | |
| onet | 1.5.33 | 0.1.0 | 1.1.1 | 2.3.0 | |
| web | 1.5.2 | | 1.1.1 | | |
| static | 1.5.32 | | | | |
| asset-editor | 1.5.0 | 0.1.0 | | | |
| game-template, battleship | yes | | game-template | 2.3.0 | |
| at (dead) | yes | | | | |

`@oh/utils` symbol usage: openhotel 36, auth 21, static 19, onet 17, web 15, asset-editor 12, at 10, game-template 8, battleship 6. Seven different versions in use.

## Client UI libs

| Consumer | pixi-components | web-components | React |
|---|---|---|---|
| openhotel | 0.1.9 | | 19 |
| game-template, battleship | 0.0.24 | | 19 |
| game-utils | 0.0.29 (peer) | | 19 |
| auth | | 0.3.9 | 18 |
| web, asset-editor | | 0.3.3 | 18 |
| static | | legacy `@oh/components` | 18 |

## Copied code (not shared as packages)
- Client `socket.utils.ts`: byte-identical in openhotel, game-template, battleship, game-utils.
- Login flow against auth: web, static, asset-editor (+ auth itself, OHAP example).
- static and asset-editor share ~20 identical server files (static was scaffolded from asset-editor).
- battleship is a copy of game-template plus game code (77 files differ).

## Pathfinding
Only `Grid` is used, in openhotel `rooms/public/room.ts` and `rooms/private/room.ts` (~445 lines lib).
