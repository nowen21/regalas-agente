# Pendiente: cada enganche se puede suspender desde Cimiento

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: [hallazgo 1 del resumen del 2026-10-08](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-08/suspender-enganches.md); seguimiento en scilit: [pendiente 037](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-08/pendientes/037-esperando-a-cimiento-cada-enganche-se-puede-suspender/pendiente.md) |

## El problema

Desde Cimiento se puede suspender una regla en un proyecto, pero de los enganches solo se puede suspender el freno (`hook_antes.py` y `hook_despues.py`). Los demás no tienen cómo apagarse en un proyecto, y en git la única salida es `--no-verify`, que salta todas las revisiones a la vez y no deja rastro.

Lo que ya existe y se reutiliza:

- El modelo `Suspension` (`proyectos/cimiento/core/proyectos/models.py`) ya guarda tipo, nombre, motivo, vencimiento (máximo 30 días), quién la creó y quién la levantó.
- `ajustes.py` acepta el tipo `enganche`, pero solo con el valor `freno`. Además bloquea `hook_historico.py` en `NO_SE_SUSPENDEN`.
- Solo el freno lee las suspensiones (`core/enganches/niveles.py`).
- El docstring de `core/comun/enganches.py` dice que cada proyecto decide qué enganches tiene prendidos. Ningún código lo hace.

El enganche no se puede apagar quitándolo de `.claude/settings.json`: el checklist (`core/validadores/checklist.py`, `_enganches_claude`) lo echa de menos y marca la instalación como incompleta en cada mensaje. Por eso el enganche se queda instalado y, al arrancar, revisa si está suspendido. Si lo está, sale sin hacer nada.

Decisiones del usuario (sesión del 2026-10-08 en scilit):

1. **Se suspende un momento concreto de un enganche, no el guion entero.** Ejemplo: «consumo al terminar la respuesta». Cada entrada de `HOOKS_CLAUDE` necesita un nombre fijo, porque hoy se reconocen por el nombre del guion, y `hook_historico`, `hook_resumen`, `hook_presupuesto` y `hook_recuerdos` corren en más de un momento.
2. **Todos los enganches se pueden suspender, el histórico incluido.** La pantalla muestra junto a cada uno la recomendación de no suspenderlo y el motivo. `NO_SE_SUSPENDEN` desaparece. El freno sigue deteniendo lo que viole el núcleo aunque esté suspendido, como ya hace hoy.
3. **Una sola consulta a la base por mensaje.** El primer enganche que corre trae la lista de suspendidos y la deja para los demás. No se suma demora a lo que ya registra el [pendiente 143](../143-los-enganches-demoran-cada-respuesta/pendiente.md).
4. **Las revisiones de git entran en la misma pantalla**, cada una por separado (`versionado`, `marcas`, `plan`, `pruebas`, etc.), con motivo, vencimiento y recomendación. Como git puede correr fuera de una sesión del agente, consulta la base de datos una vez por cada guardado.

Antes de construir, cerrar los cambios sin guardar de EP-029·HU-004 en `core/proyectos/views.py` y `ajustes.py`, que son los mismos archivos que hay que tocar.

## Por qué importa

Cuando un enganche estorba en un proyecto, porque demora o porque falla, hoy no hay forma de apagarlo sin que el checklist marque la instalación como incompleta. En git, saltar una revisión con `--no-verify` las salta todas y no deja registro de quién lo hizo, por qué ni hasta cuándo.
