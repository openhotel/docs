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
WZ_JS = """<script>(function(){var w=document.querySelector('.wz'),ps=[].slice.call(w.querySelectorAll('.wp')),ls=[].slice.call(w.querySelectorAll('.wl li')),cur=0;
function esc(t){var d=document.createElement('div');d.textContent=t;return d.innerHTML}
function sum(){var o='';w.querySelectorAll('[data-l]').forEach(function(e){var v;if(e.type==='radio'){if(!e.checked)return;v=e.dataset.t}else if(e.type==='checkbox')v=e.checked?'Yes':'No';else if(e.tagName==='SELECT')v=e.options[e.selectedIndex].text;else v=e.type==='password'?(e.value?'\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022':'(empty)'):(e.value||'(empty)');o+='<div><dt>'+esc(e.dataset.l)+'</dt><dd>'+esc(v)+'</dd></div>'});w.querySelector('.sum').innerHTML=o}
function show(n){cur=n;ps.forEach(function(p,i){p.hidden=i!==n});ls.forEach(function(l,i){l.className=i===n?'cur':(i<n?'done':'')});if(n===ps.length-1)sum()}
w.addEventListener('click',function(e){var b=e.target.closest('[data-go]');if(!b)return;var d=b.dataset.go;show(d==='n'?cur+1:d==='p'?cur-1:+d)});show(0)})();</script>"""
def wizard(steps, back="#setup"):
    n = len(steps)
    panels = ""
    for i, (t, inner) in enumerate(steps):
        prev = f'<a class="btn" href="{back}">Back</a>' if i == 0 else '<button class="btn" type="button" data-go="p">Back</button>'
        nxt = '<button class="btn main" type="button" data-go="n">Next</button>'
        panels += f'<div class="wp" hidden>' + box(f"{i+1}. {t}", '        <form class="form" onsubmit="event.preventDefault()">' + inner + f'<div class="row">{prev} {nxt}</div></form>') + '</div>'
    review = '<div class="wp" hidden>' + box(f"{n+1}. Review", '<p class="hint">Check everything. Nothing is saved until you finish. You can go back to any step.</p><dl class="kv sum"></dl><div class="row"><button class="btn" type="button" data-go="p">Back</button> <button class="btn main" type="button">Finish setup</button></div>') + '</div>'
    lst = "".join(f'<li data-go="{i}"><b>{i+1}. {t}</b></li>' for i, (t, _) in enumerate(steps + [("Review", "")]))
    return '<!--BARE--><div class="two wide wz"><div>' + panels + review + '</div><div>' + box("Steps", '<ol class="gsteps wl">' + lst + '</ol><p class="hint">Everything here can be changed later in Manage hotel, except the mode.</p>') + '</div></div>' + WZ_JS
setup_join = wizard([
  ("Network", ssel("Network", ["https://openhotel.club (official)", "Other network (enter URL)"]) + '<label>Other network URL<input class="in" type="url" placeholder="https://" disabled></label><div class="row"><button class="btn" type="button">Check network</button> <span class="badge on">Reachable · v1.4</span></div>'),
  ("Licence and sign in", '<p>Your hotel needs a licence from the network. Sign in on the network, create the licence there and approve this hotel. It comes back here by itself.</p><dl class="kv"><div><dt>This hotel</dt><dd>Code <b>K7QF-29XM</b></dd></div><div><dt>Status</dt><dd><span class="badge">Waiting for approval…</span></dd></div></dl><p><a class="btn main" href="#setup-join">Open openhotel.club to sign in</a> <button class="btn" type="button">Show a new code</button></p><p class="hint">No browser on this machine? Create the licence on the network and paste it here.</p>' + sfield("Licence (optional, paste)", "", "text", "ohl_…")),
  ("Admin", '<p>You become the first admin of this hotel with the network account you signed in with.</p><dl class="kv"><div><dt>Signed in as</dt><dd>dana (dana@example.com)</dd></div><div><dt>Role</dt><dd>Hotel admin</dd></div></dl>'),
  ("Hotel", HOTEL),
  ("Registration", schk("Guests can register on this hotel") + schk("Guests must verify their email")),
])
setup_new = wizard([
  ("Network", sfield("Network name", "My network") + sfield("Network address", "https://mynetwork.example", "url", "", "Where this server is reached. Hotels and guests connect here.")),
  ("Network admin", ADMIN("Admin")),
  ("Email sending", SMTP("no-reply@mynetwork.example")),
  ("Licences", schk("Only network admins create licences", True, "lic", "Who creates licences") + schk("Any verified account can create one", False, "lic", "Who creates licences") + '<span class="hint">A licence for the first hotel is made for you.</span>'),
  ("First hotel", HOTEL),
])
setup_stand = wizard([
  ("Hotel admin", ADMIN("Admin")),
  ("Email sending", SMTP("no-reply@myhotel.example")),
  ("Hotel", HOTEL),
  ("Registration", schk("Guests can register") + schk("Guests must verify their email")),
])

setup_welcome = '<!--BARE--><div class="two"><div>' + \
  box("Set up OpenHotel", '<p>This server has an empty database and no accounts, so nothing is configured yet. Answer a few questions here instead of setting environment variables. It takes about five minutes.</p>') + \
  sform("Setup code", sfield("Code from the server log", "", "text", "xxxx-xxxx", "The server prints a one-time code when it starts empty. This keeps strangers from setting up your server first.")) + \
  box("Changing mode later", '<p>The mode is fixed once setup ends. Switching between standalone, network and managed wipes accounts and links, so it is not in the interface. It takes a server command that asks you to type the hotel name to confirm.</p>') + \
  '</div><div>' + \
  box("Standalone", '<p>One hotel on its own. Its own accounts, no network, no licence. Pick this to run a hotel just for your community.</p><p><a class="btn main" href="#setup-standalone">Standalone hotel</a></p>') + \
  box("Network", '<p>You run a network: its accounts, hotels, licences and news. Your first hotel is part of it and other hotels can join later.</p><p><a class="btn main" href="#setup-new">Create a network</a></p>') + \
  box("Managed <span class=\"badge on\">Recommended</span>", '<p>Your hotel joins an existing network such as openhotel.club. You get a licence from the network and guests use their network account. Updates, licence and network features are handled for you.</p><p><a class="btn main" href="#setup-join">Join a network</a></p>') + '</div></div>'
