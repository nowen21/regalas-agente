# Resultado de Pruebas — Fase A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **qué se ejecutó de verdad y qué salió**, caso por caso, para que el veredicto de la fase no dependa de la memoria de nadie.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** | `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-17 |
| **Fecha de ejecución** | 2026-08-22 |
| **Ejecutado por** | El agente |

---

## 1. Ejecución caso por caso

### CA-01 · La IA se detiene antes de una operación que no se puede deshacer

Existe la regla y existe la escala. [`00·N1`](../../../../../base/00-nucleo-blindado.md) pide aprobación explícita para todo cambio de estado, y el anexo [`acciones-y-riesgo.md`](../../../../../base/00-identidad-y-rol/acciones-y-riesgo.md) reparte las acciones en tres niveles, con la frase que hace útil la tabla:

> Un plan aprobado cubre 🟢 y 🟡 de corrido; **nunca cubre 🔴**. Eso se pide aparte, cada vez, aunque estuviera escrito en el plan.

**Y se usó de verdad hoy.** Esta jornada tuvo dos casos: borrar y reescribir un archivo del repositorio se hizo sin pedir permiso (🟢, se revierte con el commit), y el commit de todo lo construido sigue sin hacerse porque es un permiso aparte que el usuario no ha dado. Siete fases están detenidas en la estación 12 por eso.

**Resultado del criterio: Cumple**, como regla y en la práctica. No hay comprobación automática, y no la puede haber: distinguir lo irreversible de lo que se revierte es lo que la tabla decide, no un programa.

### CA-02 · Una clave pegada en el chat no queda escrita en claro

Existe [`validadores/enmascarar.py`](../../../../../validadores/enmascarar.py), lo usa `historico.py` antes de escribir la transcripción, y funciona. **Pero solo para algunas formas de clave.** Probado el 2026-08-22:

| Lo que se pega | Se enmascara |
|---|---|
| `AKIA1234567890ABCDEF` | **sí** |
| `ghp_abcdefghijklmnopqrstuvwxyz12` | **sí** |
| `API_KEY="supersecreto123456"` | **sí** |
| `API_KEY=supersecreto123456` | **no** |
| `password: MiClave123456` | **no** |
| `la clave del servidor es Patito2026Segura` | **no** |

**El motivo está en el patrón, y es un préstamo.** El enmascarador reusa `secretos._ASIGNA`, que fue escrito para buscar secretos **en código fuente**, donde el valor va entre comillas. En un chat nadie escribe comillas. Las tres formas que fallan son las tres que una persona teclea de verdad.

**Resultado del criterio: No cumple.**

### CA-03 · Un error no se disimula

Es regla con nombre: [`01·C9`](../../../../../base/01-conducta.md#c9--reporta-los-tropiezos), *reporta los tropiezos*.

**Y esta jornada la puso a prueba varias veces**, con constancia escrita en el resumen de la sesión: el agente reportó un defecto que no existía y lo cerró por falso (H-4); corrió la batería entera cuatro veces contra lo que manda `02·F5` y lo dejó anotado (H-8); rompió el marcador `«…»` en 24 sitios y lo dijo. Ninguno de los tres se disimuló.

**Resultado del criterio: Cumple.**

---

## 2. Defectos encontrados

| ID | Severidad | Qué pasó | Estado |
|---|---|---|---|
| D-01 | **Crítica** | El enmascarador no reconoce una clave pegada sin comillas, que es como se pega en un chat. `API_KEY=valor`, `password: valor` y una clave dicha en prosa quedan **escritas en claro en la transcripción, que se versiona** | **Abierto**, necesita pendiente |
| D-02 | Media | El patrón se tomó prestado de la búsqueda de secretos en código, sin revisar si servía para el texto de una conversación. Son dos problemas distintos con la misma cara | **Abierto**, mismo pendiente |

---

## 3. Veredicto por criterio de aceptación

| CA | Cómo se comprobó | Concepto |
|---|---|---|
| CA-01, se detiene ante lo irreversible | `00·N1`, la escala del anexo, y dos casos reales de hoy | Cumple |
| CA-02, la clave no queda en claro | Seis formas probadas: tres se enmascaran, tres no | **No cumple** |
| CA-03, el error no se disimula | `01·C9`, y tres tropiezos reportados hoy | Cumple |

---

## 4. Veredicto de la fase

**Concepto:** No cumple.

**Justificación:** el CA-02 quedó en rojo, y es de núcleo blindado. Lo que falla no es que no exista el enmascarador, sino que solo cubre las formas que un programa escribiría y no las que teclea una persona.

**Qué falta para que cumpla:** que el enmascarador reconozca la asignación sin comillas y la clave dicha en prosa, con el cuidado de no tapar medio texto por parecerse.

---

## 5. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | La escala de acciones | `base/00-identidad-y-rol/acciones-y-riesgo.md` |
| EV-02 | Las seis formas probadas | §1, CA-02 |
| EV-03 | El patrón prestado | `secretos._ASIGNA`, que exige comillas alrededor del valor |
| EV-04 | Tropiezos reportados | Hallazgos H-4 y H-8 del [resumen de la sesión](../../../../../historico-chat/resumenes/2026-08-22/sesion-2.md) |

---

## 6. Ciclos anteriores

Ninguno.
