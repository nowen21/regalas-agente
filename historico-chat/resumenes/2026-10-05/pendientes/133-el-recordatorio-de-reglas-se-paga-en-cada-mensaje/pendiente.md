# Pendiente: las reglas llegan cuando se actúa, una sola vez, y las de código por temas

| | |
|---|---|
| **De dónde sale** | [Hallazgo V2 de H-1 · Las reglas llegan repetidas en cada mensaje y no llegan cuando se actúa](../../reglas-de-cada-turno-sin-tokens.md), según el [análisis 1](analisis-1.md), en el resumen de la sesión del 2026-10-05, y [hallazgo V2 de H-6 · Partir `cambiar-codigo` se hace por temas](../../../2026-10-09/sesion-2.md), según el [análisis 2](analisis-2.md), en el resumen de la sesión 2 del 2026-10-09 |

## El problema

Las reglas se eligen solo por la palabra clave del mensaje. Lo que de verdad dice qué reglas rigen es la acción, y antes de ella no llega nada: [base/tareas.md](../../../../../base/tareas.md) lo describe, pero ningún enganche lo hace. Por eso `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar`, que no tienen palabra clave, no entregan sus reglas en ningún momento. Mientras tanto, con cada mensaje llegan las mismas listas, y seis reglas llegan dos veces. Y las reglas de código llegan todas, sin importar qué archivo se escribe.

## Por qué importa

El agente trabaja sin las reglas de lo que está haciendo, recibe reglas que no aplican a lo que hace, y cada mensaje de todos los proyectos paga reglas que no usa.
