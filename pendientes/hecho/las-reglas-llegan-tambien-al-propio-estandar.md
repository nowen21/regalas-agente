# Pendiente · Las reglas de `base/` no le llegan al propio estándar al abrir la sesión

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-005 · HU-009 — Lo que gobierna cada frase llega puesto al abrir la sesión](../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md) — su `CA-01` dice que los capítulos que rigen cada frase llegan con su texto; en la carpeta del estándar no llegan |
| **De dónde sale** | El H-2 del resumen [../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

En [adaptadores/claude-code/hook_sesion.py](../../adaptadores/claude-code/hook_sesion.py), `main()` sale antes de llamar a `cargador.contexto()` cuando la carpeta es la del propio estándar: entrega la memoria y el índice del histórico, y nada más. Está así desde la primera versión del enganche (`4000f40`, 2026-08-05).

Se midió sobre lo que la herramienta conserva: **30 aperturas de sesión** de este repositorio entre el 16 y el 20 de agosto, y **ninguna** trae el bloque `[REGLAS BASE DEL ESTÁNDAR]`.

Hay un segundo tramo detrás: aunque esa salida no existiera, `instalar.cumple_f13()` da falso para esta carpeta (no tiene `proyectos/`), y el cargador entregaría solo el gate `F13`. El propio instalador ya sabe que esta carpeta no es un proyecto (`es_el_estandar()`); el cargador no lo sabe.

## Por qué importa

El `CLAUDE.md` de este repositorio manda en su §0 cargar todos los capítulos de `base/` al abrir, y explica por qué: sin eso "el agente escribe el estándar sin haber leído el estándar". Eso pasó en cada sesión desde que el enganche existe, y la sesión del 2026-08-20 lo mostró: se trabajó copiando una fase hecha en vez de seguir el capítulo `02`.

**Lo que el usuario veía no era esto.** Al abrir aparecen los mensajes de estado de los enganches y, en los proyectos herederos, el banner de la revisión. Las reglas van solo por `additionalContext`, que no se dibuja. Desde la pantalla no hay forma de saber si llegaron: es la única pieza del arranque que nada muestra y nada comprueba.

## Qué falta

Que para la carpeta del estándar el enganche entregue las reglas completas (el gate `F13` no le aplica: no es un proyecto, es donde viven las reglas), sin dejar de entregar la memoria y el histórico, y sin correr la revisión de instalación, que ahí no tiene qué revisar. Y un caso que compruebe que el bloque de reglas llega, para que no vuelva a faltar quince días sin que nadie lo note.

## El límite

No cambia lo que reciben los proyectos herederos, que ya lo reciben bien.

## Cómo se sabrá que cerró

Correr `hook_sesion.py --raiz <carpeta del estándar>` devuelve un `additionalContext` con el bloque `[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]` y el texto de `00-nucleo-blindado.md`. Con caso automatizado, y la próxima apertura de sesión lo trae.
