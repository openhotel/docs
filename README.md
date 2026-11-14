# OpenHotel docs

Docs for the [OpenHotel](https://github.com/openhotel) org: what each repo is, how they work together, open tasks, and ideas.

Load this file first, then only the files you need. Every file is ≤4 KB (CI-enforced). Snapshot: 2026-11-10.

## Org (cross-cutting)
- [org/overview.md](org/overview.md): all repos in one table, status and role.
- [org/architecture.md](org/architecture.md): how hotel, auth, onet, web, static and asset-editor talk at runtime.
- [org/stack.md](org/stack.md): shared tooling (Deno + yarn, tasks, CI, releases, ports).
- [org/dependencies.md](org/dependencies.md): who depends on which lib, and at which version.
- [org/licenses.md](org/licenses.md): license per repo and known inconsistencies.

## Services
- [projects/openhotel.md](projects/openhotel.md): the game (hotel server + client). Start here for gameplay.
- [projects/auth.md](projects/auth.md): accounts, hotel licenses, OHAP. Everything authenticates here.
- [projects/onet.md](projects/onet.md): inter-hotel network (OHMP), collections, teleports.
- [projects/web.md](projects/web.md): public website and account pages.
- [projects/static.md](projects/static.md): S3-backed file host.
- [projects/asset-editor.md](projects/asset-editor.md): furniture/collection/sprite editor.

## Libraries
- [projects/core.md](projects/core.md): `@oh/core`, shared isomorphic types and pure helpers.
- [projects/utils.md](projects/utils.md): `@oh/utils`, server grab-bag.
- [projects/ui-libs.md](projects/ui-libs.md): `@openhotel/pixi-components` and `@openhotel/web-components`.
- [projects/small-libs.md](projects/small-libs.md): pathfinding, queue, `@da/socket`.

## Games
- [projects/games.md](projects/games.md): game-utils, game-template, battleship and how games plug into a hotel.

## Tooling and other
- [projects/devkit.md](projects/devkit.md): Docker stack to run everything locally.
- [projects/misc.md](projects/misc.md): .github, openhotel.github.io, auth-example, at, captcha, aseprite-scripts, art.

## Ideas (proposals, not decisions)
- [ideas/README.md](ideas/README.md): rules, template and index of all ideas (one folder per author). Now: org restructuring, binary furniture and public room assets (both pagoru, proposed).

## Tasks (open issues and PRs, every item links to GitHub)
- [tasks/todo.md](tasks/todo.md): what needs to be done: critical issues and PR decisions. Start here.
- [tasks/todo-backlog.md](tasks/todo-backlog.md): issues the restructuring absorbs, product backlog, housekeeping.
- [tasks/prs.md](tasks/prs.md): the 10 open PRs.
- [tasks/openhotel-bugs.md](tasks/openhotel-bugs.md): openhotel bugs, critical, docs, infra.
- [tasks/openhotel-features-1.md](tasks/openhotel-features-1.md): openhotel features, older half.
- [tasks/openhotel-features-2.md](tasks/openhotel-features-2.md): openhotel features, newer half.
- [tasks/openhotel-art.md](tasks/openhotel-art.md): openhotel issues that need art.
- [tasks/openhotel-ideas.md](tasks/openhotel-ideas.md): openhotel loose ideas.
- [tasks/auth-1.md](tasks/auth-1.md): auth bugs, critical and older features.
- [tasks/auth-2.md](tasks/auth-2.md): auth newer features.
- [tasks/services.md](tasks/services.md): onet, web, static, asset-editor, devkit issues.
- [tasks/libs.md](tasks/libs.md): utils, pixi/web-components, game-template, pathfinding, auth-example issues.

## Meta
- [meta/conventions.md](meta/conventions.md): how these docs are written and kept up to date. Read before editing.
