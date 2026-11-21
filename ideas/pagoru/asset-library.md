# Asset library and marketplace

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: onet, asset-editor, openhotel, web, aseprite-scripts
- Discussion: none

## Summary
Every hotel owner picks which public rooms, furniture and clothes are in their hotel. Assets come from a network marketplace where anyone can publish. Anyone can create; only the owner adds an asset to a hotel. Pixel art can be drawn on the web, in Aseprite or in Resprite (iPad). Mockup: [website-2001](website-2001/) `retro-assets`, `retro-market`, `retro-create`.

## Motivation
Today each hotel ships the assets in its server folder, so sharing a room or a piece of furniture between hotels means copying files by hand. Builds on [binary-assets](binary-assets.md): every asset is one signed `.oha` file.

## Proposal
- **Hotel assets** (owner, from My hotels): three lists (public rooms, furniture, clothes) with on/off per asset, the hotel's first room, and a furniture price in the hotel's own credits. Upload a signed `.oha` or add from the marketplace.
- **Pinned versions**: a hotel keeps the version it added. New versions show under Updates; the owner updates or skips.
- **Marketplace** (onet): search, filter by kind, sort by most used, newest, best rated. Each asset shows the author, its rating and how many hotels use it. "Add to <hotel>" or download the `.oha`. All free.
- **Create**: kind, name and size in tiles, then draw. The web editor is a small version of asset-editor (pencil, eraser, fill, pick, palette, one sprite per direction). "Send for review" goes to a check, then the asset-editor server signs the `.oha` (the writer stays private, as in binary-assets).
- **Aseprite**: an extension in `aseprite-scripts` that adds File > Send to OpenHotel. Layers and tags map to directions and frames. It's linked to the account with a 6-digit code shown on the web, valid for 10 minutes.
- **Resprite (iPad)**: no plugin API that we know of (unverified). Export `.aseprite` and upload it on the web or through the iPad share sheet; the same importer as Aseprite reads it.
- **Rules**: your own art only, review before going live, CC BY-NC-SA 4.0 by default. Reported assets can be pulled; hotels using them get a notice.
- **Who can do what**: any account creates and publishes; the hotel owner adds or removes assets in the hotel. Staff roles inside a hotel are left for later.

## Alternatives
| Option | For | Against |
|---|---|---|
| Files on each hotel server (today) | Nothing to build | No sharing, no signing, manual copies |
| Marketplace + pinned versions (proposed) | Easy sharing, owner stays in control | Needs review and storage on onet |
| Marketplace with auto-updates | Always fresh | An author can change a hotel without the owner |

## Impact
- onet: asset store, search, ratings, usage counts, review queue, hotel asset lists.
- asset-editor: web editor, importer for `.aseprite` and PNG sheets, signing.
- openhotel (server): pulls the hotel's asset list and `.oha` files from onet at boot and on change.
- aseprite-scripts: Send to OpenHotel extension + device linking.
- web: Hotel assets, Marketplace and Create pages.

## Open questions
1. Who reviews assets: OpenHotel staff, trusted guests, or both?
2. Can a hotel keep an asset that was pulled from the marketplace?
3. Furniture prices: only in the hotel's credits, or also free items?
4. Does Resprite have any import/export hook we can use beyond files?
