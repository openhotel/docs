# Hotel manage pages (with sub nav) and network pages. Exec'd by subpages.py after pages_assets.py.
def box(title, inner, cls="blk box dense"): return f'      <div class="{cls}">\n        <h2>{title}</h2>\n{inner}\n      </div>\n'
def TBL(h, rows, num=(), go=False):
    cls = ' class="go"' if go else ""
    return ('<div class="tbl"><table><tr>' + "".join(f'<th{" class=\"num\"" if i in num else ""}>{x}</th>' for i, x in enumerate(h)) + "</tr>"
            + "".join(f"<tr{cls}>" + "".join(f'<td{" class=\"num\"" if i in num else ""}>{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows) + "</table></div>")
BTN = lambda t, main=False: f'<button class="btn{" main" if main else ""}" type="button">{t}</button>'
KV = lambda rows: '<dl class="kv">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>"
PAGER = lambda t, k: f'<div class="pager"><span class="hint">{t}</span><span><a href="#{k}">Next</a> &gt;&gt;</span></div>'
def subnav(items, cur, title):
    return (f'      <nav class="blk subnav" aria-label="{title}">' + "".join(f'<a class="btn{" main" if k == cur else ""}" href="#{k}">{n}</a>' for k, n in items) + '</nav>\n')
ADMIN_NAV = [("admin", "Manage hotel"), ("admin-registration", "Registration"), ("admin-accounts", "Accounts"), ("admin-blocked", "Blocked"), ("admin-rooms", "Rooms"),
             ("admin-moderation", "Moderation"), ("admin-news", "News"), ("admin-credits", "Credits"), ("library", "Catalog"), ("admin-publicrooms", "Public rooms"), ("admin-clothes", "Clothes")]
NET_NAV = [("network", "Network admin"), ("network-hotels", "Hotels"), ("network-accounts", "Accounts"), ("network-blocked", "Blocked"), ("network-emails", "Emails"), ("network-news", "News"), ("network-credits", "Credit reports"), ("network-settings", "Settings")]
AN = lambda cur: subnav(ADMIN_NAV, cur, "Manage OpenHotel")
NN = lambda cur: subnav(NET_NAV, cur, "Network admin")

admin = AN("admin") + box("Overview", KV([("Accounts", "1,204,311"), ("Online now", "1,820"), ("Rooms", "184,020"), ("Chat messages 24h", "2.1M"), ("Credits created / destroyed 24h", "310k / 262k"), ("Purchases 24h", "48,210")])
    + '<p class="hint">OpenHotel v0.156.0 · new registrations <b>open</b> · 3 open reports · 2 asset updates</p>') + box("Needs attention", TBL(
    ["What", "Where", ""], [["3 reported messages", "Moderation", '<a class="btn main" href="#admin-moderation">Review</a>'], ["2 asset updates", "Catalog", '<a class="btn main" href="#library">Update</a>'], ["1 account waiting for a role", "Accounts", '<a class="btn" href="#admin-accounts">Open</a>']]))
admin_registration = AN("admin-registration") + box("Registration", '''        <form class="form" onsubmit="event.preventDefault()"><label class="chk"><input type="checkbox"> Closed to new registrations</label>
          <span class="hint">Accounts that already exist still enter. New accounts can't connect to this hotel.</span>
          <label>Message shown to new guests<input class="in" value="We are full for now. Come back soon!"></label>
          <label class="chk"><input type="checkbox" checked> Guests need a verified email</label>
          <label class="chk"><input type="checkbox"> Only accounts older than 7 days</label>
          <div class="row"><button class="btn main" type="submit">Save</button></div></form>''')
admin_accounts = AN("admin-accounts") + box("Accounts (1,204,311)", '''        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search a name" aria-label="Search"><select class="in" aria-label="Filter"><option>Everyone</option><option>Online</option><option>Staff</option><option>New this week</option></select></form>'''
    + TBL(["Name", "Role", "Since", "Last seen", "Credits", ""], [
    ["Mintleaf", "Guest", "Aug 2026", "Online", "4,800", BTN("Mute") + " " + BTN("Block")],
    ["Captain_K", "Moderator", "Aug 2026", "Online", "950", BTN("Role") + " " + BTN("Block")],
    ["Pebbles", "Guest", "Oct 2026", "2 h ago", "120", BTN("Mute") + " " + BTN("Block")],
    ["Sparrow", "Guest", "Nov 2026", "Yesterday", "40", BTN("Mute") + " " + BTN("Block")]], (4,)) + PAGER("1-4 of 1,204,311", "admin-accounts"))
admin_blocked = AN("admin-blocked") + box("Blocked here (6)", TBL(
    ["Name", "Reason", "By", "Date", ""], [["Trollface", "Spam in 3 rooms", "Captain_K", "20 Nov", BTN("Unblock")], ["xX_cheat", "Credit exploit", "Nightowl", "14 Nov", BTN("Unblock")], ["Rude99", "Harassment", "Captain_K", "09 Nov", BTN("Unblock")]]) + PAGER("3 of 6", "admin-blocked")) + box("Blocked on other hotels (2)", TBL(
    ["Name", "Hotel", "Reason", "Date", ""], [["Sparrow", "Pixel Plaza", "Harassment", "18 Nov", BTN("Block here too", True) + " " + BTN("Ignore")], ["Wanda", "Neon Docks", "Credit exploit", "12 Nov", BTN("Block here too", True) + " " + BTN("Ignore")]])
    + '<p class="hint">Guests of this hotel who were blocked in another hotel. Only the hotel, the reason and the date are shared. A network block (<a href="#network-blocked">Network admin</a>) applies here automatically.</p>')
admin_rooms = AN("admin-rooms") + box("Rooms (184,020)", TBL(
    ["Room", "Owner", "Now", "Messages 24h", ""], [["Mint garden", "Mintleaf", "12", "1.1k", BTN("Close") + " " + BTN("Delete")], ["Pebbles' pad", "Pebbles", "0", "0", BTN("Delete")], ["Disco night", "Lumen", "7", "620", BTN("Close") + " " + BTN("Delete")]], (2, 3))
    + PAGER("3 of 184,020", "admin-rooms") + '<p class="hint">Public rooms are managed in <a href="#admin-publicrooms">Public rooms</a>.</p>')
admin_moderation = AN("admin-moderation") + box("Reported messages (3)", TBL(
    ["Message", "Room", "From", "Reports", ""], [["“...buy credits at my site...”", "The Atrium", "Trollface", "5", BTN("Delete", True) + " " + BTN("Ignore")], ["“you suck”", "Mint garden", "Rude99", "2", BTN("Mute") + " " + BTN("Ignore")]], (3,))) + box("Blocked words (42)", '''        <form class="form" onsubmit="event.preventDefault()"><label>Replace every blocked word with<input class="in" value="***" style="max-width:200px"></label>
          <span class="hint">One text for all the words, like ***. Guests see it in the chat instead of the word.</span>
          <label class="chk"><input type="checkbox" checked> Mute a guest for 10 minutes after 3 blocked messages</label><div class="row"><button class="btn main" type="submit">Save</button></div></form>
        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" placeholder="Add a word" aria-label="Word"><button class="btn" type="submit">Add</button></form>''' + TBL(
    ["Word", ""], [["casino", BTN("Remove")], ["free credits", BTN("Remove")], ["discord.gg", BTN("Remove")]]) + PAGER("3 of 42", "admin-moderation"))
admin_credits = AN("admin-credits") + box("Credits", KV([("Credit", "OHC (quote currency of the exchange)"), ("In circulation", "2.1M"), ("Created 24h", "310,000"), ("Destroyed 24h", "262,000"), ("Exchange price", "1.000 OHC")])) + box("Purchases", TBL(
    ["When", "Who", "Bought", "Price"], [["15:20", "Mintleaf", "Telephone booth", "25 OHC"], ["15:02", "Pebbles", "Pirate flag", "10 OHC"], ["14:48", "Wanda", "Striped shirt", "free"]], (3,)) + PAGER("3 of 48,210 today", "admin-credits"))
PR = [("atrium", "The Atrium", "1.2", 2, True, True, 80), ("pool", "Rooftop Pool", "2.0", 2, True, False, 40), ("disco", "Disco Hall", "1.0", 2, False, False, 40)]
def prrow(t, n, v, s, o, f, m):
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a></td><td class="num">{v}</td><td>{sch(s)}</td>'
            f'<td><select class="in sel-s" aria-label="State"><option{" selected" if o else ""}>Open</option><option{"" if o else " selected"}>Closed</option></select></td>'
            f'<td><input type="radio" name="first"{" checked" if f else ""} aria-label="First room"></td><td class="num"><input class="in price" type="number" value="{m}" aria-label="Max users"></td></tr>')
admin_publicrooms = AN("admin-publicrooms") + box("Public rooms (3)", '<div class="tbl"><table><tr><th></th><th>Room</th><th class="num">Version</th><th>Schema</th><th>State</th><th>First room</th><th class="num">Max users</th></tr>'
    + "".join(prrow(*r) for r in PR)
    + '</table></div><p><a class="btn main" href="#market">Add rooms from the marketplace</a> <button class="btn" type="button">Save</button></p><p class="hint">Guests land in the first room when they enter the hotel.</p>')
SKINS = ["#efcfb1", "#f6dcc8", "#d9a57a", "#c98e62", "#a8714a", "#7a4a2e"]
def crow(t, n, by, sl, v, on, pr, d=("", "", False)):
    return (f'<tr class="go"><td>{tb(t)}</td><td><a href="#item"><b>{n}</b></a><br><span class="hint">{by} · {sl}</span></td><td class="num">{v}</td><td>{sch(1)}</td>'
            f'<td><input type="checkbox"{" checked" if on else ""} aria-label="In wardrobe"></td>'
            f'<td class="dr"><input class="in" type="date" value="{d[0]}" aria-label="Publish"></td><td class="dr"><input class="in" type="date" value="{d[1]}" aria-label="Unpublish"><label class="chk"><input type="checkbox"{" checked" if d[2] else ""}> Repeat yearly</label></td><td class="num">{pr}</td></tr>')
PRICE = lambda v: f'<input class="in price" type="number" value="{v}" aria-label="Price">'
admin_clothes = AN("admin-clothes") + box("Character personalisation", '''        <p class="hint">What guests can change on their avatar in this hotel.</p>
        <h3>Skin colours</h3>
        <div class="skins">''' + "".join(f'<label class="skin"><span style="background:{c}"></span><input type="checkbox" checked disabled aria-label="{c} is always allowed"> {c}</label>' for c in SKINS) + '''</div>
        <p class="hint">The six default skin colours are always allowed and can't be removed or turned off, so every guest can pick their own. You can add more colours.</p>
        <h3>Extra colours</h3>
        <div class="skins"><label class="skin"><span style="background:#8fd0a4"></span><input type="checkbox" checked aria-label="Allow #8fd0a4"> #8fd0a4</label> <button class="btn" type="button">Remove</button></div>
        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" placeholder="#a1b2c3" aria-label="New colour" style="max-width:110px"><button class="btn" type="submit">Add colour</button><label class="chk">Default skin <select class="in sel-s"><option>#efcfb1</option><option>#c98e62</option></select></label></form>
        <h3>Guests can change</h3>
        <label class="chk"><input type="checkbox" checked> Skin colour</label> <label class="chk"><input type="checkbox" checked> Hair colour</label> <label class="chk"><input type="checkbox" checked> Clothes colours</label>
        <p><button class="btn main" type="button">Save</button></p>''') + box("Wardrobe (64)", '<div class="tbl"><table><tr><th></th><th>Clothes</th><th class="num">Version</th><th>Schema</th><th>In wardrobe</th><th>Publish</th><th>Unpublish</th><th class="num">Price</th></tr>'
    + crow("c", "Striped shirt", "Wanda", "top", "1.0", True, '<span class="hint">free</span>') + crow("b", "Red jacket", "Lumen", "top", "1.0", True, PRICE(20), ("2026-12-01", "2027-01-06", True)) + crow("e", "Summer dress", "nightbus", "top", "1.2", False, PRICE(30), ("2026-06-01", "2026-09-15", True))
    + '</table></div>' + PAGER("3 of 64", "admin-clothes") + '<p><a class="btn main" href="#market">Add clothes from the marketplace</a></p>')

network = NN("network") + box("Overview", KV([("Hotels", "128"), ("Public", "96"), ("Online now", "4,210"), ("Accounts", "1.2M"), ("Waiting for review", "<b>2</b>")])) + box("Needs attention", TBL(
    ["What", "Where", ""], [["Hotel Nova asks to join", "Hotels", '<a class="btn main" href="#network-hotels">Review</a>'], ["Moonbase Inn runs an old version", "Hotels", '<a class="btn" href="#network-hotels">Open</a>'], ["Moonbase Inn stopped its credit reports", "Credit reports", '<a class="btn" href="#network-credits">Open</a>']]))
network_hotels = NN("network-hotels") + box("Hotels (128)", '''        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search a hotel" aria-label="Search"><select class="in" aria-label="Filter"><option>All</option><option>Waiting for review</option><option>Suspended</option><option>Old version</option></select></form>'''
    + TBL(["Hotel", "Owner", "Version", "Accounts", "Online", "Credit", "State", ""], [
    ["OpenHotel", "Nightowl", "0.156.0", "1.2M", "1,820", "OHC", '<span class="badge on">Main</span>', ""],
    ["Pixel Plaza", "Mintleaf", "0.156.0", "86k", "312", "PXP", '<span class="badge on">Live</span>', BTN("Pause trading") + " " + BTN("Suspend")],
    ["Neon Docks", "Pebbles", "0.152.1", "9k", "74", "NDK", '<span class="badge on">Live</span>', BTN("Pause trading") + " " + BTN("Suspend")],
    ["Moonbase Inn", "Lumen", "0.149.0", "2k", "11", "MBI", '<span class="badge">Old version</span>', BTN("Pause trading") + " " + BTN("Suspend")],
    ["Hotel Nova", "Sparrow", "0.156.0", "0", "0", "NOV", '<span class="badge">Review</span>', BTN("Approve", True) + " " + BTN("Reject")]], (3, 4)) + PAGER("1-5 of 128", "network-hotels"))
network_credits = NN("network-credits") + box("Credit reports", TBL(
    ["Hotel", "Last report", "Created 24h", "Destroyed 24h", "Check"], [["OpenHotel", "Today 00:04", "310,000", "262,000", '<span class="badge on">OK</span>'], ["Pixel Plaza", "Today 00:05", "82,000", "61,000", '<span class="badge on">OK</span>'], ["Neon Docks", "Today 00:07", "3,100", "2,900", '<span class="badge on">OK</span>'], ["Moonbase Inn", "3 days ago", "-", "-", '<span class="badge">Paused</span>']], (2, 3))
    + '<p class="hint">A hotel whose reports stop or don\'t add up is paused on the exchange.</p>')
network_settings = NN("network-settings") + box("Settings", '''        <form class="form" onsubmit="event.preventDefault()"><label class="chk"><input type="checkbox" checked> New hotels can be created</label>
          <label class="chk"><input type="checkbox"> Pause the whole credit exchange</label>
          <label>News emails a hotel can request per week<input class="in" type="number" value="2" style="max-width:6em"></label>
          <label>Oldest hotel version allowed<input class="in" value="0.150.0" style="max-width:120px"></label>
          <label>Newest schema the network accepts<input class="in" value="4" style="max-width:120px"></label>
          <div class="row"><button class="btn main" type="submit">Save</button></div></form>''')

# ---- catalog: collections and their items ----
CATS = [("Alpha", 5, "Visible", "-", "-", "10"), ("Flags", 14, "Visible", "-", "-", "5"), ("Teleports", 3, "Visible", "-", "-", "5 to 25"),
        ("Summer", 12, "Scheduled", "01 Jun 2027", "31 Aug 2027", "15 to 40"), ("Winter", 10, "Scheduled", "01 Dec 2026", "06 Jan 2027", "10 to 35"), ("Pirate week", 8, "Hidden", "14 Nov 2026", "21 Nov 2026", "5 to 15")]
VB = {"Visible": '<span class="badge on">Visible</span>', "Scheduled": '<span class="badge">Scheduled</span>', "Hidden": '<span class="badge">Hidden</span>'}
exec(open(T + "pages_net.py").read())
exec(open(T + "pages_mine.py").read())
def catrow(i, n, c, st, a, b, pr):
    sel = ' class="go sel"' if n == "Teleports" else ' class="go"'
    return (f'<tr{sel}><td class="ord"><button class="btn" type="button" aria-label="Move up">↑</button><button class="btn" type="button" aria-label="Move down">↓</button></td>'
            f'<td><a href="#library"><b>{n}</b></a></td><td class="num">{c}</td><td>{VB[st]}</td><td>{a}</td><td>{b}</td><td class="num">{pr}</td></tr>')
def furow(t, n, fid, cur, latest, price):
    vs = [latest, "1.0"] if cur == latest else [latest, cur]
    opts = "".join(f'<option{" selected" if v == cur else ""}>{v}{" (latest)" if v == latest else ""}</option>' for v in vs)
    upd = '' if cur == latest else ' <span class="badge">Update</span>'
    return (f'<tr><td class="ord"><button class="btn" type="button" aria-label="Move up">↑</button><button class="btn" type="button" aria-label="Move down">↓</button></td><td>{tb(t)}</td><td><b>{n}</b>{upd}<br><span class="hint">{fid}</span></td>'
            f'<td><select class="in sel-s" aria-label="Version">{opts}</select></td><td>{sch(3)}</td>'
            f'<td class="num"><input class="in price" type="number" value="{price}" min="0" aria-label="Price in OHC"></td><td class="ra"><button class="btn" type="button" aria-label="Remove">x</button></td></tr>\n')
library = AN("library") + '''      <div class="blk box dense">
        <h2>Collections in the catalog (9)</h2>
        <p class="hint">A collection is a category in the in-game catalog. Drag order = the order guests see. OpenHotel v0.156.0 runs schemas 1 to 4. Prices are in OHC.</p>
        <div class="tbl"><table><tr><th>Order</th><th>Collection</th><th class="num">Items</th><th>Visible</th><th>Publish</th><th>Unpublish</th><th class="num">Prices</th></tr>
''' + "".join(catrow(i, *c) for i, c in enumerate(CATS)) + '''        </table></div>
        <p><button class="btn main" type="button">New collection</button> <a class="btn" href="#market">Add a collection from the marketplace</a></p>
      </div>
      <div class="split3"><div class="col">
      <div class="blk box dense">
        <h2>Edit collection: Teleports</h2>
        <form class="form" onsubmit="event.preventDefault()">
          <div class="fgrid">''' + F("Name", I("Teleports")) + F("Description", I("Step in, come out somewhere else.")) + '''</div>
          <label class="chk"><input type="checkbox" checked> Visible to guests</label>
          <div class="fgrid">''' + F("Publish on", I("", t="date")) + F("Unpublish on", I("", t="date")) + '''<label class="chk"><input type="checkbox"> Repeat every year</label></div>
          <p class="hint">Leave the dates empty to keep it always on. Use them for seasons: it shows and hides by itself.</p>
          <div class="fgrid">''' + F("Set every price to", I("25", t="number")) + '''<button class="btn" type="button">Apply</button></div>
          <div class="row"><button class="btn main" type="submit">Save collection</button></div>
        </form>
        <div class="tbl"><table><tr><th>Order</th><th></th><th>Furniture</th><th>Version</th><th>Schema</th><th class="num">Price</th><th></th></tr>
''' + furow("tel", "Telephone booth", "teleports@telephone", "1.1", "1.2", 25) + furow("tel", "Red booth", "teleports@red-booth", "1.0", "1.0", 25) + furow("flag", "Door sign", "teleports@door-sign", "1.0", "1.0", 5) + '''        </table></div>
        <p><a class="btn main" href="#market">Add furniture from the marketplace</a> <button class="btn" type="button">Remove this collection from the catalog</button></p>
      </div>
      </div><div class="col">
      <div class="blk box dense"><h2>Updates (2)</h2>
        <dl class="kv"><div><dt>Telephone booth</dt><dd>1.1 to 1.2</dd></div><div><dt>Rooftop Pool</dt><dd>2.0 to 2.1</dd></div></dl>
        <p><button class="btn main" type="button">Update both</button></p></div>
      <div class="blk box dense"><h2>How it works</h2>
        <ul class="perms"><li>Guests see visible collections in the in-game catalog, in this order.</li><li>Each item keeps the version you pick until you update it.</li><li>Rooms and clothes are in <a href="#admin-publicrooms">Public rooms</a> and <a href="#admin-clothes">Clothes</a>.</li></ul></div>
      </div></div>
'''
