# Plan de Pruebas — Fase A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-002-HU-002 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-002-HU-002-retrodocumentar-el-registro-de-cambios` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**El registro no se toca.** Lo que falte se anota como hallazgo; una entrada del [`CHANGELOG.md`](../../../../../CHANGELOG.md) no se reescribe (RN-04 de la HU).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Unitario | Que ninguna versión mencionada quede sin entrada propia, y que cada entrada cite la regla por su identificador | Lectura del registro | Sí — entran a `validadores/pruebas.py` |
| Recorrido | Que cada entrada traiga versión, fecha, tipo, qué cambió y por qué | Este repositorio | No |
| Conducta | Qué avisa hoy un cambio de regla sin entrada | Copia del repositorio | No |
| Lectura ajena | Que la entrada se entienda sin haber seguido el cambio | Este repositorio | No |

**Por qué la prueba va en `pruebas.py` y no en `metareglas.py`.** La fila 19 del [checklist](../../../../../base/20-meta-reglas/checklist.md) vive en un programa que **no se puede correr** (pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)). Una comprobación que no corre no comprueba nada.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los tres CA |
| Documento | ☑ | El contenido mínimo de cada entrada (RN-02) |
| Usabilidad del texto | ☑ | El CA-03: se entiende sin contexto |
| No regresión | ☑ | La suite que ya existe, contra su número anotado antes |

### 3.3 Técnicas de diseño de casos

- **El lector que no siguió el cambio** — el CA-03 no lo juzga quien escribió la entrada: quien la escribió la entiende por definición. Quién hace de lector lo decide la duda 1.
- **La prueba que espera fallar** — el CP-003 del CA-02 se escribe sabiendo que hoy **nada frena** un cambio sin entrada. El resultado esperado es exactamente ese, y sirve como evidencia para [EP-005 · HU-005](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md). Escribirlo al revés —esperando que frene— daría un rojo que se leería como defecto de esta fase.
- **Recorrido completo, no muestra** — el CA-01 revisa **todas** las entradas del registro, porque lo que se afirma es que ninguna falta.
- **Hallazgo listado, entrada intacta** — arriba.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —las que ya están más las dos nuevas— y `validar.py versiones` como línea base.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-002 | [CA-01](../HU-002-registro-de-cambios.md#ca-01--cada-versión-tiene-su-entrada) | [CP-001](#cp-001--ninguna-versión-mencionada-queda-sin-entrada-propia), [CP-002](#cp-002--cada-entrada-trae-versión-fecha-tipo-qué-cambió-y-por-qué) | Funcional | Alta | Parcial | ☐ |
| HU-002 | [CA-02](../HU-002-registro-de-cambios.md#ca-02--un-cambio-sin-entrada-no-pasa) | [CP-003](#cp-003--hoy-nada-frena-un-cambio-de-regla-sin-entrada) | Funcional | Crítica | No | ☐ |
| HU-002 | [CA-03](../HU-002-registro-de-cambios.md#ca-03--el-registro-se-entiende-sin-haber-seguido-el-cambio) | [CP-004](#cp-004--alguien-que-no-siguió-el-cambio-dice-qué-cambió-y-a-quién-le-afecta) | Usabilidad del texto | Alta | No | ☐ |
| HU-002 | RNF — que cada entrada cite por identificador | [CP-005](#cp-005--toda-entrada-que-cambia-una-regla-la-nombra-por-su-identificador) | Documento | Media | Sí | ☐ |

**Cobertura:** 3 de 3 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Ninguna versión mencionada queda sin entrada propia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna: la prueba lee y no escribe |
| **Datos de entrada** | El registro entero, y el número de [`VERSION`](../../../../../VERSION) |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Comprobar que la versión de `VERSION` tiene su entrada | La tiene |
| 2 | Recoger todas las versiones mencionadas en el repositorio —derogaciones, sellos de fase, checklists— | Queda la lista, con dónde se mencionan |
| 3 | Comprobar que cada una tiene entrada propia en el registro | Ninguna sin entrada |
| 4 | Anotar como hallazgo la que falte, sin escribirla | Queda citable |

**Resultado esperado final:** una versión que alguien cita existe en el registro, o queda dicho que no.

---

### CP-002 — Cada entrada trae versión, fecha, tipo, qué cambió y por qué

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-01 |
| **Tipo** | Documento |
| **Prioridad** | Alta |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Todas las entradas del registro |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar cuántas entradas tiene el registro | Queda el número, con la fecha de la cuenta |
| 2 | Por cada una, comprobar los cinco datos de la RN-02 | Cada entrada con su veredicto |
| 3 | Listar las incompletas, con qué le falta a cada una | Ninguna se completa: se lista |
| 4 | Comprobar que el registro quedó igual | Ningún byte cambiado |

**Resultado esperado final:** se sabe cuántas entradas cumplen y cuáles no, sin haber tocado ninguna.

> **El paso 4 no es adorno.** El defecto más fácil de cometer acá es "arreglar mientras se revisa", y eso borra el rastro que la HU quiere conservar.

---

### CP-003 — Hoy nada frena un cambio de regla sin entrada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-02 |
| **Tipo** | Funcional — estado del arte |
| **Prioridad** | Crítica |
| **Precondiciones** | Una copia del repositorio. **No se edita el repositorio vivo** |
| **Datos de entrada** | Una regla de `base/` editada en la copia, sin entrada en el registro |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Editar una regla en la copia, sin tocar el registro ni `VERSION` | El archivo queda cambiado |
| 2 | Intentar guardar el cambio | **Nada lo frena** — ese es el resultado esperado hoy |
| 3 | Correr las comprobaciones disponibles | Ninguna reporta la falta de entrada |
| 4 | Dejar escrito qué avisó cada una y qué no | Queda la evidencia, atada a [EP-005 · HU-005](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-005-cambio-de-reglas-con-version/HU-005-cambio-de-reglas-con-version.md) |
| 5 | Borrar la copia | No queda rastro de la edición |

**Resultado esperado final:** el CA-02 queda en «No» con la evidencia de por qué, que es lo que la HU que lo construye necesita.

> **El caso está escrito para pasar afirmando la falta.** Si se hubiera escrito esperando que el cambio se frene, el rojo se leería como defecto de esta fase en vez de como el hueco que es.

---

### CP-004 — Alguien que no siguió el cambio dice qué cambió y a quién le afecta

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / CA-03 |
| **Tipo** | Usabilidad del texto |
| **Prioridad** | Alta |
| **Precondiciones** | Duda 1 resuelta: quién hace de lector |
| **Datos de entrada** | Tres entradas del registro: una MAYOR, una MENOR y una PARCHE |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Darle al lector solo las tres entradas, sin contexto | Las tiene a la vista |
| 2 | Pedirle que diga, por cada una, qué cambió | Responde las tres sin preguntar |
| 3 | Pedirle que diga a quién le afecta y qué tiene que hacer | Responde las tres |
| 4 | Comparar sus respuestas contra lo que la entrada quiso decir | Coinciden |

**Resultado esperado final:** el registro sirve para quien llega después, que es para quien está escrito.

---

### CP-005 — Toda entrada que cambia una regla la nombra por su identificador

| Campo | Valor |
|---|---|
| **HU / CA** | HU-002 / RNF |
| **Tipo** | Documento |
| **Prioridad** | Media |
| **Precondiciones** | El número de pruebas de la suite anotado antes de tocarla |
| **Datos de entrada** | Las entradas que dicen haber cambiado una regla |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aislar las entradas que hablan de una regla | Queda el subconjunto |
| 2 | Comprobar que cada una la nombra por identificador, no solo por descripción | Todas |
| 3 | Comprobar que el identificador nombrado existe, vigente o derogado | Ninguno apunta al vacío |
| 4 | Correr la suite completa y comparar contra la línea base | Ninguna prueba que pasaba, falla |

**Resultado esperado final:** desde el registro se llega a la regla, que es lo que hace rastreable un cambio.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una versión citada en una fase sellada no exista en el registro | Se anota. Corregirlo es otra fase: el registro no se reescribe |
| **Alta** | Que aparezcan entradas sin lo que pide la RN-02 (riesgo `R-01`) | Se listan como hallazgo |
| **Alta** | Que el lector del CP-004 no pueda decir a quién le afecta un cambio | Antes de cerrar — la entrada no sirve para quien llega después |
| **Media** | Que la prueba del CA-01 falle por el tramo de las dos numeraciones vivas | Se documenta la excepción, atada al pendiente [22](../../../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md) |
| **Baja** | Entradas que nombran la regla por descripción y no por identificador | Se listan |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 3 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Entradas del registro recorridas | Todas, con la fecha de la cuenta |
| Entradas del registro modificadas | **0** |
| Versiones mencionadas sin entrada propia | Las que salgan, todas listadas |
| Pruebas de la suite | Las de la línea base, más 2, todas en verde |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
