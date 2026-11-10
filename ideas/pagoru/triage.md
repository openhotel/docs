# Phase 0: triage before restructuring

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-10
- Part of: [restructuring](restructuring.md). Sources: [todo](../../tasks/todo.md), [prs](../../tasks/prs.md)

## Critical: fix now in current repos, port during the split
- [auth#447](https://github.com/openhotel/auth/issues/447) + [utils#119](https://github.com/openhotel/utils/issues/119): email encryption, encrypt/decrypt headers.
- [auth#422](https://github.com/openhotel/auth/issues/422): cap verification emails, then delete account.
- [onet#19](https://github.com/openhotel/onet/issues/19): `ip:port` rejected as URL.
- [web-components#132](https://github.com/openhotel/web-components/issues/132) + [auth#450](https://github.com/openhotel/auth/issues/450): hamburger menu invisible on phone.
- Wait for their phase: [utils#92](https://github.com/openhotel/utils/issues/92) (phase 3), [openhotel#1146](https://github.com/openhotel/openhotel/issues/1146) (phase 6).

## Open PRs
- [openhotel#1176](https://github.com/openhotel/openhotel/pull/1176) client to @da/socket: merge as a step (one less socket copy, phase 6 becomes a lib swap).
- [pixi-components#44](https://github.com/openhotel/pixi-components/pull/44): review, merge.
- [pathfinding#27](https://github.com/openhotel/pathfinding/pull/27) + [pathfinding#26](https://github.com/openhotel/pathfinding/issues/26): close (repo gets inlined).
- Dependabot: merge openhotel#1166, openhotel#1177, auth#444; close battleship#13/#14, game-template#39/#41 (moot after games rebuild).

## Housekeeping
- One label set across repos.
- Org project board, one column per phase.
- ~23 openhotel ideas to Discussions; review epics, close done ones.
