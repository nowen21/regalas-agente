# Funcionalidad implementada — Fase `A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion` (módulo Documentos modelo)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-003-HU-008-retrodocumentar-los-puntos-de-aprobacion` |
| **Módulo** | Documentos modelo y procedimientos |
| **Especificación del módulo** | La propia [HU-008](../HU-008-puntos-de-aprobacion.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-008](../HU-008-puntos-de-aprobacion.md): `CA-01`, `CA-02` y `CA-03`. Los tres |
| **Fecha de cierre** | 2026-08-26 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | Por anotar al guardar |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-26.** Entre las dos fechas no se tocó nada de esta fase: faltaba este documento.

---

## 1. Qué se implementó — resumen

**Los puntos donde aprueba una persona están escritos, y se comprobó que se usan.** Son siete, marcados en el molde que heredan los proyectos, y aparecen llenos en cada fase real.

**Una respuesta ambigua no habilita** — lo dice `00·N1`, que pide aprobación explícita.

**Y aprobar una cosa no aprueba la siguiente**, que es `02·F25`, con su uso real en la jornada.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| `CA-01` la lista existe y dice qué se aprueba | documento | El molde del estado de fase, que heredan los proyectos | ✅ | **Siete puntos**, llenos en cada fase real |
| `CA-02` una respuesta ambigua no habilita | norma | [`00·N1`](../../../../../base/00-nucleo-blindado.md) | ✅ | La regla, **sin comprobación automática y dicho** |
| `CA-03` aprobar una cosa no aprueba la siguiente | norma | `02·F25` | ✅ | Su uso real en la jornada |

**El `CA-02` se marcó cumplido diciendo que no tiene comprobación automática.** No se disfrazó de verificado: se dice que descansa en la regla y en la conducta, y que ningún programa lo mira.

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
| **Defectos abiertos que se aceptaron** | `D-02` (baja). `D-01` se cerró al comprobarlo |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

La lista vive en el **molde del estado de fase**, que cada fase copia. Se llena a medida que las estaciones pasan, y las que llevan marca de persona no se marcan solas.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El `CA-02` se marca cumplido **declarando que nadie lo comprueba con un programa** | Es honesto y es lo que `04·R4` pide: no afirmar sobre lo que no se observó. Marcarlo verificado habría sido afirmar de más |
| La lista vive en un **molde**, no en `base/` | Es donde se usa. El costo está en `D-02` |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · El plan afirmaba que la lista no llega a los proyectos que heredan.** Llega: está en el molde del estado de fase | Media | **Cerrada al comprobarlo.** El plan estaba equivocado, no el producto |
| **`D-02` · La lista vive en un molde, no en `base/`.** Quien busque la exigencia en el cuerpo de reglas no la encuentra como lista | Baja | **Abierta** |

**`D-01` merece leerse con atención**, porque es de la clase que más costó en este repositorio: **el plan afirmaba algo del producto sin haberlo verificado**, y al ejecutar resultó falso. Verificar cerró la deuda sin tocar nada.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-008](../HU-008-puntos-de-aprobacion.md): su §8 nombra esta fase.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna.
- **Qué cambia para quien ya tenía el estándar:** nada. Los puntos ya estaban en el molde.
- **Reversión:** no aplica. La fase comprobó; no cambió el producto.
