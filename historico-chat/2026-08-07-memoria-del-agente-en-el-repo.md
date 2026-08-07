<!-- sesion: 1ce57ecc-c109-4bb7-a79f-45e94b7f24be -->

# 2026-08-07 — Sesión

## Conversación

### 1 · Usuario — 2026-08-07 14:49:13
> hay que agregar a la instalacion que nada debe quedar en 
> "C:/Users/user/.claude/projects/<ruta-proyecto>/memory";  sino que debe quedar en: historico-chat/memory. Si se entiende mi petición?

**Agente** — 2026-08-07 14:50:26
<!-- agente: ff49cde8-562c-49da-83cb-71366ef042d1 -->

Sí, se entiende. Lo que pido confirmar antes de tocar nada:

**Lo que entendí:** que `instalar.py` deje instalado en *cada* proyecto la norma de que la memoria persistente del agente se escriba en `<proyecto>/historico-chat/memory/` — y que la carpeta `~/.claude/projects/<ruta>/memory/` quede vacía, no como copia ni como índice.

**Cómo tendría que hacerse** (no hay ajuste de Claude Code que reubique esa carpeta; es instrucción + verificación):

1. `instalar_historico()` crea también `historico-chat/memory/` con su `memory.md` (índice) desde una plantilla nueva, sellada como los demás heredados.
2. `hook_sesion.py` inyecta la norma en `additionalContext` cada sesión — es lo único que hace que el agente la escriba ahí y no en la carpeta local.
3. `checklist.py` la revisa: si aparecen archivos en `~/.claude/projects/<ruta>/memory/`, lo marca como pendiente.
4. Va como regla en `base/13-documentacion.md` o `15-registros-inmutables.md` + entrada en `CHANGELOG.md` y subida de `VERSION` (MAYOR: obliga a un proyecto al día a mover su memoria).

**La duda que sí cambia el trabajo:** hoy este repo tiene la convención opuesta — la carpeta local guarda *punteros* y el repo el texto ([memory.md:3](historico-chat/memory/memory.md#L3), y `MEMORY.md` local). ¿"Nada debe quedar" incluye borrar esos punteros y reescribir esa convención, o los punteros se quedan y lo que se prohíbe es que el *texto* viva allá?

Confirmame eso y lo implemento.

### 2 · Usuario — 2026-08-07 15:23:46
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\02-flujo-de-trabajo\reglas\F1-carga-el-contexto-antes-de-actuar.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> toda la memoria se guarda en el <proyecto>/historico-chat/memory/

**Agente** — 2026-08-07 16:04:25
<!-- agente: 4b7a1e7f-2c76-4e05-ab14-f88d83b57539 -->

Escribo el código. Empiezo por el módulo y su enganche.

Ahora el enganche:

Ahora el instalador:

Ahora las pruebas:

Hecho. La memoria del agente ahora es un componente más de la instalación.

**La norma** — `base/01-conducta.md` · **`C19`** (nueva): la memoria va en `historico-chat/memory/` del proyecto, un archivo por recuerdo, y el almacén de la herramienta queda vacío — ni texto ni puntero. Va en `01` y no en `13` por lo mismo que `C18`: ese capítulo se carga literal en cada sesión.

**Que se cumpla sin acordarse** — [recuerdos.py](validadores/recuerdos.py) resuelve dónde guarda Claude Code la memoria de cada proyecto y la **mueve**; [hook_recuerdos.py](validadores/hook_recuerdos.py) lo corre en `SessionStart` (lo que quedó de antes) y en `PostToolUse`·`Write|Edit` (el recuerdo recién escrito, antes de que la sesión termine con él en la carpeta equivocada). Nada se pisa: el idéntico se borra, el de nombre ocupado entra como `-local.md` y se avisa. La comparación ignora mayúsculas — en Windows `MEMORY.md` y `memory.md` son el mismo archivo.

**Que llegue solo** — [instalar.py](validadores/instalar.py) crea la carpeta con su índice sellado ([plantillas/memoria.md](plantillas/memoria.md), nueva) y vacía el almacén local en la misma corrida; el componente `recuerdos` reprueba el checklist si falta la carpeta, si el índice quedó viejo o si algo sigue afuera. `CLAUDE.md.plantilla` §2.4 lo documenta como cuarta carpeta del proyecto.

**Versión 3.0.0** — MAYOR: un proyecto al día tiene que correr `instalar.py "<proyecto>" --aplicar` para mover la suya. No toqué ningún otro proyecto.

**En este repo:** las 16 punteros del almacén local se borraron (verifiqué uno por uno que fueran punteros con su texto completo ya en el repo; respaldo en el scratchpad por si acaso), `memory.md` quedó sellado, y los dos enganches nuevos entraron en `.claude/settings.json`.

Dos cosas que no son mías: la suite queda en **198/199** y `validar.py estandar` da 14 avisos — todos de las reglas `F14`–`F20` y `F4.x` que otra sesión está escribiendo ahora mismo, con citas todavía sin enlazar. Mis archivos pasan limpios.

¿Reviso algo antes de que lo leas, o te digo qué commitear cuando lo apruebes?

### 3 · Usuario — 2026-08-07 16:05:45
> que hizo ?

**Agente** — 2026-08-07 16:05:58
<!-- agente: 6907b8cc-f054-42e3-9680-0553131c4a12 -->

Cambié el estándar para que la memoria del agente viva en el repo. Concreto, archivo por archivo:

**Nuevos**
- [validadores/recuerdos.py](validadores/recuerdos.py) — sabe dónde guarda Claude Code la memoria de un proyecto (`~/.claude/projects/<slug>/memory/`) y la **mueve** a `historico-chat/memory/`.
- [validadores/hook_recuerdos.py](validadores/hook_recuerdos.py) — el enganche que lo ejecuta al abrir sesión y cada vez que se escribe un archivo.
- [plantillas/memoria.md](plantillas/memoria.md) — el índice que se instala como `historico-chat/memory/memory.md`.

**Modificados**
- [base/01-conducta.md](base/01-conducta.md) — regla nueva `C19`: la memoria se escribe en el repo; el almacén de la herramienta queda vacío.
- [validadores/instalar.py](validadores/instalar.py) — crea la carpeta sellada y vacía el almacén local; registra los dos enganches nuevos.
- [validadores/checklist.py](validadores/checklist.py) + [versiones.py](validadores/versiones.py) — componente `recuerdos`: reprueba si falta la carpeta o si algo sigue afuera.
- [plantillas/stack-instalacion.md](plantillas/stack-instalacion.md), [plantillas/CLAUDE.md.plantilla](plantillas/CLAUDE.md.plantilla) §2.4 — lo declaran como componente y como carpeta del proyecto.
- [VERSION](VERSION) 2.4.0 → **3.0.0** y su entrada en [CHANGELOG.md](CHANGELOG.md).
- [validadores/pruebas.py](validadores/pruebas.py) — 9 pruebas nuevas · [reglas-validables.md](validadores/reglas-validables.md), [validadores/README.md](validadores/README.md), [anatomia/mapa-del-sitio.md](anatomia/mapa-del-sitio.md), [CLAUDE.md](CLAUDE.md), [historico-chat/memory/memory.md](historico-chat/memory/memory.md).

**En esta máquina**
- Vacié `C:/Users/user/.claude/projects/c--Ing--Jose-ia-agente/memory` (eran 16 punteros; el texto ya estaba en el repo — respaldo en el scratchpad).
- Agregué los dos enganches a `.claude/settings.json` de este repo.

Nada commiteado todavía.

### 4 · Usuario — 2026-08-07 16:07:22
> también en histórico debe quedar cada una de la sesiones que se crean para que la sesión pueda leer ese histórico

**Agente** — 2026-08-07 16:24:19
<!-- agente: 97a67fbb-4c68-488d-8643-e5f7ff634474 -->

Ahora la garantía del índice y el contexto que se inyecta:

Ahora el enganche de arranque, que es quien lo inyecta:

Ahora las pruebas de lo nuevo:

Listo. Ahora el histórico no solo se escribe: se lee.

**Cada sesión queda registrada, sin excepción**
- [historico.py](validadores/historico.py) — la línea del índice se comprueba **en cada mensaje**, no solo al crear el archivo. Si al crearlo no había `README.md`, esa sesión quedaba invisible para siempre. Es idempotente.
- [enlaces.py](validadores/enlaces.py) — `historico-chat/` entra en las carpetas con índice obligatorio: una sesión sin su línea pasa a ser **falla**, y una línea que apunta a un archivo renombrado, aviso. Ya había una perdida —`2026-08-07-sesion-6.md`—, le puse su línea.

**La sesión nueva lo lee al arrancar** — [hook_sesion.py](validadores/hook_sesion.py) le inyecta al agente, además de las reglas base:

| Qué | De dónde |
|---|---|
| Índice de la memoria | `historico-chat/memory/memory.md` |
| Índice del histórico | las últimas 40 sesiones, con el tema de cada una |

Va el **índice, no el contenido**: las transcripciones son la conversación entera y llenarían la ventana. El agente abre con `Read` la que le sirva — pero para eso tiene que saber que existe. Son 6 KB en total; lo verifiqué corriendo el enganche contra este repo.

Y se cargan **también en el propio estándar**, que era el hueco grande: aquí el enganche salía sin hacer nada, así que la memoria que ayer movimos al repo no la habría leído nadie.

**Documentado y versionado** — `plantillas/historico-chat.md` explica por qué el índice importa y que renombrar sin corregir la línea lo rompe; [validadores/README.md](validadores/README.md) gana la sección del `SessionStart`; **3.1.0** MENOR en el [CHANGELOG](CHANGELOG.md). 6 pruebas nuevas, **205** en total.

Sigue en 204/205 y 14 avisos de citas: todo de las reglas `F4.x` y `F14`–`F20` que otra sesión está escribiendo en paralelo. Ojo con eso al commitear — esa sesión también va a tocar `VERSION` (sus checklists ya dicen v2.5.0 y yo la dejé en 3.1.0).

Nada commiteado. ¿Lo revisás?

### 5 · Usuario — 2026-08-07 16:24:41
> suba
