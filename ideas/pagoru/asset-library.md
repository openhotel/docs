# Asset library and marketplace

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: onet, asset-editor, openhotel, web, aseprite-scripts
- Discussion: none

## Summary
Every hotel owner picks which public rooms, furniture and clothes are in their hotel. Assets come from a network marketplace where anyone can publish. Anyone can create; only the owner adds an asset to a hotel. Pixel art is drawn in Aseprite or Resprite (iPad), never on the web. Mockup: [website-2001](website-2001/) `retro-assets` (catalog), `retro-market`, `retro-item`, `retro-create`, `retro-link`.

## Motivation
Today each hotel ships the assets in its server folder, so sharing a room or a piece of furniture between hotels means copying files by hand. Builds on [binary-assets](binary-assets.md): every asset is one signed `.oha` file.

## Proposal
- **Version vs schema**: version = the item's own iterations (1.0, 1.1...), shown with its history. Schema = the data shape; each hotel version runs a range of schemas, and that decides if a hotel can use an item. There is no "minimum hotel version" field. Versions with a schema the hotel doesn't run are hidden or marked unsupported.
- **Catalog on the web**: a hotel's catalog today is `catalog.yml` (categories with id, label, description, enabled, optional from/to dates, furniture `id` + `price`). The owner edits it on the web: categories, availability dates, per-item version and price. Adding an item is done from its marketplace page (any compatible version, old ones too) or from the catalog; no one-click add on the marketplace list.
- **Marketplace** (onet): list with version, schema, your catalog version, hotels using it, and stars. Filter by kind, search, sort, "schemas my hotel runs". No downloads: hotels get assets through the catalog.
- **Item and collection pages**: version picker with each version's data (revision, schema, size w/d/h, icon, actions, lang, directions, sprite sheet), history with "use this one", stars and comments once, who uses it.
- **Collections**: asset-editor `CollectionData` (`id`, `category.label`, `category.description`, furniture list).
- **Your creations**: state, versions, hotels using each, rating. Download (own files only), new version, edit collections. **Delete only while no hotel uses the asset or version.**
- **Uploads**: only OpenHotel files made like asset-editor does today (`.furniture` zip: sprite.png, sheet.json, data.yml, lang.yml; `.collection`; `.oha` later). Revision is a ULID. The Create page is an editable form of those fields (id, type, size, icon, actions, lang, directions). Rooms and clothes come when the editor supports them.
- **Link app**: desktop app on `127.0.0.1`; Aseprite Lua extension (scripting `WebSocket`, to verify) fills the form from an export. Layers = directions, tags = action states, slices = icon and pivot.
- **Resprite (iPad)**: no plugin or localhost; file export and upload only.
- **Rules**: own art only, review, CC BY-NC-SA 4.0. Anyone creates; only the owner adds to a hotel.

## Alternatives
| Option | For | Against |
|---|---|---|
| Files on each server (today) | Nothing to build | No sharing, manual copies |
| Marketplace + pinned versions (proposed) | Easy sharing, owner in control | Review and storage on onet |
| Auto-updates | Always fresh | An author can change a hotel |

## Impact
- onet: asset store, search, ratings, usage counts, review queue, hotel asset lists.
- asset-editor: importer for `.aseprite` and PNG sheets, validation, signing.
- openhotel (server): pulls the hotel's asset list and `.oha` files from onet at boot and on change.
- aseprite-scripts: Lua extension; new Link app (desktop).
- web: Hotel catalog, Marketplace, item, creations, Create and Link pages.

## Open questions
1. Who reviews assets: OpenHotel staff, trusted guests, or both?
2. Can a hotel keep an asset that was pulled from the marketplace?
3. Furniture prices: only in the hotel's credits, or also free items?
4. Does Resprite have any import/export hook we can use beyond files?
