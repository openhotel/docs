# Binary assets: container format

Part of: [binary assets](binary-assets.md) · Author: pagoru · Status: proposed · 2026-11-14

All integers little-endian. Payloads use a fixed schema per kind and version (no CBOR/JSON): field names and types are never stored, only values in a known order.

## File layout
```
[Header 32 B][Section table N x 24 B][Section payloads ...][Signature 72 B]
```

## Header (32 bytes)
First 8 bytes: what the file is and which schema it uses.

| Off | Type | Field | Notes |
|---|---|---|---|
| 0 | u8[4] | magic | `OHA\0` (0x4F 0x48 0x41 0x00): it is an OpenHotel asset |
| 4 | u16 | kind | what it is, see table below |
| 6 | u16 | schemaVersion | schema of that kind used by the payload |
| 8 | u16 | containerVersion | layout of header/table/trailer, starts at 1 |
| 10 | u8 | flags | bit0 deflate, bit1 obfuscated, bit2 signed |
| 11 | u8 | reserved | 0 |
| 12 | u16 | sectionCount | |
| 14 | u16 | keyId | which public key signed it (0 = unsigned) |
| 16 | u32 | fileLength | whole file, sanity check |
| 20 | u32 | assetRevision | bumped by the editor on every save |
| 24 | u8[4] | assetIdHash | first 4 B of SHA-256(asset id), quick lookup |
| 28 | u32 | headerCrc | CRC32 of bytes 0..27 |

## Kinds
| kind | Asset | Required sections |
|---|---|---|
| 1 | furniture | META, DATA, SHET, IMGS, LANG |
| 2 | public room | META, DATA, IMGS, LANG (SHET optional) |
| 3+ | reserved | defined when added |

Each `(kind, schemaVersion)` pair maps to one decoder in `@oh/core`. A new field in furniture means furniture `schemaVersion` 2; other kinds are not affected.

## Header check (reader, in order)
1. Magic is `OHA\0`.
2. `kind` is known and is the one the caller asked for (loading a room as furniture fails).
3. `schemaVersion` has a decoder for that kind: older ones are decoded and upgraded in memory, newer ones are refused ("update the hotel").
4. `containerVersion` supported, `headerCrc` and `fileLength` match.
5. Signature, then sections.

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
2. **Signature trailer** (72 B): `u16 keyId · u16 alg (1 = Ed25519) · u32 reserved · u8[64] sig`. Signed bytes = everything before the trailer. WebCrypto `Ed25519`.
3. **Compression**: deflate via `CompressionStream` on schema sections; PNG is already compressed, stored as is.
4. **Obfuscation (optional)**: XOR with a keystream from SHA-256(assetIdHash + salt). The salt ships in the client: not encryption.

Order on write: schema encode, deflate, obfuscate, CRC (on raw), table, sign. Read in reverse; verify the signature **before** decoding anything.

Reader limits: see [rollout](binary-assets-rollout.md#reader-limits).
