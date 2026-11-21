# Marketplace, item, collection, creations, create, catalog, link. Exec'd by subpages.py after pages_social.py.
def img(f, w, h, alt=""): return f'<img src="assets/oh/{f}.png" width="{w}" height="{h}" alt="{alt}">'
def ct(f, w, h): return f'<div class="ct">{img(f, w, h)}</div>'
HOTEL = "Sunset Plaza"; HV = "0.156.0"; MAXS = 4  # the hotel version runs schemas 1 to MAXS
TH = {"tel": ("furni-icon-telephone", 24, 50), "flag": ("furni-icon-flag", 18, 22), "poster": ("furni-icon-poster", 16, 24),
      "pool": ("news-pool", 64, 64), "disco": ("news-disco", 64, 64), "atrium": ("news-atrium", 64, 64),
      "c": ("av-idle-c", 21, 66), "b": ("av-idle-b", 21, 66), "e": ("av-idle-e", 21, 66), "coll": ("news-flag", 64, 64)}
tb = lambda k: ct(*TH[k])
def stars(r):
    n = round(float(r)); return f'<span class="stars" title="{r} of 5">{"★" * n}<span class="dim">{"★" * (5 - n)}</span></span>'
def sch(n): return f'<span class="badge on">Schema {n}</span>' if n <= MAXS else f'<span class="badge">Schema {n} not supported</span>'
def kv(rows): return '<dl class="kv">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>"
def tbl(h, rows): return '<div class="tbl"><table><tr>' + "".join(f"<th>{x}</th>" for x in h) + "</tr>" + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows) + "</table></div>"
INCAT = '<span class="badge on">In catalog</span>'
exec(open(T + "pages_link.py").read())

# ---------- Marketplace ----------
# kind, thumb, name, by, version, schema, hotels, rating, version in my catalog
ITEMS = [
 ("Furniture", "tel", "Telephone booth", "OpenHotel", "1.2", 3, "1,204", "4.8", "1.1"),
 ("Room", "pool", "Rooftop Pool", "Mintleaf", "2.1", 2, "312", "4.5", "2.0"),
 ("Clothes", "c", "Striped shirt", "Wanda", "1.0", 1, "880", "4.1", "1.0"),
 ("Furniture", "flag", "Pirate flag", "Captain_K", "1.0", 3, "540", "4.6", "1.0"),
 ("Collection", "coll", "Beach set (12)", "Mintleaf", "1.3", 3, "260", "4.7", None),
 ("Room", "disco", "Disco Hall", "Pebbles", "1.0", 2, "96", "3.9", None),
 ("Clothes", "b", "Red jacket", "Lumen", "1.0", 1, "410", "4.3", None),
 ("Furniture", "poster", "Poster A-24", "OpenHotel", "1.0", 3, "990", "4.0", "1.0"),
 ("Collection", "coll", "Pirate pack (8)", "Captain_K", "1.1", 3, "180", "4.4", None),
 ("Room", "atrium", "The Atrium", "OpenHotel", "1.2", 2, "540", "4.9", "1.2"),
 ("Clothes", "e", "Summer dress", "nightbus", "1.2", 1, "205", "3.8", None),
 ("Furniture", "poster", "Neon sign", "Nightowl", "1.0", 3, "58", "4.2", None),
]
def mrow(k, t, n, by, v, sc, ho, r, mine):
    link = "#collection" if k == "Collection" else "#item"
    note = (f'{mine}' + (' <b>update</b>' if mine != v else '')) if mine else '<span class="hint">-</span>'
    return (f'<tr><td>{tb(t)}</td><td><a href="{link}"><b>{n}</b></a><br><span class="hint">{k} · {by}</span></td>'
            f'<td class="num">{v}</td><td><span class="badge{" on" if sc <= MAXS else ""}" title="Schema {sc}">{sc}</span></td><td class="num">{note}</td><td class="num">{ho}</td><td class="num">{stars(r)}</td></tr>\n')
market = f'''      <div class="split3 narrow"><div class="col">
      <div class="blk box dense">
        <h2>Marketplace</h2>
        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search" aria-label="Search">
          <select class="in" aria-label="Kind"><option>Everything</option><option>Public rooms</option><option>Furniture</option><option>Clothes</option><option>Collections</option></select>
          <select class="in" aria-label="Sort"><option>Most used</option><option>Newest</option><option>Best rated</option></select>
          <label class="chk"><input type="checkbox" checked> Only schemas {HOTEL} runs (1 to {MAXS})</label></form>
        <div class="tbl"><table><tr><th></th><th>Name</th><th class="num">Version</th><th>Schema</th><th class="num">Yours</th><th class="num">Hotels</th><th class="num">Rating</th></tr>
''' + "".join(mrow(*i) for i in ITEMS) + f'''        </table></div>
        <div class="pager"><span class="hint">1-12 of 1,860 · 2 hidden: schema 5 needs a newer hotel</span><span><a href="#market">Next</a> &gt;&gt;</span></div>
      </div></div><div class="col">
      <div class="blk box dense"><h2>Make your own</h2>
        <p>Draw in Aseprite, edit the data here and upload it as an OpenHotel file.</p>
        <p><a class="btn main" href="#create">Create an asset</a> <a class="btn" href="#link">Link app</a></p></div>
      <div class="blk box dense"><h2>Your creations (4)</h2>
        <dl class="kv"><div><dt>Telephone booth</dt><dd><span class="badge on">Live</span></dd></div><div><dt>Neon sign</dt><dd><span class="badge on">Live</span></dd></div><div><dt>Palm tree</dt><dd><span class="badge">In review</span></dd></div><div><dt>Beach towel</dt><dd><span class="badge">Draft</span></dd></div></dl>
        <p><a href="#mine">See them all</a> &gt;&gt;</p></div>
      <div class="blk box dense"><h2>{HOTEL}</h2>
        <p class="hint">Runs v{HV}: schemas 1 to {MAXS}.</p>
        <p><a href="#library">Hotel catalog</a> &gt;&gt; <b>2 updates</b></p></div>
      </div></div>
'''

# ---------- Item page ----------
cmts = comments(True)
VERS = [  # key, version, date, revision, schema, changes, sheet, size, in my catalog
 ("v12", "1.2", "21 Nov 2026", "01JD3QZ8M0K4V7R2XW9H5T6BNC", 3, "Opening animation is smoother.", "96 × 196 · 9 frames", "14 KB", False),
 ("v11", "1.1", "02 Nov 2026", "01JBX7H2P9Q4M6T1ZR8C3D5EVA", 3, "Fixes the west side.", "96 × 196 · 8 frames", "13 KB", True),
 ("v10", "1.0", "12 Aug 2026", "01J4Q9K2W7B3N8Y5T1V6X0RMDE", 2, "First version.", "48 × 98 · 4 frames", "6 KB", False),
 ("v20", "2.0", "Preview", "01JE0A5C7D9F2H4J6K8M1N3PQR", 5, "New schema with sound.", "96 × 196 · 14 frames", "22 KB", False),
]
def vpanel(k, v, d, rev, sc, ch, sheet, size, inc):
    act = INCAT if inc else ('<a class="btn main" href="#library">Use this version in my catalog</a>' if sc <= MAXS else f'<span class="hint">{HOTEL} runs schemas up to {MAXS}</span>')
    return (f'<div class="st st-{k}">' + kv([("Version", f"<b>{v}</b>"), ("Released", d), ("Revision", f"<code>{rev}</code>"), ("Schema", sch(sc)), ("Changes", ch),
            ("Type", "furniture"), ("Size (w × d × h)", "1 × 1 × 2"), ("Icon texture", "telephone-icon"), ("Languages", "English, Español"), ("Sprite sheet", f"png · {sheet}"), ("File", size)])
            + tbl(["Action", "States", "Default"], [["door", "closed, open", "closed"]])
            + tbl(["Direction", "Textures", "zIndex", "Pivot"], [["north", "2", "0, 1", "24, 98"], ["east", "2", "0, 1", "24, 98"]])
            + f'<p>{act}</p></div>')
def hrow(k, v, d, rev, sc, ch, sheet, size, inc):
    a = INCAT if inc else ('<a class="btn" href="#library">Use this one</a>' if sc <= MAXS else '<span class="hint">not supported</span>')
    return f'<tr><td><b>{v}</b></td><td>{d}</td><td>{sch(sc)}</td><td>{ch}</td><td class="ra">{a}</td></tr>\n'
item = f'''      <div class="blk box">
        <p class="crumb"><a href="#market">Marketplace</a> &gt; Furniture &gt; Telephone booth</p>
        <div class="ihead"><div class="ipv">{img("furni-telephone", 48, 98, "Telephone booth")}</div>
          <div><h2>Telephone booth</h2>
            <p class="hint">by <a href="#">OpenHotel</a> · Furniture · id <code>teleports@telephone</code> · used by 1,204 hotels</p>
            <p>Step in, wait for the light and come out in another booth. Link it to any other booth you own.</p></div></div>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense vp" data-state="v12">
        <h2>Versions</h2>
        <p class="hint">Pick a version to see its data. The version counts the changes of the item; the schema says which hotels can run it.</p>
        <div class="ktabs">''' + "".join(f'<button class="btn{" main" if v[0] == "v12" else ""}" type="button" data-go="{v[0]}">{v[1]}</button>' for v in VERS) + '''</div>
''' + "".join(vpanel(*v) for v in VERS) + '''
      </div>
      <div class="blk box dense">
        <h2>History</h2>
        <div class="tbl"><table><tr><th>Version</th><th>Date</th><th>Schema</th><th>Changes</th><th></th></tr>
''' + "".join(hrow(*v) for v in VERS) + '''        </table></div>
        <p class="hint">Any version with a schema your hotel runs can go in your catalog, old ones too.</p>
      </div>
''' + cmts + f'''      </div><div class="col">
      <div class="blk box dense"><h2>In {HOTEL}</h2>
        {kv([("In catalog", "Teleports"), ("Version", "1.1 · <b>1.2 is out</b>"), ("Price", "25 SNP")])}
        <p><a class="btn main" href="#library">Open the catalog</a></p></div>
''' + inter.replace("4.2", "4.8").replace("86 votes", "1,102 votes").replace("1,204</b> views", "1,204</b> hotels") + '''      <div class="blk box dense">
        <h2>Information</h2>
        <dl class="kv"><div><dt>Published</dt><dd>12 Aug 2026</dd></div><div><dt>Last version</dt><dd>21 Nov 2026</dd></div><div><dt>Used by</dt><dd>1,204 hotels</dd></div><div><dt>Part of</dt><dd><a href="#collection">Beach set</a></dd></div><div><dt>Licence</dt><dd>CC BY-NC-SA 4.0</dd></div></dl>
        <p><a class="danger" href="#">Report</a></p>
      </div>
      </div></div>
<script>
document.querySelectorAll(".vp").forEach((box) => box.addEventListener("click", (e) => {
  const b = e.target.closest("[data-go]");
  if (b) { box.dataset.state = b.dataset.go; box.querySelectorAll(".ktabs .btn").forEach((x) => x.classList.toggle("main", x === b)); }
}));
</script>
'''

# ---------- Collection page ----------
NOT = '<span class="hint">not in catalog</span>'
CI = [("tel", "Beach hut", "1.0", 3), ("flag", "Beach flag", "1.1", 3), ("poster", "Surf poster", "1.0", 3), ("tel", "Shower", "1.2", 3), ("flag", "Palm tree", "1.0", 3), ("poster", "Towel", "1.0", 2)]
CV = [("1.3", "14 Nov 2026", 3, "Adds the shower.", True), ("1.2", "20 Oct 2026", 3, "Palm tree fixes.", False), ("1.0", "02 Sep 2026", 2, "First version.", False)]
def cvrow(v, d, s, c, l):
    a = '<span class="hint">latest</span>' if l else '<a class="btn" href="#library">Use this one</a>'
    return f'<tr><td><b>{v}</b></td><td>{d}</td><td>{sch(s)}</td><td>{c}</td><td class="ra">{a}</td></tr>\n'
collection = f'''      <div class="blk box">
        <p class="crumb"><a href="#market">Marketplace</a> &gt; Collections &gt; Beach set</p>
        <div class="ihead"><div class="ipv">{img("news-flag", 64, 64)}</div>
          <div><h2>Beach set</h2><p class="hint">by <a href="#">Mintleaf</a> · Collection · id <code>beach-set</code> · 12 furniture · used by 260 hotels</p>
            <p>Everything for a beach room: huts, palms, towels and a shower.</p>
            <p><a class="btn main" href="#library">Add all 12 to the catalog</a></p></div></div>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense"><h2>Furniture in version 1.3 (12)</h2>
        <div class="tbl"><table><tr><th></th><th>Name</th><th class="num">Version</th><th>Schema</th><th>{HOTEL}</th></tr>
''' + "".join(f'<tr><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a></td><td class="num">{v}</td><td>{sch(s)}</td><td>{INCAT if i == 1 else NOT}</td></tr>\n' for i, (t, n, v, s) in enumerate(CI)) + '''        </table></div>
        <div class="pager"><span class="hint">6 of 12</span><span><a href="#collection">More</a> &gt;&gt;</span></div></div>
      <div class="blk box dense"><h2>History</h2>
        <div class="tbl"><table><tr><th>Version</th><th>Date</th><th>Schema</th><th>Changes</th><th></th></tr>
''' + "".join(cvrow(*c) for c in CV) + '''        </table></div></div>
''' + cmts + '''      </div><div class="col">
''' + inter + '''      <div class="blk box dense"><h2>Collection data</h2>
        <dl class="kv"><div><dt>id</dt><dd>beach-set</dd></div><div><dt>category.label</dt><dd>Beach</dd></div><div><dt>category.description</dt><dd>Sun and sand</dd></div><div><dt>Schema</dt><dd>3</dd></div><div><dt>Published</dt><dd>02 Sep 2026</dd></div></dl></div>
      </div></div>
'''

# ---------- Your creations ----------
MINE = [("Furniture", "tel", "Telephone booth", "1.2", "Live", 3, "1,204", "4.8"), ("Furniture", "poster", "Neon sign", "1.0", "Live", 3, "58", "4.2"),
        ("Furniture", "flag", "Palm tree", "1.0", "In review", 3, "0", ""), ("Furniture", "poster", "Beach towel", "0.1", "Draft", 3, "0", "")]
def mine_row(k, t, n, v, s, sc, ho, r):
    b = '<span class="badge on">Live</span>' if s == "Live" else f'<span class="badge">{s}</span>'
    dele = f'<button class="btn" type="button" disabled title="Used by {ho} hotels">Delete</button>' if ho != "0" else '<button class="btn danger-btn" type="button">Delete</button>'
    return (f'<tr><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a><br><span class="hint">{k}</span></td><td>{b}</td><td class="num">{v}</td><td>{sch(sc)}</td>'
            f'<td class="num">{ho}</td><td class="num">{stars(r) if r else ""}</td><td class="ra"><a class="btn" href="#create">Edit</a> <a class="btn" href="#create">New version</a> <a class="btn" href="#">.furniture</a> {dele}</td></tr>\n')
mine = '''      <div class="blk box dense">
        <h2>Your creations</h2>
        <p class="hint">4 assets · 1,262 hotels use them · <a href="#create">Create an asset</a> · <a href="#link">Link app</a></p>
        <div class="tbl"><table><tr><th></th><th>Name</th><th>State</th><th class="num">Version</th><th>Schema</th><th class="num">Hotels</th><th class="num">Rating</th><th></th></tr>
''' + "".join(mine_row(*m) for m in MINE) + '''        </table></div>
        <p class="hint">Download is only for your own files. An asset or a version can be deleted only while no hotel uses it.</p>
      </div>
      <div class="blk box dense">
        <h2>Your collections</h2>
        <div class="tbl"><table><tr><th></th><th>Collection</th><th class="num">Items</th><th class="num">Version</th><th class="num">Hotels</th><th></th></tr>
          <tr><td>''' + tb("coll") + '''</td><td><a href="#collection"><b>Beach set</b></a></td><td class="num">12</td><td class="num">1.3</td><td class="num">260</td><td class="ra"><a class="btn" href="#mine">Edit</a> <a class="btn" href="#">.collection</a> <button class="btn" type="button" disabled title="Used by 260 hotels">Delete</button></td></tr>
        </table></div>
        <details class="disc newh"><summary class="btn main">Edit collection: Beach set</summary>
          <form class="form" onsubmit="event.preventDefault()">
            <label>id<input class="in" value="beach-set" disabled></label>
            <label>Category<input class="in" value="Beach"></label>
            <label>Description (optional)<input class="in" value="Sun and sand"></label>
            <fieldset class="vis"><legend>Items (tick to include)</legend>
''' + "".join(f'<label class="chk"><input type="checkbox"{" checked" if i < 4 else ""}> {n} <span class="hint">{v}</span></label>' for i, (t, n, v, s) in enumerate(CI)) + '''
            </fieldset>
            <div class="row"><button class="btn main" type="submit">Save as version 1.4</button></div>
          </form>
        </details>
      </div>
'''

# ---------- Create (an editor like asset-editor) ----------
def F(label, inner): return f'<label class="f">{label}{inner}</label>'
def I(v="", ph="", t="text", dis=False): return f'<input class="in" type="{t}" value="{v}" placeholder="{ph}"{" disabled" if dis else ""}>'
def S(opts, cur=None): return '<select class="in">' + "".join(f'<option{" selected" if o == cur else ""}>{o}</option>' for o in opts) + '</select>'
TEX = ["telephone-n", "telephone-n-top", "telephone-e", "telephone-icon"]
def tex_row(tx, z, px, py, x, zz, act):
    return ('<div class="fgrid tx">' + F("texture", S(TEX, tx)) + F("zIndex", I(z, t="number")) + F("pivot.x", I(px, t="number")) + F("pivot.y", I(py, t="number"))
            + F("position.x", I(x, t="number")) + F("position.z", I(zz, t="number")) + F("actions.door", S(["-", "closed", "open"], act)) + '<button class="btn" type="button" aria-label="Remove texture">x</button></div>')
def direction(d, rows, op=False):
    return f'<details class="disc dir"{" open" if op else ""}><summary class="btn">{d} ({len(rows)})</summary>' + "".join(tex_row(*r) for r in rows) + '<button class="btn" type="button">Add texture</button></details>'
create = f'''      <div class="blk box dense">
        <h2>Create an asset</h2>
        <ol class="stepbar"><li class="on">1 Load</li><li class="on">2 Edit</li><li>3 Send</li></ol>
        <div class="row" role="group" aria-label="Kind"><span class="btn main">Furniture</span> <span class="btn">Collection</span> <span class="btn" aria-disabled="true" title="Not in the editor yet">Public room · soon</span> <span class="btn" aria-disabled="true" title="Not in the editor yet">Clothes · soon</span></div>
        <form class="form" onsubmit="event.preventDefault()"><label>Load a file<input class="in" type="file" accept=".furniture,.collection,.oha"></label>
          <span class="hint">Only OpenHotel files (.furniture, .collection) can be uploaded. Or fill the form from an Aseprite export: <a href="#link">Link app</a>.</span></form>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense">
        <h2>Data</h2>
        <form class="ed2" onsubmit="event.preventDefault()">
          <div class="fgrid">{F("id", I("teleports@telephone"))}{F("revision", I("01JD3QZ8M0K4V7R2XW9H5T6BNC", dis=True))}{F("type", S(["furniture", "frame"], "furniture"))}</div>
          <div class="fgrid">{F("size.width", I("1", t="number"))}{F("size.depth", I("1", t="number"))}{F("size.height", I("2", t="number"))}{F("icon.texture", S(TEX, "telephone-icon"))}</div>
          <h3>Actions</h3>
          <div class="fgrid">{F("id", I("door"))}{F("label", I("Door"))}{F("states (comma separated)", I("closed, open"))}{F("defaultState", I("closed"))}<button class="btn" type="button" aria-label="Remove action">x</button></div>
          <button class="btn" type="button">Add action</button>
          <h3>Lang</h3>
          <div class="fgrid lg">{F("language", S(["English", "Español", "Deutsch"], "English"))}{F("name", I("Telephone booth"))}{F("description", I("Dial a friend"))}<button class="btn" type="button" aria-label="Remove language">x</button></div>
          <div class="fgrid lg">{F("language", S(["English", "Español", "Deutsch"], "Español"))}{F("name", I("Cabina"))}{F("description", I("Llama a un amigo"))}<button class="btn" type="button" aria-label="Remove language">x</button></div>
          <button class="btn" type="button">Add language</button>
          <h3>Directions</h3>
          {direction("north", [("telephone-n", 0, 24, 98, 0, 0, "closed"), ("telephone-n-top", 1, 24, 98, 0, 0, "open")], True)}
          {direction("east", [("telephone-e", 0, 24, 98, 0, 0, "closed")], True)}
          {direction("south", [])}{direction("west", [])}
        </form>
      </div>
      </div><div class="col">
      <div class="blk box dense"><h2>Preview</h2>
        <div class="ipv">{img("furni-telephone", 48, 98, "Preview, north")}</div>
        {kv([("Sprite sheet", "png · 96 × 196 · scale 1"), ("Frames", "9"), ("Animations", "2"), ("Schema", sch(3) + " <span class=\"hint\">set by the editor</span>")])}
      </div>
      <div class="blk box dense"><h2>Checks</h2><ul class="perms"><li>Revision is valid</li><li>Name and description in English</li><li>Icon texture exists in the sheet</li><li>2 of 4 directions have textures</li><li>No frame is outside the image</li></ul>
        <p><button class="btn main" type="button">Send for review</button> <button class="btn" type="button">Save draft</button></p>
        <p class="hint">Once live, an asset can't be deleted while a hotel uses it. Send a new version instead.</p></div>
      </div></div>
'''

# ---------- Hotel catalog (owner) ----------
CATS = [("Alpha", "Enabled", 5), ("Flags", "Enabled", 14), ("Teleports", "Enabled", 3), ("Summer", "Scheduled", 12), ("Pirate week", "Off", 8)]
BADGE = {"Enabled": '<span class="badge on">Enabled</span>', "Scheduled": '<span class="badge">Scheduled</span>', "Off": '<span class="badge">Off</span>'}
def catrow(n, st, c, sel):
    return f'<li{" class=sel" if sel else ""}><a href="#library">{n}</a> {BADGE[st]}<span class="hint">{c}</span></li>'
def furow(t, n, fid, cur, latest, price):
    vs = [latest, "1.0"] if cur == latest else [latest, cur]
    opts = "".join(f'<option{" selected" if v == cur else ""}>{v}{" (latest)" if v == latest else ""}</option>' for v in vs)
    upd = '' if cur == latest else ' <span class="badge">Update</span>'
    return (f'<tr><td>{tb(t)}</td><td><b>{n}</b>{upd}<br><span class="hint">{fid}</span></td><td><select class="in sel-s" aria-label="Version">{opts}</select></td><td>{sch(3)}</td>'
            f'<td class="num"><input class="in price" type="number" value="{price}" min="0" aria-label="Price in SNP"></td><td class="ra"><button class="btn" type="button" aria-label="Remove">x</button></td></tr>\n')
library = f'''      <div class="split3"><div class="col">
      <div class="blk box dense">
        <h2>Hotel catalog · {HOTEL}</h2>
        <p class="hint">The catalog guests see in the hotel, edited from the web. {HOTEL} runs v{HV}: schemas 1 to {MAXS}. Prices are in SNP.</p>
        <form class="form" onsubmit="event.preventDefault()">
          <div class="fgrid">{F("Category", I("Teleports"))}{F("Description", I("Step in, come out somewhere else."))}</div>
          <div class="fgrid">{F("Available from", I("", t="date"))}{F("Available until", I("", t="date"))}<label class="chk"><input type="checkbox" checked> Enabled</label></div>
          <div class="row"><button class="btn main" type="submit">Save category</button></div>
        </form>
        <div class="tbl"><table><tr><th></th><th>Furniture</th><th>Version</th><th>Schema</th><th class="num">Price</th><th></th></tr>
''' + furow("tel", "Telephone booth", "teleports@telephone", "1.1", "1.2", 25) + furow("tel", "Red booth", "teleports@red-booth", "1.0", "1.0", 25) + furow("flag", "Door sign", "teleports@door-sign", "1.0", "1.0", 5) + '''        </table></div>
        <p><a class="btn main" href="#market">Add furniture from the marketplace</a> <a class="btn" href="#collection">Add a collection</a></p>
      </div>
      </div><div class="col">
      <div class="blk box dense"><h2>Categories (9)</h2>
        <ul class="cats">''' + "".join(catrow(n, st, c, n == "Teleports") for n, st, c in CATS) + '''</ul>
        <p><button class="btn" type="button">New category</button></p></div>
      <div class="blk box dense"><h2>Updates (2)</h2>
        <dl class="kv"><div><dt>Telephone booth</dt><dd>1.1 to 1.2</dd></div><div><dt>Rooftop Pool</dt><dd>2.0 to 2.1</dd></div></dl>
        <p><button class="btn main" type="button">Update both</button></p></div>
      <div class="blk box dense"><h2>Public rooms (3)</h2>
        <div class="tbl"><table><tr><td>The Atrium</td><td class="num">1.2</td><td><span class="badge on">Open</span></td></tr><tr><td>Rooftop Pool</td><td class="num">2.0</td><td><span class="badge on">Open</span></td></tr><tr><td>Disco Hall</td><td class="num">1.0</td><td><span class="badge">Closed</span></td></tr></table></div>
        <p class="hint">The Atrium is the first room.</p></div>
      <div class="blk box dense"><h2>Clothes (64)</h2><p class="hint">Striped shirt, Red jacket and 62 more. <a href="#library">Manage</a></p></div>
      </div></div>
'''
