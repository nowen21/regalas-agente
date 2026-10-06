# Funcionalidad implementada · Fase `A-EP-025-HU-020-quitar-con-sus-filas` (módulo `proyectos/cimiento/core/herramientas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-020-quitar-con-sus-filas` |
| **Módulo** | `proyectos/cimiento/core/herramientas/andamio.py` |
| **Especificación del módulo** | Los CA de la [HU-020](../HU-020-lo-que-crea-el-andamio-se-puede-quitar.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-020 (CA-01 a CA-03) |
| **Fecha de cierre** | 2026-10-05 |
| **Versión del estándar al cerrar** | 54.4.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`andamio quitar «carpeta»` deshace una HU, una fase o un pendiente que creó el andamio. Si sigue idéntico a lo que el andamio crearía, lo borra con las filas que agregó en la épica y en su índice. Si tiene trabajo, lo mueve a `_archivo/` de la misma carpeta padre y deja las filas apuntando ahí con «(archivada)»; el número archivado no se vuelve a usar.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/herramientas/andamio.py` (`textos_de_hu`, `textos_de_fase`, `texto_de_pendiente`, `es_plantilla`, `quitar`) | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/herramientas/andamio.py` (`quitar`, `siguiente_hu`, `hu_pedida`) | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/herramientas/andamio.py` (`_que_es`, `quitar`, `main`) | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 5 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Desde la raíz del estándar: `python validadores/andamio.py quitar «carpeta»` dice qué haría; con `--aplicar`, lo hace. La carpeta va relativa a la raíz.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Comparar el texto entero, no buscar marcadores «…» | Un marcador queda aunque se haya escrito mucho alrededor | No hace falta: está en `andamio.py` |
| Al archivar, los enlaces que suben bajan un nivel | La carpeta queda un nivel más abajo; sin esto sus enlaces se rompen | No hace falta: está en `andamio.py` |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

No aplica.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica.
