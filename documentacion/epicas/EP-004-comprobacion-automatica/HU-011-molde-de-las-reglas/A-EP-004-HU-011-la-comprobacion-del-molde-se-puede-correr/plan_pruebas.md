# Plan de Pruebas — Fase A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-004-HU-011 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-004-HU-011-la-comprobacion-del-molde-se-puede-correr` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Nada se puede probar hasta que el programa se pueda correr.** Hoy `metareglas.py` no imprime nada y sale con 0. Abrir la puerta —T-01— es la precondición de los cinco CA.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Punto de entrada | Que el programa corra y diga algo | Este repositorio | Sí |
| Negativa por CA | Que cada defecto del molde se reporte, y su versión correcta no | Carpetas temporales | Sí |
| Medición | Cuál es la cuenta real de reglas sin checklist el día de la corrida | Este repositorio | Parcial |

**Por qué no se reescriben las comprobaciones.** Reescribir y correr a la vez impide saber si un hallazgo es del programa viejo o del nuevo. Esta fase **abre la puerta** al programa que ya está.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los cinco CA |
| Negativa | ☑ | Cada CA con su defecto sembrado |
| Seguridad del cuerpo de reglas | ☑ | El CA-02: la dependencia que manda hacia arriba es la que protege el núcleo |
| Medición | ☑ | La cuenta real contra las 121 del pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) |

### 3.3 Técnicas de diseño de casos

- **Cada CA con su par** — defecto sembrado y versión correcta. Con solo el defecto no se distingue "lo detecta" de "reporta siempre".
- **Ningún programa termina en silencio** — el caso del punto de entrada comprueba que, si algo no se puede correr, el programa **muere diciendo por dónde se corre**. Es la exigencia del pendiente [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md): salir con 0 sin haber mirado es peor que fallar.
- **La cuenta se mide, no se hereda** — el pendiente 19 dice 121 reglas sin checklist. Esa cuenta se hizo a mano; la corrida da la real, y la del pendiente se corrige con ella.
- **La avalancha esperada, declarada** — el riesgo `R-01`: abrir la puerta va a destapar cientos de hallazgos. Se anotan como línea base del primer día, y la entrada del registro lo dice, para que no se lea como regresión.
- **Un caso resuelto no cierra el pendiente** — el riesgo `R-03`: el [53](../../../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) queda abierto por sus otros puntos.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validadores/pruebas.py` entera —se toca `validar.py`— más el subcomando nuevo sobre este repositorio y sobre las carpetas temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-011 | [CA-01](../HU-011-molde-de-las-reglas.md#ca-01--un-identificador-repetido-o-con-prefijo-ajeno-se-reporta) | [CP-001](#cp-001--el-programa-corre-y-no-termina-en-silencio), [CP-002](#cp-002--el-identificador-repetido-y-el-de-prefijo-ajeno-se-reportan) | Negativa | Crítica | Sí | ☐ |
| HU-011 | [CA-02](../HU-011-molde-de-las-reglas.md#ca-02--una-dependencia-que-no-existe-o-que-manda-hacia-arriba-se-reporta) | [CP-003](#cp-003--la-dependencia-inexistente-y-la-que-manda-sobre-una-blindada-se-reportan) | Seguridad | Crítica | Sí | ☐ |
| HU-011 | [CA-03](../HU-011-molde-de-las-reglas.md#ca-03--una-regla-sin-su-checklist-se-reporta) | [CP-004](#cp-004--la-regla-sin-bloque-de-checklist-se-reporta-y-la-cuenta-real-se-mide) | Negativa | Alta | Sí | ☐ |
| HU-011 | [CA-04](../HU-011-molde-de-las-reglas.md#ca-04--una-regla-que-nombra-una-tecnología-se-reporta) | [CP-005](#cp-005--la-regla-que-nombra-un-lenguaje-se-reporta-y-su-versión-agnóstica-no) | Negativa | Alta | Sí | ☐ |
| HU-011 | [CA-05](../HU-011-molde-de-las-reglas.md#ca-05--una-regla-del-proyecto-sin-respaldo-en-la-base-se-reporta) | [CP-006](#cp-006--la-regla-propia-sin-respaldo-se-reporta-y-la-que-lo-tiene-no) | Negativa | Alta | Sí | ☐ |
| HU-011 | RNF — que ningún validador vuelva a callar sin haber mirado | [CP-001](#cp-001--el-programa-corre-y-no-termina-en-silencio) | Funcional | Crítica | Sí | ☐ |

**Cobertura:** 5 de 5 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El programa corre y no termina en silencio

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-01 y RNF |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Duda 1 resuelta: uno con dos modos o dos subcomandos |
| **Datos de entrada** | Este repositorio |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr el programa **antes** del cambio | No imprime nada y sale con 0: queda la evidencia del defecto |
| 2 | Aplicar el punto de entrada | Queda aplicado |
| 3 | Correr el subcomando nuevo | Imprime hallazgos o dice que no encontró ninguno |
| 4 | Correr en una situación donde no pueda trabajar | **Muere diciendo por dónde se corre**, no calla |
| 5 | Comprobar que nunca sale con 0 sin haber mirado | Nunca |

**Resultado esperado final:** el silencio deja de ser una forma de pasar.

> **El paso 1 se corre a propósito antes del cambio.** Sin esa evidencia, el arreglo no tiene contra qué compararse.

---

### CP-002 — El identificador repetido y el de prefijo ajeno se reportan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-01 |
| **Tipo** | Negativa |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Carpeta temporal con un cuerpo de reglas de mentira |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sembrar dos reglas con el mismo identificador | Se reporta la repetición |
| 2 | Sembrar una regla con el prefijo de otro capítulo | Se reporta |
| 3 | Correr sobre un cuerpo sin esos defectos | No sale hallazgo |
| 4 | Comprobar que el hallazgo nombra las dos reglas en conflicto | Las nombra |

**Resultado esperado final:** el identificador único deja de depender de que nadie se equivoque ([`20·M4`](../../../../../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md)).

---

### CP-003 — La dependencia inexistente y la que manda sobre una blindada se reportan

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-02 |
| **Tipo** | Seguridad |
| **Prioridad** | Crítica |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Una regla que depende de un identificador que no existe, y una de capa 2 que deroga una `[BLINDADA]` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sembrar la dependencia a un identificador inexistente | Se reporta, y nombra el identificador que falta |
| 2 | Sembrar la regla de capa 2 que manda sobre una blindada | Se reporta |
| 3 | Corregir la dependencia y volver a correr | Deja de reportarse |
| 4 | Comprobar sobre el cuerpo real que ninguna regla manda hacia arriba | Ninguna, o se anota cuál |

**Resultado esperado final:** lo que protege el núcleo se puede correr, no solo leer.

> **Este es el caso más caro de los cinco.** Una regla normal que mande sobre una `[BLINDADA]` desarma el capítulo `00` entero.

---

### CP-004 — La regla sin bloque de checklist se reporta, y la cuenta real se mide

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-03 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Una regla sin bloque de checklist y otra con él; y el cuerpo real |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sembrar la regla sin bloque de checklist | Se reporta |
| 2 | Sembrar la que sí lo tiene | No se reporta |
| 3 | Correr sobre el cuerpo real y contar cuántas reglas salen | Sale un número |
| 4 | Comparar contra las 121 que dice el pendiente [19](../../../../../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md) | Se anota la diferencia |
| 5 | Corregir la cuenta del pendiente con lo medido | El pendiente queda con el dato real |

**Resultado esperado final:** la deuda del capítulo `20` deja de estimarse a mano.

---

### CP-005 — La regla que nombra un lenguaje se reporta, y su versión agnóstica no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-04 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Una regla que nombra un lenguaje, y la misma exigencia escrita sin nombrarlo |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Sembrar la regla con nombre de tecnología | Se reporta ([`20·M3`](../../../../../base/20-meta-reglas/reglas/M3-la-base-es-agnostica-sin-stack-y-sin-dominio.md)) |
| 2 | Sembrar la versión agnóstica | No se reporta |
| 3 | Sembrar una que **ilustra** con una herramienta sin exigirla | Se anota qué hace el programa: si la reporta, es falso positivo |
| 4 | Correr sobre el cuerpo real | Se anotan los hallazgos que salgan |

**Resultado esperado final:** la agnosticidad se comprueba, y se sabe si el programa distingue exigir de ilustrar.

---

### CP-006 — La regla propia sin respaldo se reporta, y la que lo tiene no

| Campo | Valor |
|---|---|
| **HU / CA** | HU-011 / CA-05 |
| **Tipo** | Negativa |
| **Prioridad** | Alta |
| **Precondiciones** | El punto de entrada acepta la comprobación del catálogo de un proyecto (T-07) |
| **Datos de entrada** | Un catálogo de proyecto de mentira, con una regla sin respaldo y otra con respaldo válido |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr sobre el catálogo con la regla sin respaldo | Se reporta ([`20·M16`](../../../../../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md)) |
| 2 | Correr sobre la que nombra una regla de base que existe | No se reporta |
| 3 | Probar una que nombra una regla de base que **no** existe | Se reporta |
| 4 | Comprobar que ninguna corrida escribió en el catálogo | Ningún archivo modificado |

**Resultado esperado final:** el respaldo de la capa 3 se comprueba, y no alcanza con nombrar cualquier cosa.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que el programa siga saliendo con 0 sin haber mirado | Inmediato. Es el defecto que la fase viene a cerrar |
| **Crítica** | Que una regla que manda sobre una `[BLINDADA]` no se reporte | Inmediato. El CA-02 queda en «No» |
| **Alta** | Que alguna comprobación reporte de más (riesgo `R-02`) | **Se para y se propone**: corregir la comprobación es otra fase |
| **Media** | Que al abrir la puerta aparezcan cientos de hallazgos (riesgo `R-01`) | Se anotan como línea base del primer día, dicho en el registro |
| **Media** | Que el arreglo se lea como cierre del pendiente 53 (riesgo `R-03`) | Se marca este caso como resuelto; el pendiente queda abierto por sus otros puntos |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 5 CA y los RNF con caso |
| Casos ejecutados | 6 de 6 |
| Corridas que terminan en silencio con código 0 | **0** |
| Reglas sin checklist | La cuenta real medida, contra las 121 estimadas |
| Reglas que mandan hacia arriba | **0**, o todas anotadas |
| Comprobaciones del programa modificadas | **0** — corregirlas es otra fase |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
