# Binary socket library (phase 5)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Part of: [restructuring](restructuring.md). Facts: [small-libs](../../projects/small-libs.md), [architecture](../../org/architecture.md)

## Problem
`@da/socket` (external) sends JSON text frames `{ event, message, responseEventId }` with string event names. The client is a copied `socket.utils.ts` in 4 repos. onet auth rides on WS protocols `[hotelId, licenseToken]`.

## Proposal
- Binary frames: u16 event id, u32 request id, CBOR payload; per-event schemas later for hot paths (movement).
- Versioned handshake carrying auth (connection token, or hotelId + license token for onet).
- Built-in reconnect ([openhotel#1045](https://github.com/openhotel/openhotel/issues/1045)), fallback endpoint/transport for blocked onet ([openhotel#1146](https://github.com/openhotel/openhotel/issues/1146)).
- Same `emit` / `on` / `connect` / `close` API, one package for client + server, in the org on JSR.

## Links to migrate (in order)
1. openhotel client <-> hotel proxy
2. hotel <-> onet
3. game client <-> game server (via game-utils)

## Issues absorbed
[openhotel#183](https://github.com/openhotel/openhotel/issues/183), [openhotel#1153](https://github.com/openhotel/openhotel/issues/1153), [openhotel#1045](https://github.com/openhotel/openhotel/issues/1045), [openhotel#1146](https://github.com/openhotel/openhotel/issues/1146).
