# 2026-08-20 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-20-core-del-agente-en-la-herramienta.md](../../2026-08-20-core-del-agente-en-la-herramienta.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** «el agente ya cumple esto: agent/core/ (orchestrator, state, budget, planner, errors) ???»

---

## Hallazgos de esta sesión

### H-1 · El `core/` de `notas/estructura.md` no existe como código en el repo, y por diseño no debe existir

- **Qué pasó.** El usuario preguntó si el agente ya cumple la capa `agent/core/` de [notas/estructura.md](../../../notas/estructura.md) §2 (orquestador, estado, presupuesto, planificador, errores). Se revisó el repo pieza por pieza.
- **Por qué importa.** Esa capa es el *loop* del agente. Este repo es el estándar + el linter de proceso; el loop lo ejecuta la herramienta, y [adaptadores/contrato.md](../../../adaptadores/contrato.md) lo declara así. Confundir «no está escrito acá» con «no se cumple» llevaría a reimplementar lo que la herramienta ya hace.
- **Qué se decidió.** Nada nuevo: se confirma lo que dejó H-2 del 19-08. Orquestador y planificador existen como **criterio** (`skills/sdd-orchestrator`, `skills/planificar-tareas`); el estado, como checkpoint en texto (`plantillas/ciclo-vida-proyectos/10-estado-fase.md`); el presupuesto, como medición sin corte (`validadores/presupuesto.py`, v27.0.0); la jerarquía de errores del dominio no existe y `validadores/errores.py` es otra cosa (comprueba `05·E1/E5` en los proyectos). Si el usuario quiere corte por presupuesto o estado reanudable con `run_id`, eso es pendiente nuevo, no hallazgo.
- **Dónde queda.** Las dos fisuras del `core/` bajaron por la cadena (`02·F23`): pendientes [64](../../../pendientes/hecho/el-checkpoint-se-reclama-solo.md) y [65](../../../pendientes/hecho/el-consumo-se-ve-a-tiempo.md) → HU-013 y HU-014 de EP-005 → fases [`A-EP-005-HU-013-el-enganche-del-checkpoint`](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-013-el-checkpoint-se-reclama-solo/A-EP-005-HU-013-el-enganche-del-checkpoint/README.md) y [`A-EP-005-HU-014-el-aviso-por-tramo`](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-014-el-consumo-se-ve-a-tiempo/A-EP-005-HU-014-el-aviso-por-tramo/README.md), aprobadas por el usuario, ejecutadas y cerradas con veredicto Cumple (8 de 8 casos cada una). Versión 27.1.0, instalada en los 9 proyectos. Los dos pendientes pasaron a `hecho/`.
- **Estado:** resuelto acá.

### H-2 · El enganche de apertura no le carga las reglas de `base/` al propio estándar

- **Qué pasó.** El usuario preguntó por qué el agente hace cosas que las reglas no dicen, si se cargan al abrir. Se corrió `hook_sesion.py` a mano: para este repo devuelve **solo** la memoria y el índice del histórico. En [adaptadores/claude-code/hook_sesion.py](../../../adaptadores/claude-code/hook_sesion.py) `main()` sale antes de llamar a `cargador.contexto()` cuando el proyecto es la propia carpeta del estándar («el propio estándar no se revisa a sí mismo»). Está así desde la **primera versión** del enganche (`4000f40`, 2026-08-05: `return 0` seco para la carpeta del estándar), y la evidencia lo confirma: de las **30 aperturas de sesión** que la herramienta conserva de este repo (del 16 al 20 de agosto, incluida la del banco de evals del 19), **ninguna** trae el bloque `[REGLAS BASE DEL ESTÁNDAR]`. No es de hoy: nunca llegaron. Y aunque no saliera: `instalar.cumple_f13()` da `False` para esta carpeta (no tiene `proyectos/`), así que llegaría solo el gate `F13`.
- **Por qué importa.** El `CLAUDE.md` §0 manda cargar todos los capítulos de `base/` al abrir, y lo explica: sin eso «el agente escribe el estándar sin haber leído el estándar». Hoy eso pasa en cada sesión de este repo, y explica esta misma sesión: se trabajó copiando una fase en vez de seguir `02` y las plantillas.
- **Qué se decidió.** Bajó por la cadena: pendiente [66](../../../pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md) → fase `B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar` (defecto del `CA-01` de HU-009), aprobada, ejecutada y cerrada: `hook_sesion.py` entrega `base/` también en esta carpeta, con 7 casos y un caso nuevo en `evals/`. Queda por confirmar desde afuera en la próxima apertura (CP-006 del resultado). Mientras tanto, en esta sesión se cargó `base/` completo a mano.
- **Lo que el usuario veía no era esto.** Al abrir cada sesión aparecen los mensajes de estado de los enganches («Revisando el estándar…», «Recogiendo la memoria…», «Preparando el resumen…») y, en los proyectos herederos, el banner de la revisión de arranque. Eso es el proceso corriendo. Las reglas van **solo** por `additionalContext`, que no se dibuja nunca —a propósito: son decenas de KB—, así que **desde la pantalla no hay forma de saber si llegaron**. Es la única pieza del arranque que nada muestra y nada comprueba; un caso en `evals/` lo cubriría.
- **Estado:** resuelto acá.
- **Dónde queda.** [pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md](../../../pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md) · fase [`B-EP-005-HU-009`](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar/README.md) · señal S-007. La decisión sobre `F13` quedó en el plan: al estándar no se le aplica el gate, porque no es un proyecto.

### H-3 · El andamio deja un enlace roto en cada fase que levanta

- **Qué pasó.** Al levantar las tres fases del día con `validadores/andamio.py`, `validar.py estandar` reportó el mismo enlace roto en los tres `resultado_pruebas.md`: la plantilla enlaza `../../base/08-pruebas.md`, que vale desde `plantillas/planes/` y no desde la carpeta de la fase.
- **Por qué importa.** El andamio existe para que la fase nazca bien; un esqueleto que nace roto se corrige a mano en cada fase.
- **Qué se decidió.** El usuario pidió corregir los hallazgos en vez de dejarlos anotados. Bajó por la cadena y se cerró el mismo día: fase `C-EP-004-HU-005`, el andamio traslada los enlaces al copiar. 27.2.0.
- **Estado:** resuelto acá.
- **Dónde queda.** [pendientes/hecho/el-andamio-no-deja-enlaces-rotos.md](../../../pendientes/hecho/el-andamio-no-deja-enlaces-rotos.md) · señal S-010.

### H-4 · La suite de `validadores/tests/` estaba en rojo por causas ajenas a las fases del día

- **Qué pasó.** La no regresión de las tres fases (454 casos) dejó dos fallas que ninguna tocó: el resumen [historico-chat/resumenes/2026-08-19/sesion-3.md](../2026-08-19/sesion-3.md) tiene un hallazgo sin la `H-` del molde, y cuatro enlaces reprueban `13·DOC14`, dos de ellos escritos por los propios enganches del histórico y del resumen.
- **Por qué importa.** Una suite en rojo por causas viejas esconde la falla nueva: hubo que leer siete fallas una por una para separar las tres de la sesión. Y un enganche que escribe enlaces que el estándar reprueba agrega uno por sesión.
- **Qué se decidió.** No tocarlo desde las fases de la mañana (`02·F8`); bajó por la cadena como fase `C-EP-004-HU-008` y se cerró en la tarde: los dos enganches escriben índices legibles y la suite entera volvió a `OK` (473 casos). 27.2.0.
- **Estado:** resuelto acá.
- **Dónde queda.** [pendientes/hecho/la-corrida-entera-vuelve-a-verde.md](../../../pendientes/hecho/la-corrida-entera-vuelve-a-verde.md) · señal S-011.

### H-5 · Lo que más costó del día no fue el código sino la mitad mecánica de la cadena

- **Qué pasó.** El usuario preguntó cómo hacer que Cimiento haga más y gaste menos. Medido sobre la propia sesión: bajar tres defectos por la cadena fueron unas quince escrituras de índice a mano por defecto y doce copias del veredicto al cerrar, y el código fue lo corto.
- **Por qué importa.** La cadena es lo que el estándar exige y lo que más cuesta cumplir; cada copia a mano es una contradicción esperando y fichas gastadas en lo que un programa hace sin opinar.
- **Qué se decidió.** Dos pendientes (69 y 70) que el usuario pidió corregir de una: el andamio levanta también la historia y el pendiente con sus índices (fase `B-EP-007-HU-003`), y el veredicto se copia solo a la historia y los README (fase `C-EP-005-HU-003`). Las dos cerradas y estrenadas sobre sus propias fases. 27.2.0.
- **Estado:** resuelto acá.
- **Dónde queda.** [pendientes/hecho/el-andamio-levanta-la-historia-y-el-pendiente.md](../../../pendientes/hecho/el-andamio-levanta-la-historia-y-el-pendiente.md) · [pendientes/hecho/el-veredicto-se-copia-solo.md](../../../pendientes/hecho/el-veredicto-se-copia-solo.md) · señales S-012 y S-013.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ |
| Todo hallazgo abierto tiene su pendiente creado | ☑ no queda ninguno abierto: los cinco se resolvieron |
| Toda historia disparada está escrita en su épica | ☑ (HU-013, HU-014, y las fases nuevas de HU-009, HU-005, HU-008, EP-007·HU-003 y EP-005·HU-003) |
| Lo que se hizo está aprobado y guardado | ☐ aprobado; falta el commit, que el usuario autoriza aparte |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
