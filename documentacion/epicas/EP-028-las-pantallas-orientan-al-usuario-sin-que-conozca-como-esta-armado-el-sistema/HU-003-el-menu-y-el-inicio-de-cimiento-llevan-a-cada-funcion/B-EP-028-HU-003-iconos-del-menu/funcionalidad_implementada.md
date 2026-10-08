# Funcionalidad implementada · Fase `B-EP-028-HU-003-iconos-del-menu` (módulo Cimiento: `templates/base.html` y una plantilla parcial de íconos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-028-HU-003-iconos-del-menu` |
| **Módulo** | Cimiento: el menú |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 (CA-03) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cada entrada principal del menú lleva su ícono de Tabler Icons, en el lugar que le da la plantilla: casa para el inicio, carpetas para los proyectos, libro para el estándar, barras para el gasto, reloj para la historia y signo de pregunta para el manual. Los íconos van como SVG en línea, como en la plantilla Tabler, desde una plantilla parcial (`templates/includes/icono.html`), y el lector de pantalla no los lee: el texto va al lado.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-03 · Cada entrada del menú lleva su ícono | CA | `templates/includes/icono.html`, `templates/base.html` | Hecho | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

La tarea del plan quedó hecha.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Un ícono nuevo se agrega a `templates/includes/icono.html` con su nombre de Tabler Icons y se usa con `{% include "includes/icono.html" with nombre="…" %}`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| SVG en línea desde una plantilla parcial | Es como lo hace la plantilla Tabler y no agrega una dependencia; se descartó instalar el paquete de íconos | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
