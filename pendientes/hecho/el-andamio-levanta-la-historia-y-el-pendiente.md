# Pendiente · El andamio levanta solo la fase; la historia, el pendiente y sus índices se escriben a mano

**Estado:** abierto · anotado 2026-08-20.

| | |
|---|---|
| **Historia de usuario** | [EP-007 · HU-003 — Crear la estructura de carpetas del trabajo](../../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-003-estructura-de-carpetas/HU-003-estructura-de-carpetas.md) — el andamio es la estructura del trabajo puesta por un programa, y hoy solo cubre el último eslabón |
| **De dónde sale** | La pregunta del usuario del 2026-08-20: cómo hacer que Cimiento haga más y gaste menos. Quedó en el [resumen](../../historico-chat/resumenes/2026-08-20/core-del-agente-en-la-herramienta.md) |
| **Proyecto de origen** | El estándar mismo |

## El problema

[validadores/andamio.py](../../validadores/andamio.py) crea la carpeta de la fase con sus cinco documentos. Todo lo que está arriba de la fase en la cadena se escribe a mano: el archivo del pendiente con su ficha, la carpeta de la historia con su documento y su `README.md`, la fila en el §9 de la épica, la fila en el `README.md` de la épica, la fila en el índice del backlog y la del mapa «en qué historia está cada uno».

El 2026-08-20 se bajaron tres defectos por la cadena: fueron unas quince escrituras de índice a mano, dos de ellas corregidas después por los validadores, y el andamio dejó su propio enlace roto (pendiente 67). Lo que más fichas costó de la sesión no fue el código: fue eso.

## Por qué importa

La cadena es lo que el estándar exige (`02·F0`, `02·F23`) y es lo que más cuesta cumplir. Cada eslabón que se escribe a mano es un sitio donde el agente se equivoca, el validador lo atrapa después, y se vuelve a escribir. Lo mecánico de la cadena, que es la mitad, lo puede hacer un programa sin opinar: el contenido sigue siendo del agente.

## Qué falta

Que el andamio acepte `pendiente`, `hu` y `fase` como unidades: cree el archivo desde su plantilla con los marcadores, y ponga **las filas de los índices en los dos sentidos** (épica → HU, README de la épica, backlog, mapa de historias). Sin escribir contenido, como hoy.

## El límite

No redacta el pendiente ni la historia: solo deja el esqueleto y los enlaces puestos. El criterio sigue siendo de quien escribe.

## Cómo se sabrá que cerró

Levantar un pendiente, su historia y su fase con tres comandos deja `validar.py estandar`, `fases` y `pendientes` sin avisos antes de escribir una sola línea de contenido.
