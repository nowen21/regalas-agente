# Plan de Trabajo · Fase A-EP-025-HU-028-el-trabajo-abierto (módulo El gasto)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-028-el-trabajo-abierto` |
| **Épica** | `EP-025` |
| **HU** | [`HU-028`](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md), una sola (`F12.1`) |
| **Módulo** | El gasto: `core/consumo/` |
| **Especificación del módulo** | Los CA de la HU-028 |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, con «apruebo» a las opciones 1 y 2, el 2026-10-08, con la versión 58.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-025-HU-010-segunda-tanda`, que creó el trabajo de cada mensaje.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-028` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md#ca-01--el-análisis-prendido-es-el-trabajo-del-mensaje) | ☐ |
| [CA-02](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md#ca-02--se-reconocen-todas-las-fases-y-las-órdenes-de-consola) | ☐ |
| [CA-03](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md#ca-03--el-mensaje-sin-rastro-sigue-en-el-trabajo-de-la-conversación) | ☐ |
| [CA-04](../HU-028-el-trabajo-de-cada-mensaje-sale-de-lo-que-esta-abierto.md#ca-04--lo-ya-guardado-se-recalcula) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que cada mensaje quede con su trabajo: el análisis prendido, la fase o el análisis que tocó su turno, o el de su conversación.

**Fuera de alcance:** enlazar el mensaje con la transcripción.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`trabajo.py` busca `A-EP-NNN-HU-NNN` y `analisis-N.md` en las rutas que el turno pasa a las herramientas de archivos; las órdenes de consola no cuentan. En el `.jsonl`, el aviso «[ANÁLISIS EN CURSO]» es un `hook_additional_context` de `UserPromptSubmit` que va justo después del mensaje (verificado en la sesión de hoy). La base tiene 102.478 líneas de sesión de 66 archivos y 3.667 mensajes.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/trabajo.py` | Modificar | Lógica | Todas las fases; el trabajo del aviso |
| `proyectos/cimiento/core/consumo/lector.py` | Modificar | Lógica | El aviso de cada mensaje y las órdenes de consola |
| `proyectos/cimiento/core/consumo/guardar.py` | Modificar | Lógica | El orden de las fuentes y la herencia |
| `proyectos/cimiento/core/consumo/models.py` | Modificar | Modelo | `Pedido.origen` |
| `proyectos/cimiento/core/consumo/migrations/0006_origen_del_trabajo.py` | Crear | Migración | |
| `proyectos/cimiento/core/consumo/management/commands/recalcular_trabajo.py` | Crear | Orden | |
| `proyectos/cimiento/core/consumo/tablero.py` | Modificar | Lógica | El origen en los últimos mensajes |
| `proyectos/cimiento/core/consumo/templates/consumo/_actividad.html` | Modificar | Plantilla | Dice cuándo el trabajo sigue de la conversación |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Lógica | El «?» de «Trabajo» explicaba mal de dónde sale |
| `proyectos/cimiento/core/consumo/tests_trabajo_abierto.py` | Crear | Test | |
| `proyectos/cimiento/core/consumo/tests_segunda_tanda.py` | Modificar | Test | Si sus casos cambian con la herencia |
| `historico-chat/scripts/2026-10-08/README.md` | Modificar | Índice | |
| `historico-chat/scripts/2026-10-08/salida_recalcular_trabajo.txt` | Crear | Evidencia | Antes y después en la base real |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `lector.py`, `guardar.py`, `trabajo.py` | El vigilante y `leer_consumo` | `core.consumo` |
| `textos.py` | La ayuda | `core.ayuda` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Gasto de tokens → «Dónde se gasta» → Trabajo, y «Actividad».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El análisis se lee del aviso que ya queda en el `.jsonl` | Agregar una línea «[TRABAJO]» al aviso de cada mensaje | No cuesta tokens (RNF-01) | |
| La fase de un mensaje sin rastro sale de la conversación | Que el freno anote la fase en curso | El freno solo corre cuando hay acciones, y entonces ya hay rutas; y hay varias fases abiertas a la vez, de otras sesiones | Docstring de `trabajo.py` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

`recalcular_trabajo` se puede volver a correr: el resultado es el mismo. La migración se devuelve con `migrate consumo 0005`.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El aviso del análisis y las órdenes de consola en la lectura; todas las fases | Lógica | 1 h | Ninguna | EV-01 |
| T-02 | `origen`, el orden de las fuentes y la herencia | Lógica | 1 h | T-01 | EV-01 |
| T-03 | `recalcular_trabajo` y correrla en la base real | Orden | 0,5 h | T-02 | EV-01, EV-02 |
| T-04 | La pantalla y la ayuda | Plantilla | 0,25 h | T-02 | EV-01 |

**Total estimado:** 2,75 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |
| CA-03 | Prueba de Django | EV-01 | | ☐ |
| CA-04 | Prueba de Django y la base real | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Antes y después en la base real | `historico-chat/scripts/2026-10-08/salida_recalcular_trabajo.txt` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; la base real para recalcular |
| Usuarios de prueba | Ninguno |
| Datos precargados | Líneas de `.jsonl` armadas en la prueba |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `migrate consumo 0005`. El trabajo recalculado se rehace con la versión anterior de `recalcular_trabajo`, que no existe: se acepta, porque el anterior era el 93 % vacío.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: un campo con valor vacío por defecto. Después de migrar, `manage.py recalcular_trabajo` una vez.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F10`, `00·N6`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
