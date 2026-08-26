# Resultado de Pruebas — Fase «B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-007-HU-003-el-andamio-levanta-la-historia-y-el-pendiente` |
| **HU** | [HU-003](../HU-003-estructura-de-carpetas.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el usuario leyendo |
| **Ambiente y versión** | Esta máquina, repositorio en 27.2.0, Python 3.11 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

Los casos están automatizados en `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` y repiten los pasos de su caso del plan.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--la-historia-nace-con-sus-índices) | `crear_hu` sobre una copia de EP-005 | `HU-015-prueba-del-andamio/` con su documento y su README; fila en el §9 con tantas celdas como la cabecera real (cuatro); fila en el README de la épica |
| [CP-002](plan_pruebas.md#cp-002--el-número-se-lee-lo-que-hay) | Épica con `HU-001-a` y `HU-003-c` | `HU-004`: el siguiente al mayor |
| [CP-003](plan_pruebas.md#cp-003--el-pendiente-nace-con-su-fila-y-su-historia-en-el-mapa) | `crear_pendiente` enrutado a HU-008 sobre una copia del índice | `02-prueba.md` con la historia enlazada; fila en «Sin agrupar todavía»; el mapa dice `32, 2`; el próximo libre es el 3 |
| — | Una historia que no estaba en el mapa | Nace su fila con el número |
| [CP-004](plan_pruebas.md#cp-004--no-escribe-contenido) | Contar `«` en la historia creada contra la plantilla | Iguales, menos `«Épica padre»` y el marcador de la ruta |
| [CP-005](plan_pruebas.md#cp-005--los-validadores-no-reclaman-nada) | `enlaces.validar_enlaces` sobre la copia | Nada sobre la historia nueva |
| [CP-006](plan_pruebas.md#cp-006--el-modo-de-fase-sigue-igual) | `andamio.py EP HU descripcion` sin `--aplicar` | La salida de siempre, «simulado» |

**La no regresión, con las cuatro fases de la tarde corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **473 casos · OK**. Las dos fallas previas que el pendiente 68 describía quedaron cerradas en su fase |
| `validadores/pruebas.py` | **365 · OK** (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |

**Dos cosas que los casos corrigieron antes de cerrar:** el número de la historia se tomaba del primer hueco y el plan pedía el siguiente al mayor (la historia se cita por número, como el pendiente); y el enlace a `../epica.md` se ponía antes de trasladar los de la plantilla, y se trasladaba también. Las dos están en el cierre §5.

## 3. Verificaciones manuales

Ninguna hizo falta: todo lo que la fase afirma lo mide un caso.

## 4. Defectos encontrados

Ninguno en lo construido que haya quedado abierto. Los que aparecieron al escribir los casos se corrigieron antes de cerrar y están en el [funcionalidad_implementada.md](funcionalidad_implementada.md) §5.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / exigencia | Casos | Veredicto |
|---|---|---|
| [CA-04](../HU-003-estructura-de-carpetas.md#ca-04--la-historia-y-el-pendiente-nacen-con-su-esqueleto-y-sus-índices-puestos) · la historia | CP-001, CP-002 | **Sí** |
| CA-04 · el pendiente | CP-003 | **Sí** |
| CA-04 · sin contenido | CP-004 | **Sí** |
| CA-04 · los validadores callan | CP-005 | **Sí** |
| No regresión | CP-006 | **Sí** |

## 5.1 Lo que el plan exigía

5 de 5 exigencias con caso, todas en Sí.

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
| EV-01 | La suite de la fase | `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` |

## 8. Ciclos anteriores

Ninguno.
