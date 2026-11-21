# Aseprite link: test kit and protocol

Part of [aseprite-link](aseprite-link.md). Files in [aseprite-link/](aseprite-link/).

## Run
1. `deno run --allow-net --allow-read relay.ts` in `aseprite-link/`.
2. Open http://127.0.0.1:48621, click "Download Aseprite plugin", double-click `oh-link.aseprite-extension`.
3. In Aseprite: File > OpenHotel Link (next to Scripts). Allow the file and network prompts.
4. On the page: width and height, "Create in Aseprite", then draw.

## Files
| File | Role |
|---|---|
| `relay.ts` | Link stand-in: relay, origin check, serves the page and zips the extension on the fly |
| `index.html` | Website stand-in: version check, create image, live view, sprite sheet |
| `oh-link.lua` | Aseprite extension (`init(plugin)` adds the command) |
| `package.json` | Aseprite extension manifest (not npm) |

## Protocol v1
Sockets: `ws://127.0.0.1:48621/ws?role=aseprite` and `?role=web`. Bump `VERSION` in `oh-link.lua` and `index.html` only when this table changes.

| Web sends | Plugin does |
|---|---|
| `hello` | replies `hello <version>` |
| `deny <webVersion>` | disconnects, dialog asks to update |
| `command <Name> key=value ...` | runs `app.command.<Name>{...}` (numbers, true/false converted) |
| `frame` | sends the current frame |
| `sheet` | sends `sheet <json>` then the sheet PNG |
| `live on/off` | sends the current frame after every change |

Plugin to web: text `hello <v>`, `error <text>`, `sheet <json>`; binary `"<kind> <w> <h>\n"` + PNG bytes (`kind` = `frame` or `sheet`).

Example: create a 64x64 sprite = `command NewFile ui=false width=64 height=64`.
