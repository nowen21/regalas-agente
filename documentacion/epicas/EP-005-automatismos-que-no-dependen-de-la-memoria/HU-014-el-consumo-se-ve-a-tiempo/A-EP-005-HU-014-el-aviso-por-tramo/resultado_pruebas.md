# Resultado de Pruebas — Fase «A-EP-005-HU-014-el-aviso-por-tramo»   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**. El diseño de los casos vive en el [plan_pruebas.md](plan_pruebas.md), que no se modifica al ejecutar.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-014-el-aviso-por-tramo` |
| **HU** | [HU-014](../HU-014-el-consumo-se-ve-a-tiempo.md) |
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

Los ocho casos están automatizados en [validadores/tests/test_el_consumo_se_ve_a_tiempo.py](../../../../../validadores/tests/test_el_consumo_se_ve_a_tiempo.py); cada uno repite los pasos de su caso del plan con transcripciones de sumas conocidas. Se corren con `python -m unittest validadores.tests.test_el_consumo_se_ve_a_tiempo`.

| Caso | Qué decide | Qué salió |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-reporte-de-cierre-no-cambia) | Dos turnos (100+20 con 5 de caché, 50+30), sin `--modo` y con `--modo cierre` | `Consumo de la sesión: 2 turno(s) · 150 fichas de entrada · 50 de salida · 5 leídas de caché`, las dos veces |
| [CP-002](plan_pruebas.md#cp-002--el-último-turno-cruza-el-millón) | 500.000 + 450.000 + 100.000 | `[LA SESIÓN CRUZÓ EL TRAMO 1 DE CONSUMO]` con `1,050,000` |
| [CP-003](plan_pruebas.md#cp-003--un-turno-más-dentro-del-mismo-tramo) | Más un turno de 10.000 | Sin salida, código 0 |
| [CP-004](plan_pruebas.md#cp-004--el-segundo-millón) | Más un turno de 990.000 (2.050.000) | Aviso del `TRAMO 2` |
| [CP-005](plan_pruebas.md#cp-005--sin-ruta-ruta-inexistente-y-línea-ilegible) | Sin `transcript_path`; ruta inexistente; una línea válida de 1.000.000 y una ilegible | Silencio con 0; silencio con 0; aviso del tramo 1 con 0 |
| [CP-006](plan_pruebas.md#cp-006--exactamente-el-tramo-y-el-umbral-apagado) | 999.999 y 1.000.000; umbral 0 sobre 5.000.000; lista vacía | Falso, verdadero con tramo 1; falso; falso |
| [CP-007](plan_pruebas.md#cp-007--la-transcripción-más-grande-se-lee-rápido) | La transcripción real más grande de la máquina (3.407 turnos) | Menos de 2 segundos, código 0 |
| [CP-008](plan_pruebas.md#cp-008--nada-de-lo-que-ya-estaba-deja-de-pasar) | Las dos suites enteras | Ver abajo |

**Un detalle que se corrigió en la propia prueba:** la primera redacción de los casos buscaba `tramo 1` en minúsculas y el aviso lo escribe en mayúsculas. Se corrigió la aserción, no el aviso.

**CP-008, la no regresión, con las otras dos fases del día corridas juntas:**

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **454 casos**. Una falla previa y ajena (un resumen del 2026-08-19 escrito sin la `H-` del molde), anotada como hallazgo de la sesión |
| `validadores/pruebas.py` | **365 · OK**, con `TestPresupuesto` sin cambios (5 fallos esperados, los de siempre) |
| `python evals/correr.py` | 9 de 9 |
| `validar.py estandar` | Sin incumplimientos |

## 3. Verificaciones manuales

- El instalador corrido sobre los 9 proyectos: `9 de 9 proyecto(s) procesados`.
- `C:/wamp64/www/proyectos/personales/agro-system/.claude/settings.json` leído después: trae `hook_presupuesto.py` dos veces, la de `Stop` sin argumentos y la de `UserPromptSubmit` con `--modo aviso`.

## 4. Defectos encontrados

| ID | Qué | Severidad | Estado |
|---|---|---|---|
| DEF-01 | La aserción de los casos CP-002, CP-004 y CP-005 buscaba el texto en minúsculas | Baja | Corregido en la prueba |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| CA / RNF | Casos | Veredicto |
|---|---|---|
| [CA-01](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-01--al-terminar-se-reporta-el-consumo-de-la-sesión) | CP-001 | **Sí** |
| [CA-02](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-02--al-cruzar-un-tramo-se-avisa-una-vez) | CP-002, CP-003, CP-004 | **Sí** |
| [CA-03](../HU-014-el-consumo-se-ve-a-tiempo.md#ca-03--sin-transcripción-calla-y-nunca-detiene) | CP-005 | **Sí** |
| Límites | CP-006 | **Sí** |
| RNF-01 · silencio entre tramos | CP-003 | **Sí** |
| RNF-02 · no se nota | CP-007 | **Sí** |
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
| EV-01 | La suite de la fase | `validadores/tests/test_el_consumo_se_ve_a_tiempo.py` |
| EV-02 | Salida del instalador, el `settings.json` de AgroSystem y el tiempo de CP-007 | §2 y §3 |
| EV-03 | Diff de la especificación y el mapa del sitio | [funcionalidad_implementada.md](funcionalidad_implementada.md) §7 |

## 8. Ciclos anteriores

Ninguno.
