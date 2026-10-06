# Resultado de Pruebas · Fase `A-EP-025-HU-020-quitar-con-sus-filas`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-020-quitar-con-sus-filas` |
| **HU** | [HU-020](../HU-020-lo-que-crea-el-andamio-se-puede-quitar.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; versión 54.4.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LoQueCreaElAndamioSePuedeQuitar` (3) | La HU, la fase y el pendiente recién creados se borran; `epica.md` y el `README.md` de la épica quedan idénticos a antes de crear | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `LoQueCreaElAndamioSePuedeQuitar` (1) | La HU cambiada pasa a `_archivo/` con el cambio; sus enlaces que suben bajan un nivel; las dos filas apuntan ahí con «(archivada)»; la siguiente HU es la 2 y pedir la 1 se rechaza | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `LoQueCreaElAndamioSePuedeQuitar` (3) | La HU con fase y la carpeta ajena dan error y quedan; sin aplicar dice qué haría y no toca nada | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** nada.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que crear siga igual | `core.herramientas.tests_andamio` y `core.enganches.tests_freno` | 10 y 322 pruebas pasan |
| 2 | Sobre una HU real | `python validadores/andamio.py quitar` con la carpeta de la HU-024, sin `--aplicar` | La reconoce como plantilla y nombra la carpeta y `epica.md` |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| RNF-01 | CP-002 | Lo cambiado se archiva, no se borra | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan, crear sigue igual, y la simulación sobre una HU real hace lo esperado.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_andamio.py` (7 pruebas nuevas) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
