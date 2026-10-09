// `EP-028·HU-007`, fase B · Abre el gasto en Chrome sin ventana, pulsa cada pestaña y
// cuenta lo que se ve: si su contenido llegó, si quedó marcada y cuántos «?» tienen globo.
//
// Uso, con Cimiento en marcha:
//   node historico-chat/scripts/2026-10-08/ver_pestanas.mjs <sessionid> [http://127.0.0.1:8015]
// El sessionid sale de una sesión abierta en Cimiento (la cookie «sessionid»).
import { spawn } from "node:child_process";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const [sesion, base = "http://127.0.0.1:8015"] = process.argv.slice(2);
if (!sesion) { console.error("Falta el sessionid."); process.exit(2); }

const CHROME = "C:/Program Files/Google/Chrome/Application/chrome.exe";
const PUERTO = 9333;
const chrome = spawn(CHROME, ["--headless=new", "--disable-gpu", `--remote-debugging-port=${PUERTO}`,
  `--user-data-dir=${mkdtempSync(join(tmpdir(), "cimiento-"))}`, "--window-size=1400,1000", "about:blank"]);

const esperar = ms => new Promise(r => setTimeout(r, ms));
let pagina;
for (let i = 0; i < 50 && !pagina; i++) {
  await esperar(200);
  try { pagina = (await (await fetch(`http://127.0.0.1:${PUERTO}/json/list`)).json()).find(t => t.type === "page"); } catch {}
}
const ws = new WebSocket(pagina.webSocketDebuggerUrl);
await new Promise(r => ws.addEventListener("open", r));
let id = 0;
const pendientes = new Map();
const errores = [];
ws.addEventListener("message", ({ data }) => {
  const m = JSON.parse(data);
  if (m.id && pendientes.has(m.id)) { pendientes.get(m.id)(m); pendientes.delete(m.id); }
  if (m.method === "Runtime.exceptionThrown") errores.push(m.params.exceptionDetails.exception?.description || m.params.exceptionDetails.text);
  // `htmx:sendAbort` no es una falla: es la pestaña nueva cancelando la que cargaba (hx-sync).
  if (m.method === "Runtime.consoleAPICalled" && m.params.type === "error"
      && !/htmx:(sendAbort|afterRequest)/.test(m.params.args[0]?.value || "")) errores.push(m.params.args.map(a => a.value ?? a.description).join(" "));
  if (m.method === "Network.requestWillBeSent" && m.params.request.url.includes("/gasto/pestana/"))
    pedidos.set(m.params.requestId, { url: m.params.request.url.replace(base, ""), desde: Date.now() });
  if (m.method === "Network.loadingFinished" && pedidos.has(m.params.requestId)) {
    const p = pedidos.get(m.params.requestId);
    console.log(`   pedido ${p.url} tardó ${Date.now() - p.desde} ms`);
  }
});
const pedidos = new Map();
const cdp = (method, params = {}) => new Promise(r => { const n = ++id; pendientes.set(n, r); ws.send(JSON.stringify({ id: n, method, params })); });
const evaluar = async expr => (await cdp("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise: true })).result?.result?.value;

await cdp("Runtime.enable");
// Sin ventana, la página no tiene el foco y el «?», que abre al recibirlo, no abriría.
await cdp("Emulation.setFocusEmulationEnabled", { enabled: true });
await cdp("Network.enable");
await cdp("Network.setCookie", { name: "sessionid", value: sesion, url: base });
await cdp("Page.navigate", { url: `${base}/gasto/` });
await esperar(Number(process.env.ESPERA_INICIAL || 3000));

const estado = `(() => {
  const activa = document.querySelector('#pestanas a.nav-link.active');
  const cuerpo = document.getElementById('pestana');
  return {
    direccion: location.search,
    activa: activa && activa.textContent.trim(),
    contenido: cuerpo && (cuerpo.querySelector('[hx-get]') || {}).getAttribute?.('hx-get'),
    cargando: !!(cuerpo && /Cargando/.test(cuerpo.textContent)),
    tablas: cuerpo ? cuerpo.querySelectorAll('table').length : -1,
    graficas: cuerpo ? cuerpo.querySelectorAll('.apexcharts-canvas').length : -1,
    ayudas: cuerpo ? cuerpo.querySelectorAll('.ayuda-icono').length : -1,
    ayudas_con_globo: cuerpo ? [...cuerpo.querySelectorAll('.ayuda-icono[data-bs-toggle="popover"]')].filter(e => window.bootstrap && bootstrap.Popover.getInstance(e)).length : -1,
    htmx: typeof htmx !== 'undefined', bootstrap: typeof bootstrap !== 'undefined',
  };
})()`;

console.log("al abrir:", JSON.stringify(await evaluar(estado)));
const nombres = await evaluar(`[...document.querySelectorAll('#pestanas a.nav-link')].map(a => a.textContent.trim())`) || [];
for (const [n, nombre] of nombres.entries()) {
  await evaluar(`document.querySelectorAll('#pestanas a.nav-link')[${n}].click()`);
  await esperar(Number(process.env.ESPERA || 1500));
  console.log(`pulsada «${nombre}»:`, JSON.stringify(await evaluar(estado)));
  if (process.env.CAPTURA === nombre) {
    const { result } = await cdp("Page.captureScreenshot", { format: "png" });
    writeFileSync(new URL("pestanas.png", import.meta.url), Buffer.from(result.data, "base64"));
  }
}
// Un «?» de la pestaña que llegó por htmx: al pulsarlo abre su globo.
const globo = await evaluar(`(async () => { const i = document.querySelector('#pestana .ayuda-icono'); if (!i) return 'no hay «?»';
  i.click(); i.focus(); await new Promise(r => setTimeout(r, 500)); const p = document.querySelector('.popover');
  return p ? 'abre: ' + p.querySelector('.popover-header').textContent.trim() : 'no abre'; })()`);
console.log("el «?» de la última pestaña:", globo);

// La carrera: se pulsa «Dónde se gasta» mientras el Resumen todavía carga, y después
// llega el aviso de gasto nuevo (lo que pasa cuando el agente está trabajando).
await cdp("Page.navigate", { url: `${base}/gasto/` });
await esperar(400);
await evaluar(`document.querySelectorAll('#pestanas a.nav-link')[1].click()`);
await esperar(3000);
console.log("pulsada «Dónde se gasta» mientras cargaba el Resumen:", JSON.stringify(await evaluar(estado)));
await evaluar(`document.querySelectorAll('#pestanas a.nav-link')[0].click()`);
await esperar(3000);
await evaluar(`document.body.dispatchEvent(new Event('actualizar'))`);
await esperar(100);
await evaluar(`document.querySelectorAll('#pestanas a.nav-link')[3].click()`);
await esperar(3000);
console.log("pulsada «Ahorro» justo después del aviso de gasto nuevo:", JSON.stringify(await evaluar(estado)));

// Lo que reportó el usuario: en «Dónde se gasta» se pulsa un botón de agrupar y después otra pestaña.
await evaluar(`document.querySelectorAll('#pestanas a.nav-link')[1].click()`);
await esperar(2500);
await evaluar(`document.querySelectorAll('#pestana .btn-group button')[1].click()`);
await esperar(2500);
console.log("agrupado por el segundo botón:", JSON.stringify(await evaluar(estado)));
await evaluar(`document.querySelectorAll('#pestanas a.nav-link')[2].click()`);
await esperar(2500);
console.log("pulsada «Contexto» después de agrupar:", JSON.stringify(await evaluar(estado)));

const encima = await evaluar(`(() => { const a = document.querySelector('#pestanas a.nav-link:not(.active)'); if (!a) return null;
  const r = a.getBoundingClientRect(); const e = document.elementFromPoint(r.x + r.width / 2, r.y + r.height / 2);
  return e === a || a.contains(e) ? 'la pestaña' : (e ? e.tagName + '.' + e.className : 'nada'); })()`);
console.log("lo que recibe el clic sobre una pestaña:", encima);
console.log("errores de la consola:", errores.length ? errores : "ninguno");
ws.close();
chrome.kill();
