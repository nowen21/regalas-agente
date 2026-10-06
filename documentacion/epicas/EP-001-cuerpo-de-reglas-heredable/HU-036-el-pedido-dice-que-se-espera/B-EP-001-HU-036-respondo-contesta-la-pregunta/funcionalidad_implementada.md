# Funcionalidad implementada · Fase `B-EP-001-HU-036-respondo-contesta-la-pregunta` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-036-respondo-contesta-la-pregunta` |
| **Módulo** | Cuerpo de reglas, capítulo `01 · Conducta del agente` |
| **Especificación del módulo** | Los CA de la [HU-036](../HU-036-el-pedido-dice-que-se-espera.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-036 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.1.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

La tabla de las palabras que mandan sobre el trabajo, en `base/01-conducta/palabras-clave.md`, suma «Respondo»: contestar la pregunta del agente, y nada más. El enganche de reglas la reconoce sin tocar código y no le da tarea propia.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


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

Abrir el mensaje con «Respondo» para contestar una pregunta del agente.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Ninguna | No hubo decisiones nuevas; las de la fase salen de los acuerdos del análisis 1 del pendiente 131 | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

`README.md` de HU-036 con la fila de la fase B; CHANGELOG y `VERSION` en 56.1.0.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
