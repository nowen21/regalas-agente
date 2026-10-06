# Plan de Trabajo · Fase A-EP-025-HU-027-aviso-y-eventos (módulo Cimiento, consumo)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-027-aviso-y-eventos` |
| **Épica** | `EP-025` |
| **HU** | [`HU-027`](../HU-027-la-pantalla-se-entera-en-el-momento.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | [HU-027](../HU-027-la-pantalla-se-entera-en-el-momento.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-025-HU-008-tablero-en-vivo` (el refresco de 10 segundos, que la HU-026 ya quitó) y `A-EP-025-HU-025-lineas-a-la-base-sin-relojes` (el vigilante, que ahora avisa). Sale del análisis 1 del pendiente 124, acuerdos 4 y 7.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-027` que cierra esta fase | Estado |
|---|---|
| CA-01 | ☐ |
| CA-02 | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** el vigilante avisa al guardar, Cimiento pasa el aviso por SSE y la pantalla vuelve a pedir lo que se ve.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | Lo nuevo aparece sin recargar ni intervalos | Funcional | Media |
| CA-02 | El aviso solo desde la misma máquina | Seguridad | Baja |
| RNF-01 | Sin bibliotecas nuevas | No funcional | Baja |
| RNF-02 | Con Cimiento apagado, a lo sumo 2 segundos por aviso | No funcional | Baja |

**Fuera de alcance:** la ayuda, fase `B` (`02·F11`).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`VigilanteDeConsumo.avisar` guarda en el hilo de `watchdog` y devuelve si hubo algo nuevo. La pantalla ya escucha el evento `actualizar` en `body` (HU-026). Toda ruta pide cuenta por `LoginRequiredMiddleware`; `login_not_required` la exime. El puerto de Cimiento está en `PUERTO` de su `.env`, que lee `config.ambiente.leer`. Se buscó `consumo:` en todo `core/`: la usa también `core/ayuda/secciones.py`, que va en la fase `B`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/avisos.py` | Nuevo | Servicio | Avisos en memoria y aviso a Cimiento |
| `proyectos/cimiento/core/consumo/views.py` | Modificar | Endpoint | Aviso y eventos |
| `proyectos/cimiento/core/consumo/urls.py` | Modificar | Endpoint | |
| `proyectos/cimiento/core/consumo/vigilante.py` | Modificar | Servicio | Avisa al guardar |
| `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | Modificar | UI | `EventSource` |
| `proyectos/cimiento/core/consumo/tests_en_vivo.py` | Nuevo | Test | |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 55.5.0, MENOR |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

No aplica: solo se agregan rutas y una llamada.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Método + ruta | Autenticación | Permiso | Alcance |
|---|---|---|---|
| `POST /gasto/aviso/` | No: la llama el vigilante | Solo desde `127.0.0.1` o `::1`; otro origen da 403 | Global |
| `GET /gasto/eventos/` | Sí | El de «Gasto» | Global |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Gasto», sin cambio: se actualiza sola.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| `EventSource` del navegador, que dispara el `actualizar` de la HU-026 | La extensión SSE de htmx | No suma bibliotecas (RNF-01) y reusa lo que ya hay | Análisis 1, acuerdo 7 |
| Los avisos viven en memoria del proceso de Cimiento, con una condición de hilos | Guardarlos en la base | La base obligaría a preguntarle cada cierto tiempo | Análisis 1, acuerdo 4 |
| El vigilante avisa con `POST` local y espera a lo sumo 2 segundos | Sin tiempo máximo | Con Cimiento colgado, el vigilante no debe quedarse esperando; es un tope, no un reloj | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: un aviso no cambia datos.

## 3. Desglose de tareas por criterio de aceptación

### CA-01 y CA-02

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `avisos.py` | Servicio | 1 h | — | EV-01 |
| T-02 | Rutas de aviso y eventos | Endpoint | 1 h | T-01 | EV-01 |
| T-03 | El vigilante avisa | Servicio | 0,5 h | T-01 | EV-01 |
| T-04 | La pantalla escucha | UI | 0,5 h | T-02 | EV-01 |
| T-05 | `tests_en_vivo.py` | Test | 1,5 h | T-01 a T-04 | EV-01 |
| T-06 | CHANGELOG y VERSION | Versión | 0,2 h | T-05 | |

**Total estimado:** 4,7 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-06.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | `tests_en_vivo` | EV-01 | | ☐ |
| CA-02 | `tests_en_vivo` | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `manage.py test core.consumo` | `resultado_pruebas.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | `manage.py test` local |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit: la pantalla queda con el botón ↻.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin datos. Hay que reiniciar Cimiento y el vigilante para que tomen el código nuevo.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), `04·S9`.

## 10. Riesgos y bloqueos

Ninguno.

## 11. Definition of Done

- [ ] CA-01 y CA-02 verificados

## 13. Cierre

Las 6 tareas quedaron hechas el 2026-10-06, con la versión 55.5.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
