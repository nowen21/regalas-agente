# Resultado de Pruebas — Fase A-EP-007-HU-008: la regla y el aviso de vuelta

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-A-EP-007-HU-008](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--las-dos-plantillas-se-nombran-entre-sí) | ✅ **Pasa** | Cada una enlaza a la otra; la del proyecto dice que no se cierra al reportar |
| [CP-002](plan_pruebas.md#cp-002--el-proyecto-de-origen-se-comprueba) | ✅ **Pasa** | Los cuatro casos, incluido el que **no** se reporta |
| [CP-003](plan_pruebas.md#cp-003--el-aviso-llega-solo-a-quien-le-toca) | ✅ **Pasa** | Uno recibe; los otros dos con la carpeta vacía |
| [CP-004](plan_pruebas.md#cp-004--el-arreglo-que-rige-para-todos-avisa-a-todos) | ✅ **Pasa** | Los tres |
| [CP-005](plan_pruebas.md#cp-005--cerrar-dos-veces-no-duplica-el-aviso) | ✅ **Pasa** | Un solo archivo tras dos cierres |
| [CP-006](plan_pruebas.md#cp-006--lo-que-no-se-puede-hacer-se-dice-no-se-rompe) | ✅ **Pasa** | Los tres casos se dicen, ninguno falla |
| [CP-007](plan_pruebas.md#cp-007--no-escribe-nada-fuera-de-la-carpeta-de-pendientes) | ✅ **Pasa** | La raíz del proyecto queda idéntica |
| [CP-008](plan_pruebas.md#cp-008--cerrar-un-pendiente-sigue-funcionando) | ✅ **Pasa** | Ver §2 |

**8 de 8 ejecutados. 8 pasan.** 12 casos automatizados en [validadores/tests/test_aviso_de_vuelta.py](../../../../../validadores/tests/test_aviso_de_vuelta.py).

---

## 2. CP-008 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **121 · OK** — eran 109 |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |
| `validar.py estandar` | **Sin incumplimientos** |
| `validar.py pendientes` | **Sin incumplimientos** — los 34 pendientes pasan la comprobación nueva |
| `validar.py metareglas` | `F24` no aparece en ningún hallazgo |

**Los 34 pendientes del backlog pasan la comprobación del proyecto de origen sin tocar ninguno.** Es la señal de que la regla describe lo que ya se venía haciendo bien, en vez de inventar una exigencia nueva.

---

## 3. Lo que apareció y no se arregló  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**Tres cierres anteriores quedaron sin su aviso, y no se mandan hacia atrás.**

| Cerrado | Quién lo espera |
|---|---|
| [pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md](../../../../../pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md) | `shopnest-mesa` |
| [pendientes/hecho/renombrar-deja-el-resumen-coherente.md](../../../../../pendientes/hecho/renombrar-deja-el-resumen-coherente.md) | `shopnest-mesa` |
| [pendientes/46-el-registro-de-version-dice-que-falta-escribirse.md](../../../../../pendientes/46-el-registro-de-version-dice-que-falta-escribirse.md) | `dp` |

**Mandarlos ahora sería inventar un aviso con fecha de hoy sobre correcciones de hace dos días.** Se anota cuáles son y quién los espera; el aviso lo manda quien decida decírselo.

**Es la prueba de que el paso 6 hecho a mano se olvida**, que era el argumento del pendiente 36 desde el principio.

---

## 4. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | 4 de 4, más las dos transversales |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | uno: los tres avisos atrasados, fuera del alcance declarado en el plan §1 |
| **Ciclos** | 1 |
