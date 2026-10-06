# Pendiente: el tapado de claves no reconoce las de Anthropic ni las variables con prefijo

| | |
|---|---|
| **De dónde sale** | [H-3 · El tapado de claves no reconoce las de Anthropic ni las variables con prefijo](../../../../../../historico-chat/resumenes/2026-10-05/sesion-2.md), en el resumen de la sesión del 2026-10-05, versión 2 según el [análisis 1](analisis-1.md). La versión 1 decía «El enmascarador no reconoce las claves de Anthropic» |

## El problema

`SEGUROS`, en [secretos.py](../../../../../../proyectos/cimiento/core/validadores/secretos.py), no trae la forma `sk-ant-`, y `ASIGNA` y `_ASIGNA_SIN_COMILLAS`, en [enmascarar.py](../../../../../../proyectos/cimiento/core/enganches/enmascarar.py), exigen un límite de palabra antes de `api_key`, así que `ANTHROPIC_API_KEY=...` no entra. Lo ya guardado en la base no se vuelve a revisar cuando el tapado aprende algo.

## Por qué importa

Una clave sin tapar queda en la base, en el histórico o en un commit, contra `00·N6`.
