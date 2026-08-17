# Plan de Pruebas — Fase A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice **cómo se comprueba que lo construido hace lo que la HU pidió**: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que **ningún criterio de aceptación quede sin al menos un caso**. Se aprueba **antes** de correr la primera prueba y **no se modifica al ejecutar**: lo que pasó va en el `resultado_pruebas.md` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-A-EP-006-HU-007 |
| **Versión** | 1.0 |
| **Alcance del plan** | Fase `A-EP-006-HU-007-retrodocumentar-la-marca-de-lo-que-dejo-de-aplicar` |
| **Fecha** | 2026-08-17 |
| **Elaborado por** | El agente |
| **Aprobado por** | Sin aprobar — se presenta junto con el [`plan_trabajo.md`](plan_trabajo.md) ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) |
| **Estado** | Borrador |

> Fase chica: se llenan las secciones **3, 5, 6, 9 y 12** ([proporcionalidad de la plantilla](../../../../../plantillas/planes/pruebas.md)).

**Condición de arranque.** Las pruebas corren sobre una **base temporal**. La base real tiene el aprendizaje del proyecto.

---

## 3. Estrategia de pruebas

### 3.1 Niveles de prueba

| Nivel | Objetivo | Ambiente | Automatizado |
|---|---|---|---|
| Conservación | Que la señal marcada **siga existiendo** en la tabla | Base temporal | Sí |
| Visibilidad | Que lo marcado no aparezca en la búsqueda | Base temporal | Sí |
| Estados | Que los cinco estados hagan lo que dicen | Base temporal | Sí |
| Vigencia | Que lo no revisado hace meses se distinga de lo fresco | Base temporal, con fechas puestas a mano | Sí |

**Por qué se comprueba la fila y no solo la búsqueda.** No aparecer y no existir se ven **igual** desde la búsqueda, y lo que la HU exige es que exista.

### 3.2 Tipos de prueba

| Tipo | Aplica | Criterio |
|---|:--:|---|
| Funcional | ☑ | Los dos CA |
| Integridad | ☑ | Ninguna señal se borra, en ningún estado |
| Límites | ☑ | La vigencia, con fechas fijas |
| Cobertura de estados | ☑ | Los cinco, uno por uno |

### 3.3 Técnicas de diseño de casos

- **Los cinco estados, uno por uno** — cada uno tiene su motivo, y **el que no se prueba es el que se rompe en silencio**. Un solo caso sobre el reemplazo dejaría cuatro sin mirar.
- **Fechas puestas a mano** — la vigencia se prueba con fechas fijas, no esperando a que una señal envejezca. Y no se usa la fecha de hoy, para que el resultado no dependa del huso horario (riesgo `R-03`).
- **Existir y no aparecer, comprobados aparte** — arriba.
- **La señal que reemplaza apunta a la reemplazada** — el caso comprueba el enlace en los dos sentidos: desde la nueva se llega a la vieja, y desde la vieja se sabe cuál la reemplazó.

### 3.5 Alcance de la corrida

Quirúrgica ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)): `memoria/pruebas.py` entera, sobre bases temporales.

---

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-007 | [CA-01](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-01--lo-que-dejó-de-aplicar-queda-marcado-y-visible) | [CP-001](#cp-001--el-reemplazo-conserva-la-vieja-marcada-y-enlazada), [CP-002](#cp-002--lo-archivado-se-puede-seguir-leyendo-si-se-lo-busca-a-propósito) | Integridad | Crítica | Sí | ☐ |
| HU-007 | [CA-02](../HU-007-marcar-lo-que-dejo-de-aplicar.md#ca-02--lo-marcado-no-se-confunde-con-lo-vigente) | [CP-003](#cp-003--los-cinco-estados-uno-por-uno), [CP-004](#cp-004--la-señal-sin-revisar-hace-meses-se-distingue-de-una-fresca) | Funcional | Alta | Sí | ☐ |
| HU-007 | RNF — que nada se borre y nada se confunda | [CP-003](#cp-003--los-cinco-estados-uno-por-uno) | Integridad | Crítica | Sí | ☐ |

**Cobertura:** 2 de 2 CA, más los RNF = 100%.

---

## 6. Casos de prueba

### CP-001 — El reemplazo conserva la vieja, marcada y enlazada

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Integridad |
| **Prioridad** | Crítica |
| **Precondiciones** | Base temporal con una señal activa |
| **Datos de entrada** | Una señal que reemplaza a otra |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Contar las señales de la base | Sale un número |
| 2 | Reemplazar la señal por una nueva | Entra la nueva |
| 3 | Contar otra vez | El número **subió en uno**: nada se borró |
| 4 | Comprobar que la vieja quedó marcada como reemplazada | Marcada |
| 5 | Comprobar que desde la nueva se llega a la vieja | Se llega |
| 6 | Comprobar que desde la vieja se sabe cuál la reemplazó | Se sabe |

**Resultado esperado final:** el reemplazo agrega, no sustituye, y la cadena se puede recorrer en los dos sentidos.

> **El paso 3 es el que prueba «sin borrarlo».** Comprobar solo la marca no distingue reemplazar de sobrescribir.

---

### CP-002 — Lo archivado se puede seguir leyendo si se lo busca a propósito

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondiciones** | El CP-001 corrido |
| **Datos de entrada** | Una señal archivada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Archivar una señal | Queda marcada |
| 2 | Buscarla en la búsqueda normal | No aparece |
| 3 | Pedirla a propósito, incluyendo lo archivado | Aparece, con su contenido entero |
| 4 | Comprobar que dice desde cuándo está archivada | Lo dice |

**Resultado esperado final:** archivar esconde, no borra, y lo escondido se puede recuperar.

---

### CP-003 — Los cinco estados, uno por uno

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 y RNF |
| **Tipo** | Cobertura de estados |
| **Prioridad** | Crítica |
| **Precondiciones** | Base temporal con una señal por estado |
| **Datos de entrada** | Señales en los cinco estados: activa, reemplazada, revertida, archivada y cerrada |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner una señal en cada uno de los cinco estados | Quedan las cinco |
| 2 | Buscar con la búsqueda normal | Aparece **solo** la activa |
| 3 | Comprobar una por una que las otras cuatro siguen en la tabla | Las cuatro |
| 4 | Por cada estado, comprobar que hace lo que dice su nombre | Los cinco |
| 5 | Contar el total antes y después de todo el recorrido | El mismo: ninguna se borró |

**Resultado esperado final:** los cinco estados están probados, y el que se rompa no lo hará en silencio.

> **Probar solo el reemplazo dejaría cuatro sin mirar**, y el que no se prueba es el que pierde memoria sin que nadie lo note (riesgo `R-01`).

---

### CP-004 — La señal sin revisar hace meses se distingue de una fresca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-007 / CA-02 |
| **Tipo** | Límites |
| **Prioridad** | Alta |
| **Precondiciones** | Base temporal, con fechas de revisión **puestas a mano** |
| **Datos de entrada** | Una señal revisada hace mucho y otra revisada recién |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Poner las dos señales con sus fechas fijas | Quedan puestas |
| 2 | Buscar y mirar cómo se muestra cada una | La vieja se distingue de la fresca |
| 3 | Revisar la vieja y volver a buscar | Ahora se muestra como fresca |
| 4 | Comprobar que el resultado no depende de la fecha de hoy ni del huso horario | No depende |
| 5 | Comprobar que ninguna de las dos se borró ni cambió de estado | Ninguna |

**Resultado esperado final:** la vigencia se ve, y la prueba no envejece.

---

## 9. Gestión de defectos

| Severidad | Qué sería en esta fase | Atención |
|---|---|---|
| **Crítica** | Que una señal se borre en cualquiera de los cinco estados | Inmediato. Es lo que la HU prohíbe |
| **Crítica** | Que la prueba toque la base real (riesgo `R-02`) | Inmediato. Se detiene y se restaura |
| **Alta** | Que alguno de los cinco estados no funcione como dice (riesgo `R-01`) | Se anota y se propone: el estado que falla pierde memoria en silencio |
| **Media** | Que lo marcado aparezca en la búsqueda normal | Antes de cerrar |
| **Media** | Que la prueba de vigencia dependa del huso horario (riesgo `R-03`) | Fechas fijas puestas a mano, no la de hoy |

Se diagnostica y se deja escrito. Un ciclo nuevo **se agrega** al `resultado_pruebas.md` sin pisar el anterior.

---

## 12. Métricas e informe

| Métrica | Meta |
|---|---|
| Cobertura de exigencias | 100% — los 2 CA y los RNF con caso |
| Casos ejecutados | 4 de 4 |
| Estados probados | 5 de 5 |
| Señales borradas en cualquier estado | **0** |
| Señales de la base real modificadas | **0** |
| Pruebas atadas a la fecha de hoy | **0** |

El veredicto va en el `resultado_pruebas.md` de esta fase; acá solo se dice qué se va a medir.
