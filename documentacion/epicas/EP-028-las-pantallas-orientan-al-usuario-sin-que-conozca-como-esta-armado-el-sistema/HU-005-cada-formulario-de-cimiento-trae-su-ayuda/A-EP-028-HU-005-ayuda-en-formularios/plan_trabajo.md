# Plan de Trabajo · Fase A-EP-028-HU-005-ayuda-en-formularios (módulo Ayuda de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-005-ayuda-en-formularios` |
| **Épica** | `EP-028` |
| **HU** | [`HU-005`](../HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md), una sola (`F12.1`) |
| **Módulo** | Ayuda de Cimiento: `core/ayuda/` y las plantillas de formulario |
| **Especificación del módulo** | La HU-005, la EP-025·HU-018 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §3 y §5) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), el 2026-10-07, con la versión 57.1.1 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la de la ayuda (EP-025·HU-018), que no llegó a los formularios nacidos después. Sale del análisis 1 del pendiente 137, punto 8.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-005` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md#ca-01--cada-campo-tiene-su-) | ☐ |
| [CA-02](../HU-005-cada-formulario-de-cimiento-trae-su-ayuda.md#ca-02--cada-pantalla-con-formulario-dice-para-qué-sirve) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que cada campo de los formularios de Cimiento tenga su «?» y cada pantalla con formulario sus botones de ayuda.

**Fuera de alcance:** las tablas (HU-006).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

La ayuda de la EP-025·HU-018 da `ayuda_campo` (el «?» con su globo) y `ayuda_pantalla` (los botones debajo del título), con sus textos en `core/ayuda/textos.py`; `core/ayuda/tests.py` exige que toda clave usada tenga texto. Solo `proyectos/configuracion.html` y `proyectos/suspensiones.html` la usan. Los formularios sin ella y sus campos: entrar (usuario, contraseña); gasto (proyecto, período); documento (ruta, texto); git (asunto, idea, hecho, subir); lista del estándar (buscar); recuerdo (nombre, texto); reportes (proyecto, qué pasa, regla, detalle, versión, motivo); vista previa (proyecto, mensaje); historia (tabla, acción); versiones (proyecto); reglas de un proyecto (nivel); proyecto (nombre, ruta, activo y sus ajustes); y propuestas (el motivo de rechazo).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | Los textos de cada campo y de cada pantalla |
| `proyectos/cimiento/core/ayuda/tests_formularios.py` | Crear | Test | Cada formulario con su ayuda |
| `proyectos/cimiento/core/consumo/tests_tablero.py` | Modificar | Test | Defecto de la HU-003: buscaba «Gasto» en el menú, que pasó a «Gasto de tokens» |
| `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/documento.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/git.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/recuerdo.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/reportes.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/vista_previa.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/propuestas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/lista.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/versiones.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/niveles/templates/niveles/reglas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/_ayuda_del_campo.html` | Crear | Plantilla | Escoge la clave de ayuda de cada campo del formulario del proyecto |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| Las plantillas de formulario | Sus pantallas | Las suites de cada app y `core.ayuda` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Cada formulario.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se usa la ayuda que ya existe | Una ayuda nueva | La trae Cimiento desde la EP-025·HU-018 | `17·I5`, guía §12 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: solo ayuda.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El «?» de cada campo y la ayuda de cada pantalla, con sus textos | Plantilla | 3 h | Ninguna | EV-01 |
| T-02 | Prueba de cobertura y regresión | Test | 0,5 h | T-01 | EV-01 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.

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
| Usuarios de prueba | Ninguno: la prueba lee las plantillas |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I4`, `17·I5`, `00·ID7`, guía §3 y §5.

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
