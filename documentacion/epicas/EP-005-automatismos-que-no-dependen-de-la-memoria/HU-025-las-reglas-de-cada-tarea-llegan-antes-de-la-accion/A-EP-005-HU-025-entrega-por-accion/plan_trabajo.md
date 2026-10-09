# Plan de Trabajo · Fase A-EP-005-HU-025-entrega-por-accion (módulo enganches de reglas)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-025-entrega-por-accion` |
| **Épica** | `EP-005` |
| **HU** | [`HU-025`](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md), una sola (`F12.1`) |
| **Módulo** | Enganches de reglas: `proyectos/cimiento/core/herramientas/` y `adaptadores/claude-code/` |
| **Especificación del módulo** | La HU-025 y la [épica EP-005](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-1.md), el 2026-10-09, en el turno 30, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): retoma la promesa de la HU-023 de la EP-005 (elegir las reglas también por la acción, escrita en `base/tareas.md` y nunca conectada), según el análisis 1 del pendiente 133, acuerdos 1, 2 y 6.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-025` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md#ca-01--antes-de-la-acción-llegan-las-reglas-de-su-tarea) | ☐ |
| [CA-02](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md#ca-02--cada-regla-llega-una-sola-vez-por-sesión-y-por-agente) | ☐ |
| [CA-03](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md#ca-03--con-cada-mensaje-llega-solo-lo-que-falta) | ☐ |
| [CA-04](../HU-025-las-reglas-de-cada-tarea-llegan-antes-de-la-accion.md#ca-04--el-aviso-de-las-señales-llega-una-vez-al-abrir-la-sesión) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** antes de cada acción le llegan al agente las reglas de su tarea, una sola vez por sesión y por agente; con cada mensaje llega solo lo que falta de `responder` y `recibir-pedido`; y el aviso de las señales llega una vez, al abrir la sesión.

**Fuera de alcance:** cambiar `base/tareas.md` (CA-05, fase B), partir `cambiar-codigo` (HU-026) y lo que vuelve después de un resumen (HU-027).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`MapaDeTareas.acciones()` (`core/herramientas/mapa_tareas.py`) ya lee la columna de acciones de `base/tareas.md`, pero solo la usa un guion de `historico-chat/scripts/`. `hook_antes.py` corre en `PreToolUse` y solo frena. `hook_reglas.py` arma con cada mensaje el bloque «LAS REGLAS DE CADA TURNO», los títulos de `recibir-pedido` y `responder` y el texto de las tareas que pide la palabra (`RecuperadorDeReglas.como_texto`). `hook_senales.py` corre en `UserPromptSubmit` y busca la sesión en `CLAUDE_SESSION_ID`, que Claude Code no llena: por eso avisa en cada mensaje. El catálogo de enganches vive en `core/comun/enganches.py`, y `instalar.py` lo copia a `.claude/settings.json`. Lo que no se versiona va en `historico-chat/.estado/` (`.gitignore`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/entrega_de_reglas.py` | Crear | Lógica | La tarea de cada acción, lo entregado por sesión y agente, y el texto de cada entrega |
| `proyectos/cimiento/core/herramientas/tests_entrega_de_reglas.py` | Crear | Test | |
| `adaptadores/claude-code/hook_reglas_accion.py` | Crear | Enganche | `PreToolUse`: entrega las reglas de la acción por `additionalContext` |
| `adaptadores/claude-code/hook_reglas.py` | Modificar | Enganche | Sin el bloque de cada turno; usa la entrega del mensaje |
| `adaptadores/claude-code/hook_senales.py` | Modificar | Enganche | Lee la sesión de la entrada; corre al abrir la sesión |
| `proyectos/cimiento/core/comun/enganches.py` | Modificar | Catálogo | El enganche nuevo, y las señales en `SessionStart` |
| `proyectos/cimiento/core/enganches/tests_suspendidos.py` | Modificar | Test | Si nombra el momento de las señales en `UserPromptSubmit` |
| `.claude/settings.json` | Modificar | Configuración | Lo reescribe `instalar.py` desde el catálogo |

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
| La entrega por acción va en un enganche propio de `PreToolUse` | Meterla en `hook_antes.py` | Suspender el freno apagaría también las reglas, y cada uno se suspende por su nombre | Propuesta del agente |
| Lo entregado se guarda por sesión en `historico-chat/.estado/reglas-entregadas/`, con la cuenta de cada agente | Guardarlo en la base | Es estado de trabajo, como el del análisis en curso, y el enganche lo lee en cada acción | Propuesta del agente |
| Cuando todas las reglas de la tarea ya llegaron, el enganche sale sin leer el estándar | Leerlo en cada acción | Corre antes de toda acción: leer la base cada vez demora el trabajo | Propuesta del agente |
| Si una tarea no cabe completa, llega por partes en las acciones siguientes | Mandar solo los títulos | Así la regla llega completa antes de que se use, sin pasar del tope | Acuerdo 1 |
| Las palabras que autorizan cambiar algo son las que no están en la primera tabla de `palabras-clave.md` | Una lista escrita en el programa | La lista la dueña el estándar | Acuerdo 1 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

El enganche nuevo se suspende por su momento desde Cimiento, y `instalar.py --desinstalar` lo quita. El archivo de estado de una sesión se puede borrar: la entrega vuelve a empezar.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La tarea de cada acción y lo entregado por sesión y agente | Lógica | 1 h | — | EV-01 |
| T-02 | El enganche de antes de la acción | Enganche | 0,5 h | T-01 | EV-01 |
| T-03 | La entrega del mensaje y el enganche de cada mensaje | Enganche | 1 h | T-01 | EV-01 |
| T-04 | Las señales al abrir la sesión, y el catálogo | Enganche | 0,5 h | — | EV-01 |
| T-05 | Pruebas | Test | 1 h | T-01 a T-04 | EV-01 |

**Total estimado:** 4 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |
| CA-04 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales con un estándar de prueba |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y volver a correr `instalar.py`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base. Los proyectos que heredan reciben el enganche nuevo con `instalar.py`.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `00·M13`, `01·C28`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Un enganche más antes de cada acción | Cada acción tarda un poco más | Sale sin leer el estándar cuando todo ya llegó | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
