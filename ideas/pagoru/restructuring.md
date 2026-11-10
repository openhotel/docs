# Restructure the OpenHotel org

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-10
- Related: [org overview](../../org/overview.md), [dependencies](../../org/dependencies.md), [todo](../../tasks/todo.md)

## Problem
~20 repos, 7 versions of `@oh/utils`, copied code (login flow x5, socket client x4, game shell x3), no shared CI, mixed licenses.

## Proposal: target layout (~8 active repos)
| Repo | Proposed fate |
|---|---|
| openhotel | stays; drops utils, inlines pathfinding, new socket, own updater |
| auth, onet, web, asset-editor, static | merge into one services monorepo, clients to Tailwind |
| web-components | merge as monorepo `packages/ui`, Tailwind |
| utils | kill: split into core / packages/server / openhotel / game-utils, archive |
| core | stays, love: single isomorphic lib + game event types |
| game-utils, game-template, battleship | stay, love: one shared game shell |
| pixi-components | stays, love |
| aseprite-scripts | stays, love (not reachable yet) |
| docs | stays: source of truth |
| devkit | reworked for the new layout |
| @da/socket | rewritten as binary org package |
| pathfinding | kill: inline into openhotel, archive |
| auth-example, captcha, at | kill: archive |
| queue, openhotel.github.io | undecided |

## Proposed phases
0. [Triage](triage.md) (any time)
1. [core](utils-split.md) gets the pure parts of utils
2. [Services monorepo](services-monorepo.md)
3. [openhotel off utils](utils-split.md) + inline pathfinding
4. [Archive + devkit](archive-devkit.md)
5. [Tailwind](services-monorepo.md)
6. [Socket rewrite](socket.md)
7. [Games and Pixi](games.md)
8. devkit follows every phase

5, 6, 7 can run in parallel after 1-3. Open points: [questions](questions.md).
