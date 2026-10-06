# Plan de Trabajo · Fase B-EP-025-HU-027-la-ayuda-en-vivo (módulo Cimiento, ayuda)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-027-la-ayuda-en-vivo` |
| **Épica** | `EP-025` |
| **HU** | [`HU-027`](../HU-027-la-pantalla-se-entera-en-el-momento.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/ayuda/` |
| **Especificación del módulo** | [HU-027](../HU-027-la-pantalla-se-entera-en-el-momento.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `B-EP-025-HU-026-la-ayuda-de-gasto`, que decía que lo nuevo se trae con el botón. Va aparte de la fase `A` porque la ayuda es otro módulo (`02·F11`).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-027` que cierra esta fase | Estado |
|---|---|
| CA-03 | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que la ayuda diga que lo nuevo aparece solo, y que la lista de rutas que no son pantalla conozca `consumo:aviso` y `consumo:eventos`.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-03 | La ayuda dice que se actualiza sola | Documental | Baja |

**Fuera de alcance:** la pantalla, fase `A`.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`gasto.html` dice «para ver lo más reciente, oprimir ↻». `NO_SON_PANTALLAS`, en `secciones.py`, no tiene las dos rutas nuevas, y la prueba de cobertura de la ayuda las pediría.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/gasto.html` | Modificar | UI | |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Servicio | `consumo:aviso` y `consumo:eventos` |
| `proyectos/cimiento/core/ayuda/tests_gasto.py` | Modificar | Test | |

### 2.2 a 2.8

No aplica.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reescribir el paso de actualizar y «Qué debe pasar» | UI | 0,2 h | — | EV-01 |
| T-02 | Las dos rutas en `NO_SON_PANTALLAS` | Servicio | 0,1 h | — | EV-01 |
| T-03 | Ajustar la prueba de la sección | Test | 0,2 h | T-01 | EV-01 |

**Total estimado:** 0,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 | `manage.py test core.ayuda` | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `manage.py test core.ayuda` | `resultado_pruebas.md` |

## 6. a 10.

No aplica: sin datos, sin despliegue y sin riesgos.

## 11. Definition of Done

- [ ] CA-03 verificado

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-06, con la versión 55.5.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
