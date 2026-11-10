# What needs to be done (2/2)

Continues [todo](todo.md): issues the restructuring absorbs, product backlog, housekeeping.

## 3. Absorbed by the restructuring (close or move when the phase lands)
- [utils (all 9)](https://github.com/openhotel/utils/issues): logs, atomic db, useApi, migration traces, rate-limit on updater -> move to packages/server / openhotel or close with utils archive.
- "Implement log system" exists 5 times ([openhotel#1029](https://github.com/openhotel/openhotel/issues/1029), [auth#432](https://github.com/openhotel/auth/issues/432), [auth#58](https://github.com/openhotel/auth/issues/58), [onet#46](https://github.com/openhotel/onet/issues/46), [web#9](https://github.com/openhotel/web/issues/9), [utils#90](https://github.com/openhotel/utils/issues/90)) -> one issue in the monorepo packages/server.
- [openhotel#183](https://github.com/openhotel/openhotel/issues/183) (binary socket) + [openhotel#1153](https://github.com/openhotel/openhotel/issues/1153) + [openhotel#1045](https://github.com/openhotel/openhotel/issues/1045) (reconnect in dev) -> socket rewrite (phase 6).
- [game-template#44](https://github.com/openhotel/game-template/issues/44) "library with the basics" -> game-utils shell (phase 7).
- [web-components (7)](https://github.com/openhotel/web-components/issues) -> packages/ui Tailwind rewrite; re-file what still applies.
- [auth-example (2)](https://github.com/openhotel/auth-example/issues) -> archive.
- static and asset-editor duplicates, [auth#177](https://github.com/openhotel/auth/issues/177) (endpoint naming) -> monorepo cleanup.

## 4. Product backlog (no plan impact)
- openhotel epics: Human ([openhotel#233](https://github.com/openhotel/openhotel/issues/233)), Inventory ([openhotel#212](https://github.com/openhotel/openhotel/issues/212)), Public rooms ([openhotel#277](https://github.com/openhotel/openhotel/issues/277)), Private room ([openhotel#756](https://github.com/openhotel/openhotel/issues/756)), Catalog ([openhotel#733](https://github.com/openhotel/openhotel/issues/733)), Navigator ([openhotel#729](https://github.com/openhotel/openhotel/issues/729)), Economy ([openhotel#727](https://github.com/openhotel/openhotel/issues/727)), Minigames ([openhotel#818](https://github.com/openhotel/openhotel/issues/818)), Furniture interactions ([openhotel#583](https://github.com/openhotel/openhotel/issues/583), [openhotel#1102](https://github.com/openhotel/openhotel/issues/1102)), Pets ([openhotel#1129](https://github.com/openhotel/openhotel/issues/1129)). Some look partly shipped (unverified); review each epic and close or split.
- Art queue: ~26 openhotel issues tagged art (banners, furniture, animations). See [art](openhotel-art.md).
- Ideas (~23, [list](openhotel-ideas.md)): keep as Discussions instead of issues to shrink the tracker.

## Suggested housekeeping
- Triage pass on openhotel: close done epics, move ideas to Discussions.
- One shared label set across repos (most already use feature/bug/ideas/art/critical).
- Org project board tracking the 8 restructuring phases.
