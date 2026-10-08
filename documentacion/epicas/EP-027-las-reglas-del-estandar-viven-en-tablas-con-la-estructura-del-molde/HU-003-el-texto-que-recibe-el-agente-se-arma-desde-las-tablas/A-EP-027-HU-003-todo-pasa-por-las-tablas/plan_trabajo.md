# Plan de Trabajo · Fase A-EP-027-HU-003-todo-pasa-por-las-tablas (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-003-todo-pasa-por-las-tablas` |
| **Épica** | `EP-027` |
| **HU** | [`HU-003`](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | La HU-003 |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), el 2026-10-07, con la versión 57.4.0; el usuario pidió terminar la épica («continúe termine todo», 2026-10-07) |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que hizo `guardar_documento` y `quitar_documento` (EP-026·HU-005) y la que hizo `sincronizar` (EP-026·HU-004). Sale del acuerdo 2 del análisis 1 del pendiente 136.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-003` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md#ca-01--cambiar-un-documento-pasa-por-las-tablas) | ☐ |
| [CA-02](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md#ca-02--nada-se-borra) | ☐ |
| [CA-03](../HU-003-el-texto-que-recibe-el-agente-se-arma-desde-las-tablas.md#ca-03--el-agente-recibe-el-texto-armado) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que todo cambio de un documento pase por las tablas, y que el texto guardado, el que leen el agente y el freno, sea siempre el armado desde ellas.

**Fuera de alcance:** dejar de guardar `base/reglas-por-tarea/` (espera la decisión del usuario: armarlas al vuelo tarda 0,8 s por mensaje).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Un documento cambia por tres caminos: `cambios.guardar_documento` (la pantalla y las propuestas aprobadas), `cambios.quitar_documento` y `importar.sincronizar` (lo que trae git). `Regla.documento` es `PROTECT`: hoy, quitar un documento con reglas fallaría. `reglas.pasar_documento` y `reglas.armar_documento` (HU-002) hacen el paso de un documento. Los enganches leen `estandar_documento.contenido` (`en_base.py`) y `ver_estandar` también.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/cambios.py` | Modificar | Lógica | Guardar y quitar pasan por las tablas |
| `proyectos/cimiento/core/estandar/importar.py` | Modificar | Lógica | Sincronizar pasa por las tablas |
| `proyectos/cimiento/core/estandar/reglas.py` | Modificar | Lógica | `pasar_y_armar(documento)` y `soltar_reglas(documento)` |
| `proyectos/cimiento/core/estandar/management/commands/importar_estandar.py` | Modificar | Comando | En una instalación nueva, las reglas pasan a las tablas después de importar |
| `proyectos/cimiento/core/estandar/tests_texto_desde_tablas.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `guardar_documento`, `quitar_documento` | La pantalla del estándar, las propuestas | `core.estandar` |
| `sincronizar` | `sincronizar_estandar` | `core.estandar` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Los de siempre: «Cambiar el texto» y «Propuestas».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El texto armado se guarda en el documento | Armarlo al leer | Los enganches leen sin Django en cada mensaje; así no se demoran | RNF-01 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: guardar, quitar y sincronizar conservan su contraria, «Deshacer» en la historia.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Guardar, quitar y sincronizar pasan por las tablas | Lógica | 1 h | Ninguna | EV-01 |
| T-02 | Pruebas y regresión | Test | 1 h | T-01 | EV-01 |

**Total estimado:** 2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.

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
| Ambiente | La base de pruebas de Django, con el estándar importado de `base/` y pasado a las tablas |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | El estándar |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración: la base viva ya tiene las tablas llenas (HU-002).

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M10`, `20·M11`.

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
