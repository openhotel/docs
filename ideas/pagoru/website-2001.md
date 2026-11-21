# Website rework: 2001 style

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21 (v2)
- Affects: web, auth, onet
- Discussion: none

## Summary
Static mockups of a new OpenHotel website in the style of the 2001 hotel community sites: grey boxes, yellow accents, Verdana, game art shown only as pictures at native size. Light and dark.

## Files
Everything is in [website-2001/](website-2001/): open `index.html` (page picker + Light/Dark toggle) or any `retro-<page>-<light|dark>.html` directly. Assets in `assets/oh/`, generators in `tools/`.

| Page | Files |
|---|---|
| Home, main hotel | `retro-lobby`, `retro-lobby-in` (logged in) |
| Home, community hotel | `retro-hotel`, `retro-hotel-in` |
| News list, article | `retro-news[-in]`, `retro-post[-in]` |
| Register, forgot password | `retro-register`, `retro-forgot` |
| Friends, credit exchange | `retro-friends`, `retro-exchange` |
| My account, connected hotels, my hotels | `retro-account`, `retro-connections`, `retro-my-hotels` |
| Assets, marketplace, item, collection, creations, create, link | `retro-assets`, `retro-market`, `retro-item`, `retro-collection`, `retro-mine`, `retro-create`, `retro-link` |
| Exchange credit page, hotel admin, network | `retro-coin`, `retro-admin`, `retro-network` |

## Proposal
- **Layout**: 1060px max, three columns on home (main · news · sidebar), two on subpages (content · same sidebar). Subpages reuse a short version of the home hero as header.
- **Boxes**: plain CSS, 1px black border, no game 9-slices, no pixel font on the web.
- **Main vs community hotel**: the main hotel is the auth (email, password, 6-digit 2FA). Community hotels show "Log in with OpenHotel" and redirect to auth.openhotel.club; they keep their own name, about, news and footer note.
- **Network**: registered guests, public hotels, online in all hotels; "Hotels online now" grid with picture + favicon per hotel, official hotel always first.
- **News**: 4 items with 64x64 images on home; article with rating, views and comments.
- **Avatar**: shown on the web, never edited there.
- **Account**: 2FA on/off both need a captcha and a 6-digit code. Delete account stays here.
- **Connected hotels**: the only way to link a hotel. Shows the hotel, its permissions and Disconnect; the main hotel can't be disconnected.
- **My hotels**: one licence per hotel, shown once; remake it to get a new one. Picture (160 x 72) and icon (max 24 x 24), public/private, client and web URLs. Credit code (3 letters) set on create, can't change. No integrations.
- **Assets**: owner picks rooms, furniture, clothes; marketplace + web/Aseprite/Resprite: see [asset-library](asset-library.md). **Admin**: boxes at the bottom of My account, see [hotel-admin](hotel-admin.md).
- **Credits box**: credits come from playing; no paid credits.
- **Friends** are network-wide; furniture and credits stay per hotel. Credits swap between hotels on an exchange: see [credit-exchange](credit-exchange.md).
- **Explore box**: one box on every page linking to news, marketplace, exchange, friends and admin (logged out: public links only).
- **Footer**: socials, CC BY-NC-SA 4.0, hotel version.

## Impact
- web: new pages and components; dark/light tokens.
- auth: needs a public `GET` for online users across hotels; uses existing `/api/v3/user/count` and `/api/v3/hotel/list`.
- onet: per-hotel online counts and hotel picture/favicon upload.
- Comments, ratings and views on news need storage (none today).

## Open questions
1. Where do news and comments live (web, auth or a new service)?
2. Picture and favicon limits for hotels (size, format, moderation)?
3. Keep the 2FA field always visible or only after the password step?

## Tools
`tools/lightdark.py <out>` builds the home pages, then `tools/subpages.py <out>` builds subpages and wires links. Edit `lobby.tpl.html`, `lobby.css`, `sub.css`, `login*.html`, `account*.html`. `room2.py` renders the lobby room from client sprites (`OH_CLIENT_ASSETS`, `OH_FURNI` env vars). Names and numbers are sample data.
