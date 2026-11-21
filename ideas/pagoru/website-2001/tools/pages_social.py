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

import math
MARKET = [  # icon, w, h, hotel, code, price, change
  ("navigator", 23, 23, "OpenHotel (your hotel)", "OHC", "1.000", "0.0"),
  ("console-off", 15, 23, "Pixel Plaza", "PXP", "0.420", "+3.2"),
  ("club", 23, 21, "Neon Docks", "NDK", "1.850", "-1.4"),
  ("purse", 18, 20, "Hotel Aurora", "AUR", "0.075", "+12.0"),
  ("inventory", 20, 19, "Moonbase Inn", "MBI", "0.910", "-0.3"),
]
def mrow(ic, w, h, n, c, p, ch):
    cls = "up" if ch.startswith("+") else ("down" if ch.startswith("-") else "")
    arrow = "▲" if cls == "up" else ("▼" if cls == "down" else "")
    return f'          <tr><td><img class="fav" src="assets/oh/icon-{ic}.png" width="{w}" height="{h}" alt=""> <a href="#coin">{n}</a></td><td><b>{c}</b></td><td class="num">{p}</td><td class="num {cls}">{arrow} {ch}%</td></tr>\n'
HIST = [("21 Nov 15:02", "PXP to OHC", "Sold", "1,000 PXP", "0.419", "415 OHC", "10 PXP"),
        ("20 Nov 21:40", "OHC to NDK", "Bought", "200 OHC", "1.862", "107 NDK", "2 OHC"),
        ("19 Nov 18:12", "AUR to OHC", "Sold", "20,000 AUR", "0.071", "1,406 OHC", "200 AUR"),
        ("17 Nov 10:05", "PXP to OHC", "Open order", "5,000 PXP", "0.430", "-", "-")]
def hrow(*c): return "          <tr>" + "".join(f'<td class="{"num" if i >= 3 else ""}">{x}</td>' for i, x in enumerate(c)) + "</tr>\n"
XFORM = """            <form class="form xform" onsubmit="event.preventDefault()">
              <label>You give<span class="pair"><input class="in" type="number" value="1000" min="1"><select class="in"><option>PXP</option><option>OHC</option><option>NDK</option></select></span></label>
              <label>You get<span class="pair"><input class="in" type="text" value="415" readonly><select class="in"><option>OHC</option><option>PXP</option><option>NDK</option></select></span></label>
              <fieldset class="vis"><legend>Price</legend>
                <label class="chk"><input type="radio" name="ot" checked> Market: 0.419 now</label>
                <label class="chk"><input type="radio" name="ot"> Limit: only at my price</label>
              </fieldset>
              <p class="hint">Fee 1%: 10 PXP. Daily limit left: 46,000 OHC.</p>
              <div class="row"><button class="btn main" type="submit">Exchange</button></div>
            </form>
"""
WALLETS = """            <dl class="kv">
              <div><dt>OpenHotel</dt><dd>1,250 OHC</dd></div>
              <div><dt>Pixel Plaza</dt><dd>4,800 PXP</dd></div>
              <div><dt>Neon Docks</dt><dd>320 NDK</dd></div>
            </dl>
"""
exchange_body = """      <div class="split3">
        <div class="col">
          <div class="blk box dense">
            <h2>Credit exchange</h2>
            <p class="hint">Swap the credits of one hotel for another's. Prices are in OHC. Click a hotel for the chart and details.</p>
            <div class="tbl"><table>
              <tr><th>Hotel</th><th>Credit</th><th class="num">Price (OHC)</th><th class="num">24h</th></tr>
""" + "".join(mrow(*m) for m in MARKET) + """            </table></div>
          </div>
          <div class="blk box dense">
            <h2>Your exchanges</h2>
            <div class="tbl"><table>
              <tr><th>Date</th><th>Pair</th><th>Type</th><th class="num">You gave</th><th class="num">Price</th><th class="num">You got</th><th class="num">Fee</th></tr>
""" + "".join(hrow(*h) for h in HIST) + """            </table></div>
            <div class="pager"><span class="hint">Last 4 of 37</span><span><a href="#exchange">All</a> &gt;&gt;</span></div>
          </div>
        </div>
        <div class="col">
          <div class="blk box"><h2>Your wallets</h2>
""" + WALLETS + """          </div>
          <div class="blk box"><h2>Exchange</h2>
""" + XFORM + """          </div>
        </div>
      </div>
"""

pts = [0.40 + 0.012 * math.sin(i / 3.1) + 0.008 * math.sin(i / 1.3) + i * 0.0004 for i in range(60)]
lo, hi = min(pts) - 0.004, max(pts) + 0.004
xy = [(i * 520 / 59, 150 - (v - lo) / (hi - lo) * 140) for i, v in enumerate(pts)]
line = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy)
area = line + " L520,160 L0,160 Z"
chart = (f'<div class="chart"><svg viewBox="0 0 520 160" preserveAspectRatio="none" role="img" aria-label="PXP price, up 3.2%"><path class="ar" d="{area}"/><path class="ln" d="{line}"/></svg>'
         f'<div class="axis"><span>{hi:.3f}</span><span>{lo:.3f}</span></div></div>'
         '<div class="ktabs"><a class="btn" href="#coin">1D</a><a class="btn main" href="#coin">1W</a><a class="btn" href="#coin">1M</a><a class="btn" href="#coin">All</a></div>')
coin_body = """      <div class="split3">
        <div class="col">
          <div class="blk box dense">
            <p class="crumb"><a href="#exchange">Exchange</a> &gt; Pixel Plaza</p>
            <h2><img class="fav" src="assets/oh/icon-console-off.png" width="15" height="23" alt=""> Pixel Plaza · PXP</h2>
            <p><b style="font-size:20px">0.420 OHC</b> <span class="up">▲ +3.2%</span> <span class="hint">24h</span></p>
            """ + chart + """
          </div>
          <div class="blk box dense">
            <h2>Order book</h2>
            <div class="two book">
              <div class="tbl"><table><tr><th>Buying PXP</th><th class="num">Price</th></tr>
                <tr><td>12,000</td><td class="num up">0.419</td></tr><tr><td>4,500</td><td class="num up">0.418</td></tr><tr><td>30,000</td><td class="num up">0.415</td></tr></table></div>
              <div class="tbl"><table><tr><th>Selling PXP</th><th class="num">Price</th></tr>
                <tr><td>2,000</td><td class="num down">0.421</td></tr><tr><td>9,800</td><td class="num down">0.423</td></tr><tr><td>15,000</td><td class="num down">0.430</td></tr></table></div>
            </div>
          </div>
          <div class="blk box dense">
            <h2>Latest trades</h2>
            <div class="tbl"><table><tr><th>Time</th><th class="num">Price</th><th class="num">Amount (PXP)</th></tr>
              <tr><td>15:02</td><td class="num up">0.420</td><td class="num">1,000</td></tr><tr><td>14:51</td><td class="num down">0.419</td><td class="num">250</td></tr><tr><td>14:20</td><td class="num up">0.420</td><td class="num">3,400</td></tr></table></div>
          </div>
        </div>
        <div class="col">
          <div class="blk box dense"><h2>Numbers</h2>
            <dl class="kv"><div><dt>24h high / low</dt><dd>0.425 / 0.401</dd></div><div><dt>In circulation</dt><dd>5.6M</dd></div><div><dt>Created 24h</dt><dd>82,000</dd></div><div><dt>Destroyed 24h</dt><dd>61,000</dd></div><div><dt>Traded 24h</dt><dd>41,250</dd></div><div><dt>Fee</dt><dd>1%, burned</dd></div><div><dt>Hotel</dt><dd><a href="#">Pixel Plaza</a></dd></div></dl>
            <p class="hint">The hotel reports its credits every day. If reports stop, trading pauses.</p>
          </div>
          <div class="blk box"><h2>You hold</h2><dl class="kv"><div><dt>Pixel Plaza</dt><dd>4,800 PXP</dd></div></dl></div>
          <div class="blk box"><h2>Exchange</h2>
""" + XFORM + """          </div>
        </div>
      </div>
"""
