# Plan de Trabajo · Fase A-EP-026-HU-008-los-reportes (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-008-los-reportes` |
| **Épica** | `EP-026` |
| **HU** | [`HU-008`](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-008 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que escribió el aviso de versión atrasada (`EP-002·HU-004`). Sale del análisis 1 del pendiente 132, acuerdos 13 y 14.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-008` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md#ca-01--reportar) | ☐ |
| [CA-02](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md#ca-02--corregir-con-su-versión) | ☐ |
| [CA-03](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md#ca-03--el-proyecto-se-entera) | ☐ |
| [CA-04](../HU-008-lo-que-un-proyecto-reporta-llega-al-estandar-como-pendiente.md#ca-04--el-aviso-de-versión-mira-la-base) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que un proyecto reporte al estándar, que el reporte se cierre con la versión que lo corrigió y que el proyecto se entere; y que el aviso de versión mire la base.

**Fuera de alcance:** corregir el estándar (HU-005).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`VersionDelEstandar` (`core/validadores/version.py`) lee la vigente de `VERSION` (`vigente`) y las publicadas de `CHANGELOG.md` (`versiones_publicadas`); lo llama el arranque. Con `base/` congelado (HU-006) los dos archivos quedaron quietos en la 56.8.0 y la base va en la 56.8.1. El arranque está en `adaptadores/claude-code/hook_sesion.py`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/models.py` | Modificar | Modelo | `Reporte` |
| `proyectos/cimiento/core/estandar/migrations/0003_reporte.py` | Crear | Migración | Aditiva |
| `proyectos/cimiento/core/historia/versiones.py` | Modificar | Lógica | El reporte no sube versión |
| `proyectos/cimiento/core/estandar/avisos.py` | Crear | Lógica | Reportes corregidos sin avisar, sin Django |
| `proyectos/cimiento/core/estandar/congelado.py` | Modificar | Lógica | Las versiones del estándar en la base |
| `proyectos/cimiento/core/estandar/views.py` | Modificar | Vista | Reportes |
| `proyectos/cimiento/core/estandar/urls.py` | Modificar | Rutas | |
| `proyectos/cimiento/core/estandar/templates/estandar/reportes.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | Enlace |
| `proyectos/cimiento/core/estandar/management/commands/reportar.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/tests_reportes.py` | Crear | Test | |
| `proyectos/cimiento/core/validadores/version.py` | Modificar | Lógica | Vigente y publicadas de la base |
| `proyectos/cimiento/core/herramientas/tests_instalacion.py` | Modificar | Test | Dos pruebas daban por hecho que la vigente es la de `VERSION`; con el estándar congelado es la de la base |
| `adaptadores/claude-code/hook_sesion.py` | Modificar | Enganche | El aviso del reporte corregido |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/estandar.html` | Modificar | Ayuda | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `VersionDelEstandar.vigente` y `versiones_publicadas` | el arranque, `instalar.py`, `validar.py` | `core.validadores`, `core.herramientas.tests_instalacion` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `/estandar/reportes/` | GET; POST crea | Toda cuenta mira; administrador crea |
| `/estandar/reportes/<id>/resolver/` | POST | Administrador |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar» → «Reportes».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se corrige eligiendo la versión del estándar que lo corrigió | Subir una versión al marcar | La versión sube con la corrección, que se hizo antes en la pantalla | Acuerdo 13 |
| El aviso al proyecto va una sola vez, al abrir su sesión | Avisar en cada mensaje | Ya se enteró; repetirlo gasta tokens | Propuesta del agente |
| Con el estándar congelado, la vigente y las publicadas salen de la base | Seguir con los archivos | Quedaron quietos | Acuerdo 14 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Reportar | Descartar el reporte, con su motivo |
| Marcar corregido o descartado | Deshacer el cambio desde «Historia» |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Modelo, pantalla y `reportar` | Modelo | 1,5 h | — | EV-01 |
| T-02 | Corregir con su versión, o descartar | Vista | 0,5 h | T-01 | EV-01 |
| T-03 | Aviso al proyecto | Enganche | 0,5 h | T-02 | EV-01 |
| T-04 | El aviso de versión mira la base | Lógica | 0,5 h | — | EV-01 |
| T-05 | Pruebas y regresión | Test | 1 h | T-01 a T-04 | EV-01 |

**Total estimado:** 4 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-05. **Paralelizable:** T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |
| CA-04 | Pruebas de Django | EV-01 | | ☐ |

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

Revertir el commit y `manage.py migrate estandar 0002`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: una tabla nueva.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F29`, `20·M10`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión escribe en la misma carpeta y el freno se lo cobra a esta | Detiene órdenes de consola | Se anota y se sigue | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
