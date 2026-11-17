# Shared migration: duplicates across apps

Part of [shared migration](shared-migration.md). Snapshot of `monster` f956b43 (2026-11-17): 946 exports in every app's `src/shared` and `app/shared/src`. 100 names exist in 2+ places: 46 identical, 54 different.

## Identical: move now
- Already in `@shared`, delete the local copy: `RequestMethod` (4 clients), `wait`, `getRandomNumber`, `Size2d`, `getDirection`, `getCrossDirectionFromDirection`, `CollectionCategory`.
- `Scope` enum: auth, web, openhotel servers and onet.
- auth client + server: `EMAIL_REGEX`, `USERNAME_REGEX`, `PROTO_DID_REGEX`, `RestrictionCode`, `DbHotelIntegrationType`.
- openhotel client + server: `TILE_WIDTH`, `TILE_Y_HEIGHT`, `WALL_HEIGHT`, `STEP_TILE_HEIGHT`, `MOVEMENT_BETWEEN_TILES_DURATION`, `MAX_MESSAGE_LENGTH`, `Hemisphere`, `TransactionType`, `MarketplaceListingStatus`, `Room`, `Catalog`, `MarketplaceListing`, `FurnitureDirectionData`, `getNextCrossDirection`.
- asset-editor client + server: `FurnitureDirection`, `FurnitureIcon`, `FurniturePivot`, `SpriteSheet`, `SpriteSheetFrame`, `SpriteSheetMeta`, `SpriteSheetRectangle`.
- `FurnitureAction`: asset-editor + openhotel (openhotel/client has a second, different one).

## Different: unify first
- `Envs` / `getProcessedEnvs`: openhotel adds `upgrade`, onet adds `isDevelopment`.
- asset-editor/server: own copies of `getCORSHeaders`, `appendCORSHeaders`, `getContentType`.
- `getRandomString` in openhotel and asset-editor clients uses `Math.random`; shared uses crypto.
- `waitUntil` (3 versions), `Point3d`, `Size3d` (openhotel/client).
- auth/client `CollectionManifest`, `Collection`, `Hotel`, onet/asset-editor `CollectionFurniture`.
- openhotel client vs server: room types (`BaseRoom`, `PrivateRoom`, `PublicRoom`, `RoomFurniture`, `RoomLayout`, `RoomPoint`, `RoomPointEnum`), catalog, transaction, furniture direction types, `isDoorRenderable`, `isWallRenderable`.
- `FurnitureType`, `FurnitureData`, `FurnitureTexture`, `SpriteSheetSize`, `getPositionFromIsometricPosition` across openhotel and asset-editor.
- auth client vs server: `Connection`, `DbHotel`, `DbHotelIntegration`, `Backup`.

## React (to shared components)
`cn`, `RedirectComponent`, `_TemplateProvider`, `useTemplate`, `useAppSession`, `ContainerComponent`, `TitleProvider`/`useTitle`, `SideContentProvider`/`useSideContent`, `LinkComponent`, `useCookies`, `useAccount`, `useFurniture`, `downloadURI`.

## Keep local
`ConfigTypes`, `CONFIG_DEFAULT`, `useApi`, `Request`, `User`, `Account`, `AccountProvider`, `AppSessionProvider`, `Event`, `File`: same name, different meaning.
