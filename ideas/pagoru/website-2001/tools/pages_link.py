# Link app page. Exec'd by pages_assets.py (needs kv, tbl).
# ---------- Link app ----------
LUA = '''-- OpenHotel extension for Aseprite (sketch)
local ws = WebSocket{ url = "ws://127.0.0.1:48621", deflate = false,
  onreceive = function(t, msg) if t == WebSocketMessageType.OPEN then ws:sendText("hello") end end }
app.command.ExportSpriteSheet{ ui = false, askOverwrite = false,
  type = SpriteSheetType.PACKED, textureFilename = tmp .. ".png", dataFilename = tmp .. ".json",
  dataFormat = SpriteSheetDataFormat.JSON_ARRAY, listLayers = true, listTags = true, listSlices = true }
ws:sendText(json.encode({ kind = "furniture", sheet = tmp .. ".json" }))'''
link = f'''      <div class="blk box">
        <h2>OpenHotel Link</h2>
        <p>A small app on your computer. It lets this website and your pixel art program talk to each other, so you send art to OpenHotel without uploading files by hand.</p>
        <p><a class="btn main" href="#">Download for Windows</a> <a class="btn" href="#">macOS</a> <a class="btn" href="#">Linux</a></p>
        <p><span class="badge on">Running</span> <span class="hint">This page sees Link on 127.0.0.1:48621 (shown here only as a preview)</span></p>
        <p>Link code: <b class="code" style="display:inline-block;padding:2px 8px">482 913</b> <span class="hint">type it in the app once. Works 10 minutes.</span></p>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense"><h2>How it works</h2>
        <ol class="steps"><li>Link runs on your computer and listens only on <code>127.0.0.1</code>. Nothing is open to the network.</li><li>This website asks Link for the file you pick; the browser allows it only for openhotel.club.</li><li>The Aseprite extension sends your sprite to Link. Link checks it and shows it here as a preview.</li><li>You press Send for review on the website. Only OpenHotel files are uploaded.</li></ol>
        <h3>What Aseprite sends</h3>
        ''' + tbl(["In Aseprite", "Becomes"], [["Layer named <code>north</code>, <code>east</code>...", "A direction"], ["Tags <code>door:open</code>", "Action states"], ["Slice <code>icon</code>", "icon.texture"], ["Slice pivot", "pivot x, y"], ["Frames", "Sprite sheet frames"], ["User data of the sprite", "id, name, size, lang (JSON)"]]) + f'''
      </div>
      <div class="blk box dense"><h2>The Aseprite extension</h2>
        <p>Written in Lua and installed as <code>openhotel.aseprite-extension</code>. Aseprite 1.3 has a <code>WebSocket</code> in its scripting API, which is what talks to Link. If your version lacks it, the extension saves to <code>~/OpenHotel/outbox</code> and Link picks the files up. <span class="hint">To verify against the Aseprite API docs.</span></p>
        <pre class="pre">{LUA}</pre>
      </div></div><div class="col">
      <div class="blk box dense"><h2>Resprite (iPad)</h2>
        <p>Resprite can't run a plugin and the iPad has no <code>localhost</code> for this website to reach, so Link isn't possible there. Use files instead:</p>
        <ol class="steps"><li>Export a sprite sheet (.png + .json) or .aseprite to Files.</li><li>Open <a href="#create">Create an asset</a> in Safari and pick the file.</li></ol>
        <p class="hint">If Resprite has a share sheet or URL scheme for sending to a web page, we can use it later. Unverified.</p>
      </div>
      <div class="blk box dense"><h2>Linked programs</h2>
        ''' + kv([("Aseprite on PC", '<a class="danger" href="#">Unlink</a>'), ("Link app", "v0.1 · up to date")]) + '''
      </div>
      </div></div>
'''

