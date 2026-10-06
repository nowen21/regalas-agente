# Plan de Trabajo · Fase B-EP-025-HU-026-la-ayuda-de-gasto (módulo Cimiento, ayuda)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-026-la-ayuda-de-gasto` |
| **Épica** | `EP-025` |
| **HU** | [`HU-026`](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/ayuda/` |
| **Especificación del módulo** | [HU-026](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-025-HU-018-la-ayuda`, que describió la pantalla vieja. Va aparte de la fase `A` porque la ayuda es otro módulo (`02·F11`).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-026` que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md#ca-04--la-ayuda-describe-la-pantalla-nueva) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que la ayuda de «Gasto» describa la franja, las cinco pestañas y el botón de actualizar, sin «cada 10 segundos».

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-04 | La ayuda describe la pantalla nueva | Documental | Baja |

**Fuera de alcance:** la pantalla, que es la fase `A`.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`core/ayuda/templates/ayuda/secciones/gasto.html` dice «se actualizan solas cada 10 segundos». Ninguna prueba de `core/ayuda` lee esa sección.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/gasto.html` | Modificar | UI | |
| `proyectos/cimiento/core/ayuda/tests_gasto.py` | Nuevo | Test | |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Servicio | Las rutas que no son pantalla: sale `consumo:datos`, entran `consumo:franja` y `consumo:pestana` |

### 2.2 a 2.5

No aplica.

### 2.6 Decisiones técnicas

Ninguna.

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica.

## 3. Desglose de tareas por criterio de aceptación

### CA-04

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reescribir la sección | UI | 0,3 h | — | EV-01 |
| T-02 | Prueba que lee la sección | Test | 0,3 h | T-01 | EV-01 |

**Total estimado:** 0,6 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 | Prueba de la sección | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `manage.py test core.ayuda` | `resultado_pruebas.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | `manage.py test` local |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), `00·ID7`.

## 10. Riesgos y bloqueos

Ninguno.

## 11. Definition of Done

- [ ] CA-04 verificado

## 13. Cierre

Las 2 tareas quedaron hechas el 2026-10-06, con la versión 55.4.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
