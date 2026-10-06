# Plan de Trabajo · Fase «A-EP-001-HU-041-las-reglas-nombran-la-base» (módulo «Capítulos 01 y 20»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-041-las-reglas-nombran-la-base` |
| **Épica** | `EP-001` |
| **HU** | [`HU-041`](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md), una sola (`F12.1`) |
| **Módulo** | Capítulos `01 · Conducta de la IA` y `20 · Meta-reglas` |
| **Especificación del módulo** | [base/01-conducta.md](../../../../../base/01-conducta.md) y [base/20-meta-reglas/base.md](../../../../../base/20-meta-reglas/base.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 55.6.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las que escribieron `20·M10` y `01·C19`. Sale del análisis 1 del pendiente 132, acuerdos 1, 2, 7, 12 a 15, 17 y 22.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-041` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-01--2010-pone-la-versión-y-su-registro-en-la-base) | ☐ |
| [CA-02](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-02--lo-que-decía-la-fuente-es-el-texto-queda-derogado) | ☐ |
| [CA-03](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md#ca-03--las-reglas-pasan-sus-comprobaciones) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que `20·M10` exija versionar y registrar todo cambio, del estándar o de un proyecto, en la base de datos del agente cuando la tiene; que `01·C19` admita la memoria en esa base; y que nada diga ya que la fuente es el texto.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | `M10` pone la versión y su registro en la base | Funcional | Media |
| CA-02 | «La fuente es el texto» queda derogado | Funcional | Baja |
| CA-03 | Las reglas pasan sus comprobaciones | Funcional | Baja |
| RNF-01 | Cada regla cita el acuerdo del que sale | No funcional | Baja |

**Fuera de alcance:**

- Construir el registro, las versiones y la pantalla: HU de EP-026.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`20·M10` está en `base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md`, en CUMPLE contra v48.0.0; exige `CHANGELOG.md` y `VERSION`. Sus tipos están en `base/20-meta-reglas/base.md`, sección «M10». `01·C19` está en `base/01-conducta.md` y exige `historico-chat/memory/`. Las copian, generadas por `validadores/mapa_tareas.py`, `base/reglas-por-tarea/cambiar-estandar.md`, `escribir-documento-1.md` y `escribir-documento-2.md`. La versión es 55.6.0.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/20-meta-reglas/reglas/M10-todo-cambio-de-regla-se-versiona-y-se-registra.md` | Modificar | Regla | Cuerpo, ejemplo y checklist |
| `base/20-meta-reglas/base.md` | Modificar | Regla | Sección «M10»: las dos preguntas |
| `base/01-conducta.md` | Modificar | Regla | Cuerpo, ejemplo y checklist de `C19` |
| `base/reglas-por-tarea/cambiar-estandar.md`, `base/reglas-por-tarea/escribir-documento-1.md`, `base/reglas-por-tarea/escribir-documento-2.md`, `base/mapa-de-tareas.md` | Modificar | Regla | Los regenera `mapa_tareas.py` |
| `notas/la-fuente-de-las-reglas-es-el-texto.md` | Modificar | Nota | Marcada como derogada |
| `documentacion/epicas/EP-016-el-cuerpo-de-reglas-se-administra-desde-la-plataforma/epica.md` | Modificar | Épica | Restricción derogada |
| `CLAUDE.md` | Modificar | Instructivo | Secciones 2 y 4 |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 56.0.0, MAYOR |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

No aplica: los títulos y las anclas de `M10` y `C19` no cambian.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: son reglas.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Las reglas dicen «la base de datos del agente» | «La base de Cimiento» | `20·M3` prohíbe nombres propios en `base/` | Propuesta del agente |
| Mientras la base no guarde el estándar, la versión sigue en `CHANGELOG.md` y `VERSION` | Dejar de usar los archivos ya | Sin EP-026 construida, no hay dónde registrar | Propuesta del agente |
| MAYOR | MENOR | Todo cambio de configuración de un proyecto pasa a exigir versión y registro | Acuerdos 1 y 12 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: la fase no agrega acciones.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · `M10` pone la versión y su registro en la base

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reescribir cuerpo y ejemplo de `M10` | Regla | 0,5 h | — | EV-01 |
| T-02 | Escribir las dos preguntas en la sección «M10» de `base.md` | Regla | 0,2 h | T-01 | EV-01 |

### CA-02 · «La fuente es el texto» queda derogado

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Reescribir cuerpo y ejemplo de `C19` | Regla | 0,3 h | — | EV-02 |
| T-04 | Marcar como derogada la nota y la restricción de EP-016 | Documento | 0,2 h | — | EV-02 |
| T-05 | Ajustar `CLAUDE.md`, secciones 2 y 4 | Instructivo | 0,2 h | — | EV-02 |

### CA-03 · Las reglas pasan sus comprobaciones

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-06 | Volver a aplicar el checklist de `M10` y `C19` | Regla | 0,4 h | T-01, T-03 | EV-01, EV-02 |
| T-07 | Regenerar el mapa y las copias de `reglas-por-tarea/` | Regla | 0,1 h | T-06 | EV-03 |
| T-08 | CHANGELOG y VERSION 56.0.0 | Versión | 0,2 h | T-07 | EV-03 |
| T-09 | Correr `validar.py metareglas` y `validar.py estandar` | Test | 0,2 h | T-08 | EV-04 |

**Total estimado:** 2,3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-06, T-07, T-08, T-09
**Paralelizables:** T-04 y T-05 con T-01.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Lectura de la regla | EV-01 | | ☐ |
| CA-02 | Lectura de la regla y los documentos | EV-02 | | ☐ |
| CA-03 | Validadores y lectura de CHANGELOG y VERSION | EV-03, EV-04 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Texto de la regla | `M10-…md` y `base/20-meta-reglas/base.md` |
| EV-02 | Texto | `base/01-conducta.md` (`C19`), la nota, EP-016, `CLAUDE.md` |
| EV-03 | Versión | `CHANGELOG.md`, `VERSION` |
| EV-04 | Salida de validadores | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio del estándar, en la máquina local |
| Usuarios de prueba | No aplica |
| Datos precargados | No aplica |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit de la fase devuelve el texto anterior de las reglas, los documentos y la versión.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Un proyecto al día no hace nada hasta que su base de datos del agente guarde el estándar: la regla dice que, mientras tanto, siguen `CHANGELOG.md` y `VERSION`.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M3`, `20·M5`, `20·M10`, `20·M11`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | `CHANGELOG.md` puede tener cambios de otra sesión | Mezcla el versionado | Se agrega solo la entrada de esta fase | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Requisitos no funcionales validados
- [ ] Validadores en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
