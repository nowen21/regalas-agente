# Resultado de pruebas — Fase A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-006-HU-005-retrodocumentar-la-separacion-aprendizaje-preferencia` |
| **HU** | [HU-005](../HU-005-separar-aprendizaje-de-preferencia.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) · PP-A-EP-006-HU-005 v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-17 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario ese mismo día |
| **Ambiente y versión** | Este repositorio: los 18 recuerdos y una lectura en solo lectura de las 237 señales. Estándar 23.2.1 |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 3 | 1 | 0 | 0 |

**Veredicto de la fase: No cumple** (§6). El criterio quedó escrito y resuelve el caso de borde, y los 18 recuerdos traen sus tres partes. Lo que falla es el CA-01: **una cosa está guardada en los dos sitios a la vez, y las dos versiones ya dicen cosas distintas.**

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--cinco-cosas-guardadas-clasificadas-con-el-criterio) | CA-01 | Alta | 2026-08-17 | Cinco cosas guardadas de verdad, tres señales y dos recuerdos | **Falla en el paso 3** | EV-02 | D-01 |
| [CP-002](plan_pruebas.md#cp-002--el-caso-de-borde-se-resuelve-con-el-criterio) | CA-01 | Alta | 2026-08-17 | La preferencia que resultó valer para cualquier proyecto | Aprobado | EV-02 | — |
| [CP-003](plan_pruebas.md#cp-003--todo-recuerdo-trae-sus-tres-partes) | CA-02 | Crítica | 2026-08-17 | Los 18 recuerdos de esta casa | Aprobado | EV-01 | — |
| [CP-004](plan_pruebas.md#cp-004--el-recuerdo-sin-el-porqué-se-detecta) | CA-02 | Alta | 2026-08-17 | Un recuerdo armado sin el porqué, y uno completo | Aprobado | EV-01 | — |

---

### Detalle de CP-001 — Cinco cosas guardadas, clasificadas con el criterio

**El criterio que se aplicó** (escrito en esta fase, en [`historico-chat/memory/memory.md`](../../../../../historico-chat/memory/memory.md)): la pregunta que separa los tres sitios es **qué haría que eso cambiara**. Si cambia porque el usuario cambia de opinión, es **preferencia** y va como recuerdo. Si cambia porque cambia el código, es **aprendizaje** y va como señal. Si cambia lo que se le exige a cualquier proyecto, es **regla** y va a `base/`.

**Pasos 2 y 3 — las cinco, con su veredicto y contra dónde están de verdad:**

| # | Lo guardado | Dónde está | Qué dice el criterio | ¿Coincide? |
|---|---|---|---|---|
| 1 | «No usar `git add -A`; stagear por ruta explícita» | Señal `S-001` | **Aprendizaje.** Pasó de verdad —arrastró un archivo local y se publicó— y seguirá siendo cierto aunque el usuario opine distinto | **Sí** |
| 2 | «El estándar es 100% agnóstico; lo específico va solo en capa 3» | Señal `S-003` | **Regla.** Se le exige a cualquier proyecto, y de hecho **ya es** `20·M3` | **No del todo:** está bien que sea señal del día en que se decidió, y su sitio definitivo es `base/`, donde ya está |
| 3 | «Terminología: el agente / el estándar / Claude» | Señal `S-002` **y** recuerdo [Terminología](../../../../../historico-chat/memory/terminologia-agente-vs-estandar.md) | **Preferencia.** Es nomenclatura que el usuario eligió | **No: está en los dos sitios** |
| 4 | «Respuestas cortas» | Recuerdo, y regla `00·ID9` | **Caso de borde**, resuelto: subió a regla y el recuerdo se quedó con el registro de las veces que hubo que repetirlo | **Sí** |
| 5 | «Fixtures sin secretos literales» | Recuerdo | **Aprendizaje**, no preferencia: lo que lo hace cierto es que GitHub bloquea el push, no una opinión del usuario | **No** |

**Paso 4 — las que no coinciden, anotadas y sin mover** (`R-01` del plan: mover un recuerdo cambia lo que rige la sesión):

- **La número 3 es la grave.** No es que esté en el sitio equivocado: está en **los dos**, y **ya dicen cosas distintas**. El recuerdo dice que el proyecto se llama **Cimiento** desde el 2026-08-14; la señal `S-002` sigue diciendo *«'el agente' = Claude Code»*. Es exactamente lo que el índice de la memoria advierte que pasa con dos copias — escrito ahí para el almacén local, y ocurriendo aquí entre los dos sitios del repositorio.
- **La número 5** es aprendizaje guardado como preferencia. Es de bajo daño: se lee igual y no contradice nada. Se anota, no se mueve.

**Paso 5 — lo que debería subir a regla, propuesto y no hecho:** la número 5, «los fixtures no llevan un secreto con forma real», le sirve a cualquier proyecto que use GitHub y hoy vive solo acá. Queda **propuesto**; subirla a `base/` es decisión del usuario (`20·M13`).

---

### Detalle de CP-002 — El caso de borde se resuelve con el criterio

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Tomar la preferencia de borde | Queda a la vista | «Responder corto»: nació como gusto del usuario y hoy se le exige a cualquiera |
| 2 | Aplicarle el criterio | Da una respuesta concreta | **Regla** — cambia lo que se le exige a cualquier proyecto |
| 3 | Comprobar que la respuesta es una sola | Una sola | Una sola. El criterio agrega qué pasa con el recuerdo: **no se borra**, se queda con el registro de que el usuario lo pidió y cuántas veces lo repitió |
| 4 | Si el criterio no permitiera decidirlo, anotarlo | Es hallazgo del criterio | **No hizo falta.** El caso se resuelve, y la prueba está en que **ya está resuelto así en la realidad**: `00·ID9` es regla y [`respuestas-cortas.md`](../../../../../historico-chat/memory/respuestas-cortas.md) sigue existiendo con las tres veces que hubo que repetirlo |

**Por qué el recuerdo no se borra al subir a regla.** «El usuario lo cortó tres veces, dos de ellas seguidas, y siempre al reportar trabajo terminado» no cabe en una regla y es justo lo que evita volver a discutirlo.

---

### Detalle de CP-003 — Todo recuerdo trae sus tres partes

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Contar los recuerdos | Sale un número, con su fecha | **18**, el 2026-08-17 |
| 2 | Comprobar que dice **qué se pide** | Todos | Los 18 |
| 3 | Comprobar que dice **por qué** | Todos | Los 18 |
| 4 | Comprobar que dice **cómo se aplica** | Todos | Los 18 |
| 5 | Listar los incompletos | Se anotan y se completan | **Ninguno.** No hubo nada que completar |

---

### Detalle de CP-004 — El recuerdo sin el porqué se detecta

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr sobre un recuerdo sin el porqué | Se detecta, y dice qué parte falta | Se detecta, y nombra el porqué |
| 2 | Correr sobre el completo | No se detecta | No se detecta |
| 3 | Quitarle otra parte al completo | Se detecta, y nombra esa | Se detecta |
| 4 | Comprobar que **no se juzga si el porqué convence** | No se juzga | No se juzga: la prueba mira que la parte esté, no cómo está redactada. Si el porqué es bueno es criterio, y eso no lo decide un programa |

> **El caso negativo es el que da valor a CP-003.** Sin él, «los 18 traen sus tres partes» lo diría igual un comprobador que no comprueba nada.

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que nada se moviera de sitio | Comparando la carpeta y la base antes y después | **0 recuerdos y 0 señales movidos** |
| 2 | Que la terminología esté duplicada | Leyendo `S-002` en solo lectura y el recuerdo | Duplicada, y **divergente** |
| 3 | Que las tres partes estén en los 18 | Recorriendo la carpeta | 18 de 18 |
| 4 | Que la suite entera siga verde | `python validadores/pruebas.py` | 260 pruebas · verde, con 2 fallos esperados |

---

## 4. Defectos encontrados

| ID | Severidad | Qué es | Dónde queda |
|---|---|---|---|
| D-01 | **Alta** | **La terminología del proyecto está guardada en los dos sitios y las dos versiones ya divergen.** El recuerdo dice «Cimiento» desde el 2026-08-14; la señal `S-002` sigue diciendo «el agente = Claude Code» | Anotado en el criterio nuevo de [`memory.md`](../../../../../historico-chat/memory/memory.md), con el caso citado. **No se movió ni se corrigió ninguna de las dos**: cuál manda lo decide el usuario, y mover un recuerdo cambia lo que rige la sesión (`R-01` del plan) |
| D-02 | Baja | «Fixtures sin secretos literales» es aprendizaje guardado como preferencia, y además le serviría a cualquier proyecto | Anotado y **propuesto** subir a `base/`. No se movió |
| D-03 | Baja | El plan de pruebas declara cobertura completa y **no le escribe caso a los dos transversales** de la HU. Se probaron igual | El plan aprobado no se modifica. Mismo defecto de molde de las 51 fases |

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-005-separar-aprendizaje-de-preferencia.md#ca-01--las-dos-cosas-se-guardan-por-separado) | CP-001, CP-002 | Los dos sitios existen, cada uno con su índice, y ahora hay criterio escrito de cuál va dónde. **Pero una cosa está en los dos a la vez, y divergida** | **No** |
| [CA-02](../HU-005-separar-aprendizaje-de-preferencia.md#ca-02--la-preferencia-dice-por-qué-se-pidió) | CP-003, CP-004 | 18 de 18 con sus tres partes, y el detector caza al que le falta una sin juzgar la redacción | Sí |
| Transversal · Límites | CP-002 | Algo que parece de los dos tipos **tiene criterio para decidirse**: se escribió en esta fase, con su caso de borde | Sí |
| Transversal · No regresión | Verificación 1 | Lo ya guardado no se mezcló al agregar lo nuevo: 0 recuerdos y 0 señales movidos | Sí |

**Los que no cumplen:** el **CA-01**. «Están en lugares distintos» no se cumple mientras una misma cosa esté en los dos. La corrección —decidir cuál manda y dejar que el otro la enlace— **es del usuario**.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 100% de lo que el plan contó, más los dos transversales | Sí |
| Casos ejecutados | Plan §12 | 4 de 4 | 4 de 4 | Sí |
| Recuerdos o señales movidos de sitio | Plan §12 | **0** | **0** | Sí |
| Recuerdos sin sus tres partes | Plan §12 | Todos listados | **0** que listar | Sí |
| Casos de borde que el criterio no resuelve | Plan §12 | **0** | **0** | Sí |
| Recuerdos que deberían ser reglas | Plan §12 | Todos anotados y propuestos | 1 anotado y propuesto (`D-02`) | Sí |

**Lo que no se cumplió:** ninguna meta. Las seis en verde y la fase no cumple, por tercera vez en esta épica: las métricas miraban el criterio y las tres partes, y lo que falla es que **algo está guardado dos veces** — que ninguna medía.

---

## 6. Veredicto de la fase

**Concepto:** **No cumple.**

**Justificación:** el CA-02 quedó verificado, el criterio que faltaba está escrito y resuelve el caso de borde —con la prueba de que ya estaba resuelto así en la práctica—, y nada se movió de sitio. El CA-01 pide que las dos cosas estén «en lugares distintos», y la terminología del proyecto está en los **dos**: como señal `S-002` y como recuerdo. Las dos versiones ya dicen cosas distintas, que es el daño concreto que la separación existía para evitar.

**Qué falta para que cumpla:**

1. Decidir cuál de las dos versiones de la terminología manda, y que la otra la **enlace** en vez de copiarla (`D-01`). Es del usuario: cambiar un recuerdo cambia lo que rige la sesión.
2. Decidir si «fixtures sin secretos literales» sube a `base/` (`D-02`).

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Casos automatizados | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `ElRecuerdoTraeSusTresPartes`: 2 pruebas, en verde |
| EV-02 | Clasificación a mano | La tabla de cinco filas de §2, con dónde está cada una de verdad |
| EV-03 | El criterio escrito | [`historico-chat/memory/memory.md`](../../../../../historico-chat/memory/memory.md), sección «Cuál va dónde» |
| EV-04 | Corrida completa | `python validadores/pruebas.py` — 260 pruebas, verde, 2 fallos esperados |

---

## 8. Ciclos anteriores

Ninguno: es el primero.
