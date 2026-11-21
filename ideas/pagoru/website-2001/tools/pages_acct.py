# My account, Connected hotels and My hotels bodies. Exec'd by subpages.py.
CAPTCHA = '''<div class="captcha"><label class="chk"><input type="checkbox"> I'm a person, not a bot</label><span class="hint">captcha</span></div>'''
OTP = '<label>6-digit code from your app<input class="in otp big" type="text" inputmode="numeric" autocomplete="one-time-code" pattern="[0-9]{6}" maxlength="6" placeholder="000000"></label>'

account = f'''      <div class="blk box">
        <h2>My account</h2>
        <div class="two">
          <div>
            <dl class="kv">
              <div><dt>Username</dt><dd>Nightowl</dd></div>
              <div><dt>Email</dt><dd>n******@*****.com</dd></div>
              <div><dt>Member since</dt><dd>Mar 2025</dd></div>
              <div><dt>Role</dt><dd>Hotel owner</dd></div>
            </dl>
          </div>
          <div class="avbox"><div class="av"><img src="assets/oh/av-wave-a.png" width="23" height="68" alt="Your avatar"></div><p class="hint">Your avatar as guests see it. You change it inside the hotel.</p></div>
        </div>
        <h3>Languages</h3>
        <ul class="pills"><li>English <button type="button" aria-label="Remove English">x</button></li><li>Español <button type="button" aria-label="Remove Español">x</button></li></ul>
        <div class="row" style="display:flex;gap:8px;max-width:340px"><select class="in"><option>Add a language</option><option>Deutsch</option><option>Français</option></select><button class="btn" type="button">Add</button></div>
      </div>
      <div class="blk box">
        <h2>Email news</h2>
        <form class="form" onsubmit="event.preventDefault()">
          <label class="chk"><input type="checkbox"> Send me the news by email (network and the hotels I joined)</label>
          <span class="hint">Off until you turn it on. News only, never spam. Hotels never see your email: the network sends it for them. Every email has an unsubscribe link. Account emails (verify, password, security) are always sent.</span>
          <div class="row"><button class="btn main" type="submit">Save</button></div>
        </form>
      </div>
      <div class="blk box tfa" data-state="off">
        <h2>Two-step login (2FA)</h2>
        <p class="demo hint">Preview: <button type="button" class="btn" data-set="off">2FA is off</button> <button type="button" class="btn" data-set="on">2FA is on</button></p>
        <div class="st st-off">
          <p><span class="badge">Off</span> Add a 6-digit code from an app like Aegis or Google Authenticator to your login.</p>
          <button class="btn main" type="button" data-go="enable">Turn on 2FA</button>
        </div>
        <form class="st st-enable form" onsubmit="event.preventDefault()">
          <p><b>1.</b> Scan this code with your app, or type the key by hand.</p>
          <div class="qrrow"><div class="qr" role="img" aria-label="QR code for your app">QR code</div><p class="hint">Key<br><code>JBSW Y3DP EHPK 3PXP</code></p></div>
          <p><b>2.</b> Prove you're not a bot.</p>
          {CAPTCHA}
          <p><b>3.</b> Type the code your app shows.</p>
          {OTP}
          <div class="row"><button class="btn main" type="submit" data-go="on">Turn on</button><button class="btn" type="button" data-go="off">Cancel</button></div>
        </form>
        <div class="st st-on">
          <p><span class="badge on">On</span> You need a code from your app every time you log in.</p>
          <button class="btn" type="button" data-go="disable">Turn off 2FA</button>
        </div>
        <form class="st st-disable form" onsubmit="event.preventDefault()">
          <p>To turn off 2FA, prove you're not a bot and type a code from your app.</p>
          {CAPTCHA}
          {OTP}
          <div class="row"><button class="btn main" type="submit" data-go="off">Turn off</button><button class="btn" type="button" data-go="on">Cancel</button></div>
        </form>
      </div>
      <div class="blk box">
        <h2>Delete account</h2>
        <p>Deletes your account, your avatar and your rooms in every hotel. This can't be undone.</p>
        <a class="btn danger-btn" href="#">Delete my account</a>
      </div>
<script>
document.querySelectorAll(".tfa").forEach((box) => {{
  const set = (s) => (box.dataset.state = s);
  box.addEventListener("click", (e) => {{
    const b = e.target.closest("[data-go],[data-set]");
    if (b) set(b.dataset.go || b.dataset.set);
  }});
}});
</script>
'''

def conn(thumb, icon, iw, ih, name, main, client, web, since, last, perms):
    pl = "".join(f"<li>{p}</li>" for p in perms)
    act = ('<p class="hint">This is the main hotel. Your OpenHotel account lives here, so you can\'t disconnect from it.</p>' if main else
           f'<details class="disc"><summary class="btn">Disconnect</summary><p>{name} loses access to your account. Your avatar and rooms there stay, but you need to connect again to enter.</p><button class="btn danger-btn" type="button">Yes, disconnect</button></details>')
    return f'''      <div class="blk box conn">
        <div class="hotel">
          <div class="thumb"><img src="assets/oh/hotel-thumb-{thumb}.png" width="160" height="72" alt=""></div>
          <div><h3><img class="fav" src="assets/oh/icon-{icon}.png" width="{iw}" height="{ih}" alt=""> {name} {'<span class="badge on">Main hotel</span>' if main else ''}</h3>
            <dl class="kv">
              <div><dt>Client</dt><dd><a href="#">{client}</a></dd></div>
              <div><dt>Website</dt><dd><a href="#">{web}</a></dd></div>
              <div><dt>Connected since</dt><dd>{since}</dd></div>
              <div><dt>Last login</dt><dd>{last}</dd></div>
            </dl>
          </div>
        </div>
        <h3>What {name} can see and do</h3>
        <ul class="perms">{pl}</ul>
        {act}
      </div>
'''
BASE = ["See your username, avatar and language", "Know when you are online in this hotel"]
connections = '''      <div class="blk box">
        <h2>Connected hotels</h2>
        <p>Every hotel you have entered with your OpenHotel account. A hotel only gets what is listed under it. Disconnect a hotel to take its access away.</p>
      </div>
''' + conn("main", "navigator", 23, 23, "OpenHotel", True, "client.openhotel.club", "openhotel.club", "Mar 2025", "Today, 15:40",
           BASE + ["See your friends list"]) \
    + conn("plaza", "console-off", 15, 23, "Pixel Plaza", False, "play.pixelplaza.example", "pixelplaza.example", "12 Aug 2026", "Yesterday, 21:12",
           BASE + ["See your friends list"]) \
    + conn("disco", "club", 23, 21, "Neon Docks", False, "neondocks.example/play", "neondocks.example", "02 Oct 2026", "3 weeks ago", BASE)

def myhotel(thumb, icon, iw, ih, name, hid, public, accounts, client, web, lic, code):
    if lic:
        licb = f'''<div class="lic" data-state="has">
            <div class="st st-has"><p><span class="badge on">Active</span> Licence made on {lic}. It was shown once and can't be shown again.</p>
              <details class="disc"><summary class="btn">Remake licence</summary><p>The current licence stops working at once. The hotel server needs the new one to start.</p><button class="btn danger-btn" type="button" data-go="new">Remake licence</button></details></div>
            <div class="st st-new"><p><b>Copy your new licence now.</b> You won't see it again.</p><div class="key"><code>ohl_9f3K2mQ7xV1pR8tZ4wL6yB0nC5sD</code><button class="btn" type="button">Copy</button></div><p class="hint">Put it in the hotel server's config as <code>LICENSE</code>.</p><button class="btn" type="button" data-go="has">Done</button></div>
          </div>'''
    else:
        licb = '''<div class="lic" data-state="none">
            <div class="st st-none"><p><span class="badge">None</span> This hotel has no licence yet. The server won't start without one.</p><button class="btn main" type="button" data-go="new">Generate licence</button></div>
            <div class="st st-new"><p><b>Copy your licence now.</b> You won't see it again. Lost it? Remake it.</p><div class="key"><code>ohl_2Hq8Wc4Nt6Jm1Xe9Ru3Ky7Bv5Pa0Gs</code><button class="btn" type="button">Copy</button></div><p class="hint">Put it in the hotel server's config as <code>LICENSE</code>.</p><button class="btn" type="button" data-go="has">Done</button></div>
            <div class="st st-has"><p><span class="badge on">Active</span> Licence made today. It was shown once and can't be shown again.</p></div>
          </div>'''
    return f'''      <div class="blk box">
        <div class="mh-head"><h3><img class="fav" src="assets/oh/icon-{icon}.png" width="{iw}" height="{ih}" alt=""> {name}</h3><span class="id">{hid}</span></div>
        <div class="mh">
          <div class="media">
            <figure><div class="thumb"><img src="assets/oh/hotel-thumb-{thumb}.png" width="160" height="72" alt="Hotel picture"></div><figcaption>Picture · 160 × 72 px</figcaption><a class="btn" href="#">Change picture</a></figure>
            <figure><div class="iconbox"><img src="assets/oh/icon-{icon}.png" width="{iw}" height="{ih}" alt="Hotel icon"></div><figcaption>Icon · {iw} × {ih} px<br><span class="hint">max 24 × 24</span></figcaption><a class="btn" href="#">Change icon</a></figure>
          </div>
          <form class="form" onsubmit="event.preventDefault()">
            <label>Name<input class="in" value="{name}"></label>
            <label>Client URL<input class="in" type="url" value="https://{client}"></label>
            <label>Website URL<input class="in" type="url" value="https://{web}"></label>
            <fieldset class="vis"><legend>Who can find it</legend>
              <label class="chk"><input type="radio" name="v-{thumb}"{' checked' if public else ''}> Public: listed in "Hotels online now"</label>
              <label class="chk"><input type="radio" name="v-{thumb}"{'' if public else ' checked'}> Private: only people with the link</label>
            </fieldset>
            <div class="row"><button class="btn main" type="submit">Save</button></div>
          </form>
        </div>
        <dl class="kv wide"><div><dt>Credit code</dt><dd><b>{code}</b> <span class="hint">can't be changed</span></dd></div><div><dt>Accounts connected</dt><dd>{accounts}</dd></div><div><dt>Online now</dt><dd>{'312' if public else '0'}</dd></div></dl>
        <p><a href="#library">Hotel catalog</a> &gt;&gt; &nbsp; <a href="#admin">Hotel admin</a> &gt;&gt;</p>
        <h3>Licence</h3>
        {licb}
        <p><a class="danger" href="#">Delete hotel</a></p>
      </div>
'''
hotels = '''      <div class="blk box">
        <h2>My hotels</h2>
        <p>Hotels you run on the OpenHotel network. Each hotel has one licence; its server uses it to talk to OpenHotel. Guests log in with their OpenHotel account.</p>
        <details class="disc newh"><summary class="btn main">Create a hotel</summary>
          <form class="form" onsubmit="event.preventDefault()">
            <label>Name<input class="in" placeholder="My hotel"></label>
            <label>Client URL<input class="in" type="url" placeholder="https://play.myhotel.example"></label>
            <label>Website URL<input class="in" type="url" placeholder="https://myhotel.example"></label>
            <label>Credit code<input class="in cc" placeholder="MYH" maxlength="3" pattern="[A-Z]{3}" autocapitalize="characters" style="max-width:80px;text-transform:uppercase"></label>
            <span class="hint">3 letters, A to Z. Your hotel's credits use this name on the exchange. <b>You can't change it later.</b></span>
            <fieldset class="vis"><legend>Who can find it</legend>
              <label class="chk"><input type="radio" name="v-new" checked> Public</label>
              <label class="chk"><input type="radio" name="v-new"> Private</label>
            </fieldset>
            <div class="row"><button class="btn main" type="submit">Create</button><span class="hint">You get the licence on the next step.</span></div>
          </form>
        </details>
      </div>
''' + myhotel("main", "navigator", 23, 23, "OpenHotel", "01M7XSPG3W92FQ0EEJ2EPHCY3C", True, "1,204,311", "client.openhotel.club", "openhotel.club", "12 Nov 2026", "OHC") \
    + myhotel("cafe", "club", 23, 21, "Pixel Inn", "01M7XSPG4KXBVQ8V0HYY57DZ69", False, 0, "play.pixelinn.example", "pixelinn.example", None, "PXI") + '''<script>
document.querySelectorAll(".lic").forEach((box) => box.addEventListener("click", (e) => {
  const b = e.target.closest("[data-go]");
  if (b) { box.dataset.state = b.dataset.go; box.querySelectorAll("details").forEach((d) => (d.open = false)); }
}));
document.querySelectorAll(".key .btn").forEach((b) => b.addEventListener("click", () => {
  const t = b.previousElementSibling.textContent;
  try { navigator.clipboard.writeText(t).then(() => (b.textContent = "Copied"), () => (b.textContent = "Select it")); } catch (e) { b.textContent = "Select it"; }
}));
</script>
'''
