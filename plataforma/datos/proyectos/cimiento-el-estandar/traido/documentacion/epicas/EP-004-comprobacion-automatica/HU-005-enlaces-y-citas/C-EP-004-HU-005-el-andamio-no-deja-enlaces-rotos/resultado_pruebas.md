# Resultado de Pruebas — Fase «C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-005-el-andamio-no-deja-enlaces-rotos` |
| **HU** | [HU-005](../HU-005-enlaces-y-citas.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el usuario leyendo |
| **Ambiente y versión** | Esta máquina, repositorio en 27.2.0, Python 3.11 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

Los casos están automatizados en `validadores/tests/test_el_andamio_no_deja_enlaces_rotos.py` y repiten los pasos de su caso del plan.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-esqueleto-nuevo-no-trae-el-enlace-crudo) | Fase levantada sobre una copia de `plantillas/` y `base/` | Ninguno de los cinco trae `](../../base/` ni `«RUTA-ESTANDAR»`; el resultado y el estado traen `](../../../../../base/` |
| [CP-002](plan_pruebas.md#cp-002--el-validador-de-enlaces-lo-da-por-bueno) | `enlaces.validar_enlaces` sobre la copia | Ningún roto dentro de la fase |
| [CP-003](plan_pruebas.md#cp-003--un-enlace-que-no-llega-a-la-raíz-no-se-toca) | `](../otra/cosa.md)` y `](../../../x.md)` desde `plantillas/planes/` | Quedan iguales; `](../../base/x.md)` se traslada |
| [CP-004](plan_pruebas.md#cp-004--nada-de-lo-que-ya-estaba-deja-de-pasar) | Las dos suites | Ver abajo |

**La no regresión, con las cuatro fases de la tarde corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **473 casos · OK**. Las dos fallas previas que el pendiente 68 describía quedaron cerradas en su fase |
| `validadores/pruebas.py` | **365 · OK** (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |

## 3. Verificaciones manuales

Ninguna hizo falta: todo lo que la fase afirma lo mide un caso.

## 4. Defectos encontrados

Ninguno en lo construido que haya quedado abierto. Los que aparecieron al escribir los casos se corrigieron antes de cerrar y están en el [funcionalidad_implementada.md](funcionalidad_implementada.md) §5.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / exigencia | Casos | Veredicto |
|---|---|---|
| [CA-05](../HU-005-enlaces-y-citas.md#ca-05--lo-que-un-programa-del-estándar-escribe-no-nace-con-enlaces-rotos) | CP-001, CP-002 | **Sí** |
| Límites · lo que no llega a la raíz | CP-003 | **Sí** |
| No regresión | CP-004 | **Sí** |

## 5.1 Lo que el plan exigía

3 de 3 exigencias con caso, todas en Sí.

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 (CA-05) |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 |

## 7. Evidencias

| ID | Qué | Dónde |
|---|---|---|
| EV-01 | La suite de la fase | `validadores/tests/test_el_andamio_no_deja_enlaces_rotos.py` |

## 8. Ciclos anteriores

Ninguno.
