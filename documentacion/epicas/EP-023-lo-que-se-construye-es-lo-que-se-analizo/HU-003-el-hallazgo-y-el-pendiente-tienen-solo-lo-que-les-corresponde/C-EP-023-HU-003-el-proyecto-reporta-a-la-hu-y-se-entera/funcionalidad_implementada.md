# Funcionalidad implementada · Fase `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera` (módulo `validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-023-HU-003-el-proyecto-reporta-a-la-hu-y-se-entera` |
| **Módulo** | `validadores/` |
| **Especificación del módulo** | El CA-10 y el CA-11 de la [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 (CA-10 y CA-11) |
| **Fecha de cierre** | 2026-10-03 |
| **Versión del estándar al cerrar** | 53.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El pendiente que reporta un proyecto nace en la HU que citan la regla o el programa que fallan, o en el resumen del día. Al anotar el commit de la fase que cumple su plan, `aviso_resuelto.py` sigue los enlaces y deja `aviso-resuelto.md` al lado del seguimiento del proyecto. El seguimiento cierra cuando el proyecto pone la fecha en «Comprobado».

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-10 | Regla y plantillas | `02·F24`, `plantillas/pendiente-reportado.md`, `plantillas/pendiente-de-seguimiento.md` | ✅ | CP-001 |
| CA-11 | Programas y enganche | `validadores/aviso_resuelto.py`, `validadores/pendientes.py`, `adaptadores/claude-code/hook_estacion.py` | ✅ | CP-002, CP-003 |

**Faltantes / diferimientos:** la regla que obliga a pasar el pendiente a su versión siguiente espera la aprobación del análisis 14.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `validadores/tests/test_el_pendiente_tiene_solo_lo_suyo.py`, bajo la fila 8 del análisis 14 del pendiente 103; y `base/reglas-por-tarea/trabajar-cadena-1.md`, donde `mapa_tareas.py` copió `02·F24` (el plan nombró `trabajar-cadena-2.md`), bajo la fila 9.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

El aviso sale solo, desde el enganche de después del commit. El proyecto que lo recibe comprueba la corrección y cambia «no» por la fecha en la línea «Comprobado».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El seguimiento se encuentra siguiendo los enlaces, sin campo nuevo | El pendiente del estándar ya enlaza el hallazgo, y el hallazgo su pendiente | No hace falta: está en el código |
| Un aviso ya escrito no se vuelve a escribir | Así no se pisa la fecha que puso el proyecto | No hace falta: está en el código |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `anatomia/mapa-del-sitio.md`.
- [x] `base/reglas-por-tarea/` y `base/mapa-de-tareas.md`, regenerados.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 53.0.0.
