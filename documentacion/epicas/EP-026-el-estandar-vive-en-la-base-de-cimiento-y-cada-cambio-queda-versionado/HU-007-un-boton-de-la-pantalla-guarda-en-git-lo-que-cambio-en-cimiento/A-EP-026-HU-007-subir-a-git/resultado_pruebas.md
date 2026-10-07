# Resultado de Pruebas · Fase `A-EP-026-HU-007-subir-a-git`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-026-HU-007-subir-a-git` |
| **HU** | [HU-007](../HU-007-un-boton-de-la-pantalla-guarda-en-git-lo-que-cambio-en-cimiento.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Cimiento en la máquina local con la base de pruebas de Django y un repositorio git temporal; versión 56.8.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | 2026-10-06 | `LoQueCambioCadaSesion`: dos sesiones con sus archivos y uno compartido | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Crítica | 2026-10-06 | `ElCommitDeUnaSesion`: el commit lleva solo `uno.txt`, la idea antes que lo hecho y sin `Co-Authored-By` | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Alta | 2026-10-06 | `SiFalla`: un `pre-commit` que rechaza; sin commit nuevo, nada preparado y «Sin subir» en la pantalla | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-04 | Crítica | 2026-10-06 | `ConsultaNoHaceCommits`: 403 y sin commit | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 4 casos en el plan, 4 acá.

**Qué salió distinto de lo esperado:** nada: los cuatro casos pasaron en la primera corrida

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `.venv\Scripts\python.exe manage.py test core.estandar.tests_git --noinput` | Ran 4 tests in 9.521s, OK |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 4 de 4 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 4 de 4 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios tienen su caso aprobado: 4 pruebas nuevas y 37 en la regresión de `core.estandar core.ayuda core.herramientas.tests_cambios`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `manage.py test core.estandar.tests_git`: 4 OK; regresión: 37 OK |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 4 | 0 | Primera ejecución |
