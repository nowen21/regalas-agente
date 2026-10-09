# Plan de Trabajo · Fase A-EP-025-HU-030-resumen-rapido (módulo el gasto de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-030-resumen-rapido` |
| **Épica** | `EP-025` |
| **HU** | [`HU-030`](../HU-030-el-resumen-del-gasto-responde-en-la-mitad-del-tiempo-y-no-se-recalcula-con-cada-aviso.md), una sola (`F12.1`) |
| **Módulo** | El gasto de Cimiento, `proyectos/cimiento/core/consumo/` |
| **Especificación del módulo** | La HU-030 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 146](../../../../../historico-chat/resumenes/2026-10-08/pendientes/146-el-resumen-del-gasto-tarda-y-se-pide-con-cada-mensaje/analisis-1.md), el 2026-10-09, en el turno 17, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 146, acuerdos 1 a 3, puntos 1 y 2 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-030` que cierra esta fase | Estado |
|---|---|
| CA-01 · La gráfica por día suma en la base y da lo mismo | ☑ |
| CA-02 · La pantalla junta los avisos | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** el Resumen del gasto tarda menos de la mitad, y la pantalla se refresca sola como máximo cada 30 segundos.

**Fuera de alcance:** cargar las zonas horarias en MySQL; guardar el Resumen ya calculado.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Medido el 2026-10-09 sobre la base real (10.550 llamadas en 7 días): `pestana("resumen")` tarda 1,1 a 1,3 s; `por_dia_por_tipo` (`tablero.py:236`), 0,65 s. Agrupar por hora en UTC en la base tarda 0,10 s. `CONVERT_TZ` devuelve vacío: MySQL no tiene las zonas horarias. En `tablero.html:70`, cada evento `gasto` del SSE dispara `actualizar`, que escuchan la pestaña abierta y la franja.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/tablero.py` | Modificar | Lógica | `por_dia_por_tipo` y `por_dia` suman por hora en la base |
| `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | Modificar | Pantalla | Junta los avisos |
| `proyectos/cimiento/core/consumo/tests_rapido.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

La pantalla del gasto, `/gasto/`.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Agrupar por hora con `TruncHour(..., tzinfo=UTC)` y pasar cada hora a su día local en Python | Agrupar por día en la base | MySQL sin zonas horarias devuelve vacío | Acuerdo 1 |
| Las dos gráficas por día comparten una sola función que suma por hora | Arreglar cada una por su lado | Es la misma cuenta | Propuesta del agente |
| Juntar los avisos en el navegador | Juntar en el servidor | El servidor no sabe si la pantalla está escondida | Acuerdo 2 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: no crea nada que haya que deshacer.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Las gráficas por día suman por hora en la base | Lógica | 0,5 h | — | EV-01 |
| T-02 | La pantalla junta los avisos | Pantalla | 0,5 h | — | EV-01 |
| T-03 | Pruebas y medición | Test | 0,5 h | T-01, T-02 | EV-01 |

**Total estimado:** 1,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django y medición sobre la base real | EV-01 | 2026-10-09 | ☑ |
| CA-02 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas y de la medición | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; la medición, sobre la base real, sin escribir |
| Usuarios de prueba | Una cuenta del grupo de consulta |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `08·T8`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que una llamada cerca de la medianoche caiga en otro día | La gráfica cambia | Prueba con llamadas a las 23:30 y a las 00:30 hora local | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
