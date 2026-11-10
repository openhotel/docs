# web

Repo: github.com/openhotel/web · last tag v0.3.2 · CC BY-NC-SA 4.0 · idle since 2025-10, but live (keep).

Public website for OpenHotel: home/landing and account pages, logged in through auth.

- Server `app/server/src/modules/api/`: `auth` (login flow against auth: request, user), `misc`.
- Client `app/client/src/modules/`: home, account, application. React 18 + `@openhotel/web-components` 0.3.3, ~7 scss files.
- Run: `deno task install && deno task start` (Deno >= 2). devkit port 2025.

Proposed (pagoru): merged into the services monorepo, first app to move to Tailwind (smallest). See [restructuring](../ideas/pagoru/restructuring.md).
