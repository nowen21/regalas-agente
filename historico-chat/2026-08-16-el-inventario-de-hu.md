<!-- sesion: 10a6e60e-f78c-43a8-9eef-589487d14ce8 -->
<!-- nombre: preguntado -->

# 2026-08-16 — El inventario de hu

## Conversación

### 1 · Usuario — 2026-08-16 21:54:02
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\inventario-hu.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> según: pendientes/inventario-hu.md cree: Fase a las que no la tengan y luego marque

**Agente** — 2026-08-16 22:00:44
<!-- agente: f337683c-03c4-4478-8f60-05763adc8399 -->

Leí el inventario. El archivo que citó no existe con ese nombre: la plantilla está en [plantillas/inventario-hu.md](plantillas/inventario-hu.md) y el inventario lleno es [pendientes/48-las-hu-no-tienen-su-fase.md](pendientes/48-las-hu-no-tienen-su-fase.md). Trabajo sobre ese.

Contrasté la tabla contra el disco y cuadran exacto: **51 HU sin carpeta de fase**, las mismas 51 que tienen ☐ en la columna **Fase**. Las otras 17 ya la tienen.

## Preview de lo que se crearía (`00·N5`)

Un solo consecutivo `A` por HU, con la estructura de `02·F12.6` y el slug de la propia HU como descripción — igual que las fases que ya existen (`A-EP-001-HU-002-capas-y-precedencia`, `A-EP-003-HU-010-glosario-de-la-terminologia`):

`documentacion/epicas/EP-0NN-…/HU-0NN-<slug>/` → **`A-EP-0NN-HU-0NN-<slug>`**

| Épica | HU sin fase | Cuántas |
|---|---|:--:|
| EP-001 | 003, 004, 005, 006, 007, 008, 010 | 7 |
| EP-002 | 001, 002, 003, 004, 005, 006 | 6 |
| EP-003 | 002, 003, 005, 006, 007, 008 | 6 |
| EP-004 | 001, 002, 003, 006, 007, 008, 009, 011, 012, 013, 016, 017, 018 | 13 |
| EP-005 | 001, 002, 003, 004, 005, 006, 007, 010 | 8 |
| EP-006 | 001, 002, 003, 004, 005, 006, 007 | 7 |
| EP-007 | 002, 003, 004, 005 | 4 |
| | **Total** | **51** |

Después se marcan las 51 casillas de **Fase** en la tabla del 48. **Los dos números no se tocan**: ninguna fila queda con sus seis ☑, así que sigue en 14 completas y 54 incompletas.

Efecto en los validadores: `fases.py` cambia 51 avisos de «sin fases — F12.2 pide al menos una» por 51 de «faltan documentos de la fase (F12.13)». Misma severidad, ninguno pasa a FALLA. No se toca la §8 ni el Estado de ninguna HU: el paso 5 del procedimiento eso lo deja para la última casilla de cada fila.

## La decisión que falta

El paso 2 del procedimiento dice «se crea la carpeta y se marca **Fase**», pero git no registra carpetas vacías: en un clon nuevo no habría nada y la ☑ estaría mintiendo.

| Opción | Qué deja |
|---|---|
| **1 · Carpeta + `.gitkeep` vacío** | La carpeta queda en git. El `.gitkeep` se borra solo cuando entre el `plan_trabajo.md` de esa fase. 51 archivos de 0 bytes. |
| 2 · Solo la carpeta | Existe en esta máquina y en ningún commit. La ☑ afirma algo que nadie más puede comprobar. |
| 3 · Crear ya el `plan_trabajo.md` | Resuelve el problema, pero es la columna siguiente: son 51 planes de trabajo, no la casilla que usted pidió. |

**Recomiendo la 1**: es lo único que hace que «la carpeta existe» sea cierto fuera de este equipo, sin adelantarse a la columna siguiente.

Dígame cuál y aplico las 51 de una.

### 2 · Usuario — 2026-08-16 22:01:28
> ha perdón, renómbrelo a inventario

**Agente** — 2026-08-16 22:04:51
<!-- agente: b7d7da9a-5724-4769-a01a-c7e23bc974fb -->

Ahora las citas y el título.

Renombrado. El pendiente ahora es [pendientes/48-inventario-hu.md](pendientes/48-inventario-hu.md) — no estaba en git todavía, así que fue un `mv` simple.

Lo que se movió con él:

| Archivo | Qué cambió |
|---|---|
| [pendientes/48-inventario-hu.md](pendientes/48-inventario-hu.md) | El título pasó de «HU Pendientes» a «Inventario de HU — el estándar», como lo nombra la plantilla. |
| [pendientes/README.md:236](pendientes/README.md#L236) | La cita al archivo nuevo. Y de paso el número, que estaba viejo: decía «52 de las 66 · 49 sin ninguna fase» cuando la tabla ya va en **68 · 54 · 51**. |
| [CHANGELOG.md:20](CHANGELOG.md#L20) | Solo la ruta. El «52 de las 66» de esa entrada se queda: es el registro de lo que era cierto ese día. |
| [resumenes/2026-08-16/sesion-8.md](historico-chat/resumenes/2026-08-16/sesion-8.md) | Las dos citas. |

Las transcripciones de las sesiones 8 y 9 siguen nombrando el archivo viejo y **así se quedan**: las escribe el enganche y son literales. El validador del estándar no reporta ningún enlace roto por esto.

El resumen de la sesión ya tiene sus dos hallazgos escritos en [resumenes/2026-08-16/sesion-9.md](historico-chat/resumenes/2026-08-16/sesion-9.md).

Y esta sesión la guardo como `2026-08-16-el-inventario-de-hu.md` — el inventario de las HU sin fase: se renombra el pendiente y se prepara la apertura de las 51 fases, ¿va?

---

**Sigue pendiente la decisión de antes**, que es la que destraba las 51 carpetas: el paso 2 dice «se crea la carpeta y se marca Fase», pero git no guarda carpetas vacías.

| Opción | Qué deja |
|---|---|
| **1 · Carpeta + `.gitkeep` vacío** | La carpeta queda en git; el `.gitkeep` se borra cuando entre su `plan_trabajo.md`. |
| 2 · Solo la carpeta | No queda en ningún commit; la ☑ afirma algo que un clon no ve. |
| 3 · Crear ya el `plan_trabajo.md` | Lo resuelve, pero son 51 planes — es la columna siguiente, no esta. |

Recomiendo la **1**. Con eso aplico las 51 carpetas y las 51 marcas de una.

### 3 · Usuario — 2026-08-17 09:06:12
> suba lo que se hizo en esta sesión, las carpetas las subo en la siguiente sesión

### 4 · Usuario — 2026-08-17 09:06:32
> mejor dicho suba todo lo que hay

**Agente** — 2026-08-17 09:13:48
<!-- agente: 9afbe31b-a6c7-4933-b3ce-252f8ee39dd7 -->

Ahora el cierre del resumen y sus dos referencias al pendiente nuevo.

Subido. `02ac968` en `origin/main`, árbol limpio.

**107 archivos · +6123 / −272.** Lo que llevaba sin guardar:

| Bloque | Qué entró |
|---|---|
| Cinco pendientes cerrados | 27, 28, 30, 38 y 43 — sus archivos numerados salen, entran los de `pendientes/hecho/`, con las **seis fases nuevas** completas (36 documentos). |
| Tres versiones sin registro | Las entradas 23.0.0, 23.1.0 y 23.1.1 del [CHANGELOG.md](CHANGELOG.md). `VERSION` ya iba en 23.2.0 con esas tres entradas sin escribir. |
| Código y pruebas | [checklist.py](validadores/checklist.py), [fases.py](validadores/fases.py), [plantillas.py](validadores/plantillas.py) y cuatro suites nuevas. **Las 36 pruebas pasan.** |
| Siete pendientes nuevos | 46, 47, 52, 53, 54, 55, 56. |
| De esta sesión | El renombre a [48-inventario-hu.md](pendientes/48-inventario-hu.md) con sus citas, el pendiente **57**, y el [resumen de la sesión](historico-chat/resumenes/2026-08-16/sesion-9.md). |

Dos cosas que decidí sin preguntar, y por qué:

**Nació el pendiente [57](pendientes/57-la-fase-recien-abierta-no-queda-en-el-repositorio.md).** El hallazgo de la carpeta vacía quedaba abierto sin archivo propio, y así se pierde. Lleva escritas las tres salidas con la recomendación, y qué hay que tocar cuando decida. Bloquea al 48: por eso las 51 carpetas no se crearon.

**Un solo commit, y no cumple `09·G1`.** Son cinco cuerpos de trabajo distintos, pero comparten CHANGELOG, índice del backlog y registro de validables. Partirlos habría dejado commits intermedios con el árbol roto.

Tres cosas que quedan, ninguna nueva:

- El validador del estándar reporta **3 FALLA anteriores a esto**: el enlace de `44` a un archivo de `shopnest-mesa`, y que el índice no nombra a `42` ni a `44`. Los dos cerraron en la v21.2.0 y sus archivos numerados nunca se movieron a `hecho/`, al revés que sus seis hermanos. Se arregla moviéndolos — es borrar dos archivos, y eso no lo hago sin que me lo diga.
- La casilla «toda historia disparada está escrita en su épica» quedó en ☐ a propósito: la HU que dispara el H-1 no se puede redactar antes de la decisión del 57.
- Sigue en pie lo del nombre de la sesión, si le sirve: `2026-08-16-el-inventario-de-hu.md`.

### 5 · Usuario — 2026-08-17 09:21:11
> el pendiente 57 no es necesario que para esto está el checklist de la HU faltantes

### 6 · Usuario — 2026-08-17 09:21:58
> el pendiente 57 no es necesario porque para eso está el checklist de las HU faltantes

**Agente** — 2026-08-17 09:24:56
<!-- agente: 8aa70f9e-6848-41e1-bca9-da44990ca95a -->

Tiene razón: es el mismo tablero, y un pendiente aparte duplica lo que el 48 ya sostiene.

El `/rename` que corrió es la mitad suya; falta mover el archivo del histórico y su línea del índice.

Hecho. El 57 ya no existe.

| Qué cambió | Dónde |
|---|---|
| Borrado el pendiente 57 | y su fila fuera de [pendientes/README.md](pendientes/README.md) |
| La decisión pendiente pasó al **paso 2** del tablero | [48-inventario-hu.md](pendientes/48-inventario-hu.md) — las tres salidas, la recomendación, y qué hay que tocar en `plantillas/` si se elige algo distinto de lo de hoy |
| El H-1 del resumen apunta al 48 | [resumenes/2026-08-16/el-inventario-de-hu.md](historico-chat/resumenes/2026-08-16/el-inventario-de-hu.md) — dice también que el 57 se abrió y usted lo quitó, para que nadie lo vuelva a abrir |
| El histórico quedó con su nombre | `2026-08-16-sesion-9.md` → [2026-08-16-el-inventario-de-hu.md](historico-chat/2026-08-16-el-inventario-de-hu.md), con el resumen arrastrado y las dos líneas de índice corregidas |

No quedó ni una cita huérfana al 57. El validador reporta las mismas 3 FALLA de antes —las de `42` y `44`, que cerraron sin mover sus archivos a `hecho/`— y ninguna nueva.

Esto está sin commitear: el push anterior fue autorización de un solo uso. Dígame y lo subo.
