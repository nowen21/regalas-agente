# Plan de Trabajo · Fase A-EP-027-HU-007-el-molde-habla-de-casillas (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-027-HU-007-el-molde-habla-de-casillas` |
| **Épica** | `EP-027` |
| **HU** | [`HU-007`](../HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, capítulo `20` |
| **Especificación del módulo** | La HU-007 y la [épica EP-027](../../epica.md) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md), el 2026-10-07, con la versión 56.11.1 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las que escribieron `20·M5` y `20·M9` (EP-001·HU-033). Sale del análisis 1 del pendiente 136, punto 12, y de la decisión S-346.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-007` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas.md#ca-01--20m5-habla-de-casillas) | ☐ |
| [CA-02](../HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas.md#ca-02--20m9-manda-a-la-casilla-validable) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que `20·M5` y `20·M9`, y lo que las desarrolla en el capítulo 20, digan que la regla vive en casillas.

**Fuera de alcance:** las otras reglas que nombran `validadores/reglas-validables.md` (HU-002).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

En la base, `20·M5` describe el encabezado `## <PREFIJO><n> · <título>` como texto; `20·M9` y la línea 25 del catálogo de `base/20-meta-reglas/base.md` mandan a `validadores/reglas-validables.md`, igual que la sección de M9 sobre qué se sigue de cada respuesta (línea 109), el paso de revisión (línea 142), la fila 18 de `checklist.md` y el bloque de pasos de `estructura-regla.md` (línea 330). Los cambios del estándar se proponen con `manage.py proponer` y se aprueban en «Estándar» → «Propuestas».

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/A-EP-027-HU-007-el-molde-habla-de-casillas/propuestas/M5.txt` | Crear | Texto | Lo que se propone para `20·M5` |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/A-EP-027-HU-007-el-molde-habla-de-casillas/propuestas/M9.txt` | Crear | Texto | Lo que se propone para `20·M9` |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/A-EP-027-HU-007-el-molde-habla-de-casillas/propuestas/base.txt` | Crear | Texto | Lo que se propone para el capítulo 20 |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/A-EP-027-HU-007-el-molde-habla-de-casillas/propuestas/checklist.txt` | Crear | Texto | Fila 18 |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-007-las-reglas-m5-y-m9-dicen-que-la-regla-vive-en-casillas/A-EP-027-HU-007-el-molde-habla-de-casillas/propuestas/estructura-regla.txt` | Crear | Texto | Los pasos después de escribir |
| `proyectos/cimiento/core/estandar/tests_molde.py` | Crear | Test | Lee el estándar aprobado |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| El texto de `20·M5` y `20·M9` | El agente al recibir reglas; `CuerpoDeReglas` lee el encabezado, que no cambia | `core.estandar.tests_molde` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar» → «Propuestas», para aprobar.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se proponen los cinco documentos y se aprueban en la pantalla | Editarlos directo en la base | Todo cambio del estándar se autoriza en la pantalla | Análisis 1 del pendiente 132, acuerdo 3 |
| «Validable» con tres valores y el programa al lado | Solo sí o no | No se pierde qué programa comprueba cada regla | S-346 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Aprobar una propuesta | Rechazarla, o deshacer el cambio desde «Historia» |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Redactar los cinco textos, con el checklist de `M5` y `M9` aplicado | Texto | 1 h | Ninguna | EV-01 |
| T-02 | Proponerlos y esperar la aprobación | Texto | 0 h | T-01 | EV-01 |
| T-03 | Prueba que lee el estándar aprobado | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 1,5 h, más la espera de la aprobación.

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
| Datos precargados | Los documentos aprobados |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Deshacer los cinco cambios desde «Historia».

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración: cambia texto.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M5`, `20·M9`, `20·M10`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La fase espera la aprobación del usuario en la pantalla | No cierra hasta entonces | Se avisa en el chat | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
