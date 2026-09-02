# Funcionalidad implementada — Fase `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-037-la-norma-sube-al-cuerpo-de-reglas` |
| **Módulo** | Cuerpo de reglas |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-037](../HU-037-la-norma-de-redaccion-del-agente.md): los tres |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `37.0.0` — **MAYOR**, y este cambio es el que la sube |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |

---

## 1. Qué se implementó — resumen

**La norma de cómo escribe el agente ya no vive dentro de un documento modelo.**

| Antes | Ahora |
|---|---|
| Escrita como la regla once de dos manuales | Es una regla del cuerpo de reglas, con su identificador |
| Solo la heredaba quien llenara uno de esos dos | Rige todo lo que el agente entrega, **y también lo que contesta en el chat** |
| Se aplicaba copiándola a mano de una plantilla | Se cita |

**El alcance lo decidió el usuario**, y es lo que tuvo la historia detenida: todo documento y también el chat. La respuesta del chat es lo que más se lee y lo único que no queda versionado, así que es donde la convención se pierde primero.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| CA | Ubicación | Estado | Evidencia |
|---|---|---|---|
| CA-01 · la regla existe, con su checklist | `base/00-identidad-y-rol/reglas/ID10-…md` | ✅ | CP-001 |
| CA-02 · los modelos la citan | `plantillas/manual-instalacion.md` | ✅ a medias | CP-003 |
| CA-03 · dice el idioma del proyecto | El cuerpo de la regla | ✅ | CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Evidencia |
|---|---|
| T-01 · decidir el alcance | La decisión del usuario, 2026-08-30 |
| T-02 · escribir la regla | CP-001 |
| T-03 · clasificarla | `validadores/reglas-validables.md` |
| T-04 · que los modelos la citen | CP-003, a medias |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `validar.py metareglas`, `versionado` y `estandar`: sin fallas |
| **Defectos abiertos** | Uno declarado: el modelo de manual de usuario no cita todavía |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

La regla se lee al abrir sesión, con el resto del cuerpo de reglas. No agrega comando.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Rige también lo que el agente contesta en el chat | Es lo que más se lee y lo único que no queda versionado |
| No fija un idioma | Un proyecto en otro idioma tiene que poder cumplirla |
| El impersonal con «se» se nombra aparte | Es la forma en que la regla se incumple sin darse cuenta |
| El modelo de manual de usuario no se tocó | Tiene cambios sin guardar de otra sesión |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| El modelo de manual de usuario no cita la regla | **Abierta y declarada.** Se hace cuando la otra sesión suelte el archivo |
| La ortografía y la gramática siguen sin regla | **Abierta.** El anexo de marcas ya las nombraba como pendientes suyas |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [x] El índice del capítulo.
- [x] `CHANGELOG.md` y `VERSION`, en `37.0.0`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Obliga a migrar.** Un proyecto al día tiene que escribir así de aquí en adelante. Los documentos ya escritos no se reabren: un cambio de norma no reabre lo cerrado.
