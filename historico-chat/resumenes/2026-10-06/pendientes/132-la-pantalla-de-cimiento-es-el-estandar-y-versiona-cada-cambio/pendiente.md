# Pendiente: el estándar vive en la base de Cimiento y cada cambio queda versionado

| | |
|---|---|
| **De dónde sale** | [H-1 · Lo que se guarda en la pantalla de Cimiento no tiene la historia de los archivos, y el estándar no se administra desde ella](../../sesion.md), en el resumen de la sesión del 2026-10-06 |

## El problema

El estándar vive en archivos de `base/` y la configuración de cada proyecto vive en la base de datos de Cimiento. La base guarda los cambios de tres maneras distintas: los niveles de las reglas no tienen versión, las suspensiones no dejan rastro al editarlas y los ajustes no dejan ningún rastro. No hay una sola historia ni una sola versión para lo que se administra.

## Por qué importa

Lo que no tiene historia no se puede revisar ni deshacer. Y mientras el estándar viva en dos sitios, uno de los dos se desactualiza.
