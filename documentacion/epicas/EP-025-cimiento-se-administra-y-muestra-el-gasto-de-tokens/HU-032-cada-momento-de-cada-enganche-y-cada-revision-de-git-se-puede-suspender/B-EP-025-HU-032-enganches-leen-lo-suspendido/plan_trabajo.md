# Plan de Trabajo · Fase B-EP-025-HU-032-enganches-leen-lo-suspendido (módulo los enganches de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-025-HU-032-enganches-leen-lo-suspendido` |
| **Épica** | `EP-025` |
| **HU** | [`HU-032`](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md), una sola (`F12.1`) |
| **Módulo** | Los enganches de Cimiento: `proyectos/cimiento/core/enganches/` y sus adaptadores en `adaptadores/claude-code/` |
| **Especificación del módulo** | La HU-032 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md), el 2026-10-09, en el turno 27, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 149, punto 2 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de `HU-032` que cierra esta fase | Estado |
|---|---|
| CA-02 · El enganche suspendido no hace nada, con una sola consulta por mensaje | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** al arrancar, cada enganche de Claude Code sabe si su momento está suspendido. En cada mensaje, el primero que gana el turno consulta la base y deja la lista; los demás esperan hasta 2 segundos y la leen. El suspendido sale sin hacer nada. El freno solo se apaga con la suspensión «freno».

**Fuera de alcance:** las revisiones de git (fase C).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Cada adaptador de `adaptadores/claude-code/` lee el JSON de la entrada a su manera y llama a su programa en `core/enganches/`; se instala con `--raiz «proyecto»`. Solo el freno lee las suspensiones, con PyMySQL (`core/enganches/niveles.py`), y **toma toda suspensión de tipo «enganche» como el freno entero** (`niveles.py:117`): con la fase A, suspender el histórico apagaría el freno. Los 8 enganches de `UserPromptSubmit` arrancan a la vez.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/suspendidos.py` | Crear | Lógica | El turno, la consulta, la lista y la salida |
| `proyectos/cimiento/core/enganches/niveles.py` | Modificar | Lógica | Solo «freno» apaga el freno entero |
| `proyectos/cimiento/core/enganches/tests_suspendidos.py` | Crear | Test | |
| `adaptadores/claude-code/hook_acuerdos.py` | Modificar | Adaptador | Sale si su momento está suspendido |
| `adaptadores/claude-code/hook_analisis.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_checklist.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_checkpoint.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_externo.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_historico.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_md.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_presupuesto.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_recuerdos.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_redaccion.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_reglas.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_relacionadas.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_resumen.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_rutas.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_senales.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_sesion.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_turno.py` | Modificar | Adaptador | Igual |
| `adaptadores/claude-code/hook_veredicto.py` | Modificar | Adaptador | Igual |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: son los enganches.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El turno se gana creando un archivo con `O_CREAT \| O_EXCL` en `.agente/` | Que el primero en terminar escriba | Crear con `O_EXCL` lo gana uno solo aunque lleguen a la vez | Acuerdo 3 |
| La lista es por sesión y vale hasta el siguiente mensaje: su clave es el mensaje | Una lista con plazo fijo | El acuerdo dice una consulta por mensaje | Acuerdo 3 |
| La revisión va en una línea al comienzo de cada adaptador: lee la entrada y se la devuelve intacta | Cambiar cómo lee la entrada cada adaptador | La entrada se lee una sola vez y cada adaptador la lee distinto | Propuesta del agente |
| Los dos del freno no salen solos | Que salgan como los demás | El núcleo se sigue frenando con el freno suspendido: lo decide `Freno.nivel_para` | Acuerdo 2 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

Los archivos de turno se borran al terminar; las listas de más de un día se borran al escribir una nueva.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El turno, la consulta y la lista | Lógica | 1,5 h | — | EV-01 |
| T-02 | Solo «freno» apaga el freno entero | Lógica | 0,2 h | — | EV-01 |
| T-03 | Cada adaptador sale si su momento está suspendido | Adaptador | 0,5 h | T-01 | EV-01 |
| T-04 | Pruebas con varios a la vez | Test | 1,5 h | T-01 a T-03 | EV-01 |

**Total estimado:** 3,7 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-02 | Pruebas | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales; la consulta a la base, simulada y contada |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  `02·F14` Q12

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F11`, `02·F30`, `08·T1`, `00·N10`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el que ganó el turno no termine | Los demás esperan | Espera de 2 s; un turno de más de 5 s se ignora | Abierto |
| B-02 | Que la revisión rompa la entrada de un enganche | El enganche no ve su JSON | Se devuelve la entrada intacta; prueba que la lee después | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 4 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** el freno tomaba toda suspensión de enganche como el freno entero; se corrigió en la fase.
