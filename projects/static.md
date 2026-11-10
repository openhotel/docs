# static

Repo: github.com/openhotel/static · last tag v0.0.10 · no license file · active.

File host for OpenHotel content, backed by S3 (SeaweedFS in devkit). Scaffolded from asset-editor (~20 identical server files).

- Server `api/`: `auth` (login via auth), `files` (put, delete, get), `version`, plus migrations.
- Client: home, application. React 18, still on legacy `@oh/components`, ~11 scss files.
- Run: `deno task install && deno task start`. devkit port 1995, S3 9000.

Plan: merged into the services monorepo, moves to the shared UI package. See [restructuring](../plan/restructuring.md).
