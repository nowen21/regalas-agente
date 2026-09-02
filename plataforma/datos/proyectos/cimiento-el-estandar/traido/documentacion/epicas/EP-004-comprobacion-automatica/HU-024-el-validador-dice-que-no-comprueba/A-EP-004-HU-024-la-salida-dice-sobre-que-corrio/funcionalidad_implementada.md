# Funcionalidad implementada — Fase `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-024-la-salida-dice-sobre-que-corrio` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-024](../HU-024-el-validador-dice-que-no-comprueba.md): los tres |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.2` — **sin cambio** |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Que el cero diga sobre qué corrió.**

| Antes | Ahora |
|---|---|
| «0 falla(s)» sin decir sobre qué | Dice qué carpetas recorrió y cuántos archivos miró |
| El mismo cero para «no hay marcas» y «acá no miré» | Dos frases distintas |
| No decía qué partes de la norma no cuenta | Las nombra |

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| CA | Ubicación | Estado | Evidencia |
|---|---|---|---|
| CA-01 | `marcas.alcance()` y el conteo de `validar()` | ✅ | CP-001, CP-002, CP-005 |
| CA-02 | `marcas.NO_SE_CUENTAN` | ✅ | CP-004 |
| CA-03 | `marcas.alcance()` con cero mirados | ✅ | CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · contar lo que mira | CP-001 |
| T-02 · armar las frases con ese dato | CP-001, CP-004 |
| T-03 · distinguir el árbol sin nada | CP-003 |
| T-04 · que el subcomando las imprima | La corrida del §3 |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | 5 pruebas nuevas, 5 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

```
python validadores/validar.py marcas
```

Sin cambios en cómo se llama: cambia lo que responde.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| El alcance sale de lo recorrido | Una frase escrita aparte envejece sin avisar |
| Se dice **cuántos** archivos, no solo la carpeta | «Se recorrió base/» es cierto también con cero archivos |
| Las frases van después del resultado | Lo primero que se lee tiene que ser el veredicto |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| El alcance sigue siendo `base/` y `plantillas/` | **Abierta y declarada.** Ampliarlo es una decisión aparte; lo que cambia acá es que deja de ser invisible |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
