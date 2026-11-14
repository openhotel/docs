# Binary assets: reader, writer and migration

Part of: [binary assets](binary-assets.md) · Author: pagoru · Status: proposed · 2026-11-14

## Code placement
| Piece | Repo / path (proposed) | Notes |
|---|---|---|
| Types, tags, consts | `@oh/core` `src/binary-asset/` | isomorphic, no Deno APIs ([core](../../projects/core.md) rule) |
| `readAsset(bytes, keys)` | `@oh/core` | returns `{ meta, data, sheet, images: Blob[], lang }` or throws a typed error |
| `writeAsset(...)` + signing | asset-editor server only | private key from env/secret, never in the client or in core |
| Pack CLI | asset-editor `deno task pack <dir>` | old folder format to `.oha`, used once for migration |
| Server loader | openhotel `system/game/furniture`, `rooms/public` | loads `*.oha` at boot, logs and skips bad files |
| Client | openhotel client | asks the hotel for decoded data; images to Pixi via `createImageBitmap` |

## Reader limits
- Max file 16 MB, max 64 sections, reject overlapping or out-of-range offsets (fuzz the reader).
- Check every length against the section end before reading; never trust lengths from the file.

## asset-editor flow
- Open `.oha` (verify + decode), edit, save: bump `assetRevision`, re-sign on the editor server.
- Import old folder format (png + sheet json + yml + locales) for the migration.
- Public rooms tab ([asset-editor#11](https://github.com/openhotel/asset-editor/issues/11)) writes `kind = 2`.
- Export straight to onet collections later (export path not wired yet, see [asset-editor](../../projects/asset-editor.md)).

## openhotel flow
- Server: `assets/furniture/*.oha`, `assets/rooms/*.oha`; public keys in code (keyId to key), extra keys optional in `config.yml` (open question 1).
- Proxy serves `.oha` bytes as is (client decodes with core) or decoded parts; pick one (proposed: bytes as is, one request per asset, cacheable).
- `version: development` may allow unsigned files (open question 3), never in release builds.

## Migration steps
1. Write the spec (this idea) and freeze `formatVersion = 1`.
2. core: reader + tests (round trip, bad magic, bad CRC, bad signature, truncated, fuzz).
3. asset-editor: writer, signing, pack CLI, open/save `.oha`.
4. openhotel: loader that reads **both** formats, behind a flag.
5. Pack all furniture and the public rooms of [openhotel#1124](https://github.com/openhotel/openhotel/issues/1124); compare decoded output with the old loader in a test.
6. Switch the flag, delete old loose files and the old loader in the same release.
7. onet collections move to `.oha` (separate step).

Rollback: keep the old loader one release behind the flag.

## Tasks to open (when accepted)
- core: binary asset reader + spec constants.
- asset-editor: writer, signing key setup, pack CLI, open/save `.oha`.
- asset-editor: public rooms tab writes `.oha` (extends #11).
- openhotel: `.oha` loader for furniture and public rooms (#1124).
- openhotel: remove loose furniture/room files after migration.
- docs: move facts into `projects/` when done.
