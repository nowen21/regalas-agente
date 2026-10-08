# Funcionalidad implementada · Fase `A-EP-027-HU-002-el-paso` (módulo Estándar en la base: `core/estandar/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-002-el-paso` |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-002](../HU-002-las-269-reglas-pasan-a-las-tablas-sin-perder-nada.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-002 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`manage.py pasar_reglas` pasa cada regla del texto a sus tablas, en una sola versión. Cada regla queda con sus casillas, su capítulo, su documento, su lugar, sus tareas en orden y sus dependencias unidas a su destino. «Validable» se toma de `validadores/reglas-validables.md`. Las 156 notas con fecha del sello pasan a la historia de su regla, con su fecha, y salen del sello. Después, el texto de cada documento se arma desde las tablas.

En la base viva quedaron 270 reglas, en la versión 57.4.0, y lo que recibe el agente no cambió.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · Todas las reglas quedan en las tablas | CA | `core/estandar/reglas.py` (`pasar_documento`, `enlazar_dependencias`, `validables`) | Hecho | CP-001 |
| CA-02 · Nada se pierde | CA | `reglas.py` (`separar_notas`, `_notas_a_la_historia`, `armar_documento`) | Hecho | CP-002 |
| CA-03 · Pasar dos veces no duplica | CA | `reglas.py` (`_guardar`, `_tareas`, `_dependencias`) | Hecho | CP-003 |
| RNF-01 · Todo o nada | RNF | `reglas.py` (`pasar_todo`, en una transacción) | Hecho | CP-001 |
| RNF-02 · Una sola versión | RNF | `management/commands/pasar_reglas.py` | Hecho | §3 del resultado |

**Faltantes / diferimientos:** diez reglas quedan con «validable» sin declarar porque el registro no las nombra: C28, F4.1 a F4.5, G8, DOC8, I7 y M16. Declararlas es de `20·M9`, regla por regla.

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

`manage.py pasar_reglas`. Se puede correr de nuevo: actualiza sin duplicar. Las notas se ven en «Historia», en la tabla de reglas.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La nota es un cambio de la historia de su regla, con la fecha de la nota | La historia ya cuenta cuándo y por qué cambió algo; se descartó una tabla aparte | Ninguna |
| Solo salen del sello los párrafos que abren con negrita y una fecha | El cuerpo también cita fechas, y eso sí es la regla | Ninguna |
| «Validable» se lee con prioridad de la lista de validadores hechos, después la de faltan y después la de no validables | La prosa de una lista nombra reglas de otra | Ninguna |

## 6. Deuda técnica y pendientes generados

- [Pendiente 140](../../../../../historico-chat/resumenes/2026-10-07/pendientes/140-la-regla-opt-in-de-un-capitulo-que-no-es-opt-in-no-se-apaga/pendiente.md): la prueba en rojo de `core.enganches`, que no es de esta fase.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

El mapa de tareas se volvió a armar en la misma versión; no cambió.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Hecho en la base viva: `copiar_base`, `migrate estandar` y `pasar_reglas`.
