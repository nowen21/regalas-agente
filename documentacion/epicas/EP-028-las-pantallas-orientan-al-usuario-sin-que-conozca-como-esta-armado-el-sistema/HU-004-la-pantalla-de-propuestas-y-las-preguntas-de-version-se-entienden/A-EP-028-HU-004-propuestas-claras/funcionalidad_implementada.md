# Funcionalidad implementada · Fase `A-EP-028-HU-004-propuestas-claras` (módulo Estándar en la base: `core/estandar/` y las preguntas de versión de `core/historia/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-004-propuestas-claras` |
| **Módulo** | Estándar en la base: `core/estandar/` y las preguntas de versión de `core/historia/` |
| **Especificación del módulo** | Los CA de la [HU-004](../HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-004 () |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

«Propuestas por aprobar» dice qué hacer, muestra en cada propuesta qué cambia (en rojo lo que sale, en verde lo que entra, con `difflib`), deja ver el texto completo y pide el motivo al rechazar, que queda guardado. Las dos preguntas del tipo de versión, en todos los formularios, se escriben para quien no conoce `20·M10`, tienen su «?» con ejemplos y muestran el tipo que resulta; con «Sí» en la primera, la segunda se oculta. El menú ya no ofrece «Registrar un proyecto» a una cuenta de consulta.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** mostrar la regla por su nombre y no por su ruta queda en la EP-027·HU-005

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna

**Archivos tocados que el plan no declaraba** (`02·F8`): `tests_pantalla.py`, `tests_capitulo17.py`, `templates/base.html` y `core/inicio/pendientes.py`, que se agregaron al plan antes de tocarlos

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Menú «Estándar» → «Propuestas por aprobar». Las preguntas de versión aparecen en todo formulario que sube una versión.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Toda prueba `TransactionTestCase` lleva `serialized_rollback = True` | Sin eso vacía la base y daña las pruebas siguientes | S-349 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La sección «El estándar y la memoria» del manual de ayuda.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Aplicar `manage.py migrate estandar` (hecho en esta máquina el 2026-10-07).
