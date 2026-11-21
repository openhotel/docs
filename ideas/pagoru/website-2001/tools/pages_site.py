# Manage hotel: Website and Connection tabs. Exec'd by pages_admin.py.
CHK = lambda on=True, lab="": f'<label class="chk"><input type="checkbox"{" checked" if on else ""} aria-label="{lab or "Shown"}"></label>'
UD = '<button class="btn" type="button" aria-label="Move up">↑</button><button class="btn" type="button" aria-label="Move down">↓</button>'
PLACE = lambda cur: '<select class="in" aria-label="Column">' + "".join(f'<option{" selected" if o == cur else ""}>{o}</option>' for o in ("Left", "Middle", "Right")) + '</select>'
SECTIONS = [("Hotel picture and enter button", "Left", True, "always"), ("About the hotel", "Left", True, ""), ("Hotels online now", "Left", True, ""), ("Marketplace and Credit exchange boxes", "Left", True, ""),
            ("Hotel news", "Middle", True, ""), ("Want more credits", "Middle", True, ""), ("New in the catalog", "Middle", True, ""),
            ("Friends online", "Right", True, "guests"), ("In this hotel (rooms)", "Right", True, ""), ("OpenHotel network numbers", "Right", True, ""), ("Find us on (socials)", "Right", True, "")]
def secrow(n, col, on, note):
    box = '<input type="checkbox" checked disabled aria-label="Always shown">' if note == "always" else f'<input type="checkbox"{" checked" if on else ""} aria-label="Show {n}">'
    return f'<tr><td class="ord">{UD}</td><td>{n}{" <span class=hint>(always)</span>" if note == "always" else ""}</td><td>{PLACE(col)}</td><td>{box}</td></tr>'
CUSTOM = [("Summer party", "Image + text + button", "Middle", "Shown", "01 Jun to 15 Sep, every year"), ("Join our Discord", "Text + button", "Right", "Shown", "Always"), ("Rules", "Links", "Left", "Hidden", "Always")]
def cbrow(t, ty, pl, st, d):
    return f'<tr class="go"><td class="ord">{UD}</td><td><a href="#admin-website"><b>{t}</b></a><br><span class="hint">{ty}</span></td><td>{pl}</td><td><span class="badge{" on" if st == "Shown" else ""}">{st}</span></td><td>{d}</td></tr>'
SOC = [("GitHub", "https://github.com/openhotel", True), ("Discord", "https://discord.gg/openhotel", True), ("Bluesky", "https://bsky.app/profile/openhotel.club", True), ("YouTube", "", False), ("X / Twitter", "", False), ("Instagram", "", False), ("TikTok", "", False), ("Twitch", "", False), ("Mastodon", "", False)]
def socrow(n, u, on): return f'<tr><td><b>{n}</b></td><td><input class="in" type="url" value="{u}" placeholder="https://" aria-label="{n} link"></td><td><input type="checkbox"{" checked" if on else ""} aria-label="Show {n}"></td></tr>'
admin_website = AN("admin-website") + '<div class="two wide"><div>' + box("Home sections", '<p class="hint">Choose what the home page shows and where. Drag with the arrows.</p><div class="tbl"><table><tr><th></th><th>Section</th><th>Column</th><th>Shown</th></tr>' + "".join(secrow(*s) for s in SECTIONS) + '</table></div><p><button class="btn main" type="button">Save</button> <a class="btn" href="#lobby-in">Preview home</a></p>') + box("Custom boxes (3)", '<p class="hint">Your own boxes on the home page: text, a picture, a button or a list of links.</p><div class="tbl"><table><tr><th></th><th>Box</th><th>Place</th><th>State</th><th>When</th></tr>' + "".join(cbrow(*c) for c in CUSTOM) + '</table></div><p><button class="btn" type="button">New box</button></p>') + box("Socials", '<p class="hint">Shown in the right bar and the footer. Empty ones are hidden.</p><div class="tbl"><table><tr><th>Network</th><th>Link</th><th>Shown</th></tr>' + "".join(socrow(*s) for s in SOC) + '</table></div><p><button class="btn" type="button">Add another link</button> <button class="btn main" type="button">Save</button></p>') + '</div><div>' + box("Edit box: Summer party", '''        <form class="form" onsubmit="event.preventDefault()">
          <label>Title<input class="in" value="Summer party"></label>
          <label>Kind<select class="in"><option>Image + text + button</option><option>Text + button</option><option>Image</option><option>Links</option></select></label>
          <label>Picture<input type="file" accept="image/png,image/jpeg" aria-label="Picture"></label><span class="hint">Shown as it is, up to 320 px wide. Pixel art stays sharp.</span>
          <label>Text<textarea class="in tx" rows="4">Saturday at 20:00 on the roof. Bring a towel.</textarea></label>
          <label>Button text<input class="in" value="Join the party"></label>
          <label>Button link<input class="in" type="url" value="https://openhotel.club/party"></label>
          <label>Place<select class="in"><option>Left</option><option selected>Middle</option><option>Right</option></select></label>
          <label>Show from<input class="in" type="date" style="max-width:10em"></label>
          <label>Hide on<input class="in" type="date" style="max-width:10em"></label>
          <label class="chk"><input type="checkbox" checked> Repeat every year</label>
          <label class="chk"><input type="checkbox" checked> Shown</label>
          <div class="row"><button class="btn main" type="submit">Save box</button> <button class="btn danger-btn" type="button">Delete</button></div>
        </form>''') + box("Hotel page", '''        <form class="form" onsubmit="event.preventDefault()">
          <label>Name<input class="in" value="OpenHotel" disabled></label><span class="hint">Set when the hotel was created in My hotels.</span>
          <label>About<textarea class="in tx" rows="4">OpenHotel is a chill-out space where you can hang out with your friends.</textarea></label>
          <label>Picture<input type="file" accept="image/png"></label><span class="hint">160 x 72.</span>
          <label>Icon<input type="file" accept="image/png"></label><span class="hint">24 x 24 at most.</span>
          <label>Footer note<input class="in" placeholder="Shown under the footer"></label>
          <label>Default language<select class="in"><option>English</option><option>Español</option></select></label>
          <div class="row"><button class="btn main" type="submit">Save</button></div>
        </form>''') + '</div></div>'
admin_connection = AN("admin-connection") + '<div class="two wide"><div>' + box("Network connection", '''        <p><span class="badge on">Connected</span> to the OpenHotel network · last seen 12 s ago</p>
        <p class="hint">Public hotels show on the Hotels online list. Credits, friends and the exchange need this connection.</p>
        <form class="form" onsubmit="event.preventDefault()"><label class="chk"><input type="checkbox" checked> Connect on start and reconnect by itself</label>
          <label class="chk"><input type="checkbox" checked> Public: show this hotel on the network list</label>
          <div class="row"><button class="btn main" type="button">Try to connect now</button> <button class="btn" type="button">Disconnect</button> <button class="btn main" type="submit">Save</button></div></form>''' + TBL(["When", "Result"], [["17:41", '<span class="badge on">Connected</span>'], ["17:40", "Ping 38 ms"], ["16:02", '<span class="badge">Lost, retried in 5 s</span>'], ["16:02", '<span class="badge on">Connected</span>']]) + PAGER("4 of 120", "admin-connection")) + box("Licence", '''        <p><span class="badge on">Valid</span> <code>ohl_9f3K…sD</code> · checked 2 min ago</p>
        <form class="form" onsubmit="event.preventDefault()"><label>Set a new licence<input class="in" type="password" placeholder="Paste the licence" autocomplete="off"></label>
          <span class="hint">The licence goes in the hotel server's config (proposal: <code>licence</code> in its config file or the OH_LICENCE variable). This page saves it there. A licence is shown once, when it is made in <a href="#hotels">My hotels</a>; lost it? Remake it there and paste the new one.</span>
          <div class="row"><button class="btn main" type="submit">Save licence</button> <button class="btn" type="button">Check it</button></div></form>''') + '</div><div>' + box("Addresses", '''        <form class="form" onsubmit="event.preventDefault()">
          <label>Client (where guests play)<input class="in" type="url" value="https://play.openhotel.club"></label>
          <label>Website<input class="in" type="url" value="https://openhotel.club"></label>
          <label>Assets (static)<input class="in" type="url" value="https://static.openhotel.club"></label>
          <label>Allowed origins (one per line)<textarea class="in tx" rows="3">https://play.openhotel.club
https://openhotel.club</textarea></label>
          <label>Account login (auth)<input class="in" value="https://auth.openhotel.club" disabled></label>
          <label>Network (onet)<input class="in" value="https://onet.openhotel.club" disabled></label>
          <span class="hint">The last two are set by the network.</span>
          <div class="row"><button class="btn main" type="submit">Save</button> <button class="btn" type="button">Test addresses</button></div>
        </form>''') + box("Test results", TBL(["Address", "Result"], [["Client", '<span class="badge on">200 OK</span>'], ["Website", '<span class="badge on">200 OK</span>'], ["Assets", '<span class="badge on">200 OK</span>'], ["Auth", '<span class="badge on">200 OK</span>'], ["Network", '<span class="badge on">Connected</span>']])) + box("Versions", KV([("Hotel", "v0.156.0"), ("Schemas it runs", "1 to 4"), ("Network asks for", "0.150.0 or newer")])) + '</div></div>'
