# Funcionalidad implementada — Fase `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` (módulo Documentos modelo)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-003-HU-002-el-veredicto-se-vuelve-a-medir-contra-su-criterio` |
| **Módulo** | Documentos modelo |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-27 |
| **HU / CA cubiertas** | [HU-002](../HU-002-modelos-del-encargo.md): el `CA-01` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.4.0` — **sin cambio**: no se toca código |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | `b3df9f1` |
| **Reemplaza el veredicto de** | `A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo` |

> **Por qué se declara el reemplazo:** Se volvió a medir el `CA-01` contra lo que su criterio pide, y cumple. Aquel rojo se puso por un hueco que el `CA-01` no menciona. **El veredicto de aquella fase no se toca** (`20·M11`): la cuenta lo deja atrás, el documento sigue diciendo lo que decía.

---

## 1. Qué se implementó — resumen

**Nada. Esta fase vuelve a medir un criterio contra lo que el criterio pide.**

La fase [`A`](../A-EP-003-HU-002-retrodocumentar-los-modelos-del-encargo/resultado_pruebas.md) cerró con «No cumple» porque *«el planteamiento de esta casa está vacío»*. **Su `CA-01` no pide eso**: pide que existan los tres modelos y que la cadena se recorra en los dos sentidos — y **la propia fase `A` midió eso y le dio verde**.

**Se reprobó a sí misma por algo de al lado.**

| Antes | Ahora |
|---|---|
| «No cumple», por un hueco que el criterio no menciona | **Cumple**: 0 fallas sobre 11 épicas y 119 historias |

**El hallazgo de la fase `A` no se descarta.** Que la casa no tuviera su planteamiento era cierto y valía; lo mal puesto era la factura. Y hoy **ni siquiera sigue abierto**.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` los tres modelos existen | documento | `plantillas/ciclo-vida-proyectos/` | ✅ | CP-001 |
| `CA-01` y la cadena se recorre en los dos sentidos | servicio | `validar.py trazabilidad` sobre el árbol real | ✅ | CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · los tres modelos | ✅ | CP-001 |
| T-02 · la cadena, **corrida** | ✅ | CP-002, y el hallazgo del ciclo 1 |
| T-03 · el hueco que la `A` señaló | ✅ | CP-003 |
| T-04 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): **uno**, la tabla de `EP-001`, con **una fila**. Se paró, se reportó, y el usuario amplió el alcance. Está en el §4.1 del resultado.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 2 |
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia código |
| **Defectos abiertos** | Ninguno. `DEF-01` corregido |

**El único defecto no era de esta fase ni de la `A`:** `HU-036` no estaba en la tabla de `EP-001`, y lo mismo había pasado con dos historias de `EP-005` el mismo día. Es `S-064`.

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py trazabilidad
```

Sin cambios. Es la comprobación que ya existía, corrida sobre el árbol real.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué | Señal |
|---|---|---|
| **Se corre, no se cita** | Apoyarse en la medición de la `A` habría heredado su resultado de hace diez días — y la falla de hoy habría pasado invisible | `S-064` |
| El veredicto de la `A` **no se toca** | El error enseña más que la conclusión. Es lo mismo que se decidió con `H-34` | `20·M11` |
| **El hallazgo se conserva**, y se dice dónde debía cobrarse | Era cierto y valía. Borrarlo por estar mal ubicado perdería algo útil | `S-063` |
| Se comprueba si el hueco **sigue abierto**, aunque no sea del `CA-01` | Decir «ya no aplica» sin mirarlo sería el defecto del día | `CP-003` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Una historia se crea y nadie vuelve a la tabla de su épica | **Las tres del día, corregidas.** La detección ya existía y funcionaba: el problema es que su aviso convive con otros cuarenta y cuatro. Es `S-064` |
| Nadie vuelve a mirar un veredicto en rojo | **Abierta.** Es `S-061`, y esta fase es una de las dos que lo hizo a mano |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La tabla de [EP-001](../../../EP-001-cuerpo-de-reglas-heredable/epica.md), con la `HU-036`.
- [x] La épica [EP-003](../../epica.md).
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Lo que cambia es que la historia deja de arrastrar un rojo que su criterio no sostiene.
