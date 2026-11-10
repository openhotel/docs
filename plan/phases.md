# Restructuring: phases and open questions

## Phases
1. **core first**: move domain types and pure helpers out of utils. Unblocks the rest.
2. **Monorepo**: import the 6 repos with history, workspaces, one CI, create packages/server and packages/auth-client.
3. **openhotel off utils** + inline pathfinding.
4. **Archive** at, captcha, auth-example, pathfinding, utils. Update org profile.
5. **Tailwind**: preset, ui, then apps.
6. **Socket library**: write it, migrate openhotel, onet, game-utils.
7. **Games**: game-utils shell, game-template and battleship on top, pixi-components bump.
8. **devkit** follows each phase; final rework after phase 2.

Phases 5, 6, 7 can run in parallel once 1 to 3 are done.

## Open questions
1. Monorepo name (`openhotel/platform`? `openhotel/services`?).
2. queue: move into core, into the org, or replace?
3. openhotel.github.io: archive?
4. Socket package name/home (`openhotel/socket` as `@oh/socket`?).
5. OK with the utils split (core / packages/server / local)?
6. aseprite-scripts: grant access to plan it.
7. License policy: 7 repos have none; others mix MIT, CC BY-SA, CC BY-NC-SA. See [licenses](../org/licenses.md).
