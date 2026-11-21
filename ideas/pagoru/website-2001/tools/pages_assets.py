# Marketplace, item, collection, creations, create, catalog, link. Exec'd by subpages.py after pages_social.py.
def img(f, w, h, alt=""): return f'<img src="assets/oh/{f}.png" width="{w}" height="{h}" alt="{alt}">'
def ct(f, w, h): return f'<div class="ct">{img(f, w, h)}</div>'
HOTEL = "OpenHotel"; HV = "0.156.0"; MAXS = 4  # the hotel version runs schemas 1 to MAXS
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
def author(by): return f'<a href="#">{by}</a>' + (' <span class="badge on" title="Comes with the OpenHotel default catalog">Official</span>' if by == "OpenHotel" else "")
def mrow(k, t, n, by, v, sc, ho, r, mine):
    link = "#collection" if k == "Collection" else "#item"
    note = (f'{mine}' + (' <b>update</b>' if mine != v else '')) if mine else '<span class="hint">-</span>'
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="{link}"><b>{n}</b></a><br><span class="hint">{k} · {author(by)}</span></td>'
            f'<td class="num">{v}</td><td class="c"><span class="badge{" on" if sc <= MAXS else ""}" title="Schema {sc}">{sc}</span></td><td class="num">{note}</td><td class="num">{ho}</td><td class="num">{stars(r)}</td></tr>\n')
market = f'''      <div class="split3 narrow"><div class="col">
      <div class="blk box dense">
        <h2>Marketplace</h2>
        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search" aria-label="Search">
          <select class="in" aria-label="Kind"><option>Everything</option><option>Public rooms</option><option>Furniture</option><option>Clothes</option><option>Collections</option></select>
          <select class="in" aria-label="Sort"><option>Most used</option><option>Newest</option><option>Best rated</option></select>
          <select class="in" aria-label="Author"><option>Everyone</option><option>Official (OpenHotel)</option><option>My creations</option></select>
          <label class="chk"><input type="checkbox" checked> Only schemas {HOTEL} runs (1 to {MAXS})</label></form>
        <div class="tbl"><table><tr><th></th><th>Name</th><th class="num">Version</th><th class="c" title="The data shape. Your hotel runs schemas 1 to 4">Schema</th><th class="num" title="The version in your hotel catalog">In catalog</th><th class="num" title="Hotels that use it">Used by</th><th class="num">Rating</th></tr>
''' + "".join(mrow(*i) for i in ITEMS) + f'''        </table></div>
        <p class="hint">Used by: hotels that have it. In catalog: the version in your catalog. Official: comes with the OpenHotel default catalog.</p>
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
            <p class="hint">by <a href="#">OpenHotel</a> <span class="badge on">Official</span> · Furniture · id <code>teleports@telephone</code> · used by 1,204 hotels</p><p class="hint">Comes with the OpenHotel default catalog.</p>
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
        {kv([("In catalog", "Teleports"), ("Version", "1.1 · <b>1.2 is out</b>"), ("Price", "25 OHC")])}
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
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a><br><span class="hint">{k}</span></td><td>{b}</td><td class="num">{v}</td><td>{sch(sc)}</td>'
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

# ---------- Create: spritesheet first, then forms for each kind ----------
def F(label, inner): return f'<label class="f">{label}{inner}</label>'
def I(v="", ph="", t="text", dis=False): return f'<input class="in" type="{t}" value="{v}" placeholder="{ph}"{" disabled" if dis else ""}>'
def S(opts, cur=None): return '<select class="in">' + "".join(f'<option{" selected" if o == cur else ""}>{o}</option>' for o in opts) + '</select>'
FRAMES = [("telephone-n", 0, 0, 48, 98, 24, 98), ("telephone-n-top", 48, 0, 48, 98, 24, 98), ("telephone-e", 0, 98, 48, 98, 24, 98), ("telephone-icon", 48, 98, 24, 50, 12, 50)]
TEX = [f[0] for f in FRAMES]
def frow(n, x, y, w, h, ax, ay):
    return ('<div class="fgrid fr">' + F("frame", I(n)) + F("x", I(x, t="number")) + F("y", I(y, t="number")) + F("w", I(w, t="number")) + F("h", I(h, t="number"))
            + F("anchor.x", I(ax, t="number")) + F("anchor.y", I(ay, t="number")) + '<button class="btn" type="button" aria-label="Remove frame">x</button></div>')
LG = lambda lang, n, d: f'<div class="fgrid lg">{F("language", S(["English", "Español", "Deutsch"], lang))}{F("name", I(n))}{F("description", I(d))}<button class="btn" type="button" aria-label="Remove language">x</button></div>'
LANGS = LG("English", "Telephone booth", "Dial a friend") + LG("Español", "Cabina", "Llama a un amigo") + '<button class="btn" type="button">Add language</button>'
def tex_row(tx, z, px, py, x, zz, act):
    return ('<div class="fgrid tx">' + F("texture", S(TEX, tx)) + F("zIndex", I(z, t="number")) + F("pivot.x", I(px, t="number")) + F("pivot.y", I(py, t="number"))
            + F("position.x", I(x, t="number")) + F("position.z", I(zz, t="number")) + F("actions.door", S(["-", "closed", "open"], act)) + '<button class="btn" type="button" aria-label="Remove texture">x</button></div>')
def direction(d, rows, op=False):
    return f'<details class="disc dir"{" open" if op else ""}><summary class="btn">{d} ({len(rows)})</summary>' + "".join(tex_row(*r) for r in rows) + '<button class="btn" type="button">Add texture</button></details>'
st_furn = (f'<div class="fgrid">{F("id", I("teleports@telephone"))}{F("revision", I("01JD3QZ8M0K4V7R2XW9H5T6BNC", dis=True))}{F("type", S(["furniture", "frame"], "furniture"))}</div>'
  f'<div class="fgrid">{F("size.width", I("1", t="number"))}{F("size.depth", I("1", t="number"))}{F("size.height", I("2", t="number"))}{F("icon.texture", S(TEX, "telephone-icon"))}</div>'
  f'<h3>Actions</h3><div class="fgrid">{F("id", I("door"))}{F("label", I("Door"))}{F("states (comma separated)", I("closed, open"))}{F("defaultState", I("closed"))}<button class="btn" type="button" aria-label="Remove action">x</button></div><button class="btn" type="button">Add action</button>'
  f'<h3>Lang</h3>{LANGS}<h3>Directions</h3>'
  + direction("north", [("telephone-n", 0, 24, 98, 0, 0, "closed"), ("telephone-n-top", 1, 24, 98, 0, 0, "open")], True) + direction("east", [("telephone-e", 0, 24, 98, 0, 0, "closed")], True) + direction("south", []) + direction("west", []))
st_room = (f'<div class="fgrid">{F("id", I("rooftop-pool"))}{F("revision", I("01JD3QZ8M0K4V7R2XW9H5T6BNC", dis=True))}{F("max users", I("40", t="number"))}</div>'
  f'<div class="fgrid">{F("size.width", I("12", t="number"))}{F("size.depth", I("9", t="number"))}{F("wall height", I("3", t="number"))}</div>'
  f'<div class="fgrid">{F("floor texture", S(TEX, "telephone-n"))}{F("wall texture", S(TEX, "telephone-e"))}</div>'
  f'<h3>Door and spawn</h3><div class="fgrid">{F("door.x", I("0", t="number"))}{F("door.z", I("4", t="number"))}{F("door.direction", S(["north", "east", "south", "west"], "east"))}{F("spawn.x", I("1", t="number"))}{F("spawn.z", I("4", t="number"))}</div>'
  f'<h3>Lang</h3>{LANGS}<h3>Furniture placed</h3><div class="fgrid">{F("furniture", I("teleports@telephone"))}{F("x", I("0", t="number"))}{F("z", I("0", t="number"))}{F("direction", S(["north", "east", "south", "west"], "east"))}<button class="btn" type="button" aria-label="Remove">x</button></div><button class="btn" type="button">Add furniture</button>'
  '<p class="hint">Room fields are a proposal; the room format is not final.</p>')
st_cloth = (f'<div class="fgrid">{F("id", I("striped-shirt"))}{F("revision", I("01JD3QZ8M0K4V7R2XW9H5T6BNC", dis=True))}{F("slot", S(["hat", "hair", "top", "legs", "shoes", "accessory"], "top"))}</div>'
  '<label class="chk"><input type="checkbox"> Takes the skin colour of the guest</label> <label class="chk"><input type="checkbox" checked> Guests can recolour it</label>'
  f'<h3>Lang</h3>{LANGS}<h3>Frames</h3>'
  + "".join(f'<div class="fgrid">{F("direction", S(["north", "east", "south", "west"], d))}{F("action", S(["idle", "walk", "wave"], a))}{F("frames", I(fr))}<button class="btn" type="button" aria-label="Remove">x</button></div>' for d, a, fr in [("north", "idle", "telephone-n"), ("east", "idle", "telephone-e")])
  + '<button class="btn" type="button">Add frames</button><p class="hint">Clothes fields are a proposal; the clothes format is not final.</p>')
create = f'''<div class="kb" data-state="furn">
      <div class="blk box dense">
        <h2>Create an asset</h2>
        <ol class="stepbar"><li class="on">1 Spritesheet</li><li class="on">2 Details</li><li>3 Send</li></ol>
        <p class="hint">Every asset starts from a spritesheet image. Pick it (or sync it from Aseprite), cut the frames, then fill the details of the furniture, room or clothes with the forms.</p>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense">
        <h2>1 · Spritesheet</h2>
        <form class="form" onsubmit="event.preventDefault()"><label>Image<input class="in" type="file" accept="image/png"></label><span class="hint">PNG only. The only file you upload.</span></form>
        {kv([("Image", "telephone.png"), ("Size", "96 × 196"), ("Scale", "1"), ("Format", "png")])}
        <div class="sheet"><img src="assets/oh/furni-telephone.png" width="48" height="98" alt="Spritesheet"><i style="left:0;top:0;width:48px;height:98px"></i></div>
        <h3>Frames (4)</h3>
        {"".join(frow(*f) for f in FRAMES)}<button class="btn" type="button">Add frame</button>
        <h3>Animations</h3>
        <div class="fgrid">{F("animation", I("door-open"))}{F("frames (comma separated)", I("telephone-n, telephone-n-top"))}<button class="btn" type="button" aria-label="Remove animation">x</button></div><button class="btn" type="button">Add animation</button>
      </div>
      <div class="blk box dense">
        <h2>2 · Details</h2>
        <div class="row" role="group" aria-label="Kind"><button class="btn main" type="button" data-go="furn">Furniture</button> <button class="btn" type="button" data-go="room">Public room</button> <button class="btn" type="button" data-go="cloth">Clothes</button></div>
        <form class="ed2" onsubmit="event.preventDefault()">
          <div class="st st-furn">{st_furn}</div><div class="st st-room">{st_room}</div><div class="st st-cloth">{st_cloth}</div>
        </form>
      </div>
      <div class="blk box dense">
        <h2>3 · Send</h2>
        <ul class="perms"><li>Spritesheet is a valid PNG</li><li>Every frame is inside the image</li><li>Name and description in English</li><li>Icon frame exists</li><li>2 of 4 directions have textures</li></ul>
        <p><button class="btn main" type="button">Send for review</button> <button class="btn" type="button">Save draft</button></p>
        <p class="hint">Schema {sch(3)} is set by the editor. Once live, an asset can't be deleted while a hotel uses it; send a new version instead.</p>
      </div>
      </div><div class="col">
      <div class="blk box dense"><h2>Aseprite</h2>
        <p><span class="badge on">Linked</span> Aseprite on PC · seen 2 min ago</p>
        <p><button class="btn main" type="button">Sync from Aseprite</button></p>
        <p class="hint">Reads the sprite open in Aseprite: image, frames and tags. Not linked yet? <a href="#link">Get the Link app</a>.</p></div>
      <div class="blk box dense"><h2>Preview</h2>
        <div class="ipv">{img("furni-telephone", 48, 98, "Preview, north")}</div>
        {kv([("Frame", "telephone-n"), ("Position", "0, 0"), ("Size", "48 × 98")])}</div>
      </div></div>
</div>
<script>
document.querySelectorAll(".kb").forEach((box) => box.addEventListener("click", (e) => {{
  const b = e.target.closest("[data-go]");
  if (b) {{ box.dataset.state = b.dataset.go; box.querySelectorAll(".row .btn").forEach((x) => x.classList.toggle("main", x === b)); }}
}}));
</script>
'''
