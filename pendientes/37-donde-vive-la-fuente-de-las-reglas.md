# Pendiente · Dónde vive la fuente de las reglas

**Estado:** abierto · anotado 2026-08-16.

| | |
|---|---|
| **De dónde sale** | El hallazgo H-1 del [resumen del 2026-08-16](../historico-chat/resumenes/2026-08-16/sesion.md) |
| **Proyecto de origen** | El estándar mismo. Nace de una pregunta del usuario, no de un defecto de un proyecto |

## El problema

El usuario preguntó qué pasaría si todas las reglas se guardaran en una base de datos. La discusión dejó claro qué se gana y qué se pierde, pero no se decidió nada, y sin dejarlo escrito la discusión vuelve a empezar de cero la próxima vez.

Lo que quedó en claro:

- **No cambia nada para los proyectos.** El estándar ya vive en una carpeta central y ningún proyecto lo copia; la base sería de Cimiento y los proyectos le seguirían preguntando a Cimiento.
- **Lo que se pierde es la revisión.** Hoy cambiar una regla deja un archivo modificado que se lee, se compara con la versión anterior y se aprueba en un commit. Una fila que cambia no deja nada que leer ni que aprobar.
- **Lo que se gana es consultar.** Qué reglas dependen de cuál, cuáles son validables, cuáles se derogaron, dónde se cita un ID: hoy eso se resuelve leyendo o con los validadores.
- **Claude lee texto.** Cimiento tendría que sacar la regla de la base y escribirla como texto para meterla en la sesión. La base no ahorra ese paso, lo agrega.

## Qué falta decidir

Una sola cosa: **qué es la fuente.**

| Si la fuente es… | Qué pasa |
|---|---|
| La base de datos | Se pierde ver qué cambió en una regla y aprobarlo antes de que rija. Habría que construir a mano el historial que git da gratis |
| El texto, con la base **generada** a partir de él | Se gana consultar sin perder nada. La base se puede borrar y volver a generar; ninguna regla vive ahí |

La segunda es la que el agente recomendó. Falta la decisión del usuario.

## Cómo se sabe que cerró

Está escrito qué es la fuente. Si se decide generar la base, existe además la historia de usuario que la construye y dice qué preguntas responde.
