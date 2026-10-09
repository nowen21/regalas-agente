# 2026-10-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-08-sesion.md](../../2026-10-08-sesion.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · Los documentos de Cimiento pasan a la base y dejan de ser archivos .md

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08, al analizar si los .md gastan más que la base, el usuario señaló que cada operación termina en un guion nuevo (hay 250 en `historico-chat/scripts/`) aunque la estructura podría estar en la base. La base no tiene tablas para épicas, HU, análisis, pendientes ni planes. El usuario decidió que todos los .md de Cimiento pasan a la base y ninguno queda como archivo; los .py siguen siendo archivos porque son el programa de Cimiento |
| Por qué importa | Sin tabla ni comando fijo, cada operación se resuelve con un guion de un solo uso; con el .md y la base a la vez, una de las dos copias se queda vieja |
| Pendiente | [Pendiente 142: los documentos de Cimiento viven en su base, con un comando fijo por cada tipo](pendientes/142-los-documentos-de-cimiento-viven-en-la-base/pendiente.md) |

### H-2 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 21:01, el freno detuvo una orden de consola sobre `/tmp/idx.md`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el archivo temporal no era necesario; el commit se hizo sin `historico-chat/README.md`, cuya línea entra en el commit siguiente |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
