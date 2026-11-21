// OpenHotel Aseprite link test relay.
// Aseprite and the browser are both WebSocket clients, so this relays between them.
// It also serves the test page and the Aseprite extension.
// Run: deno run --allow-net --allow-read relay.ts
const PORT = 48621;
const HOST = "127.0.0.1";
const WEB_ORIGINS = [`http://${HOST}:${PORT}`, `http://localhost:${PORT}`, "https://openhotel.club"];

type Role = "aseprite" | "web";
const clients: Record<Role, Set<WebSocket>> = { aseprite: new Set(), web: new Set() };

const other = (role: Role): Role => (role === "aseprite" ? "web" : "aseprite");

const log = (...args: unknown[]) => console.log(new Date().toISOString().slice(11, 19), ...args);

const isWebOrigin = (origin: string | null) =>
  origin !== null && (WEB_ORIGINS.includes(origin) || origin.endsWith(".openhotel.club"));

const status = () =>
  JSON.stringify({ type: "status", aseprite: clients.aseprite.size, web: clients.web.size });

const broadcastStatus = () => {
  for (const ws of clients.web) if (ws.readyState === WebSocket.OPEN) ws.send(status());
};

const CRC_TABLE = Array.from({ length: 256 }, (_, n) => {
  let c = n;
  for (let k = 0; k < 8; k++) c = c & 1 ? 0xedb88320 ^ (c >>> 1) : c >>> 1;
  return c >>> 0;
});

const crc32 = (data: Uint8Array) => {
  let crc = 0xffffffff;
  for (const byte of data) crc = CRC_TABLE[(crc ^ byte) & 0xff] ^ (crc >>> 8);
  return (crc ^ 0xffffffff) >>> 0;
};

// Minimal zip (stored, no compression), enough for an .aseprite-extension.
const zip = (files: { name: string; data: Uint8Array }[]) => {
  const parts: Uint8Array[] = [];
  const central: Uint8Array[] = [];
  let offset = 0;
  for (const file of files) {
    const name = new TextEncoder().encode(file.name);
    const crc = crc32(file.data);
    const local = new DataView(new ArrayBuffer(30));
    local.setUint32(0, 0x04034b50, true);
    local.setUint16(4, 20, true);
    local.setUint32(14, crc, true);
    local.setUint32(18, file.data.length, true);
    local.setUint32(22, file.data.length, true);
    local.setUint16(26, name.length, true);
    const entry = new DataView(new ArrayBuffer(46));
    entry.setUint32(0, 0x02014b50, true);
    entry.setUint16(4, 20, true);
    entry.setUint16(6, 20, true);
    entry.setUint32(16, crc, true);
    entry.setUint32(20, file.data.length, true);
    entry.setUint32(24, file.data.length, true);
    entry.setUint16(28, name.length, true);
    entry.setUint32(42, offset, true);
    parts.push(new Uint8Array(local.buffer), name, file.data);
    central.push(new Uint8Array(entry.buffer), name);
    offset += 30 + name.length + file.data.length;
  }
  const centralSize = central.reduce((size, part) => size + part.length, 0);
  const end = new DataView(new ArrayBuffer(22));
  end.setUint32(0, 0x06054b50, true);
  end.setUint16(8, files.length, true);
  end.setUint16(10, files.length, true);
  end.setUint32(12, centralSize, true);
  end.setUint32(16, offset, true);
  return new Blob([...parts, ...central, new Uint8Array(end.buffer)]);
};

const readLocal = (name: string) => Deno.readFile(new URL(`./${name}`, import.meta.url));

const handleSocket = (req: Request, url: URL) => {
  const role = url.searchParams.get("role") as Role;
  if (role !== "aseprite" && role !== "web") return new Response("role must be aseprite or web", { status: 400 });
  const origin = req.headers.get("origin");
  if (role === "web" && !isWebOrigin(origin)) return new Response("origin not allowed", { status: 403 });
  log(`connect role=${role} origin=${origin ?? "(none)"}`);

  const { socket, response } = Deno.upgradeWebSocket(req);
  socket.binaryType = "arraybuffer";
  socket.onopen = () => {
    clients[role].add(socket);
    broadcastStatus();
  };
  socket.onmessage = (event) => {
    const isText = typeof event.data === "string";
    const size = isText ? event.data.length : event.data.byteLength;
    log(`${role} -> ${other(role)} ${isText ? "text" : "binary"} ${size}b${isText ? ` "${event.data.slice(0, 80)}"` : ""}`);
    for (const target of clients[other(role)]) {
      if (target.readyState === WebSocket.OPEN) target.send(event.data);
    }
  };
  socket.onclose = () => {
    clients[role].delete(socket);
    log(`close role=${role}`);
    broadcastStatus();
  };
  socket.onerror = () => log(`error role=${role}`);
  return response;
};

Deno.serve({ hostname: HOST, port: PORT }, async (req) => {
  const url = new URL(req.url);

  if (url.pathname === "/ws") return handleSocket(req, url);

  if (url.pathname === "/" || url.pathname === "/index.html") {
    return new Response(await readLocal("index.html"), { headers: { "content-type": "text/html; charset=utf-8" } });
  }

  if (url.pathname === "/oh-link.aseprite-extension") {
    const body = zip([
      { name: "package.json", data: await readLocal("package.json") },
      { name: "oh-link.lua", data: await readLocal("oh-link.lua") },
    ]);
    return new Response(body, {
      headers: {
        "content-type": "application/zip",
        "content-disposition": 'attachment; filename="oh-link.aseprite-extension"',
      },
    });
  }

  return new Response("not found", { status: 404 });
});

log(`relay on http://${HOST}:${PORT}  (page: /, socket: /ws?role=aseprite|web, plugin: /oh-link.aseprite-extension)`);
