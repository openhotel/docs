# Shared migration: dependency versions

Part of [shared migration](shared-migration.md).

## Rule
A package used in more than one `deno.json` or `package.json` has exactly one version, pinned (no `^`). `jsr:x`, `npm:x` and `npm:@jsr/a__b` count as the same package.

## CI
`.github/workflows/deps-versions.yml` (inline Python, no setup) scans every `deno.json` and `package.json` except `node_modules` and `app/shared/old`. On a mismatch it prints every package with each version and file, adds an error annotation per file, and fails.

## Mismatches on 2026-11-17 (15 of 66)
- `@da/bcrypt` 1.0.0 (openhotel/server) vs 1.0.1 (onet)
- `@oh/utils` 1.5.0 / 1.5.2 / 1.5.32 / 1.5.33 (removed by the migration)
- `@openhotel/web-components` 0.3.3 vs 0.3.9 (replaced by shared components)
- `@std/path` 1.0.6 (web, static) vs 1.1.6 (openhotel/server, .docker/dev)
- `@std/yaml` 1.0.5 (apps) vs 1.3.0 (.docker/dev)
- `dayjs`: deno.land/x 0.5.0 (openhotel/server, onet), npm 1.11.13 (4 clients), 1.11.21 (openhotel/client)
- `react`, `react-dom`, `@types/react`: 18.3 (4 clients) vs 19.x (openhotel/client)
- `react-router-dom` 6.26.0 vs 7.18.1; `react-router` 6.26.0 vs 6.26.2
- `@vitejs/plugin-react` ^4.3.1 vs 6.0.3
- `vite` 5.2.14, 6.0.11, 6.1.6, 6.3.6, 8.3.3
- `yaml` 2.4.2, ^2.5.0, 2.9.0; `ulidx` 2.4.1 vs ^2.4.1

Biggest jump: the 4 web clients move to React 19, react-router 7 and vite 8 like openhotel/client.
