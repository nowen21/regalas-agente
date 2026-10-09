# Plan de Trabajo · Fase A-EP-005-HU-027-nucleo-y-resumen (módulo enganches de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-027-nucleo-y-resumen` |
| **Épica** | `EP-005` |
| **HU** | [`HU-027`](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md), una sola (`F12.1`) |
| **Módulo** | Enganches de reglas: `proyectos/cimiento/core/herramientas/` y `adaptadores/claude-code/` |
| **Especificación del módulo** | La HU-027 y la [épica EP-005](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), el 2026-10-09, en el turno 30, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): retoma `A-EP-005-HU-025-entrega-por-accion`, que dejó como deuda que lo entregado se pierde al resumirse la conversación (análisis 1 del pendiente 133, acuerdos 4 y 5).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-027` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md#ca-01--al-abrir-la-sesión-llega-el-núcleo-completo) | ☐ |
| [CA-02](../HU-027-el-nucleo-llega-completo-y-lo-entregado-vuelve-despues-de-un-resumen.md#ca-02--después-de-un-resumen-vuelve-lo-entregado) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** al abrir la sesión llega el núcleo, y lo que no cabe llega con los mensajes siguientes; después de un resumen, la cuenta del agente principal vuelve a cero, así que el núcleo, `responder` y las tareas usadas llegan otra vez.

**Fuera de alcance:** los subagentes, que no se resumen con la conversación principal.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`EntregaDeReglas` (`core/herramientas/entrega_de_reglas.py`, de la HU-025) guarda lo entregado por sesión y agente. Las reglas blindadas solo existen en el núcleo (`metareglas.py`, `blindada_solo_en_el_nucleo`): el núcleo son las blindadas vigentes, unos 24 KB, más que el tope de unos 8,5 KB. `SessionStart` trae `source`: `startup`, `resume`, `clear` o `compact`. Ningún enganche de `SessionStart` entrega reglas.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/entrega_de_reglas.py` | Modificar | Lógica | El núcleo como una tarea más, y volver a cero después de un resumen |
| `proyectos/cimiento/core/herramientas/tests_entrega_de_reglas.py` | Modificar | Test | |
| `adaptadores/claude-code/hook_reglas_sesion.py` | Crear | Enganche | `SessionStart`: el núcleo, y volver a cero con `compact` o `clear` |
| `proyectos/cimiento/core/comun/enganches.py` | Modificar | Catálogo | El enganche nuevo y su momento |
| `.claude/settings.json` | Modificar | Configuración | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: son enganches de Claude Code.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El núcleo se entrega como una tarea más, `nucleo`, que el mensaje sigue entregando hasta completarla | Mandarlo entero al abrir | No cabe en el tope de un enganche | Acuerdo 4 |
| Después de `compact` o `clear`, la cuenta del agente principal vuelve a cero | Volver a mandar todo en el mismo enganche | No cabe: lo demás vuelve con el mensaje y con cada acción, que ya saben entregar lo que falta | Acuerdo 5 |
| Va en un enganche propio de `SessionStart` | Meterlo en `hook_sesion.py` | Cada momento se suspende por su nombre | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

El enganche se suspende desde Cimiento por su momento, y `instalar.py --desinstalar` lo quita.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El núcleo como tarea y volver a cero | Lógica | 0,5 h | — | EV-01 |
| T-02 | El enganche de `SessionStart` y el catálogo | Enganche | 0,5 h | T-01 | EV-01 |
| T-03 | Pruebas | Test | 0,5 h | T-01, T-02 | EV-01 |

**Total estimado:** 1,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales con el estándar leído del disco |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y volver a correr `instalar.py`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `00·N10`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | El núcleo no cabe en una sola entrega | Llega en el arranque y los primeros mensajes | Se entrega por partes | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
