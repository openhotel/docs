# asset-editor

Repo: github.com/openhotel/asset-editor · last tag v0.1.5 · CC BY-NC-SA 4.0 · active.

Web tool to build game assets: furniture, collections and sprite sheets, using the shared types from `@oh/core`.

- Server `api/`: `auth`, `collection`, `furniture`, `image`, `version`.
- Client modules: home, application, collection, furniture, sprite-sheet. React 18 + `@openhotel/web-components` 0.3.3, ~23 scss files.
- onet also serves signed collections to hotels; the export path from the editor to onet is not wired in code yet (unverified). See [onet](onet.md).
- Run: `deno task install && deno task start`. devkit port 2030.

Proposed (pagoru): merged into the monorepo (`app/asset-editor` in openhotel/openhotel), Tailwind rewrite. See [restructuring](../ideas/pagoru/restructuring.md).
