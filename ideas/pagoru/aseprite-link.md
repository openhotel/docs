# Aseprite link for assets

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: aseprite-scripts, asset-editor, web
- Discussion: none

## Summary
Send a sprite from Aseprite to the website's Create page in one click. Resprite is dropped: it has no plugin system and the iPad has no `localhost`. Part of [asset-library](asset-library.md). Mockup: `retro-link`, `retro-create` in [website-2001](website-2001/).

## What Aseprite gives us
Checked against the public API docs by search only; page contents not read, so details are marked.
- **Extensions**: a Lua script packaged as an `.aseprite-extension` (zip with a `package.json`) that adds commands and menu entries (aseprite.org/api/plugin).
- **Export**: `app.command.ExportSpriteSheet` writes a PNG and a JSON (frames, tags, layers, slices) without a dialog (aseprite.org/api/app_command).
- **Network**: the API lists a `WebSocket` class and `WebSocketMessageType` (aseprite.org/api). Minimum Aseprite version and whether it can reach `ws://127.0.0.1` to verify.
- **Not available (assumed)**: plain HTTP, shelling out. Verify before relying on them.

## Proposal
- **Link app**: small desktop app, listens only on `127.0.0.1:48621`. The website talks to it with a pairing code (shown on the web, 10 minutes). Link keeps the pairing so later syncs are one click.
- **Extension**: command "Send to OpenHotel" exports the sheet and sends it over the WebSocket to Link. Fallback if WebSocket is missing: write the export to `~/OpenHotel/outbox`, Link watches the folder.
- **Mapping** Aseprite to the asset-editor `SpriteSheet` (`frames`, `animations`, `meta`):
  - frame name = layer + tag name; `frame` = x, y, w, h;
  - slice `icon` = icon frame; slice pivot = `anchor`;
  - tags = `animations`; `meta` from the PNG.
- **Website**: Create page, step 1 "Spritesheet": upload the PNG or press "Sync from Aseprite" if linked. The frames table stays editable. The only upload is the PNG.
- **Security**: Link answers only to openhotel.club origins, needs the pairing code, never sees the account password.

## Open questions
1. Does Aseprite's `WebSocket` connect to localhost, and from which version?
2. Link app on three desktop platforms, or can a browser-only path (file picker plus the outbox folder) be enough at first?
3. Who maintains the extension: `aseprite-scripts` (not reachable from here)?
