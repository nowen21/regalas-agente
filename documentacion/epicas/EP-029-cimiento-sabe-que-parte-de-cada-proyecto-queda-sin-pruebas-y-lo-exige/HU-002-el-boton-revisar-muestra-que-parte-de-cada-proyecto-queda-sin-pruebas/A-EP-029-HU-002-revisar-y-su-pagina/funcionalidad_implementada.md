# Funcionalidad implementada · Fase `A-EP-029-HU-002-revisar-y-su-pagina` (módulo Pruebas de Cimiento: `core/pruebas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-002-revisar-y-su-pagina` |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/`, con su entrada en el menú |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1, con la sección del manual que agregó el análisis 3 del pendiente 141 |
| **HU / CA cubiertas** | HU-002 (CA-01 a CA-04) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Revisión de pruebas», en el menú, muestra todos los proyectos registrados: en qué están hechos, su última revisión, qué parte tiene pruebas y si la revisión está al día, vencida o nunca se hizo. El botón «Revisar» arranca `manage.py revisar_pruebas` en otro proceso; mientras corre, la fila dice «Revisando» y la página se recarga sola cada 15 segundos. Cimiento reconoce el lenguaje por los archivos del proyecto y revisa con coverage.py (Python y Django, con el Python del proyecto), PHPUnit con PCOV (Laravel) o `ng test --code-coverage` (Angular). El detalle de cada proyecto lista sus archivos del que tiene menos pruebas al que tiene más, y deja borrar una revisión.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Dominio | `core/pruebas/lenguaje.py`, `core/pruebas/revisar.py` | Hecho | CP-001, CP-002 |
| CA-02 | Dominio | `core/pruebas/revisar.py` | Hecho | CP-003 a CP-005 |
| CA-03 | Vista y orden | `core/pruebas/views.py`, `core/pruebas/management/commands/revisar_pruebas.py` | Hecho | CP-006, CP-007 |
| CA-04 | Pantallas | `core/pruebas/templates/pruebas/`, `templates/base.html`, `core/ayuda/` | Hecho | CP-008, CP-009 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. La sección del manual faltaba en el plan (H-3 del 2026-10-07) y la agregó el análisis 3 del pendiente 141 antes de escribirla.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

«Revisión de pruebas» en el menú, o «Pruebas» en cada proyecto de «Todos los proyectos». Desde la consola: `python manage.py revisar_pruebas --proyecto «nombre»` o `--todos`. La sección «Revisión de pruebas» del manual lo explica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El botón arranca la orden en otro proceso | Una revisión tarda minutos; se descartó revisar dentro de la petición | Ninguna |
| Se usa el Python del proyecto | Sus pruebas necesitan sus dependencias; se descartó el de Cimiento | Ninguna |
| Angular se lee del resumen que imprime | Su configuración de fábrica solo imprime el resumen | Ninguna |

## 6. Deuda técnica y pendientes generados

- Angular guarda solo el total, no los archivos: su configuración de fábrica no los deja. Su detalle muestra el porcentaje sin lista de archivos.
- El pendiente 143, ajeno a esta fase (H-4).

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El menú (`templates/base.html`), la sección del manual (`core/ayuda/secciones.py`) y las listas de pantallas de las pruebas del menú, las tablas y la ayuda.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate` en la máquina de Cimiento.
