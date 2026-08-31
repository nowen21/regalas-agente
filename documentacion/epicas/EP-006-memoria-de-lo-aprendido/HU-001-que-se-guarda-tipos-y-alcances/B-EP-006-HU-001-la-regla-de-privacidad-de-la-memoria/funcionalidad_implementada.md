# Funcionalidad implementada — Fase `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` (módulo Memoria)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-006-HU-001-la-regla-de-privacidad-de-la-memoria` |
| **Módulo** | Memoria |
| **Especificación del módulo** | No hay documento aparte. `02·F19` |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), aprobado el 2026-08-30 |
| **HU / CA cubiertas** | [HU-001](../HU-001-que-se-guarda-tipos-y-alcances.md): el transversal de privacidad |
| **Fecha de cierre** | 2026-08-30 |
| **Versión del estándar al cerrar** | `36.0.0` — **MAYOR**, y este cambio es el que la sube |
| **Veredicto** | **Cumple**, copiado del §2 del resultado |
| **Commit** | Pendiente de autorización |
| **Reemplaza el veredicto de** | `A-EP-006-HU-001-retrodocumentar-que-se-guarda-y-con-que-alcance` |

> **Por qué se declara el reemplazo:** el criterio pedía una regla que no existía, y ahora existe. Aquel rojo era cierto el 2026-08-17 y siguió siéndolo trece días. **El veredicto de aquella fase no se toca** (`20·M11`).

---

## 1. Qué se implementó — resumen

**La regla [`04·S19`](../../../../../base/04-seguridad.md), que hasta hoy no existía.**

La fase `A` cerró en rojo porque el criterio transversal de privacidad pedía que la memoria no guardara datos personales ni claves, y al buscar la regla que lo dijera no había ninguna. `13·DOC5` dice qué se registra como señal, y no dice qué no.

| Antes | Ahora |
|---|---|
| Ninguna regla decía qué **no** puede entrar a la memoria | `04·S19` lo dice, y con su ejemplo |
| `00·N6` cubría la credencial, en cualquier parte | Sigue igual. `S19` agrega el dato personal, y nombra el sitio |

**Este es un rojo de los que no se cierran midiendo.** Escribir una regla es fijar norma, y eso lo decide el usuario (`01·C4`). Estuvo trece días esperando esa decisión.

---

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Historia → implementación

| Ítem | Categoría | Ubicación | Estado | Evidencia |
|---|---|---|---|---|
| Transversal · Privacidad | norma | `base/04-seguridad.md`, `S19` | ✅ | CP-001, CP-002 |

### 2.2 Plan de trabajo → ejecución

| Tarea | Estado | Evidencia |
|---|---|---|
| T-01 · comprobar que no existía | ✅ | Cero menciones en `13·DOC5` |
| T-02 · escribir la regla | ✅ | 303 caracteres de cuerpo |
| T-03 · clasificarla | ✅ | `reglas-validables.md` |
| T-04 · versionar y declarar | ✅ | `36.0.0` |

**Correspondencia:** 4 tareas, 4 con resultado.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

---

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | **Cumple**, ciclo 1 |
| **Suites ejecutadas** | `validar.py metareglas` sin incumplimientos · `validar.py versionado` 0 fallas |
| **Defectos abiertos** | Ninguno |

---

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

La regla se lee al abrir sesión, con el resto de `base/`. No agrega comando.

---

## 5. Decisiones no obvias  ·  `13·DOC5`

| Decisión | Por qué |
|---|---|
| Va en `04` y no en `13` | No es cómo se escribe un documento: es qué dato puede salir de una sesión y quedar guardado |
| Nombra a `00·N6` sin declarar dependencia | `20·M7` prohíbe extender una `[BLINDADA]` |
| **MAYOR** | Un proyecto al día tiene que revisar su memoria: eso es algo nuevo que hacer |
| Se declara qué mitad no es comprobable | El dato personal no se detecta sin decidir qué nombre propio es de una persona |

---

## 6. Deuda técnica y pendientes generados

| Descripción | Estado al cerrar |
|---|---|
| `enmascarar.py` corre sobre la transcripción y no sobre la memoria | **Abierta y declarada** en el registro de validables. Es la mitad comprobable de `S19` |
| La memoria que ya existe no se revisó | **Abierta.** Se mide antes de tocar nada |

---

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] El `Estado` de la historia y su tabla de fases.
- [x] `CHANGELOG.md` y `VERSION`, en `36.0.0`.
- [x] `validadores/reglas-validables.md`.

---

## 8. Despliegue — si aplica  ·  `13·DOC4`

**Obliga a migrar.** Un proyecto al día tiene que revisar su memoria y sacar lo que no debería estar. El aviso de desfase lo informa al abrir sesión; no migra solo.
