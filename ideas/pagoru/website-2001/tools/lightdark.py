import os
import sys
site = sys.argv[1]
T = os.path.dirname(os.path.abspath(__file__)) + "/"
rd = lambda f: open(T + f).read()
tpl = rd("lobby.tpl.html").replace("{{CSS}}", rd("lobby.css"))
OH_ABOUT = '''          <h3>About OpenHotel</h3>
          <p>OpenHotel is a chill-out space where you can hang out with your friends. Guests are represented in the hotel by a little pixel person you design yourself. Anyone can check in.</p>
          <p><a href="#">Go on a tour of the hotel</a> &gt;&gt;</p>'''
PP_ABOUT = '''          <h3>About Pixel Plaza</h3>
          <p>Pixel Plaza is a community hotel on the OpenHotel network, run by a few friends since 2025. Big public rooms, weekly events and a strict "be nice" rule.</p>
          <p><a href="#">Hotel rules</a> &gt;&gt; &nbsp; <a href="#">Meet the staff</a> &gt;&gt;</p>'''
OH_BRAND = '          <img class="logo" src="assets/oh/logo.png" width="110" height="86" alt="OpenHotel">'
PP_BRAND = '          <div class="brand"><img src="assets/oh/icon-console-off.png" width="15" height="23" alt=""><div><b>Pixel Plaza</b><span>a hotel on the OpenHotel network</span></div></div>'
acts = lambda w, a, b=None: f'          <p>{w}</p>\n          <a class="btn main" href="#">{a}</a>\n' + (f'          <a class="btn" href="#">{b}</a>\n' if b else '')
V = {
  "retro-lobby": dict(ROOM="assets/oh/room-lobby-door.png", BRAND=OH_BRAND, ABOUT=OH_ABOUT, NEWS_TITLE="Hotel news", FOOT_NOTE="",
                      ACTIONS=acts("Welcome to OpenHotel", "Check in"), AUTH=rd("login.html")),
  "retro-lobby-in": dict(ROOM="assets/oh/room-lobby-door.png", BRAND=OH_BRAND, ABOUT=OH_ABOUT, NEWS_TITLE="Hotel news", FOOT_NOTE="",
                      ACTIONS=acts("Welcome back, Nightowl", "Enter hotel"), AUTH=rd("account.html")),
}
PP = dict(ROOM="assets/oh/room-plaza-door.png", BRAND=PP_BRAND, ABOUT=PP_ABOUT, NEWS_TITLE="Pixel Plaza news",
          FOOT_NOTE="    <p>Pixel Plaza is run by its own staff, not by the OpenHotel team. Accounts are handled by OpenHotel.</p>\n")
V["retro-hotel"] = dict(PP, ACTIONS=acts("Welcome to Pixel Plaza", "Check in"), AUTH=rd("login-hotel.html"))
V["retro-hotel-in"] = dict(PP, ACTIONS=acts("Welcome back, Nightowl", "Enter Pixel Plaza"), AUTH=rd("account-hotel.html"))
for key, vals in V.items():
    for theme in ("light", "dark"):
        h = tpl.replace("{{THEME}}", theme)
        for k, v in vals.items():
            assert h.count("{{%s}}" % k) == 1, k
            h = h.replace("{{%s}}" % k, v if k in ("FOOT_NOTE", "ACTIONS", "AUTH") else v)
        h = h.replace("{{BRAND}}\n", "")
        assert "{{" not in h, key
        open(f"{site}/{key}-{theme}.html", "w").write(h)
print("ok")
