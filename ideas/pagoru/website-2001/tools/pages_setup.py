# First-run Setup wizard. Exec'd at the end of pages_site.py. Bare pages (no nav, no login side).
def sfield(l, v="", t="text", ph="", h=""):
    return f'<label>{l}<input class="in" type="{t}" value="{v}" placeholder="{ph}" data-l="{l}"></label>' + (f'<span class="hint">{h}</span>' if h else "")
def sform(title, inner): return box(title, '        <form class="form" onsubmit="event.preventDefault()">' + inner + '</form>')
def schk(t, on=True, group="", l=""):
    if group: return f'<label class="chk"><input type="radio" name="{group}"{" checked" if on else ""} data-l="{l}" data-t="{t}"> {t}</label>'
    return f'<label class="chk"><input type="checkbox"{" checked" if on else ""} data-l="{t}"> {t}</label>'
def ssel(l, opts): return f'<label>{l}<select class="in" data-l="{l}">' + "".join(f"<option>{o}</option>" for o in opts) + '</select></label>'
SMTP = lambda frm: sfield("SMTP server", "smtp.example.com") + '<div class="fgrid"><label class="f">Port<input class="in" value="587" data-l="SMTP port"></label><label class="f">Security<select class="in" data-l="SMTP security"><option>STARTTLS</option><option>SSL/TLS</option><option>None</option></select></label></div>' + sfield("SMTP user") + sfield("SMTP password", "", "password") + sfield("Send from", frm) + '<div class="row"><button class="btn" type="button">Send a test email</button> <span class="hint">Needed for verify and password emails. You can skip and add it later.</span></div>'
ADMIN = lambda role: sfield(role + " username", "admin") + sfield("Email", "", "email", "you@example.com") + sfield("Password", "", "password") + sfield("Repeat password", "", "password") + schk("Set up 2FA now", False)
HOTEL = sfield("Hotel name", "My hotel") + sfield("Short description", "", "text", "A friendly hotel for…") + ssel("Language", ["English", "Español"]) + sfield("Website (this site)", "https://myhotel.example", "url") + sfield("Client (where guests play)", "https://play.myhotel.example", "url")
WZ_JS = """<script>(function(){var w=document.querySelector('.wz'),ps=[].slice.call(w.querySelectorAll('.wp')),ls=[].slice.call(w.querySelectorAll('.wl li[data-go]')),cur=0;
function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function sum(){var o='';w.querySelectorAll('[data-l]').forEach(function(e){var v;if(e.type==='radio'){if(!e.checked)return;v=e.dataset.t}else if(e.type==='checkbox')v=e.checked?'Yes':'No';else if(e.tagName==='SELECT')v=e.options[e.selectedIndex].text;else v=e.type==='password'?(e.value?'\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022':'(empty)'):(e.value||'(empty)');o+='<div><dt>'+esc(e.dataset.l)+'</dt><dd>'+esc(v)+'</dd></div>'});w.querySelector('.sum').innerHTML=o}
function show(n){cur=n;ps.forEach(function(p,i){p.hidden=i!==n});ls.forEach(function(l,i){l.classList.toggle('cur',i===n);l.classList.toggle('done',i<n)});if(n===ps.length-1)sum()}
w.addEventListener('click',function(e){var b=e.target.closest('[data-go]');if(!b)return;var d=b.dataset.go;show(d==='n'?cur+1:d==='p'?cur-1:+d)});show(0)})();</script>"""
def wizard(steps, mode, back="#setup"):
    n = len(steps)
    panels = ""
    for i, (t, inner) in enumerate(steps):
        prev = f'<a class="btn" href="{back}">Back</a>' if i == 0 else '<button class="btn" type="button" data-go="p">Back</button>'
        panels += f'<div class="wp" hidden><h2>{t}</h2><form class="form" onsubmit="event.preventDefault()">' + inner + f'<div class="row wn">{prev} <button class="btn main" type="button" data-go="n">Next</button></div></form></div>'
    panels += f'<div class="wp" hidden><h2>Review</h2><p class="hint">Check everything. Nothing is saved until you finish. You can go back to any step.</p><dl class="kv sum"></dl><div class="row wn"><button class="btn" type="button" data-go="p">Back</button> <button class="btn main" type="button">Finish setup</button></div></div>'
    lst = '<li class="m done"><a href="#setup"><b>1. Mode</b></a></li><li class="g"><b>2. ' + mode + ' config</b></li>' + "".join(f'<li class="s" data-go="{i}"><b>2.{i+1} {t}</b></li>' for i, (t, _) in enumerate(steps)) + f'<li data-go="{n}"><b>3. Review</b></li>'
    return '<!--BARE--><div class="blk box wzbox wz"><div class="wzm">' + panels + '</div><div class="wzs"><h2>Steps</h2><ol class="gsteps wl">' + lst + '</ol><p class="hint">Everything here can be changed later in Manage hotel, except the mode.</p></div></div>' + WZ_JS
setup_join = wizard(mode="Managed", steps=[
  ("Network", ssel("Network", ["https://openhotel.club (official)", "Other network (enter URL)"]) + '<label>Other network URL<input class="in" type="url" placeholder="https://" disabled></label><div class="row"><button class="btn" type="button">Check network</button> <span class="badge on">Reachable · v1.4</span></div>'),
  ("Licence and sign in", '<p>Your hotel needs a licence from the network. Sign in on the network, create the licence there and approve this hotel. It comes back here by itself.</p><dl class="kv"><div><dt>This hotel</dt><dd>Code <b>K7QF-29XM</b></dd></div><div><dt>Status</dt><dd><span class="badge">Waiting for approval…</span></dd></div></dl><p><a class="btn main" href="#setup-join">Open openhotel.club to sign in</a> <button class="btn" type="button">Show a new code</button></p><p class="hint">No browser on this machine? Create the licence on the network and paste it here.</p>' + sfield("Licence (optional, paste)", "", "text", "ohl_…")),
  ("Admin", '<p>You become the first admin of this hotel with the network account you signed in with.</p><dl class="kv"><div><dt>Signed in as</dt><dd>dana (dana@example.com)</dd></div><div><dt>Role</dt><dd>Hotel admin</dd></div></dl>'),
  ("Hotel", HOTEL),
  ("Registration", schk("Guests can register on this hotel") + schk("Guests must verify their email")),
])
setup_new = wizard(mode="Network", steps=[
  ("Network", sfield("Network name", "My network") + sfield("Network address", "https://mynetwork.example", "url", "", "Where this server is reached. Hotels and guests connect here.")),
  ("Network admin", ADMIN("Admin")),
  ("Email sending", SMTP("no-reply@mynetwork.example")),
  ("Licences", schk("Only network admins create licences", True, "lic", "Who creates licences") + schk("Any verified account can create one", False, "lic", "Who creates licences") + '<span class="hint">A licence for the first hotel is made for you.</span>'),
  ("First hotel", HOTEL),
])
setup_stand = wizard(mode="Standalone", steps=[
  ("Hotel admin", ADMIN("Admin")),
  ("Email sending", SMTP("no-reply@myhotel.example")),
  ("Hotel", HOTEL),
  ("Registration", schk("Guests can register") + schk("Guests must verify their email")),
])

MODES = [("join", "Managed", True, "Joins an existing network such as openhotel.club. You get a licence from the network and guests use their network account.", ["Network", "Licence and sign in", "Admin", "Hotel", "Registration"]),
         ("standalone", "Standalone", False, "One hotel on its own, with its own accounts. No network, no licence.", ["Hotel admin", "Email sending", "Hotel", "Registration"]),
         ("new", "Network", False, "You run the network: accounts, hotels, licences and news. Your first hotel is part of it.", ["Network", "Network admin", "Email sending", "Licences", "First hotel"])]
WJS = "<script>(function(){var nm=" + str({k: t for k, t, _, _, _ in MODES}).replace("'", '"') + ",d=" + str({k: v for k, _, _, _, v in MODES}).replace("'", '"') + ",w=document.querySelector('.wzbox'),l=w.querySelector('.wl'),n=w.querySelector('#wnext');function up(){var r=w.querySelector('[name=mode]:checked');if(!r)return;var k=r.value;l.innerHTML='<li class=cur><b>1. Mode</b></li><li class=g><b>2. '+nm[k]+' config</b></li>'+d[k].map(function(t,i){return '<li class=s><b>2.'+(i+1)+' '+t+'</b></li>'}).join('')+'<li><b>3. Review</b></li>';n.href=w.querySelector('[data-m='+k+']').href;n.removeAttribute('aria-disabled')}w.addEventListener('change',up);var ci=w.querySelector('.wzm input[type=text]'),ce=w.querySelector('#codeerr');ci.addEventListener('input',function(){var bad=ci.value.length>0;ce.hidden=!bad;ci.setAttribute('aria-invalid',bad);ci.classList.toggle('bad',bad)});up()})();</script>"
setup_welcome = '<!--BARE--><div class="blk box wzbox"><div class="wzm"><h2>Set up OpenHotel</h2><p>This server has an empty database and no accounts, so nothing is configured yet. Answer a few questions here instead of setting environment variables. It takes about five minutes.</p><form class="form" onsubmit="event.preventDefault()">' + sfield("Setup code", "", "text", "xxxx-xxxx", "The server prints a one-time code in its log when it starts empty. This keeps strangers from setting up your server first.") + '<span class="hint err" id="codeerr" role="alert" hidden>That code is not correct. Copy it from the server log.</span>' + '<h3>Choose a mode</h3>' + "".join(f'<label class="chk"><input type="radio" name="mode" value="{k}"{" checked" if rec else ""}> <b>{t}</b>{" <span class=badge>Recommended</span>" if rec else ""}</label><span class="hint">{d}</span><a data-m="{k}" href="#setup-{k}" hidden>x</a>' for k, t, rec, d, _ in MODES) + '<div class="row wn"><a class="btn main" id="wnext" href="#setup-join">Next</a></div></form></div><div class="wzs"><h2>Steps</h2><ol class="gsteps wl"></ol><p class="hint">Pick a mode and the steps for it show here. You answer one step at a time, then check everything before anything is saved.</p><h3>Changing mode later</h3><p class="hint">The mode is fixed once setup ends. Switching between standalone, network and managed wipes accounts and links, so it is not in the interface. It takes a server command that asks you to type the hotel name to confirm.</p></div></div>' + WJS
