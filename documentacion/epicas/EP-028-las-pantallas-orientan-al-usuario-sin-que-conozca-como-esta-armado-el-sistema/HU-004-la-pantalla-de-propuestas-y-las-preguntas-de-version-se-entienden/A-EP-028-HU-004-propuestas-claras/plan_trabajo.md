# Plan de Trabajo · Fase A-EP-028-HU-004-propuestas-claras (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-004-propuestas-claras` |
| **Épica** | `EP-028` |
| **HU** | [`HU-004`](../HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` y las preguntas de versión de `core/historia/` |
| **Especificación del módulo** | La HU-004 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §5, §8 y §11) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), el 2026-10-07, con la versión 57.1.1 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que hizo «Propuestas» (EP-026·HU-005) y la de las preguntas de versión (EP-026·HU-002). Sale del análisis 1 del pendiente 137, puntos 6 y 7.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md#ca-01--se-ve-qué-cambia-y-rechazar-pide-el-motivo) | ☐ |
| [CA-02](../HU-004-la-pantalla-de-propuestas-y-las-preguntas-de-version-se-entienden.md#ca-02--las-preguntas-de-versión-se-entienden) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que «Propuestas» muestre qué cambia, pida el motivo al rechazar y diga qué hacer; y que las preguntas de versión se entiendan en todo formulario.

**Fuera de alcance:** mostrar las reglas por su nombre en lugar de su ruta (EP-027·HU-005).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`core/estandar/templates/estandar/propuestas.html` muestra el `contenido` entero de cada propuesta. `cambios.rechazar(propuesta, cuenta)` no recibe motivo y `Propuesta` no tiene dónde guardarlo. `historia/_tipo_de_version.html` trae las dos preguntas sin ayuda; lo incluyen `estandar/documento.html`, `propuestas.html`, `recuerdo.html`, `niveles/reglas.html`, `proyectos/configuracion.html`, `formulario.html` y `suspensiones.html`, y el middleware `CuentaDeLaPeticion` lee `version_obliga` y `version_agrega`. La ayuda por campo vive en `core/ayuda/textos.py` y se pinta con `{% ayuda_campo %}`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/models.py` | Modificar | Modelo | `motivo_rechazo` |
| `proyectos/cimiento/core/estandar/migrations/0004_motivo_rechazo.py` | Crear | Migración | Aditiva |
| `proyectos/cimiento/core/estandar/cambios.py` | Modificar | Lógica | Qué cambia; rechazar con motivo |
| `proyectos/cimiento/core/estandar/views.py` | Modificar | Vista | |
| `proyectos/cimiento/core/estandar/templates/estandar/propuestas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/_tipo_de_version.html` | Modificar | Plantilla | Preguntas claras, su «?» y el tipo a la vista |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | Los dos «?» |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/estandar.html` | Modificar | Ayuda | Cómo se aprueba |
| `proyectos/cimiento/core/estandar/tests_propuestas_claras.py` | Crear | Test | |
| `proyectos/cimiento/core/estandar/tests_pantalla.py` | Modificar | Test | Rechazar ahora pide el motivo |
| `proyectos/cimiento/core/estandar/tests_capitulo17.py` | Modificar | Test | Defecto de la HU-001: vaciaba la base sin `serialized_rollback` y dañaba las pruebas siguientes |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | Defecto de la HU-003: «Registrar un proyecto» se mostraba a una cuenta de consulta |
| `proyectos/cimiento/core/inicio/pendientes.py` | Modificar | Lógica | Dice si la cuenta administra, para el menú |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `_tipo_de_version.html` | Siete formularios | `core.estandar`, `core.proyectos`, `core.niveles`, `core.historia` |
| `cambios.rechazar` | La vista `Resolver` | `core.estandar` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Las de siempre: `/estandar/propuestas/<id>/aprobar/` y `/rechazar/`, solo administrador.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú «Estándar» → «Propuestas por aprobar».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Lo que cambia se calcula con `difflib` | Una librería de diferencias | Viene con Python | RNF-01 |
| Los nombres de los campos de las preguntas no cambian | Renombrarlos | El middleware los lee igual | Línea base |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Rechazar con motivo | Volver a proponer el cambio |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Qué cambia y rechazar con motivo | Lógica | 1,5 h | Ninguna | EV-01 |
| T-02 | Preguntas de versión con su ayuda y el tipo a la vista | Plantilla | 1 h | Ninguna | EV-01 |
| T-03 | Pruebas y regresión | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-03. **Paralelizable:** T-02.

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
| Datos precargados | Un documento y una propuesta que cambia una línea |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `manage.py migrate estandar 0003`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: un campo nuevo con valor vacío.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I2`, `17·I4`, `17·I5`, `17·I7`, guía §5, §8 y §11.

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
