# Plan de Trabajo · Fase A-EP-025-HU-031-formatos-de-las-plantillas (módulo herramientas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-031-formatos-de-las-plantillas` |
| **Épica** | `EP-025` |
| **HU** | [`HU-031`](../HU-031-cerrar-fase-entiende-los-formatos-de-las-plantillas-y-marca-todo-lo-que-cierra.md), una sola (`F12.1`) |
| **Módulo** | Herramientas de Cimiento, `proyectos/cimiento/core/herramientas/` |
| **Especificación del módulo** | La HU-031 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 150](../../../../../historico-chat/resumenes/2026-10-09/pendientes/150-cerrar-fase-lee-todos-los-casos-y-marca-todo-lo-que-cierra/analisis-1.md), el 2026-10-09, en el turno 22, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 150, acuerdos 1 a 3, puntos 1 y 2 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-031` que cierra esta fase | Estado |
|---|---|
| CA-01 · Lee los planes en el formato de las plantillas | ☑ |
| CA-02 · Marca todo lo que cierra, y reabrir lo desmarca | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** `cerrar_fase` lee la matriz y los CA en los formatos de las plantillas y marca todo lo que la fase cierra; `reabrir_fase` lo desmarca.

**Fuera de alcance:** marcar las fases ya cerradas; pasar los documentos a la base (EP-030·HU-004).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`Fase.casos()` (`fase.py:148`) solo toma filas con un caso sin enlace; `Fase.plan()` (`fase.py:125`) solo toma CA como «CA-01 · nombre». La segunda pasada (`_marcar_cerrada`) marca la matriz con el mismo formato, los CA, el cierre del plan, la HU y la épica; no marca la sección 5 ni las Definition of Done. Las pruebas (`tests_fase.py`, 9 casos) usan solo el formato viejo. Las plantillas están en `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md` y `08-plan-pruebas.md`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/fase.py` | Modificar | Lógica | Leer y marcar en los formatos de las plantillas |
| `proyectos/cimiento/core/herramientas/tests_fase.py` | Modificar | Test | Casos con el formato de las plantillas |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: es la consola (`manage.py cerrar_fase` y `reabrir_fase`).

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| De cada fila de la matriz se sacan todos los `CP-NNN` de su celda | Exigir un caso por fila | Es lo que pide la plantilla | Acuerdo 1 |
| La Definition of Done del plan se marca menos la casilla del commit | Marcarla entera | El commit es la estación 12, que no hace el cierre | Propuesta del agente |
| Las tareas y la Definition of Done de la HU se desmarcan solo al reabrir | Desmarcarlas también al cerrar una fase con la HU en curso | Al cerrar no se borra lo que alguien marcó a mano | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

`reabrir_fase` desmarca lo que esta fase hace marcar a `cerrar_fase`.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer la matriz y los CA en los formatos de las plantillas | Lógica | 0,5 h | — | EV-01 |
| T-02 | Marcar y desmarcar la matriz, los CA, la sección 5 y las Definition of Done | Lógica | 1 h | T-01 | EV-01 |
| T-03 | Pruebas con el formato de las plantillas | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 2,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas | EV-01 | 2026-10-09 | ☑ |
| CA-02 | Pruebas | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Una fase de juguete en una carpeta temporal |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F7`, `02·F30`, `08·T1`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que las fases en el formato viejo cierren distinto | Se rompe lo que funciona | Las 9 pruebas que ya había siguen pasando | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** ninguno.
