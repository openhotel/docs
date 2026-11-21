# Aseprite link for assets

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: aseprite-scripts, asset-editor, web
- Discussion: none

## Summary
Create a sprite from the website, draw it in Aseprite and see it live on the website. A working test lives in [aseprite-link/](aseprite-link/); protocol and run steps in [aseprite-link-test](aseprite-link-test.md). Resprite is dropped: no plugin system, no `localhost` on iPad. Part of [asset-library](asset-library.md). Mockup: `retro-link`, `retro-create` in [website-2001](website-2001/).

## Tested (2026-11-21, works with Aseprite)
- Aseprite's Lua `WebSocket` (since v1.2.30, API 15) is a **client only**. A browser page is a client too, so a local process must be the server: the **Link** app (in the test, `relay.ts`, Deno, `127.0.0.1:48621`).
- The plugin ships as an `.aseprite-extension` (zip of `package.json` + `oh-link.lua`). Link serves it, so the website can offer a download. The command appears in the **File** menu (group `file_scripts`), not inside File > Scripts.
- From the website: set width and height, "Create in Aseprite". Every stroke, undo, resize, frame or sprite switch is sent back as a PNG and shown on the page at the new size.
- Plugin and website each have a `VERSION`. If they differ, the website sends `deny`, the plugin disconnects and the page shows both versions with a download link.
- An https page to `ws://127.0.0.1` is not mixed content. Chrome (157) blocks it with `ERR_BLOCKED_BY_LOCAL_NETWORK_ACCESS_CHECKS` until the user allows the "apps and services on this device" prompt.
- A claude.ai artifact cannot be the page: its CSP blocks WebSocket to any host.

## Proposal
- **Plugin stays generic** so it rarely needs updates: it only offers primitives (`hello`, `deny`, `command <Name> k=v`, `frame`, `sheet`, `live`). Product logic lives on the website.
- **Link app** listens only on `127.0.0.1:48621`, accepts web sockets only from openhotel.club origins (because `command` runs any Aseprite command), serves the plugin, and relays messages.
- **Website** Create page, step 1 "Spritesheet": create the image or "Sync from Aseprite"; `sheet` gives the PNG plus Aseprite JSON.
- **Mapping** Aseprite to the asset-editor `SpriteSheet` (`frames`, `animations`, `meta`): frame name = layer + tag name; slice `icon` = icon frame; slice pivot = `anchor`; tags = `animations`.

## Open questions
1. Link app on three desktop platforms, or bundle the relay into an existing OpenHotel desktop app (Steam shell)?
2. Pairing code on top of the origin check, so other local apps cannot drive Aseprite?
3. Who maintains the extension: `aseprite-scripts` or the monorepo?
