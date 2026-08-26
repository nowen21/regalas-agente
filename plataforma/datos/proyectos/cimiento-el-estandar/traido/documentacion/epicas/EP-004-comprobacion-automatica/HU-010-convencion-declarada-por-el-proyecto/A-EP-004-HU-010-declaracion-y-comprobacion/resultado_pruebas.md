# Resultado de Pruebas — Fase A-EP-004-HU-010-declaracion-y-comprobacion

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el [estado-fase.md](estado-fase.md) para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del documento de cierre. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md) de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-004-HU-010-declaracion-y-comprobacion` |
| **HU** | [HU-010](../HU-010-convencion-declarada-por-el-proyecto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | No ejecutado |
| **Ejecutado por** | No ejecutado |
| **Ambiente y versión** | No ejecutado |

---

## 1. Resumen de la corrida

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 12 | 0 | 0 | 0 | 0 | 12 |

**Casos no ejecutados y por qué:** los doce. La fase no ha empezado: el plan de trabajo y este plan de pruebas están sin aprobar.

---

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Fecha | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | — | No ejecutado | — | — |
| CP-002 | CA-01 | Crítica | — | No ejecutado | — | — |
| CP-003 | CA-02 | Alta | — | No ejecutado | — | — |
| CP-004 | CA-02 | Alta | — | No ejecutado | — | — |
| CP-005 | CA-02 | Alta | — | No ejecutado | — | — |
| CP-006 | CA-03 | Alta | — | No ejecutado | — | — |
| CP-007 | CA-03 | Alta | — | No ejecutado | — | — |
| CP-008 | CA-04 | Alta | — | No ejecutado | — | — |
| CP-009 | CA-04 | Alta | — | No ejecutado | — | — |
| CP-010 | CA-05 | Alta | — | No ejecutado | — | — |
| CP-011 | RNF-01 | Crítica | — | No ejecutado | — | — |
| CP-012 | RNF-01 | Crítica | — | No ejecutado | — | — |

**Correspondencia con el plan:** 12 casos en el plan, 12 acá. Ninguno de más, ninguno de menos.

**Qué salió distinto de lo esperado:** nada todavía: no se ejecutó.

---

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el mensaje del hallazgo se lea bien en una consola de Windows, con tildes | A mano, corriendo un subcomando | No ejecutado |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| — | Ninguno todavía | — | — | — | — |

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación

| CA de la HU | Casos que lo cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002 | No ejecutado | Todavía no se ejecutó |
| CA-02 | CP-003, CP-004, CP-005 | No ejecutado | Todavía no se ejecutó |
| CA-03 | CP-006, CP-007 | No ejecutado | Todavía no se ejecutó |
| CA-04 | CP-008, CP-009 | No ejecutado | Todavía no se ejecutó |
| CA-05 | CP-010 | No ejecutado | Todavía no se ejecutó |
| RNF-01 | CP-011, CP-012 | No ejecutado | Todavía no se ejecutó |

**Los que no cumplen:** ninguno declarado: no se ha ejecutado nada.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios de aceptación | Plan §5 | 100% | No ejecutado | Todavía no se ejecutó |
| Casos críticos y altos ejecutados | Plan §3.4 | 100% | No ejecutado | Todavía no se ejecutó |
| Tasa de aprobación | Plan §12.1 | 100% | No ejecutado | Todavía no se ejecutó |
| Falsos positivos | Plan §12.1 | 0 | No ejecutado | Todavía no se ejecutó |

**Lo que no se cumplió:** nada declarado todavía.

---

## 6. Veredicto de la fase

**Concepto:** todavía no se ejecutó.

**Justificación:** la fase está en la puerta de aprobación de sus dos planes. No se ha escrito código bajo este plan ni se ha corrido ninguna prueba.

**Qué falta para que cumpla:** aprobar el plan de trabajo y este plan, ejecutar las tareas y correr los doce casos.

---

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| — | Ninguna todavía | — |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | No ejecutado | 0 | 0 | Primera corrida, sin ejecutar |
