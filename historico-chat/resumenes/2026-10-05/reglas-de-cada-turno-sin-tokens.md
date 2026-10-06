# 2026-10-05 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-05-reglas-de-cada-turno-sin-tokens.md](../../2026-10-05-reglas-de-cada-turno-sin-tokens.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### H-1 · El recordatorio de reglas se paga en cada mensaje

| Campo | Valor |
|---|---|
| Qué pasó | El usuario preguntó cómo dejar de gastar tokens en el bloque «LAS REGLAS DE CADA TURNO». Se encontró que repite seis reglas del bloque recuperado, que en un turno agregó unos 2.567 tokens contra un límite de 2.000 y que ningún enganche aprovecha el aviso de Claude Code después de resumir la conversación. Se habló también de revisar con un modelo de lenguaje local y de ensayarlo antes contra las correcciones del usuario |
| Por qué importa | Se paga en todos los mensajes de todos los proyectos, y la mayor parte se repite |
| Qué se decidió | El usuario dejó la propuesta para análisis |
| Pendiente | [Pendiente 133: el recordatorio de reglas se paga en cada mensaje](pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md) |

### H-2 · El enganche de redacción dice que no puede detener

| Campo | Valor |
|---|---|
| Qué pasó | La descripción de `hook_redaccion.py` dice que no detiene porque al cerrar el turno «no hay nada que bloquear». El motivo real es que el usuario decidió medir sin detener (EP-005·HU-012, RN-05). La primera versión de este hallazgo propuso bloquear sin haber buscado esa decisión, y se corrigió en la misma sesión |
| Por qué importa | Quien lea el comentario cree que detener es imposible y no sabe que es una decisión del usuario |
| Qué se decidió | Corregir solo el comentario; el comportamiento no cambia |
| Pendiente | [Pendiente 134: el enganche de redacción dice que no puede detener](pendientes/134-el-enganche-de-redaccion-dice-que-no-puede-detener/pendiente.md) |

### H-3 · La palabra clave no se reconoce en plural

| Campo | Valor |
|---|---|
| Qué pasó | El mensaje «preguntas las pruebas...» se tomó como mensaje sin palabra de `01·C28`, porque la comparación es exacta |
| Por qué importa | El agente queda entre no responder un pedido claro o saltarse la regla |
| Pendiente | [Pendiente 135: la palabra clave no se reconoce en plural](pendientes/135-la-palabra-clave-no-se-reconoce-en-plural/pendiente.md) |

### H-4 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-06 12:14, el freno detuvo una orden de consola sobre `$TMP/p.patch`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Qué se decidió | Fue un error del agente: la orden traía una línea que escribía en `$TMP` y sobraba. El usuario entendió cómo funciona el freno y decidió no tocarlo por ahora |
| Pendiente | No deja pendiente |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
