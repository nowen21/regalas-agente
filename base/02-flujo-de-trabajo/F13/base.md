# F13 · Estructura base obligatoria del proyecto

> **Fuente única de la regla F13.** El índice `02-flujo-de-trabajo.md` solo la referencia; el detalle vive aquí. La estructura está definida en la plantilla `plantillas/base-proyecto.md`.

## Alcance — solo valida estructura

F13 hace **una sola cosa: validar que exista la estructura base** para que el agente pueda armar su espacio de trabajo. No detecta el stack, no conoce el propósito, el dominio ni la funcionalidad del proyecto.

Si durante F13 el agente usa información del stack, el propósito o el dominio, **el flujo está mal**: eso corresponde a etapas posteriores, no a F13.

## El gate: la carpeta `proyectos/`

Al arrancar, el agente valida **un solo hecho**: **¿existe la carpeta `proyectos/`?** — donde el usuario coloca el/los código(s) fuente.

- **SÍ** → el agente **crea su espacio de trabajo** (`.agente/`, `prompts/`, `documentacion/`) al lado y continúa.
- **NO** → **no cumple**: el agente **no crea nada**, **se detiene** y **orienta al usuario** para que cree `proyectos/` y coloque ahí el código. El usuario decide la ubicación y los nombres (ej. RNI: `proyectos/rni-back/` + `proyectos/rni-front/`) — el agente **no lo asume**.

## Qué crea el agente y qué no

- **Crea y gestiona:** su propio espacio — `.agente/`, `prompts/`, `documentacion/` (aditivo, al lado de `proyectos/`).
- **Nunca toca:** el código dentro de `proyectos/`. No lo modifica, no lo reestructura, no asume su organización.

## Regla general

`proyectos/` (código del usuario) y el espacio del agente son **mundos separados**. El agente valida el gate (`proyectos/` existe) **antes de cualquier acción**; sin él, no continúa. Crear y organizar `proyectos/` corresponde **exclusivamente al usuario**.
