# 2026-10-08 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-08-guiones-que-pasan-a-cimiento.md](../../2026-10-08-guiones-que-pasan-a-cimiento.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | La pregunta del usuario: qué guiones de `historico-chat/scripts/` se pueden convertir en comandos de Cimiento para no volver a escribirlos |

---

## Hallazgos de esta sesión

### H-1 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 22:19, el freno detuvo lo que escribió una orden de consola sobre `proyectos/cimiento/core/herramientas/tests_instalacion.py`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [Pendiente 144: el freno sigue tomando texto de los comandos como rutas u órdenes](pendientes/144-el-freno-sigue-tomando-texto-de-los-comandos-como-rutas-u-ordenes/pendiente.md) |

### H-2 · Completar el cierre de una fase se hace con un guion suelto

| Campo | Valor |
|---|---|
| Qué pasó | `manage.py cerrar_fase` deja `«…»` en lo que un programa no sabe. El 2026-10-06 esos huecos se llenaron con `historico-chat/scripts/2026-10-06/llenar_marcas.py` y 25 archivos `.txt`, uno por documento |
| Por qué importa | Cada cierre vuelve a armar los mismos archivos a mano, y el guion que ya funciona no está en Cimiento |
| Pendiente | [Pendiente 147: cerrar una fase llena sus huecos sin guiones sueltos](pendientes/147-cerrar-fase-llena-sus-huecos-sin-guiones-sueltos/pendiente.md) |

### H-3 · Cada sabotaje de pruebas se vuelve a programar desde cero

| Campo | Valor |
|---|---|
| Qué pasó | Hay unos 20 guiones `sabotaje_*` en `historico-chat/scripts/` que hacen lo mismo: copiar el archivo, dañarlo, correr las pruebas, devolverlo desde la copia y borrar lo que el daño dejó escrito. Cada uno copia en su encabezado las lecciones de los anteriores |
| Por qué importa | Una lección que vive en el encabezado de un guion se pierde en el siguiente; si queda en el código de un comando, se cumple siempre |
| Pendiente | [Pendiente 148: probar que las pruebas sirven con un solo comando](pendientes/148-probar-que-las-pruebas-sirven-con-un-solo-comando/pendiente.md) |

### H-4 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 23:03, el freno detuvo una orden de consola sobre `$M`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el archivo era el mensaje del commit, escrito fuera del proyecto; el commit se hizo con el mensaje dentro de la orden |

### H-5 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-08 23:06, el freno detuvo lo que escribió una orden de consola sobre `proyectos/cimiento/core/herramientas/desinstalar.py`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [Pendiente 144: el freno sigue tomando texto de los comandos como rutas u órdenes](pendientes/144-el-freno-sigue-tomando-texto-de-los-comandos-como-rutas-u-ordenes/pendiente.md) |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☑ |
| Todo pendiente enlazado existe | ☑ |
| Lo que se hizo está aprobado y guardado | ☑ commit `f7a13f8` |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
