# Resultado de Pruebas — Fase «C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-004-HU-008-la-corrida-entera-vuelve-a-verde` |
| **HU** | [HU-008](../HU-008-corrida-completa.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el usuario leyendo |
| **Ambiente y versión** | Esta máquina, repositorio en 27.2.0, Python 3.11 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 3 | 3 | 3 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

Los casos están automatizados en `validadores/tests/test_los_indices_nacen_legibles.py` y repiten los pasos de su caso del plan.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-enlace-al-resumen-dice-dónde-vive) | `_enlace_al_resumen` sobre una carpeta temporal | ` · [historico-chat/resumenes/2026-01-01/tema.md](resumenes/2026-01-01/tema.md)` |
| [CP-002](plan_pruebas.md#cp-002--la-línea-del-día-dice-dónde-vive) | `_indexar_dias` y `enlaces._texto_esperado` sobre la línea | `- [historico-chat/resumenes/2026-01-01/](2026-01-01/) — sin escribir todavía.`; el validador no le pide otro texto |
| [CP-003](plan_pruebas.md#cp-003--la-corrida-entera-termina-en-ok) | Las dos suites enteras | `OK` las dos, ver abajo |

**La no regresión, con las cuatro fases de la tarde corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **473 casos · OK**. Las dos fallas previas que el pendiente 68 describía quedaron cerradas en su fase |
| `validadores/pruebas.py` | **365 · OK** (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |

**Lo que se corrigió a mano, una sola vez:** el hallazgo `### 1 ·` de `historico-chat/resumenes/2026-08-19/sesion-3.md` pasó a `### H-1 ·`, y los cuatro enlaces ya escritos (`evals/README.md`, `historico-chat/README.md` y los dos de `historico-chat/resumenes/README.md`) llevan ahora la ruta desde la raíz. Los que vengan los escriben bien los enganches.

## 3. Verificaciones manuales

Ninguna hizo falta: todo lo que la fase afirma lo mide un caso.

## 4. Defectos encontrados

Ninguno en lo construido que haya quedado abierto. Los que aparecieron al escribir los casos se corrigieron antes de cerrar y están en el [funcionalidad_implementada.md](funcionalidad_implementada.md) §5.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / exigencia | Casos | Veredicto |
|---|---|---|
| [CA-04](../HU-008-corrida-completa.md#ca-04--lo-que-los-programas-del-estándar-escriben-no-pone-la-corrida-en-rojo) | CP-001, CP-002, CP-003 | **Sí** |

## 5.1 Lo que el plan exigía

1 de 1 exigencias con caso, todas en Sí.

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 (CA-04) |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 |

## 7. Evidencias

| ID | Qué | Dónde |
|---|---|---|
| EV-01 | La suite de la fase | `validadores/tests/test_los_indices_nacen_legibles.py` |

## 8. Ciclos anteriores

Ninguno.
