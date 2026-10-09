# Resultado de Pruebas · Fase `A-EP-025-HU-031-formatos-de-las-plantillas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-031-formatos-de-las-plantillas` |
| **HU** | [HU-031](../HU-031-cerrar-fase-entiende-los-formatos-de-las-plantillas-y-marca-todo-lo-que-cierra.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Python 3.11.9 de `proyectos/cimiento/.venv/`, Windows 11, carpetas temporales; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | `test_lee_todos_los_casos_y_los_ca_sin_nombre` | Toma CP-001 a CP-004, con la fila de RNF-01; los CA sin nombre y como enlace salen con «Uno» y «Dos», de la HU; leída sin escribir, la fase del pendiente 148 da sus 6 casos y sus 3 CA | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Crítica | `test_al_cerrar_marca_todo` | No queda ☐ en la matriz ni en los CA; la sección 5 lleva la fecha y ☑; la Definition of Done del plan queda marcada menos el commit; las tareas y la Definition of Done de la HU, marcadas | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-02 | Alta | `test_al_reabrir_desmarca_lo_mismo`, `test_con_la_hu_en_curso_no_desmarca_lo_marcado_a_mano` | Todo vuelve a ☐ y sin fecha; con otra fase en curso, lo marcado a mano en la HU se queda | Aprobado | EV-01 | Ninguno |
| CP-004 | RNF-01 | Alta | Las 9 pruebas que ya había, con el formato viejo | Pasan sin cambios | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `python -m unittest core.herramientas.tests_fase` | Ran 13 tests in 0.799s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002, CP-003 | Aprobado | Sí |
| RNF-01 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los 4 casos pasan (13 pruebas), y el formato viejo cierra igual.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/fase.py`, `core/herramientas/tests_fase.py`; la salida de `python -m unittest core.herramientas.tests_fase` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 4 | 0 | Primera ejecución |
