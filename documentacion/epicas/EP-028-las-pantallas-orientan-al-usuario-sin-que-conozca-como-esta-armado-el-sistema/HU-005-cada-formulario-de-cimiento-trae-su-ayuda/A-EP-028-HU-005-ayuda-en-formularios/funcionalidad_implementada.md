# Funcionalidad implementada · Fase `A-EP-028-HU-005-ayuda-en-formularios` (módulo Ayuda de Cimiento: `core/ayuda/` y las plantillas de formulario)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-005-ayuda-en-formularios` |
| **Módulo** | Ayuda de Cimiento: `core/ayuda/` y las plantillas de formulario |
| **Especificación del módulo** | Los CA de la [HU-005](../HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-005 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Los 13 formularios de Cimiento que no tenían ayuda ya la traen: cada campo tiene su «?» con explicación y ejemplo, y cada pantalla con formulario sus botones de ayuda («¿Para qué sirve?»). El formulario del proyecto escoge la clave de cada campo con una plantilla parcial: los datos del proyecto usan «proyecto.*» y sus ajustes la misma ayuda de «Configuración».

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): `_ayuda_del_campo.html` y `core/consumo/tests_tablero.py`, que se agregaron al plan antes de tocarlos

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El «?» junto a cada campo abre su globo; los botones debajo del título de cada pantalla abren su ayuda.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Los ajustes del proyecto usan la ayuda de «Configuración» | Es el mismo ajuste en otra capa; se descartó escribir el texto dos veces | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Los textos de ayuda en `core/ayuda/textos.py`.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
