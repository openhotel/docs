# 2001 subpages + link wiring for all 2001 pages. Run after lightdark.py.
import re, sys, glob, os
site = sys.argv[1]; T = "/tmp/claude-0/oh/"
rd = lambda f: open(T + f).read()
tpl = rd("lobby.tpl.html")
head = tpl[:tpl.index("<body>")].replace("{{CSS}}", rd("lobby.css") + rd("sub.css"))
foot = tpl[tpl.index('  <footer class="foot">'):].replace("{{FOOT_NOTE}}", "")
soc = re.search(r'      <section class="soc">.*?</section>\n', tpl, re.S).group(0)
NEWS = [("booths","21 Nov 2026","Telephone booths are here","Step into a booth and come out in another room, or in another hotel on the network."),
        ("flag","14 Nov 2026","Pirate week","Hoist the flag in your room. The best decorated rooms win a spot on the front page."),
        ("disco","09 Nov 2026","Disco Hall reopens","New lights, a bigger dance floor and a DJ booth anyone can book for an hour."),
        ("server","05 Nov 2026","Hotel server 1.5 beta","Run it next to 1.4 and tell us what breaks. Hotel owners first, please."),
        ("atrium","02 Nov 2026","The Atrium is open","A new public room with a fountain and two staircases. Come and see it before it gets busy."),
        ("pool","30 Oct 2026","Rooftop pool party","Saturday at 20:00. Bring a towel and keep the splashing in the pool.")]

GO = '<script>document.addEventListener("click",function(e){var b=e.target.closest("[data-sub-btn]");if(b)b.closest(".subnews").hidden=true});document.addEventListener("click",(e)=>{const r=e.target.closest("tr.go");if(r&&!e.target.closest("a,button,input,select,label,summary")){const a=r.querySelector("a");if(a)location.href=a.href}})</script>\n'
import re as _re
FSKIP = ("Test results", "Home sections", "Custom boxes", "What each kind needs", "Overview", "Needs attention", "Numbers", "Updates", "Who sends", "Email templates", "Latest trades", "Order book")
def addfind(b):
    b = b.replace('<input class="in" type="search"', '<input data-filter class="in" type="search"')
    out, pos = "", 0
    for m in _re.finditer('<div class="tbl">', b):
        h2 = b.rfind("<h2>", 0, m.start())
        title = _re.sub("<.*?>|\\s*\\(.*", "", b[h2 + 4:b.find("</h2>", h2)]) if h2 >= 0 else ""
        seg = b[h2:m.start()] if h2 >= 0 else ""
        if "mfind" in seg or any(title.startswith(k) for k in FSKIP) or b[m.start():b.find("</table>", m.start())].count("<tr") < 3:
            continue
        out += b[pos:m.start()] + f'<form class="mfind" onsubmit="event.preventDefault()"><input data-filter class="in" type="search" placeholder="Search {title.lower()}" aria-label="Search {title.lower()}"></form>'
        pos = m.start()
    return out + b[pos:]
FIND = '<script>document.addEventListener("input",function(e){var i=e.target;if(!i.hasAttribute||!i.hasAttribute("data-filter"))return;var t=i.closest(".friends");if(!t){t=i.closest("form").nextElementSibling;while(t&&!t.classList.contains("tbl")&&t.tagName!="UL")t=t.nextElementSibling}if(!t)return;var q=i.value.toLowerCase();t.querySelectorAll("tr,li").forEach(function(r){if(r.querySelector("th"))return;r.hidden=!!q&&r.textContent.toLowerCase().indexOf(q)<0})})</script>\n'
def page(title, tab, logged, body):
    extra = ''
    if '<!--SIDE-->' in body:
        i, j = body.index('<!--SIDE-->'), body.index('<!--/SIDE-->')
        extra, body = body[i + 11:j], body[:i] + body[j + 12:]
    if 'class="blk subnav"' in body or title in ("Friends",): body = addfind(body)
    tabs = [("Home","home"),("News","news")] + ([("Friends","friends"),("Exchange","exchange"),("Marketplace","market"),("My account","account"),("Connections","connections"),("My hotels","hotels")] if logged else [("Register","register")])
    nav = "".join(f'<a class="btn{" main" if k == tab else ""}" href="#{k}">{n}</a>' for n, k in tabs)
    side = '      <div class="blk">\n' + (rd("account.html") if logged else rd("login.html")) + '      </div>\n' + extra + (rd("sidebar-in.html") if logged else "") + '      <div class="blk">\n' + soc + '      </div>\n'
    return (head.replace("<title>OpenHotel 2001</title>", f"<title>{title} · OpenHotel</title>") + '<body>\n<div class="page">\n'
      + '  <div class="grid2">\n    <main class="mainc">\n'
      + '      <header class="blk top"><div class="hero mini"><img class="room" src="assets/oh/room-lobby-door.png" width="396" height="300" alt=""><a class="logo" href="#home"><img src="assets/oh/logo.png" width="110" height="86" alt="OpenHotel home"></a></div>'
      + f'<nav class="actions" aria-label="Site">{nav}</nav></header>\n' + body + '    </main>\n    <aside class="side">\n' + side + '    </aside>\n  </div>\n' + foot.replace('</body>', GO + FIND + '</body>'))

SUBBOX = open(T + "sub-news.html").read()
news_list = '      <div class="blk box">\n        <h2>Hotel news</h2>\n        <ul class="newslist">\n' + "".join(
    f'          <li><img src="assets/oh/news-{i}.png" width="64" height="64" alt=""><div><time>{d}</time><b>{t}</b><p>{x}</p><a href="#post">Read more</a> &gt;&gt;</div></li>\n' for i, d, t, x in NEWS
  ) + '        </ul>\n        <div class="pager"><span class="hint">Page 1 of 4</span><a href="#news">Older news</a> &gt;&gt;</div>\n      </div>\n'

article = '''      <div class="blk box article">
        <p class="crumb"><a href="#news">Hotel news</a> &gt; Telephone booths are here</p>
        <h2>Telephone booths are here</h2>
        <p><time>21 Nov 2026</time> · by the hotel staff</p>
        <div class="pic"><img src="assets/oh/furni-telephone.png" width="48" height="98" alt="Telephone booth"></div>
        <p class="lead">Step into a booth and come out in another room, or in another hotel on the network.</p>
        <p>Telephone booths are in the catalog from today. Put one in your room, give it a name and link it to any other booth you own. Walk in, wait for the light, and you are there.</p>
        <p>Booths also work between hotels. If a hotel on the network has a public booth, you can dial it from yours and arrive with your avatar, your friends list and your badges. Your account comes with you.</p>
        <h3>How to get one</h3>
        <p>Open the catalog in the hotel and look under Teleports. The first booth is free for every guest until the end of the month.</p>
        <p><a href="#news">Back to news</a> &lt;&lt;</p>
      </div>
      <div class="blk box">
        <h2>More news</h2>
        <ul class="newslist">
''' + "".join(f'          <li><img src="assets/oh/news-{i}.png" width="64" height="64" alt=""><div><time>{d}</time><b>{t}</b><a href="#post">Read more</a> &gt;&gt;</div></li>\n' for i, d, t, x in NEWS[1:3]) + '''        </ul>
      </div>
'''


STARS = '<div class="rate" role="radiogroup" aria-label="Rate this post">' + "".join(f'<input type="radio" name="r" id="r{i}" value="{i}"><label for="r{i}" title="{i} stars">★</label>' for i in range(5, 0, -1)) + '</div>'
inter = f"""      <div class="blk box stats">
        <div class="score"><span class="stars" aria-label="4.2 out of 5">★★★★<span class="dim">★</span></span> <b>4.2</b> <span class="hint">from 86 votes</span></div>
        <div class="nums"><span><b>1,204</b> views</span><span><b>12</b> comments</span></div>
        <div class="you"><span class="hint">Your rating</span>{STARS}</div>
      </div>
"""
COMMENTS = [("a","Mintleaf","2 hours ago","Already linked my room to the Lobby booth. Works great!",5),
            ("c","Captain_K","3 hours ago","Can we pick the colour of the booth? Red would be nice.",3),
            ("b","Pebbles","5 hours ago","Dialled Pixel Plaza from here and kept my friends list. Magic.",8),
            ("e","nightbus","yesterday","Free until the end of the month, so get one now.",2),
            ("d","Lumen","yesterday","First!",0)]
def comments(logged):
    li = "".join(f'          <li><img src="assets/oh/av-idle-{a}.png" width="21" height="66" alt=""><div><b>{n}</b> <time>{t}</time><p>{x}</p></div></li>\n' for a, n, t, x, k in COMMENTS)
    form = ('        <form class="cform" onsubmit="event.preventDefault()"><label class="sr" for="c1">Your comment</label><textarea id="c1" class="in" rows="3" placeholder="Say something nice"></textarea><button class="btn main" type="submit">Post comment</button></form>\n'
            if logged else '        <p class="hint"><a href="#home">Log in</a> or <a href="#register">register</a> to comment.</p>\n')
    return ('      <div class="blk box comments">\n        <h2>Comments (12)</h2>\n' + form + '        <ul>\n' + li
            + '        </ul>\n        <p class="all"><a href="#post">Show 7 more</a> &gt;&gt;</p>\n      </div>\n')
MN = '      <div class="blk box">\n        <h2>More news</h2>'
def post(logged):
    assert MN in article
    return ('      <div class="split3">\n        <div class="col">\n' + article.replace(MN, inter + MN, 1) + '        </div>\n        <div class="col">\n'
            + comments(logged) + '        </div>\n      </div>\n')
register = '''<div class="two wide"><div>
      <div class="blk box">
        <h2>Register</h2>
        <p>One account for OpenHotel and every hotel on the network. It takes a minute.</p>
        <form class="form" onsubmit="event.preventDefault()">
          <label>Email<input class="in" type="email" autocomplete="email"></label>
          <label>Username<input class="in" type="text" autocomplete="username"></label>
          <span class="hint">3 to 16 letters, numbers or _. Other guests see this name.</span>
          <label>Password<input class="in" type="password" autocomplete="new-password"></label>
          <label>Repeat password<input class="in" type="password" autocomplete="new-password"></label>
          <label>Language<select class="in"><option>English</option><option>Español</option><option>Deutsch</option></select></label>
          <label class="chk"><input type="checkbox" required> I accept the <a href="#">Terms of Service</a> and the <a href="#">EULA</a></label>
          <label class="chk"><input type="checkbox"> Send me the news by email (optional, news only, never spam)</label>
          <div class="row"><button class="btn main" type="submit">Register</button><span>Already registered? <a href="#home">Log in</a></span></div>
        </form>
      </div>
      </div><div>
      <div class="blk box">
        <h2>What happens next</h2>
        <ol class="steps">
          <li><b>Register.</b> Fill the form. One account works in every hotel.</li>
          <li><b>Check your email.</b> We send a link to confirm the address. It works for one hour. Look in spam if it doesn't come.</li>
          <li><b>Check in.</b> Open a hotel and make your avatar there. You can't change it on the website, but it shows here once you have one.</li>
          <li><b>Pick your hotels.</b> Join the main hotel or any community hotel with the same login.</li>
        </ol>
        <p class="hint">Free. No credit card. Credits come from playing. You can turn on 2FA and delete your account at any time in My account.</p>
      </div>
      </div></div>
'''
forgot = '''      <div class="blk box">
        <h2>Forgot your password?</h2>
        <p>Type the email you registered with. If it has an account, we send you a link to choose a new password. The link works for one hour.</p>
        <form class="form" onsubmit="event.preventDefault()">
          <label>Email<input class="in" type="email" autocomplete="email"></label>
          <div class="row"><button class="btn main" type="submit">Send me a link</button><a href="#home">Go back</a></div>
        </form>
      </div>
      <div class="blk box">
        <h2>No email?</h2>
        <p>Check your spam folder first. Still nothing after ten minutes? Ask on <a href="https://discord.gg/qBZfPdNWUj" target="_blank" rel="noopener">Discord</a> and a staff member will help.</p>
      </div>
'''
exec(open(T + "pages_acct.py").read())
exec(open(T + "pages_social.py").read())
exec(open(T + "pages_assets.py").read())
exec(open(T + "pages_admin.py").read())

PAGES = {  # key: (title, tab, logged, body)
  "retro-news": ("News", "news", False, news_list), "retro-news-in": ("News", "news", True, SUBBOX + news_list),
  "retro-post": ("Telephone booths are here", "news", False, post(False)), "retro-post-in": ("Telephone booths are here", "news", True, SUBBOX + post(True)),
  "retro-register": ("Register", "register", False, register), "retro-forgot": ("Forgot password", "", False, forgot),
  "retro-account": ("My account", "account", True, account), "retro-my-hotels": ("My hotels", "hotels", True, hotels),
  "retro-connections": ("Connected hotels", "connections", True, connections),
  "retro-friends": ("Friends", "friends", True, friends_body), "retro-exchange": ("Credit exchange", "exchange", True, exchange_body),
  "retro-assets": ("Catalog", "", True, library), "retro-market": ("Marketplace", "market", True, market), "retro-create": ("Create an asset", "market", True, create), "retro-create-sheet": ("Spritesheet", "market", True, create_sheet), "retro-create-furniture": ("Furniture", "market", True, create_furniture), "retro-create-clothes": ("Clothes", "market", True, create_clothes), "retro-create-room": ("Room", "market", True, create_room),
  "retro-item": ("Telephone booth", "market", True, item), "retro-collection": ("Beach set", "market", True, collection), 
  "retro-link": ("OpenHotel Link", "market", True, CN("link") + link), "retro-mine-collections": ("Your collections", "market", True, mine_collections), "retro-coin": ("Pixel Plaza · PXP", "exchange", True, coin_body),
  "retro-admin": ("Manage OpenHotel", "", True, admin), "retro-admin-registration": ("Registration", "", True, admin_registration), "retro-admin-accounts": ("Accounts", "", True, admin_accounts),
  "retro-admin-blocked": ("Blocked", "", True, admin_blocked), "retro-admin-rooms": ("Rooms", "", True, admin_rooms), "retro-admin-moderation": ("Moderation", "", True, admin_moderation),
  "retro-admin-credits": ("Credits", "", True, admin_credits), "retro-admin-publicrooms": ("Public rooms", "", True, admin_publicrooms), "retro-admin-clothes": ("Clothes", "", True, admin_clothes),
  "retro-network": ("Network admin", "", True, network), "retro-network-hotels": ("Hotels", "", True, network_hotels), "retro-network-news": ("News", "", True, network_news), "retro-admin-news": ("News", "", True, admin_news), "retro-admin-website": ("Website", "", True, admin_website), "retro-admin-connection": ("Connection", "", True, admin_connection), "retro-network-accounts": ("Accounts", "", True, network_accounts), "retro-network-blocked": ("Blocked", "", True, network_blocked), "retro-network-emails": ("Emails", "", True, network_emails), "retro-network-credits": ("Credit reports", "", True, network_credits), "retro-network-settings": ("Settings", "", True, network_settings),
}
for key, (title, tab, logged, body) in PAGES.items():
    h = page(title, tab, logged, body)
    for theme in ("light", "dark"):
        open(f"{site}/{key}-{theme}.html", "w").write(h.replace("{{THEME}}", theme))

# wire links in all 2001 pages
def wire(path, theme, logged, community):
    s = open(path).read()
    sfx = "-in" if logged else ""
    m = {"#home": f"retro-lobby{sfx}", "#news": f"retro-news{sfx}", "#post": f"retro-post{sfx}", "#register": "retro-register",
         "#account": "retro-account", "#hotels": "retro-my-hotels", "#connections": "retro-connections", "#friends": "retro-friends", "#exchange": "retro-exchange", "#market": "retro-market", "#create": "retro-create", "#library": "retro-assets", "#item": "retro-item", "#collection": "retro-collection", "#mine": "retro-create", "#link": "retro-link", "#coin": "retro-coin", "#admin": "retro-admin", "#network": "retro-network"}
    for k in PAGES: m.setdefault("#" + k[6:], k)
    for k, v in m.items(): s = s.replace(f'href="{k}"', f'href="{v}-{theme}.html"')
    txt = {"Register for free": "retro-register", "Register on OpenHotel": "retro-register", "Forgot password?": "retro-forgot",
           "Account settings": "retro-account", "OpenHotel account": "retro-account", "My hotels (2)": "retro-my-hotels", "Connected hotels": "retro-connections", "Friends online (4)": "retro-friends",
           "All news": f"retro-news{sfx}", "Read more": f"retro-post{sfx}", "Create assets": "retro-create", "Log out": "retro-lobby", "Get the code": None}
    if community:  # community pages link news inside the hotel site; keep its own home
        txt.update({"All news": None, "Read more": None, "Log out": "retro-hotel"})
    for t, v in txt.items():
        if v: s = s.replace(f'<a href="#">{t}</a>', f'<a href="{v}-{theme}.html">{t}</a>')
    s = s.replace('<a href="#">Get the code</a>', '<a href="https://github.com/openhotel" target="_blank" rel="noopener">Get the code</a>')
    open(path, "w").write(s)
for f in glob.glob(f"{site}/retro-*-light.html") + glob.glob(f"{site}/retro-*-dark.html"):
    n = os.path.basename(f); theme = "light" if n.endswith("-light.html") else "dark"; key = n.rsplit("-", 1)[0]
    if key in ("retro-orange", "retro-portal"): continue
    logged = key.endswith("-in") or (key in PAGES and PAGES[key][2])
    wire(f, theme, logged, key.startswith("retro-hotel"))
print("ok")
