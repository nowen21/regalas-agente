# Resultado de Pruebas · Fase `A-EP-025-HU-021-desinstalar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-021-desinstalar` |
| **HU** | [HU-021](../HU-021-el-estandar-se-puede-desinstalar-de-un-proyecto.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `ElEstandarSePuedeDesinstalar` (6), en un repositorio git temporal | Sin `.githooks/` propios ni `core.hooksPath`, y con un enganche ajeno el `hooksPath` se queda; en `settings.json` solo el ajeno; sin la copia del stack, la plantilla sellada, la CI de Cimiento ni las carpetas vacías, y la CI ajena sigue; fuera del registro, la otra fila sigue; la telemetría sale y lo demás del usuario se queda; la baja y su contraria | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElEstandarSePuedeDesinstalar` (1) | `CLAUDE.md`, `.agente/stack.md`, `historico-chat/README.md` y `documentacion/x.md` iguales | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-03 | Media | `ElEstandarSePuedeDesinstalar` (3) | Sin aplicar, todo igual archivo por archivo; la segunda vez no hay nada; reinstalar vuelve a poner los enganches | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 3 casos en el plan, 3 acá.

**Qué salió distinto de lo esperado:** `manage.py registrar` con una carpeta ya registrada no la reactivaba; ahora sí, como contraria de `--baja`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && python -m unittest core.herramientas.tests_desinstalar` | Ran 10 tests in 9.975s, OK |
| 2 | Sobre un proyecto real | `python validadores/instalar.py C:/DesarrollosClaude/personales/scilit --desinstalar`, sin aplicar | Nombra 4 enganches de git, `core.hooksPath`, 24 entradas de Claude Code, la copia del stack, la plantilla sellada y la fila del registro |
| 3 | Que la instalación siga | `core.herramientas.tests_instalacion` | 227 pruebas pasan |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 3 de 3 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 3 de 3 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los tres criterios pasan; `tests_instalacion` (227) sigue en verde, y la simulación sobre scilit nombra lo que quitaría sin tocarlo.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/herramientas/tests_desinstalar.py` (10 pruebas) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 3 | 0 | Primera ejecución |
