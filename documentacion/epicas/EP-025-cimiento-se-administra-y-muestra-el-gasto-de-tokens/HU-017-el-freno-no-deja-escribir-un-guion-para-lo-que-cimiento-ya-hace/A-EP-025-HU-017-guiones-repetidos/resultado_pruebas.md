# Resultado de Pruebas · Fase `A-EP-025-HU-017-guiones-repetidos`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-017-guiones-repetidos` |
| **HU** | [HU-017](../HU-017-el-freno-no-deja-escribir-un-guion-para-lo-que-cimiento-ya-hace.md) |
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
| CP-001 | CA-01 | Alta | `LosGuionesRepetidos` (2) y el enganche en vivo | Seis guiones, uno por cada tarea que Cimiento hace, se detienen nombrando su orden y con `04·S18` como regla; fuera de la carpeta de guiones, o si no es `.py`, no se mira | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Media | `LosGuionesRepetidos` (5) | El mismo nombre con otro número avisa y nombra el anterior; casi el mismo texto con otro nombre avisa; uno distinto pasa; el mismo archivo no se compara consigo; el aviso dice que no se detiene | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** la regla del motivo tiene que ir sola entre paréntesis para que el freno aplique su nivel; se ajustó la redacción.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && python -c "import core.validadores, unittest, sys; r=unittest.TextTestRunner(verbosity=0).run(unittest.defaultTestLoader.loadTestsFromNames(['core.enganches.tests_guiones','core.enganches.tests_freno'])); sys.exit(not r.wasSuccessful())"` | Ran 329 tests in 45.842s, OK |
| 2 | En vivo | `hook_antes.py` con un guion `cerrar_hu_011.py` que llena `estado-fase.md` | Lo detiene y nombra `manage.py cerrar_fase` |

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

**Justificación:** los dos criterios pasan, `tests_freno` sigue en verde, y en vivo el freno detiene un guion de cierre nombrando `cerrar_fase`.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/enganches/tests_guiones.py` (7) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 2 | 0 | Primera ejecución |
