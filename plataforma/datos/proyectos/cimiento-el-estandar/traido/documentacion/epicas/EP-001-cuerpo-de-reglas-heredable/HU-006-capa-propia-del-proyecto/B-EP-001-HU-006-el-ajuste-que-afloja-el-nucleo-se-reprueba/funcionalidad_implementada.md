# Funcionalidad implementada — Fase `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-006-el-ajuste-que-afloja-el-nucleo-se-reprueba` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-006](../HU-006-capa-propia-del-proyecto.md): el CA-03 |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `35.10.0`, **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-001-HU-006-retrodocumentar-la-capa-del-proyecto` |

> **Por qué se declara el reemplazo:** el CA-03 se ejecutó por primera vez, falló, se construyó lo que faltaba y ahora se cumple. Aquel rojo era cierto el 2026-08-17 y siguió siéndolo hasta hoy. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**Que `validar_catalogo` vea lo que `20·M7` prohíbe.**

La fase `A` cerró en rojo con una razón honesta: el caso no se pudo provocar sin escribir en un proyecto real, y eso está prohibido. Provocado en una carpeta temporal, **falló**: un proyecto que declaraba «afloja `N2`» y «deroga `N6`» pasaba con cero hallazgos, porque la comprobación solo miraba lo que pide `20·M16`, que haya respaldo y que el ID exista, y esos dos IDs existen.

| Antes | Ahora |
|---|---|
| Un ajuste que declara aflojar el núcleo pasa sin reclamo | Falla, nombrando la regla y su marca `[BLINDADA]` |
| Un ajuste que endurece el núcleo pasa | Sigue pasando |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-03 | comprobación | `validadores/metareglas.py` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · provocar el caso | ✅ | «hallazgos: 0» antes de construir |
| T-02 · construir la comprobación | ✅ | `_afloja_una_blindada` |
| T-03 · probar los dos casos | ✅ | 2 pruebas en verde |
| T-04 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.ElAjusteDelProyectoNoAflojaElNucleo`: 2 pruebas, 2 en verde. `validar.py metareglas`: sin incumplimientos |
| **Defectos abiertos** | Ninguno nuevo |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin punto de entrada nuevo. Corre dentro de lo que ya existía:

```
python validadores/validar.py metareglas --catalogo <ruta del proyecto>
```

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se mira el **verbo del respaldo**, no la intención del texto | Interpretar intención no es comprobar |
| Lista cerrada de verbos que aflojan | Reprobar toda mención del núcleo volvería inservible la capa propia |
| Se dice lo que **no** se detecta | Un proyecto que contradiga el núcleo sin declararlo sigue sin verse. Prometer más sería un veredicto falso |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| La contradicción que el proyecto no declara sigue sin detectarse | **Abierta y declarada**, con su motivo |
| Los defectos `D-01` y `D-02` de la fase `A` | **Abiertos.** Son de otro asunto |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.** Un proyecto con reglas propias verá la comprobación la próxima vez que la corra.
