# UI libraries

## pixi-components (`@openhotel/pixi-components`)
Repo: github.com/openhotel/pixi-components · npm · LICENSE CC BY-SA 4.0 (package.json wrongly says `NC BY-SA 4.0`).

React bindings + prefabs on top of Pixi.js for game clients. `src/components/{core,prefabs}`, hooks, utils. Storybook, Vite build to `dist/index.es.js`.
Consumers: openhotel 0.1.9, game-template/battleship 0.0.24, game-utils 0.0.29 (peer).
Proposed (pagoru): stays; bump everyone to latest, fix license string and README badges (point to old `openhotel/components`).

## web-components (`@openhotel/web-components`)
Repo: github.com/openhotel/web-components · npm · CC BY-NC-SA 4.0 (package.json says `NC BY-NC-SA 4.0`).

React 18 + Sass CSS-module components for web apps: account-item, card, form, hotel-card, icons, layout, license, palette, social, tooltip; hooks (modal, theme, layout, click-outside); `styles.scss` (colors, mixins). Storybook. ~35 scss files, ~1,970 lines.
Consumers: auth 0.3.9, web 0.3.3, asset-editor 0.3.3. static still on legacy `@oh/components`.
Proposed (pagoru): becomes `app/ui` in the monorepo (openhotel/openhotel), rewritten to Tailwind. See [restructuring](../ideas/pagoru/restructuring.md).
