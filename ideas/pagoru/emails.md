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
