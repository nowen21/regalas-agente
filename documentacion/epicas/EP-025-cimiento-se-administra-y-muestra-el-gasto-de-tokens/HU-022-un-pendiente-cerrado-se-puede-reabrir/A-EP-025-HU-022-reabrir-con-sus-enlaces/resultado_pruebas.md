# Resultado de Pruebas · Fase `A-EP-025-HU-022-reabrir-con-sus-enlaces`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-022-reabrir-con-sus-enlaces` |
| **HU** | [HU-022](../HU-022-un-pendiente-cerrado-se-puede-reabrir.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `UnPendienteCerradoSePuedeReabrir` (2) | Cerrado y reabierto, el archivo vuelve como `07-algo-resuelto.md`; la cita de otro documento y la del archivo hacia afuera quedan bien, sin enlaces rotos; la fila vuelve a abierta; la marca dice el motivo; «Estado: hecho» pasa a «reabierto» | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Media | `UnPendienteCerradoSePuedeReabrir` (3) | Un número abierto y la falta de motivo se rechazan; sin aplicar dice qué haría y no cambia ni el archivo ni el índice | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && python -m unittest core.herramientas.tests_reabrir` | Ran 5 tests in 0.427s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 2 de 2 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 2 de 2 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los dos criterios pasan; `CerrarArrastraLasCitas` (14) sigue en verde, y la simulación sobre el índice real del 04 encontró su fila y sus citas.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_reabrir.py` (5 pruebas) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 2 | 0 | Primera ejecución |
