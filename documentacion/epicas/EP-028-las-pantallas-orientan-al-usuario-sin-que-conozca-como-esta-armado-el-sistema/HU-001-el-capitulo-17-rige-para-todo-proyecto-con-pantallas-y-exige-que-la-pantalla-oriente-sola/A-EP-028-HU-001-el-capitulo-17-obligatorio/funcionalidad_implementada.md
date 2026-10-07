# Funcionalidad implementada · Fase `A-EP-028-HU-001-el-capitulo-17-obligatorio` (módulo Estándar en la base)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-001-el-capitulo-17-obligatorio` |
| **Módulo** | Estándar en la base, capítulo `17`, y Proyectos (`core/proyectos/`) |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-001 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El capítulo 17 dejó de ser opt-in y rige para todo proyecto con pantallas; `17·I5` pide usar primero lo que trae la plantilla instalada, y nació `17·I7 · La pantalla orienta sola`. El ajuste `opt_in_17` salió del catálogo y de la base, la línea del 17 salió de la plantilla del `CLAUDE.md`, y un `CLAUDE.md` viejo ya no apaga el 17.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): `proyectos/cimiento/core/herramientas/recuperar.py`, que se agregó al plan antes de tocarlo

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Las reglas `17·I1` a `17·I7` le llegan al agente en toda tarea de cambiar código, en todo proyecto. El capítulo se lee con `manage.py ver_estandar base/17-interfaz.md` o en el menú «Estándar».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Del `CLAUDE.md` solo cuentan los capítulos que siguen siendo opt-in | Un `CLAUDE.md` viejo dice «no» en el 17, que ya rige siempre | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El mapa de tareas se rearmó solo al aprobar la propuesta 7.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar `manage.py migrate proyectos` (hecho en esta máquina el 2026-10-07).
