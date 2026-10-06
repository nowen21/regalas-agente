# Funcionalidad implementada · Fase `A-EP-025-HU-013-tres-capas` (módulo `proyectos/cimiento/core/proyectos/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-013-tres-capas` |
| **Módulo** | `proyectos/cimiento/core/proyectos/` |
| **Especificación del módulo** | Los CA de la [HU-013](../HU-013-cada-proyecto-tiene-su-configuracion-en-tres-capas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-013 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 55.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Los ajustes van en tres capas: el de fábrica, el de la base de Cimiento en «Configuración» y el del proyecto en su formulario. Son «Rutas en los avisos» y los dos límites de tokens, que dejaron de ser columnas del proyecto. Una regla, o el freno entero, se suspende en «Suspensiones» con motivo y hasta 30 días, y se levanta con un botón; el núcleo y el histórico no. Los enganches leen todo sin Django; el freno aplica lo suspendido. Cada cambio escribe la copia `.agente/configuracion.md` en el proyecto. El aviso por límite vive en `core/`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa y pantallas | `proyectos/cimiento/core/proyectos/ajustes.py`, `proyectos/cimiento/core/proyectos/models.py`, `proyectos/cimiento/core/proyectos/migrations/0004_tres_capas.py`, `proyectos/cimiento/core/enganches/configuracion.py`, `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/urls.py`, las plantillas, `proyectos/cimiento/templates/base.html` | ✅ | CP-001 |
| CA-02 | Programa y pantallas | `proyectos/cimiento/core/proyectos/views.py`, `proyectos/cimiento/core/proyectos/forms.py`, `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html`, `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/enganches/freno.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/proyectos/copia.py`, `proyectos/cimiento/core/enganches/niveles.py`, `proyectos/cimiento/core/enganches/presupuesto.py`, `adaptadores/claude-code/hook_presupuesto.py` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `tests_analisis_prendido.py` y `tests_vigilante.py` se declararon durante la fase, al ver que tumbaban a las pruebas que corren después.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

1. «Configuración» en el menú: el valor común de cada ajuste.
2. «Proyectos» → «Editar»: el valor propio del proyecto; vacío, usa el de «Configuración».
3. «Proyectos» → «Suspensiones»: suspender una regla o el freno entero, con motivo y vencimiento, y «Levantar» para terminarla antes.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se suspende una regla o el freno entero, no cualquier enganche | El acuerdo habla del que frena; los demás solo informan | No hace falta: está en `ajustes.py` |
| Las suspensiones no se borran: se levantan | Son la historia de por qué algo pasó | No hace falta: está en el modelo |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El menú de Cimiento suma «Configuración».

## 8. Despliegue, si aplica  ·  `13·DOC4`

`preparar_base` aplica la `0004`.
