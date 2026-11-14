# Binary assets: container format

Part of: [binary assets](binary-assets.md) · Author: pagoru · Status: proposed · 2026-11-14

All integers little-endian. Payloads use a fixed schema per kind and version (no CBOR/JSON): field names and types are never stored, only values in a known order.

## File layout
```
[Header 32 B][Section table N x 24 B][Section payloads ...][Signature 72 B]
```

## Header (32 bytes)
| Off | Type | Field | Notes |
|---|---|---|---|
| 0 | u8[4] | magic | `OHA1` (0x4F 0x48 0x41 0x31) |
| 4 | u16 | formatVersion | starts at 1; reader refuses unknown majors |
| 6 | u8 | kind | 1 furniture, 2 public room (room for more) |
| 7 | u8 | flags | bit0 deflate, bit1 obfuscated, bit2 signed |
| 8 | u16 | sectionCount | |
| 10 | u16 | keyId | which public key signed it (0 = unsigned) |
| 12 | u32 | fileLength | whole file, sanity check |
| 16 | u8[8] | assetIdHash | first 8 B of SHA-256(asset id), quick lookup |
| 24 | u16 | schemaVersion | payload schema for this kind |
| 26 | u16 | assetRevision | bumped by the editor on every save |
| 28 | u32 | headerCrc | CRC32 of bytes 0..27 |

## Primitives
`u8 u16 u32 i16 i32 f32` · `str` = u16 length + UTF-8 · `bytes` = u32 length + raw · `list<T>` = u16 count + items.

## Section table entry (24 bytes)
| Off | Type | Field |
|---|---|---|
| 0 | u8[4] | tag (FourCC) |
| 4 | u32 | offset (from file start) |
| 8 | u32 | storedLength |
| 12 | u32 | rawLength (after inflate) |
| 16 | u32 | crc32 (of raw bytes) |
| 20 | u16 | index (for repeated tags, e.g. several images) |
| 22 | u16 | sectionFlags (bit0 deflate) |

## Sections
| Tag | Kind | Payload |
|---|---|---|
| `META` | all | str id, str author, str editorVersion, u32 createdAt, u32 updatedAt |
| `DATA` | furniture | `@oh/core` furniture type in schema order (size, directions, type, hit area, interactions) |
| `DATA` | room | layout, spawn point, doors, list of placed furniture (str id, i16 x, i16 y, i16 z, u8 dir), u16 max users |
| `SHET` | all | list of frames (str name, u8 image, u16 x, y, w, h, i16 pivotX, pivotY), list of animations |
| `IMGS` | all | raw PNG (or WebP) bytes, one section per atlas/preview, `index` orders them |
| `LANG` | all | list of locales (str locale, list of (str key, str value)): name, description, room texts |

Unknown tags are skipped, so new sections do not break old readers. Adding a field means a new `schemaVersion`; readers keep decoders for older versions.

## Integrity and tamper resistance
1. **CRC32** per section and on the header: catches corruption, not tampering.
2. **Signature trailer** (72 B): `u16 keyId · u16 alg (1 = Ed25519) · u32 reserved · u8[64] sig`. Signed bytes = everything before the trailer. Verify with WebCrypto `Ed25519` (Deno, current Chrome, Firefox, Safari).
3. **Compression**: deflate via `CompressionStream` on schema sections; PNG is already compressed, stored as is.
4. **Obfuscation (optional)**: XOR payloads with a keystream from SHA-256(assetIdHash + salt). Stops `strings`/binwalk-style poking only; the salt ships in the client, so it is not encryption.

Order on write: schema encode, deflate, obfuscate, CRC (on raw), table, sign. Read in reverse; verify the signature **before** decoding anything.

## Limits
- Max file 16 MB, max 64 sections, reject overlapping or out-of-range offsets (fuzz the reader).
- Check every length against the section end before reading; never trust lengths from the file.
