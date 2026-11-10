# Games

## How a game plugs into a hotel
- openhotel reads `app/server/assets/games.yml`: entries with `repo` (GitHub, e.g. `openhotel/game-template`, `alqubo/oh-snake-minigame`) or local `path`, plus `enabled`.
- The hotel downloads/copies each game into `.games/` and spawns it as a child process (`@oh/utils` process worker).
- Hotel -> game events: USER_JOIN, USER_READY, USER_LEAVE (with a per-user token). Credits flow back through the hotel economy.
- The client opens the game in an iframe (`shared/hooks/game/game.provider.tsx`); the game client talks to its own server via `@da/socket`.

## game-template
Repo: github.com/openhotel/game-template · no license · active (2026-02).
Starter for mini-games: `app/server` (Deno, `modules/{development,system}`; dev mode fakes the hotel parent) + `app/client` (React 19, Vite, zustand, pixi-components 0.0.24) + `build.ts`. Contains its own copy of the game shell and socket utils.

## game-utils (`@oh/game-utils`)
Repo: github.com/openhotel/game-utils · JSR · CC BY-NC-SA 4.0 · no README, no consumers.
Exports `./core` and `./client` (application, core-loader, initial-loader, render, start components). Peer deps: pixi-components 0.0.29, react 19, zustand, yaml, ulidx.
Plan: becomes the real shell; game-template depends on it instead of copying.

## battleship
Repo: github.com/openhotel/battleship · no license · 2026-05. Copy of game-template + game code (77 files differ); README still says game-template.
Plan: stays as the first real game, rebuilt on game-utils + new socket + latest pixi-components.

See [restructuring](../plan/restructuring.md).
