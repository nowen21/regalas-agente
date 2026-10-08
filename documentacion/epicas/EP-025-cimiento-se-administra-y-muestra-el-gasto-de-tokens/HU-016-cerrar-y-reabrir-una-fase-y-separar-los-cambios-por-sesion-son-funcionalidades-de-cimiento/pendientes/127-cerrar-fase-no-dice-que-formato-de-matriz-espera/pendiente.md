# Pendiente: `cerrar_fase` no dice qué formato de matriz espera

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: [H-9 del resumen del 2026-10-05](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-05/construir-ep-007.md); seguimiento en scilit: [pendiente 024](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-05/pendientes/024-esperando-a-cimiento-cerrar-fase-no-dice-que-formato-de-matriz-espera/pendiente.md) |

## El problema

`manage.py cerrar_fase` respondió «el plan de pruebas de A-EP-011-HU-001-indicadores no tiene casos en su matriz». El plan sí tenía casos, en una tabla «| Caso | CA | Qué se comprueba | Cómo |». `Fase.casos()` (`proyectos/cimiento/core/herramientas/fase.py`) solo reconoce filas «| HU-NNN | CA-NN | CP-NNN | tipo | prioridad | automatizado | ☐ |», y `Fase.plan()` solo reconoce los CA del plan de trabajo como «| CA-NN · nombre | ☐ |». El mensaje no nombra ninguno de los dos formatos.

## Por qué importa

Para saber qué corregir hubo que leer el código de la herramienta. El mensaje debería mostrar la fila que espera y, si encuentra una tabla de casos en otro formato, decir que no es la de la plantilla 08, sección 5.
