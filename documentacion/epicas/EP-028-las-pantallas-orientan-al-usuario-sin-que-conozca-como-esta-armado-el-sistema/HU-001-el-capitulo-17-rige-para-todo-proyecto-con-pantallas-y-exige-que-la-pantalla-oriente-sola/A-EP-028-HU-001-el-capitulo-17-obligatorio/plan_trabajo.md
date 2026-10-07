# Plan de Trabajo · Fase A-EP-028-HU-001-el-capitulo-17-obligatorio (módulo Estándar en la base y Proyectos)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-001-el-capitulo-17-obligatorio` |
| **Épica** | `EP-028` |
| **HU** | [`HU-001`](../HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, capítulo `17`, y Proyectos (`core/proyectos/`) |
| **Especificación del módulo** | La HU-001 y la [épica EP-028](../../epica.md) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), el 2026-10-07, con la versión 56.16.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que escribió el capítulo `17` (EP-001·HU-030) y la de los opt-in por proyecto (EP-026·HU-009). Sale del análisis 1 del pendiente 137, puntos 2 y 3.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md#ca-01--el-capítulo-17-rige-para-todo-proyecto-con-pantallas) | ☐ |
| [CA-02](../HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola.md#ca-02--la-pantalla-orienta-sola-y-la-plantilla-instalada-va-primero) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el capítulo `17` rija para todo proyecto con pantallas, con la regla `I7` y la `I5` ajustada, y que el ajuste `opt_in_17` desaparezca.

**Fuera de alcance:** la guía de diseño (HU-002).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

En la base, `base/17-interfaz.md` abre con `[CAPA 2 · opt-in]` y un párrafo «Opt-in»; tiene de `I1` a `I6`, y `I5` remite al sistema de diseño de la capa 3. El recuperador apaga una regla opt-in si su encabezado dice «opt-in» y el capítulo está apagado (`ReglasQueAutorizan.vigente`, `RecuperadorDeReglas.elegir`). `core/proyectos/ajustes.py` trae `"17"` en `CAPITULOS_OPT_IN`, y la base tiene ajustes `opt_in_17` de 12 proyectos. La plantilla `plantillas/CLAUDE.md.plantilla` lista el patrón opt-in `17` en su punto 5.1. El mapa de tareas se vuelve a armar solo al guardar un documento (`cambios.rearmar_mapa`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-001-el-capitulo-17-rige-para-todo-proyecto-con-pantallas-y-exige-que-la-pantalla-oriente-sola/A-EP-028-HU-001-el-capitulo-17-obligatorio/propuestas/17-interfaz.txt` | Crear | Texto | Lo que se propone para el capítulo |
| `proyectos/cimiento/core/proyectos/ajustes.py` | Modificar | Lógica | Sale `17` de `CAPITULOS_OPT_IN` |
| `proyectos/cimiento/core/proyectos/migrations/0006_sin_opt_in_17.py` | Crear | Migración | Quita los ajustes `opt_in_17` |
| `proyectos/cimiento/core/proyectos/tests_opt_in.py` | Modificar | Test | Si alguna prueba usa el 17 |
| `proyectos/cimiento/core/herramientas/recuperar.py` | Modificar | Lógica | Del `CLAUDE.md` solo cuentan los capítulos que siguen siendo opt-in: los viejos dicen «no» en el 17 |
| `proyectos/cimiento/core/estandar/tests_capitulo17.py` | Crear | Test | |
| `plantillas/CLAUDE.md.plantilla` | Modificar | Plantilla | Sale la línea del patrón opt-in `17` |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `CAPITULOS_OPT_IN` | formularios de ajustes, ayuda, copia `.agente/configuracion.md`, recuperador | `core.proyectos`, `core.ayuda`, `core.herramientas` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú «Estándar» → enlace «Propuestas», para aprobar.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La regla nueva es `I7`, el siguiente número libre | Renumerar | El número no cambia nunca | `20·M4` |
| Se borran los ajustes `opt_in_17` | Dejarlos sin uso | Un ajuste que no hace nada confunde en la pantalla | RN-05 de la HU |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Aprobar la propuesta del capítulo | Deshacer el cambio desde «Historia» |
| Quitar los ajustes `opt_in_17` | `manage.py migrate proyectos 0005` y volverlos a poner desde el `CLAUDE.md` de cada proyecto |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Redactar el capítulo con `I5` ajustada e `I7` nueva, con sus checklist, y proponerlo | Texto | 1 h | Ninguna | EV-01 |
| T-02 | Quitar el `17` del catálogo y sus ajustes, y la línea de la plantilla | Lógica | 0,5 h | Ninguna | EV-01 |
| T-03 | Prueba del capítulo | Test | 0,5 h | T-01 | EV-01 |
| T-04 | Regresión de las suites tocadas | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 2,5 h, más la espera de la aprobación.

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-03. **Paralelizable:** T-02 y T-04.

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
| Ambiente | La base de pruebas de Django, y el estándar real leído sin escribir |
| Usuarios de prueba | Ninguno |
| Datos precargados | Una carpeta con `CLAUDE.md` que dice «no» en el 17 |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit, `manage.py migrate proyectos 0005` y deshacer el cambio del capítulo desde «Historia».

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

La migración borra filas de ajustes que ya no hacen nada.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M4`, `20·M5`, `20·M10`, `02·F30`.

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
