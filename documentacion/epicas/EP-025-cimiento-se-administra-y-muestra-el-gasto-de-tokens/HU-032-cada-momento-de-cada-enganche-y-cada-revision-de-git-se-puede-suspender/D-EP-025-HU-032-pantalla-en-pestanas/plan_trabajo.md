# Plan de Trabajo · Fase D-EP-025-HU-032-pantalla-en-pestanas (módulo las suspensiones de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-025-HU-032-pantalla-en-pestanas` |
| **Épica** | `EP-025` |
| **HU** | [`HU-032`](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md), una sola (`F12.1`) |
| **Módulo** | Las suspensiones de Cimiento: `proyectos/cimiento/core/proyectos/` |
| **Especificación del módulo** | La HU-032 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 3 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-3.md), el 2026-10-09, en el turno 45, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 3 del pendiente 149, punto 2 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de `HU-032` que cierra esta fase | Estado |
|---|---|
| CA-04 · La pantalla de suspensiones va en tres pestañas | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** la pantalla de suspensiones en tres pestañas: «Suspensiones», abierta al entrar, con un botón al principio de la tabla que abre el formulario en un modal; «Reglas» y «Enganches», cada una con una tabla igual a la de suspensiones.

**Fuera de alcance:** cambiar qué se puede suspender o cómo se guarda.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`suspensiones.html` pone en una sola página la tabla de suspensiones (List.js, `data-tabla-avanzada`), el formulario y la tabla de enganches. La vista `Suspensiones` (`core/proyectos/views.py:70`) arma el contexto y, si el formulario trae errores, vuelve a pintar la página. Las reglas que se pueden suspender salen de `core.niveles.catalogo.reglas_configurables()` (código, capítulo, título). Las pestañas y el modal ya se usan en `estandar/reglas_del_proyecto.html` y `estandar/documento.html`.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | Modificar | Pantalla | Tres pestañas, el modal y las dos tablas |
| `proyectos/cimiento/core/proyectos/views.py` | Modificar | Vista | Pasa las reglas y si el formulario trae errores |
| `proyectos/cimiento/core/proyectos/tests_suspender_enganches.py` | Modificar | Test | Los casos de la pantalla |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

Cimiento → Proyectos → Suspensiones.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Pestañas y modal de Bootstrap, como en `estandar/` | Pestañas con htmx que piden cada parte | Las tres partes son cortas y ya están en la página | Propuesta del agente |
| Las tablas de «Reglas» y «Enganches» con List.js, como la de suspensiones | Tablas simples | El acuerdo pide «igual a la de suspensiones» | Acuerdos 1 y 2 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

No aplica: no crea nada que haya que deshacer.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La vista pasa las reglas y si hay errores | Vista | 0,3 h | — | EV-01 |
| T-02 | Las tres pestañas, el modal y las dos tablas | Pantalla | 1 h | T-01 | EV-01 |
| T-03 | Pruebas | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 1,8 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 | Pruebas | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta de administrador y una de consulta |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  `02·F14` Q12

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F11`, `08·T1`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el error del formulario quede escondido en el modal cerrado | No se sabe por qué no se guardó | Con errores, el modal vuelve abierto | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
