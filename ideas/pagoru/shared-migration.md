# Replace @oh and @da libs with app/shared

- Author: pagoru
- Status: accepted
- Created: 2026-11-16 · Updated: 2026-11-17
- Affects: openhotel (monorepo, branch `monster`)
- Discussion: none

## Summary
Execution plan for [app/shared](shared.md): remove every `@oh/*` and `@da/*` dependency, move the code into `app/shared/src` (like `updater.module.ts`), and remove the code that is copied across apps. When done, `monster` replaces `master`.

## Scope (before monster replaces master)
1. `@oh/utils`, `@oh/core`, `@oh/pathfinding`, then `@oh/yaml`, `@oh/queue`, `@oh/components`, `@da/worker`, `@da/bcrypt`, `@da/socket` into `app/shared`. Details: [libs](shared-migration-libs.md).
2. Duplicated types, consts, enums and utils across apps into `app/shared`. Details: [duplicates](shared-migration-duplicates.md).
3. Same dependency versions in every `deno.json` and `package.json`, enforced in CI. Details: [versions](shared-migration-versions.md).
4. `@openhotel/web-components` replaced by `app/shared/components` (tsx) + Tailwind.
5. New updater module in every app. Docker containers restart when the app exits.

Next, after the merge: `@da/socket` replaced by the binary [socket](socket.md) idea.

## Order
1. pathfinding (done 2026-11-16)
2. core (done 2026-11-17)
3. utils base: request/response/http/cors, api, config/yaml, db (+ s3, sss, zip, chunks), random
4. utils per app, smallest first: web, static, asset-editor, onet, auth, openhotel (openhotel done 2026-11-17)
5. other libs: yaml, worker, bcrypt, queue, socket, components
6. updater swap: every `update()` call becomes `updaterModule`
7. cleanup: drop `@oh/*`/`@da/*` from every config, delete `app/shared/old/`

One commit per step, run each app after it.

## Conventions
- Alias `@shared/` → `app/shared/src/` in every deno.json (onet: `../shared/src/`, others `../../../shared/src/`).
- Vite clients: tsconfig `paths` (relative to `baseUrl`) + vite `resolve.alias` `@shared` + `server.fs.allow` on `app/`.
- `modules/*.module.ts` only holds the main export; helpers in `utils/`, consts and types in their own files.
- Tests: `@std/testing/bdd` + `@std/expect`, no Jest.
- Keep `cbor-x` in db chunks: values over 64 KB are stored with it, so changing it needs a data migration.

## Links
[shared](shared.md), [restructuring](restructuring.md), [release manifest](release-manifest.md)
