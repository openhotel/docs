# auth

Repo: github.com/openhotel/auth · last tag v0.11.1 · CC BY-NC-SA 4.0 · active.

Central identity service. Every other service authenticates against it. Defines **OHAP** (OpenHotel Auth Protocol).

## Responsibilities
- Accounts: register, login, logout, refresh, email verify, recover/change password, OTP (2FA), captcha.
- Tokens: connection tokens for hotels, token check endpoints, user scopes.
- Hotels: register hotels, issue **license tokens**, list hotels, `/hotel/license` for a hotel to identify itself.
- Apps / integrations: third-party apps (`apps/check`).
- Admin: users, hotels, tokens, backups, update, resend verification.
- onet link: shared token, checks onet via `/auth/check`.

## API
`/api/v3/` groups: account, admin, apps, data (languages), hotel, misc (captcha, version), tokens, user (`@me`, `@me/scopes`, count). One route per `*.request.ts`, samples in `*.http`.

## Layout
```
app/server/src/modules/api/v3/   routes
app/server/src/modules/system/   accounts, admins, apps, backups, captcha, email, hotels, onet, tokens, api
app/server/src/modules/migrations/
app/server/__tests__/            deno tests (deno task test)
app/client/src/modules/          account, admin, application, apps, change-password, connection, home, login, logout, recover-password, register, verify
```
Client: React 18 + `@openhotel/web-components` 0.3.9 (33 files import it).

## Run
`deno task install && deno task start` or `docker compose up --build` (server 20240, client 2024). devkit: port 2024.

## Proposed (pagoru, not committed)
Merged into the monorepo (`apps/auth`), client rewritten to Tailwind. See [restructuring](../ideas/pagoru/restructuring.md).
