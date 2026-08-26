# Resultado de Pruebas — Fase «B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-005-HU-009-las-reglas-llegan-tambien-al-propio-estandar` |
| **HU** | [HU-009](../HU-009-lo-que-rige-cada-frase-llega-puesto.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el usuario leyendo |
| **Ambiente y versión** | Esta máquina, repositorio en 27.1.0, Python 3.11 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 6 | 6 | 0 | 0 | 1 |

**Casos no ejecutados y por qué:** CP-006, la apertura real de la siguiente sesión, no se puede ejecutar desde adentro de esta. Se anota abajo con la fecha cuando ocurra. Lo que sí se ejecutó (CP-001) corre el enganche real sobre la carpeta real, que es lo mismo que hace la herramienta al abrir.

## 2. Ejecución caso por caso

Los casos CP-001 a CP-004 están en [validadores/tests/test_las_reglas_llegan_al_propio_estandar.py](../../../../../validadores/tests/test_las_reglas_llegan_al_propio_estandar.py) (7 pruebas); CP-005 es `python evals/correr.py`.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-estándar-recibe-el-bloque-de-reglas-y-el-núcleo) | `hook_sesion.py --raiz <RAIZ>`: código, JSON, el bloque, el núcleo, sin gate | Código 0, JSON válido; trae `[REGLAS BASE DEL ESTÁNDAR — CARGADAS, OBLIGATORIAS]`, `<<< base/00-nucleo-blindado.md >>>` y `## N1 ·`; no trae `[ARRANQUE DETENIDO` |
| [CP-002](plan_pruebas.md#cp-002--la-memoria-y-el-histórico-siguen-llegando) | En la misma salida | Trae `[MEMORIA DEL AGENTE` y `[HISTÓRICO DE SESIONES` |
| [CP-003](plan_pruebas.md#cp-003--un-heredero-recibe-lo-mismo-que-antes) | Carpeta temporal con `proyectos/`; y otra sin | Con: bloque de reglas y `[Revisión de arranque del estándar]`. Sin: solo el gate, sin bloque |
| [CP-004](plan_pruebas.md#cp-004--el-tiempo-del-arranque) | El enganche sobre `RAIZ`, medido | Menos de 3 segundos |
| [CP-005](plan_pruebas.md#cp-005--el-caso-de-evals) | `python evals/correr.py` | `arranque-reglas-en-el-estandar` en verde; 9 de 9 |
| [CP-006](plan_pruebas.md#cp-006--la-siguiente-sesión-lo-trae) | La apertura real | **No ejecutado en esta sesión.** Se confirma al abrir la siguiente, leyendo el archivo de apertura que la herramienta conserva, y se anota acá con la fecha |
| [CP-007](plan_pruebas.md#cp-007--nada-de-lo-que-ya-estaba-deja-de-pasar) | Las dos suites enteras | Ver abajo |

**CP-007, la no regresión, con las otras dos fases del día corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **454 casos**. Una falla previa y ajena (un resumen del 2026-08-19 sin la `H-` del molde), anotada como hallazgo de la sesión |
| `validadores/pruebas.py` | **365 · OK** (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |

## 3. Verificaciones manuales

- **CP-006, pendiente de la próxima apertura.** Cuando se abra la siguiente sesión en este repositorio, se lee el archivo `hook-*-additionalContext.txt` de esa apertura y se anota acá: fecha, y si trae el bloque de reglas. Hasta hoy, 0 de 30 aperturas lo traían.

## 4. Defectos encontrados

Ninguno en lo construido. El defecto que la fase corrige está descrito en el [pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md](../../../../../pendientes/hecho/las-reglas-llegan-tambien-al-propio-estandar.md).

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / RNF | Casos | Veredicto |
|---|---|---|
| [CA-01](../HU-009-lo-que-rige-cada-frase-llega-puesto.md#ca-01--los-capítulos-que-rigen-cada-frase-llegan-con-su-texto), en el estándar | CP-001, CP-005, CP-006 | **Sí** por CP-001 y CP-005; CP-006 se confirma en la próxima apertura |
| La memoria y el histórico siguen llegando | CP-002 | **Sí** |
| Los herederos no cambian | CP-003 | **Sí** |
| RNF-03 de la HU · el arranque no se vuelve lento | CP-004 | **Sí** |
| La promesa queda en el banco | CP-005 | **Sí** |
| No regresión | CP-007 | **Sí**, con la falla previa y ajena anotada |

## 5.1 Lo que el plan exigía

7 de 7 exigencias con caso; 6 ejecutadas en Sí y 1 (CP-006) que por su naturaleza se ejecuta en la sesión siguiente.

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 1 de 1 |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | ninguno. CP-006 no es defecto: es la confirmación desde afuera, anotada para la próxima apertura |
| **Ciclos** | 1 |

## 7. Evidencias

| ID | Qué | Dónde |
|---|---|---|
| EV-01 | La suite de la fase | `validadores/tests/test_las_reglas_llegan_al_propio_estandar.py` |
| EV-02 | El banco de evals | `python evals/correr.py` |
| EV-03 | Diff de la especificación | [funcionalidad_implementada.md](funcionalidad_implementada.md) §7 |
| EV-04 | La apertura de la siguiente sesión | §3, cuando ocurra |

## 8. Ciclos anteriores

Ninguno.
