# Pendiente: el andamio no sirve desde un proyecto

| | |
|---|---|
| **De dónde sale** | Proyecto scilit: los hallazgos del [resumen de la sesión del 2026-10-03](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-03/sesion.md); seguimiento en scilit: [pendiente 5](C:/DesarrollosClaude/personales/scilit/historico-chat/resumenes/2026-10-04/pendientes/5-esperando-a-cimiento-el-andamio-no-sirve-desde-un-proyecto/pendiente.md) |

## El problema

`validadores/andamio.py` falla cuando se corre con `--raiz` de un proyecto que no es Cimiento:

1. Busca las plantillas de HU y de fase en `<proyecto>/plantillas/ciclo-vida-proyectos/`, que no existe: `falta la plantilla plantillas\ciclo-vida-proyectos\04-HU.md`. Se reproduce con `python validadores/andamio.py hu EP-001-x algo --raiz <proyecto>`.
2. Al copiar la plantilla, arma los enlaces a `base/` y `plantillas/` como rutas relativas dentro de Cimiento (`../../../../base/...`); en el proyecto quedan rotos.
3. `pendiente` solo crea el pendiente debajo de una HU o en el resumen del día; no hay forma de crearlo en la carpeta `pendientes/` de una épica, que es donde scilit los necesitó (EP-001 y EP-002).

scilit lo rodeó con guiones que cambian las rutas de las plantillas y corrigen los enlaces después (`historico-chat/scripts/2026-10-03/crear_hu_ep001.py`).

## Por qué importa

Cada proyecto que use el andamio tiene que escribir su propio arreglo, y los enlaces rotos aparecen en cada HU y fase nuevas.
