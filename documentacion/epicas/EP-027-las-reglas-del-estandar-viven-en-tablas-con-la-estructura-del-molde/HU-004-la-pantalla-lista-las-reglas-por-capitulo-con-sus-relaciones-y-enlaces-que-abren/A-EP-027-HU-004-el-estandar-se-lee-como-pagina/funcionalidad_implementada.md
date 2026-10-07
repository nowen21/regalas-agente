# Funcionalidad implementada · Fase `A-EP-027-HU-004-el-estandar-se-lee-como-pagina` (módulo Estándar en la base: `core/estandar/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-004-el-estandar-se-lee-como-pagina` |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | Los CA de la [HU-004](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-004 (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-07 |
| **Versión del estándar al cerrar** | 57.2.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El estándar se ve en Cimiento como páginas, no como texto crudo. La pantalla «Reglas y documentos» agrupa todo por capítulo en un acordeón de Tabler, con el nombre del capítulo y, en cada renglón, el código y el título de la regla; las derogadas se marcan. Ninguna ruta de archivo se muestra.

Cada documento se abre como página:

- migas que dicen dónde está;
- títulos, listas y tablas de Tabler;
- las citas, como avisos;
- el ejemplo, en dos tarjetas: «Incorrecto» en rojo y «Correcto» en verde;
- «Aplica a», como insignias;
- el sello del checklist, en una tarjeta que se abre al pulsarla.

Los enlaces a otra regla abren esa regla en Cimiento, en su sección. A la derecha, «Relaciones» muestra en tres grupos de qué depende la regla, cuáles nombra y cuáles la nombran. Quien administra cambia el texto en la pestaña «Cambiar el texto». Para quitar el documento, una ventana pide confirmarlo.

La conversión es código propio (`core/estandar/presentar.py`), sin la librería `markdown`: escapa el texto antes de ponerle etiquetas.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 · La lista va por capítulo y por nombre | CA | `core/estandar/presentar.py` (`Estandar.capitulos`), `views.py` (`Lista`), `templates/estandar/lista.html` | Hecho | CP-001 |
| CA-02 · El documento se lee como página | CA | `presentar.py` (`Pagina`), `templates/estandar/documento.html`, `static/estandar.css` | Hecho | CP-002, CP-003 |
| CA-03 · Los enlaces abren y las relaciones se ven | CA | `presentar.py` (`Estandar.url`, `Estandar.relaciones`), `templates/estandar/_relacion.html` | Hecho | CP-004 |
| RNF-02 · El texto se escapa | RNF | `presentar.py` (`Pagina.linea`) | Hecho | CP-003 |

**Faltantes / diferimientos:** ninguno. Armar el texto desde las tablas es de la HU-003; la página lo muestra igual.

### 2.2 Plan de trabajo → ejecución

Las 3 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna. `tests_pantalla.py` estaba declarado para cambiar y no hizo falta: ninguna prueba vieja se rompió.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. `_relacion.html` se declaró en el plan antes de crearla.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

Menú «Estándar» → «Reglas y documentos»: se abre un capítulo y se pulsa la regla. En la página, los enlaces y la tarjeta «Relaciones» llevan a las otras reglas; las migas de arriba devuelven al capítulo o al estándar.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las anclas siguen la forma de GitHub, con `-1`, `-2` para las repetidas | Así ya las escriben los 2.697 enlaces del estándar; se descartó inventar otra forma | Ninguna |
| Un enlace a un archivo que no está en la base se ve como texto | Abriría un archivo que Cimiento no tiene; se descartó dejar el enlace roto | Ninguna |
| Las relaciones se leen del texto | La HU no depende de las tablas; cuando lleguen, cambia de dónde se leen y la pantalla queda igual | Ninguna |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

Ninguno.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Ninguno: basta con recargar Cimiento.
