# Archive dead repos, rework devkit (phases 4 and 8)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-10
- Part of: [restructuring](restructuring.md). Facts: [misc](../../projects/misc.md), [devkit](../../projects/devkit.md)

## Archive
- at, captcha, auth-example (close its 2 issues).
- pathfinding (after inlining), utils (after moving its issues).
- web-components and auth/onet/web/asset-editor/static after the monorepo import, as read-only pointers.
- Update the `.github` profile and these docs at the same time.

## devkit
- Follows every phase.
- Final rework after phase 2: clone openhotel + the monorepo (2 repos instead of 6), compose points to `apps/*`, ports unchanged.
