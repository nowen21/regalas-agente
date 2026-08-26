# Funcionalidad implementada — Fase A-EP-002-HU-001-retrodocumentar-el-numero-de-version (módulo Versionado)

> **Veredicto de la fase: [No cumple](resultado_pruebas.md#6-veredicto-de-la-fase).** El número existe, sale de un solo archivo y las 73 entradas declaran su tipo. Falla el CA-01: **`15.4.0` aparece dos veces**, con contenidos distintos.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** ([`02·F12.6`](../../../../../base/02-flujo-de-trabajo/reglas/F12-relacion-y-nomenclatura-de-fases.md)) | `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |
| **Módulo** | Versionado — [`VERSION`](../../../../../VERSION), [`CHANGELOG.md`](../../../../../CHANGELOG.md), [`validadores/version.py`](../../../../../validadores/version.py) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / exigencias cubiertas** | HU-001: CA-01, CA-02, CA-03 y sus dos transversales |
| **Fecha de cierre** | 2026-08-17 · **Commit** pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Nada de programa: la fase recorrió las 73 entradas del registro una por una.** El número existe desde la `1.0.0` y nadie había comprobado que la serie fuera coherente.

No lo es del todo.

---

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| El número, en un solo archivo | datos | [`VERSION`](../../../../../VERSION) | ✅ Ya existía | CP-001 |
| Lo lee un solo programa | programa | [`version.py`](../../../../../validadores/version.py) · `version_estandar()` | ✅ Ya existía | CP-001 |
| Cada entrada declara su tipo | documentación | [`CHANGELOG.md`](../../../../../CHANGELOG.md) | ✅ Ya existía | CP-003, CP-004 |
| MAYOR obliga; PARCHE no cambia qué se exige | documentación | Las seis entradas revisadas | ✅ Ya existía | CP-003, CP-004 |
| **Que ningún número se repita** | — | `15.4.0` figura dos veces | ❌ **No se cumple** | CP-005 |
| Las exigencias, con red | pruebas | [`validadores/pruebas.py`](../../../../../validadores/pruebas.py), clase `NumeroDeVersion` | ✅ Escritas acá | 4 pruebas |

### Criterios de aceptación

| CA | Cómo quedó | Estado |
|---|---|---|
| CA-01 | Tres partes, un solo archivo, coincide con el registro. **Un número repetido** | ❌ |
| CA-02 | Las tres MAYOR revisadas obligan a hacer algo | ✅ |
| CA-03 | Las tres PARCHE revisadas no cambian qué se exige | ✅ |
| Transversal · Límites · No regresión | Manda el tipo más alto; el número nunca baja en 73 entradas | ✅ |

---

## 3. Lo que la fase midió

| Medición, 2026-08-17 | Valor |
|---|---:|
| Entradas del registro | **73** |
| Que no declaran su tipo | **1**, la `1.0.0` — y está bien: no hay nada anterior |
| Veces que el número baja | **0** |
| Saltos mal formados | **0** |
| **Números repetidos** | **1** — `15.4.0` |

---

## 4. El defecto, y por qué no lo arregla esta fase

**`15.4.0` figura dos veces**, con fechas y contenidos distintos:

| Fecha | De qué trata |
|---|---|
| 2026-08-14 | El enganche que sostenía el resumen no creaba el resumen |
| 2026-08-15 | Una sección más en una plantilla |

La segunda tendría que haber sido `15.5.0`.

**Por qué importa y no es cosmético:** un proyecto declara qué versión adoptó, y el aviso de desfase compara ese número contra el del estándar. Con dos `15.4.0`, un proyecto que diga «adopté la 15.4.0» **no puede saber cuál tiene** — ni él ni el validador. Es exactamente el problema que el número existe para resolver.

**No se corrige acá.** Renumerar una versión ya publicada obliga a revisar qué la cita, y [`20·M11`](../../../../../base/20-meta-reglas/reglas/M11-las-reglas-no-se-borran-se-derogan.md) es explícito en que nada se renumera a la ligera. **Es decisión del usuario.**

---

## 5. Decisiones y señales

| Decisión | Dónde quedó |
|---|---|
| La serie se recorre **entera**, de la más vieja a la más nueva: el choque estaba en el medio y una muestra no lo habría visto | CP-005 del [resultado](resultado_pruebas.md) |
| La `1.0.0` se exime de declarar tipo, **con su motivo**: no hay nada anterior contra lo que compararla | La prueba `test_toda_entrada_del_registro_declara_su_tipo` |
| El marcador cuenta con o sin punto dentro de la negrita: `**MENOR**` y `**MENOR.**` son lo mismo | La misma prueba |

---

## 6. Lo que no entró, y dónde sigue

| Qué | Dónde |
|---|---|
| Qué hacer con la segunda `15.4.0` | **Decisión del usuario**: toca una versión publicada |
| El registro de qué cambió en cada versión | [HU-002](../../HU-002-registro-de-cambios/HU-002-registro-de-cambios.md) |
| La versión que declara el proyecto | [HU-003](../../HU-003-version-adoptada-por-el-proyecto/HU-003-version-adoptada-por-el-proyecto.md) |

**La advertencia que deja esta fase:** el número de versión es el contrato entre el estándar y los proyectos que lo heredan, y llevaba dos días con dos significados sin que nada lo notara. Bastaba con recorrer la lista.
