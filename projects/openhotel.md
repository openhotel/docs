# openhotel (the game)

Repo: github.com/openhotel/openhotel · last tag v0.8.6 · CC BY-NC-SA 4.0 · active.

A self-hostable hotel: isometric rooms, avatars, chat, furniture, economy, mini-games. Each owner runs their own hotel binary; players log in with their auth account.

## Layout
```
app/server/  Deno. mod.ts -> System.load()
  src/modules/system/   config, db, game/, commands/, onet/, proxy/, phantom/, tasks, updater
  src/modules/proxy/    client-facing worker (HTTP + WS)
  src/modules/phantom/  puppeteer worker, room captures
  src/modules/migrations/  dated *.migration.ts on Deno KV
  assets/  rooms, locales, furniture, games(.yml), icon
app/client/  Vite + React 19 + @openhotel/pixi-components + zustand
  src/modules/  application, home, modals, moderator, phantom, private-room, router
build.ts      compiles server binaries per OS
scripts/      checkTranslations.ts
```

## Game domain (server `system/game`)
rooms (public, private, layout, pathfinding via `@oh/pathfinding` Grid), users, furniture, economy (credits, transactions), marketplace (commission rates in config), companies, teleports, games.

Chat commands (`system/commands`): op/deop, ban/unban, kick, blacklist/whitelist, set/unset (place furniture), move, rotate, tp/teleport, credits, photo, game, token, update, whisper/reply, color, clear, help, stop.

## Config (`app/server/config.yml`)
version, name, description, port, limits.players, languages, auth {enabled, licenseToken, api}, onet {enabled, api}, phantom {enabled, browser, sleep}, autoupdate {enabled, cron}, marketplace {...}. `users.yml` holds the op list.

## Run (dev)
`deno task install && deno task start`, or `docker compose up --build`. Set `version: development`, put a `username` in browser localStorage, add it to `users.yml` op list. Or use [devkit](devkit.md).

## Talks to
auth (license + player tokens), onet (network), spawned games. See [architecture](../org/architecture.md).

## Deps
`@oh/utils`, `@oh/core`, `@oh/queue`, `@oh/pathfinding`, `@da/socket`, `@da/worker`. See [dependencies](../org/dependencies.md).

## Plan
Stays. Drop `@oh/utils`, inline pathfinding under `app/server/src/shared/pathfinding/`, move to new binary socket. See [restructuring](../plan/restructuring.md).
