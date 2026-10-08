# Pendiente: la fila de la HU nueva cae en la bitácora de la épica

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: [H-7 del resumen del 2026-10-05](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-05/construir-ep-007.md); seguimiento en scilit: [pendiente 022](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-05/pendientes/022-esperando-a-cimiento-la-fila-de-la-hu-nueva-cae-en-la-bitacora/pendiente.md) |

## El problema

`andamio.py hu` agrega la fila de la HU nueva con `agregar_fila(epica_md, fila, "## 9.", escribir)` (`proyectos/cimiento/core/herramientas/andamio.py`, `crear_hu`). `agregar_fila` toma la primera tabla que aparece después de «## 9.», en cualquier parte del archivo. Si la sección 9 todavía no tiene tabla (la épica recién creada dice «Pendiente: se define en el análisis de esta épica.»), esa primera tabla es la de la bitácora, sección 20, y la fila queda ahí.

En scilit pasó con las 8 HU de EP-010 a EP-013, el 2026-10-05: la fila «| [HU-001](...) | «Título» |» quedó al final de la bitácora de las cuatro épicas, y hubo que moverla a mano.

## Por qué importa

La sección 9 queda sin listar la HU y la bitácora con una fila que no es un cambio: quien lee la épica no encuentra sus historias (`13·DOC16`).
