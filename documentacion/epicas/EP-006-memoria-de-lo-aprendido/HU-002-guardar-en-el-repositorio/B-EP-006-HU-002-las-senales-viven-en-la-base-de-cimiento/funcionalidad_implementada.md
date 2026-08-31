# Funcionalidad implementada — Fase `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-002-las-senales-viven-en-la-base-de-cimiento` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-002](../HU-002-guardar-en-el-repositorio.md): el CA-01, lo guardado vive en el repositorio con su historial |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **sin cambio**: no se toca `base/` ni `plantillas/` |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio` |

> **Por qué se declara el reemplazo:** la decisión que faltaba está tomada y aplicada. Aquel rojo era cierto el 2026-08-17. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

La fase [`A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio`](../A-EP-006-HU-002-retrodocumentar-el-guardado-en-el-repositorio/resultado_pruebas.md) cerró en rojo porque las **237 señales** no estaban versionadas: `memoria/senales.db` está en `.gitignore` a propósito y no tiene ningún historial. Los 18 recuerdos sí cumplían.

**Las señales se quedan en su propia base, la de Cimiento.** Cimiento es la línea base de todos los proyectos, y su memoria es de todos: hoy la base guarda **268 señales**, de las cuales **186 son de siete proyectos distintos** y 82 son de organización. Meterla al control de versiones de este repositorio la ataría a uno solo de los proyectos que sirve.

**Por qué el criterio se relee y no se incumple.** El `CA-01` se escribió pensando en un solo repositorio, cuando la memoria era una carpeta de archivos. Al crecer resultaron ser dos cosas con dueños distintos:

- **Los recuerdos** son de este repositorio y de quien trabaja en él. Viven en `historico-chat/memory/`, versionados, y ahí el criterio se cumple entero: 23 archivos con su índice.
- **Las señales** son de Cimiento, que es la línea base de todos los proyectos. Su base es compartida, y por eso no puede vivir dentro del control de versiones de uno.

Lo que este repositorio sí versiona de señales es [`documentacion/senales.md`](../../../../../documentacion/senales.md), las suyas: 85 al cerrar esta fase.

**Y lo que no se decidió acá:** cómo se respalda esa base. Que no vaya al control de versiones de este repositorio no significa que no tenga que tener respaldo, y eso es de Cimiento como producto.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| CA-01, lo guardado vive en el repositorio con su historial | decisión aplicada | Este cierre | ✅ | CP-001 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · medir los dos sitios | ✅ | §3 del resultado |
| T-02 · aplicar la decisión | ✅ | §3 del resultado |
| T-03 · declarar el veredicto | ✅ | Este documento |

**Correspondencia:** 3 tareas, 3 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | Ninguna nueva: esta fase no cambia código |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Sin cambios.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Las señales se quedan en la base de Cimiento | Es binario, dos sesiones se lo pisan sin fusión posible, y 186 de sus 268 señales son de otros proyectos |
| El criterio se relee, no se incumple | Fue escrito cuando la memoria era una carpeta de un solo repositorio. Lo que cambió es el alcance, no la exigencia |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| El respaldo de la base de Cimiento no está decidido | **Abierta.** Es de Cimiento como producto, no de este cuerpo de reglas |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [ ] `VERSION` y `CHANGELOG.md`: **no aplica**, no se toca `base/` ni `plantillas/`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Nada que desplegar.**
