# Hotel admin box + page, network box + page. Exec'd by subpages.py after pages_assets.py.
def box(title, inner, cls="blk box dense"): return f'      <div class="{cls}">\n        <h2>{title}</h2>\n{inner}\n      </div>\n'
def TBL(h, rows, num=()):
    return ('<div class="tbl"><table><tr>' + "".join(f'<th{" class=\"num\"" if i in num else ""}>{x}</th>' for i, x in enumerate(h)) + "</tr>"
            + "".join("<tr>" + "".join(f'<td{" class=\"num\"" if i in num else ""}>{c}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows) + "</table></div>")
BTN = lambda t, main=False: f'<button class="btn{" main" if main else ""}" type="button">{t}</button>'
KV = lambda rows: '<dl class="kv">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows) + "</dl>"

# ---- boxes at the bottom of My account ----
admin_box = box("Manage this hotel", f'''        <p class="hint">You are an admin of <select class="in sel-s" aria-label="Hotel"><option>Sunset Plaza</option><option>Pixel Inn</option></select></p>
        {KV([("Accounts", "1,842"), ("Online now", "312"), ("Rooms", "640"), ("Credits in circulation", "5.6M PXP"), ("Open reports", "<b>3</b>"), ("Asset updates", "<b>2</b>")])}
        <form class="form" onsubmit="event.preventDefault()"><label class="chk"><input type="checkbox"> Closed to new registrations</label>
          <span class="hint">Guests who already have an account can still enter. New accounts can't connect to this hotel.</span><div class="row"><button class="btn" type="submit">Save</button></div></form>
        <p><a class="btn main" href="#admin">Open hotel admin</a> <a class="btn" href="#library">Asset library</a></p>''')
network_box = box("OpenHotel network", f'''        <p class="hint">Only the main hotel sees this.</p>
        {KV([("Hotels", "128 (96 public)"), ("Online now", "4,210"), ("Hotels waiting for review", "<b>2</b>"), ("Exchange paused", "none")])}
        <p><a class="btn main" href="#network">Manage the network</a></p>''')
account = account + admin_box + network_box

# ---- hotel admin page ----
admin = box("Hotel admin · Sunset Plaza", f'''        <p class="hint">Every section below is for this hotel only. <a href="#library">Asset library</a> · <a href="#hotels">My hotels</a></p>
        {KV([("Accounts", "1,842"), ("Online now", "312"), ("Rooms", "640"), ("Chat messages 24h", "48.2k"), ("Credits created / destroyed 24h", "82k / 61k"), ("Purchases 24h", "1,204")])}''') + box("Registration", f'''        <form class="form" onsubmit="event.preventDefault()"><label class="chk"><input type="checkbox"> Closed to new registrations</label>
          <label>Message shown to new guests<input class="in" value="We are full for now. Come back soon!"></label>
          <label class="chk"><input type="checkbox" checked> Guests need a verified email</label><div class="row"><button class="btn main" type="submit">Save</button></div></form>''') + box("Accounts (1,842)", f'''        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search a name" aria-label="Search"><select class="in" aria-label="Filter"><option>Everyone</option><option>Online</option><option>Staff</option><option>New this week</option></select></form>
        ''' + TBL(["Name", "Role", "Since", "Last seen", "Credits", ""], [
    ["Mintleaf", "Guest", "Aug 2026", "Online", "4,800", BTN("Mute") + " " + BTN("Block")],
    ["Captain_K", "Moderator", "Aug 2026", "Online", "950", BTN("Role") + " " + BTN("Block")],
    ["Pebbles", "Guest", "Oct 2026", "2 h ago", "120", BTN("Mute") + " " + BTN("Block")],
    ["Sparrow", "Guest", "Nov 2026", "Yesterday", "40", BTN("Mute") + " " + BTN("Block")]], (4,)) + '<div class="pager"><span class="hint">1-4 of 1,842</span><span><a href="#admin">Next</a> &gt;&gt;</span></div>') + box("Blocked (6)", TBL(
    ["Name", "Reason", "By", "Date", ""], [["Trollface", "Spam in 3 rooms", "Captain_K", "20 Nov", BTN("Unblock")], ["xX_cheat", "Credit exploit", "Nightowl", "14 Nov", BTN("Unblock")], ["Rude99", "Harassment", "Captain_K", "09 Nov", BTN("Unblock")]]) + '<div class="pager"><span class="hint">3 of 6</span><span><a href="#admin">All</a> &gt;&gt;</span></div>') + box("Rooms (640)", TBL(
    ["Room", "Owner", "Now", "Messages 24h", ""], [["The Atrium", "Public", "86", "9.4k", BTN("Close")], ["Mint garden", "Mintleaf", "12", "1.1k", BTN("Close") + " " + BTN("Delete")], ["Pebbles' pad", "Pebbles", "0", "0", BTN("Delete")]], (2, 3))) + box("Chat and moderation", TBL(
    ["Reported message", "Room", "From", "Reports", ""], [["“...buy credits at my site...”", "The Atrium", "Trollface", "5", BTN("Delete", True) + " " + BTN("Ignore")], ["“you suck”", "Mint garden", "Rude99", "2", BTN("Mute") + " " + BTN("Ignore")]], (3,)) + '''
        <p class="hint">Blocked words: 42 · Auto-muted today: 7 · <a href="#admin">Edit the word list</a></p>''') + box("Credits and purchases", KV([("Credits in circulation", "5.6M PXP"), ("Created 24h", "82,000"), ("Destroyed 24h", "61,000"), ("Listed on the exchange", "Yes, price 0.420 OHC")]) + TBL(
    ["When", "Who", "Bought", "Price"], [["15:20", "Mintleaf", "Telephone booth", "25 PXP"], ["15:02", "Pebbles", "Pirate flag", "10 PXP"], ["14:48", "Wanda", "Striped shirt", "free"]], (3,)) + '<div class="pager"><span class="hint">Last 3 of 1,204 today</span><span><a href="#admin">All</a> &gt;&gt;</span></div>') + box("Asset library applied", KV([("Public rooms", "3"), ("Furniture", "128"), ("Clothes", "64"), ("Updates waiting", "<b>2</b>")]) + '<p><a class="btn main" href="#library">Open the asset library</a> <a class="btn" href="#market">Marketplace</a></p>')

# ---- network page (main hotel only) ----
network = box("OpenHotel network", f'''        <p class="hint">Hotels connected to this main hotel. Only the main hotel owners see this page.</p>
        {KV([("Hotels", "128"), ("Public", "96"), ("Online now", "4,210"), ("Accounts", "1.2M"), ("Waiting for review", "<b>2</b>")])}
        <form class="form" onsubmit="event.preventDefault()"><label class="chk"><input type="checkbox" checked> New hotels can be created</label>
          <label class="chk"><input type="checkbox"> Pause the whole credit exchange</label>
          <label>Oldest hotel version allowed<input class="in" value="0.150.0" style="max-width:120px"></label><div class="row"><button class="btn main" type="submit">Save</button></div></form>''') + box("Hotels", '''
        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search a hotel" aria-label="Search"><select class="in" aria-label="Filter"><option>All</option><option>Waiting for review</option><option>Suspended</option><option>Old version</option></select></form>
        ''' + TBL(["Hotel", "Owner", "Version", "Accounts", "Online", "Exchange", "State", ""], [
    ["OpenHotel", "Nightowl", "0.156.0", "1.2M", "1,820", "OHC", '<span class="badge on">Main</span>', ""],
    ["Pixel Plaza", "Mintleaf", "0.156.0", "86k", "312", "PXP", '<span class="badge on">Live</span>', BTN("Pause trading") + " " + BTN("Suspend")],
    ["Neon Docks", "Pebbles", "0.152.1", "9k", "74", "NDK", '<span class="badge on">Live</span>', BTN("Pause trading") + " " + BTN("Suspend")],
    ["Moonbase Inn", "Lumen", "0.149.0", "2k", "11", "MBI", '<span class="badge">Old version</span>', BTN("Pause trading") + " " + BTN("Suspend")],
    ["Hotel Nova", "Sparrow", "0.156.0", "0", "0", "NOV", '<span class="badge">Review</span>', BTN("Approve", True) + " " + BTN("Reject")]], (3, 4)) + '<div class="pager"><span class="hint">1-5 of 128</span><span><a href="#network">Next</a> &gt;&gt;</span></div>') + box("Credit reports", TBL(
    ["Hotel", "Last report", "Created 24h", "Destroyed 24h", "Check"], [["Pixel Plaza", "Today 00:05", "82,000", "61,000", '<span class="badge on">OK</span>'], ["Neon Docks", "Today 00:07", "3,100", "2,900", '<span class="badge on">OK</span>'], ["Moonbase Inn", "3 days ago", "-", "-", '<span class="badge">Paused</span>']], (2, 3)))
