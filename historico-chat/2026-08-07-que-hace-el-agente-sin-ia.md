<!-- sesion: e3350f0b-0dae-4f74-bb72-993b3195e75d -->

# 2026-08-07 — Que hace el agente sin ia

## Conversación

### 1 · Usuario — 2026-08-07 07:39:46
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\historico-chat\reglas-2026-08-06\reglas.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> que capacidades tiene el agente sin la ayuda de la ia?

**Agente** — 2026-08-07 07:41:14
<!-- agente: b4539ff7-65a7-4ead-86fe-2230d1185606 -->

Sin IA, lo que queda del repo es **todo lo determinista en Python** (solo biblioteca estándar, salvo el visor y la búsqueda semántica). Es harto: valida, engancha, recuerda, mide y se instala solo. Lo que se pierde es el criterio — las reglas de `base/`, las skills y los prompts son texto que alguien (o algo) tiene que aplicar.

**Lo que funciona sin IA**

| Capacidad | Cómo se usa | Depende de IA |
|---|---|---|
| 23 validadores ([validadores/](validadores/)) — enlaces, plantillas, commits, fases, trazabilidad, secretos, SQL/shell, N+1, FK, migraciones, CI, rama, lockfile… | `python validadores/validar.py <sub>` | No |
| Corredores de herramientas del stack (`linter`, `suite`, `audit`) — detectan el ecosistema por el manifiesto | `validar.py linter` | No |
| 5 enganches automáticos ([.claude/settings.json](.claude/settings.json)): enlaces tras editar `.md`, revisión al abrir sesión, histórico usuario+agente, checklist de instalación | corren solos | No¹ |
| Hook de git `commit-msg` — bloquea el commit que incumpla `09·G2` | `git config core.hooksPath .githooks` | No |
| Memoria por señales ([memoria/memoria.py](memoria/memoria.py)) — SQLite+FTS5: `add`, `search`, `supersede`, `revisar`, `archivar`, `pendientes`, `cerrar` | CLI | No |
| Búsqueda semántica local ([memoria/semantica.py](memoria/semantica.py)) — embeddings en la máquina, opt-in | `memoria.py indexar` | Modelo local, no API |
| Métricas del proceso ([metricas/metricas.py](metricas/metricas.py)) — deuda diferida, vigencia, señales por estado | CLI | No |
| Visor web ([interfaz/](interfaz/)) — Django + AdminLTE, offline, lee reglas/skills/plantillas/notas y la memoria | `python interfaz/manage.py runserver` | No |
| Instalador ([validadores/instalar.py](validadores/instalar.py)) — replica hooks, `historico-chat/` y el stack a cualquier proyecto | `python instalar.py` | No |
| Chequeo de desfase de versión estándar vs proyecto | `validar.py version` | No |

¹ El hook del histórico *lee* el transcript que produce Claude Code, así que registra IA; pero el que escribe es Python.

**Lo que no funciona sin IA:** las reglas de [base/](base/) (texto normativo), las 11 [skills/](skills/) (analizar proyecto, diseñar arquitectura, generar spec, revisar crítico…), los [prompts/](prompts/), y todo lo que el README de validadores llama *"lo que necesita criterio"* — puertas del flujo, calidad de una spec, si una decisión fue buena.

En una frase: sin IA tienes un **linter de proceso + una memoria de proyecto + un visor**, que se autoinstalan; lo que no tienes es quien redacte, decida o revise.

### 2 · Usuario — 2026-08-07 07:49:26
> # Prompt
>
> Dentro de la carpeta **`inventario`**, agregue un documento en formato **Markdown (.md)** con la explicación que me acaba de dar sobre cómo funciona el agente.
>
> El documento debe quedar redactado de forma clara, organizada y fácil de entender, de manera que sirva como referencia para comprender los componentes, recursos y elementos que conforman el agente.
>
> Además, analice si el nombre de la carpeta **`inventario`** es el más adecuado para la intención del contenido que se va a almacenar allí. Si considera que existe un nombre más representativo, proponga una o varias alternativas y justifique por qué serían más apropiadas.

### 3 · Usuario — 2026-08-07 07:50:42
> pero por qué está analizando diplomado si esa no fue la instrucción

### 4 · Usuario — 2026-08-07 07:51:36
> inventario no está y debe quedar en la raíz del proyecto

**Agente** — 2026-08-07 07:55:28
<!-- agente: 16092438-c6ed-4d08-9662-346f7c38e436 -->

Listo: [inventario/componentes-del-agente.md](inventario/componentes-del-agente.md) — creada la carpeta en la raíz y el documento dentro.

El documento cubre: las dos mitades (determinista vs. criterio), el inventario general por carpeta, y luego el detalle de lo que corre sin IA — validadores con sus 23 comprobaciones agrupadas, los 5 enganches, memoria, métricas, visor e instalador — más lo que sí necesita IA y por qué. `validar.py estandar` no reporta nada sobre la carpeta nueva (las 20 fallas que salen son previas y de `diplomado-ia/`).

**Sobre el nombre `inventario`**

No es el mejor. Un inventario **cuenta existencias**: dice cuántas cosas hay, no cómo funcionan. El documento que acaba de quedar ahí explica el mecanismo — por qué el hook va en `.githooks/`, por qué el histórico lo escribe un script y no el agente, por qué hay dos severidades. Eso es anatomía, no conteo. Con el nombre `inventario` el lector espera una lista y encuentra una explicación.

Alternativas, en orden de recomendación:

| Nombre | Por qué | Contra |
|---|---|---|
| **`anatomia/`** | Dice exactamente la intención: de qué está hecho el agente y cómo encajan las piezas. No se confunde con ninguna carpeta existente. | Palabra poco común en repos |
| `como-funciona/` | Literal, imposible de malinterpretar. | Nombre largo y con verbo |
| `manual/` | Coherente con el `Manual-Estandar-Agente.docx` que ya está en la raíz; sería su versión viva en Markdown. | Sugiere instrucciones de uso, no descripción interna |

Descarto `arquitectura/` (choca con la skill `disenar-arquitectura`, que trata la arquitectura *del proyecto*, no la del agente) y `catalogo/` (mismo problema que `inventario`: promete lista).

Mi voto es **`anatomia/`**.

Dos cosas antes de seguir: si acepta el cambio de nombre lo hago; y sea cual sea el nombre, hay que agregar la fila a la tabla de `CLAUDE.md` §3 para que quede claro qué va ahí y qué no — eso es cambio de estándar, así que dígame si lo hago. No he hecho commit.

### 5 · Usuario — 2026-08-07 07:58:38
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\.claude\settings.json in the IDE. This may or may not be related to the current task.</ide_opened_file>
> listo entonces que se llame anatomia

**Agente** — 2026-08-07 07:59:03
<!-- agente: 4ea32533-c538-49ab-9187-f453d0999e7c -->

Renombrada: [anatomia/componentes-del-agente.md](anatomia/componentes-del-agente.md). Los enlaces internos del documento son relativos (`../base/`, `../validadores/`), así que no se rompió ninguno — el validador no reporta nada.

Queda pendiente lo otro que le pregunté: agregar la fila a la tabla de [CLAUDE.md](CLAUDE.md) §3 («Dónde va cada cosa») para dejar escrito que en `anatomia/` va la descripción de cómo funciona el agente — y así distinguirla de `notas/`, que guarda el *por qué* de las decisiones. Eso toca el estándar, así que espero su visto bueno. Tampoco he hecho commit.

### 6 · Usuario — 2026-08-07 07:59:56
> # Prompt
>
> Dentro de la misma carpeta **`anatomia`**, cree un documento en formato **Markdown (.md)** que contenga el **mapa del sitio** del agente.
>
> Este documento debe representar de forma jerárquica toda la estructura del agente, mostrando las carpetas, archivos y componentes principales, así como la relación entre ellos. El objetivo es que cualquier persona pueda comprender rápidamente cómo está organizado el agente y dónde se encuentra cada elemento.
>
> El mapa del sitio debe mantenerse actualizado cada vez que se agreguen, eliminen o modifiquen componentes dentro del agente, de manera que siempre refleje la estructura real del proyecto.

**Agente** — 2026-08-07 08:06:43
<!-- agente: a51e17d1-0983-44bd-bcd4-3c7acd94f067 -->

Listo: [anatomia/mapa-del-sitio.md](anatomia/mapa-del-sitio.md). Sin enlaces rotos.

Cómo quedó armado:

1. **Cuatro zonas** — Norma (`base/`, `plantillas/`, `skills/`), Herramientas (`validadores/`, `memoria/`, `metricas/`, `interfaz/`), Bitácora (`historico-chat/`, `notas/`, `pendientes/`, `anatomia/`) y Apoyo. Con el dato que más se olvida: solo la zona Norma viaja a los proyectos que heredan el estándar.
2. **El árbol completo** anotado archivo por archivo — los 21 capítulos de `base/`, las 23 plantillas, las 11 skills, y `validadores/` agrupado por tema (documentación, git, seguridad, código, instalación, enganches) en vez de alfabético, que era ilegible.
3. **Quién usa a quién** — que `plantillas.py` lee las plantillas reales, que `checklist.py` saca la lista de `stack-instalacion.md`, que los `hook_*.py` no tienen lógica propia. Cierra con la cadena regla → validador → enganche → instalador.
4. **Lo que existe en disco pero no en el repo** — `senales.db`, `.claude/`, `proyectos.md` y por qué cada uno está en `.gitignore`.
5. **Cómo mantenerlo al día** — la regla, una tabla de "si el cambio hace X, actualice la sección Y", y los dos comandos para verificar.

Dos cosas para su decisión, ninguna hecha todavía:

- Lo de mantenerlo actualizado hoy queda como texto dentro del propio documento. Si quiere que se **cumpla siempre** y no cuando alguien se acuerde, el camino del repo es el de siempre: escribirlo en `CLAUDE.md` y, si se puede comprobar sin criterio, un validador que compare el árbol del mapa contra el disco. Eso es cambio de estándar — dígame si lo hago.
- Sigue pendiente la fila de `anatomia/` en la tabla §3 de [CLAUDE.md](CLAUDE.md).

No he hecho commit.

### 7 · Usuario — 2026-08-07 08:15:31
> osea que el agente todavía no está en capacidad de ejecutar las fases de una HU?

**Agente** — 2026-08-07 08:16:06
<!-- agente: 9ea7ea26-e60d-4c83-b9d9-950ab584595b -->

Sí está en capacidad. Lo que falta no es **ejecutar** las fases, es **comprobar mecánicamente** que se ejecutaron bien.

Son dos cosas distintas y las mezclé en la respuesta anterior:

| | Estado |
|---|---|
| **Ejecutar** una HU y sus fases | ✅ Está. [`sdd-orchestrator`](skills/sdd-orchestrator/SKILL.md) dirige 13 estaciones con sus puertas, las 11 skills hacen el trabajo de cada estación, y el estado se persiste en `estado-fase.md` para sobrevivir a la compactación. |
| **Comprobar** que se ejecutó bien | ⚠️ Parcial. ~50 reglas ya tienen validador; quedan ~9 sin cubrir. |

De las 13 estaciones, 7 puertas son suyas (alcance, épica, HUs, spec, plan, commit, despliegue) y 6 son internas. Todas se ejecutan hoy.

Lo que **sí** falta, y es lo que dije mal:

- **`F2` — que no haya código de una fase sin su spec y su plan aprobados.** Hoy esa puerta la verifica el agente leyendo, no un script. Es la más pesada del backlog porque hay que cruzar el código de la fase contra su spec, no solo revisar carpetas ([pendientes/01](pendientes/01-validadores-de-codigo-de-proyecto.md)).
- **La trazabilidad hasta el commit.** La de documentación (épica↔HU, ORIGEN, tabla de cierre) sí está automatizada en `trazabilidad.py`.
- **Cinco reglas más** (`EST1`, parte de `EST2`, `D1`, `IM2`/`IM5`) que necesitan que el proyecto declare su convención en `.agente/` — sin eso no hay contra qué comparar.

La diferencia práctica: si el agente se salta la puerta `F2`, hoy nada lo detiene mecánicamente. El resto de las puertas sí tienen validador o enganche detrás.

Y el punto honesto: **nada de esto se ha corrido punta a punta contra un proyecto real** — no hay nada bajo `proyectos/`. Los validadores que faltan quedaron pendientes precisamente porque no se pueden construir "en seco".

### 8 · Usuario — 2026-08-07 08:19:28
> # Prompt
>
> Analice el agente e identifique qué funcionalidades, procesos, validaciones o automatizaciones podrían implementarse para que funcionen de manera autónoma, sin depender de la intervención de la IA durante su ejecución.
>
> Con base en ese análisis, cree un documento en formato **Markdown (.md)** dentro de la carpeta **`pendientes`** con todas las ideas identificadas.
>
> Para cada propuesta incluya, como mínimo:
>
> * Nombre de la funcionalidad.
> * Descripción.
> * Problema que resolvería.
> * Beneficio esperado.
> * Cómo podría automatizarse sin depender de la IA.
> * Prioridad (Alta, Media o Baja).
> * Complejidad estimada (Alta, Media o Baja).
> * Dependencias, si existen.
> * Recomendaciones para su implementación.
>
> El objetivo es construir un backlog de funcionalidades que permitan que el agente sea cada vez más autónomo, automatizando tareas repetitivas y reduciendo la necesidad de intervención de la IA cuando estas puedan resolverse mediante reglas, validaciones, procesos o mecanismos programables.

**Agente** — 2026-08-07 08:26:00
<!-- agente: b5bc4aaa-188f-4fc4-b9f4-e8c1e917d60d -->

Analizado. Encontré 16 automatizaciones reales — verifiqué en el código que ninguna existe ya. Escribo el backlog.

Listo: [pendientes/09-autonomia-sin-ia.md](pendientes/09-autonomia-sin-ia.md), con su fila en el índice de [pendientes/README.md](pendientes/README.md). Sin hallazgos del validador.

**16 propuestas**, cada una con los 9 campos que pidió. Las verifiqué en el código antes de proponerlas — ninguna existe ya.

Los seis de prioridad Alta:

| # | Qué | Complejidad |
|---|---|---|
| 01 | Guardián de versión y CHANGELOG en `pre-commit` | Baja |
| 02 | Barrido de secretos en `historico-chat/` | Baja |
| 03 | Sello de puerta por CLI (`estado.py`) | Baja |
| 04 | Manifiesto de convenciones en `.agente/` | Media |
| 05 | Validador de forma de regla (`M4`/`M5`/`M11`) | Media |
| 06 | Gate `F2`: código sin spec | Alta |

Tres hallazgos que salieron del análisis y vale la pena que vea aparte:

- **El histórico puede filtrar un secreto real.** El enganche copia el chat literal a un archivo versionado, y ningún validador lo revisa: `secretos.py` excluye los `.md` a propósito (la documentación muestra secretos de ejemplo) y `versionado.py` mira nombres, no contenido. Si alguien pega un token en el chat, queda en el repo y en el historial de git. Es el ítem 02, y es Alta con complejidad Baja.
- **Nada obliga a subir `VERSION`.** `CLAUDE.md §2` y `M10` dicen que versionar no es opcional, pero no hay validador — verifiqué que ningún `.py` menciona el CHANGELOG. Si se olvida, `version.py` deja de poder detectar el desfase en los proyectos. Ítem 01.
- **Las meta-reglas del capítulo 20 son las únicas que nadie comprueba.** Ítem 05.

El orden sugerido no es el de prioridad: 01 → 02 → 03 → 07 → 08 primero, porque los cinco son de complejidad Baja. El gate `F2` va casi al final aunque sea Alta — depende del 04 y del 12, y sin ellos daría demasiados falsos positivos.

Cierra con una sección de **lo que deliberadamente no propongo**: decidir MAYOR/MENOR/PARCHE, aprobar las puertas de usuario y juzgar si una spec está bien escrita. La frontera es que completitud se comprueba y calidad se juzga.

Sigue pendiente lo de la fila de `anatomia/` en `CLAUDE.md` §3, y no he hecho commit.

### 9 · Usuario — 2026-08-07 12:57:52
> con esas capacidades que haría?

**Agente** — 2026-08-07 12:58:23
<!-- agente: 8a167724-269b-462d-9eca-16470ccb1d62 -->

Empezaría por **no construir nada todavía**.

Los 16 están priorizados por intuición, no por evidencia: nada de esto se ha corrido punta a punta contra un proyecto real, y el [pendiente 01](pendientes/01-validadores-de-codigo-de-proyecto.md) lleva abierto desde el 04-08 esperando exactamente eso. Tomaría un proyecto suyo, lo llevaría de brief a fase cerrada con el orquestador, y anotaría cada vez que tuve que acordarme de algo. Esa lista real reordena el backlog en un día y probablemente descarta dos o tres ítems.

Si hay que construir ya, esto:

**Primer bloque — los cinco de complejidad Baja, juntos.** 01, 02, 03, 07 y 08. Son enganches y comparaciones de cadenas; ninguno necesita diseño. Juntos eliminan la clase entera de "se olvidó": versionar, filtrar un secreto al histórico, anotar el estado, dejar el mapa viejo, publicar sin revisar.

**El primero de todos: el 03 (`estado.py`).** Es el cuello de botella real — los ítems 06, 10 y 11 lo leen. Mientras el estado de la fase sea una redacción y no un dato, tres automatizaciones más quedan bloqueadas. Es también el más barato.

**Después, el 04 (manifiesto de convenciones).** Desbloquea cinco validadores de una sola vez. Es la mejor relación esfuerzo/reglas ganadas del backlog.

**El 06 (`F2`) lo dejaría de último**, aunque sea la puerta que define al estándar. Sin el 03 y el 12 daría tantos falsos positivos que se terminaría desactivando — y un gate desactivado es peor que un gate ausente, porque figura como cubierto.

Qué compra todo eso: el agente deja de gastar contexto en acordarse y lo gasta en decidir. Lo que **no** compra es autonomía de criterio — las siete puertas de usuario (alcance, épica, HUs, spec, plan, commit, despliegue) siguen siendo suyas por diseño, y automatizarlas sería quitarlas.

### 10 · Usuario — 2026-08-07 12:59:56
> explique de manerea sencilla. Recuerde que menos es más

**Agente** — 2026-08-07 13:00:06
<!-- agente: 4ae9ec78-7b10-4467-b18a-0fddc8829e5e -->

Haría esto, en orden:

**1. Probarlo en un proyecto real, antes de construir nada.** Nunca se ha usado de principio a fin. Una sola pasada muestra qué falta de verdad — hoy las 16 ideas están ordenadas por corazonada.

**2. Construir primero las cinco fáciles.** Que el agente no pueda olvidar: subir la versión, tapar un secreto en el histórico, anotar en qué va, mantener el mapa, revisar antes de publicar. Son un par de días y quitan de golpe todos los "se me olvidó".

**3. De esas cinco, arrancar por `estado.py`.** Es la más barata y otras tres dependen de ella.

**4. Dejar el gate `F2` para el final.** Es el más importante, pero si se hace antes de tiempo se equivoca tanto que uno lo termina apagando. Y un control apagado es peor que ninguno, porque uno cree que está.

Al final el agente no tiene que **acordarse** de las cosas, y usa la cabeza en decidir. Lo que sigue siendo suyo son los permisos: aprobar el alcance, la spec, el plan y el commit. Eso no se automatiza — sería quitarlo.
