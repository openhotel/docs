# Friends and Credit exchange bodies. Exec'd by subpages.py after pages_acct.py.
FRIENDS = [  # avatar, name, motto, online, where, hotel icon (file, w, h)
  ("a", "Mintleaf", "gardening in the Atrium", True, "Pixel Plaza · Disco Hall", ("console-off", 15, 23)),
  ("c", "Captain_K", "arr", True, "OpenHotel · Lobby", ("navigator", 23, 23)),
  ("b", "Pebbles", "back at 9", True, "Neon Docks · Rooftop", ("club", 23, 21)),
  ("e", "nightbus", "", True, "OpenHotel · The Cafe", ("navigator", 23, 23)),
  ("d", "Lumen", "first!", False, "Last seen 2 days ago in Pixel Plaza", None),
  ("a", "Wanda", "on holiday", False, "Last seen 3 weeks ago in OpenHotel", None),
]
def friend(a, n, motto, on, where, ic):
    icon = f'<img class="fav" src="assets/oh/icon-{ic[0]}.png" width="{ic[1]}" height="{ic[2]}" alt="">' if ic else ""
    act = '<a class="btn main" href="#">Join</a>' if on else '<a class="btn" href="#">Message</a>'
    return (f'          <li class="{"on" if on else "off"}"><img src="assets/oh/av-idle-{a}.png" width="21" height="66" alt="">'
            f'<div><b>{n}</b>{f" <i>{motto}</i>" if motto else ""}<p>{icon}{where}</p></div>{act}</li>\n')
friends_body = '''      <div class="split3">
        <div class="col">
          <div class="blk box friends">
            <h2>Friends (6)</h2>
            <h3>Online now (4)</h3>
            <ul>
''' + "".join(friend(*f) for f in FRIENDS if f[3]) + '''            </ul>
            <h3>Offline (2)</h3>
            <ul>
''' + "".join(friend(*f) for f in FRIENDS if not f[3]) + '''            </ul>
          </div>
        </div>
        <div class="col">
          <div class="blk box">
            <h2>Requests (2)</h2>
            <ul class="reqs">
              <li><b>Sparrow</b> <span class="hint">from Neon Docks</span><div class="acts"><button class="btn main" type="button">Accept</button><button class="btn" type="button">Ignore</button></div></li>
              <li><b>Tobi_92</b> <span class="hint">from OpenHotel</span><div class="acts"><button class="btn main" type="button">Accept</button><button class="btn" type="button">Ignore</button></div></li>
            </ul>
          </div>
          <div class="blk box">
            <h2>Add a friend</h2>
            <form class="form" onsubmit="event.preventDefault()"><label>Username<input class="in" placeholder="Their name in any hotel"></label><div class="row"><button class="btn" type="submit">Send request</button></div></form>
          </div>
          <div class="blk box">
            <h2>One list, every hotel</h2>
            <p>Your friends come with your OpenHotel account, so you see them in every hotel you join. Furniture and credits stay in the hotel where you got them.</p>
          </div>
        </div>
      </div>
'''

MARKET = [  # icon, w, h, hotel, code, price, change, supply, volume
  ("navigator", 23, 23, "OpenHotel", "OHC", "1.000", "0.0", "2.1M", "18,400"),
  ("console-off", 15, 23, "Pixel Plaza", "PXP", "0.420", "+3.2", "5.6M", "41,250"),
  ("club", 23, 21, "Neon Docks", "NDK", "1.850", "-1.4", "310K", "6,900"),
  ("purse", 18, 20, "Hotel Aurora", "AUR", "0.075", "+12.0", "48M", "122,000"),
  ("inventory", 20, 19, "Moonbase Inn", "MBI", "0.910", "-0.3", "760K", "2,140"),
]
def mrow(ic, w, h, n, c, p, ch, s, v):
    cls = "up" if ch.startswith("+") else ("down" if ch.startswith("-") else "")
    arrow = "▲" if cls == "up" else ("▼" if cls == "down" else "")
    return f'          <tr><td><img class="fav" src="assets/oh/icon-{ic}.png" width="{w}" height="{h}" alt=""> {n}</td><td><b>{c}</b></td><td class="num">{p}</td><td class="num {cls}">{arrow} {ch}%</td><td class="num">{s}</td><td class="num">{v}</td></tr>\n'
exchange_body = '''      <div class="split3">
        <div class="col">
          <div class="blk box">
            <h2>Credit exchange</h2>
            <p>Every hotel has its own credits, earned by playing there. Here you can swap them between hotels. Prices are in OpenHotel credits (OHC) and move with what guests buy and sell.</p>
            <div class="tbl"><table>
              <tr><th>Hotel</th><th>Credit</th><th class="num">Price (OHC)</th><th class="num">24h</th><th class="num">In circulation</th><th class="num">Traded 24h</th></tr>
''' + "".join(mrow(*m) for m in MARKET) + '''            </table></div>
            <p class="hint">Sample prices. A hotel that gives away lots of credits sees its price fall.</p>
          </div>
          <div class="blk box">
            <h2>PXP / OHC order book</h2>
            <div class="two book">
              <div class="tbl"><table><tr><th>Buying PXP</th><th class="num">Price</th></tr>
                <tr><td>12,000</td><td class="num up">0.419</td></tr><tr><td>4,500</td><td class="num up">0.418</td></tr><tr><td>30,000</td><td class="num up">0.415</td></tr></table></div>
              <div class="tbl"><table><tr><th>Selling PXP</th><th class="num">Price</th></tr>
                <tr><td>2,000</td><td class="num down">0.421</td></tr><tr><td>9,800</td><td class="num down">0.423</td></tr><tr><td>15,000</td><td class="num down">0.430</td></tr></table></div>
            </div>
          </div>
          <div class="blk box">
            <h2>How it works</h2>
            <ul class="perms">
              <li>Credits are never sold for real money. You get them by playing, and trade them here.</li>
              <li>Each trade pays a 1% fee in credits; the fee is removed from circulation.</li>
              <li>Furniture never moves between hotels. Credits do, at the market price.</li>
              <li>Hotel owners see how many credits their hotel creates, so the price stays honest.</li>
            </ul>
          </div>
        </div>
        <div class="col">
          <div class="blk box">
            <h2>Your wallets</h2>
            <dl class="kv">
              <div><dt>OpenHotel</dt><dd>1,250 OHC</dd></div>
              <div><dt>Pixel Plaza</dt><dd>4,800 PXP</dd></div>
              <div><dt>Neon Docks</dt><dd>320 NDK</dd></div>
            </dl>
          </div>
          <div class="blk box">
            <h2>Exchange</h2>
            <form class="form xform" onsubmit="event.preventDefault()">
              <label>You give<span class="pair"><input class="in" type="number" value="1000" min="1"><select class="in"><option>PXP</option><option>OHC</option><option>NDK</option></select></span></label>
              <label>You get<span class="pair"><input class="in" type="text" value="415" readonly><select class="in"><option>OHC</option><option>PXP</option><option>NDK</option></select></span></label>
              <fieldset class="vis"><legend>Price</legend>
                <label class="chk"><input type="radio" name="ot" checked> Market: 0.419 now</label>
                <label class="chk"><input type="radio" name="ot"> Limit: only at my price</label>
              </fieldset>
              <p class="hint">Fee 1%: 10 PXP. Daily limit left: 46,000 OHC.</p>
              <div class="row"><button class="btn main" type="submit">Exchange</button></div>
            </form>
          </div>
        </div>
      </div>
'''
