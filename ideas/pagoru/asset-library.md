# Asset library and marketplace

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: onet, asset-editor, openhotel, web, aseprite-scripts
- Discussion: none

## Summary
Every hotel owner picks which public rooms, furniture and clothes are in their hotel. Assets come from a network marketplace where anyone can publish. Anyone can create; only the owner adds an asset to a hotel. Pixel art is drawn in Aseprite or Resprite (iPad), never on the web. Mockup: [website-2001](website-2001/) `retro-assets`, `retro-market`, `retro-item`, `retro-create`, `retro-link`.

## Motivation
Today each hotel ships the assets in its server folder, so sharing a room or a piece of furniture between hotels means copying files by hand. Builds on [binary-assets](binary-assets.md): every asset is one signed `.oha` file.

## Proposal
- **Versions and schemas**: every asset (room, furniture, clothes) and collection has a version, a schema number and a `minHotelVersion`. A hotel only sees versions it can run; newer ones are hidden with a count. Owners see "Update to x" when a newer compatible version exists.
- **Hotel assets** (owner): list with version, latest, hotel-from, on/off, price (furniture) and first room. Upload a signed `.oha` or add from the marketplace. A hotel keeps its version until the owner updates.
- **Marketplace** (onet): dense table (thumb, name, kind, version, hotels using it, downloads, rating, Add or Update). Filters: kind, search, sort, "works with my hotel". Download gives the signed `.oha` for hotels that upload by hand; Add is one click for the hotel you pick.
- **Collections**: a set of furniture (asset-editor `CollectionData`: `id`, `category.label`, `category.description`, `minHotelVersion`, furniture list). Add all in one click.
- **Item and collection pages**: versions table with compat, data in the version (revision, type, size w/d/h, icon, actions, lang, directions with texture, zIndex, pivot, position, sprite sheet), who uses it, downloads, dates, stars, comments like news, report.
- **Your creations**: state (draft, review, live), versions, hotels using each, downloads, rating, new version, edit collections.
- **Create**: no drawing on the web. Send a file (.aseprite, .png + .json, .oha); the page validates it and previews every field. Furniture fields come from asset-editor; room and clothes fields are a proposal.
- **Link app**: small desktop app on `127.0.0.1` that joins the website and Aseprite. Aseprite Lua extension sends the export via the scripting `WebSocket` (to verify), else drops files in an outbox folder. Layers = directions, tags = action states, slices = icon and pivot.
- **Resprite (iPad)**: no plugin and no localhost, so files only (export, then pick the file on the website). A share-sheet route is unverified.
- **Rules**: own art only, review, CC BY-NC-SA 4.0. Anyone creates; only the owner adds to a hotel.

## Alternatives
| Option | For | Against |
|---|---|---|
| Files on each hotel server (today) | Nothing to build | No sharing, no signing, manual copies |
| Marketplace + pinned versions (proposed) | Easy sharing, owner stays in control | Needs review and storage on onet |
| Marketplace with auto-updates | Always fresh | An author can change a hotel without the owner |

## Impact
- onet: asset store, search, ratings, usage counts, review queue, hotel asset lists.
- asset-editor: importer for `.aseprite` and PNG sheets, validation, signing.
- openhotel (server): pulls the hotel's asset list and `.oha` files from onet at boot and on change.
- aseprite-scripts: Lua extension; new Link app (desktop).
- web: Hotel assets, Marketplace, item, creations, Create and Link pages.

## Open questions
1. Who reviews assets: OpenHotel staff, trusted guests, or both?
2. Can a hotel keep an asset that was pulled from the marketplace?
3. Furniture prices: only in the hotel's credits, or also free items?
4. Does Resprite have any import/export hook we can use beyond files?
