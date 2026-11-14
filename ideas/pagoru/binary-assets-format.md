# Binary assets: container format

Part of: [binary assets](binary-assets.md) · Author: pagoru · Status: proposed · 2026-11-14

All integers little-endian. Structured payloads are CBOR, same as the [socket idea](socket.md).

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
| 24 | u32 | assetRevision | bumped by the editor on every save |
| 28 | u32 | headerCrc | CRC32 of bytes 0..27 |

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
| `META` | all | CBOR: id, name, author, editorVersion, createdAt, updatedAt |
| `DATA` | furniture | CBOR of the `@oh/core` furniture type (size, directions, type, hit area, interactions) |
| `DATA` | room | CBOR: layout, spawn point, doors, placed furniture ids + positions, max users |
| `SHET` | all | CBOR sprite sheet: frames {name, image index, x, y, w, h, pivot}, animations |
| `IMGS` | all | raw PNG (or WebP) bytes, one section per atlas/preview, `index` orders them |
| `LANG` | all | CBOR map `locale -> key -> string` (name, description, room texts) |

Unknown tags are skipped, so new sections do not break old readers.

## Integrity and tamper resistance
1. **CRC32** per section and on the header: catches corruption, not tampering.
2. **Signature trailer** (72 B): `u16 keyId · u16 alg (1 = Ed25519) · u32 reserved · u8[64] sig`. Signed bytes = everything before the trailer. Verify with WebCrypto `Ed25519` (Deno, current Chrome, Firefox, Safari).
3. **Compression**: deflate via `CompressionStream` on CBOR sections; PNG is already compressed, stored as is.
4. **Obfuscation (optional)**: XOR payloads with a keystream from SHA-256(assetIdHash + salt). Stops `strings`/binwalk-style poking only; the salt ships in the client, so it is not encryption.

Order on write: CBOR encode, deflate, obfuscate, CRC (on raw), table, sign. Read in reverse; verify the signature **before** decoding anything.

## Limits
- Max file 16 MB, max 64 sections, reject overlapping or out-of-range offsets (fuzz the reader).
- CBOR decode with depth and size limits; never trust lengths from the file.
