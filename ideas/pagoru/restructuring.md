# Restructure the OpenHotel org

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: openhotel, auth, onet, web, asset-editor, static, core, utils, web-components, pathfinding
- Discussion: none

## Summary
Turn `openhotel/openhotel` into **the monorepo**: game, every service and the shared code under `app/`, and all issues in one tracker. Games, Pixi kit and tooling stay outside.

## Motivation
~20 repos, 7 versions of `@oh/utils`, copied code (login flow x5, socket client x4, game shell x3), no shared CI, mixed licenses. See [overview](../../org/overview.md), [dependencies](../../org/dependencies.md), [todo](../../tasks/todo.md).

## Proposal: target layout
| Repo | Proposed fate |
|---|---|
| openhotel | **is** the monorepo; game stays in `app/client` + `app/server`, pathfinding inlined |
| auth, onet, web, asset-editor, static | into the monorepo as `app/<name>` |
| core + utils | merged into one project, `app/shared` |
| web-components | into the monorepo as `app/ui`, rewritten to Tailwind |
| pathfinding | inlined in `app/server`, repo archived |
| game-utils, game-template, battleship | stay outside, love: one shared game shell |
| pixi-components | stays outside, love |
| aseprite-scripts | stays, love (not reachable yet) |
| docs | stays: source of truth |
| devkit | reworked to run the monorepo |
| @da/socket | rewritten as binary org package |
| auth-example, captcha, at | archived |
| queue, openhotel.github.io | undecided |

Details: [monorepo](monorepo.md), [app/shared](shared.md), [issues](issues.md).

## Proposed phases
0. [Triage](triage.md) (any time)
1. [Monorepo](monorepo.md): import 8 repos into `openhotel/openhotel` with history, workspaces, one CI; [move issues](issues.md)
2. [app/shared](shared.md): merge core + utils, everyone on the workspace, dedupe, inline pathfinding
3. [Archive + devkit](archive-devkit.md)
4. Tailwind ([monorepo](monorepo.md))
5. [Socket rewrite](socket.md)
6. [Games and Pixi](games.md)

4, 5, 6 can run in parallel after 1-3. devkit follows every phase.

## Open questions
See [questions](questions.md).
