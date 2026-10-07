# Funcionalidad implementada · Fase `A-EP-026-HU-002-las-versiones` (módulo Historia de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-002-las-versiones` |
| **Módulo** | Historia de Cimiento, `proyectos/cimiento/core/historia/` |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-cada-proyecto-tiene-su-version-y-el-estandar-la-suya.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-002 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.1.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Todo cambio de configuración sube una versión: la del proyecto si es solo suya (ficha, ajustes, niveles, suspensiones) y la del estándar si es común (ajustes de capa 1 y, desde la HU-003, el estándar). Los formularios hacen las dos preguntas que fijan MAYOR, MENOR o PARCHE; lo que se guarda en un envío es una sola versión. «Historia» → «Versiones» las lista con sus cambios.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Historia» → «Versiones» (`/historia/versiones/`). En una pantalla nueva, incluir `historia/_tipo_de_version.html` en su formulario; desde código, `quien_y_por_que(tipo=MENOR)`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La versión la crea el primer cambio de cada envío y el ámbito sale de la fila completa | Una pantalla nueva solo incluye la plantilla; el diff no trae el proyecto | S-332 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar la migración `historia 0002` con `manage.py migrate` (hecho en esta máquina el 2026-10-06).
