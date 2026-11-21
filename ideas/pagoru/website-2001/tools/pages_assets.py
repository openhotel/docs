# Hotel assets, Marketplace and Create bodies. Exec'd by subpages.py after pages_social.py.
def img(f, w, h, alt=""): return f'<img src="assets/oh/{f}.png" width="{w}" height="{h}" alt="{alt}">'
FURNI = {"tel": ("furni-icon-telephone", 24, 50), "flag": ("furni-icon-flag", 18, 22), "poster": ("furni-icon-poster", 16, 24)}

ROOMS = [("news-atrium", "The Atrium", "OpenHotel", "1.2", True, True), ("news-pool", "Rooftop Pool", "Mintleaf", "2.0", True, False),
         ("news-disco", "Disco Hall", "Pebbles", "1.0", False, False)]
FURN = [("tel", "Telephone booth", "OpenHotel", "1.1", True, "25"), ("flag", "Pirate flag", "Captain_K", "1.0", True, "10"),
        ("poster", "Poster A-24", "OpenHotel", "1.0", False, "5")]
CLOTH = [("c", "Striped shirt", "Wanda", True), ("b", "Red jacket", "Lumen", True), ("e", "Summer dress", "nightbus", False)]
chk = lambda on: f'<input type="checkbox"{" checked" if on else ""} aria-label="In this hotel">'
library = '''      <div class="split3">
        <div class="col">
          <div class="blk box">
            <h2>Hotel assets</h2>
            <p>Everything guests can see in your hotel: public rooms, furniture in the catalog and clothes. Tick what you want in; untick to take it out. Rooms guests built stay as they are.</p>
            <div class="row" style="display:flex;gap:8px;flex-wrap:wrap;align-items:center"><select class="in" style="max-width:220px"><option>Sunset Plaza</option><option>Pixel Inn</option></select><span class="hint">3 rooms · 128 furniture · 64 clothes</span></div>
          </div>
          <div class="blk box">
            <h2>Public rooms</h2>
            <div class="tbl"><table><tr><th></th><th>Room</th><th>Made by</th><th class="num">Version</th><th>Open</th><th>First room</th></tr>
''' + "".join(f'              <tr><td>{img(t, 64, 64)}</td><td><b>{n}</b></td><td>{b}</td><td class="num">{v}</td><td>{chk(on)}</td><td><input type="radio" name="first"{" checked" if first else ""} aria-label="First room"></td></tr>\n' for t, n, b, v, on, first in ROOMS) + '''            </table></div>
            <p class="hint">The first room is where guests land when they enter the hotel.</p>
          </div>
          <div class="blk box">
            <h2>Furniture</h2>
            <div class="tbl"><table><tr><th></th><th>Furniture</th><th>Made by</th><th class="num">Version</th><th>In catalog</th><th class="num">Price</th></tr>
''' + "".join(f'              <tr><td class="ic">{img(*FURNI[k])}</td><td><b>{n}</b></td><td>{b}</td><td class="num">{v}</td><td>{chk(on)}</td><td class="num"><input class="in price" type="number" value="{p}" min="0" aria-label="Price in credits"></td></tr>\n' for k, n, b, v, on, p in FURN) + '''            </table></div>
            <div class="pager"><span class="hint">Page 1 of 43 · price in this hotel's credits</span><span><a href="#">Next</a> &gt;&gt;</span></div>
          </div>
          <div class="blk box">
            <h2>Clothes</h2>
            <div class="tbl"><table><tr><th></th><th>Clothes</th><th>Made by</th><th>In wardrobe</th></tr>
''' + "".join(f'              <tr><td>{img("av-idle-" + a, 21, 66)}</td><td><b>{n}</b></td><td>{b}</td><td>{chk(on)}</td></tr>\n' for a, n, b, on in CLOTH) + '''            </table></div>
            <div class="pager"><span class="hint">Page 1 of 22</span><span><a href="#">Next</a> &gt;&gt;</span></div>
          </div>
        </div>
        <div class="col">
          <div class="blk box">
            <h2>Add assets</h2>
            <p><a class="btn main" href="#market">Find in the marketplace</a></p>
            <form class="form" onsubmit="event.preventDefault()"><label>Or upload a file<input class="in" type="file" accept=".oha"></label><span class="hint">Only signed .oha files.</span></form>
          </div>
          <div class="blk box">
            <h2>Updates (2)</h2>
            <ul class="reqs">
              <li><b>Telephone booth</b> <span class="hint">1.1 to 1.2</span><div class="acts"><button class="btn main" type="button">Update</button><button class="btn" type="button">Skip</button></div></li>
              <li><b>Rooftop Pool</b> <span class="hint">2.0 to 2.1</span><div class="acts"><button class="btn main" type="button">Update</button><button class="btn" type="button">Skip</button></div></li>
            </ul>
            <p class="hint">Your hotel keeps the version you chose until you update.</p>
          </div>
          <div class="blk box">
            <h2>Who can do what</h2>
            <ul class="perms"><li>Anyone can make assets and share them in the marketplace.</li><li>Only the hotel owner puts them in the hotel.</li></ul>
          </div>
        </div>
      </div>
'''

MKT = [("furni-telephone", 48, 98, "Telephone booth", "Furniture", "OpenHotel", "4.8", "1,204"),
       ("news-pool", 64, 64, "Rooftop Pool", "Public room", "Mintleaf", "4.5", "312"),
       ("av-idle-c", 21, 66, "Striped shirt", "Clothes", "Wanda", "4.1", "880"),
       ("furni-icon-flag", 18, 22, "Pirate flag", "Furniture", "Captain_K", "4.6", "540"),
       ("news-disco", 64, 64, "Disco Hall", "Public room", "Pebbles", "3.9", "96"),
       ("av-idle-b", 21, 66, "Red jacket", "Clothes", "Lumen", "4.3", "410")]
def card(f, w, h, n, k, b, r, u):
    return (f'            <li><div class="pv">{img(f, w, h)}</div><b>{n}</b><span class="hint">{k} · by {b}</span><span class="hint">★ {r} · in {u} hotels</span>'
            f'<div class="acts"><button class="btn main" type="button">Add to Sunset Plaza</button><a class="btn" href="#">.oha</a></div></li>\n')
market = '''      <div class="split3">
        <div class="col">
          <div class="blk box">
            <h2>Marketplace</h2>
            <p>Rooms, furniture and clothes made by guests and hotel owners. All free. Add one to your hotel in one click, or download the file.</p>
            <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search assets" aria-label="Search assets"><select class="in" aria-label="Kind"><option>Everything</option><option>Public rooms</option><option>Furniture</option><option>Clothes</option></select><select class="in" aria-label="Sort"><option>Most used</option><option>Newest</option><option>Best rated</option></select><button class="btn" type="submit">Search</button></form>
          </div>
          <div class="blk box">
            <h2>Most used this week</h2>
            <ul class="agrid">
''' + "".join(card(*m) for m in MKT) + '''            </ul>
            <div class="pager"><span class="hint">Page 1 of 120</span><span><a href="#">More</a> &gt;&gt;</span></div>
          </div>
        </div>
        <div class="col">
          <div class="blk box">
            <h2>Make your own</h2>
            <p>Draw on the website, in Aseprite on your computer, or in Resprite on your iPad.</p>
            <p><a class="btn main" href="#create">Create an asset</a></p>
          </div>
          <div class="blk box">
            <h2>Your creations (3)</h2>
            <dl class="kv"><div><dt>Neon sign</dt><dd><span class="badge on">Live</span></dd></div><div><dt>Palm tree</dt><dd><span class="badge">In review</span></dd></div><div><dt>Beach towel</dt><dd><span class="badge">Draft</span></dd></div></dl>
          </div>
          <div class="blk box">
            <h2>Rules</h2>
            <ul class="perms"><li>Your own art only. Copied art gets removed.</li><li>Every asset is checked before it goes live, then signed so hotels can trust it.</li><li>Shared under CC BY-NC-SA 4.0.</li></ul>
          </div>
        </div>
      </div>
'''

PAL = ["#000000", "#ffffff", "#7f7f7f", "#c0392b", "#e67e22", "#f1c40f", "#27ae60", "#2980b9", "#8e44ad", "#efcfb1"]
DIRS = ["North", "East", "South", "West"]
create = '''      <div class="split3">
        <div class="col">
          <div class="blk box">
            <h2>Create an asset</h2>
            <form class="form" onsubmit="event.preventDefault()">
              <fieldset class="vis"><legend>What are you making?</legend>
                <label class="chk"><input type="radio" name="k" checked> Furniture</label>
                <label class="chk"><input type="radio" name="k"> Public room</label>
                <label class="chk"><input type="radio" name="k"> Clothes</label>
              </fieldset>
              <label>Name<input class="in" value="Telephone booth"></label>
              <label>Size in tiles<span class="pair tiles"><input class="in" type="number" value="1" min="1" aria-label="Width"><input class="in" type="number" value="1" min="1" aria-label="Depth"></span></label>
            </form>
          </div>
          <div class="blk box">
            <h2>Draw</h2>
            <div class="ed">
              <div class="tools" role="toolbar" aria-label="Tools"><button class="btn main" type="button">Pencil</button><button class="btn" type="button">Eraser</button><button class="btn" type="button">Fill</button><button class="btn" type="button">Pick</button></div>
              <div class="canvas"><img src="assets/oh/furni-telephone.png" width="48" height="98" alt="Telephone booth, north"></div>
              <div class="pal">''' + "".join(f'<button type="button" class="sw" style="background:{c}" aria-label="Colour {c}"></button>' for c in PAL) + '''</div>
            </div>
            <div class="dirs">''' + "".join(f'<button class="btn{" main" if d == "North" else ""}" type="button">{d}{" ✓" if d in ("North", "East") else ""}</button>' for d in DIRS) + '''</div>
            <p class="hint">2 of 4 directions drawn. Furniture needs all four, or two if it is the same mirrored.</p>
          </div>
          <div class="blk box">
            <h2>Send</h2>
            <p>We check it, then sign it as a .oha file. Once it is live, any hotel owner can add it.</p>
            <div class="row" style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn main" type="button">Send for review</button><button class="btn" type="button">Save draft</button></div>
          </div>
        </div>
        <div class="col">
          <div class="blk box apps">
            <h2>Draw in your own app</h2>
            <h3>Aseprite</h3>
            <p>Install the OpenHotel extension, then <b>File &gt; Send to OpenHotel</b>. Layers and tags become directions and frames.</p>
            <p><a class="btn" href="#">Get the extension</a></p>
            <h3>Resprite (iPad)</h3>
            <p>Export as .aseprite, then share it to this page or upload it below.</p>
            <form class="form" onsubmit="event.preventDefault()"><label>Upload<input class="in" type="file" accept=".aseprite,.ase,.png"></label></form>
          </div>
          <div class="blk box">
            <h2>Link an app</h2>
            <p>Type this code in the extension. It works for 10 minutes.</p>
            <p class="code">482 913</p>
            <dl class="kv"><div><dt>Aseprite on PC</dt><dd><a class="danger" href="#">Unlink</a></dd></div></dl>
          </div>
        </div>
      </div>
'''
