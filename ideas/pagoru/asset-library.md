# Asset library and marketplace

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: onet, asset-editor, openhotel, web, aseprite-scripts
- Discussion: none

## Summary
Every hotel owner picks which public rooms, furniture and clothes are in their hotel. Assets come from a network marketplace where anyone can publish. Anyone can create; only the owner adds an asset to a hotel. Pixel art is drawn in Aseprite, never on the web. Mockup: [website-2001](website-2001/) `retro-assets` (catalog), `retro-market`, `retro-item`, `retro-create`, `retro-link`.

## Motivation
Today each hotel ships the assets in its server folder, so sharing a room or a piece of furniture between hotels means copying files by hand. Builds on [binary-assets](binary-assets.md): every asset is one signed `.oha` file.

## Proposal
- **Version vs schema**: version = the item's own iterations (1.0, 1.1...) with a history. Schema = the data shape; each hotel version runs a range of schemas, which decides if a hotel can use an item. No "minimum hotel version" field. Unsupported schemas are hidden or marked.
- **Catalog on the web**: today `catalog.yml` (categories with id, label, description, enabled, optional from/to, furniture `id` + `price`). The owner edits it in the manage area: collections in order, name, items, visible, publish/unpublish dates (seasonal, optional yearly repeat), version and price per item, bulk price.
- **Marketplace** (onet): list with version, schema, version in my catalog, hotels using it, stars, author and an Official tag (ships in the OpenHotel default catalog). Whole rows are clickable. No downloads and no one-click add on the list; add from the item page or the catalog.
- **Item and collection pages**: version picker, history with "use this one", stars and comments once, who uses it.
- **Creator sub nav**: Create, Your creations, Spritesheets (uploaded PNGs, reuse, delete when unused), Furniture, Clothes, Rooms, Collections, Link app.
- **Your creations**: state, versions, hotels using each, rating, new version, edit collections. Download of own files only. **Delete only while no hotel uses it.**
- **Create**: the only upload is a PNG spritesheet (as the asset-editor sprite-sheet section). Cut frames and animations, then fill the form for the kind: furniture (asset-editor fields), public room or clothes (proposed fields). Revision is a ULID.
- **Aseprite**: Link app plus Lua extension, see [aseprite-link](aseprite-link.md). Resprite dropped.
- **Rules**: own art only, review, CC BY-NC-SA 4.0. Anyone creates; only the owner adds to a hotel.

## Alternatives
| Option | For | Against |
|---|---|---|
| Files on each server (today) | Nothing to build | No sharing, manual copies |
| Marketplace + pinned versions (proposed) | Easy sharing, owner in control | Review and storage on onet |
| Auto-updates | Always fresh | An author can change a hotel |

## Impact
- onet: asset store, search, ratings, usage counts, review queue, hotel asset lists.
- asset-editor: spritesheet import, validation, signing.
- openhotel (server): pulls the hotel's asset list and `.oha` files from onet at boot and on change.
- aseprite-scripts: Lua extension and Link app.
- web: Hotel catalog, Marketplace, item, creations, Create and Link pages.

## Open questions
1. Who reviews assets: OpenHotel staff, trusted guests, or both?
2. Can a hotel keep an asset that was pulled from the marketplace?
3. Furniture prices: only in the hotel's credits, or also free items?
4. Should Official items be locked to OpenHotel staff?
