# Pendiente: los documentos de Cimiento viven en su base, con un comando fijo por cada tipo, y dejan de ser archivos .md

| | |
|---|---|
| **De dónde sale** | [H-1 · Los documentos de Cimiento pasan a la base y dejan de ser archivos .md](../../sesion.md), en el resumen de la sesión del 2026-10-08 |

## El problema

La base de Cimiento tiene tablas para las reglas, los recuerdos, el consumo, los proyectos y las pruebas (`proyectos/cimiento/core/*/models.py`), pero no para las épicas, las HU, los análisis, los pendientes ni los planes: esos viven solo como archivos .md. El repositorio tiene 2.921 .md, unos 24 MB, y 13,6 MB están en `documentacion/`.

Como no hay un comando fijo para cada operación, Claude escribe un guion nuevo cada vez: hay 250 `.py` de un solo uso en `historico-chat/scripts/`.

El usuario decidió que todos los .md de Cimiento pasan a la base y ninguno queda como archivo. Los `.py` siguen siendo archivos porque son el programa de Cimiento. `CLAUDE.md` también sale: lo que dice puede llegar por los enganches, que ya le pasan a Claude las reglas y la memoria desde la base.

## Por qué importa

Sin tabla ni comando fijo, cada operación se resuelve con un guion de un solo uso, y ese código se repite y hay que mantenerlo. Con el .md y la base a la vez, una de las dos copias se queda vieja, como pasó con `.agente/configuracion.md`.
