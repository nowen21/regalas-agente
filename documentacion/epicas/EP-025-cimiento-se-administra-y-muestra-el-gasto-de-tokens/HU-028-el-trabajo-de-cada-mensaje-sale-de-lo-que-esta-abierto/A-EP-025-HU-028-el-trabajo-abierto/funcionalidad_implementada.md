# Funcionalidad implementada · Fase `A-EP-025-HU-028-el-trabajo-abierto` (módulo El gasto: `core/consumo/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-028-el-trabajo-abierto` |
| **Módulo** | El gasto: `core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-028](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-028 (CA-01, CA-02, CA-03, CA-04) |
| **Fecha de cierre** | 2026-10-08 |
| **Versión del estándar al cerrar** | 58.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El trabajo de cada mensaje sale de tres fuentes, en orden:

1. **El análisis prendido.** El lector toma del aviso «[ANÁLISIS EN CURSO]», que ya queda en el `.jsonl` justo después de cada mensaje, el análisis al que entra la conversación. No se agregó texto a ningún aviso.
2. **Lo que tocó el turno.** Las rutas de las herramientas de archivos, y ahora también las órdenes de consola. Se reconocen las fases de cualquier letra, no solo las `A-`.
3. **La conversación.** El mensaje que no da trabajo por sí mismo (una pregunta, un «Apruebo») toma el del mensaje anterior de la misma sesión. Si después su turno toca algo, eso lo reemplaza.

Cada mensaje guarda de dónde salió su trabajo (`Pedido.origen`). En «Actividad», el que viene de la conversación lleva al lado «sigue la conversación». El «?» de «Trabajo» explica las tres fuentes. `manage.py recalcular_trabajo` aplicó todo esto a lo ya guardado: en la última semana, los mensajes sin trabajo bajaron del 93 % al 30 %.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · El análisis prendido es el trabajo del mensaje | CA | `core/consumo/trabajo.py`, `core/consumo/lector.py`, `core/consumo/guardar.py` | Hecho | CP-001 |
| CA-02 · Se reconocen todas las fases y las órdenes de consola | CA | `core/consumo/trabajo.py`, `core/consumo/lector.py` | Hecho | CP-002 |
| CA-03 · El mensaje sin rastro sigue en el trabajo de la conversación | CA | `core/consumo/guardar.py`, `core/consumo/models.py`, migración `0006`, `_actividad.html`, `tablero.py` | Hecho | CP-003 |
| CA-04 · Lo ya guardado se recalcula | CA | `core/consumo/management/commands/recalcular_trabajo.py` | Hecho | CP-004 |
| RNF-01 · Sin texto nuevo en los avisos | RNF | `core/consumo/lector.py` | Hecho | CP-001 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `tests_segunda_tanda.py` estaba declarado por si cambiaba, y no hizo falta.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Gasto de tokens → «Dónde se gasta» → Trabajo, y «Actividad». Después de instalar el cambio en otra máquina: `manage.py migrate` y `manage.py recalcular_trabajo` una vez, y reiniciar el vigilante del consumo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El análisis se lee del aviso que ya está en el `.jsonl` | Se descartó agregar una línea de trabajo al aviso de cada mensaje: costaría tokens en cada mensaje | Ninguna |
| La fase de un mensaje sin rastro sale de la conversación, no del freno | El freno solo corre cuando hay acciones, y entonces ya hay rutas; además hay varias fases abiertas a la vez, de otras sesiones | Ninguna |

## 6. Deuda técnica y pendientes generados

Quedan sin trabajo 597 de 1.983 mensajes de 7 días (30 %): no tocaron nada ni seguían una conversación con trabajo.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate consumo`, `manage.py recalcular_trabajo` y reiniciar el vigilante del consumo (`vigilar_consumo`): el que está corriendo usa el código de antes.
