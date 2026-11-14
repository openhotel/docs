# Restructure the OpenHotel org

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: openhotel, auth, onet, web, asset-editor, static, core, utils, web-components, pathfinding
- Discussion: none

## Summary
Move the game client and every service into **one monorepo** that also holds the shared libraries (`@oh/core`, `@oh/utils`, UI kit). Games, Pixi kit and tooling stay outside.

## Motivation
~20 repos, 7 versions of `@oh/utils`, copied code (login flow x5, socket client x4, game shell x3), no shared CI, mixed licenses. See [overview](../../org/overview.md), [dependencies](../../org/dependencies.md), [todo](../../tasks/todo.md).

## Proposal: target layout
| Repo | Proposed fate |
|---|---|
| openhotel (client) | into the monorepo as `apps/client`; pathfinding inlined |
| auth, onet, web, asset-editor, static | into the monorepo as `apps/*` |
| core (`@oh/core`) | into the monorepo as `packages/core` |
| utils (`@oh/utils`) | into the monorepo as `packages/utils` (no longer killed) |
| web-components | into the monorepo as `packages/ui`, rewritten to Tailwind |
| pathfinding | inlined in `apps/client`, repo archived |
| game-utils, game-template, battleship | stay outside, love: one shared game shell |
| pixi-components | stays outside, love |
| aseprite-scripts | stays, love (not reachable yet) |
| docs | stays: source of truth |
| devkit | reworked to run the monorepo |
| @da/socket | rewritten as binary org package |
| auth-example, captcha, at | archived |
| queue, openhotel.github.io | undecided |

Details: [monorepo](monorepo.md), [shared packages](shared-packages.md).

## Proposed phases
0. [Triage](triage.md) (any time)
1. [Monorepo](monorepo.md): import the 9 repos with history, workspaces, one CI
2. [Shared packages](shared-packages.md): everyone on workspace core/utils, dedupe, inline pathfinding
3. [Archive + devkit](archive-devkit.md)
4. Tailwind ([monorepo](monorepo.md))
5. [Socket rewrite](socket.md)
6. [Games and Pixi](games.md)

4, 5, 6 can run in parallel after 1-3. devkit follows every phase.

## Open questions
See [questions](questions.md).
