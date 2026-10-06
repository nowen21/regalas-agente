# Funcionalidad implementada · Fase `A-EP-025-HU-023-desde-un-turno-y-en-la-base` (módulo `proyectos/cimiento/core/enganches/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-023-desde-un-turno-y-en-la-base` |
| **Módulo** | `proyectos/cimiento/core/enganches/` |
| **Especificación del módulo** | Los CA de la [HU-023](../HU-023-el-analisis-se-prende-desde-un-turno-anterior.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-023 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Analicemos: el pendiente N desde el turno T» prende el análisis desde un turno anterior, o lo corre si ya estaba prendido. El estado del análisis prendido de un proyecto registrado vive en la tabla `proyectos_analisisprendido`, una fila por sesión; sin registro o sin base sigue en su archivo, y lo que quedó en archivo pasa solo a la base.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/enganches/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/0003_analisisprendido.py`, `proyectos/cimiento/core/enganches/estado_en_base.py`, `proyectos/cimiento/core/enganches/analisis_en_curso.py` | ✅ | CP-002 |

**Faltantes / diferimientos:** que el freno lea el estado de su propia sesión queda para la HU-024; mientras tanto lee la fila más reciente, como leía el archivo único.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Escribir «Analicemos: el pendiente N desde el turno T». El estado se ve en la tabla `proyectos_analisisprendido` de la base de Cimiento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Sin sesión se lee la fila más reciente | Es lo que leía el archivo único; el freno lee así hasta la HU-024 | No hace falta: está en `analisis_en_curso.py` |

## 6. Deuda técnica y pendientes generados

Ninguno: lo del freno ya es la fila 11 del análisis, en la HU-024.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`python manage.py migrate proyectos` (o `preparar_base`) aplica la `0003`; los estados en archivo pasan solos a la base.
