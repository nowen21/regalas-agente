# 2026-10-09 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-10-09-sesion-2.md](../../2026-10-09-sesion-2.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

| Campo | Valor |
|---|---|
| Viene de | «...» |

---

## Hallazgos de esta sesión

### 1 · Las reglas de cada acción no se cargan, aunque `base/tareas.md` dice que sí

- **Qué pasó.** `base/tareas.md` dice que las reglas se eligen de dos maneras: por la palabra clave del mensaje y, antes de cada acción, por la acción («Acciones que la señalan»). La segunda no la hace ningún enganche: `MapaDeTareas.acciones()` solo lo usa el guion `historico-chat/scripts/2026-10-04/paridad_reglas.py`, y `hook_antes.py` frena, pero no entrega reglas.
- **Por qué importa.** `cambiar-codigo`, `tocar-datos`, `ir-afuera` y `cambiar-estandar` no tienen palabra clave. Hoy sus reglas no le llegan al agente en ningún momento, ni siquiera cuando cambia código o el estándar.
- **Dónde queda.** En el [análisis 1 del pendiente 133: el recordatorio de reglas se paga en cada mensaje](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), que lo vuelve su hallazgo V2.

### H-7 · Llenar un análisis lo hace Cimiento, sin guiones sueltos

V2, según el [análisis 3 del pendiente 133](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md).

- **Qué pasó.** Para llenar los análisis del pendiente 133 se escribieron guiones sueltos, y ya hay 49 en `historico-chat/scripts/`. Se decidió que Cimiento llene solo la parte que siempre es igual y que la parte que cambia se guarde con un comando fijo.
- **Por qué importa.** Según `04·S18`, lo que se repite va como funcionalidad de Cimiento; cada guion nuevo gasta trabajo y puede traer un error distinto.
- **Dónde queda.** [Pendiente 133: las reglas llegan cuando se actúa, por temas, y los análisis se llenan sin guiones](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md).

### H-1 · El freno le carga a una sesión lo que hizo otra

V2, según el [análisis 4 del pendiente 133](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md).

| Campo | Valor |
|---|---|
| Qué pasó | Otra sesión cambió `.gitignore` mientras esta corría una orden que solo leía, y el freno la detuvo. La foto de antes y después no distingue quién cambió cada archivo |
| Por qué importa | Con dos sesiones abiertas, el freno detiene trabajo permitido y anota hallazgos que no son de la sesión |
| Pendiente | [Pendiente 133](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md) |

### H-2 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 11:31, el freno detuvo una orden de consola sobre `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Lo que se encontró | La orden era un `mkdir` de la carpeta de la HU. `13·DOC15` autoriza el archivo `documentacion/epicas/*/HU-*/HU-*.md`, no la carpeta vacía: escribir el archivo la crea. El agente usó el camino equivocado; no es un defecto del freno ni del plan |
| Pendiente | No hace falta |

### H-3 · El freno detuvo una escritura fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 11:50, el freno detuvo una escritura sobre `historico-chat/scripts/2026-10-09/llenar_cierre_ep005_hu025_a.py`: es un guion para cerrar o reabrir una fase, que Cimiento ya hace: se usa `manage.py cerrar_fase «fase» (o reabrir_fase)`, como acordó el análisis 2 del pendiente 119 (04·S18). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Lo que se encontró | El guion iba a llenar los 28 huecos que `cerrar_fase --aplicar` dejó en la fase A de la EP-005·HU-025. `cerrar_fase` sí se usó, pero deja esos huecos para llenarlos aparte: es el problema del pendiente 147, que trabaja otra sesión. Los huecos se llenaron editando los documentos de la fase, que el plan permite |
| Pendiente | El 147 (`cerrar_fase` deja huecos que hay que llenar a mano). No hace falta otro |

### H-4 · El freno detuvo una orden de consola fuera del plan

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-09 11:56, el freno detuvo una orden de consola sobre `$R`: el plan de la fase en curso no lo declara, o no está aprobado, y ninguna regla lo autoriza (02·F8). |
| Por qué importa | Lo que no está en el plan aprobado ni lo autoriza una regla es un hallazgo: la ejecución se detiene y vuelve al análisis (análisis 1 del pendiente 103, acuerdos 18 y 44). |
| Lo que se encontró | La orden escribía el README de la HU-025 con la ruta guardada en una variable de la consola (`$R`). El freno lee la ruta tal como está escrita y no resuelve variables, así que vio `$R`. La ruta real sí estaba autorizada (`documentacion/epicas/**/README.md`). Fue un error de forma del agente: se repitió con la ruta escrita |
| Pendiente | No hace falta |

### H-5 · El freno corta las órdenes por los separadores que están dentro de comillas

V2, según el [análisis 4 del pendiente 133](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-4.md).

| Campo | Valor |
|---|---|
| Qué pasó | Un `sed` cambiaba una fila de tabla, con barras verticales dentro de las comillas. El freno partió la orden por esas barras y tomó los pedazos como archivos |
| Por qué importa | Detiene cambios permitidos cada vez que una orden lleva una barra vertical o un punto y coma dentro de un texto |
| Pendiente | [Pendiente 133](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md) |

### H-6 · Partir `cambiar-codigo` se hace por temas

V2, según el [análisis 2 del pendiente 133](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md).

| Campo | Valor |
|---|---|
| Qué pasó | El análisis 1 dijo partir `cambiar-codigo` en pruebas, código y configuración, sin decir cómo repartir sus 128 reglas. Se decidió repartirlas por temas: cada capítulo es un tema y cada tipo de archivo recibe los suyos |
| Por qué importa | Cada acción sobre código trae solo lo que le aplica, con una sola propuesta del estándar |
| Pendiente | [Pendiente 133: las reglas llegan cuando se actúa, una sola vez, y las de código por temas](../2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/pendiente.md) |

---

## ¿Se puede cerrar la sesión?

Se cierra cuando ningún hallazgo queda sin anotar: cada uno enlaza su pendiente, y su pendiente existe. Anotar es dejar el archivo, no decir «quedó pendiente».

| Para cerrar | Estado |
|---|---|
| Todo hallazgo enlaza su pendiente | ☐ |
| Todo pendiente enlazado existe | ☐ |
| Lo que se hizo está aprobado y guardado | ☐ |

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

_(Si la sesión no dejó nada, se escribe «nada»: es un dato, no un olvido.)_
