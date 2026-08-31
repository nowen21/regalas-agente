# Funcionalidad implementada — Fase `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse` (módulo Programas de comprobación)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-004-HU-021-las-dos-formas-que-quedaban-sin-leerse` |
| **Módulo** | Programas de comprobación |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-021](../HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido.md): la tercera cuenta |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**Que el lector del veredicto reconozca las dos formas que quedaban.**

Cinco historias se contaban como «no dicen si cumplen» y las cinco lo dicen, en
la primera línea de su sección final.

| Antes | Ahora |
|---|---|
| `**Concepto: Cumple.**` no se leía | Se lee |
| `## 6. Concepto final` con la palabra debajo, tampoco | Se lee |
| 5 historias sin veredicto | **0** |

**No se tocó ninguno de los cinco resultados.** Son fases cerradas: se corrige
quien lee, no lo leído.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| La tercera cuenta | comprobación | `validadores/fases.py` | ✅ | CP-001, CP-002, CP-003 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · leer las cinco mudas | ✅ | §3 del resultado |
| T-02 · ampliar el lector | ✅ | Dos patrones más |
| T-03 · probar que no lee de más | ✅ | CP-003 |
| T-04 · declarar el resultado | ✅ | Este documento |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `pruebas.LaCuentaMiraElVeredicto`: 35 pruebas, 35 en verde |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios: `python validadores/validar.py fases`.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Se corrige el lector, no los cinco resultados | Son fases cerradas (`20·M11`) |
| Se amplía qué título vale, nunca dónde se busca | «Cumple» aparece en cada fila de criterio |
| La prueba que más importa es la que **no** debe leer | Ampliar sin ella sería aflojar |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| Cuatro fases para el mismo lector, cada una contando lo que ya sabía reconocer | **Anotada** en el §4.1 del resultado. El remedio no es otro patrón: es abrir lo que queda |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] La tabla de fases de la historia.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
