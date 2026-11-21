# Hotel admin in My account

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: openhotel, onet, auth, web
- Discussion: none

## Summary
Boxes in the right bar for hotel admins, and one more for owners of the main hotel. Mockup: [website-2001](website-2001/) `retro-lobby-in`, `retro-admin`, `retro-network`.

## Proposal
- **Manage this hotel** (right bar box): accounts, online, open reports, registration state, links to admin and catalog. The registration lock lives on the admin page: existing accounts still enter, new accounts can't connect.
- **Friends online** (right bar box) sits above them.
- **Hotel admin page**, per hotel: registration (lock, message, verified email), accounts (search, mute, block, role), blocked list with reason and unblock, rooms (close, delete), chat and moderation (reported messages, blocked words, auto-mutes), credits and purchases, hotel catalog (see [asset-library](asset-library.md)).
- **Network admin** (right bar box, main hotel owners only): hotels, online, hotels waiting for review. Page: allow new hotels, pause the whole [credit exchange](credit-exchange.md), oldest allowed hotel version, hotel table (owner, version, accounts, online, credit code, state; approve, pause trading, suspend), daily credit reports with a check.
- **Data**: the hotel server exposes these lists and actions to its admins through onet; auth only says who is an admin. The website shows data it gets from the hotel, it doesn't store it.
- **Roles**: owner, admin, moderator with different actions (not final).

## Impact
- openhotel (server): admin read/write endpoints, registration lock, moderation log.
- onet: relays admin calls, review queue for new hotels, network settings.
- auth: admin role per hotel; a hotel locked to new accounts refuses new connections.
- web: the two boxes and two pages.

## Open questions
1. Which actions can a moderator do versus an admin?
2. Does a locked hotel show on the public list as "closed"?
3. Who can see chat content, and for how long is it kept?
