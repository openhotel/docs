# Docs conventions

How to read and maintain these docs. Written for humans and AI agents.

## Reading
1. Open [README.md](../README.md). Each line is a one-line summary + link.
2. Open only the files you need. Files link to each other with relative links.

## Rules
- **Hard cap: 4096 bytes per file** (`scripts/check-docs-size.sh`, run in CI). If a file grows past it, split by subtopic and add the new file to `README.md`.
- One subject per file. No duplication: link instead of copying.
- Lead with facts: repo URL, version, license, status on the first line.
- Dense Markdown: short bullets and tables, no badges, no images, no long prose.
- English. Dates absolute (YYYY-MM-DD).
- Mark guesses as "(unverified)".
- Every file must be listed in `README.md` (ideas: in `ideas/README.md`). Indexes stay under 4 KB too.

## Layout
```
README.md     entry point (index)
org/          cross-cutting: overview, architecture, stack, dependencies, licenses
projects/     one file per repo (or per small group of repos)
ideas/        proposals, one folder per author (ideas/<github-login>/); rules in ideas/README.md
tasks/        open issues/PRs per repo + prioritized todo (regenerate on re-survey)
meta/         this file
scripts/check-docs-size.sh   size + index check (CI)
```

## Updating
- When a repo changes in a way that affects these facts (new service, dep bump, merge, archive), update the matching file in the same PR or right after.
- Update the snapshot date in README.md when you re-survey.
- Ideas are not facts: `org/` and `projects/` describe what exists; proposals live in `ideas/` until done, then their facts move into `org/` or `projects/`.
