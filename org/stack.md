# Shared stack and conventions

## Languages and runtimes
- TypeScript everywhere.
- Servers: **Deno** (README says >=1.44, newer repos use Deno 2), Deno KV for storage (wrapped by `@oh/utils` `getDb`, with chunking), `deno compile` to single binaries per OS (linux, linux_aarch64, darwin, windows).
- Clients: **React** (18 in web/auth/static/asset-editor, 19 in openhotel and games), **Vite**, **zustand** in game clients, **Pixi.js** via `@openhotel/pixi-components`, **Sass** CSS modules via `@openhotel/web-components`.
- Package managers: yarn 4 (corepack) in most repos, yarn 1 in older ones; Deno imports via JSR (`jsr:`) and npm.

## Repo layout (services)
```
app/server/   Deno server (mod.ts, src/modules, src/shared, config.yml)
app/client/   Vite + React client
deno.json     root tasks
package.json  prettier only
```
Older single-service repos (onet, at) put `mod.ts` + `src/` at root.

`src/modules/api/vN/**/*.request.ts` = one HTTP route per file, `*.http` = REST client samples. `src/shared/{types,enums,consts,utils}` with `main.ts` barrels.

## Root deno tasks (same names across repos)
`install`, `install:force`, `start` (server + client), `start:server`, `start:client`, `start:nowatch`, `build`/`compile:*`, `check-storybook`, `progress` (gource).

## Formatting and CI
- Prettier everywhere (`prettier:check` in CI).
- Per service: `server-build.yml`, `client-build.yml`, `prettier-check.yml`, `publish.yml` (release binaries on tag). openhotel also checks translations and builds a changelog.
- Libs: `build.yml` + `publish.yml` to JSR or npm.

## Config
Each server reads `app/server/config.yml` (auto-created with defaults). Set `version: development` for dev mode. openhotel also uses `users.yml` (op list) and `.env`.

## Community
Discord linked from every README. Contributions: `.github/CONTRIBUTING.md`.
