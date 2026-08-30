# Funcionalidad implementada — Fase `B-EP-002-HU-001-el-numero-repetido-se-declara` (módulo Versionado y adopción)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-002-HU-001-el-numero-repetido-se-declara` |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-001](../HU-001-numero-de-version-y-que-significa.md): el CA-01 |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `35.10.0`, **sin cambio** |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-002-HU-001-retrodocumentar-el-numero-de-version` |

> **Por qué se declara el reemplazo:** el CA-01 se mide ahora contra lo que la casa sostiene. Aquel rojo era cierto el 2026-08-22 con la lectura de entonces. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que la prueba exija lo que se sostiene, no lo que se decidió no cumplir.**

`15.4.0` aparece dos veces porque dos sesiones numeraron a la vez. El registro decidió el 2026-08-15 **no renumerar**, y escribió el motivo: un proyecto pudo haber adoptado ese número, y cambiárselo después le mueve el piso sin que se entere.

La prueba, mientras tanto, seguía exigiendo unicidad y llevaba ocho días marcada como fallo esperado. **Una prueba que exige lo que la casa decidió no cumplir no mide nada:** enseña a mirar los fallos esperados como paisaje.

| Antes | Ahora |
|---|---|
| La prueba exige unicidad y está en fallo esperado | Exige que la repetición esté declarada, y corre |
| Un número repetido en silencio pasaría igual | Falla |

**El `CHANGELOG.md` no se tocó.**

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | prueba | `validadores/pruebas.py`, clase `NumeroDeVersion` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · leer qué exige el CA y qué decidió el registro | ✅ | §1 de este documento |
| T-02 · que la prueba exija lo que se sostiene | ✅ | 5 de 5 en verde |
| T-03 · probar el repetido callado | ✅ | CP-002 |

**Correspondencia:** 3 tareas, 3 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.NumeroDeVersion`: 5 pruebas, 5 en verde, 0 fallos esperados |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios. El aviso de `validar.py versionado` sigue saliendo en cada corrida, y se conserva a propósito: mantiene el caso a la vista.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| No renumerar | Ya estaba decidido en el registro, con su motivo: quien adoptó `15.4.0` tiene las dos cosas |
| Cambiar la prueba, no el registro | Lo que estaba mal era la exigencia, no el dato |
| La marca vale en cualquiera de las dos entradas del par | Comparten número; lo que importa es que la repetición esté dicha |
| Probar el repetido callado | Sin eso, aceptar el declarado es aceptar cualquiera |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Dos sesiones pueden volver a numerar a la vez | **Abierta.** Es el pendiente 22, y la comprobación de sesiones mezcladas es lo que se construyó para eso |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, y en esta fase es lo importante: no se tocan.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
