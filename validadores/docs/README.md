# Cómo funciona por dentro el código del estándar

Esta carpeta tenía una ficha por cada archivo de `validadores/`. El 2026-10-05 se retiraron (análisis 1 del pendiente 116, acuerdos 13 y 15): esos programas pasaron a [`proyectos/cimiento/core/`](../../proyectos/cimiento/core/) y dejaron de existir aquí.

Hoy cada pieza se explica en su propio código: cada módulo y cada clase de `core/` abre con lo que hace y por qué, y sus pruebas (`tests*.py`, en la misma carpeta) muestran cómo se usa.

| Carpeta | Qué hay |
|---|---|
| [`core/comun/`](../../proyectos/cimiento/core/comun/) | Lo que comparten todos: el proyecto y sus rutas, git, la lectura de archivos, los hallazgos, la consola y el catálogo de los enganches |
| [`core/validadores/`](../../proyectos/cimiento/core/validadores/) | Las comprobaciones, una clase por validador |
| [`core/enganches/`](../../proyectos/cimiento/core/enganches/) | La lógica de los enganches; lo que habla con la herramienta está en [`adaptadores/claude-code/`](../../adaptadores/claude-code/) |
| [`core/herramientas/`](../../proyectos/cimiento/core/herramientas/) | Las órdenes que se piden a mano: `validar`, `instalar`, `andamio`, `cerrar`, `retirar` y las demás |

Qué pieza sirve con cualquier agente y cuál hay que rehacer si cambia la herramienta está en [`anatomia/que-esta-amarrado-a-la-herramienta.md`](../../anatomia/que-esta-amarrado-a-la-herramienta.md).
