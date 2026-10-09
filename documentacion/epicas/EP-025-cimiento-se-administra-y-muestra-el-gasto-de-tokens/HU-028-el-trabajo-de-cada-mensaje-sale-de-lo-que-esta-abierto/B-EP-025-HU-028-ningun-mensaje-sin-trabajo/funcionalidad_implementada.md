# Funcionalidad implementada · Fase `B-EP-025-HU-028-ningun-mensaje-sin-trabajo` (módulo El gasto: `core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-028-ningun-mensaje-sin-trabajo` |
| **Módulo** | El gasto: `core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-028](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-028 (CA-05) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El diagnóstico (`historico-chat/scripts/2026-10-08/diagnostico_sin_trabajo.py`) encontró dos causas de «(sin trabajo)»:

1. **Faltaban las líneas de sesión.** El vigilante del consumo corre desde el 2026-10-05 con el código de antes de la HU-025, y no guardó ninguna línea desde el 2026-10-06. Sin líneas no se podía recalcular nada. Se trajeron con `leer_consumo --desde-cero`.
2. **Trabajo hecho por fuera de la cadena.** Conversaciones que nunca abrieron una fase ni un análisis, y los primeros mensajes de las demás.

Para la segunda, el trabajo tiene una cuarta fuente: la conversación misma, «Conversación «título»», con el título que Claude Code le pone (la línea `ai-title` del `.jsonl`). Si el título todavía no llega, queda el comienzo del código y se cambia cuando llega. `recalcular_trabajo` le pone su conversación también al mensaje cuyo `.jsonl` ya no existe. En la base real quedan 0 de 3.669 mensajes sin trabajo.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-05 · Ningún mensaje queda sin trabajo | CA | `core/consumo/trabajo.py`, `core/consumo/lector.py`, `core/consumo/guardar.py`, `core/consumo/management/commands/recalcular_trabajo.py`, `core/ayuda/textos.py` | Hecho | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. No hizo falta un campo nuevo ni migración, ni tocar `tablero.py`, `_actividad.html` ni `_donde.html`, que estaban declarados por si acaso.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Gasto de tokens → «Dónde se gasta» → Trabajo. Lo que aparece como «Conversación ...» es gasto hecho por fuera de una fase o un análisis.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Los primeros mensajes de una conversación quedan en su título, no en la fase que aparece después | Una conversación puede cambiar de tema; pasarle hacia atrás la fase de después la culparía de un gasto que no fue suyo | Ninguna |
| El título se toma del `.jsonl`, no se le pide al usuario | Claude Code ya lo escribe en cada conversación; no cuesta nada | Ninguna |

## 6. Deuda técnica y pendientes generados

El vigilante que corre usa el código viejo hasta reiniciarlo. Mientras tanto, los mensajes nuevos entran sin sus líneas y con la regla vieja; `recalcular_trabajo` los arregla después de traer las líneas.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Reiniciar el vigilante del consumo, después `manage.py leer_consumo --desde-cero` y `manage.py recalcular_trabajo`.
