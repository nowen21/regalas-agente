# Plan de Trabajo · Fase A-EP-027-HU-004-el-estandar-se-lee-como-pagina (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-004-el-estandar-se-lee-como-pagina` |
| **Épica** | `EP-027` |
| **HU** | [`HU-004`](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | La HU-004 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), el 2026-10-07, con la versión 57.2.0; el usuario pidió hacerla ya («corrija» y «continúe», 2026-10-07) |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que hizo las pantallas del estándar (EP-026·HU-005). Sale del acuerdo 3 del análisis 1 del pendiente 136 y de la corrección del usuario del 2026-10-07.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md#ca-01--la-lista-va-por-capítulo-y-por-nombre) | ☐ |
| [CA-02](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md#ca-02--el-documento-se-lee-como-página) | ☐ |
| [CA-03](../HU-004-la-pantalla-lista-las-reglas-por-capitulo-con-sus-relaciones-y-enlaces-que-abren.md#ca-03--los-enlaces-abren-y-las-relaciones-se-ven) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el estándar se vea en Cimiento como páginas ordenadas con los componentes de Tabler, listado por capítulo y por nombre, con enlaces que abren y sus relaciones a la vista.

**Fuera de alcance:** leer las casillas de las tablas (HU-001 y HU-002); propuestas, historia y memoria (HU-005).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

La base tiene 153 documentos en `estandar_documento` (`ruta`, `contenido`). `Lista` (`core/estandar/views.py`) los agrupa por carpeta y muestra la ruta; `documento.html` muestra el texto en un `<pre>`. `core/comun/markdown.py` ya lee enlaces y encabezados para los validadores, pero no arma HTML. Los capítulos son de dos formas: un archivo con sus reglas como secciones (`base/01-conducta.md`, `## C1 · …`) o una carpeta con `base.md` y una regla por archivo en `reglas/`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/presentar.py` | Crear | Lógica | Título, capítulo y relaciones de cada documento, y su paso a HTML |
| `proyectos/cimiento/core/estandar/views.py` | Modificar | Vista | `Lista` por capítulo; `VerDocumento` con la página y las relaciones |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | Capítulos en acordeón, reglas por código y título |
| `proyectos/cimiento/core/estandar/templates/estandar/documento.html` | Modificar | Plantilla | Encabezado, migas, pestañas Leer / Cambiar, relaciones |
| `proyectos/cimiento/core/estandar/templates/estandar/_relacion.html` | Crear | Plantilla | Un renglón del espacio de relaciones |
| `proyectos/cimiento/static/estandar.css` | Crear | Estilo | Solo lo que Tabler no trae para el texto largo |
| `proyectos/cimiento/core/estandar/tests_vista_estandar.py` | Crear | Test | |
| `proyectos/cimiento/core/estandar/tests_pantalla.py` | Modificar | Test | Lo que esperaba la ruta en la lista |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Texto | La ayuda de las pantallas «estandar» y «documento» |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/estandar.html` | Modificar | Plantilla | El manual describe la pantalla nueva |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `Lista` y `VerDocumento` | Las pantallas del estándar | `core.estandar` |
| Los textos de ayuda | La ayuda de cada pantalla | `core.ayuda` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva. Cambiar el texto sigue siendo solo del grupo administrador.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú «Estándar → Reglas y documentos».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Un convertidor propio, que escapa el texto antes de armar el HTML | La librería `markdown` | Acordado; y escapar primero evita que el texto meta HTML | Acuerdo 3, RNF-02 |
| El enlace se resuelve contra las rutas de la base | Dejar el destino del archivo | El enlace tiene que abrir en Cimiento | RN-05 |
| Las relaciones se leen del texto | Esperar las tablas | La HU no depende de ellas; con las tablas cambia la fuente, no la pantalla | §3 de la HU |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: la pantalla solo muestra.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `presentar.py`: título, capítulo, relaciones y HTML | Lógica | 2 h | Ninguna | EV-01 |
| T-02 | Vistas, plantillas y estilo | Vista | 1,5 h | T-01 | EV-01 |
| T-03 | Ayuda, manual, pruebas y regresión | Test | 1 h | T-02 | EV-01 |

**Total estimado:** 4,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |
| CA-03 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora y una de consulta |
| Datos precargados | Documentos con la forma de un capítulo de un archivo, uno de carpeta y una regla |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I5`, `17·I7`, guía §2, §3, §4, §6 y §12.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
