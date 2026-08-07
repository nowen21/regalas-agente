# F13 · Estructura base obligatoria del proyecto   ·   `[GATE DE ARRANQUE · PRECONDICIÓN]`

> **Precondición de arranque:** aunque su ID sea `F13`, esta regla **corre primero** — antes de cargar contexto (`F1`) y de cualquier paso del flujo. El número es solo un identificador de catálogo, no orden de ejecución. Se aplica en `CLAUDE.md §3` (paso previo obligatorio).
>
> **Fuente única de la regla F13.** El índice `02-flujo-de-trabajo.md` solo la referencia; el detalle vive aquí. El árbol de la estructura está en el anexo [`estructura-base.md`](estructura-base.md), al lado de este archivo.

## Alcance — solo valida estructura

F13 hace **una sola cosa: validar que exista la estructura base** para que el agente pueda armar su espacio de trabajo. No detecta el stack, no conoce el propósito, el dominio ni la funcionalidad del proyecto.

Si durante F13 el agente usa información del stack, el propósito o el dominio, **el flujo está mal**: eso corresponde a etapas posteriores, no a F13.

## El gate: la carpeta `proyectos/`

Al arrancar, el agente valida **un solo hecho**: **¿existe la carpeta `proyectos/`?** — donde el usuario coloca el/los código(s) fuente.

- **SÍ** → el agente **crea su espacio de trabajo** (`.agente/`, `prompts/`, `documentacion/`) al lado y continúa.
- **NO** → **no cumple**: el agente **no crea nada**, **se detiene** y **muestra al usuario el mensaje de orientación** (abajo). El usuario decide la ubicación y los nombres (ej. RNI: `proyectos/rni-back/` + `proyectos/rni-front/`) — el agente **no lo asume**.

**Mensaje de orientación (cuando `proyectos/` NO existe):**

```
⚠️ No puedo continuar: falta la estructura base.

No existe la carpeta `proyectos/`, donde debe vivir el código fuente.

Para continuar, creá:
    proyectos/
    └── <tu-proyecto>/     ← coloca aquí tu código (uno o varios proyectos)

Vos decidís la organización y los nombres. Cuando `proyectos/` exista,
creo mi espacio (.agente/, prompts/, documentacion/) y sigo.
No adecúo el proyecto por mi cuenta.
```

## Qué crea el agente y qué no

- **Crea y gestiona:** su propio espacio — `.agente/`, `prompts/`, `documentacion/` (aditivo, al lado de `proyectos/`).
- **Nunca toca:** el código dentro de `proyectos/`. No lo modifica, no lo reestructura, no asume su organización.

## Regla general

`proyectos/` (código del usuario) y el espacio del agente son **mundos separados**. El agente valida el gate (`proyectos/` existe) **antes de cualquier acción**; sin él, no continúa. Crear y organizar `proyectos/` corresponde **exclusivamente al usuario**.
