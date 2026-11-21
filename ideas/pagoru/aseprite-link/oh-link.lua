-- OpenHotel Aseprite link (Aseprite extension).
-- Install: download oh-link.aseprite-extension from the web page and double-click it,
-- or Edit > Preferences > Extensions > Add Extension. Then File > Scripts > OpenHotel Link.
--
-- Kept generic on purpose: the web decides what to do, this script only offers primitives.
-- Bump VERSION only when the protocol below changes.
--
-- Text messages, web -> Aseprite (space separated):
--   hello                          -> replies "hello <VERSION>"
--   deny <webVersion>              -> versions differ, the plugin disconnects
--   command <Name> key=value ...   -> app.command.<Name>{...} (numbers and true/false are converted)
--   frame                          -> sends the current frame
--   sheet                          -> sends the sprite sheet (JSON text + PNG)
--   live <on|off>                  -> send the current frame on every change
-- Messages, Aseprite -> web:
--   text   "hello <VERSION>", "error <text>", "sheet <json>"
--   binary "<kind> <width> <height>\n" .. png bytes   (kind: frame | sheet)
local VERSION = "1"
local URL = "ws://127.0.0.1:48621/ws?role=aseprite"

local ws
local dlg
local connected = false
local live = true
local hooked

local tempFile = function(name)
  return app.fs.joinPath(app.fs.tempPath, name)
end

local readFile = function(path)
  local f = io.open(path, "rb")
  if not f then return nil end
  local data = f:read("a")
  f:close()
  return data
end

local setStatus = function(text)
  if dlg then dlg:modify{ id = "status", text = text } end
end

local send = function(text)
  if connected then ws:sendText(text) end
end

local sendPng = function(kind, path, width, height)
  local data = readFile(path)
  if not data then return send("error cannot read " .. path) end
  ws:sendBinary(kind .. " " .. width .. " " .. height .. "\n", data)
end

local parseValue = function(value)
  if value == "true" then return true end
  if value == "false" then return false end
  return tonumber(value) or value
end

local isAlive = function(sprite)
  return sprite ~= nil and pcall(function() return sprite.width end)
end

local commands = {}

commands.hello = function()
  send("hello " .. VERSION)
end

commands.deny = function(webVersion)
  connected = false
  ws:close()
  setStatus("Update needed: web " .. tostring(webVersion) .. ", plugin " .. VERSION)
end

commands.command = function(name, ...)
  local command = name and app.command[name]
  if not command then return send("error unknown command " .. tostring(name)) end
  local params = {}
  for _, pair in ipairs{ ... } do
    local key, value = pair:match("^([^=]+)=(.*)$")
    if key then params[key] = parseValue(value) end
  end
  local ok, err = pcall(command, params)
  if not ok then send("error " .. name .. " " .. tostring(err)) end
end

commands.frame = function()
  local sprite = app.sprite
  if not sprite then return send("error no sprite open") end
  local path = tempFile("oh-link-frame.png")
  local image = Image(sprite.width, sprite.height, sprite.colorMode)
  image:drawSprite(sprite, app.frame)
  image:saveAs{ filename = path, palette = sprite.palettes[1] }
  sendPng("frame", path, sprite.width, sprite.height)
end

commands.sheet = function()
  local sprite = app.sprite
  if not sprite then return send("error no sprite open") end
  local png = tempFile("oh-link-sheet.png")
  local json = tempFile("oh-link-sheet.json")
  local ok, err = pcall(app.command.ExportSpriteSheet, {
    ui = false,
    askOverwrite = false,
    type = SpriteSheetType.PACKED,
    textureFilename = png,
    dataFilename = json,
    dataFormat = SpriteSheetDataFormat.JSON_ARRAY,
    listLayers = true,
    listTags = true,
    listSlices = true,
  })
  if not ok then return send("error sheet " .. tostring(err)) end
  send("sheet " .. (readFile(json) or "{}"))
  local image = Image{ fromFile = png }
  sendPng("sheet", png, image.width, image.height)
end

commands.live = function(state)
  live = state ~= "off"
  if dlg then dlg:modify{ id = "live", selected = live } end
  if live and app.sprite then commands.frame() end
end

local onChange = function()
  if live and connected and app.sprite then commands.frame() end
end

-- Follows the active sprite and frame.
local hook = function()
  if isAlive(hooked) then hooked.events:off(onChange) end
  hooked = app.sprite
  if hooked then hooked.events:on("change", onChange) end
  onChange()
end

local onText = function(data)
  local words = {}
  for word in data:gmatch("%S+") do words[#words + 1] = word end
  local name = table.remove(words, 1)
  local handler = commands[name]
  if not handler then return send("error unknown message " .. tostring(name)) end
  handler(table.unpack(words))
end

local onReceive = function(type, data, err)
  if type == WebSocketMessageType.OPEN then
    connected = true
    setStatus("Connected, plugin " .. VERSION)
    commands.hello()
  elseif type == WebSocketMessageType.CLOSE then
    if connected then setStatus("Disconnected (retrying)") end
    connected = false
  elseif type == WebSocketMessageType.ERROR then
    setStatus("Error: " .. tostring(err or data))
  elseif type == WebSocketMessageType.TEXT then
    onText(data)
  end
end

local stop = function()
  app.events:off(hook)
  if isAlive(hooked) then hooked.events:off(onChange) end
  hooked = nil
  if ws then ws:close() end
  ws = nil
  connected = false
end

local start = function()
  if dlg then return dlg:show{ wait = false } end
  ws = WebSocket{
    url = URL,
    onreceive = onReceive,
    deflate = false,
    minreconnectwait = 1,
    maxreconnectwait = 5,
  }
  dlg = Dialog{
    title = "OpenHotel Link " .. VERSION,
    onclose = function() stop(); dlg = nil end,
  }
  dlg:label{ id = "status", text = "Connecting to " .. URL }
  dlg:newrow()
  dlg:check{ id = "live", text = "Live", selected = live, onclick = function() commands.live(dlg.data.live and "on" or "off") end }
  dlg:button{ text = "Reconnect", onclick = function() ws:close(); ws:connect() end }
  dlg:show{ wait = false }
  app.events:on("sitechange", hook)
  ws:connect()
  hook()
end

function init(plugin)
  plugin:newCommand{
    id = "OpenHotelLink",
    title = "OpenHotel Link",
    group = "file_scripts",
    onclick = start,
  }
end

function exit(plugin)
  stop()
end
