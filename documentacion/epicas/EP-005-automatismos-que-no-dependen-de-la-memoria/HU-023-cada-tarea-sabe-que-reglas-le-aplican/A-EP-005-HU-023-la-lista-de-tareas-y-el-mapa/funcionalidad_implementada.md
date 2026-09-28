# Funcionalidad implementada · Fase `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-023-la-lista-de-tareas-y-el-mapa` |
| **Módulo** | Cuerpo de reglas y `validadores/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-03 de [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-023 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.2.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Existe la lista cerrada de diez tareas en `base/tareas.md`. Una regla dice a qué tareas aplica con la línea `**Aplica a:**`, que no cuenta para su largo ni anula su checklist. `validadores/mapa_tareas.py` lee esas líneas y escribe `base/mapa-de-tareas.md`, con cada tarea y el enlace a sus reglas. Las diez reglas del núcleo ya tienen su línea.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · lista cerrada de tareas en `base/` | doc | `base/tareas.md` | ✅ | CP-001 |
| RN-02 · la línea `**Aplica a:**` fuera del cuerpo | código | `validadores/metareglas.py`, `_FUERA_DEL_CUERPO` | ✅ | CP-002 |
| RN-03 · el mapa lo escribe un programa | código | `validadores/mapa_tareas.py` y `base/mapa-de-tareas.md` | ✅ | CP-003 |

**Faltantes / diferimientos:** RN-04, el validador, es de la fase `B`.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | La lista de tareas | ✅ hecha | `base/tareas.md` | CP-001 |
| T-02 | `**Aplica a:**` en `_FUERA_DEL_CUERPO` | ✅ hecha | `validadores/metareglas.py` | CP-002 |
| T-03 | Anotar `N1` a `N10` | ✅ hecha | `base/00-nucleo-blindado.md` | CP-002 |
| T-04 | El programa del mapa | ✅ hecha | `validadores/mapa_tareas.py` | CP-003 |
| T-05 | Sus pruebas | ✅ hecha | `validadores/tests/test_cada_tarea_sabe_que_reglas_le_aplican.py`, 8 pruebas | CP-003 |
| T-06 | Correr el programa | ✅ hecha | `base/mapa-de-tareas.md` | CP-003 |
| T-07 | Versión 39.2.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-004 |
| T-08 | Actualizar HU-023 y el pendiente 100 | ✅ hecha | HU-023 y `pendientes/100-...md` | — |

**Correspondencia con el plan:** 8 tareas en el plan, 8 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `anatomia/que-esta-amarrado-a-la-herramienta.md`. La prueba del mapa del amarre exige que todo programa de `validadores/` esté clasificado, y `mapa_tareas.py` es nuevo (DEF-02).

**Esfuerzo real contra estimado:** cerca de 1,5 h contra 4,1 h del plan. El mecanismo para dejar la línea fuera del cuerpo ya existía.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: las 8 pruebas nuevas y las 74 de los módulos que usan `metareglas.py`, en OK; `metareglas`, `estandar` y `ejecutable` sin incumplimientos; `versionado` y `fases` sin fallas. Las del amarre bajan de 4 fallas a 3; las 3 que quedan son de dos programas que no son de esta fase.
- Verificaciones manuales: `mapa_tareas.py` clasificado en el mapa del amarre.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Punto de entrada: `python validadores/mapa_tareas.py` escribe el mapa. Se corre cada vez que una regla cambia su línea `**Aplica a:**`.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La lista y el mapa en archivos distintos | La lista la decide una persona y el mapa lo escribe un programa; juntos, el programa pisaría la lista | En el plan §2.6 |
| El mapa escribe «[`00·N1`](enlace): nombre» y no con `·` entre los dos | En una lista el punto medio es prosa, y es marca de `ID8` | En el comentario de `mapa_tareas.py` |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino (fase futura / ticket / `pendientes/`) |
|---|---|---|
| Anotar las 242 reglas vigentes restantes y el validador que exige la línea | Diferido por el plan | Fase `B` de HU-023 |
| El validador del amarre da por clasificado un programa con solo nombrarlo | Salió al corregir el DEF-02 | Fase `B` de HU-023, por decisión del usuario (H-8 del resumen del 2026-09-28) |

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa del amarre con `mapa_tareas.py`.
- [x] Índice de la épica con HU-023.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: el mapa entra con la versión 39.2.0, y los proyectos lo reciben al actualizar el estándar.
