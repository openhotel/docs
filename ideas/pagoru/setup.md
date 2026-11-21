# First-run setup

Idea by pagoru. Mockups: `website-2001/retro-setup*.html`.

When the database is empty and there are no accounts, every page redirects to `/setup`. No environment variables to fill in. Once finished, `/setup` locks for good and changes go to [hotel-admin](hotel-admin.md).

- **Setup code.** The server prints a one-time code in its log at start. Setup asks for it, so nobody else can claim a fresh server first.
- **Welcome.** Pick a mode (managed is recommended): standalone (one hotel, own accounts, no network), network (you run accounts, licences and hotels) or managed (joins an existing network such as openhotel.club).
- **Mode is fixed.** Switching wipes accounts and links, so it is not in the interface. Only a server command can do it, and it asks you to type the hotel name. Manage hotel shows the mode read-only.

## Standalone
1. Hotel admin: username, email, password, optional 2FA.
2. Email sending (SMTP, test email, can be skipped).
3. Hotel: name, description, language, website and client URLs.
4. Registration: open or closed, email verification.

## Managed (joins a network, for example openhotel.club)
1. Network: the official one or another URL, with a reachability check.
2. Licence and sign in: setup shows a short code and opens the network. The owner signs in there, creates the licence and approves the code. The licence returns to the hotel by itself. Pasting a licence also works.
3. Admin: the network account used to sign in becomes the first hotel admin.
4. Hotel: name, description, language, website URL, client URL.
5. Registration: open or closed, email verification.

## Network
1. Network name and address.
2. Network admin account: username, email, password, optional 2FA.
3. Email sending: SMTP, with a test email (can be skipped).
4. Licences: who may create them. One is made for the first hotel.
5. First hotel: name, website URL, client URL.

Finish writes everything to the database. Email: see [emails](emails.md).
