# Release manifest (`release.oh`)

- Author: pagoru
- Status: proposed
- Created: 2026-11-15 · Updated: 2026-11-15
- Affects: openhotel (monorepo release workflow), every app with an updater
- Discussion: none

## Summary
One monorepo tag (`vX.Y.Z`) releases all apps, but only changed apps are rebuilt. Unchanged apps reuse the previous build and keep their old version. Every release ships a tiny binary `release.oh` with each app's real version, so updaters check one file instead of downloading builds they already have.

## Motivation
With partial releases, `v0.9.0` may contain openhotel `0.7.5` (unchanged since then). Without a manifest, an updater sees a new tag and downloads the same build again.

## Proposal
**Release workflow** (`.github/workflows/release.yml` in openhotel/openhotel):
- `version`: validates the tag (`vX.Y.Z[-pre]`), outputs it without the `v`.
- `changes`: finds the previous tag (`git describe --tags --abbrev=0 <tag>^`) and diffs `app/<name>` + `app/shared` per app. Output `true`/`false` per app.
- `<app>-build`: runs only when its app changed, uploads `<app>_<os>.zip`.
- `reuse`: copies `<app>_*.zip` of unchanged apps from the previous release, then writes and uploads `release.oh`.
- Top-level env: `RELEASE_SCHEMA_VERSION` and `RELEASE_PROJECTS` (comma list, position = id).

**`release.oh` format** (big-endian, values only, fixed order):
```
u8[2]  magic          "OH"
u8     schemaVersion  1
u8     count
entries[count]
  u8   projectId      0 openhotel, 1 web, 2 auth, 3 asset-editor, 4 onet, 5 static
  u16  major
  u16  minor
  u16  patch
```
- All projects listed every release (4 + 7 per project, 46 bytes for 6).
- Changed app: the tag's version. Unchanged app: its version from the previous `release.oh`. No previous file (or other schema): unchanged apps get the previous tag's version, changed apps the new one. No previous tag: everyone gets the tag's version.
- The release version is not stored: it is the tag the file lives in.
- Pre-release suffix is not stored (`1.1.0-beta.1` is written as `1.1.0`).
- Project ids: only append to `RELEASE_PROJECTS`, never reorder or remove.

Example, release `v0.9.0`:
```
4F 48 01 06
00 0000 0007 0005   openhotel     0.7.5
01 0000 0009 0000   web           0.9.0
02 0000 0009 0000   auth          0.9.0
03 0000 0008 0009   asset-editor  0.8.9
04 0000 0008 0000   onet          0.8.0
05 0000 0009 0000   static        0.9.0
```

## Tasks
- [ ] Updaters (openhotel, onet, auth, ...): on a new release, download only `release.oh`, check `"OH"` + schema, find own `projectId`, compare with the installed version. Equal: skip. Higher: download `<app>_<os>.zip`.
- [ ] Shared reader for `release.oh` in `app/shared` so every app parses it the same way.
- [ ] Decide how updaters treat pre-releases, since the suffix is not in the file.

## Open questions
1. Store pre-release info (`u8 pre` per entry, schema 2)?

## Links
- [Org restructuring](restructuring.md), [monorepo](monorepo.md)
- [utils#92](https://github.com/openhotel/utils/issues/92): updater leaves old client JS behind
