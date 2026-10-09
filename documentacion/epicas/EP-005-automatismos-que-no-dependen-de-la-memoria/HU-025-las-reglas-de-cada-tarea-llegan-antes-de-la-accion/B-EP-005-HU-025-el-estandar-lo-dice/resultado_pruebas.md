# Resultado de Pruebas · Fase `B-EP-005-HU-025-el-estandar-lo-dice`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-025-el-estandar-lo-dice` |
| **HU** | [HU-025](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-09 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | La base de Cimiento; versión 59.3.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-05 | Alta | `manage.py documento ver estandar base/tareas.md` | Trae «Con cada mensaje, solo `responder` y `recibir-pedido`» y «Cada regla llega una sola vez en la sesión» | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-05 | Alta | La tabla de versiones de la base | Al aprobar la propuesta 18 quedó la 59.2.0, MENOR, «Cómo se elige la tarea, sin adivinar» | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** el plan decía subir la versión con `registrar_version`; Cimiento la sube sola al aprobar la propuesta, así que no hizo falta.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | El texto y la versión en la base | `documento ver` y la tabla de versiones | Propuestas 18 y 19 aprobadas por el usuario el 2026-10-09; versiones 59.2.0 y 59.3.0 |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-05 | CP-001, CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% | 1 de 1 | Sí |
| Casos ejecutados | Plan §12 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** el estándar dice cuándo llegan las reglas, y la versión subió como MENOR.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Propuestas y versión | Propuesta 18 en Cimiento → Estándar → Propuestas; texto en `historico-chat/scripts/2026-10-09/tareas-despues.txt` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-09 | 2 | 0 | Primera ejecución |
