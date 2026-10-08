# Funcionalidad implementada · Fase `B-EP-027-HU-006-reglas-en-la-tabla` (módulo Estándar en la base: `core/estandar/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-027-HU-006-reglas-en-la-tabla` |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-02) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Las reglas propias de un proyecto pasan a la tabla de reglas con `manage.py pasar_reglas_proyecto`. Se leen escritas con `##` o con `###`, y quedan con su proyecto, sus casillas y la sección donde iban (casilla «grupo»). Con `--borrar`, el archivo entero queda en la historia del proyecto y se borra. Un archivo con un código repetido no pasa: se dice cuál y el archivo queda.

`manage.py ver_regla --proyecto <carpeta>` da el índice; con un código, la regla entera, y con `--todas`, todas. En «Estándar → Reglas y documentos», la tarjeta «Reglas de cada proyecto» lleva a la pantalla de cada uno. Allí cada regla se lee en su grupo y quien administra las cambia sobre el texto de todas. La regla que sale del texto queda apartada, no se borra.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-02 · Las reglas del proyecto pasan a la tabla sin perder nada | CA | `core/estandar/molde.py` (`nivel_de`, `partir`), `models.py` (`grupo`, `apartada`), `reglas.py`, `pasar_reglas_proyecto.py`, `ver_regla.py`, `views.py` (`ReglasDelProyecto`), `reglas_del_proyecto.html` | Hecho | CP-001 a CP-003 |

**Faltantes / diferimientos:** pasar los cinco proyectos va en la fase E, cuando el agente ya reciba las reglas de la base.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `core/ayuda/textos.py` y `core/ayuda/secciones.py` se declararon en el plan antes de tocarlos.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`manage.py pasar_reglas_proyecto --proyecto <carpeta>` o `--todos`, con `--borrar` para borrar el archivo; `manage.py ver_regla --proyecto <carpeta> [código]`; y la pantalla «Reglas de cada proyecto».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El archivo entero queda como un cambio de la historia del proyecto | Lo que no es regla es casi todo el texto de la plantilla; se descartó una casilla para ese texto | Ninguna |
| Un código repetido detiene el paso de ese proyecto | Pasar perdería una regla; renumerar lo decide el proyecto (`20·M4`) | Ninguna |
| La regla del proyecto que sale del texto queda apartada | No tiene documento del que quedar sin; nada se borra (`20·M11`) | Ninguna |

## 6. Deuda técnica y pendientes generados

H-26: AgroSystem tiene dos P45; lo decide el usuario.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El manual: la pantalla nueva entra a la sección «El estándar y la memoria».

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate estandar` (migración `0007_grupo`).
