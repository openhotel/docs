# Creator area: sub nav and the Your creations pages. Exec'd at the end of pages_admin.py.
CREATE_NAV = [("create", "Create"), ("mine", "Your creations"), ("mine-sheets", "Spritesheets"), ("mine-furniture", "Furniture"), ("mine-clothes", "Clothes"), ("mine-rooms", "Rooms"), ("mine-collections", "Collections"), ("link", "Link app")]
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
_old = mine
mine_collections = CN("mine-collections") + _old[_old.index('      <div class="blk box dense">\n        <h2>Your collections</h2>'):]
mine = CN("mine") + alist("Your creations", ALL, f"1,262 hotels use them · {NOTE}")
mine_furniture = CN("mine-furniture") + alist("Your furniture", [m for m in ALL if m[0] == "Furniture"], NOTE)
mine_clothes = CN("mine-clothes") + alist("Your clothes", [m for m in ALL if m[0] == "Clothes"], NOTE)
mine_rooms = CN("mine-rooms") + alist("Your rooms", [m for m in ALL if m[0] == "Room"], NOTE)
SHEETS = [("tel", "telephone.png", "256 x 128", 12, 2, "Telephone booth", "21 Nov"), ("poster", "neon-sign.png", "128 x 64", 4, 1, "Neon sign", "14 Nov"),
          ("flag", "palm-tree.png", "192 x 192", 6, 0, "Palm tree", "12 Nov"), ("c", "shirts.png", "256 x 256", 16, 0, "Striped shirt, Red jacket", "03 Nov"), ("pool", "rooftop.png", "512 x 384", 3, 0, "Rooftop pool", "28 Oct")]
def srow(t, f, sz, fr, an, used, d):
    dele = '<button class="btn" type="button" disabled title="Used by an asset">Delete</button>' if used else '<button class="btn danger-btn" type="button">Delete</button>'
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="#create"><b>{f}</b></a><br><span class="hint">{sz} px · uploaded {d}</span></td><td class="num">{fr}</td><td class="num">{an}</td><td>{ "Not used yet" if not used else used}</td>'
            f'<td class="ra"><a class="btn main" href="#create">New asset from it</a> <a class="btn" href="#">Download</a> {dele}</td></tr>\n')
mine_sheets = CN("mine-sheets") + box("Your spritesheets", '''        <p class="hint">PNG files you uploaded. Every asset starts from one. You can reuse a sheet in several assets. <a href="#create">Upload a spritesheet</a> · <a href="#link">Send from Aseprite</a></p>
        <div class="tbl"><table><tr><th></th><th>File</th><th class="num">Frames</th><th class="num">Animations</th><th>Used by</th><th></th></tr>
''' + "".join(srow(t, f, sz, fr, an, u if (u != "Palm tree") else "", d) for t, f, sz, fr, an, u, d in SHEETS) + '''        </table></div>
        <p class="hint">A sheet can be deleted only when no asset uses it.</p>''')
