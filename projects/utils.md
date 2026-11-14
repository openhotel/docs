# utils (`@oh/utils`)

Repo: github.com/openhotel/utils · JSR `@oh/utils` · MIT · active (proposed: moves into the monorepo).

Server-side grab-bag used by almost every Deno repo (7 versions in use, see [dependencies](../org/dependencies.md)).

## Modules (`src/modules`)
- `api`: getApiHandler, getResponse, CORS headers, RequestType/RequestKind.
- `db`: Deno KV wrapper `getDb` / `DbMutable`, chunked values (cbor-x), migrations.
- `s3`: `getS3` (minio client).
- `config`: `getConfig` (yaml config with defaults).
- `worker`, `process-worker`: worker and child-process messaging (`getParentProcessWorker`).
- `updater`: self-update of compiled binaries.
- `yaml`, `lang`.
- `src/utils`: points/sizes/directions, random strings, version compare, dates, base64, encryption/tokens (bcrypt), OS helpers, copyDirectory, getURL, getIpFromRequest.

## Proposed (pagoru, not committed): keep, move into the monorepo
- Merges with core into `app/shared` in openhotel/openhotel; apps use the workspace version (no more drift).
- Pure/isomorphic parts move to [core](core.md); utils keeps the server runtime.
- Keeps publishing to JSR for games outside the monorepo.
See [shared packages](../ideas/pagoru/shared.md).
See [restructuring](../ideas/pagoru/restructuring.md).
