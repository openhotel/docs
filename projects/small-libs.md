# Small libraries

## pathfinding (`@oh/pathfinding`)
Repo: github.com/openhotel/pathfinding · MIT · last commit 2024-07.
Jump Point Search with diagonal movement on a height `Grid` (`Grid.from(number[][])`). ~445 lines, preview page in `preview/`.
Used only by openhotel rooms (`Grid`, v2.0.3). Proposed (pagoru): inline into the monorepo `apps/client`, archive.

## queue (`@oh/queue`, `@tu/queue` in deno.json)
Repo: github.com/openhotel/queue · MIT · last commit 2024-09. Not listed on the org profile.
Ticker + queue that behaves the same on server (`setTimeout`) and web (`requestAnimationFrame`).
Used by openhotel, auth, onet, web, game-template (v1.1.1). Proposed (pagoru): undecided (move into core, keep, or replace).

## @da/socket (external, JSR)
Not in the org. WebSocket client/server (`getServerSocket`, `getClientSocket`, `emit`/`on`/`connect`/`close`), JSON frames `{ event, message, responseEventId }`. v2.3.0 in openhotel, onet, game-template, battleship. Client side is a copied `socket.utils.ts`.
Proposed (pagoru): rewrite as an org package with binary frames (u16 event id, u32 request id, CBOR payload, versioned handshake), same API. See [restructuring](../ideas/pagoru/restructuring.md).

## @da/worker (external, JSR)
Worker messaging used by openhotel (proxy, phantom workers).
