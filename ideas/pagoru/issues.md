# All issues in openhotel/openhotel

- Author: pagoru
- Status: proposed
- Created: 2026-11-14 · Updated: 2026-11-14
- Affects: every repo with issues
- Discussion: none

## Summary
Part of [restructuring](restructuring.md). Move every open issue from the other repos into `openhotel/openhotel`, the [monorepo](monorepo.md), so there is one tracker.

## Scope (snapshot 2026-11-10, see [todo](../../tasks/todo.md))
~92 open issues outside openhotel: auth 36, static 12, utils 9, pixi-components 8, web-components 7, asset-editor 7, onet 5, game-template 2, pathfinding 2, auth-example 2, web 1, devkit 1. Closed issues stay where they are.

## Proposal
- Use GitHub **issue transfer** (`gh issue transfer <n> openhotel/openhotel -R openhotel/<repo>`): keeps author, comments, reactions, assignees; old URL redirects. Labels and milestones that do not exist in the target are dropped, so create them first.
- Before: one shared label set, plus a `repo:<name>` / `app:<name>` label per source so issues stay filterable.
- After transfer: add the source label, and a mention of the original number in the body if not kept.
- Skip repos being archived as dead (auth-example, pathfinding): close their issues instead.
- Do repos that stay outside the monorepo (pixi-components, game-template, devkit) only if the single tracker is meant for the whole org ([questions](questions.md)).
- Run as a script, dry-run first (list what moves), then repo by repo.
