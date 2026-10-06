# Funcionalidad implementada · Fase `B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos` (módulo Cimiento)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos` |
| **Módulo** | Cimiento, `core/herramientas/` |
| **Especificación del módulo** | Los CA de la [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-024 () |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 55.6.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`RecuperadorDeReglas.como_texto` no devuelve nada ante un aviso interno de Claude Code: el agente ya no recibe reglas ni el aviso de `01·C28` por algo que el usuario no escribió.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|


**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 2 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Nada que hacer: lo aplica el enganche de reglas en cada mensaje.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| `recuperar.py` usa `es_aviso_interno` de `historico.py` | Las marcas viven en un solo sitio | S-322 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
