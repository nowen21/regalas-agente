# Funcionalidad implementada · Fase `A-EP-025-HU-018-la-ayuda` (módulo `proyectos/cimiento/core/ayuda/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-018-la-ayuda` |
| **Módulo** | `proyectos/cimiento/core/ayuda/` |
| **Especificación del módulo** | Los CA de la [HU-018](../HU-018-cimiento-trae-su-ayuda-y-su-manual.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-018 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La aplicación `core.ayuda`: un botón «Ayuda» en cada pantalla, que abre un panel con la ayuda de esa pantalla; el «?» con la ayuda de cada campo; y un manual de 10 secciones en `/ayuda/`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Pantallas | `proyectos/cimiento/core/ayuda/`, `proyectos/cimiento/core/ayuda/textos.py`, las dos plantillas, `proyectos/cimiento/templates/base.html`, `proyectos/cimiento/config/settings/base.py`, `proyectos/cimiento/config/urls.py` | ✅ | CP-001 |
| CA-02 | Pantallas y pruebas | `proyectos/cimiento/core/ayuda/secciones.py`, `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/`, `proyectos/cimiento/core/ayuda/claves.py`, `proyectos/cimiento/core/ayuda/tests.py` | ✅ | CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `anatomia/que-esta-amarrado-a-la-herramienta.md` y `CHANGELOG.md` se declararon en el plan durante la fase, antes de tocarlos.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

En cualquier pantalla de Cimiento, el botón «Ayuda» del menú abre la ayuda de esa pantalla, y el «?» junto a un campo dice qué es. El manual completo está en `/ayuda/`. Una pantalla nueva necesita su sección en `secciones.py`, y un campo nuevo su texto en `textos.py`: las pruebas fallan si falta alguno.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las pruebas exigen texto para toda clave y sección para toda pantalla | Así la ayuda no se queda atrás cuando entra una pantalla; se descartó revisarla a mano | No hace falta: lo dicen las pruebas |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`anatomia/que-esta-amarrado-a-la-herramienta.md` (34 amarrados de 120) y la entrada 55.0.0 de `CHANGELOG.md`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Llega con la versión 55.0.0; no necesita migraciones.
