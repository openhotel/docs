# Network accounts, blocked and emails pages. Exec'd by pages_admin.py.
import html as _h
network_accounts = NN("network-accounts") + box("Accounts on the network (1,204,311)", '''        <form class="mfind" onsubmit="event.preventDefault()"><input class="in" type="search" placeholder="Search a name or email" aria-label="Search"><select class="in" aria-label="Filter"><option>Everyone</option><option>Online</option><option>Blocked on a hotel</option><option>Blocked on the network</option><option>No 2FA</option></select></form>'''
    + TBL(["Name", "Hotels", "Since", "Last seen", "State", ""], [
    ["Mintleaf", "3", "Aug 2026", "Online", '<span class="badge on">OK</span>', BTN("Open") + " " + BTN("Block on network")],
    ["Sparrow", "2", "Nov 2026", "Yesterday", '<span class="badge">Blocked on Pixel Plaza</span>', BTN("Open") + " " + BTN("Block on network")],
    ["Wanda", "2", "Sep 2026", "3 days ago", '<span class="badge">Blocked on Neon Docks</span>', BTN("Open") + " " + BTN("Block on network")],
    ["Trollface", "1", "Oct 2026", "20 Nov", '<span class="badge">Blocked on the network</span>', BTN("Open") + " " + BTN("Unblock")]]) + PAGER("1-4 of 1,204,311", "network-accounts")) + box("Block on the network", '''        <form class="form" onsubmit="event.preventDefault()"><label>Name or email<input class="in" value="Sparrow"></label>
          <label>Reason<select class="in"><option>Harassment</option><option>Credit exploit</option><option>Spam</option><option>Other</option></select></label>
          <label>Note (only staff see it)<input class="in" placeholder="What happened"></label>
          <span class="hint">The account can't log in to any hotel. Its hotels see the reason. You can unblock it at any time.</span>
          <div class="row"><button class="btn main" type="submit">Block on the network</button></div></form>''')
network_blocked = NN("network-blocked") + box("Blocked on the network (4)", TBL(
    ["Name", "Reason", "By", "Date", ""], [["Trollface", "Spam in 3 hotels", "Nightowl", "20 Nov", BTN("Unblock")], ["xX_cheat", "Credit exploit", "Nightowl", "14 Nov", BTN("Unblock")], ["Rude99", "Harassment", "Nightowl", "09 Nov", BTN("Unblock")]]) + PAGER("3 of 4", "network-blocked")) + box("Blocked on a hotel (9)", TBL(
    ["Name", "Hotel", "Reason", "Date", ""], [["Sparrow", "Pixel Plaza", "Harassment", "18 Nov", BTN("Block on network", True) + " " + BTN("Ignore")], ["Wanda", "Neon Docks", "Credit exploit", "12 Nov", BTN("Block on network", True) + " " + BTN("Ignore")], ["Lumen2", "OpenHotel", "Spam", "10 Nov", BTN("Block on network", True) + " " + BTN("Ignore")]]) + PAGER("3 of 9", "network-blocked")
    + '<p class="hint">Hotels see each other\'s blocks (hotel, reason, date) in their own Blocked page and can copy them.</p>')

EM_BODY = """<div style="font-family:Verdana,Arial,sans-serif;background:#efefef;padding:24px">
  <div style="max-width:480px;margin:auto;background:#fff;border:1px solid #000">
    <div style="background:#335ca6;color:#fff;padding:18px 20px;font-size:20px;font-weight:bold">OpenHotel</div>
    <div style="padding:20px;color:#222;font-size:13px;line-height:1.5">
      <h1 style="font-size:18px;margin:0 0 12px">Welcome, {{username}}!</h1>
      <p>Your account <b>{{email}}</b> is ready. Confirm your email to enter {{hotel}}.</p>
      <p style="text-align:center;margin:20px 0"><a href="{{link}}" style="background:#f3b52e;border:1px solid #000;color:#000;padding:10px 18px;text-decoration:none;font-weight:bold">Confirm email</a></p>
      <p style="color:#666;font-size:11px">Or use this code: {{code}}. It expires in 30 minutes.</p>
    </div>
  </div>
</div>"""
EM_NAMES = [("Welcome", "Verify your OpenHotel account", True), ("Verify email", "Your code is {{code}}", True), ("Reset password", "Reset your password", True), ("2FA changed", "Two-factor changed on your account", True), ("Account blocked", "Your account was blocked", True), ("Hotel connected", "{{hotel}} was connected to your account", False), ("Newsletter", "{{title}}", True)]
emrows = "".join(f'<tr><td><b>{n}</b></td><td>{sub}</td><td><span class="badge{" on" if on else ""}">{"On" if on else "Off"}</span></td><td>{"Default" if i < 5 or n == "Newsletter" else "Custom"}</td></tr>' for i, (n, sub, on) in enumerate(EM_NAMES))
EM_JS = """<script>(function(){
var $=function(i){return document.getElementById(i)},body=$('em-body'),subj=$('em-subj'),pv=$('em-pv'),st=$('em-st'),name=$('em-name'),list=$('em-list'),v=4;
var P={username:'Nightowl',email:'night@example.com',hotel:'OpenHotel',code:'482 913',link:'https://auth.openhotel.club/confirm/x7Qp',reason:'Harassment',date:'21 Nov'};
function fill(t){return t.replace(/\\{\\{(\\w+)\\}\\}/g,function(m,k){return P[k]!==undefined?P[k]:m;});}
function draw(){pv.srcdoc=fill(body.value);$('em-psub').textContent=fill(subj.value);}
body.addEventListener('input',draw);subj.addEventListener('input',draw);draw();
document.querySelectorAll('[data-p]').forEach(function(b){b.addEventListener('click',function(){var t='{{'+b.dataset.p+'}}',s=body.selectionStart;body.value=body.value.slice(0,s)+t+body.value.slice(body.selectionEnd);body.focus();body.selectionStart=body.selectionEnd=s+t.length;draw();});});
$('em-save').addEventListener('click',function(){st.textContent='Saved as version '+(++v)+'.';});
$('em-new').addEventListener('click',function(){var tr=document.createElement('tr'),n=name.value||'New template';tr.innerHTML='<td><b></b></td><td></td><td><span class="badge on">On</span></td><td>Custom</td>';tr.cells[0].firstChild.textContent=n;tr.cells[1].textContent=subj.value;list.appendChild(tr);st.textContent='Saved as a new template: '+n+'.';});
$('em-test').addEventListener('click',function(){st.textContent='Test sent to night@example.com.';});
document.querySelectorAll('[data-dev]').forEach(function(b){b.addEventListener('click',function(){pv.style.width=b.dataset.dev;document.querySelectorAll('[data-dev]').forEach(function(x){x.classList.toggle('main',x===b);});});});
})();</script>"""
network_emails = NN("network-emails") + box("Email templates (7)", '<div class="tbl"><table id="em-list"><tr><th>Template</th><th>Subject</th><th>Sending</th><th></th></tr>' + emrows + '</table></div>') + '<div class="two">' + box("Edit template", '''        <form class="form" onsubmit="event.preventDefault()">
          <label>Name<input class="in" id="em-name" value="Welcome"></label>
          <label>From<input class="in" value="OpenHotel &lt;no-reply@openhotel.club&gt;"></label>
          <label>Subject<input class="in" id="em-subj" value="Verify your OpenHotel account"></label>
          <label>Body (HTML)<textarea class="in tx" id="em-body" rows="14" spellcheck="false">''' + _h.escape(EM_BODY) + '''</textarea></label>
          <span class="hint">Click a parameter to add it where the cursor is.</span>
          <p>''' + " ".join(f'<button class="btn" type="button" data-p="{p}">{{{{{p}}}}}</button>' for p in ["username", "email", "hotel", "code", "link", "reason", "date", "title", "text"]) + '''</p>
          <div class="row"><button class="btn main" type="button" id="em-save">Save template</button> <button class="btn" type="button" id="em-new">Save as new template</button> <button class="btn" type="button" id="em-test">Send a test to me</button></div>
          <p class="hint" id="em-st" role="status">Last saved 16 Nov, version 4. Older versions can be restored.</p>
        </form>''') + box("Preview", '''        <p class="hint">Subject: <b id="em-psub"></b></p>
        <p><button class="btn main" type="button" data-dev="100%">Desktop</button> <button class="btn" type="button" data-dev="320px">Phone</button></p>
        <div style="background:#efefef;border:1px solid var(--line);overflow:auto;padding:6px"><iframe id="em-pv" title="Email preview" style="display:block;margin:auto;width:100%;height:420px;border:0;background:#fff" sandbox></iframe></div>
        <p class="hint">Sample values: Nightowl, night@example.com, OpenHotel.</p>''') + '</div>' + box("Images and style", '''        <p class="hint">Upload the picture here: it goes to the static server and you get a full https URL for an <code>&lt;img&gt;</code>. Don't embed pictures in the email: Gmail blocks them.</p>
        <p><input type="file" accept="image/png,image/jpeg" aria-label="Image"></p>
        <p class="hint">Tailwind works if it is compiled before sending: the classes become inline <code>style</code> attributes (Maizzle or React Email do this). Mail apps don't run Tailwind themselves.</p>''') + box("Who sends", '''        <p class="hint">Emails are sent by the network (auth), never by a hotel.</p>''') + EM_JS

def news_rows(items):
    return "".join(f'<tr class="go"><td><a href="#post"><b>{t}</b></a><br><span class="hint">{d}</span></td><td>{st}</td><td>{em}</td><td>{BTN("Edit")} {BTN("Delete")}</td></tr>' for t, d, st, em in items)
def news_editor(scope, who, count, mail_note):
    return box("Write news", f'''        <form class="form" onsubmit="event.preventDefault()">
          <label>Title<input class="in" value="Telephone booths are here"></label>
          <label>Text<textarea class="in tx" rows="6">Meet a friend in another hotel: step into a telephone booth and dial their hotel.</textarea></label>
          <label>Picture<input type="file" accept="image/png,image/jpeg" aria-label="Picture"></label>
          <span class="hint">64 x 64, shown as it is.</span>
          <label>Publish on<input class="in" type="date" style="max-width:10em"></label>
          <label class="chk"><input type="checkbox" id="nm-{scope}" checked> Send by email to {who} ({count} subscribed)</label>
          <span class="hint">{mail_note}</span>
          <div class="row"><button class="btn" type="button">Save draft</button> <button class="btn main" type="submit">Publish</button> <button class="btn" type="button">Preview email</button></div>
        </form>''')
admin_news = AN("admin-news") + box("Hotel news (4)", TBL(["News", "State", "Email", ""], [], ) .replace("</table>", news_rows([("Telephone booths are here", "Publishes 24 Nov", '<span class="badge">Draft</span>', '<span class="badge">Requested</span>'), ("Winter room contest", "15 Nov", '<span class="badge on">Published</span>', '<span class="badge on">Sent to 1,102</span>'), ("Maintenance on Friday", "08 Nov", '<span class="badge on">Published</span>', "Not sent"), ("New clothes", "01 Nov", '<span class="badge on">Published</span>', '<span class="badge on">Sent to 1,085</span>')]) + "</table>") + PAGER("4 of 12", "admin-news")) + news_editor("hotel", "guests who joined OpenHotel", "1,240", "Only guests who joined this hotel and subscribed to its news get it, never the rest of the network. The hotel never sees any email address: ticking this sends a request to the main hotel, which sends it with the Newsletter template. The main hotel can refuse a request that breaks its limits (for example 2 per week).")
network_news = NN("network-news") + box("Network news (3)", TBL(["News", "State", "Email", ""], [], ).replace("</table>", news_rows([("Network update 0.157", "Draft", '<span class="badge">Draft</span>', "Not sent"), ("New hotel: Neon Docks", "Published 12 Nov", '<span class="badge on">Published</span>', '<span class="badge on">Sent to 410,200</span>'), ("Credit exchange is open", "Published 02 Nov", '<span class="badge on">Published</span>', '<span class="badge on">Sent to 398,000</span>')]) + "</table>") + PAGER("3 of 8", "network-news")) + box("Email requests from hotels (2)", TBL(
    ["Hotel", "News", "Its subscribed guests", "This week", ""], [["Pixel Plaza", "Summer party", "9,400", "1 of 2", BTN("Preview") + " " + BTN("Send", True) + " " + BTN("Refuse")], ["Neon Docks", "New DJ room", "2,100", "2 of 2", BTN("Preview") + " " + BTN("Send", True) + " " + BTN("Refuse")]], (2,))
    + '<p class="hint">A hotel asks, the network sends, and only to guests who joined that hotel and subscribed. The hotel only gets the result (sent, refused, how many). Hotels never get addresses. Limits per hotel are in <a href="#network-settings">Settings</a>.</p>') + news_editor("net", "all subscribers of the network", "410,200", "Sent from the network with the Newsletter template. Subscribers can unsubscribe in one click and the link is added to every email.")
