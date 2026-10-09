# Plan de Trabajo · Fase C-EP-025-HU-032-revisiones-de-git (módulo las revisiones de git de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-025-HU-032-revisiones-de-git` |
| **Épica** | `EP-025` |
| **HU** | [`HU-032`](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md), una sola (`F12.1`) |
| **Módulo** | Las revisiones de git: `proyectos/cimiento/core/herramientas/`, con el adaptador de `post-commit` y lo que queda de `NO_SE_SUSPENDEN` |
| **Especificación del módulo** | La HU-032 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md), el 2026-10-09, en el turno 27, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 149, punto 3 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de `HU-032` que cierra esta fase | Estado |
|---|---|
| CA-03 · La revisión de git suspendida no detiene | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** cada revisión de git sabe si está suspendida, con una sola consulta por guardado; si lo está, no detiene y dice que está suspendida, con su motivo y su vencimiento. `NO_SE_SUSPENDEN` desaparece.

**Fuera de alcance:** cambiar las plantillas de los enganches de git: la revisión se reconoce por la orden de `validar.py`.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Los enganches de git llaman a `validadores/validar.py «revisión»`, que entra a `Consola.correr` (`core/herramientas/validar.py:840`). `post-commit` llama a `adaptadores/claude-code/hook_estacion.py`. `instalar.py:43` importa `NO_SE_SUSPENDEN` sin usarlo, y `core/comun/tests.py:155` lo prueba; desde la fase A nadie más lo usa.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/herramientas/validar.py` | Modificar | Lógica | Antes de correr una revisión de git, mira si está suspendida |
| `proyectos/cimiento/core/herramientas/instalar.py` | Modificar | Lógica | Sin `NO_SE_SUSPENDEN` |
| `proyectos/cimiento/core/comun/enganches.py` | Modificar | Catálogo | Se quita `NO_SE_SUSPENDEN` |
| `proyectos/cimiento/core/comun/tests.py` | Modificar | Test | Sin `NO_SE_SUSPENDEN` |
| `adaptadores/claude-code/hook_estacion.py` | Modificar | Adaptador | La revisión de `post-commit` también se suspende |
| `proyectos/cimiento/core/herramientas/tests_validar_suspendida.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

No aplica: es git.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La revisión se reconoce por la orden de `validar.py` | Pasar el nombre desde cada plantilla de git | Sin reinstalar los `.githooks` de cada proyecto | Acuerdo 4 |
| La lista de git es la de `Suspendidos` con sesión «git», por minuto | Una lista por enganche de git | Un guardado corre sus revisiones en segundos y en varios enganches | Acuerdo 4 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

Levantar la suspensión en Cimiento.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | `validar.py` y `hook_estacion.py` miran la suspensión de su revisión | Lógica | 1 h | — | EV-01 |
| T-02 | Quitar `NO_SE_SUSPENDEN` | Lógica | 0,3 h | — | EV-01 |
| T-03 | Pruebas | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 2,3 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 | Pruebas | EV-01 | 2026-10-09 | ☑ |

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

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F11`, `08·T1`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que el agente corra a mano una revisión suspendida | No ve sus fallas | Dice que está suspendida, con motivo y vencimiento | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** H-3: la lista cayó en .agente/ de la raíz, que el estándar no ignoraba; resuelto en el análisis 2 del pendiente 149.
