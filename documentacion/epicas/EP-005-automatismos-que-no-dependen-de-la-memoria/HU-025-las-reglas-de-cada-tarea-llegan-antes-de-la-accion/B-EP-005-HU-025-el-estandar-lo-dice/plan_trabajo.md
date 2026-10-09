# Plan de Trabajo · Fase B-EP-005-HU-025-el-estandar-lo-dice (módulo estándar)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-025-el-estandar-lo-dice` |
| **Épica** | `EP-005` |
| **HU** | [`HU-025`](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md), una sola (`F12.1`) |
| **Módulo** | Estándar: `base/tareas.md`, que vive en la base de Cimiento |
| **Especificación del módulo** | La HU-025 y la [épica EP-005](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), el 2026-10-09, en el turno 30, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): sigue a `A-EP-005-HU-025-entrega-por-accion`, que cambió cuándo llegan las reglas; esta fase lo escribe en el estándar.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-025` que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md#ca-05--el-estándar-dice-cuándo-llegan-las-reglas) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** `base/tareas.md` dice que la acción trae las reglas de su tarea y que el mensaje trae solo las de `responder` y `recibir-pedido`, una sola vez; y la versión sube como MENOR.

**Fuera de alcance:** cambiar la tabla de tareas (es la HU-026).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`base/tareas.md` vive en la base; se lee con `manage.py documento ver estandar base/tareas.md` (copia en `historico-chat/scripts/2026-10-09/tareas-antes.txt`). Su sección «Cómo se elige la tarea» dice que con cada mensaje la palabra clave trae las reglas de las tareas de la tercera columna. `manage.py documento editar` deja una propuesta, que se aprueba en Cimiento → Estándar → Propuestas, y `manage.py registrar_version` sube la versión en la base. Con el estándar congelado, `base/`, `VERSION` y `CHANGELOG.md` no se escriben a mano.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `historico-chat/scripts/2026-10-09/tareas-antes.txt` | Crear | Apoyo | El texto que tenía la base |
| `historico-chat/scripts/2026-10-09/tareas-despues.txt` | Crear | Apoyo | El texto que se propone |
| `base/tareas.md` | Modificar | Estándar | Por propuesta en la base, con `manage.py documento editar` |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Cimiento → Estándar → Propuestas, donde el usuario aprueba el cambio.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se cambia solo la sección «Cómo se elige la tarea» | Quitar la tercera columna de la tabla | La columna sigue diciendo qué tarea anuncia cada palabra; quitarla toca el mapa y es otra decisión | Propuesta del agente |
| La versión sube como MENOR | MAYOR | No obliga a un proyecto a hacer nada: llega con `instalar.py` | Análisis 1 del pendiente 133, «El entorno» |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

La propuesta se rechaza en la misma pantalla, y un cambio aprobado se revierte con otra propuesta.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Escribir el texto nuevo y proponerlo | Estándar | 0,3 h | — | EV-01 |
| T-02 | Subir la versión cuando el usuario apruebe | Estándar | 0,1 h | T-01 | EV-01 |

**Total estimado:** 0,4 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-05 | Leer `base/tareas.md` de la base y la versión | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `documento ver` y de `registrar_version` | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de Cimiento |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Rechazar la propuesta, o proponer el texto anterior.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: `20·M10`, `00·N1`, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | La propuesta espera la aprobación del usuario en la pantalla | La fase no cierra hasta entonces | Se le pide al usuario | Abierto |

## 11. Definition of Done

- [ ] El CA de la sección 0 verificado con evidencia en la sección 5
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
