# 2026-08-16 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-16-sesion.md](../../2026-08-16-sesion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** —, es trabajo nuevo.

---

## Hallazgos de esta sesión

### H-1 · Guardar las reglas en una base de datos: qué se gana y qué se pierde

- **Qué pasó:** el usuario preguntó qué pasaría si todas las reglas se pasaran a una base de datos. El agente contestó que se perdería la revisión en git, que Claude lee texto y que cada proyecto necesitaría conexión a la base. Lo tercero está mal y el usuario lo corrigió: el estándar ya vive en una carpeta central y ningún proyecto lo copia, así que la base sería de Cimiento y los proyectos seguirían preguntándole a Cimiento igual que hoy.
- **Por qué importa:** la pregunta toca dónde vive la fuente de las reglas, que es de lo que cuelga todo lo demás — el versionado, la aprobación de un cambio y cómo llegan las reglas a la sesión. Sin dejarlo escrito, la discusión se repite desde cero.
- **Qué lo soluciona:** nada todavía; es una discusión de diseño, no un defecto. Lo que quedó en claro es el criterio con que se decidiría: el texto sigue siendo la fuente y la base se **genera** a partir de él, para consultar y no para guardar.
- **Qué se decidió:** sin decidir.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** —, mientras no haya decisión.
- **Orden de resolución:** 2 de 2 · va después del H-3, que es deuda de esta misma sesión.
- **Dónde queda:** [pendientes/37](../../../pendientes/37-donde-vive-la-fuente-de-las-reglas.md).
- **Nace en:** 2026-08-16 · sesión sin nombrar.
- **Cerrado en:** —
- **Con qué se retoma:** si la base de datos guarda las reglas, ¿con qué se reemplaza lo que hoy da git — ver qué cambió en una regla y aprobarlo antes de que rija?

### H-2 · Quedarse en una versión vieja del estándar: ¿aviso o incumplimiento?

- **Qué pasó:** hablando de qué pasa cuando se deroga una regla, se vio que el proyecto no se actualiza solo: declara su versión en su `CLAUDE.md` y ahí se queda hasta que el usuario decida subirla. [`validadores/version.py`](../../../validadores/version.py) reporta ese desfase como **aviso**, no como error. El usuario no aceptó esa lectura: *"aunque me diga que no es un incumplimiento sí lo es porque no está cumpliendo el estándar"*.
- **Por qué importa:** define contra qué se mide "cumple el estándar" — contra la versión que el proyecto adoptó o contra la vigente. Hoy es la adoptada, y por eso un proyecto puede quedarse atrás para siempre sin que ningún reporte lo llame incumplimiento. Con la otra definición, toda derogación deja trabajo abierto en cada proyecto hasta que se cierre.
- **Qué lo soluciona:** lo que faltaba era el amarre — el momento exacto en que el desfase deja de tolerarse. Se escribió como regla nueva, con la fase como amarre: abrir y cerrar una fase ya son paradas donde alguien revisa y firma.
  **EP-004 · HU nueva — comprobar el desfase con derogación**
  - **Como** dueño de un proyecto que hereda el estándar
  - **Quiero** que la comprobación falle sola cuando entre mi versión y la vigente hay una derogación sin adoptar
  - **Para** no descubrir el atraso leyendo el `CHANGELOG.md` a mano
  - **Contexto:** [`validadores/version.py`](../../../validadores/version.py) ya compara la versión declarada con la vigente, pero solo avisa. Falta leer del `CHANGELOG.md` qué versiones trajeron derogación y cobrarlo al abrir y al cerrar fase. Sin eso, [`02·F22`](../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) depende de que alguien se acuerde.
- **Qué se decidió:** ninguna fase se abre ni se cierra mientras el proyecto declare una versión anterior a la que derogó una regla que ese proyecto cumplía. Lo único que se abre es la fase que la adopta, una por cada HU que implementaba la regla derogada, y al cerrarla se sube la versión declarada — lo puso el usuario: adoptar no es cambiar el número, es trabajo, y el trabajo va en fases. Fuera de esos momentos el desfase se reporta pero no detiene nada. Quedó como [`02·F22`](../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) en la versión 19.0.0 (MAYOR) — se numeró así porque otra sesión, en paralelo, ya había tomado la 18.0.0 para el cambio de «brief» a «planteamiento».
- **Estado:** resuelto acá — la regla, escrita; su comprobación automática, programada.
- **Responde a:** —
- **Dispara:** 1. [EP-004 · HU-015](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md) — la comprobación del desfase con derogación; se construyó en esta sesión y le falta su fase (ver H-3).
- **Orden de resolución:** —
- **Dónde queda:** la regla, en [`02·F22`](../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md); la comprobación, en [`validadores/version.py`](../../../validadores/version.py) (`derogaciones`, `sin_adoptar`, `validar_fase`) llamada desde [`validadores/flujo.py`](../../../validadores/flujo.py), registrada en [`validadores/reglas-validables.md`](../../../validadores/reglas-validables.md) y documentada en [`validadores/docs/version.md`](../../../validadores/docs/version.md); versionada en [`CHANGELOG.md`](../../../CHANGELOG.md) 19.0.0. Se corrigieron dos textos que decían lo contrario: la nota de retroactividad de [`base/20-meta-reglas/base.md`](../../../base/20-meta-reglas/base.md) y [`plantillas/stack-instalacion.md`](../../../plantillas/stack-instalacion.md).
- **Nace en:** 2026-08-16 · sesión sin nombrar.
- **Cerrado en:** 2026-08-16 · sesión sin nombrar.
- **Con qué se retoma:** —

### H-3 · El validador de la F22 se programó sin pasar por la cadena

- **Qué pasó:** el usuario aprobó programar la comprobación y el agente la escribió derecho en [`validadores/version.py`](../../../validadores/version.py) y [`validadores/flujo.py`](../../../validadores/flujo.py). Eso es desarrollo, y [`02·F0`](../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) pide `épica → HU → especificación → plan → código`, sin atajos por tamaño. No hubo HU ni fase: el código existe y su cadena no.
- **Por qué importa:** es el mismo repo que escribe la regla, incumpliéndola mientras la escribe. Y sin fase no hay plan aprobado ni cierre, así que el código quedó sin el registro que lo justifica.
- **Qué lo soluciona:** retrodocumentar el trabajo como fase de EP-004, con su HU y su cierre, usando [`plantillas/retrodocumentacion.md`](../../../plantillas/retrodocumentacion.md).
  **EP-004 · HU nueva — la comprobación del desfase con derogación**
  - **Como** dueño de un proyecto que hereda el estándar
  - **Quiero** que la comprobación falle sola cuando hay una regla derogada sin adoptar
  - **Para** no descubrir el atraso leyendo el `CHANGELOG.md` a mano
  - **Contexto:** el código ya está escrito y probado a mano; falta la HU, la fase y su cierre. Sin eso, [`02·F22`](../../../base/02-flujo-de-trabajo/reglas/F22-no-avances-de-fase-con-una-derogacion-sin-adoptar.md) tiene validador pero no tiene rastro de cómo nació.
- **Qué se decidió:** sin decidir — el agente lo reporta, el usuario decide si se retrodocumenta o se deja anotado.
- **Estado:** abierto.
- **Responde a:** —
- **Dispara:** 1. [EP-004 · HU-015](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md), escrita, con su fase de retrodocumentación todavía sin abrir.
- **Orden de resolución:** 1 de 2 · va antes del H-1: es deuda de esta misma sesión.
- **Dónde queda:** [pendientes/38](../../../pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md).
- **Nace en:** 2026-08-16 · sesión sin nombrar.
- **Cerrado en:** —
- **Con qué se retoma:** ¿se retrodocumenta el validador como fase de EP-004, o se deja el código con su registro pendiente?

### H-4 · "Menos es más" no era norma, era un reclamo que se repetía

- **Qué pasó:** el usuario cortó una respuesta larga con *"menos es más"* y pidió que fuera regla. Estaba solo en la memoria del agente ([respuestas cortas](../../memory/respuestas-cortas.md)), que es preferencia, no norma; y se venía repitiendo desde el 2026-08-14.
- **Por qué importa:** lo que solo está en la memoria no lo hereda ningún proyecto y no lo revisa nadie. La regla que ya existía, [`00·ID7`](../../../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), pide que el texto se entienda, no que sea corto: un texto puede entenderse perfecto y no leerse por largo.
- **Qué lo soluciona:** se escribió como regla del estándar, extendiendo a `ID7` en vez de repetirla.
- **Qué se decidió:** [`00·ID9 · Di lo mismo en menos palabras`](../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md), en la versión 20.0.0 (MAYOR). La menor extensión con la que se entienda; lo que no cabe corto va al archivo y en el mensaje queda su enlace.
- **Estado:** resuelto acá.
- **Responde a:** —
- **Dispara:** —
- **Orden de resolución:** —
- **Dónde queda:** la regla, en [`00·ID9`](../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md); registrada como no validable en [`validadores/reglas-validables.md`](../../../validadores/reglas-validables.md); versionada en [`CHANGELOG.md`](../../../CHANGELOG.md) 20.0.0. La memoria [respuestas cortas](../../memory/respuestas-cortas.md) ahora apunta a la regla.
- **Nace en:** 2026-08-16 · sesión sin nombrar.
- **Cerrado en:** 2026-08-16 · sesión sin nombrar.
- **Con qué se retoma:** —

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-2 y H-4, con su regla y su versión |
| Todo hallazgo abierto tiene su pendiente creado | ☑ [37](../../../pendientes/37-donde-vive-la-fuente-de-las-reglas.md) y [38](../../../pendientes/hecho/el-validador-de-la-f22-tiene-su-fase.md) |
| Toda historia disparada está escrita en su épica | ☑ [EP-004 · HU-015](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-015-derogacion-sin-adoptar/HU-015-derogacion-sin-adoptar.md) |
| Lo que se hizo está aprobado y guardado | ☑ commit `2030a4c` · falta commitear lo de este cierre |

**Se puede cerrar** en cuanto se commitee este cierre. Los dos hallazgos abiertos quedaron anotados con su archivo, que es la otra forma válida de terminarlos.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: resumen sin hallazgos -->

<!-- aviso: falta decir si la sesión se puede cerrar -->
