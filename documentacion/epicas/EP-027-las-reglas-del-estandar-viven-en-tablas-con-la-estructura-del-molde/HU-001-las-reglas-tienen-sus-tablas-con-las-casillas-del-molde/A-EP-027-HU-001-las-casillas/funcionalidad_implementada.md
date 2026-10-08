# Funcionalidad implementada · Fase `A-EP-027-HU-001-las-casillas` (módulo Estándar en la base: `core/estandar/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-001-las-casillas` |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-001](../HU-001-las-reglas-tienen-sus-tablas-con-las-casillas-del-molde.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-001 (CA-01, CA-02) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.3.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Las reglas tienen sus tablas: capítulo, tarea, regla, regla-tarea y dependencia (migración `0005_reglas`). La regla tiene una casilla por parte del molde, con su marca, su «validable» y su sello. De cada casilla salen las partes menores: incorrecto y correcto; condición, límite y autoriza; y resultado, versión, fecha y observación del sello.

`core/estandar/molde.py`, sin Django, lee el texto de una regla en casillas y la vuelve a armar. Las 269 reglas de `base/` dan el mismo texto; en cuatro (F8, D5, G5 y G7) sale con el orden del molde.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · Las tablas tienen las casillas del molde | CA | `core/estandar/models.py`, `migrations/0005_reglas.py` | Hecho | CP-001 |
| CA-02 · Una regla se lee en casillas y se vuelve a armar igual | CA | `core/estandar/molde.py` | Hecho | CP-002 |
| RNF-01 · Sin Django | RNF | `core/estandar/molde.py` solo importa `re` | Hecho | CP-002 |

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

`molde.leer(texto_de_la_regla)` devuelve sus casillas; `molde.armar(casillas)` devuelve el texto; `molde.partir(texto_del_documento)` dice dónde está cada regla dentro de un documento.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Cada casilla guarda su parte tal cual, y las partes menores salen de ella | Armar el texto exacto pide el texto de cada parte; se descartó guardar solo las partes menores | Ninguna |
| La casilla «notas» recoge lo que va después del ejemplo y no es del molde | Nada se pierde; se descartó mezclarlo con la exigencia | Ninguna |
| El código repetido lo rechaza la validación del modelo | MariaDB no tiene índices únicos con condición, y el código se repite entre el estándar y un proyecto | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

`manage.py migrate estandar`: tablas nuevas, vacías. Las llena la HU-002.
