# Funcionalidad implementada · Fase `C-EP-027-HU-006-el-agente-las-recibe` (módulo Enganches: `core/enganches/` y su adaptador de arranque (`adaptadores/claude-code/hook_sesion.py`))   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-027-HU-006-el-agente-las-recibe` |
| **Módulo** | Enganches: `core/enganches/` y `adaptadores/claude-code/hook_sesion.py` |
| **Especificación del módulo** | Los CA de la [HU-006](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-006 (CA-03) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Al abrir la sesión de un proyecto que tiene sus reglas en la base de Cimiento llega el índice de esas reglas, con el comando para leer cada una o todas. El freno deja escribir lo que esas reglas autorizan, leído de la tabla con el código de cada regla. Un proyecto sin reglas en la base, o sin base, sigue con su archivo, como antes.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-03 · El agente del proyecto las recibe de la base | CA | `core/enganches/reglas_del_proyecto.py`, `core/enganches/autorizado.py` (`del_proyecto`), `adaptadores/claude-code/hook_sesion.py` | Hecho | CP-001, CP-002 |

**Faltantes / diferimientos:** ninguno de esta fase.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Solo: al abrir la sesión de un proyecto llega el índice de sus reglas propias, con el comando `manage.py ver_regla --proyecto "<carpeta>" <código>`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Llega el índice y no las reglas enteras | Las de AgroSystem ocupan más de 100.000 caracteres y el arranque tiene 10.000; se descartó inyectarlas | Ninguna |
| Sin reglas en la base, el freno lee el archivo | El proyecto no registrado o que aún no pasó sigue funcionando | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: los enganches leen el código de Cimiento en cada llamada.
