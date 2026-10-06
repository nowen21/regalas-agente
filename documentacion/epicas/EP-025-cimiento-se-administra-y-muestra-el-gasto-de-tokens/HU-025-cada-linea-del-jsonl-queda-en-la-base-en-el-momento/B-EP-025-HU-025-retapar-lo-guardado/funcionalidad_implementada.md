# Funcionalidad implementada · Fase `B-EP-025-HU-025-retapar-lo-guardado` (módulo Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-025-retapar-lo-guardado` |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-025 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.3.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py retapar_lineas` vuelve a pasar el tapado por todas las líneas guardadas y tapa lo que hoy reconoce. Se corrió sobre la base: 8 de 102.478 líneas cambiaron, y no quedó ninguna clave de Anthropic en claro.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python manage.py retapar_lineas`, cada vez que el tapado aprenda una forma nueva.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La huella no cambia al volver a tapar | Identifica la línea original; si cambiara, la próxima lectura la guardaría otra vez | S-314 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Fila de la fase en la HU-025.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py retapar_lineas` una vez; ya corrida en esta máquina.
