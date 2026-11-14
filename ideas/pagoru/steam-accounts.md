# Steam and OpenHotel accounts

- Author: pagoru
- Status: proposed
- Created: 2026-11-14 · Updated: 2026-11-14
- Affects: openhotel, auth
- Discussion: none

Part of [OpenHotel on Steam](steam.md).

Steam allows own accounts and documents linking a SteamID to them; once linked, the SteamID alone signs in, and unknown SteamIDs can get an account created on the fly ([Steam auth](https://partner.steamgames.com/doc/features/auth)). Only **auth** talks to Steam; hotels keep getting normal connection tokens.

## Login in the Steam app
1. App gets `getAuthTicketForWebApi("openhotel-auth")`.
2. Sends the ticket (hex) to auth, e.g. `POST /api/v3/account/steam`.
3. Auth calls `ISteamUserAuth/AuthenticateUserTicket` with the publisher key and gets the SteamID ([docs](https://partner.steamgames.com/doc/webapi/isteamuserauth)). Key stays on the server.
4. Linked: auth session, then connection token for the official hotel.
5. Not linked: "Log in to link your account" or "Create account" (username only).

## Linking
| Where | How |
|---|---|
| Steam app | Logged in with OpenHotel account, Link Steam, app sends a ticket, auth stores the SteamID. |
| Website | "Sign in through Steam" (OpenID 2.0, `https://steamcommunity.com/openid/`), verify server side. |
| Unlink | Auth settings. Only if the account has a password + email, so nobody is locked out. |

Rules: one SteamID per account, unique, link/unlink logged, admins can remove links, bans stay on the OpenHotel account.

## Email
Steam never gives the email. Web API returns SteamID, persona name, avatar, profile URL ([ISteamUser](https://partner.steamgames.com/doc/webapi/ISteamUser)); OpenID returns only the SteamID. Steam-created accounts have no email: make it optional and ask for it later (needed for unlinking and password recovery). While linked, Steam is the recovery path.

## Other hotels in the browser
The browser does not share the app's session. The player logs in on the web with password, or with "Sign in through Steam" if linked. Same account, no extra token sharing.
