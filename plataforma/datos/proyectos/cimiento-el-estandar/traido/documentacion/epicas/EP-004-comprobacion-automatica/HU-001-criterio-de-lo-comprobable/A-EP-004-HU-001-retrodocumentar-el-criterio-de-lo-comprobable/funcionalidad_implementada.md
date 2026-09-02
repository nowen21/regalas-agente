# Funcionalidad implementada — Fase `A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-001-retrodocumentar-el-criterio-de-lo-comprobable` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | La propia [HU-001](../HU-001-criterio-de-lo-comprobable.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-001](../HU-001-criterio-de-lo-comprobable.md): `CA-01`, `CA-02` y `CA-03`. Los tres |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `b19ca91` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-26.** Entre las dos fechas no se tocó nada de esta fase: faltaba este documento.

---

## 1. Qué se implementó — resumen

**El criterio que decide qué regla se puede comprobar con un programa existe, tiene identificador y se puede citar.** Es `20·M9`.

**Y se comprobó que se aplica de verdad:** 99 reglas están clasificadas como criterio humano, **cada una con su motivo escrito**. No es una lista de excepciones sin justificar.

**Lo comprobable a medias se parte**, en vez de darlo por comprobable entero o descartarlo.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` el criterio existe y se puede citar | norma | `20·M9`, con su identificador | ✅ | El enunciado **en las dos direcciones**: qué entra y qué no |
| `CA-02` lo que se discute queda afuera | clasificación | `validadores/reglas-validables.md` | ✅ | **99 reglas** clasificadas como criterio humano, con su motivo |
| `CA-03` lo comprobable a medias se parte | clasificación | La misma | ✅ | Las cuatro *difusas* y las cinco que esperan declaración, más el caso de `A-EP-004-HU-013` |

**Que las 99 traigan su motivo es lo que hace útil el `CA-02`.** Una lista de reglas «no comprobables» sin razones es una lista de reglas que nadie quiso comprobar.

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado |
|---|---|
| Las del plan | ✅ hechas |

**Lo que no se hizo:** cerrar la trazabilidad, que es este documento. **La fase quedó cuatro días en la estación 11.**

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, los tres criterios |
| **Defectos abiertos que se aceptaron** | `D-02` (media). `D-01` se cerró al comprobarlo |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- **El criterio:** `20·M9`, en el capítulo de meta-reglas.
- **La clasificación de cada regla:** [`validadores/reglas-validables.md`](../../../../../validadores/reglas-validables.md), con su motivo cuando no es comprobable.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El criterio se enuncia **en las dos direcciones** | Decir solo qué entra deja el borde a interpretación. Decir también qué queda afuera lo cierra |
| Lo comprobable **a medias se parte**, no se descarta ni se da por entero | Si no, la parte comprobable se pierde por culpa de la que no lo es |
| Cada regla no comprobable **trae su motivo** | Sin motivo, la clasificación es una lista de lo que nadie quiso hacer |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · El plan daba el criterio por no citable**, y al comprobarlo resultó que sí tiene identificador | Baja | **Cerrada al comprobarlo.** El plan estaba equivocado, no el producto |
| **`D-02` · El conteo de `reglas-validables.md` está escrito con `~` delante** — «~54», «~22», «~99». Es una auditoría del 2026-08-05 que nadie volvió a correr | Media | **Abierta** |

**`D-02` es de la misma familia que lo que se arregló el 2026-08-26 con el inventario de historias:** un número escrito a mano que envejece. Acá está peor disimulado —lleva `~` delante, admitiendo que es aproximado— pero es el mismo problema: **un dato que vive fuera de donde se calcula.**

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-001](../HU-001-criterio-de-lo-comprobable.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** nada. El criterio ya estaba publicado.
- **Reversión:** no aplica. La fase comprobó; no cambió el producto.
