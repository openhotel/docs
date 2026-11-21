# Creator area: sub nav and the Your creations pages. Exec'd at the end of pages_admin.py.
CREATE_NAV = [("create", "Create"), ("create-sheet", "Spritesheet"), ("create-furniture", "Furniture"), ("create-clothes", "Clothes"), ("create-room", "Room"), ("mine-collections", "Collections"), ("link", "Link app")]
CN = lambda cur: subnav(CREATE_NAV, cur, "Create")
ALL = [("Furniture", "tel", "Telephone booth", "1.2", "Live", 3, "1,204", "4.8"), ("Furniture", "poster", "Neon sign", "1.0", "Live", 3, "58", "4.2"),
       ("Furniture", "flag", "Palm tree", "1.0", "In review", 3, "0", ""), ("Furniture", "poster", "Beach towel", "0.1", "Draft", 3, "0", ""),
       ("Clothes", "c", "Striped shirt", "1.0", "Live", 1, "980", "4.5"), ("Clothes", "b", "Red jacket", "1.0", "Live", 1, "410", "4.1"),
       ("Room", "pool", "Rooftop pool", "2.0", "Live", 2, "37", "4.7")]
EXT = {"Furniture": ".furniture", "Clothes": ".clothes", "Room": ".room"}
def arow(m):
    k, t, n, v, s, sc, ho, r = m
    b = '<span class="badge on">Live</span>' if s == "Live" else f'<span class="badge">{s}</span>'
    dele = f'<button class="btn" type="button" disabled title="Used by {ho} hotels">Delete</button>' if ho != "0" else '<button class="btn danger-btn" type="button">Delete</button>'
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a><br><span class="hint">{k}</span></td><td>{b}</td><td class="num">{v}</td><td>{sch(sc)}</td>'
            f'<td class="num">{ho}</td><td class="num">{stars(r) if r else ""}</td><td class="ra"><a class="btn" href="#create">Edit</a> <a class="btn" href="#create">New version</a> <a class="btn" href="#">{EXT[k]}</a> {dele}</td></tr>\n')
def alist(title, rows, note):
    return box(title, f'        <p class="hint">{len(rows)} assets · {note}</p>\n        <div class="tbl"><table><tr><th></th><th>Name</th><th>State</th><th class="num">Version</th><th>Schema</th><th class="num">Hotels</th><th class="num">Rating</th><th></th></tr>\n'
               + "".join(arow(m) for m in rows) + '        </table></div>\n        <p class="hint">Download is only for your own files. An asset or a version can be deleted only while no hotel uses it.</p>')
NOTE = '<a href="#create">Create an asset</a>'
NOTE0 = 'start a new one below'
_old = mine
mine_collections = CN("mine-collections") + _old[_old.index('      <div class="blk box dense">\n        <h2>Your collections</h2>'):]
SHEETS = [("tel", "telephone.png", "256 x 128", 12, 2, "Telephone booth", "21 Nov"), ("poster", "neon-sign.png", "128 x 64", 4, 1, "Neon sign", "14 Nov"),
          ("flag", "palm-tree.png", "192 x 192", 6, 0, "Palm tree", "12 Nov"), ("c", "shirts.png", "256 x 256", 16, 0, "Striped shirt, Red jacket", "03 Nov"), ("pool", "rooftop.png", "512 x 384", 3, 0, "Rooftop pool", "28 Oct")]
def srow(t, f, sz, fr, an, used, d):
    dele = '<button class="btn" type="button" disabled title="Used by an asset">Delete</button>' if used else '<button class="btn danger-btn" type="button">Delete</button>'
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="#create"><b>{f}</b></a><br><span class="hint">{sz} px · uploaded {d}</span></td><td class="num">{fr}</td><td class="num">{an}</td><td>{ "Not used yet" if not used else used}</td>'
            f'<td class="ra"><a class="btn main" href="#create">New asset from it</a> <a class="btn" href="#">Download</a> {dele}</td></tr>\n')
mine_sheets = box("Your spritesheets", '''        <p class="hint">PNG files you uploaded. Every asset starts from one. You can reuse a sheet in several assets. <a href="#link">Send from Aseprite</a></p>
        <div class="tbl"><table><tr><th></th><th>File</th><th class="num">Frames</th><th class="num">Animations</th><th>Used by</th><th></th></tr>
''' + "".join(srow(t, f, sz, fr, an, u if (u != "Palm tree") else "", d) for t, f, sz, fr, an, u, d in SHEETS) + '''        </table></div>
        <p class="hint">A sheet can be deleted only when no asset uses it.</p>''')

GUIDE = [("1", "Draw", "Draw your art in Aseprite, or any editor, and save it as one PNG spritesheet. All the frames of the asset go in that one image. Only your own art, shared under CC BY-NC-SA 4.0.", "You need: a PNG file or Aseprite with the Link app.", "create-sheet", "Spritesheet"),
         ("2", "Cut", "Upload the PNG. Mark each frame (x, y, width, height and anchor) and group frames into animations. The preview shows each frame at its real size.", "You need: the PNG from step 1.", "create-sheet", "Spritesheet"),
         ("3", "Describe", "Pick what the sheet is and fill its form. Names and descriptions need English; other languages are optional.", "You need: a name, an id and the details of the kind (below).", "create-furniture", "Furniture"),
         ("4", "Send", "The editor checks the sheet and the form. Staff review the asset, then it goes Live in the marketplace. Hotel owners add it to their catalog, you never add it yourself.", "You need: nothing else. You get a message when it is reviewed. Each step page lists what you already made.", "create-furniture", "Furniture")]
KINDS = [("Furniture", "id, size (width, depth, height), icon frame, actions and states, textures for each direction, name and description.", "create-furniture"),
         ("Clothes", "id, slot (hat, hair, top, legs, shoes, accessory), skin colour and recolour options, frames for each direction and action.", "create-clothes"),
         ("Room", "id, size, wall height, floor and wall textures, door and spawn, furniture placed, max users.", "create-room")]
create = CN("create") + box("Create an asset", '        <p>Every asset is made in four steps. Anyone can create. Only a hotel owner can add an asset to a hotel.</p>' + "".join(
    f'        <div class="gstep"><b class="gn">{n}</b><div><h3>{t}</h3><p>{d}</p><p class="hint">{need}</p><p><a class="btn main" href="#{k}">{lab} &gt;&gt;</a></p></div></div>\n' for n, t, d, need, k, lab in GUIDE)) + box("What each kind needs", TBL(
    ["Kind", "Fields", ""], [[f"<b>{k}</b>", f, f'<a class="btn" href="#{h}">Open</a>'] for k, f, h in KINDS]) + '<p class="hint">Furniture follows the asset-editor format. Clothes and rooms are proposals and will change.</p>')

def rcol(sheet=True):
    return ('<div class="blk box dense"><h2>Spritesheet</h2><p><b>telephone.png</b> · 96 × 196 px · 4 frames</p>'
            '<p><a class="btn" href="#create-sheet">Change</a> </p></div>'
            '<div class="blk box dense"><h2>Preview</h2><div class="ipv">' + img("furni-telephone", 48, 98, "Preview, north") + '</div>' + kv([("Frame", "telephone-n"), ("Position", "0, 0"), ("Size", "48 × 98")]) + '</div>')
def cform(title, form, checks):
    return ('<div class="two wide2"><div>' + box(title, '        <form class="ed2" onsubmit="event.preventDefault()">' + form + '</form>')
      + box("Send", f'        <ul class="perms">{checks}</ul><p><button class="btn main" type="button">Send for review</button> <button class="btn" type="button">Save draft</button></p><p class="hint">Schema {sch(3)} is set by the editor. Once live, an asset can\'t be deleted while a hotel uses it; send a new version instead.</p>')
      + '</div><div>' + rcol() + '</div></div>')
create_furniture = CN("create-furniture") + alist("Your furniture", [m for m in ALL if m[0] == "Furniture"], NOTE0) + cform("Furniture details", st_furn, "<li>Spritesheet is a valid PNG</li><li>Every frame is inside the image</li><li>Name and description in English</li><li>Icon frame exists</li><li>2 of 4 directions have textures</li>")
create_clothes = CN("create-clothes") + alist("Your clothes", [m for m in ALL if m[0] == "Clothes"], NOTE0) + cform("Clothes details", st_cloth, "<li>Spritesheet is a valid PNG</li><li>Name and description in English</li><li>Every direction has frames</li>")
create_room = CN("create-room") + alist("Your rooms", [m for m in ALL if m[0] == "Room"], NOTE0) + cform("Room details", st_room, "<li>Spritesheet is a valid PNG</li><li>Name and description in English</li><li>Door is inside the room</li>")
create_sheet = (CN("create-sheet") + mine_sheets + '<div class="two wide2"><div>' + box("Spritesheet", '''        <form class="form" onsubmit="event.preventDefault()"><label>Image<input class="in" type="file" accept="image/png"></label><span class="hint">PNG only. The only file you upload.</span></form>''' + kv([("Image", "telephone.png"), ("Size", "96 × 196"), ("Scale", "1"), ("Format", "png")])
    + '<div class="sheet"><img src="assets/oh/furni-telephone.png" width="48" height="98" alt="Spritesheet"><i style="left:0;top:0;width:48px;height:98px"></i></div><h3>Frames (4)</h3>' + "".join(frow(*f) for f in FRAMES) + '<button class="btn" type="button">Add frame</button><h3>Animations</h3>'
    + f'<div class="fgrid">{F("animation", I("door-open"))}{F("frames (comma separated)", I("telephone-n, telephone-n-top"))}<button class="btn" type="button" aria-label="Remove animation">x</button></div><button class="btn" type="button">Add animation</button>'
    + '<p><a class="btn main" href="#create-furniture">Next: Furniture &gt;&gt;</a> <a class="btn" href="#create-clothes">Clothes</a> <a class="btn" href="#create-room">Room</a></p>') + '</div><div>'
    + box("Aseprite", '''        <p><span class="badge on">Linked</span> Aseprite on PC · seen 2 min ago</p><p><button class="btn main" type="button">Sync from Aseprite</button></p><p class="hint">Reads the sprite open in Aseprite: image, frames and tags. Not linked yet? <a href="#link">Get the Link app</a>.</p>''')
    + box("Preview", '<div class="ipv">' + img("furni-telephone", 48, 98, "Preview, north") + '</div>' + kv([("Frame", "telephone-n"), ("Position", "0, 0"), ("Size", "48 × 98")])) + '</div></div>')
