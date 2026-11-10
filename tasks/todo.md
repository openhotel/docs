# What needs to be done (1/2)

Synthesis of 195 open issues + 10 open PRs (snapshot 2026-11-10) against the [restructuring plan](../plan/restructuring.md). Lists per repo: see README index.

## Numbers
openhotel 103, auth 36, static 12, utils 9, pixi-components 8, web-components 7, asset-editor 7, onet 5, game-template 2, pathfinding 2, auth-example 2, web 1, devkit 1. ~80% are 2024-2025 backlog; many openhotel issues were last touched in one bulk relabel on 2025-04-10.

## 1. Critical first (security / data / outage)
- [auth#447](https://github.com/openhotel/auth/issues/447) + [utils#119](https://github.com/openhotel/utils/issues/119): email encryption and encrypt/decrypt headers (do together; lands in packages/server after the utils split).
- [auth#422](https://github.com/openhotel/auth/issues/422): cap verification emails, then delete the account.
- [utils#92](https://github.com/openhotel/utils/issues/92): updater leaves old client JS behind (move fix into openhotel's own updater).
- [openhotel#1146](https://github.com/openhotel/openhotel/issues/1146): onet unreachable from Spain during football blocks; needs a fallback.
- [onet#19](https://github.com/openhotel/onet/issues/19): `ip:port` rejected as URL.
- [web-components#132](https://github.com/openhotel/web-components/issues/132): hamburger menu invisible on phone (also [auth#450](https://github.com/openhotel/auth/issues/450)).
- [openhotel#1169](https://github.com/openhotel/openhotel/issues/1169): HMR test + absolute imports.
- [openhotel#1082](https://github.com/openhotel/openhotel/issues/1082): in-game docs (Gym, Zoo, Museum).

## 2. Review or close open PRs ([prs](prs.md))
- [openhotel#1176](https://github.com/openhotel/openhotel/pull/1176) (community, fixes [openhotel#1153](https://github.com/openhotel/openhotel/issues/1153)): client to `@da/socket`. Decide vs. socket rewrite: merge as a step, or close in favor of phase 6.
- [pixi-components#44](https://github.com/openhotel/pixi-components/pull/44) (community, fixes [pixi-components#43](https://github.com/openhotel/pixi-components/issues/43) touch position): small, review and merge.
- [pathfinding#27](https://github.com/openhotel/pathfinding/pull/27) `wip` + [pathfinding#26](https://github.com/openhotel/pathfinding/issues/26) "migrate to Rust": close, repo gets inlined.
- 7 dependabot bumps ([list](prs.md)): merge or close; battleship/game-template ones are moot after the games rebuild.

Next: [restructuring overlap and backlog](todo-backlog.md).
