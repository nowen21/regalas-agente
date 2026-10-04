# Pendiente: el control de redacción ve guiones suaves en cada í

Se resuelve en el [análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](../../../../EP-023-lo-que-se-construye-es-lo-que-se-analizo/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/pendientes/110-el-andamio-no-sirve-desde-un-proyecto/analisis-1.md), que reúne los cinco reportes de scilit.

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: los hallazgos del [resumen de la sesión del 2026-10-03](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-03/sesion.md); seguimiento en scilit: [pendiente 6](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/6-esperando-a-cimiento-el-control-de-redaccion-ve-guiones-suaves-en-cada-i-tildada/pendiente.md) |

## El problema

`adaptadores/claude-code/hook_md.py` marca «guion suave (U+00AD)» en casi todas las líneas que tienen «í». Los archivos no tienen ese carácter: se comprobó contando `\u00ad` con Python, y dio cero. La «í» en UTF-8 es `C3 AD`; el segundo byte coincide con U+00AD, así que parece que el texto se lee con la codificación equivocada. Pasó en todas las especificaciones y planes de scilit del 2026-10-03 y 2026-10-04.

## Por qué importa

Las marcas falsas tapan las verdaderas, y el agente gasta turnos revisando lo que no está.
