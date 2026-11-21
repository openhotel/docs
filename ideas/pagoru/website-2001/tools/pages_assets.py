# Library, marketplace, item, collection, creations, create, link app. Exec'd by subpages.py after pages_social.py.
def img(f, w, h, alt=""): return f'<img src="assets/oh/{f}.png" width="{w}" height="{h}" alt="{alt}">'
def ct(f, w, h): return f'<div class="ct">{img(f, w, h)}</div>'
HOTEL = "Sunset Plaza"; HV = "0.156.0"
TH = {"tel": ("furni-icon-telephone", 24, 50), "flag": ("furni-icon-flag", 18, 22), "poster": ("furni-icon-poster", 16, 24),
      "pool": ("news-pool", 64, 64), "disco": ("news-disco", 64, 64), "atrium": ("news-atrium", 64, 64), "booths": ("news-booths", 64, 64),
      "c": ("av-idle-c", 21, 66), "b": ("av-idle-b", 21, 66), "e": ("av-idle-e", 21, 66), "coll": ("news-flag", 64, 64)}
tb = lambda k: ct(*TH[k])
def state(st, ver):
    return {"added": '<span class="badge on">In hotel</span>', "update": f'<button class="btn main" type="button">Update to {ver}</button>'}.get(st, '<button class="btn" type="button">Add</button>')

# kind, thumb, name, by, ver, schema, minHotel, hotels, downloads, rating, in-hotel state
ITEMS = [
 ("Furniture", "tel", "Telephone booth", "OpenHotel", "1.2", 3, "0.140", "1,204", "18.2k", "4.8", "update"),
 ("Room", "pool", "Rooftop Pool", "Mintleaf", "2.1", 2, "0.150", "312", "4.1k", "4.5", "update"),
 ("Clothes", "c", "Striped shirt", "Wanda", "1.0", 1, "0.120", "880", "9.0k", "4.1", "added"),
 ("Furniture", "flag", "Pirate flag", "Captain_K", "1.0", 3, "0.140", "540", "6.7k", "4.6", "added"),
 ("Collection", "coll", "Beach set (12)", "Mintleaf", "1.3", 3, "0.145", "260", "2.2k", "4.7", None),
 ("Room", "disco", "Disco Hall", "Pebbles", "1.0", 2, "0.150", "96", "1.1k", "3.9", None),
 ("Clothes", "b", "Red jacket", "Lumen", "1.0", 1, "0.120", "410", "3.5k", "4.3", None),
 ("Furniture", "poster", "Poster A-24", "OpenHotel", "1.0", 3, "0.140", "990", "12k", "4.0", "added"),
 ("Collection", "coll", "Pirate pack (8)", "Captain_K", "1.1", 3, "0.140", "180", "1.6k", "4.4", None),
 ("Room", "atrium", "The Atrium", "OpenHotel", "1.2", 2, "0.150", "540", "7.3k", "4.9", "added"),
 ("Clothes", "e", "Summer dress", "nightbus", "1.2", 1, "0.120", "205", "1.9k", "3.8", None),
 ("Furniture", "poster", "Neon sign", "Nightowl", "1.0", 3, "0.140", "58", "640", "4.2", None),
]
def mrow(k, t, n, by, v, sc, mh, ho, dl, r, st):
    link = "#collection" if k == "Collection" else "#item"
    return (f'<tr><td>{tb(t)}</td><td><a href="{link}"><b>{n}</b></a><br><span class="hint">by {by}</span></td><td>{k}</td>'
            f'<td class="num">{v}<br><span class="hint">schema {sc}</span></td><td class="num">{ho}</td><td class="num">{dl}</td><td class="num">★ {r}</td>'
            f'<td class="ra">{state(st, v)} <a class="dl" href="#" title="Download the signed .oha file">Download</a></td></tr>\n')

FLT = lambda extra="": '''<form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search" aria-label="Search">
  <select class="in" aria-label="Sort"><option>Most used</option><option>Newest</option><option>Best rated</option><option>Most downloaded</option></select>
  <label class="chk"><input type="checkbox" checked> Works with ''' + HOTEL + ''' (v''' + HV + ''')</label>''' + extra + '</form>'
KINDS = lambda cur: '<div class="ktabs" role="tablist">' + "".join(f'<a class="btn{" main" if k == cur else ""}" href="#market">{k}</a>' for k in ("All", "Rooms", "Furniture", "Clothes", "Collections")) + '</div>'

market = f'''      <div class="blk box dense">
        <h2>Marketplace</h2>
        <p class="hint">Free assets made by guests. Adding to <b>{HOTEL}</b> <select class="in sel-s" aria-label="Hotel"><option>{HOTEL}</option><option>Pixel Inn</option></select> · <a href="#create">Create an asset</a> · <a href="#mine">Your creations (4)</a> · <a href="#link">Link app</a></p>
        {KINDS("All")}
        {FLT()}
        <div class="tbl"><table><tr><th></th><th>Name</th><th>Kind</th><th class="num">Version</th><th class="num">Hotels</th><th class="num">Downloads</th><th class="num">Rating</th><th></th></tr>
''' + "".join(mrow(*i) for i in ITEMS) + '''        </table></div>
        <div class="pager"><span class="hint">1-12 of 1,860 · 3 hidden: they need a newer hotel version (0.158 or later)</span><span><a href="#market">Next</a> &gt;&gt;</span></div>
      </div>
'''

# ---------- Item page ----------
VERS = [("1.2", 3, "0.140", "21 Nov 2026", "Opening animation is smoother.", "ok", "update"),
        ("1.1", 3, "0.140", "02 Nov 2026", "Fixes the west side.", "ok", "now"),
        ("1.0", 2, "0.120", "12 Aug 2026", "First version.", "ok", ""),
        ("2.0", 4, "0.158", "Preview", "New schema with sound.", "no", "")]
def vrow(v, sc, mh, d, ch, comp, st):
    c = '<span class="badge on">Works</span>' if comp == "ok" else f'<span class="badge">Needs {mh}</span>'
    a = {"update": '<button class="btn main" type="button">Update</button>', "now": '<span class="hint">In hotel now</span>'}.get(st, "") if comp == "ok" else ""
    return f'<tr><td><b>{v}</b></td><td class="num">{sc}</td><td class="num">{mh}</td><td>{d}</td><td>{ch}</td><td>{c}</td><td class="ra">{a}</td></tr>\n'
cmts = comments(True)
item = f'''      <div class="blk box">
        <p class="crumb"><a href="#market">Marketplace</a> &gt; Furniture &gt; Telephone booth</p>
        <div class="ihead"><div class="ipv">{img("furni-telephone", 48, 98, "Telephone booth")}</div>
          <div><h2>Telephone booth</h2>
            <p class="hint">by <a href="#">OpenHotel</a> · Furniture · id <code>teleports@telephone</code></p>
            <p>Step in, wait for the light and come out in another booth. Link it to any other booth you own.</p>
            <p><span class="stars">★★★★<span class="dim">★</span></span> <b>4.8</b> <span class="hint">from 1,102 votes · 18.2k downloads · in 1,204 hotels</span></p>
            <div class="acts"><button class="btn main" type="button">Update {HOTEL} to 1.2</button><a class="btn" href="#">Download 1.2</a></div></div></div>
      </div>
      <div class="blk box dense">
        <h2>Versions</h2>
        <p class="hint">Each version has a schema (the shape of the data) and the oldest hotel it needs. Versions your hotel can't run are shown dimmed.</p>
        <div class="tbl"><table><tr><th>Version</th><th class="num">Schema</th><th class="num">Hotel from</th><th>Date</th><th>Changes</th><th>{HOTEL} v{HV}</th><th></th></tr>
''' + "".join(vrow(*v) for v in VERS) + '''        </table></div>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense">
        <h2>Data in this version</h2>
        <dl class="kv"><div><dt>Revision</dt><dd>1.2</dd></div><div><dt>Type</dt><dd>furniture</dd></div><div><dt>Size (w × d × h)</dt><dd>1 × 1 × 2</dd></div><div><dt>Icon texture</dt><dd>telephone-icon</dd></div><div><dt>Languages</dt><dd>English, Español</dd></div><div><dt>Sprite sheet</dt><dd>png · 96 × 196 · scale 1 · 9 frames</dd></div><div><dt>File</dt><dd>14 KB · signed by OpenHotel</dd></div></dl>
        <div class="tbl"><table><tr><th>Action</th><th>States</th><th>Default</th></tr><tr><td>door</td><td>closed, open</td><td>closed</td></tr></table></div>
        <div class="tbl"><table><tr><th>Direction</th><th class="num">Textures</th><th class="num">zIndex</th><th class="num">Pivot</th></tr>
          <tr><td>north</td><td class="num">2</td><td class="num">0, 1</td><td class="num">24, 98</td></tr><tr><td>east</td><td class="num">2</td><td class="num">0, 1</td><td class="num">24, 98</td></tr></table></div>
      </div>
''' + cmts + f'''      </div><div class="col">
      <div class="blk box">
        <h2>In your hotels</h2>
        <dl class="kv"><div><dt>{HOTEL}</dt><dd>1.1 · <b>update</b></dd></div><div><dt>Pixel Inn</dt><dd><span class="hint">not added</span></dd></div></dl>
      </div>
''' + inter.replace("4.2", "4.8").replace("86 votes", "1,102 votes").replace("1,204</b> views", "18,204</b> downloads") + '''      <div class="blk box dense">
        <h2>Information</h2>
        <dl class="kv"><div><dt>Published</dt><dd>12 Aug 2026</dd></div><div><dt>Updated</dt><dd>21 Nov 2026</dd></div><div><dt>Downloads</dt><dd>18,204</dd></div><div><dt>Used by</dt><dd>1,204 hotels</dd></div><div><dt>Part of</dt><dd><a href="#collection">Beach set</a></dd></div><div><dt>Licence</dt><dd>CC BY-NC-SA 4.0</dd></div></dl>
        <p><a class="danger" href="#">Report</a></p>
      </div>
      </div></div>
'''

# ---------- Collection page ----------
INH = '<span class="badge on">In hotel</span>'; NOT = '<span class="hint">not added</span>'
CI = [("tel", "Beach hut", "1.0", "furniture"), ("flag", "Beach flag", "1.1", "furniture"), ("poster", "Surf poster", "1.0", "furniture"),
      ("tel", "Shower", "1.2", "furniture"), ("flag", "Palm tree", "1.0", "furniture"), ("poster", "Towel", "1.0", "furniture")]
collection = f'''      <div class="blk box">
        <p class="crumb"><a href="#market">Marketplace</a> &gt; Collections &gt; Beach set</p>
        <div class="ihead"><div class="ipv">{img("news-flag", 64, 64)}</div>
          <div><h2>Beach set</h2><p class="hint">by <a href="#">Mintleaf</a> · Collection · id <code>beach-set</code> · 12 furniture</p>
            <p>Everything for a beach room: huts, palms, towels and a shower.</p>
            <p><span class="stars">★★★★<span class="dim">★</span></span> <b>4.7</b> <span class="hint">from 190 votes · 2.2k downloads · in 260 hotels</span></p>
            <div class="acts"><button class="btn main" type="button">Add all 12 to {HOTEL}</button><a class="btn" href="#">Download .collection</a></div></div></div>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense"><h2>Furniture in this collection (12)</h2>
        <div class="tbl"><table><tr><th></th><th>Name</th><th class="num">Version</th><th>{HOTEL}</th></tr>
''' + "".join(f'<tr><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a></td><td class="num">{v}</td><td>{INH if i == 1 else NOT}</td></tr>\n' for i, (t, n, v, k) in enumerate(CI)) + f'''        </table></div>
        <div class="pager"><span class="hint">6 of 12</span><span><a href="#collection">More</a> &gt;&gt;</span></div></div>
''' + cmts + f'''      </div><div class="col">
''' + inter + '''      <div class="blk box dense"><h2>Collection data</h2>
        <dl class="kv"><div><dt>id</dt><dd>beach-set</dd></div><div><dt>category.label</dt><dd>Beach</dd></div><div><dt>category.description</dt><dd>Sun and sand</dd></div><div><dt>minHotelVersion</dt><dd>0.145</dd></div><div><dt>Schema</dt><dd>3</dd></div><div><dt>Published</dt><dd>02 Sep 2026</dd></div><div><dt>Updated</dt><dd>14 Nov 2026</dd></div></dl></div>
      </div></div>
'''

# ---------- Your creations ----------
MINE = [("Furniture", "tel", "Telephone booth", "1.2", "Live", "1,204", "18.2k", "★ 4.8", ["OpenHotel", "Sunset Plaza", "Pixel Inn", "Neon Docks"]),
        ("Furniture", "poster", "Neon sign", "1.0", "Live", "58", "640", "★ 4.2", ["Sunset Plaza", "Neon Docks"]),
        ("Furniture", "flag", "Palm tree", "1.0", "In review", "0", "0", "", []),
        ("Clothes", "c", "Beach towel", "0.1", "Draft", "0", "0", "", [])]
def mine_row(k, t, n, v, s, ho, dl, r, used):
    b = '<span class="badge on">Live</span>' if s == "Live" else f'<span class="badge">{s}</span>'
    u = ("<br>".join(used) if used else "Nobody yet")
    return (f'<tr><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a><br><span class="hint">{k}</span></td><td>{b}</td><td class="num">{v}</td><td class="num">{ho}</td><td class="num">{dl}</td><td class="num">{r}</td>'
            f'<td><details class="disc"><summary class="btn">Used by</summary><p>{u}</p></details></td><td class="ra"><a class="btn" href="#create">Edit</a> <a class="btn" href="#create">New version</a></td></tr>\n')
mine = '''      <div class="blk box dense">
        <h2>Your creations</h2>
        <p class="hint">4 assets · 1,262 hotels use them · 18,840 downloads · <a href="#create">Create an asset</a> · <a href="#link">Link app</a></p>
        <div class="tbl"><table><tr><th></th><th>Name</th><th>State</th><th class="num">Version</th><th class="num">Hotels</th><th class="num">Downloads</th><th class="num">Rating</th><th></th><th></th></tr>
''' + "".join(mine_row(*m) for m in MINE) + '''        </table></div>
      </div>
      <div class="blk box dense">
        <h2>Your collections</h2>
        <div class="tbl"><table><tr><th></th><th>Collection</th><th class="num">Items</th><th class="num">Version</th><th class="num">Hotels</th><th class="num">Downloads</th><th></th></tr>
          <tr><td>''' + tb("coll") + '''</td><td><a href="#collection"><b>Beach set</b></a></td><td class="num">12</td><td class="num">1.3</td><td class="num">260</td><td class="num">2.2k</td><td class="ra"><a class="btn" href="#mine">Edit</a></td></tr>
        </table></div>
        <details class="disc newh"><summary class="btn main">Edit collection: Beach set</summary>
          <form class="form" onsubmit="event.preventDefault()">
            <label>id<input class="in" value="beach-set" disabled></label>
            <label>Category<input class="in" value="Beach"></label>
            <label>Description (optional)<input class="in" value="Sun and sand"></label>
            <label>Minimum hotel version<input class="in" value="0.145"></label>
            <fieldset class="vis"><legend>Items (tick to include)</legend>
''' + "".join(f'<label class="chk"><input type="checkbox"{" checked" if i < 4 else ""}> {n} <span class="hint">{v}</span></label>' for i, (t, n, v, k) in enumerate(CI)) + '''
            </fieldset>
            <div class="row"><button class="btn main" type="submit">Save as new version</button><button class="btn" type="button">New collection</button></div>
          </form>
        </details>
      </div>
'''

# ---------- Create (preview only) ----------
def kv(rows): return '<dl class="kv">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>"
def tbl(h, rows): return '<div class="tbl"><table><tr>' + "".join(f"<th>{x}</th>" for x in h) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table></div>"
st_furn = ('<div class="ipv">' + img("furni-telephone", 48, 98, "Preview, north") + '</div>' +
  kv([("id", "teleports@telephone"), ("revision", "1.2"), ("type", "furniture (or frame)"), ("size w × d × h", "1 × 1 × 2"), ("icon.texture", "telephone-icon"), ("minHotelVersion · schema", "0.140 · 3")]) +
  '<h3>Actions</h3>' + tbl(["id", "label", "states", "default"], [["door", "Door", "closed, open", "closed"]]) +
  '<h3>Lang</h3>' + tbl(["lang", "name", "description"], [["English", "Telephone booth", "Dial a friend"], ["Español", "Cabina", "Llama a un amigo"]]) +
  '<h3>Directions</h3>' + tbl(["direction", "texture", "zIndex", "pivot", "position", "actions"], [["north", "telephone-n", "0", "24, 98", "0, 0", "door: closed"], ["north", "telephone-n-top", "1", "24, 98", "0, 0", "door: open"], ["east", "telephone-e", "0", "24, 98", "0, 0", "door: closed"]]) +
  '<h3>Sprite sheet</h3>' + kv([("format · scale", "png · 1"), ("size", "96 × 196"), ("frames", "9"), ("animations", "2")]))
st_room = (kv([("id", "rooftop-pool"), ("revision", "2.1"), ("name", "Rooftop Pool (en), Piscina (es)"), ("size w × d", "12 × 9 tiles"), ("wall height", "3"), ("door / spawn", "tile 0,4 · facing east"), ("max users", "40"), ("minHotelVersion · schema", "0.150 · 2")]) +
  '<h3>Floor</h3><p class="hint">Tile map with heights, 108 tiles, 2 levels.</p><h3>Furniture placed</h3>' + tbl(["furniture", "tile", "direction"], [["Sunbed", "3,2", "south"], ["Telephone booth", "0,0", "east"], ["Palm tree", "11,8", "north"]]) +
  '<p class="hint">Public room fields are a proposal; the format is not final.</p>')
st_cloth = ('<div class="ipv">' + img("av-idle-c", 21, 66, "Preview") + '</div>' +
  kv([("id", "striped-shirt"), ("revision", "1.0"), ("slot", "top"), ("colours", "3 (body, stripes, sleeves)"), ("minHotelVersion · schema", "0.120 · 1")]) +
  '<h3>Lang</h3>' + tbl(["lang", "name"], [["English", "Striped shirt"], ["Español", "Camiseta de rayas"]]) +
  '<h3>Frames</h3>' + tbl(["direction", "action", "frames"], [["north", "idle", "1"], ["north", "walk", "4"], ["east", "idle", "1"], ["east", "walk", "4"]]) +
  '<p class="hint">Clothes fields are a proposal; the format is not final.</p>')
CHECKS = '<ul class="perms"><li>Schema 3 is valid</li><li>All 4 directions have textures</li><li>Icon texture exists in the sprite sheet</li><li>Name and description in English</li><li>No frame is outside the image</li></ul>'
create = f'''      <div class="blk box kb" data-state="furn">
        <h2>Create an asset</h2>
        <p>You can't draw on the website. Draw in Aseprite (or Resprite on iPad) and send it here: this page checks it and shows a preview of everything that will be saved.</p>
        <div class="row" role="group" aria-label="Kind"><button class="btn main" type="button" data-go="furn">Furniture</button> <button class="btn" type="button" data-go="room">Public room</button> <button class="btn" type="button" data-go="cloth">Clothes</button></div>
        <form class="form" onsubmit="event.preventDefault()"><label>Send a file<input class="in" type="file" accept=".aseprite,.ase,.png,.json,.oha"></label><span class="hint">.aseprite, or a .png sprite sheet with its .json, or a .oha</span></form>
        <h3>Preview</h3>
        <div class="st st-furn">{st_furn}</div><div class="st st-room">{st_room}</div><div class="st st-cloth">{st_cloth}</div>
        <h3>Checks</h3>{CHECKS}
        <div class="row" style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn main" type="button">Send for review</button><button class="btn" type="button">Save draft</button></div>
      </div>
      <div class="blk box"><h2>No app yet?</h2><p>The <a href="#link">OpenHotel Link</a> app sends from Aseprite to this page in one click. <a class="btn" href="#link">Download Link app</a></p></div>
<script>
document.querySelectorAll(".kb").forEach((box) => box.addEventListener("click", (e) => {{
  const b = e.target.closest("[data-go]");
  if (b) {{ box.dataset.state = b.dataset.go; box.querySelectorAll(".row .btn").forEach((x) => x.classList.toggle("main", x === b)); }}
}}));
</script>
'''

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
        <ol class="steps"><li>Link runs on your computer and listens only on <code>127.0.0.1</code>. Nothing is open to the network.</li><li>This website asks Link for the file you pick; the browser allows it only for openhotel.club.</li><li>The Aseprite extension sends your sprite to Link. Link checks it and shows it here as a preview.</li><li>You press Send for review on the website. Your account never leaves the website.</li></ol>
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

# ---------- Hotel assets (owner) ----------
def arow(t, n, by, cur, latest, mh, on, extra=""):
    s = (f'<span class="badge on">Up to date</span>' if cur == latest else f'<button class="btn main" type="button">Update to {latest}</button>')
    return (f'<tr><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a><br><span class="hint">by {by}</span></td><td class="num">{cur}</td><td>{s}</td><td class="num">{mh}</td>'
            f'<td><input type="checkbox"{" checked" if on else ""} aria-label="In this hotel"></td>{extra}</tr>\n')
library = f'''      <div class="blk box dense">
        <h2>Hotel assets</h2>
        <p class="hint"><select class="in sel-s" aria-label="Hotel"><option>{HOTEL}</option><option>Pixel Inn</option></select> runs v{HV} · 3 rooms · 128 furniture · 64 clothes · <b>2 updates</b> · <a href="#market">Find more in the marketplace</a> · <label class="chk" style="display:inline"><input type="checkbox"> Upload a .oha</label></p>
        {KINDS("All")}
        <div class="tbl"><table><tr><th></th><th>Name</th><th class="num">Version</th><th>Latest</th><th class="num">Hotel from</th><th>On</th><th class="num">Price</th></tr>
''' + arow("tel", "Telephone booth", "OpenHotel", "1.1", "1.2", "0.140", True, '<td class="num"><input class="in price" type="number" value="25" aria-label="Price"></td>')
library += arow("pool", "Rooftop Pool", "Mintleaf", "2.0", "2.1", "0.150", True, '<td class="num"><span class="hint">first room</span></td>')
library += arow("flag", "Pirate flag", "Captain_K", "1.0", "1.0", "0.140", True, '<td class="num"><input class="in price" type="number" value="10" aria-label="Price"></td>')
library += arow("poster", "Poster A-24", "OpenHotel", "1.0", "1.0", "0.140", False, '<td class="num"><input class="in price" type="number" value="5" aria-label="Price"></td>')
library += arow("c", "Striped shirt", "Wanda", "1.0", "1.0", "0.120", True, '<td class="num"><span class="hint">free</span></td>')
library += arow("atrium", "The Atrium", "OpenHotel", "1.2", "1.2", "0.150", True, '<td class="num"><span class="hint">public</span></td>')
library += f'''        </table></div>
        <div class="pager"><span class="hint">1-6 of 195 · versions that need a newer hotel are hidden · prices in this hotel's credits</span><span><a href="#">Next</a> &gt;&gt;</span></div>
        <p class="hint">Anyone can make assets. Only the hotel owner adds them here.</p>
      </div>
'''
