# Open questions for the restructuring

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: whole org
- Discussion: none

Part of [restructuring](restructuring.md).

1. JSR name for `app/shared`: one `@oh/shared`, or keep publishing `@oh/core` + `@oh/utils` from it?
2. queue: small isomorphic ticker used by 5 repos. Proposal: move into `app/shared`.
3. openhotel.github.io: archive?
4. Socket package: inside the monorepo as `app/socket` (`@oh/socket`), or its own repo?
5. devkit: move into the monorepo, or stay separate? Single issue tracker for repos outside the monorepo too (pixi-components, games, devkit)?
6. [openhotel#1176](https://github.com/openhotel/openhotel/pull/1176): merge as a step (proposed) or close for the socket rewrite?
7. Critical fixes: now in current repos (proposed) or after the import?
8. @da/worker: keep external or bring into the monorepo with the socket?
9. aseprite-scripts: access needed to plan.
10. License policy: one license for the monorepo? Today core/utils are MIT, the apps CC BY-NC-SA, onet/static none ([licenses](../../org/licenses.md)).
