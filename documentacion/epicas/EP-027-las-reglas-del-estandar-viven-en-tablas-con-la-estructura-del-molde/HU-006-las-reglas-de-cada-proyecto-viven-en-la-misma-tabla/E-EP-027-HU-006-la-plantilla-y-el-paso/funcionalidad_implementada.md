# Funcionalidad implementada · Fase `E-EP-027-HU-006-la-plantilla-y-el-paso` (módulo Plantillas del estándar (`plantillas/`) e instalación (`core/herramientas/`))   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `E-EP-027-HU-006-la-plantilla-y-el-paso` |
| **Módulo** | Plantillas del estándar e instalación |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-05) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La plantilla `CLAUDE.md` dice que las reglas propias de un proyecto registrado viven en Cimiento y llegan como índice al abrir la sesión. El archivo `.agente/reglas-proyecto.md` queda para el proyecto que no está registrado. Cada proyecto se pone al día con el instalador de su próxima sesión, y el estándar subió a la 58.0.0 (MAYOR).

Las reglas de dp_card, Gestión de Servicios Tecnológicos, LocalHub y RNI pasaron a la tabla. Su archivo quedó entero en la historia de cada proyecto y se borró. AgroSystem no pasó: tiene dos reglas P45 (H-26).

Cinco documentos del estándar nombraban el archivo como el sitio de las reglas del proyecto. Su cambio quedó como las propuestas 10 a 14, que esperan la aprobación del usuario.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-05 · La plantilla y el instalador dicen dónde viven | CA | `plantillas/CLAUDE.md.plantilla` (2.1, paso 4, 5.2), `plantillas/reglas-proyecto.md` | Hecho | CP-001, CP-002 |

**Faltantes / diferimientos:** AgroSystem, hasta que se decida su P45; las propuestas 10 a 14, hasta que el usuario las apruebe.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna. La copia de después del paso no se hizo: habría pisado la de antes.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Las reglas de un proyecto se ven y se cambian en Cimiento, menú Estándar, opción Reglas y documentos, tarjeta Reglas de cada proyecto. Un proyecto que se registra lleva las suyas con `manage.py pasar_reglas_proyecto --proyecto <carpeta> --borrar`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Cada proyecto pone al día su `CLAUDE.md` con el instalador de su próxima sesión | Es el camino de siempre y no toca otros repositorios; se descartó correr el instalador desde aquí | Ninguna |
| Los documentos del estándar cambian por propuesta | El estándar se cambia así | Ninguna |

## 6. Deuda técnica y pendientes generados

H-26: la P45 repetida de AgroSystem, que decide el usuario.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Hecho en la base viva: `copiar_base`, `migrate estandar`, `pasar_reglas_proyecto --todos --borrar` y `registrar_version --obliga si`.
