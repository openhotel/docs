# Runtime architecture

## Services and trust
- **auth** is the root of trust. It holds accounts, admin flags, scopes, apps and **hotels**. A hotel owner registers a hotel in auth and gets a **license token**.
- **openhotel** (a hotel) starts, calls `GET {auth.api}/api/v3/hotel/license` with header `license-token` and learns its `hotelId`, `integrationId` and owner `accountId`. If auth is disabled in `config.yml`, the hotel runs open (dev mode).
- **Player login**: the player signs in on auth, auth issues a **connection token** for that hotel. The client connects to the hotel proxy over WebSocket; the proxy calls `/user/@me/scopes` and `/user/@me` on auth with `connection-token` and builds the session (accountId, username, admin, languages).
- **onet**: the hotel opens a WebSocket client to onet with protocols `[hotelId, licenseToken]` and uses HTTP `/api/v1` with an api token and `hotel-id`. onet validates the hotel against auth (auth also has an `onet` module with a shared token, checked via `/auth/check`). onet serves signed **collections** (furniture packs) and **teleports** between hotels.
- **web, static, asset-editor**: each has an `api/auth` module that runs the same login flow against auth (copied code, see [restructuring idea](../ideas/pagoru/restructuring.md)).
- **static** stores files in S3 (SeaweedFS locally).

## Inside openhotel server
One Deno process (`mod.ts` -> `System.load`) with workers:
- **system**: config, Deno KV db (`./server-database`), migrations, game state (rooms, users, furniture, economy, marketplace, teleports, games), tasks/cron, onet link, auto-updater.
- **proxy** worker: HTTP + WebSocket front door for clients (`@da/socket`), auth checks, routes events to system.
- **phantom** worker: headless browser (puppeteer) that captures room images.
- **games**: external game servers listed in `assets/games.yml` (GitHub repo or local path), copied to `.games/` and spawned as child processes; the client shows them in an iframe. Events: USER_JOIN, USER_READY, USER_LEAVE.

## Wire formats
- Client <-> hotel, hotel <-> onet, game <-> client: `@da/socket` JSON text frames `{ event, message, responseEventId }`.
- Services: JSON over HTTP, versioned paths (`/api/v3` auth, `/api/v1` onet).

## Local ports (devkit)
client 1994, static 1995, auth 2024, web 2025, asset-editor 2030, onet 9400, S3 9000, Mailpit 8025. Standalone docker-compose in openhotel/auth: server 20240, client 2024.
