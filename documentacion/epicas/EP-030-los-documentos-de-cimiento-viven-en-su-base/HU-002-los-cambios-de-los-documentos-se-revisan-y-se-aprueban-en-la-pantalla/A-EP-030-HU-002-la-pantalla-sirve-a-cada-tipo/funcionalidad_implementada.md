# Funcionalidad implementada · Fase `A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo` (módulo Estándar de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-030-HU-002-la-pantalla-sirve-a-cada-tipo` |
| **Módulo** | Estándar de Cimiento, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-los-cambios-de-los-documentos-se-revisan-y-se-aprueban-en-la-pantalla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-002 (CA-01, CA-02) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La pantalla «Estándar → Propuestas», que ya mostraba el antes y el después y aprobaba con un botón, deja de conocer los tipos a mano: `cambios.aplicar` y `cambios.actual_de` le preguntan al tipo que atiende la propuesta (`documentos.de_la_propuesta`), y cada tipo trae su `actual` y su `aplicar`. Un tipo que se registre en el camino único se revisa y se aprueba en la misma pantalla sin código aparte.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `core/estandar/documentos.py` (`actual`), `cambios.actual_de` | Hecho | EV-01 |
| CA-02 | Funcional | `core/estandar/documentos.py` (`aplicar`, `de_la_propuesta`), `cambios.aplicar` | Hecho | EV-01 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Cimiento → Estándar → Propuestas: cada propuesta muestra lo que sale y lo que entra, y se aprueba o se rechaza con su botón.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se reusó la pantalla de propuestas | Ya mostraba el antes y el después y aprobaba con un botón (EP-026·HU-005, EP-028·HU-004) | S-359 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Nada.
