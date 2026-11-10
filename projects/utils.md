# utils (`@oh/utils`)

Repo: github.com/openhotel/utils · JSR `@oh/utils` · MIT · active, **to be killed**.

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

## Proposed (pagoru, not committed): split, then archive
- Pure/isomorphic -> [core](core.md).
- HTTP/db/S3/tokens/config -> monorepo `packages/server`.
- Game-only (workers, updater, OS, yaml) -> openhotel itself.
- Template needs (workers, readYaml, getDb) -> game-utils.
See [restructuring](../ideas/pagoru/restructuring.md).
