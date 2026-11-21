# Emails and templates

- Author: pagoru
- Status: draft
- Created: 2026-11-21 · Updated: 2026-11-21
- Affects: auth, web, static
- Discussion: none

## Summary
The network sends emails (verify, reset password, 2FA, block notice). Network admins edit the templates on the web with a live preview. Mockup: [website-2001](website-2001/) `retro-network-emails`.

## Proposal
- **Sender**: only auth sends email, never a hotel. One From address for the network.
- **Templates**: name, subject, HTML body, on/off. Defaults: Welcome, Verify email, Reset password, 2FA changed, Account blocked, Hotel connected. Admins can save, save as a new template, send a test to themselves and restore older versions.
- **News by email**: news can be mailed to subscribed guests. Guests subscribe in My account (network news, and each hotel's news). The Newsletter template carries `{{title}}`, `{{text}}` and an unsubscribe link.
- **Hotels have no addresses**: a hotel ticking "send by email" on its news sends a request to the main hotel (onet to auth). The network sends it only to guests who joined that hotel and subscribed to its news, never to the rest of the network, and returns the result (sent, refused, count). Network admins can preview, send or refuse, and cap requests per hotel per week.
- **Consent (EU)**: one general news switch, off by default and never pre-ticked (ePrivacy Art. 13, GDPR; CJEU Planet49). Register has it unticked, plus a required Terms of Service and EULA box. My account has the same switch; it covers the network and the hotels the guest joined. To raise opt-ins without a default: ask once at first login with Yes and No and nothing pre-selected. Keep when and how consent was given. One-click unsubscribe in every email. Account and service emails (verify, security, downtime, terms changes) need no consent; news, events and promotions do, even without money involved. Not legal advice.
- **Parameters**: `{{username}}`, `{{email}}`, `{{hotel}}`, `{{code}}`, `{{link}}`, `{{reason}}`, `{{date}}`. Each template says which it can use. Unknown ones are refused on save.
- **Preview**: rendered with sample values, desktop and phone width, in a sandboxed frame.
- **Tailwind**: mail apps don't run it. Write with Tailwind, compile before sending so classes become inline `style` attributes (Maizzle or React Email). The editor keeps the compiled HTML.
- **Images**: upload on the editor, stored in static, used as a full https URL in `<img>` with width, height and alt. No base64 (Gmail blocks it). PNG or JPG, 600 px wide at most.

## Alternatives
| Option | For | Against |
|---|---|---|
| Templates in code | Simple | Every change is a release |
| Editable templates (proposed) | Admins change text fast | Needs versions and validation |

## Impact
- auth: template store, versions, mail provider, send log.
- web: Emails page in Network admin.
- static: email images.

## Open questions
1. Which mail provider and sending domain?
2. Do hotels get their own templates later?
3. Which languages do templates need?
