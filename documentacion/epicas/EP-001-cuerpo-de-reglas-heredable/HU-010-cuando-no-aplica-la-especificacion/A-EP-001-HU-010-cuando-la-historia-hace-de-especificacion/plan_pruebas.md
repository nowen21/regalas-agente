# Plan de Pruebas — Fase A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-001-HU-010 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Qué texto se prueba.** El que decida la duda 1 del plan. Los casos están escritos contra **lo que la regla tiene que lograr**, no contra una redacción concreta: sirven para cualquiera de los dos caminos del pendiente [20](../../../../../pendientes/20-f2-no-dice-cuando-no-aplica.md).

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Lectura por alguien ajeno | Que la regla se entienda sin haber estado en la conversación que la decidió | Este repositorio | No — es el punto: si hiciera falta explicarla, no está escrita |
| Medición sobre fases reales | Que las fases que hoy se apoyan en su historia queden cubiertas o queden dichas | Este repositorio | Parcial |
| Programa | Que `validar.py flujo` no reporte falta de especificación donde la regla exime | Este repositorio | Sí |
| No regresión | Que la exigencia siga en pie para el código de un módulo | Este repositorio | Sí |

**Por qué la lectura por alguien ajeno es el caso principal del CA-01.** El defecto que la fase corrige es que cada sesión resuelve el caso por criterio propio. Si la regla necesita que alguien la explique, sigue sin resolverlo.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Usabilidad del texto | ☑ | El CA-01: se responde leyendo, sin preguntar |
| Funcional | ☑ | El CA-02 sobre las fases contadas |
| No regresión | ☑ | Una fase que sí entrega código de módulo sigue necesitando especificación |
| Límites | ☑ | La fase mezclada, que entrega texto normativo y código a la vez |

### 3.3 Técnicas de diseño de casos

- **El lector que no participó** — el CA-01 se prueba con alguien que no estuvo en la decisión. Es la única forma de separar "la regla está clara" de "yo ya sé lo que quisimos decir".
- **Medición fechada** — la tabla del CA-02 se levanta al final y dice **contra qué día se contó** (riesgo `R-04`): la cuenta cambia mientras se trabaja porque se abren fases nuevas.
- **El par exime / no exime** — no basta con que el revisor calle donde la regla exime: tiene que **seguir hablando** donde no. Sin la segunda mitad, el caso pasaría con un revisor que dejó de mirar.
- **El caso que hoy no existe** — la fase mezclada se escribe aunque hoy no haya ninguna: si no está escrito, el primero que se lo encuentre lo resuelve por su cuenta, que es el defecto original.
- **Nada hacia atrás** — ninguna fase cerrada se reabre (RN-05). El caso lo comprueba: la regla nueva no vuelve incumplidora a una fase sellada.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py flujo` y `estandar` sobre este repositorio, y `validadores/pruebas.py` entera **solo si** la duda 3 obliga a tocar `flujo.py`.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-010 | [CA-01](../HU-010-cuando-no-aplica-la-especificacion.md#ca-01--la-regla-dice-cuándo-no-aplica) | [CP-001](#cp-001--alguien-ajeno-a-la-decisión-responde-leyendo-solo-la-regla), [CP-002](#cp-002--la-fase-mezclada-tiene-respuesta-escrita) | Usabilidad del texto | Crítica | No | ☐ |
| HU-010 | [CA-02](../HU-010-cuando-no-aplica-la-especificacion.md#ca-02--las-dos-fases-abiertas-quedan-resueltas) | [CP-003](#cp-003--las-fases-que-se-apoyan-en-su-historia-quedan-cubiertas-o-quedan-dichas), [CP-004](#cp-004--el-revisor-calla-donde-la-regla-exime-y-habla-donde-no) | Funcional | Alta | Parcial | ☐ |
| HU-010 | RNF — claridad y no regresión | [CP-005](#cp-005--el-código-de-un-módulo-sigue-necesitando-su-especificación), [CP-006](#cp-006--ninguna-fase-cerrada-se-vuelve-incumplidora) | No regresión | Alta | Parcial | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Alguien ajeno a la decisión responde leyendo solo la regla

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Tipo** | Usabilidad del texto |
| **Prioridad** | Crítica |
| **Precondiciones** | La regla ya escrita (T-01), y un lector que no participó de la decisión |
| **Datos de entrada** | Tres fases: una que entrega texto normativo, una que entrega código de módulo y una que entrega un programa de comprobación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Darle al lector solo la regla, sin explicarla | La tiene a la vista, sin contexto de la conversación |
| 2 | Preguntarle por la primera fase: ¿necesita especificación? | Responde sin preguntar de vuelta |
| 3 | Repetir con la segunda y la tercera | Responde las tres |
| 4 | Comparar sus tres respuestas contra las que la regla pretendía | Coinciden las tres |

**Resultado esperado final:** el caso deja de resolverse por criterio propio de cada sesión.

> **El paso 4 es el que decide.** Que responda rápido no basta: lo que prueba el CA es que responda **lo mismo** que la regla quiso decir.

---

### CP-002 — La fase mezclada tiene respuesta escrita

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-01 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | La tarea T-03 hecha |
| **Datos de entrada** | Una fase supuesta que entrega texto normativo **y** código a la vez |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Buscar en la regla el criterio de la fase mezclada | Está escrito, no se deduce |
| 2 | Aplicarlo a la fase supuesta | Da una sola respuesta, no dos posibles |
| 3 | Comprobar que la respuesta no deja el código sin especificación | La parte de código sigue exigiéndola |

**Resultado esperado final:** el caso que hoy no existe queda resuelto antes de que aparezca.

---

### CP-003 — Las fases que se apoyan en su historia quedan cubiertas, o quedan dichas

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | La regla escrita |
| **Datos de entrada** | Las fases del repositorio, contadas el día de la corrida |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Levantar la tabla de fases y cómo llenan la casilla de especificación | La tabla dice **contra qué día** se contó |
| 2 | Separar las que se apoyan en su historia de las que declararon la deuda | Dos grupos, con su número cada uno |
| 3 | Marcar cuáles quedan cubiertas por la regla nueva | Cada fila con su veredicto |
| 4 | Anotar las que no quedan cubiertas, con el motivo | Ninguna queda sin veredicto |

**Resultado esperado final:** la cuenta del pendiente 20 deja de ser "dos casos" y pasa a ser el número real, con fecha.

---

### CP-004 — El revisor calla donde la regla exime, y habla donde no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | La regla escrita, y `flujo.py` en el estado que decida la duda 3 |
| **Datos de entrada** | Una fase eximida y una fase no eximida |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` sobre la fase eximida | Ninguna falla por falta de especificación |
| 2 | Correr sobre la fase no eximida, sin su especificación | Sale la falla |
| 3 | Comparar las dos corridas | La diferencia es la exención, no que el revisor haya dejado de mirar |

**Resultado esperado final:** la regla y el programa dicen lo mismo.

> **El paso 2 es el que da valor al 1.** Sin él, el caso pasaría con un revisor que ya no comprueba nada.

---

### CP-005 — El código de un módulo sigue necesitando su especificación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / RNF |
| **Tipo** | No regresión |
| **Prioridad** | Alta |
| **Precondiciones** | La regla escrita |
| **Datos de entrada** | Una fase que entrega código de un módulo, sin especificación |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Aplicarle la regla nueva | No queda eximida |
| 2 | Correr `validar.py flujo` sobre ella | Sale la falla, igual que antes del cambio |
| 3 | Comprobar que la exención lleva sus tres partes: condición, límite y quién autoriza | Las tres, si el camino elegido fue el de la excepción ([`20·M8`](../../../../../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md)) |

**Resultado esperado final:** la exención no es la puerta por donde se salta la especificación siempre (riesgo `R-02`).

---

### CP-006 — Ninguna fase cerrada se vuelve incumplidora

| Campo | Valor |
|---|---|
| **HU / CA** | HU-010 / RNF |
| **Tipo** | No regresión |
| **Prioridad** | Alta |
| **Precondiciones** | La regla escrita |
| **Datos de entrada** | Las fases ya cerradas y selladas del repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `validar.py flujo` sobre el repositorio antes del cambio | Queda la línea base con su número de hallazgos |
| 2 | Correr después del cambio | Ningún hallazgo nuevo sobre una fase cerrada |
| 3 | Comparar las dos corridas fase por fase | Lo que cambió, cambió hacia adelante (RN-05) |

**Resultado esperado final:** cambiar la norma no reabre lo cerrado ([`20·M10`](../../../../../base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md)).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que la regla nueva vuelva incumplidoras a fases cerradas (riesgo `R-01`) | Inmediato. Se reescribe: la RN-05 lo prohíbe |
| **Alta** | Que el lector del CP-001 responda distinto de lo que la regla pretendía | Inmediato — la regla no está escrita, está insinuada |
| **Alta** | Que la exención quede sin condición, sin límite o sin quién autoriza | Antes de cerrar |
| **Media** | Que tocar `flujo.py` rompa una prueba de la suite (riesgo `R-03`) | Se corre la suite completa y se corrige antes de seguir |
| **Baja** | Que la cuenta de fases cambie mientras se trabaja | Se admite: la tabla dice contra qué día se contó |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 6 de 6 |
| Respuestas del lector ajeno que coinciden con la regla | 3 de 3 |
| Fases de la tabla sin veredicto | **0** |
| Hallazgos nuevos sobre fases cerradas | **0** |
| Fases cerradas reabiertas | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
