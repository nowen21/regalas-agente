# Funcionalidad implementada — Fase `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` (módulo Versionado)   ·   `[CAPA 3]`

> **Veredicto de la fase: [No cumple](resultado_pruebas.md).** El `CA-02` salió en rojo: **una versión adoptada que no existe pasaba sin reporte**. Se cierra declarándolo, no aprobándolo. **Lo que faltaba se construyó después**, en la fase [`B`](../B-EP-002-HU-003-la-version-declarada-se-comprueba/funcionalidad_implementada.md).

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-002-HU-003-retrodocumentar-la-version-adoptada` |
| **Módulo** | Versionado y adopción |
| **Especificación del módulo** | La propia [HU-003](../HU-003-version-adoptada-por-el-proyecto.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-003](../HU-003-version-adoptada-por-el-proyecto.md): `CA-01`, `CA-02` y `CA-03` |
| **Fecha de cierre** | 2026-08-27 |
| **Versión del estándar al cerrar** | `35.1.0` |
| **Commit** | `f10729c` |

> **Se ejecutó el 2026-08-22 y se cierra el 2026-08-27.** Entre las dos fechas se construyó la fase `B` que resolvió su rojo. **Este cierre no lo da por resuelto**: dice qué encontró esta fase y adónde fue a parar.

---

## 1. Qué se implementó — resumen

**Nada nuevo: esta fase midió.** Y encontró un agujero con dos filos.

**Una versión adoptada que no existe pasaba sin reporte.** Un proyecto podía declarar `99.9.9` y nadie decía nada.

**Y peor: esa versión inventada silenciaba el aviso de desfase**, porque al ser mayor que la vigente el proyecto parecía estar adelantado. Un error de escritura apagaba la comprobación que existía para detectarlo.

**Los otros dos criterios sí cumplieron:** el proyecto declara versión y fecha, y queda su historial.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem de la historia | Categoría | Estado | Evidencia |
|---|---|---|---|
| `CA-01` declara versión y fecha | comprobación | ✅ | Lectura del `CLAUDE.md` del proyecto y corrida de `validar.py version` |
| `CA-02` una versión que no existe se detecta | comprobación | ❌ **No cumple** | Copia temporal con `99.9.9`: pasaba sin reporte |
| `CA-03` queda el historial | documento | ✅ | 18, 16 y 12 registros en los tres proyectos |

**El `CA-03` se comprobó sobre tres proyectos reales**, no sobre uno.

### 2.2 Plan de trabajo → ejecución

| Qué | Resultado |
|---|---|
| Lo que el plan pedía | ✅ hecho: se midió lo que había |
| Lo que se encontró | **Un criterio en rojo**, con una deuda crítica y una alta |

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Lo que no se hizo en su momento:** este documento. **La fase quedó cinco días sin cerrar.**

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Qué | Resultado |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **No cumple** — uno de tres criterios en rojo |
| **Defectos** | `D-01` crítica, `D-02` alta, `D-03` baja |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py version --raiz <proyecto>
```

**En el momento de esta fase no detectaba la versión inventada.** Desde la fase `B`, sí.

---

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué |
|---|---|
| El `CA-03` se comprobó sobre **tres proyectos**, no uno | Un solo caso no distingue lo que funciona de lo que funcionó esa vez |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Severidad | Estado al cerrar |
|---|---|---|
| **`D-01` · Una versión adoptada que no existe pasa sin reporte, y además silencia el aviso de desfase** si es mayor que la vigente | Crítica | **Resuelta** en la fase [`B`](../B-EP-002-HU-003-la-version-declarada-se-comprueba/funcionalidad_implementada.md), el 2026-08-22 |
| **`D-02` · La versión declarada y el último registro de adopción pueden contradecirse, y nada los compara.** Caso real: shopnest-mesa | Alta | **Resuelta** en la misma fase `B` |
| **`D-03` · `plantillas/CLAUDE.md.plantilla` nombra la carpeta de dos formas** | Baja | **Abierta** |

**`D-01` merece leerse dos veces.** No era solo que faltara una comprobación: **el error apagaba otra comprobación que sí existía**. Un dato mal escrito volvía ciego al aviso de desfase, y eso no se ve mirando ninguna de las dos piezas por separado.

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La historia [HU-003](../HU-003-version-adoptada-por-el-proyecto.md): su §8 nombra esta fase y la `B`.
- [x] El inventario de historias, que **ya no se mantiene a mano** desde la `35.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

- **Migraciones a correr:** ninguna. Esta fase no cambió nada: midió.
- **Reversión:** no aplica.
