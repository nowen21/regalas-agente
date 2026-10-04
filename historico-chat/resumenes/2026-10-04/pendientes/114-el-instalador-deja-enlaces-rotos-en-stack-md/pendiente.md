# Pendiente: el instalador deja enlaces rotos en .agente/stack.md

Se resuelve en el [análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](../../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/pendientes/110-el-andamio-no-sirve-desde-un-proyecto/analisis-1.md), que reúne los cinco reportes de scilit.

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: los hallazgos del [resumen de la sesión del 2026-10-03](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-03/sesion.md); seguimiento en scilit: [pendiente 9](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/9-esperando-a-cimiento-el-instalador-deja-enlaces-rotos-en-stack-md/pendiente.md) |

## El problema

El `.agente/stack.md` que deja `validadores/instalar.py` en el proyecto trae enlaces relativos a `../base/...` (líneas 7 a 10 y 86), que solo funcionan dentro de Cimiento. El control de enlaces los reporta como rotos después de cada edición en scilit.

## Por qué importa

El aviso de enlaces rotos sale en cada edición del proyecto y esconde los enlaces rotos de verdad.
