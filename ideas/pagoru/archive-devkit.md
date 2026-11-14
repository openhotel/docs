# Archive old repos, rework devkit (phase 3)

- Author: pagoru
- Status: proposed
- Created: 2026-10-22 · Updated: 2026-11-14
- Affects: at, captcha, auth-example, pathfinding, and every repo merged into the monorepo
- Discussion: none

## Summary
Part of [restructuring](restructuring.md). Facts: [misc](../../projects/misc.md), [devkit](../../projects/devkit.md).

## Archive
- at, captcha, auth-example (close its 2 issues).
- pathfinding, after inlining it in `apps/client`.
- openhotel, auth, onet, web, asset-editor, static, core, utils, web-components after the monorepo import, as read-only pointers (README links to the monorepo path).
- Update the `.github` profile and these docs at the same time.

## devkit
- Clones 1 repo (the monorepo) instead of 6; compose points to `apps/*`; ports, SeaweedFS and Mailpit unchanged.
- Could move into the monorepo itself ([questions](questions.md)).
