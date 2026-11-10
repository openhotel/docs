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
| [Org restructuring](pagoru/restructuring.md): ~20 repos to ~8. Parts: [triage](pagoru/triage.md), [utils split](pagoru/utils-split.md), [services monorepo](pagoru/services-monorepo.md), [socket](pagoru/socket.md), [games](pagoru/games.md), [archive + devkit](pagoru/archive-devkit.md), [questions](pagoru/questions.md) | pagoru | proposed |
