# Funcionalidad implementada · Fase `A-EP-025-HU-004-niveles-por-proyecto` (módulo `proyectos/cimiento/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-004-niveles-por-proyecto` |
| **Módulo** | `proyectos/cimiento/` |
| **Especificación del módulo** | Los CA de la [HU-004](../HU-004-cada-regla-tiene-su-nivel-en-cada-proyecto.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-004 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Reglas» en cada fila de la lista de proyectos abre las reglas de `base/` por capítulo, sin las del núcleo ni las derogadas, con su nivel en ese proyecto: frena, avisa o apagada. Un administrador lo cambia y el cambio queda en el historial con la cuenta y la fecha; el grupo consulta solo lo ve. Sin nivel guardado, la regla frena.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/niveles/models.py`, `proyectos/cimiento/core/niveles/catalogo.py`, `proyectos/cimiento/core/niveles/views.py`, `proyectos/cimiento/core/niveles/templates/niveles/reglas.html` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/niveles/catalogo.py`, `proyectos/cimiento/core/niveles/views.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/niveles/models.py`, `proyectos/cimiento/core/niveles/templates/niveles/historial.html` | ✅ | CP-003 |
| CA-04 | Programa | `proyectos/cimiento/core/niveles/views.py`, `proyectos/cimiento/core/niveles/templates/niveles/reglas.html` | ✅ | CP-004 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 7 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`/proyectos/«id»/reglas/` y su historial. Para el freno (HU-005): la tabla `niveles_nivelderegla` tiene una fila por regla cambiada, con `proyecto_id`, `regla` (`02·F8`) y `nivel`; sin fila, la regla frena.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Solo se guarda lo que alguien cambió | Sin fila, la regla frena como siempre; la tabla queda corta | No hace falta: está en el modelo |
| Un envío con una regla fuera del catálogo no guarda nada | Todo o nada, y el núcleo no se toca por ningún camino | No hace falta |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`preparar_base` crea las tablas al instalar el estándar.
