# Funcionalidad implementada · Fase `A-EP-027-HU-003-todo-pasa-por-las-tablas` (módulo Estándar en la base: `core/estandar/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-003-todo-pasa-por-las-tablas` |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-003](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-003 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Todo cambio de un documento pasa por las tablas. Guardar desde la pantalla, aprobar una propuesta y sincronizar con git llevan cada regla del texto a su fila y guardan el texto armado desde las tablas. Ese texto es el que leen el agente, el freno y `ver_estandar`, sin demora, porque se guarda donde ya leían.

Quitar un documento, o sacar una regla del texto, deja la regla sin documento: no se borra. En una instalación nueva, `importar_estandar` pasa las reglas a las tablas después de importar.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · Cambiar un documento pasa por las tablas | CA | `core/estandar/cambios.py` (`guardar_documento`), `importar.py` (`sincronizar`), `reglas.py` (`pasar_y_armar`) | Hecho | CP-001 |
| CA-02 · Nada se borra | CA | `cambios.py` (`quitar_documento`), `importar.py`, `reglas.py` (`soltar_reglas`) | Hecho | CP-002 |
| CA-03 · El agente recibe el texto armado | CA | El texto armado se guarda en `estandar_documento` | Hecho | CP-003 |
| RNF-01 · Sin demora | RNF | Los enganches leen lo de siempre | Hecho | §3 del resultado |

**Faltantes / diferimientos:** ninguno. Dejar de guardar `base/reglas-por-tarea/` (acuerdo 1) costaba 0,8 s por mensaje; el usuario decidió el 2026-10-07 que siguen guardadas, armadas desde las tablas.

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `importar_estandar.py` se declaró en el plan antes de tocarlo.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Igual que antes: «Cambiar el texto», «Propuestas» y `sincronizar_estandar`. Lo que cambia es que las tablas quedan al día solas.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El texto armado se guarda en el documento | Los enganches leen sin Django en cada mensaje; se descartó armarlo al leer | Ninguna |
| `importar()` no cambia; el comando pasa las reglas después | Sus pruebas comparan el texto recién importado | Ninguna |

## 6. Deuda técnica y pendientes generados

Sincronizar con git ve diferencias en los documentos cuyas notas pasaron a la historia: guarda el texto de git y lo vuelve a armar igual. No cambia nada, pero sube una versión.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
