# Resultado de Pruebas — Fase «C-EP-005-HU-003-el-veredicto-se-copia-solo»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-003-el-veredicto-se-copia-solo` |
| **HU** | [HU-003](../HU-003-disparo-al-escribir-un-archivo.md) |
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

Los casos están automatizados en `validadores/tests/test_el_veredicto_se_copia_solo.py` y repiten los pasos de su caso del plan.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--cumple-llega-a-los-tres-sitios-con-seis-columnas) | Historia con §8 de seis columnas; resultado «Cumple, 2 de 2»; el enganche | Imprime los tres archivos; la fila dice `Cerrada el 2026-08-20: Cumple, 2 de 2 CA` y conserva las otras celdas; los dos README, lo mismo |
| [CP-002](plan_pruebas.md#cp-002--no-cumple-llega-igual-con-tres-columnas) | Tres columnas; «No cumple, 1 de 2» | `Ejecutada el 2026-08-20: No cumple, 1 de 2 CA`, sin avisos |
| [CP-003](plan_pruebas.md#cp-003--sin-concepto-no-se-toca-nada) | «Todavía no se ejecutó» | Sin salida; las tres huellas iguales |
| [CP-004](plan_pruebas.md#cp-004--el-estado-fase-no-cambia) | Huella de `estado-fase.md` | La misma |
| [CP-005](plan_pruebas.md#cp-005--cerrar-deja-la-fila-en-forma-de-hecho) | `cerrar.cerrar(tmp, 99, "p")` | `\| ~~99~~ \| — \| **hecho** → [t](hecho/p.md) \| q \|` |
| [CP-006](plan_pruebas.md#cp-006--lo-que-no-le-toca-y-lo-que-no-encuentra) | `plan_trabajo.md`; historia sin fila | Silencio con 0; «NO TIENE DÓNDE COPIARSE» con 0 |
| [CP-007](plan_pruebas.md#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | Las dos suites | Ver abajo |

**La no regresión, con las cuatro fases de la tarde corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **473 casos · OK**. Las dos fallas previas que el pendiente 68 describía quedaron cerradas en su fase |
| `validadores/pruebas.py` | **365 · OK** (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |

**Se estrenó sobre el repositorio real:** el cierre de las cuatro fases de la tarde lo propagó `veredicto.py` a las filas de sus historias y a sus README, y `cerrar.py` dejó las filas de los pendientes 67 a 70 en forma de hecho. Ninguna de esas doce copias se escribió a mano.

## 3. Verificaciones manuales

Ninguna hizo falta: todo lo que la fase afirma lo mide un caso.

## 4. Defectos encontrados

Ninguno en lo construido que haya quedado abierto. Los que aparecieron al escribir los casos se corrigieron antes de cerrar y están en el [funcionalidad_implementada.md](funcionalidad_implementada.md) §5.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / exigencia | Casos | Veredicto |
|---|---|---|
| [CA-04](../HU-003-disparo-al-escribir-un-archivo.md#ca-04--lo-que-se-deriva-del-veredicto-lo-copia-el-programa) · los tres sitios | CP-001, CP-002 | **Sí** |
| CA-04 · el borrador calla | CP-003 | **Sí** |
| CA-04 · el checkpoint intacto | CP-004 | **Sí** |
| CA-04 · la fila «hecho» | CP-005 | **Sí** |
| Límites | CP-006 | **Sí** |
| No regresión | CP-007 | **Sí** |

## 5.1 Lo que el plan exigía

6 de 6 exigencias con caso, todas en Sí.

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
| EV-01 | La suite de la fase | `validadores/tests/test_el_veredicto_se_copia_solo.py` |

## 8. Ciclos anteriores

Ninguno.
