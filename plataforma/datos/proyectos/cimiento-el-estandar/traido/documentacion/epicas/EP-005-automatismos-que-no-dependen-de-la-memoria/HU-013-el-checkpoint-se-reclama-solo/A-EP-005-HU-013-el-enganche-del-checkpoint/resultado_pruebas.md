# Resultado de Pruebas — Fase «A-EP-005-HU-013-el-enganche-del-checkpoint»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-013-el-enganche-del-checkpoint` |
| **HU** | [HU-013](../HU-013-el-checkpoint-se-reclama-solo.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el usuario leyendo |
| **Ambiente y versión** | Esta máquina, repositorio en 27.1.0, Python 3.11 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

Los ocho casos están automatizados en [validadores/tests/test_el_checkpoint_se_reclama_solo.py](../../../../../validadores/tests/test_el_checkpoint_se_reclama_solo.py); cada uno repite literalmente los pasos de su caso del plan. Se corren con `python -m unittest validadores.tests.test_el_checkpoint_se_reclama_solo`.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--sin-checkpoint-se-avisa-y-se-nombra-la-fase) | Sin checkpoint, avisa con la fase y la ruta relativa (RNF-02) | Aviso `[LA FASE PASÓ UNA PUERTA SIN CHECKPOINT]` con `A-EP-001-HU-001-prueba` y `documentacion/epicas/EP-001-prueba`; código 0 |
| [CP-002](plan_pruebas.md#cp-002--el-checkpoint-atrasado-se-avisa-con-el-documento) | Checkpoint con fecha 1000, documento con 2000 | Aviso `[EL CHECKPOINT DE LA FASE QUEDÓ ATRÁS]` con `funcionalidad_implementada.md` |
| [CP-003](plan_pruebas.md#cp-003--al-día-calla) | Checkpoint con fecha 3000 | Sin salida, código 0 |
| [CP-004](plan_pruebas.md#cp-004--los-cuatro-silencios) | `estado-fase.md`, `plan_pruebas.md`, `README.md` y un `.md` fuera de fase | Sin salida en los cuatro |
| [CP-005](plan_pruebas.md#cp-005--la-huella-no-cambia) | Huella antes y después de un aviso | La misma |
| [CP-006](plan_pruebas.md#cp-006--la-entrada-rota-y-el-archivo-que-ya-no-está) | «esto no es JSON»; ruta de un archivo nunca escrito | Código 0 y sin salida, en los dos |
| [CP-007](plan_pruebas.md#cp-007--solo-mira-fechas) | Documento con bytes al azar y checkpoint atrasado | `rezago()` devuelve `atrasado`: no leyó el contenido |
| [CP-008](plan_pruebas.md#cp-008--nada-de-lo-que-ya-estaba-deja-de-pasar) | Las dos suites enteras | Ver abajo |

**CP-008, la no regresión, con las otras dos fases del día corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **454 casos** (eran 431 en la línea base del día; 23 nuevos entre las tres fases). Una falla **previa y ajena**: `historico-chat/resumenes/2026-08-19/sesion-3.md` tiene un hallazgo escrito como `### N ·` sin la `H-`, del día anterior. Queda como hallazgo de la sesión |
| `validadores/pruebas.py` | **365 · OK** (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |
| `validar.py flujo` y `validar.py fases` | Sin avisos sobre las fases de hoy |

**Lo que CP-008 destapó.** La prueba de la frontera del adaptador contaba «8 enganches» con el número escrito y estaba en rojo desde la 27.0.0, y además reclamaba los puentes `validadores/hook_*.py` de la 26.0.1 como si fueran enganches sueltos. Las dos cosas se corrigieron en la tarea T-03, que el plan ya declaraba (`B-02`).

## 3. Verificaciones manuales

- El instalador corrido sobre los 9 proyectos del registro: `9 de 9 proyecto(s) procesados`.
- `C:/wamp64/www/proyectos/personales/agro-system/.claude/settings.json` leído después: trae `hook_checkpoint.py` una vez, en `PostToolUse`.

## 4. Defectos encontrados

| ID | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | La prueba de la frontera contaba un número fijo y estaba en rojo desde antes de esta fase | Media | Corregido en T-03 |
| DEF-02 | La primera versión del módulo nombraba el enganche en su docstring y el mapa del amarre la contaba como amarrada | Baja | Corregido: el docstring dice «el enganche del adaptador» |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / RNF | Casos | Veredicto |
|---|---|---|
| [CA-01](../HU-013-el-checkpoint-se-reclama-solo.md#ca-01--una-puerta-pasa-sin-checkpoint-y-se-avisa) | CP-001 | **Sí** |
| [CA-02](../HU-013-el-checkpoint-se-reclama-solo.md#ca-02--el-checkpoint-existe-pero-quedó-atrás) | CP-002, CP-003 | **Sí** |
| [CA-03](../HU-013-el-checkpoint-se-reclama-solo.md#ca-03--lo-que-no-es-puerta-calla-y-el-enganche-no-toca-el-checkpoint) | CP-004, CP-005 | **Sí** |
| RNF-01 · no lee el contenido | CP-007 | **Sí** |
| RNF-02 · el aviso dice dónde | CP-001 | **Sí** |
| Límites | CP-006 | **Sí** |
| No regresión | CP-008 | **Sí**, con la falla previa y ajena anotada |

## 5.1 Lo que el plan exigía

7 de 7 exigencias con caso, las 7 en Sí.

## 6. Veredicto de la fase

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 3 de 3 |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 |

## 7. Evidencias

| ID | Qué | Dónde |
|---|---|---|
| EV-01 | La suite de la fase | `validadores/tests/test_el_checkpoint_se_reclama_solo.py` |
| EV-02 | Salida del instalador y el `settings.json` de AgroSystem | §3 |
| EV-03 | Diff de la especificación, el mapa del sitio y el mapa del amarre | [funcionalidad_implementada.md](funcionalidad_implementada.md) §7 |

## 8. Ciclos anteriores

Ninguno.
