# Funcionalidad implementada · Fase `A-EP-025-HU-030-resumen-rapido` (módulo El gasto de Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-030-resumen-rapido` |
| **Módulo** | El gasto de Cimiento, `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | Los CA de la [HU-030](../HU-030-el-resumen-del-gasto-responde-en-la-mitad-del-tiempo-y-no-se-recalcula-con-cada-aviso.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-030 (CA-01 a CA-02) |
| **Fecha de cierre** | 2026-10-09 |
| **Versión del estándar al cerrar** | 56.8.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Las gráficas por día del gasto (`por_dia_por_tipo` y `por_dia`) suman en la base agrupando por hora en UTC, y Python pasa cada hora a su día local: el Resumen bajó de 1,1-1,3 s a 0,28-0,41 s. La pantalla junta los avisos del vigilante: se refresca sola como máximo cada 30 segundos, no se refresca escondida y se refresca una vez al volver si llegó algo; el botón «Actualizar» sigue inmediato.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Lógica | `core/consumo/tablero.py` (`_por_dia_y_tipo`) | ✅ | CP-001, CP-002 |
| CA-02 | Pantalla | `core/consumo/templates/consumo/tablero.html` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

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

Sin cambios para quien la usa: la pantalla del gasto, `/gasto/`. El refresco automático llega como máximo cada 30 segundos; el botón «Actualizar» trae lo último en el momento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Agrupar por hora en UTC y no por día | MySQL de WAMP no tiene zonas horarias: `CONVERT_TZ` da vacío y agrupar por día local no sirve | `S-363` |

## 6. Deuda técnica y pendientes generados

En una zona horaria con media hora de diferencia con UTC, una llamada de esa media hora caería en el día vecino. Cimiento corre en Colombia.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

La HU-030 en la tabla de la EP-025; el README de la carpeta de la HU.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: llega a los proyectos con Cimiento.
