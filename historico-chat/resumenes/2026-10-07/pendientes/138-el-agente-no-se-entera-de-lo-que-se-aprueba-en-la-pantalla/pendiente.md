# Pendiente: el agente no se entera de lo que se aprueba en la pantalla

| | |
|---|---|
| **De dónde sale** | [H-15 · El usuario tuvo que avisar en el chat que ya había aprobado las propuestas](../../../2026-10-06/sesion.md), en el resumen de la sesión del 2026-10-06 |

## El problema

Cuando el usuario aprueba o rechaza en «Estándar» → «Propuestas» lo que propuso el agente, nada se lo cuenta al agente: el enganche de cada mensaje (`adaptadores/claude-code/hook_*.py`) no revisa las propuestas resueltas. El agente se queda esperando hasta que el usuario lo dice en el chat. Pasó el 2026-10-07 con las propuestas 1 a 6.

## Por qué importa

La pantalla es donde se autoriza todo (análisis 1 del pendiente 132, acuerdo 3). Si después hay que repetirlo en el chat, cada aprobación cuesta dos veces y el trabajo se detiene sin razón.
