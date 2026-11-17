# Shared migration: libs

Part of [shared migration](shared-migration.md). Snapshot of `monster` on 2026-11-16.

## @oh/utils, @oh/core, @oh/pathfinding

| Lib | Files | Functions | Classes | Enums | Consts | Types | Exports | Used by apps |
|---|---|---|---|---|---|---|---|---|
| @oh/utils | 73 | 67 | 0 | 8 | 3 | 43 | 121 | 49 |
| @oh/core | 14 | 16 | 0 | 0 | 17 | 14 | 47 | 30 |
| @oh/pathfinding | 10 | 2 | 1 | 0 | 0 | 1 | 4 | 1 (`Grid`) |

Import sites: utils 230 files (openhotel/server 84, auth 78, onet 23, asset-editor 17, static 15, web 12, openhotel build 1), core 14 (onet, asset-editor client+server, openhotel/server), pathfinding 2 (openhotel/server rooms).

utils files to migrate: 49 (34 imported by apps + 15 internal deps). Not needed: ~25 (game types, lang, child workers, ports, company).

## utils deps kept
`@std/path`, `@std/fs`, `@std/yaml`, `@std/ulid`, `@std/encoding`, `@std/streams`, `@std/random` (sss), `@deno/kv-utils`, `cbor-x` (db chunks), `@da/bcrypt`, minio (`@s3`), `@zip-js` (db backups), `@xtool/dayjs`. `@oh/yaml` was declared but never imported.

## Already in app/shared before the migration
updater module, OS enum and utils, path utils, version utils and types, zip.

## Other @oh and @da libs

| Lib | Size | Used in | Symbols | Plan |
|---|---|---|---|---|
| @oh/yaml | 8 files | auth/server 1 | readYaml | use shared yaml utils |
| @da/worker | 7 files | openhotel/server 5 | getParentWorker, getChildWorker, WorkerParent | same code as utils worker, migrate that |
| @da/bcrypt | 5 files, 29 KB | onet 1, openhotel/server 2, utils tokens/encryption | hashSync, genSaltSync, compareSync | copy as is (hashes must stay identical) |
| @oh/queue | 11 files | openhotel client 9, server 2 | TickerQueue, ticker, queue | move; unused in auth, web, onet |
| @da/socket | 6 files | onet 2, openhotel/server 4 | getServerSocket, getClientSocket, ServerClient, getWebSocketUrl | move as is until the socket rewrite |
| @oh/components | dist only | static/client 3 | Table, Modal, FileInput, Button, Background | replace with shared components |
