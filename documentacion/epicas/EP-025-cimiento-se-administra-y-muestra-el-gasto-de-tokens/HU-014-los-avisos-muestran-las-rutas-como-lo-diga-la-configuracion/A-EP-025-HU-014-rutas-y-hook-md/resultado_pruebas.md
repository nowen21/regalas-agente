# Resultado de Pruebas · Fase `A-EP-025-HU-014-rutas-y-hook-md`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-014-rutas-y-hook-md` |
| **HU** | [HU-014](../HU-014-los-avisos-muestran-las-rutas-como-lo-diga-la-configuracion.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-05 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Máquina local, rama `main`, sobre el commit `2c3b67b` más los cambios sin guardar; base de pruebas en MariaDB 11.4.9; versión 55.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

| Caso | CA | Prioridad (del plan) | Con qué se probó | Qué salió | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Alta | `LasRutasSegunElAjuste` (4) | Completas en un proyecto registrado; relativas si el proyecto lo dice aunque la base diga completas; sin registro, relativas aunque la base diga completas; lo de afuera, completo | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-02 | Alta | `ElEngancheDeLosMd` (4) y el adaptador con una entrada de muestra | Enlace roto, código 2 nombrándolo; marca escrita, aviso con su línea; lo que no es `.md` o es de afuera no se revisa pero se anota; el adaptador no usa `validadores/` | Aprobado | EV-01 | Ninguno |

**Correspondencia con el plan:** 2 casos en el plan, 2 acá.

**Qué salió distinto de lo esperado:** la base se aplicaba a cualquier carpeta; ahora un proyecto sin registro usa el valor de fábrica, y `tests_limites.py` se ajustó a la consulta de tres resultados.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Las pruebas de la fase | `cd proyectos\cimiento && python -m unittest core.enganches.tests_md core.enganches.tests_limites && .venv\Scripts\python.exe manage.py test core.proyectos` | Ran 54 tests in 48.033s, OK |
| 2 | Lo que usa `mostrar` | `tests_freno`, `tests_andamio`, `tests_fase`, `tests_reabrir`, `tests_desinstalar` y `tests_analisis_en_curso` | 364 pruebas pasan |
| 3 | El enganche en vivo | `hook_md.py` con una entrada de muestra | Mismo aviso de marcas que antes, código 0 |

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

**Justificación:** los dos criterios pasan, y el freno, las herramientas y el análisis en curso (364) siguen en verde con `mostrar` leyendo el ajuste.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Programa y pruebas | `proyectos/cimiento/core/proyectos/tests_rutas.py` (4) y `proyectos/cimiento/core/enganches/tests_md.py` (4) |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-05 | 2 | 0 | Primera ejecución |
