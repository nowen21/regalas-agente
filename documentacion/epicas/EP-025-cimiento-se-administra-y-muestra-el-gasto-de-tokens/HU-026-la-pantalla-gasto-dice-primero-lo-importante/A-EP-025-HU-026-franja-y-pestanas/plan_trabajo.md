# Plan de Trabajo · Fase A-EP-025-HU-026-franja-y-pestanas (módulo Cimiento, consumo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-026-franja-y-pestanas` |
| **Épica** | `EP-025` |
| **HU** | [`HU-026`](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | [HU-026](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-025-HU-008-tablero-en-vivo`, que armó la pantalla con 20 bloques del mismo peso y el refresco de 10 segundos. Sale del análisis 1 del pendiente 124, acuerdos 1, 2 y 3. La ayuda, en `core/ayuda/`, va en la fase `B` (`02·F11`).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-026` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md#ca-01--la-franja-dice-el-total-y-si-sube-o-baja) | ☐ |
| [CA-02](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md#ca-02--cinco-pestañas-cada-una-con-lo-suyo) | ☐ |
| [CA-03](../HU-026-la-pantalla-gasto-dice-primero-lo-importante.md#ca-03--contexto-muestra-promedio-máximo-y-límite) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** la pantalla «Gasto» con la franja fija arriba y cinco pestañas, sin repetidos y sin intervalos.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Franja con total y variación | Funcional | Media |
| CA-02 | Cinco pestañas | Funcional | Media |
| CA-03 | Contexto con promedio, máximo y límite | Funcional | Baja |
| RNF-01 | Cada pestaña corre solo sus consultas | No funcional | Baja |
| RNF-02 | Solo Tabler, htmx y ApexCharts | No funcional | Baja |

**Fuera de alcance:** la ayuda (fase `B`) y la actualización por aviso (HU-027).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`GastoDelPeriodo.todo()` en `tablero.py` arma los 20 bloques; `DatosDelTablero` los devuelve en `_datos.html` cada 10 segundos (`hx-trigger="every 10s"`). El límite de cada proyecto sale de `Proyecto.ajuste("limite_enganche")` y `("limite_archivo")`; el común, de `catalogo.efectivos`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/tablero.py` | Modificar | Servicio | Sumas nuevas |
| `proyectos/cimiento/core/consumo/views.py` | Modificar | Endpoint | Franja y pestañas |
| `proyectos/cimiento/core/consumo/urls.py` | Modificar | Endpoint | |
| `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | Modificar | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_franja.html` | Nuevo | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_resumen.html` | Nuevo | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_donde.html` | Nuevo | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_contexto.html` | Nuevo | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_ahorro.html` | Nuevo | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_actividad.html` | Nuevo | UI | |
| `proyectos/cimiento/core/consumo/templates/consumo/_datos.html` | Eliminar | UI | Lo reemplazan las seis partes |
| `proyectos/cimiento/core/consumo/tests_tablero.py` | Modificar | Test | |
| `proyectos/cimiento/core/consumo/tests_segunda_tanda.py`, `proyectos/cimiento/core/consumo/tests_tercera_tanda.py` | Modificar | Test | Ampliación aprobada por el usuario el 2026-10-06: piden `/gasto/datos/`, que sale; faltaban en la matriz 2.2 |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 55.4.0, MENOR |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `views.py` | Sale `DatosDelTablero` y la ruta `consumo:datos` | `tests_tablero.py` | Pide `/gasto/datos/` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Método + ruta | Autenticación | Permiso | Alcance |
|---|---|---|---|
| `GET /gasto/` | Sí | El mismo de hoy | Global |
| `GET /gasto/franja/` | Sí | El mismo | Global |
| `GET /gasto/pestana/<nombre>/` | Sí | El mismo | Global; un nombre que no existe da 404 |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Gasto» en el menú de la izquierda, sin cambio.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cada pestaña es una ruta que htmx pide al elegirla | Traer todo y esconder | Así cada pestaña corre solo sus consultas (RNF-01) | Análisis 1, acuerdo 1 |
| La hora de la última actualización se muestra como hora fija, «Actualizado a las HH:MM:SS» | «Hace X segundos» | Contar segundos en la pantalla es un reloj (acuerdo 4) | Análisis 1, acuerdo 4 |
| Sin `hx-trigger="every"`: se actualiza con el botón hasta la HU-027 | Dejar los 10 segundos mientras tanto | Los 10 segundos no tienen acuerdo | Análisis 1, acuerdo 4 |
| Con «Todos», el límite que se muestra es el común de Cimiento | No mostrar límite | Es el que rige a los proyectos sin ajuste propio | Análisis 1, acuerdo 3 |
| La pestaña se recuerda en la dirección (`?pestana=`) | Guardarla en el navegador | Se puede compartir y recargar | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: la pantalla solo lee.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 · Franja

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `franja()`: total, tramo anterior, variación, llamadas, % caché, contexto máximo | Servicio | 1 h | — | EV-01 |
| T-02 | Vista, ruta y `_franja.html` | UI | 1 h | T-01 | EV-01 |

### CA-02 · Pestañas

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | `por_dia_por_tipo`, `agrupar`, `ahorro`, `actividad` | Servicio | 1,5 h | — | EV-01 |
| T-04 | Vista y ruta de pestaña; `tablero.html` con la barra de pestañas | UI | 1 h | T-03 | EV-01 |
| T-05 | Las cinco plantillas de pestaña y las dos gráficas del Resumen | UI | 2 h | T-04 | EV-02 |
| T-06 | Quitar `_datos.html` y la gráfica «Por proyecto» | UI | 0,2 h | T-05 | EV-01 |

### CA-03 · Contexto

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-07 | `contexto_por_vez()` con promedio, máximo y límite | Servicio | 0,5 h | — | EV-01 |

### Pruebas y versión

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-08 | `tests_tablero.py` | Test | 1,5 h | T-01 a T-07 | EV-01 |
| T-09 | CHANGELOG y VERSION 55.4.0 | Versión | 0,2 h | T-08 | |

**Total estimado:** 8,9 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-03, T-07, T-02, T-04, T-05, T-06, T-08, T-09.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | `tests_tablero` | EV-01 | | ☐ |
| CA-02 | `tests_tablero` y recorrido en el navegador | EV-01, EV-02 | | ☐ |
| CA-03 | `tests_tablero` | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `manage.py test core.consumo.tests_tablero` | `resultado_pruebas.md` |
| EV-02 | Recorrido de las cinco pestañas en `http://127.0.0.1:8015/gasto/` | `resultado_pruebas.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | `manage.py test` local; la pantalla en `runserver` local |
| Usuarios de prueba | La cuenta de consulta que arman las pruebas |
| Datos precargados | Los de `ConGasto` en `tests_tablero.py` |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit devuelve la pantalla anterior.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica porque no cambia datos: solo la pantalla.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md), `00·ID7` en los textos de la pantalla.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Sin el refresco de 10 segundos la pantalla queda quieta | Hasta la HU-027 hay que oprimir ↻ | La HU-027 va enseguida | Abierto |

## 11. Definition of Done

- [ ] CA-01 a CA-03 verificados con evidencia
- [ ] Pruebas de `core.consumo` en verde
- [ ] Rama lista para el commit único de la fase

## 13. Cierre

Las 9 tareas quedaron hechas el 2026-10-06, con la versión 55.4.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** 1: dos pruebas fuera del plan pedían /gasto/datos/; el usuario aprobó ampliar el plan el 2026-10-06.
