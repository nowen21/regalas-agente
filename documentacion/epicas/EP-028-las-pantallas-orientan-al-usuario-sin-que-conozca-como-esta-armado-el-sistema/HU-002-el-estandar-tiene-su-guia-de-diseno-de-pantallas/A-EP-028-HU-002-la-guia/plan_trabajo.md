# Plan de Trabajo · Fase A-EP-028-HU-002-la-guia (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-002-la-guia` |
| **Épica** | `EP-028` |
| **HU** | [`HU-002`](../HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, capítulo `17` |
| **Especificación del módulo** | La HU-002, la [épica EP-028](../../epica.md) y el encargo [`prompts/prompt-guia-estilo.md`](../../../../../prompts/prompt-guia-estilo.md) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), el 2026-10-07, con la versión 57.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Funcionalidad nueva: la guía de diseño de pantallas del estándar. Sale del análisis 1 del pendiente 137, punto 4, acuerdos 1 y 3.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas.md#ca-01--la-guía-cubre-el-encargo) | ☐ |
| [CA-02](../HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas.md#ca-02--la-plantilla-instalada-va-primero) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el estándar tenga su guía de diseño de pantallas, con las 14 secciones del encargo, y que el capítulo 17 la enlace.

**Fuera de alcance:** arreglar las pantallas de Cimiento (HU-003 a HU-006).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

El estándar no tiene guía de pantallas; `17·I5` pide la plantilla instalada. Cimiento usa Tabler 1.6.1 (`proyectos/cimiento/node_modules/@tabler/core`), con List.js, Tom Select, Litepicker, Driver.js, Dropzone y ApexCharts instalados. Un documento nuevo del estándar se propone con `manage.py proponer --ruta base/…` y se aprueba en la pantalla.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas/A-EP-028-HU-002-la-guia/propuestas/guia-de-pantallas.txt` | Crear | Texto | La guía que se propone, `base/17-guia-de-pantallas.md` |
| `documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-002-el-estandar-tiene-su-guia-de-diseno-de-pantallas/A-EP-028-HU-002-la-guia/propuestas/17-interfaz.txt` | Crear | Texto | El enlace del capítulo 17 a la guía |
| `proyectos/cimiento/core/estandar/tests_guia.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| Un documento nuevo del estándar | El agente, al leerlo con `ver_estandar` | `core.estandar.tests_guia` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú «Estándar» → enlace «Propuestas», para aprobar.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La guía vive junto al capítulo 17, como `base/17-guia-de-pantallas.md` | Un capítulo nuevo | Desarrolla el cómo de las reglas del 17, como `estructura-regla.md` desarrolla la `M5` | `20·M2` |
| Cada sección dice qué se exige y cómo se hace en Tabler | Escribirla solo para Tabler | La guía es de todos; Tabler es el ejemplo de Cimiento | Acuerdo 3 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Aprobar la propuesta de la guía | Rechazarla, o deshacer el cambio desde «Historia» |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Redactar la guía con las 14 secciones y el enlace del capítulo 17 | Texto | 3 h | Ninguna | EV-01 |
| T-02 | Proponerlos y esperar la aprobación | Texto | 0 h | T-01 | EV-01 |
| T-03 | Prueba que lee la guía aprobada | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 3,5 h, más la espera de la aprobación.

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
| Ambiente | El estándar en la base real, leído sin escribir |
| Usuarios de prueba | Ninguno |
| Datos precargados | La guía aprobada |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Deshacer los cambios desde «Historia».

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración: entra un documento.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I1` a `17·I7`, `20·M2`, `20·M3`, `00·ID7`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La fase espera la aprobación del usuario en la pantalla | No cierra hasta entonces | Se acompaña el paso a paso | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
