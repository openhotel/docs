# Hotel admin in My account

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: openhotel, onet, auth, web
- Discussion: none

## Summary
Boxes in the right bar for hotel admins, and one more for owners of the main hotel. Mockup: [website-2001](website-2001/) `retro-lobby-in`, `retro-admin`, `retro-network`.

## Proposal
- **Right bar boxes** (logged in): Friends online (avatar, name, hotel, Join), Manage OpenHotel (key numbers, links), Network admin (main hotel owners only). The mockup manages the main hotel, OpenHotel.
- **Manage sub nav**, one page per section: Overview, Registration (lock new accounts, message, verified email), Accounts (mute, block, role), Blocked, Rooms, Blocked (here, plus guests blocked on other hotels with hotel and reason; "Block here too"), Moderation (reports, blocked words with one replacement text for all, default `***`, auto-mute), News (write, publish, optional email request to subscribers), Credits (stats, purchases), Catalog ([asset-library](asset-library.md)), Public rooms (open, first room, max users), Website (look: header image, colours, background, light/dark or one theme; home sections and column, custom boxes with picture, text, button and dates, socials, hotel page), Connection (network link and Try to connect, licence, three URLs: network openhotel.club, this website, client; tests), Clothes (wardrobe with publish and unpublish dates, optionally yearly, and character personalisation: the six default skin colours always allowed and never removable, extra colours, default skin, what guests can recolour).
- **Network sub nav** (main hotel only): Overview, Hotels (approve, pause trading, suspend), Accounts (all accounts, block on the whole network with a reason), Blocked (network blocks and hotel blocks to promote), Emails and News ([emails](emails.md); network news goes to all subscribers, hotel requests are approved here), Credit reports, Settings (new hotels, pause the [exchange](credit-exchange.md), oldest version and newest schema allowed).
- **Data**: the hotel server exposes lists and actions to its admins through onet; auth only says who is an admin. The website doesn't store hotel data.
- **Roles**: owner, admin, moderator (not final).

## Impact
- openhotel (server): admin read/write endpoints, registration lock, moderation log.
- onet: relays admin calls, review queue for new hotels, network settings.
- auth: admin role per hotel; a hotel locked to new accounts refuses new connections.
- web: the two boxes and two pages.

## Open questions
1. Which actions can a moderator do versus an admin?
2. Does a locked hotel show on the public list as "closed"?
3. Who can see chat content, and for how long is it kept?
