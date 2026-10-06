# Plan de Trabajo · Fase B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos (módulo Cimiento, herramientas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-024-las-reglas-no-se-aplican-a-los-avisos` |
| **Épica** | `EP-005` |
| **HU** | [`HU-024`](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/herramientas/` |
| **Especificación del módulo** | [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las de `EP-005·HU-023`, que arman las reglas de cada mensaje y el aviso de `01·C28`. Sale del análisis 1 del pendiente 124, acuerdo 8. Va aparte de la fase `A` porque es otro módulo (`02·F11`).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-024` que cierra esta fase | Estado |
|---|---|
| CA-02 | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que `RecuperadorDeReglas.como_texto` devuelva nada para un aviso interno.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-02 | Las reglas del usuario no se le aplican | Funcional | Baja |

**Fuera de alcance:** el histórico, fase `A`.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`como_texto` en `core/herramientas/recuperar.py` devuelve el aviso de `01·C28` cuando el mensaje no trae palabra clave, y así le llegó al agente con cada aviso interno. `es_aviso_interno` ya existe en `core/enganches/historico.py` (fase `A`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/recuperar.py` | Modificar | Servicio | |
| `proyectos/cimiento/core/herramientas/tests_avisos_internos.py` | Nuevo | Test | |

### 2.2 a 2.8

No aplica.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `como_texto` devuelve nada ante un aviso interno | Servicio | 0,2 h | — | EV-01 |
| T-02 | Prueba | Test | 0,3 h | T-01 | EV-01 |

**Total estimado:** 0,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-02 | `tests_avisos_internos` de herramientas | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` |

## 6. a 10.

No aplica.

## 11. Definition of Done

- [ ] CA-02 verificado

## 13. Cierre

Las 2 tareas quedaron hechas el 2026-10-06, con la versión 55.6.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
