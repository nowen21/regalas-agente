# Funcionalidad implementada · Fase `A-EP-023-HU-002-cada-punto-dice-de-donde-sale` (módulo cuerpo de reglas, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-002-cada-punto-dice-de-donde-sale` |
| **Módulo** | Cuerpo de reglas (`base/`), `plantillas/` y `validadores/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-05 de la [HU-002](../HU-002-cada-documento-sale-del-anterior.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-002 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 42.0.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Cada punto de un documento de la cadena tiene que decir de qué punto del anterior sale (`02·F27`), y `validar.py origen` lo comprueba en las épicas que nacen de un análisis. Si cambia la necesidad, el cambio se escribe primero donde nace y baja en orden (`02·F28`). La plantilla de la HU distingue de dónde sale el contexto y trae «Sale de» en cada criterio.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01, RN-02, RN-05: cada punto cita su origen; lo que no lo tiene no entra | Regla y validador | `F27`, `validadores/origen.py` | ✅ | CP-001 a CP-003 |
| RN-03: el cambio baja en orden | Regla | `F28` | ✅ | CP-004 |
| RN-04: la regla nueva extiende `F18`, y `F18` no se toca | Regla | `F27` | ✅ | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `F27` | ✅ hecha | `base/02-flujo-de-trabajo/reglas/F27-…`, `base.md` | CP-001 |
| T-02 | El validador | ✅ hecha | `validadores/origen.py` | CP-002, CP-003 |
| T-03 | Subcomando `origen` | ✅ hecha | `validadores/validar.py` | CP-003 |
| T-04 | Las pruebas | ✅ hecha | `validadores/tests/test_origen.py` | CP-002 |
| T-05 | Los registros | ✅ hecha | `reglas-validables.md`, `anatomia/` | CP-006 |
| T-06 | `F28` | ✅ hecha | `base/02-flujo-de-trabajo/reglas/F28-…`, `base.md` | CP-004 |
| T-07 | El contexto de la plantilla | ✅ hecha | `plantillas/ciclo-vida-proyectos/04-HU.md` | CP-005 |
| T-08 | Reglas por tarea y versión | ✅ hecha | `base/mapa-de-tareas.md`, `base/reglas-por-tarea/`, `VERSION`, `CHANGELOG.md` | CP-006 |
| T-09 | «Sale de» en los criterios de la plantilla | ✅ hecha | `plantillas/ciclo-vida-proyectos/04-HU.md` | CP-005 |

**Correspondencia con el plan:** 9 tareas en el plan, 9 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió. El plan estimaba 7,1 horas.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas: `test_origen`, `test_analisis` y la suite del estándar; `validar.py origen`, `estandar`, `metareglas`, `tareas`, `amarre`, `version` y `flujo`; la medición de marcas.
- Verificaciones manuales: el validador encuentra EP-023 y ninguna otra épica.
- Defectos abiertos que se aceptaron: ninguno de esta fase. La suite del estándar deja una falla que ya existía, del pendiente 103 sin su fila «Historia de usuario», que resuelve la HU-003.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python validadores/validar.py origen`. También corre con `validar.py todo`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El validador solo revisa las épicas que nacen de un análisis | Las anteriores nacieron sin la regla y no se reabren (`20·M10`); revisar todas daba 160 fallas que nadie puede corregir sin reabrir | Por escribir |
| Solo se revisan los análisis aprobados | El abierto todavía se está llenando | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Índice del capítulo 02.
- [x] `base/mapa-de-tareas.md` y `base/reglas-por-tarea/`.
- [x] `anatomia/mapa-del-sitio.md` y el mapa del amarre.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto adopta la 42.0.0 con el instalador.
