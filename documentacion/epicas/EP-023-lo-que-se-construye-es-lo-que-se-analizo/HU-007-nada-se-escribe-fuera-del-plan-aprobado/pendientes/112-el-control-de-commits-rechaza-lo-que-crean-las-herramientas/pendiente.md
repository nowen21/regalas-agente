# Pendiente: el control de commits rechaza lo que crean las herramientas del estándar

Se resuelve en el [análisis 1 del pendiente 110: lo que un proyecto reporta es un defecto de Cimiento en todos los proyectos](../../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/pendientes/110-el-andamio-no-sirve-desde-un-proyecto/analisis-1.md), que reúne los cinco reportes de scilit.

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: los hallazgos del [resumen de la sesión del 2026-10-03](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-03/sesion.md); seguimiento en scilit: [pendiente 7](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/7-esperando-a-cimiento-el-control-de-commits-rechaza-lo-que-crean-las-herramientas/pendiente.md) |

## El problema

El control que compara el commit con el plan (`validadores/plan_vs_hecho.py`) rechaza archivos que crean las propias herramientas del estándar y que ningún plan nombra:

- los `README.md` que el andamio crea con cada HU;
- `documentacion/versiones/AAAA-MM-DD-X.Y.Z.md` y su `README.md`, que escribe el instalador al adoptar una versión.

También rechaza la especificación del módulo que la lista de terminado del plan exige actualizar, si el plan no la nombra archivo por archivo. En scilit eso obligó a pedir aprobación tres veces por cosas que el plan aprobado ya cubría (commits `12e5a7a` y `d6a8ab0`).

## Por qué importa

Cada commit de cierre se traba, y el usuario tiene que volver a aprobar lo que ya aprobó.
