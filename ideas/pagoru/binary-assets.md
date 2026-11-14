# Binary furniture and public room assets

- Author: pagoru
- Status: proposed
- Created: 2026-11-14 · Updated: 2026-11-14
- Affects: openhotel, asset-editor, core (onet later)
- Discussion: none

Parts: [format](binary-assets-format.md) · [rollout](binary-assets-rollout.md)

## Summary
Pack every furniture and every public room into one binary file that holds its image, sprite sheet, data and lang. Only the asset-editor can create or change these files; openhotel only reads them.

## Motivation
- Today furniture and rooms are loose files under `app/server/assets/` (rooms, locales, furniture) (exact layout unverified). Anyone can edit a png or a yml and change an asset.
- Public rooms are being built now ([openhotel#1124](https://github.com/openhotel/openhotel/issues/1124), epic [openhotel#277](https://github.com/openhotel/openhotel/issues/277), editor tab [asset-editor#11](https://github.com/openhotel/asset-editor/issues/11)), so the format should land before more rooms exist.
- One file per asset is easier to ship (onet collections, static, hotel binary) than a folder of files.

## Proposal (short)
| Piece | Where | What |
|---|---|---|
| Container `.oha` | spec in [format](binary-assets-format.md) | magic + version + kind + section table + signature |
| Sections | same | `META`, `DATA`, `SHET`, `IMGS`, `LANG` (CBOR + raw images) |
| Reader | `@oh/core` | pure isomorphic decode + verify (DataView, CompressionStream, WebCrypto) |
| Writer | asset-editor only | encode + sign; never published in core |
| Signing key | asset-editor server | Ed25519 private key; hotels ship the public key |
| Loader | openhotel server | loads `.oha` at boot, rejects bad signature |
| Client | openhotel client | gets decoded data/sheet/images from the hotel, no raw files |

## What this does and does not give
- **Gives:** an edited file is detected and refused (signature), corrupted files are caught (CRC), casual editing needs more than an image editor or text editor.
- **Does not give:** real secrecy. The client must decode images to draw them, so pixels can always be pulled from the browser. A hotel owner runs their own binary and can patch out the check. This is **deterrence and integrity**, not DRM.
- The signature is what matters; compression and obfuscation only raise the effort bar.

## Impact
- Asset sources stop being diffable in git; reviews happen in the editor (see open question 6).
- asset-editor becomes mandatory for any art change, including fixes like [openhotel#718](https://github.com/openhotel/openhotel/issues/718) hit areas.
- Self-hosted hotels cannot add their own furniture unless they get a signing key (open question 1).
- Migration plan: [rollout](binary-assets-rollout.md).

## Open questions
1. One OpenHotel key, or per-creator keys with a trust list in hotel config? Custom furniture for self-hosted hotels?
2. Reuse onet collection signatures (`system/collections/signature.ts`) and key, or a new key?
3. Should `version: development` hotels accept unsigned `.oha`?
4. Image codec: PNG (lossless, current) or WebP lossless (smaller)?
5. Keep the light obfuscation layer, or only compress + sign?
6. Keep source files (png, yml, json) in a private repo for history, or make `.oha` the only source?
7. One extension `.oha` with a kind byte, or `.ohf` (furniture) / `.ohr` (room)?
8. Should the client verify the signature too, or trust its hotel?

## Links
[asset-editor](../../projects/asset-editor.md) · [openhotel](../../projects/openhotel.md) · [core](../../projects/core.md) · [onet](../../projects/onet.md) · [socket idea](socket.md) (same CBOR choice)
