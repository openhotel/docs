# Ideas

Proposals for OpenHotel. **An idea is not a decision.** Nothing here is binding until its status is `accepted`, and even then the source of truth for what exists is the code and the other docs folders.

## Where ideas go
- `ideas/<github-login>/<slug>.md`: one folder per author, using the GitHub login (e.g. `ideas/pagoru/`). Co-owners' ideas go in their own folder too: they are proposals like anyone else's.
- One idea per file, kebab-case slug. Split long ideas into `<slug>-<part>.md` files linked from the main one.
- Every idea file is listed in the index below. Max 4 KB per file (CI).

## Status values
| Status | Meaning |
|---|---|
| `draft` | Being written, not ready for feedback |
| `proposed` | Ready for feedback |
| `discussing` | Under discussion (link the issue/Discussion) |
| `accepted` | Agreed by the maintainers; can be turned into tasks |
| `rejected` | Not going ahead (say why in the file) |
| `superseded` | Replaced by another idea (link it) |
| `done` | Implemented; facts moved into `org/` or `projects/` |

## Template
```markdown
# <Title>

- Author: <github-login>
- Status: draft | proposed | discussing | accepted | rejected | superseded | done
- Created: YYYY-MM-DD · Updated: YYYY-MM-DD
- Affects: <repos>
- Discussion: <issue/Discussion link or "none">

## Summary
One or two sentences.

## Motivation
The problem, with links to issues.

## Proposal
What changes. Bullets, tables, short code blocks.

## Impact
Repos, users, migrations, what breaks.

## Open questions
Numbered list.

## Links
Issues, PRs, related ideas.
```

## Rules
- Only the author edits Summary/Proposal; others comment in the linked Discussion or PR.
- When status changes, update `Updated` and the index line.
- Link issues with full GitHub URLs so they can be tracked.

## Index
| Idea | Author | Status |
|---|---|---|
| [Org restructuring](pagoru/restructuring.md): client, services and shared libs in one monorepo. Parts: [triage](pagoru/triage.md), [monorepo](pagoru/monorepo.md), [app/shared](pagoru/shared.md), [issues](pagoru/issues.md), [socket](pagoru/socket.md), [games](pagoru/games.md), [archive + devkit](pagoru/archive-devkit.md), [questions](pagoru/questions.md) | pagoru | proposed |
| [Binary furniture and public rooms](pagoru/binary-assets.md): one signed `.oha` file per asset, editable only in asset-editor. Parts: [format](pagoru/binary-assets-format.md), [rollout](pagoru/binary-assets-rollout.md) | pagoru | proposed |
| [OpenHotel on Steam](pagoru/steam.md): free Steam release, deno desktop shell, official hotel only, Steam login and account linking. Parts: [accounts](pagoru/steam-accounts.md) | pagoru | proposed |
| [Release manifest](pagoru/release-manifest.md): partial monorepo releases + `release.oh` with each app's real version, so updaters skip unchanged apps | pagoru | proposed |
| [Shared migration](pagoru/shared-migration.md): replace @oh and @da libs and cross-app copies with app/shared, same dep versions, before monster replaces master. Parts: [libs](pagoru/shared-migration-libs.md), [duplicates](pagoru/shared-migration-duplicates.md), [versions](pagoru/shared-migration-versions.md) | pagoru | accepted |
| [Website rework, 2001 style](pagoru/website-2001.md): static HTML mockups (home, news, auth pages, community hotel) with assets and generators in `pagoru/website-2001/` | pagoru | draft |
| [Credit exchange between hotels](pagoru/credit-exchange.md): each hotel's credits trade against OHC on an onet order book; friends network-wide, furniture stays | pagoru | draft |
| [Asset library and marketplace](pagoru/asset-library.md): owners pick rooms, furniture and clothes per hotel from a network marketplace; draw on web, Aseprite or Resprite | pagoru | draft |
| [Hotel admin in My account](pagoru/hotel-admin.md): admin box per hotel (accounts, rooms, moderation, credits, registration lock) and a network box for the main hotel | pagoru | draft |
