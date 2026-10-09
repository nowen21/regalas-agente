# Plan de Trabajo · Fase A-EP-005-HU-026-temas-por-archivo (módulo enganches de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-026-temas-por-archivo` |
| **Épica** | `EP-005` |
| **HU** | [`HU-026`](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md), una sola (`F12.1`) |
| **Módulo** | Enganches de reglas: `proyectos/cimiento/core/herramientas/`, y `base/tareas.md` por propuesta |
| **Especificación del módulo** | La HU-026 y la [épica EP-005](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 2 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-2.md), el 2026-10-09, en el turno 37, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): retoma `A-EP-005-HU-025-entrega-por-accion`, que entrega todas las reglas de `cambiar-codigo` sin importar el archivo (análisis 2 del pendiente 133, acuerdo 1).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-026` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md#ca-01--cada-archivo-recibe-solo-los-temas-que-toca) | ☐ |
| [CA-02](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md#ca-02--el-archivo-que-no-encaja-recibe-todos-los-temas) | ☐ |
| [CA-03](../HU-026-las-reglas-de-cambiar-codigo-llegan-partidas-segun-lo-que-se-toca.md#ca-03--la-tabla-de-temas-está-en-el-estándar) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** al escribir código llegan solo las reglas de los temas que toca el archivo, según la tabla de `base/tareas.md`; sin tabla, o con un archivo que no encaja, llegan todas.

**Fuera de alcance:** cambiar la línea `**Aplica a:**` de cada regla.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`EntregaDeReglas.para_la_accion` (`core/herramientas/entrega_de_reglas.py`) guarda en el estado de la sesión la columna de acciones y entrega todas las reglas de la tarea. `RecuperadorDeReglas.capitulo` da el capítulo de cada regla. `base/tareas.md` vive en la base y tiene pendiente la propuesta 18; la tabla de temas va en una propuesta nueva que parte del texto de la 18 (`historico-chat/scripts/2026-10-09/tareas-despues.txt`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/entrega_de_reglas.py` | Modificar | Lógica | Lee la tabla de temas y filtra las reglas de código por capítulo |
| `proyectos/cimiento/core/herramientas/tests_entrega_de_reglas.py` | Modificar | Test | |
| `historico-chat/scripts/2026-10-09/tareas-con-temas.txt` | Crear | Apoyo | El texto de `base/tareas.md` con la tabla, para la propuesta |
| `base/tareas.md` | Modificar | Estándar | Por propuesta en la base, con `manage.py documento editar` |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Cimiento → Estándar → Propuestas, para aprobar la tabla.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La tabla va en una sección propia de `base/tareas.md`, con tema, patrones de archivo y capítulos | Escribirla en el programa | El estándar es el dueño de qué regla aplica | Acuerdo 1 |
| Un patrón que termina en `/` busca la carpeta en la ruta; los demás se comparan con el nombre del archivo | Expresiones regulares | Los patrones con `*` se leen sin saber programar | Propuesta del agente |
| El tema `todos` va siempre, y no cuenta para decidir si el archivo encajó | Repetir sus capítulos en cada tema | Una sola fila dice lo que reciben todos | Acuerdo 1 |
| Lo ya entregado de una tarea se cuenta por tarea y temas: escribir una prueba no cierra la tarea para un `views.py` | Una sola cuenta por tarea | Si no, el `views.py` no recibiría sus temas | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

La propuesta se rechaza en la misma pantalla; sin la tabla, la entrega vuelve a ser la de la HU-025.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Leer la tabla y elegir los capítulos por la ruta | Lógica | 1 h | — | EV-01 |
| T-02 | Pruebas | Test | 0,5 h | T-01 | EV-01 |
| T-03 | Escribir la tabla y proponerla | Estándar | 0,3 h | — | EV-02 |

**Total estimado:** 1,8 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | La propuesta en la base | EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | El número de la propuesta | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales con el estándar leído del disco y la tabla de `tareas-con-temas.txt` |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y rechazar la propuesta.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base de datos.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `20·M10`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La propuesta nueva parte del texto de la 18, que no está aprobada | Si la 18 se rechaza, la nueva se rehace | Se le pide al usuario aprobar la 18 antes | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
