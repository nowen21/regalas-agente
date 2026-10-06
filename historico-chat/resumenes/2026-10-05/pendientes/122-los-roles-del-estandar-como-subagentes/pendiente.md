# Pendiente: los roles del estándar como subagentes de Claude Code

| | |
|---|---|
| **De dónde sale** | [El hallazgo 1: los roles de `00·ID6` como subagentes de Claude Code](../../roles-como-subagentes.md), en el resumen de la sesión del 2026-10-05. Lo trajo la sesión agente-e6, que trabaja el [análisis 1 del pendiente 116](../../../2026-10-04/pendientes/116-el-codigo-de-cimiento-se-repite-en-vez-de-reusarse/analisis-1.md), por orden del usuario. |

## El problema

El usuario preguntó si Cimiento puede tener sus propios subagentes para tareas específicas, como hace Claude Code al repartir una tarea grande entre varios agentes.

`00·ID6` define ocho roles: Explorador, Escritor de especificación, Diseñador, Planificador de tareas, Implementador, Verificador, Crítico y Orquestador. Están escritos como habilidades en `skills/` (11 carpetas, de `analizar-proyecto` a `usar-memoria`). Ninguno existe como subagente: no hay `.claude/agents/`, que es donde Claude Code define un subagente con su encargo, sus herramientas permitidas y su modelo.

Hoy el agente principal hace todos los roles en el mismo hilo. Lee todo lo que necesita cada etapa, y nada le impide al Crítico editar lo que revisa.

## Por qué importa

Con subagentes se gana:

- trabajo en paralelo en las tareas grandes;
- un encargo cerrado por rol, por ejemplo un Crítico que no puede escribir;
- menos lectura en el agente principal, que recibe solo el informe.

Y hay que resolver:

- **Las reglas.** Lo que se inyecta en cada mensaje no le llega al subagente. El freno y los enganches de las herramientas sí corren sobre lo que hace.
- **El histórico.** Lo que hace el subagente por dentro no queda en `historico-chat/`; solo su informe final.
- **El consumo.** Cada subagente gasta tokens por su cuenta, y eso tiene que verse en el conteo del pendiente 119.
- **Los choques.** Dos subagentes no pueden escribir el mismo archivo al tiempo.
- **El alcance.** Tiene que servir a todo proyecto que hereda Cimiento y llegar solo con `instalar.py`. Como es propio de Claude Code, su lugar es `adaptadores/claude-code/` (`adaptadores/contrato.md`), y el texto del rol sigue en un solo sitio: `skills/`.
