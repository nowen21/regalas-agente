# 2026-08-22 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-22-sesion-3.md](../../2026-08-22-sesion-3.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**Viene de:** el H-1 de [sesion-2](sesion-2.md), que reescribió el encuadre de [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md) con el texto del molde.

---

## Hallazgos de esta sesión

### H-1 · El encuadre del molde de planteamiento copia la cadena de `02·F0` y la copia ya no coincide

- **Qué pasó:** el usuario leyó el encuadre de [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md) y no entendió qué comunicaba. Al revisarlo: de sus tres afirmaciones, dos estaban ya en el estándar —la cadena es [`02·F0`](../../../base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) y «no hay código sin plan aprobado» es [`02·F2`](../../../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md) + [`02·F4`](../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)—, con seis enlaces para decirlas.
- **Por qué importa:** la copia se desactualizó. `F0` dice `planteamiento → épica → HU → especificación → plan → código`; el encuadre decía `análisis → alcance → épica/HU → especificación → plan aprobado → implementación`. Dos versiones de la misma cadena en el mismo repo, y la que se lee primero es la equivocada. Además incumplía [`00·ID9`](../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) repitiendo reglas que el agente ya cargó al abrir la sesión.
- **Qué se decidió:** el encuadre dice lo único que no está en otra parte —qué papel juega el documento— y **enlaza** la cadena en vez de copiarla. Se le agregó además que lo que se responda sobre el documento va bajo `00·ID9`.
- **Dónde queda:** encuadre reescrito en [`prompts/cimiento-planteamiento.md`](../../../prompts/cimiento-planteamiento.md), primer párrafo.
- **Estado:** resuelto acá
- **Responde a:** — (salió de que el usuario no entendió el texto)
- **Dispara:** — (se revisó [`plantillas/ciclo-vida-proyectos/01-planteamiento.md`](../../../plantillas/ciclo-vida-proyectos/01-planteamiento.md): el molde **enlaza** `02·F0`, no copia la cadena. La copia se inventó al llenar el archivo; la plantilla está bien.)

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☐ |
| Todo hallazgo abierto tiene su pendiente creado | ☐ |
| Toda historia disparada está escrita en su épica | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_
