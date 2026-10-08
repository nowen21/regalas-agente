# Plan de Trabajo · Fase A-EP-027-HU-005-propuestas-y-memoria (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-005-propuestas-y-memoria` |
| **Épica** | `EP-027` |
| **HU** | [`HU-005`](../HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | La HU-005 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §6 y §8) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), el 2026-10-07, con la versión 57.4.0; el usuario pidió terminar la épica («continúe termine todo», 2026-10-07) |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las que hicieron las propuestas y la memoria (EP-026·HU-005, EP-028·HU-004). Sale del acuerdo 4 del análisis 1 del pendiente 136.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-005` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-005-las-propuestas-la-historia-y-la-memoria-muestran-nombres-legibles.md#ca-01--propuestas-y-memoria-con-nombres-legibles) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que las propuestas y la memoria nombren cada cosa por su nombre legible, y que el documento, el recuerdo y la regla sepan decir su nombre legible a quien lo pida (la historia, en la fase B).

**Fuera de alcance:** la pantalla de la historia (fase B, `core/historia/`).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`propuestas.html` muestra `p.destino`: la ruta, o el proyecto y el nombre de archivo. `recuerdos.html` lista `r.nombre` y `recuerdo.html` lo pone de título. Los recuerdos abren con un bloque entre `---` con `name:` y `description:`. `presentar.leer_titulo` saca el título de un texto (HU-004).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/models.py` | Modificar | Modelo | `nombre_legible()` en documento, recuerdo, propuesta y regla; `descripcion()` del recuerdo; nombres de las tablas |
| `proyectos/cimiento/core/estandar/presentar.py` | Modificar | Lógica | Nombre y descripción de un recuerdo desde su texto |
| `proyectos/cimiento/core/estandar/templates/estandar/propuestas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/recuerdos.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/recuerdo.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/migrations/0006_nombres.py` | Crear | Migración | Solo los nombres de las tablas (`verbose_name`); no cambia la base |
| `proyectos/cimiento/core/estandar/tests_nombres_legibles.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| Las plantillas de propuestas y memoria | Sus pantallas | `core.estandar` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar → Propuestas por aprobar» y «Estándar → Reglas y documentos → Memoria de cada proyecto».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cada modelo dice su nombre legible con `nombre_legible()` | Que cada pantalla lo arme | Una sola manera, que la historia también usa | Guía §12 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: solo cambia cómo se muestra.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `nombre_legible()` y las plantillas | Modelo | 1 h | Ninguna | EV-01 |
| T-02 | Pruebas | Test | 0,5 h | T-01 | EV-01 |

**Total estimado:** 1,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Un documento de regla, una propuesta y un recuerdo |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

La migración solo cambia nombres que Django guarda en su estado; la base no cambia.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I4`, guía §6 y §8.

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
