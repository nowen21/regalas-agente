# Funcionalidad implementada · Fase `A-EP-005-HU-026-temas-por-archivo` (módulo Enganches de reglas: `proyectos/cimiento/core/herramientas/`, y `base/tareas.md` por propuesta)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-026-temas-por-archivo` |
| **Módulo** | Enganches de reglas: `proyectos/cimiento/core/herramientas/`, y `base/tareas.md` por propuesta |
| **Especificación del módulo** | Los CA de la [HU-026](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-026 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al escribir código, el enganche de antes de la acción mira la ruta del archivo y, con la tabla de temas de `base/tareas.md`, entrega solo las reglas de `cambiar-codigo` de los capítulos que ese archivo toca, más las de `todos`. El archivo que no encaja, o un estándar sin la tabla, recibe todas. Lo entregado se cuenta por tarea y temas, así que una vista recibe sus temas aunque antes se haya escrito una prueba. La tabla quedó como propuesta 19.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Funcional | `core/herramientas/entrega_de_reglas.py` (`leer_temas`, `capitulos_del_archivo`, `para_la_accion`) | ✅ | CP-001, CP-002 |
| CA-02 | Funcional | `core/herramientas/entrega_de_reglas.py` (`capitulos_del_archivo` devuelve `None`) | ✅ | CP-003 |
| CA-03 | Documental | Propuesta 19, texto en `historico-chat/scripts/2026-10-09/tareas-con-temas.txt` | ✅ | CP-004 |

**Faltantes / diferimientos:** la tabla rige cuando el usuario apruebe las propuestas 18 y 19, y después se sube la versión.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple: 4 de 4 casos |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

No se usa a mano. Para cambiar qué reglas recibe cada tipo de archivo se cambia la tabla «Los temas de `cambiar-codigo`» de `base/tareas.md`, con una propuesta en Cimiento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Lo entregado se cuenta por tarea y temas | Con una sola cuenta por tarea, escribir una prueba dejaba sin sus temas al `views.py` siguiente | No hace falta: está en el plan, §2.6 |

## 6. Deuda técnica y pendientes generados

El tema `todos` pesa unos 20 KB y llega con cualquier archivo de código; si sigue siendo mucho, se ajusta en la misma tabla.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
