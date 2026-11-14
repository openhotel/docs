# devkit

Repo: github.com/openhotel/devkit · no license · new Oct 2026.

Runs the whole stack locally with Docker Compose, one container image (`Dockerfile`) running all services.

## Services
client (openhotel) 1994, static 1995, auth 2024, web 2025, asset-editor 2030, onet 9400, S3 (SeaweedFS) 9000, mail (Mailpit) 8025.

Repos are cloned next to devkit (or in `REPOS_DIR` from `.env`): openhotel, auth, onet, web, asset-editor, static.

## Tasks
```
deno task setup            clone missing repos, write dev configs (configs/)
deno task up [svc...]      start all or some services
deno task seed             create users, hotel and tokens from seed.yml
deno task logs [svc]
deno task down
deno task reset [--configs] [--cache]   wipe containers, s3 data, dbs
```
Files: `compose.yml`, `configs/`, `s3/`, `seed.ts` + `seed.yml`, `setup.ts`, `reset.ts`, `utils.ts`.

## Proposed (pagoru, not committed)
Reworked to clone 1 repo (the monorepo), compose paths -> `app/*`. Ports, SeaweedFS and Mailpit stay. See [restructuring](../ideas/pagoru/restructuring.md).
