# Plan de Trabajo · Fase A-EP-005-HU-024-el-historico-los-firma-como-aviso (módulo Cimiento, enganches)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-024-el-historico-los-firma-como-aviso` |
| **Épica** | `EP-005` |
| **HU** | [`HU-024`](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/enganches/` |
| **Especificación del módulo** | [HU-024](../HU-024-el-historico-anota-los-avisos-internos-con-su-remitente.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las de `EP-005·HU-001`, la transcripción de la sesión, que anota todo lo que entra por `UserPromptSubmit` como «Usuario». Sale del análisis 1 del pendiente 124, acuerdo 8.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-024` que cierra esta fase | Estado |
|---|---|
| CA-01 | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** el histórico firma como «Aviso del sistema» lo que abre con `<task-notification>` o `<agent-message`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | El histórico lo firma como aviso | Funcional | Baja |
| RNF-01 | El aviso queda con texto y hora | No funcional | Baja |

**Fuera de alcance:** el enganche de reglas, fase `B` (`02·F11`).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`Historico.anotar_usuario` en `core/enganches/historico.py` escribe `### N · Usuario — hora` con el mensaje tapado. `AnalisisEnCurso` cuenta los turnos por `### N · Usuario`, así que un aviso firmado distinto no cuenta como turno del usuario. Se buscó `· Usuario` en `core/`: lo leen `historico.py` y `analisis_en_curso.py`, que no cambia.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/historico.py` | Modificar | Servicio | `es_aviso_interno` y la firma |
| `proyectos/cimiento/core/enganches/tests_avisos_internos.py` | Nuevo | Test | |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 55.6.0, MENOR |

### 2.2 a 2.5

No aplica.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Las marcas van en una sola tupla, `AVISOS_INTERNOS`, que la fase `B` importa | Repetirlas en cada enganche | Si Claude Code las cambia, se ajustan en un sitio | Propuesta del agente |
| El aviso conserva su número de turno en el histórico | Anotarlo sin número | El número ordena la transcripción; el análisis solo cuenta los de «Usuario» | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `es_aviso_interno` y la firma en `anotar_usuario` | Servicio | 0,5 h | — | EV-01 |
| T-02 | `tests_avisos_internos.py` | Test | 0,5 h | T-01 | EV-01 |
| T-03 | CHANGELOG y VERSION | Versión | 0,1 h | T-02 | |

**Total estimado:** 1,1 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | `tests_avisos_internos` | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` |

## 6. a 10.

No aplica: sin datos, sin despliegue y sin riesgos abiertos.

## 11. Definition of Done

- [ ] CA-01 verificado

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-06, con la versión 55.6.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
