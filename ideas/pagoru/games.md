# One game shell (phase 6)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Part of: [restructuring](restructuring.md). Facts: [games](../../projects/games.md), [ui-libs](../../projects/ui-libs.md)

## Problem
game-template and battleship each carry a copy of the shell; game-utils has the shell as a lib but no consumers. pixi-components versions: 0.0.24 / 0.0.29 / 0.1.9.

## Proposal
- **game-utils**: loaders, new socket client, child side of the hotel process protocol (event types from core). Closes [game-template#44](https://github.com/openhotel/game-template/issues/44).
- **game-template**, then **battleship**: delete copied shell, depend on game-utils. battleship stays as the first real game.
- **pixi-components**: everyone on latest; fix license string and README badges; work the 8 open issues.
- **aseprite-scripts**: plan once access exists.
