# core (`@oh/core`)

Repo: github.com/openhotel/core · JSR `@oh/core` (consumers on 0.1.0) · MIT · new Oct 2026.

Shared **isomorphic** types, enums, consts and pure functions (browser + Deno).

## Contents (`src/`)
- `types`: furniture, collection.
- `consts`: collection consts.
- `utils`: collection, furniture, validation (shared validators), tests in `__tests__`.
- `index.ts` exports all; `publish.include` = index.ts, src, README, LICENSE.

## Tooling
Both Jest + Babel (`yarn test`) and `deno test` exist; `typecheck` via tsc, `bundle:check` with esbuild for browser, publish with `npx jsr publish`.

## Consumers
openhotel, onet, asset-editor.

## Proposed (pagoru, not committed)
Moves into the monorepo as `packages/core`; receives pure parts of `@oh/utils` (Point/Size/Direction, random, version compare, dates, base64, HttpStatusCode, RequestMethod). Rule: never touch Deno APIs. Needs README API list, CI tests, one toolchain. See [restructuring](../ideas/pagoru/restructuring.md).
