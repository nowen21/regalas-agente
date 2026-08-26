# Resultado de Pruebas — Fase C-EP-005-HU-008: vacío no es lo mismo que ilegible

| Campo | Valor |
|---|---|
| **Plan de pruebas** | [PP-C-EP-005-HU-008](plan_pruebas.md) v1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-18 |

---

## 1. Casos ejecutados

| Caso | Veredicto | Qué dio |
|---|---|---|
| [CP-001](plan_pruebas.md#cp-001--el-que-no-tiene-nada-sigue-diciendo-vacío) | ✅ **Pasa** | `["vacio"]` |
| [CP-002](plan_pruebas.md#cp-002--el-escrito-sin-la-h-no-se-cuenta-como-vacío) | ✅ **Pasa** | `["molde"]` |
| [CP-003](plan_pruebas.md#cp-003--dice-cuántos-hay-escritos) | ✅ **Pasa** | Los tres títulos |
| [CP-004](plan_pruebas.md#cp-004--el-que-ya-sigue-el-molde-no-se-reporta) | ✅ **Pasa** | Silencio |
| [CP-005](plan_pruebas.md#cp-005--el-aviso-no-se-repite) | ✅ **Pasa** | La segunda vez, nada |
| [CP-006](plan_pruebas.md#cp-006--marcar-un-aviso-no-apaga-el-otro) | ✅ **Pasa** | Sigue faltando `vacio` |
| [CP-007](plan_pruebas.md#cp-007--el-cierre-no-se-miraba-y-ahora-sí) | ✅ **Pasa** | `molde` con `### 1 ·`, `cierre` con `### H-1 ·` |
| [CP-008](plan_pruebas.md#cp-008--ningún-resumen-del-repositorio-queda-ilegible) | ✅ **Pasa** | Los 47 |
| [CP-009](plan_pruebas.md#cp-009--nada-de-lo-que-ya-estaba-deja-de-pasar) | ✅ **Pasa** | Ver §2 |

**9 de 9 ejecutados. 9 pasan.** 9 casos automatizados en [validadores/tests/test_el_resumen_ilegible_no_es_vacio.py](../../../../../validadores/tests/test_el_resumen_ilegible_no_es_vacio.py).

---

## 2. CP-009 · No regresión

| Qué se corrió | Resultado |
|---|---|
| `validadores/tests/` | **154 · OK** — eran 145 |
| `validadores/pruebas.py` | **357 · OK** (5 fallos esperados, los de siempre) |
| `validar.py estandar` | **Sin incumplimientos** |

---

## 3. Lo que se midió

| Qué | Cuánto |
|---|---|
| Resúmenes del histórico | 47 |
| Que seguían el molde | 44 |
| Escritos como `### N ·` | **3**, todos del 2026-08-17 |
| Hallazgos que el programa no veía | **29** |

| Archivo | Hallazgos que estaban mudos |
|---|---|
| [`sesion-4.md`](../../../../../historico-chat/resumenes/2026-08-17/sesion-4.md) | 15 |
| [`sesion-3.md`](../../../../../historico-chat/resumenes/2026-08-17/sesion-3.md) | 10 |
| [`plan-de-pruebas-y-estado-de-las-51-fases.md`](../../../../../historico-chat/resumenes/2026-08-17/plan-de-pruebas-y-estado-de-las-51-fases.md) | 4 |

**Los tres son de la misma jornada.** No es un descuido repetido: es una forma que se adoptó en una sesión y se copió a la siguiente, **porque nada la contradijo** — y lo que debía contradecirla era justamente el aviso que se apagó solo.

---

## 4. Lo que se supo ejecutando

### El defecto se tapaba a sí mismo, por tres caminos a la vez

1. **El resumen se contaba como vacío**, así que el aviso pedía escribir lo que ya estaba escrito.
2. **La comprobación del cierre nunca corría**, porque necesita encontrar un hallazgo antes de mirar. Es lo que fija el [CP-007](plan_pruebas.md#cp-007--el-cierre-no-se-miraba-y-ahora-sí): el mismo archivo, con una letra de diferencia, cambia de `molde` a `cierre`.
3. **El aviso se marca a sí mismo como ya dado.** Se ve una vez y después calla para siempre.

**Ninguno de los tres deja rastro.** Un aviso que no sale no aparece en ningún registro, y un resumen que se cuenta como vacío se ve exactamente igual que uno que lo está.

### Un aviso que se puede desmentir de un vistazo se deja de leer

El enganche dijo *«el resumen de esta sesión sigue vacío»* con quince hallazgos en pantalla. La reacción natural es dar el aviso por equivocado y seguir — y es la reacción correcta ante un aviso que afirma algo falso. **El programa no se equivocaba al mirar: se equivocaba al nombrar lo que vio.**

Por eso el aviso nuevo dice **cuántos** hay: es lo que lo vuelve creíble para quien tiene el archivo lleno delante.

### Dos marcas, no una

Con una sola marca compartida, avisar de un caso apagaría el otro **para siempre** — y el aviso se da una sola vez, así que apagarlo por error no se recupera. Tiene su caso ([CP-006](plan_pruebas.md#cp-006--marcar-un-aviso-no-apaga-el-otro)) porque es la clase de atajo que parece limpieza al releer el código.

---

## 5. Lo que queda abierto  ·  [`02·F20`](../../../../../base/02-flujo-de-trabajo/reglas/F20-para-y-propon-lo-que-descubras-fuera-del-ca.md)

**Que el próximo resumen se escriba bien no se puede forzar, y es a propósito.** Escribir un hallazgo es criterio ([`13·DOC22`](../../../../../base/13-documentacion/reglas/DOC22-escribe-en-su-propio-documento-lo-que-la-sesion-dejo.md)): el programa crea el archivo, avisa y muestra, pero no escribe ni interpreta. Lo que cambió es que ahora **el molde equivocado se dice**, en vez de convertirse en silencio.

---

## 6. Veredicto

| Campo | Valor |
|---|---|
| **Concepto** | **Cumple** |
| **CA cumplidos** | el `CA-02`, en el caso que no distinguía |
| **CA en «No»** | ninguno |
| **Defectos abiertos aceptados** | ninguno |
| **Ciclos** | 1 |
