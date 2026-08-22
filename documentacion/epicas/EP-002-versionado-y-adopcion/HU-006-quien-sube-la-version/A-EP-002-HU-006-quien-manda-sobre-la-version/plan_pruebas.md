# Plan de Pruebas — Fase A-EP-002-HU-006-quien-manda-sobre-la-version   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-002-HU-006 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-002-HU-006-quien-manda-sobre-la-version` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/ciclo-vida-proyectos/08-plan-pruebas.md)).

**Qué texto se prueba.** El que decidan las dudas 1 a 3. Los casos están escritos contra **lo que la regla tiene que lograr** —que no queden dos numeraciones, y que nadie se lleve trabajo ajeno—, así que sirven para cualquiera de las tres salidas del pendiente [22](../../../../../pendientes/hecho/dos-sesiones-versionando-a-la-vez.md).

**Condición de arranque.** La simulación corre sobre **dos copias** de este repositorio. Durante la simulación no se escribe en el repositorio vivo.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Simulación de convivencia | Que dos sesiones que suben versión sobre la misma copia no dejen dos numeraciones | Dos copias locales del repositorio | No |
| Aislamiento del guardado | Que una sesión guarde lo propio con trabajo ajeno presente en el árbol | Copia local | No |
| Recuento | Que ninguna entrada del registro se pierda por el cruce | Copia local | Parcial |
| Histórico | Que la regla nueva hubiera resuelto los cuatro casos ya ocurridos | Este repositorio, en lectura | No |

**Por qué los casos ocurridos son material de prueba.** Una regla de convivencia sin los casos que la motivaron se vuelve a discutir cada vez. Los cuatro se escriben con **qué habría hecho la regla nueva en cada uno**, que es la comprobación más honesta que se puede hacer de algo que ya pasó.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Concurrencia | ☑ | Dos sesiones sobre el mismo archivo único |
| No regresión | ☑ | El registro no pierde entradas |
| Histórico | ☑ | Los cuatro casos ocurridos |

### 3.3 Técnicas de diseño de casos

- **Simulación con dos copias, no con el repositorio vivo** — arriba. Probar convivencia en el árbol real es exactamente el accidente que la HU quiere evitar.
- **Contraste contra lo que pasó** — el oráculo del CA-01 no es la regla nueva: es el 2026-08-14, cuando quedaron dos numeraciones y el día cerró en `12.2.0`. Si la regla aplicada a ese día no lo resuelve, no sirve.
- **Recuento antes y después** — el RNF se mide contando entradas del registro antes del cruce y después. "Se ve bien" no es una medición.
- **El tramo roto no se corrige** — renumerar para dejar la serie limpia rompería toda cita hecha a esas versiones. Se prueba **con** el tramo tal como quedó.
- **Honestidad sobre lo que no se comprueba** — si la regla no se puede mirar con un programa, se declara así en `reglas-validables.md` (riesgo `R-03`). Una regla honesta sobre su falta de comprobación vale más que una comprobación falsa.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `validar.py versiones` y `estandar` sobre las copias, más `validadores/pruebas.py` entera si la regla obliga a tocar código.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-006 | [CA-01](../HU-006-quien-sube-la-version.md#ca-01--dos-sesiones-no-dejan-dos-numeraciones) | [CP-001](#cp-001--dos-sesiones-suben-versión-y-queda-una-sola-numeración), [CP-002](#cp-002--la-regla-aplicada-al-2026-08-14-lo-resuelve) | Concurrencia | Crítica | No | ☐ |
| HU-006 | [CA-02](../HU-006-quien-sube-la-version.md#ca-02--nadie-arrastra-el-trabajo-de-otro) | [CP-003](#cp-003--se-guarda-lo-propio-con-trabajo-ajeno-en-el-árbol), [CP-004](#cp-004--los-cuatro-casos-ocurridos-contra-la-regla-nueva) | Funcional | Crítica | No | ☐ |
| HU-006 | RNF — que el registro no pierda entradas | [CP-005](#cp-005--ninguna-entrada-del-registro-se-pierde-por-el-cruce) | No regresión | Alta | Parcial | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — Dos sesiones suben versión, y queda una sola numeración

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Concurrencia |
| **Prioridad** | Crítica |
| **Precondiciones** | Dudas 1 a 3 resueltas. Dos copias locales del repositorio |
| **Datos de entrada** | Dos cambios de regla distintos, uno por copia, hechos sin verse |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Anotar `VERSION` y el número de entradas del registro | Queda la línea base |
| 2 | En la copia A, hacer el cambio y subir versión según la regla | Queda una versión nueva |
| 3 | En la copia B, hacer el otro cambio y subir versión según la regla | La regla dice qué hacer, y no queda una segunda serie |
| 4 | Juntar las dos copias | Una sola numeración, sin números repetidos ni saltados |
| 5 | Correr `validar.py versiones` sobre el resultado | Sin hallazgos de continuidad |

**Resultado esperado final:** el 2026-08-14 no vuelve a pasar.

---

### CP-002 — La regla aplicada al 2026-08-14 lo resuelve

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-01 |
| **Tipo** | Histórico |
| **Prioridad** | Crítica |
| **Precondiciones** | La regla escrita |
| **Datos de entrada** | Lo que pasó el 2026-08-14: dos numeraciones vivas y el día cerrado en `12.2.0` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Reconstruir la secuencia de ese día desde el registro | Queda a la vista, sin tocarla |
| 2 | Aplicarle la regla nueva paso por paso | Sale una sola numeración |
| 3 | Comprobar que la regla decide **quién manda**, no que "hay que coordinarse" | Hay una respuesta concreta en cada cruce |
| 4 | Comprobar que el tramo real no se modificó | El registro quedó igual |

**Resultado esperado final:** la regla se valida contra el hecho que la motivó, no contra sí misma.

> **Esto es triangulación** ([`08·T7`](../../../../../base/08-pruebas.md#t7--triangulación-derivar-los-casos-no-adivinarlos)): el resultado esperado sale de un día que ya pasó, no del criterio que se está probando.

---

### CP-003 — Se guarda lo propio con trabajo ajeno en el árbol

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Funcional |
| **Prioridad** | Crítica |
| **Precondiciones** | Una copia local con cambios de dos orígenes distintos sin guardar |
| **Datos de entrada** | Archivos propios y archivos ajenos, modificados y sin guardar |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Listar qué archivos son propios y cuáles ajenos | Queda la separación escrita antes de guardar |
| 2 | Guardar solo lo propio | Se guarda lo propio |
| 3 | Comprobar qué quedó en el guardado | Ningún archivo ajeno |
| 4 | Comprobar que lo ajeno sigue sin guardar y sin tocar | Sigue en el árbol, igual que estaba |

**Resultado esperado final:** guardar lo propio no arrastra lo de nadie.

> **El paso 1 va aparte a propósito.** Si se juntara con el 2, no quedaría rastro de contra qué lista se decidió qué era propio.

---

### CP-004 — Los cuatro casos ocurridos contra la regla nueva

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / CA-02 |
| **Tipo** | Histórico |
| **Prioridad** | Alta |
| **Precondiciones** | La regla escrita |
| **Datos de entrada** | Los cuatro cruces ya ocurridos, con lo que se llevó cada uno |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Escribir los cuatro casos, con qué pasó en cada uno | Quedan documentados, con fecha |
| 2 | Aplicarle a cada uno la regla nueva | Sale qué habría hecho |
| 3 | Comprobar que en los cuatro el resultado es distinto del real | La regla habría cambiado el desenlace |
| 4 | Anotar el que no cambie, con el motivo | Queda como límite conocido de la regla |

**Resultado esperado final:** la regla se justifica con hechos y no con una discusión que hay que repetir.

---

### CP-005 — Ninguna entrada del registro se pierde por el cruce

| Campo | Valor |
|---|---|
| **HU / CA** | HU-006 / RNF |
| **Tipo** | No regresión |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | El registro antes y después del cruce simulado |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las entradas antes del cruce | Queda el número |
| 2 | Contar después de juntar las dos copias | Es el de antes más las dos nuevas |
| 3 | Comprobar que ninguna entrada quedó pisada | Cada una con su texto entero |
| 4 | Borrar las dos copias de la simulación | No queda rastro |

**Resultado esperado final:** el cruce puede resolverse sin que se caiga una entrada al piso (RN-04).

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que se escriba en el repositorio vivo durante la simulación | Inmediato. Se detiene la fase y se restaura |
| **Crítica** | Que la regla aplicada al 2026-08-14 no resuelva el cruce | Inmediato — la regla no sirve y se vuelve a la duda 1 |
| **Alta** | Que una entrada del registro se pierda en el cruce | Antes de cerrar |
| **Media** | Que la salida elegida obligue a tocar `M10` (riesgo `R-01`) | Se declara antes de tocarla; si es más que una nota, se propone como fase aparte |
| **Media** | Que el acuerdo cubra solo `VERSION` y el problema siga en los índices (riesgo `R-02`) | Es la duda 2, y por eso se pregunta antes de escribir |
| **Baja** | Que la regla no se pueda comprobar con un programa | Se declara así en `reglas-validables.md` |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 5 de 5 |
| Numeraciones vivas al final del cruce simulado | **1** |
| Archivos ajenos arrastrados al guardar | **0** |
| Entradas del registro perdidas | **0** |
| Escrituras en el repositorio vivo durante la simulación | **0** |
| Casos ocurridos documentados | 4 de 4 |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
