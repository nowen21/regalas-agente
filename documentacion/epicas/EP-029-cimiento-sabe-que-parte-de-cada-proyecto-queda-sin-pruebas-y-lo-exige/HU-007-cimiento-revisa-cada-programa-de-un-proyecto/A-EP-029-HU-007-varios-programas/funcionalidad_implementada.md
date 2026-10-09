# Funcionalidad implementada · Fase `A-EP-029-HU-007-varios-programas` (módulo Pruebas de Cimiento: `core/pruebas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-007-varios-programas` |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/` |
| **Especificación del módulo** | Los CA de la [HU-007](../HU-007-cimiento-revisa-cada-programa-de-un-proyecto.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-007 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 59.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Cimiento encuentra todos los programas de un proyecto (`reconocer_todos`), como el frente y el servidor de RNI, y no cuenta aparte lo que vive adentro de un programa Django, Laravel o Angular. Cada revisión guarda una fila por programa con la misma fecha y el nombre de su carpeta. La lista muestra el programa con menos pruebas y todos los lenguajes del proyecto; el detalle muestra cada programa. El instalador pone la herramienta en cada programa y el desinstalador la quita de cada uno.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Dominio | `core/pruebas/lenguaje.py` | Hecho | CP-001 |
| CA-02 | Dominio | `core/pruebas/revisar.py`, `core/pruebas/parte.py`, `core/pruebas/models.py`, migración `0004` | Hecho | CP-002 |
| CA-03 | Vista | `core/pruebas/views.py`, `core/pruebas/templates/pruebas/detalle.html` | Hecho | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `models.py` se cambió antes de escribir el plan (H-9); el plan lo declara.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Igual que antes: «Revisar» revisa ahora cada programa del proyecto.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo de adentro de Django, Laravel o Angular es de ese programa | Un `requirements.txt` suelto no es otro programa | Ninguna |
| Las revisiones de una vez comparten la fecha | Sin tabla nueva | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate` y volver a instalar los proyectos con varios programas, para que reciban la herramienta en cada uno.
