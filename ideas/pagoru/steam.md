# OpenHotel on Steam

- Author: pagoru
- Status: proposed
- Created: 2026-11-14 · Updated: 2026-11-14
- Affects: openhotel, auth
- Discussion: none

## Summary
Ship the client on Steam as a free game: deno desktop shell, official hotel only, Steam login and linking through auth. No paid perks, no traditional ads. Part: [accounts](steam-accounts.md).

## Decisions
- Free, nothing paid in the Steam build.
- Steam app connects only to the official hotel. Other hotels open in the system browser.
- Shell: deno desktop, not Electron.
- Steamworks partner: pagoru.
- No traditional ads. Only product placement: sponsored furniture and rooms. No rewards for visiting or using them.

## Steam rules that matter
| Topic | Rule | Impact |
|---|---|---|
| Fee | $100 per app, recouped only past $1,000 revenue ([fee](https://partner.steamgames.com/doc/gettingstarted/appfee)) | One-off cost. |
| Onboarding | Identity, bank, tax; tax check up to 30 days ([onboarding](https://partner.steamgames.com/doc/gettingstarted/onboarding?l=english)) | Bank account in the partner's name. |
| Timing | 21 days fee to release, Coming Soon 2+ weeks, review 1-5 days | ~5-6 weeks. |
| Free | "Free product" option; no Daily/Weekend deals ([F2P](https://partner.steamgames.com/doc/store/freetoplay)) | Nothing else. |
| Ads | No paid ads as a business model, no rewards for watching ads; real brands as non-disruptive product placement OK ([advertising](https://partner.steamgames.com/doc/marketing/advertising)). Crypto/NFTs banned | No ad banners or ad income in the Steam build. Brand furniture/rooms OK. |
| Content | Content survey, disclose mature content ([survey](https://partner.steamgames.com/doc/gettingstarted/contentsurvey?l=english)) | Disclose online chat and user rooms. |
| Moderation | In-game chat is the developer's job ([moderation](https://partner.steamgames.com/doc/marketing/community_moderation)) | Official hotel = your moderators. Optional `FilterText` ([ISteamUtils](https://partner.steamgames.com/doc/api/ISteamUtils)). |
| External links | No rule found against opening the system browser from the game | Other hotels in the browser are outside the Steam product. |

## Shell: deno desktop
- [deno desktop](https://docs.deno.com/runtime/desktop/) (Deno 2.9) builds one binary per OS: code + Deno + a web engine. [Backends](https://docs.deno.com/runtime/desktop/backends.md): system WebView (default, small), CEF (bundled Chromium, ~150 MB, same everywhere), raw.
- Steamworks lives in the Deno side, not the page. Two options:
  1. [steamworks.js](https://github.com/ceifa/steamworks.js) via npm: a Rust (napi-rs + steamworks-rs) Node-API addon. Has `init`, `achievement`, `auth.getAuthTicketForWebApi`, `localplayer`, `cloud`, `input`. Deno loads Node-API addons and `deno compile` ships `.node` packages next to the binary. Last npm release 0.4.0, 2024-08: stale, test it first.
  2. `Deno.dlopen` (FFI) on `steam_api64.dll` / `libsteam_api.so` / `.dylib` from the SDK flat API. More work, no third-party dependency.
- `steam_api` redistributable sits next to the binary in every depot.
- Steam overlay (Shift+Tab) likely does not hook into the system WebView; Electron needs special flags for it. CEF backend may work, untested. The overlay is not required by Steam.

## Integration steps
1. Steamworks signup, $100, bank/tax. Get the App ID.
2. Store page, content survey, mark free, Coming Soon early.
3. deno desktop app wrapping `app/client`, loaded from local files. Steam init in Deno, expose `getTicket()` and `activateAchievement()` to the page.
4. On start: get Steam Web API ticket, log in through auth ([accounts](steam-accounts.md)), connect to the official hotel.
5. Travel to another hotel: open the system browser on that hotel's web client.
6. Achievements (optional).
7. Depots per OS + launch options, upload with `steamcmd +run_app_build` ([uploading](https://partner.steamgames.com/doc/sdk/uploading)). Beta branch first, default set live by hand.
8. CI: build per OS on tag, steamcmd to beta.
9. Review, wait 21 days, release.
