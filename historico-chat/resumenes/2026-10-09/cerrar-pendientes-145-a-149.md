# 2026-10-09 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-09-cerrar-pendientes-145-a-149.md](../../2026-10-09-cerrar-pendientes-145-a-149.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | Los pendientes 145 a 149 del 2026-10-08 |

---

## Hallazgos de esta sesión

### H-1 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 08:41, el freno detuvo una orden de consola sobre `documentacion/epicas/EP-029-cimiento-sabe-que-parte-de-cada-proyecto-queda-sin-pruebas-y-lo-exige/HU-008-un-comando-dana-el-codigo-a-proposito-y-dice-que-danos-no-detectan-las-pruebas`: no hay una fase en curso y ninguna regla autoriza escribirlo (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: era crear la carpeta de la EP-029·HU-008 desde la consola antes de que existiera la fase; la HU se escribió con la herramienta de archivos, que el freno dejó porque el análisis aprobado del pendiente 148 la nombra |

### H-2 · `cerrar_fase` lee un solo caso de prueba por fila de la matriz

| Campo | Valor |
|---|---|
| Qué pasó | Al cerrar `A-EP-029-HU-008-danar-a-proposito`, `cerrar_fase` tomó solo CP-006 de los seis casos: la matriz del plan de pruebas pone varios casos en una fila («CP-001, CP-002») y `Fase.casos()` (`proyectos/cimiento/core/herramientas/fase.py:148`) solo reconoce una fila con un caso. Tampoco marcó esas filas ni los CA del plan de trabajo escritos como enlace. El resultado y las marcas se completaron a mano. La fase de la HU-011 de EP-026 tiene el mismo formato |
| Por qué importa | El resultado de las pruebas que escribe el cierre dice menos casos de los que hubo, y el veredicto por CA deja CA afuera, sin avisar |
| Pendiente | [Pendiente 150: `cerrar_fase` lee todos los casos de prueba y marca todo lo que cierra](pendientes/150-cerrar-fase-lee-todos-los-casos-y-marca-todo-lo-que-cierra/pendiente.md); se resuelve en esta sesión, por decisión del usuario |

### H-3 · El freno detuvo lo que escribió una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 11:14, el freno detuvo lo que escribió una orden de consola sobre `.agente/suspendidos.46f1a0bd5592a2f9.json`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [Pendiente 149](../2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/pendiente.md), en su [análisis 2](../2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-2.md) |

### H-4 · La pantalla de suspensiones pone todo en una sola página

| Campo | Valor |
|---|---|
| Qué pasó | El usuario pidió (turno 39) ordenar la pantalla de suspensiones en tres pestañas, «Suspensiones», «Reglas» y «Enganches», con el formulario en un modal que abre un botón al principio de la tabla |
| Por qué importa | La tabla de enganches quedaba al final de la página, debajo del formulario, y las reglas no se veían: había que saber su código |
| Pendiente | [Pendiente 149](../2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/pendiente.md), en su [análisis 3](../2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-3.md) |

### H-5 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 13:04, el freno detuvo una orden de consola sobre `el`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | [Pendiente 144: el freno sigue tomando texto de los comandos como rutas u órdenes](../2026-10-08/pendientes/144-el-freno-sigue-tomando-texto-de-los-comandos-como-rutas-u-ordenes/pendiente.md): la orden era un `sed` y el freno tomó la palabra «el» de su texto como una ruta |

### H-6 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 13:28, el freno detuvo una orden de consola sobre `/tmp/x`: queda fuera del proyecto (04·S9). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Pendiente | No hace falta: el agente quiso guardar en `/tmp` la salida de la prueba en scilit; la repitió guardándola en una variable, sin archivos |

### H-7 · La revisión de git suspendida dice la hora de vencimiento en UTC

| Campo | Valor |
|---|---|
| Qué pasó | En la prueba en scilit (2026-10-09), `validar.py marcas` suspendida dijo «hasta el 2026-10-09 19:29»; en Colombia eran las 14:29. `suspendidos.py` lee el vencimiento con `UNIX_TIMESTAMP`, que toma la hora UTC guardada como si fuera de Colombia y le suma cinco horas |
| Por qué importa | Quien lee el aviso cree que la suspensión dura cinco horas más de lo que dura; la prueba en el proyecto quedó en «falla» y scilit no recibe el aviso de resuelto |
| Pendiente | [Pendiente 149](../2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/pendiente.md), en su [análisis 4](../2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-4.md) |

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
