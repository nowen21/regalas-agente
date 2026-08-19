# La fuente de las reglas es el texto

**Decidido el 2026-08-18** por el usuario, cerrando el [pendiente 37](../pendientes/hecho/donde-vive-la-fuente-de-las-reglas.md). Nació de una pregunta suya: *¿qué pasaría si todas las reglas se guardaran en una base de datos?*

## Qué queda decidido

**Los archivos `.md` de [`base/`](../base/) son la fuente.** No hay otra. Si algún día se construye una base de datos de reglas, se **genera** a partir de ellos: se puede borrar y volver a generar, y ninguna regla vive ahí.

## Por qué

**Lo que se perdería es la revisión, y es lo único que no se puede reponer.** Hoy cambiar una regla deja un archivo modificado: se lee, se compara con la versión anterior y se aprueba en un commit. Una fila que cambia no deja nada que leer ni que aprobar — habría que construir a mano el historial que el control de versiones da gratis.

**Y lo que se ganaría ya se tiene.** Qué reglas dependen de cuál, cuáles son validables, cuáles se derogaron, dónde se cita un identificador: eso lo contestan hoy [`citas.py`](../validadores/citas.py), [`metareglas.py`](../validadores/metareglas.py) y [`relacionadas.py`](../validadores/relacionadas.py), leyendo el texto. La consulta no necesitaba una base; necesitaba que alguien la escribiera.

**El modelo lee texto.** Meter una regla en la sesión significa escribirla como texto. Sacarla de una base para volver a escribirla no ahorra ese paso: lo agrega.

## Lo que esto no cierra

**Una base generada sigue siendo posible**, y para eso hace falta primero una historia de usuario que diga **qué preguntas responde** que hoy no se puedan responder. Sin esa lista, construirla es adelantarse.

## Con qué se relaciona

- [`20·M4`](../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) — el identificador es estable porque commits y fases cerradas lo citan. Eso vale igual en cualquier soporte, y es lo que hace la migración posible más adelante.
- [`20·M11`](../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) — nada se borra. En texto eso se ve; en una tabla hay que acordarse de no hacer `DELETE`.
- [`EP-001 · HU-001`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-001-formato-unico-de-regla/HU-001-formato-unico-de-regla.md) — si la fuente es el texto, «el formato de una regla» es el formato del archivo, y esa historia se lee sin ambigüedad.
