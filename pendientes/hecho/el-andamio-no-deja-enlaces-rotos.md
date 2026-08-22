# Pendiente · El andamio copia la plantilla del resultado con un enlace que se rompe a la profundidad de la fase

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-004 · HU-005 — Enlaces y citas](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md) — es un enlace relativo que nace roto, el mismo tema del 18, el 54 y el 55 |
| **De dónde sale** | El H-3 del resumen [../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

[validadores/andamio.py](../../validadores/andamio.py) copia [../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md](../../plantillas/ciclo-vida-proyectos/09-resultado-pruebas.md) tal cual a la carpeta de la fase. La plantilla enlaza `../../base/08-pruebas.md`, que resuelve desde `plantillas/planes/` y no desde `documentacion/epicas/EP/HU/fase/`, que está tres niveles más abajo. Las tres fases levantadas el 2026-08-20 nacieron con ese enlace roto y `validar.py estandar` lo reportó.

## Por qué importa

El andamio existe para que la fase nazca bien (su propio docstring: «la estructura se corrige en vez de nacer bien»). Un esqueleto que nace con un enlace roto obliga a corregirlo a mano en cada fase, que es lo que venía a evitar.

## Qué falta

Que el andamio reescriba los enlaces relativos de la plantilla al copiarla, calculando la ruta desde la carpeta de la fase, como ya hace el instalador con `«RUTA-ESTANDAR»` (pendiente 40). O que la plantilla use el marcador en vez de la ruta relativa, y el andamio lo rellene.

## El límite

Solo el enlace de la plantilla del resultado. Los otros cuatro documentos que copia no traen enlaces relativos a `base/`.

## Cómo se sabrá que cerró

Levantar una fase de prueba con el andamio y correr `validar.py estandar` sobre ella no reporta ningún enlace roto. Con caso automatizado.
