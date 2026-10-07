# Plan de Trabajo · Fase A-EP-028-HU-006-tablas-avanzadas (módulo Tablas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-006-tablas-avanzadas` |
| **Épica** | `EP-028` |
| **HU** | [`HU-006`](../HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla.md), una sola (`F12.1`) |
| **Módulo** | Tablas de Cimiento |
| **Especificación del módulo** | La HU-006 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §6 y §12) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), el 2026-10-07, con la versión 57.1.1 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las que hicieron las listas de proyectos, suspensiones, historia, versiones, historial de niveles, propuestas y reportes (EP-025 y EP-026). Sale del análisis 1 del pendiente 137, punto 9.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla.md#ca-01--las-listas-se-ordenan-se-filtran-y-se-paginan) | ☐ |
| [CA-02](../HU-006-las-tablas-de-cimiento-usan-los-recursos-de-tablas-de-la-plantilla.md#ca-02--un-solo-código-y-un-solo-pie) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que las listas de registros de Cimiento se ordenen, se filtren y se paginen con el patrón de tablas de Tabler.

**Fuera de alcance:** el manual, los recuadros del gasto y las reglas de un proyecto (RN-04 de la HU); quitar columnas (EP-027·HU-005).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Cimiento sirve `node_modules/@tabler/core/dist` como estáticos (`config/settings/base.py`), así que `libs/list.js/dist/list.min.js` está disponible sin instalar nada. Las listas de registros son: `proyectos/lista.html`, `proyectos/suspensiones.html`, `niveles/historial.html`, `estandar/propuestas.html` (las resueltas), `estandar/reportes.html` (los resueltos), y `historia/lista.html` y `historia/versiones.html`, que la base ya pagina. Scilit usa el mismo patrón en su `static/js/main.js` (`data-tabla-avanzada`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/static/tablas.js` | Crear | Script | El patrón de tabla de Tabler con List.js |
| `proyectos/cimiento/templates/includes/tabla_pie.html` | Crear | Plantilla | Filas por página y páginas |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | Carga List.js y `tablas.js` |
| `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/niveles/templates/niveles/historial.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/propuestas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/reportes.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/lista.html` | Modificar | Plantilla | Orden y filtro; conserva su paginación |
| `proyectos/cimiento/core/historia/templates/historia/versiones.html` | Modificar | Plantilla | Orden y filtro; conserva su paginación |
| `proyectos/cimiento/core/inicio/tests_tablas.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| Las plantillas con tablas | Sus pantallas | Las suites de cada app |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Cada lista.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El patrón de tabla de Tabler con List.js | Ordenar y paginar en el servidor | Lo trae la plantilla instalada | `17·I5`, guía §6 |
| Historia y versiones conservan la paginación de la base | Pasarlas a List.js | Tienen miles de filas; List.js ordena y filtra lo que se ve | RN-03 de la HU |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: ordenar y filtrar no cambian nada.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `tablas.js`, el pie común y la carga en `base.html` | Script | 1 h | Ninguna | EV-01 |
| T-02 | Las siete listas | Plantilla | 2 h | T-01 | EV-01 |
| T-03 | Pruebas y regresión | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Un proyecto registrado |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I5`, guía §6 y §12.

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
