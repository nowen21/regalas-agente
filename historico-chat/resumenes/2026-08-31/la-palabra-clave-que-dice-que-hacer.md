# 2026-08-31 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-31-la-palabra-clave-que-dice-que-hacer.md](../../2026-08-31-la-palabra-clave-que-dice-que-hacer.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | nada, es trabajo nuevo |

---

## Hallazgos de esta sesión

### H-1 · La lista de palabras de `01·C28` creció, y salió la fila que no servía

| Campo | Valor |
|---|---|
| Qué pasó | Al preguntar por la regla que exige la palabra clave se vio que el anexo tenía la fila «¿La pregunta que se haga?», que el programa leía como una palabra literal y por eso no coincidía con ningún mensaje. En su lugar entraron dos palabras de verdad, `Liste` y `OK`, y el sello del checklist de la regla dejó de decir cuántas palabras tiene el anexo. |
| Por qué importa | `OK` era lo que faltaba para acusar recibo sin autorizar nada: antes, un «ok» suelto hacía que el agente pidiera la palabra. Y el sello que contaba palabras quedaba desactualizado cada vez que entraba una. |
| Dónde queda | [base/01-conducta/palabras-clave.md](../../../base/01-conducta/palabras-clave.md), el sello de [`01·C28`](../../../base/01-conducta.md#c28--sin-la-palabra-que-diga-qué-se-espera-el-agente-no-actúa), y la entrada `56.2.0` de [CHANGELOG.md](../../../CHANGELOG.md) con [VERSION](../../../VERSION) |

**Lo que se descartó.** Que la pregunta escrita entre `¿` y `?` cuente como la palabra «Pregunta». Se revisó qué costaría, porque la tabla solo sabe de palabras y la detección vive en `recuperar.py`, y el usuario lo descartó en la misma sesión. No deja pendiente.

**Lo que no es hallazgo.** Se levantó LocalHub en el puerto 8002, con `manage.py start --port 8002`. Es una operación, y cómo se repite está en el README de ese proyecto.

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda a medias. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- Resuelto acá, con lo que se hizo escrito en el campo de dónde queda.
- Anotado, con su pendiente creado y su historia de usuario disparada escrita. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ H-1, en el anexo y en la entrada `56.2.0` |
| Todo hallazgo abierto tiene su pendiente creado | ☑ Ninguno quedó abierto |
| Toda historia disparada está escrita en su épica | ☐ Falta decidir si `Liste` y `OK` llevan su eslabón de cadena o entran como ajuste de la lista |
| Lo que se hizo está aprobado y guardado | ☐ Seis archivos de este tema sin commit, y el resto del árbol es de trabajo anterior |

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
