# Plan de Trabajo · Fase A-EP-025-HU-032-catalogo-y-pantalla (módulo las suspensiones de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-032-catalogo-y-pantalla` |
| **Épica** | `EP-025` |
| **HU** | [`HU-032`](../HU-032-cada-momento-de-cada-enganche-y-cada-revision-de-git-se-puede-suspender.md), una sola (`F12.1`) |
| **Módulo** | Las suspensiones de Cimiento: `proyectos/cimiento/core/proyectos/`, con el catálogo de `core/comun/enganches.py` y sus ayudas |
| **Especificación del módulo** | La HU-032 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 149](../../../../../historico-chat/resumenes/2026-10-08/pendientes/149-cada-enganche-se-puede-suspender-desde-cimiento/analisis-1.md), el 2026-10-09, en el turno 27, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 149, punto 1 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad `13·DOC11`):

| CA de `HU-032` que cierra esta fase | Estado |
|---|---|
| CA-01 · Cada momento y cada revisión tiene nombre y se suspende desde la pantalla | ☑ |

## 1. Objetivo y alcance  ·  `02·F14` Q4

**Objetivo:** cada momento de un enganche y cada revisión de git tiene un nombre fijo en el catálogo, con lo que hace y, si no conviene suspenderlo, el motivo; la pantalla de suspensiones deja escoger cualquiera y muestra la recomendación.

**Fuera de alcance:** que los enganches y git lean lo suspendido (fases B y C); quitar `NO_SE_SUSPENDEN`, que el instalador importa (fase C).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`HOOKS_CLAUDE` (`core/comun/enganches.py:21`) tiene 24 momentos sin nombre. `ajustes.se_puede_suspender` (`core/proyectos/ajustes.py:80`) solo acepta el freno, y `SuspensionForm.clean` (`core/proyectos/forms.py:83`) convierte todo enganche en «freno». La pantalla (`suspensiones.html`) y las ayudas `suspension.tipo` y `suspension.nombre` (`core/ayuda/textos.py:61`) dicen que el histórico no se suspende. `tests_configuracion.py:47` y `:193` prueban lo de hoy.

### 2.1 Archivos que se crean o modifican  ·  `02·F14` Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/comun/enganches.py` | Modificar | Catálogo | `MOMENTOS`, `REVISIONES_GIT`, `NO_CONVIENE` y `suspendibles()` |
| `proyectos/cimiento/core/proyectos/ajustes.py` | Modificar | Lógica | `se_puede_suspender` acepta lo del catálogo |
| `proyectos/cimiento/core/proyectos/forms.py` | Modificar | Formulario | El nombre se valida contra el catálogo |
| `proyectos/cimiento/core/proyectos/views.py` | Modificar | Vista | Pasa el catálogo a la pantalla |
| `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | Modificar | Pantalla | Lo que se puede suspender, con la recomendación |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | Las ayudas de tipo y nombre |
| `proyectos/cimiento/core/proyectos/tests_configuracion.py` | Modificar | Test | Lo que cambió por el acuerdo 2 |
| `proyectos/cimiento/core/proyectos/tests_suspender_enganches.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  `02·F14` Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  `02·F14` Q7

La pantalla de suspensiones de cada proyecto.

### 2.5 Permisos / roles a sembrar  ·  `02·F14` Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El nombre del momento sale de `(evento, guion)` | Un sexto campo en cada entrada de `HOOKS_CLAUDE` | El instalador, el desinstalador y el checklist desarman la tupla de cinco; Claude Code ya le dice a cada enganche su evento | Acuerdo 1 |
| Los dos enganches del freno se suspenden juntos como «freno» | Uno por uno | Es lo que se suspende hoy, y el núcleo lo sigue frenando | Acuerdo 1 |
| Las revisiones de git se nombran por la revisión | Una por enganche y revisión | El acuerdo pide «cada una por separado (versionado, marcas, plan, pruebas...)» | Acuerdo 4 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  `02·F30`

Suspender se deshace levantando la suspensión, que ya existe.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El catálogo con nombres, lo que hace cada uno y la recomendación | Catálogo | 1 h | — | EV-01 |
| T-02 | Validar y guardar el nombre; la pantalla y las ayudas | Pantalla | 1,5 h | T-01 | EV-01 |
| T-03 | Pruebas | Test | 1 h | T-02 | EV-01 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  `02·F14` Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta que puede cambiar el proyecto |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  `02·F14` Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  `02·F14` Q12

No aplica: `Suspension.nombre` ya guarda texto; no cambia el esquema.

## 9. Reglas del estándar y del proyecto aplicadas  ·  `02·F14` Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F11`, `02·F30`, `08·T1`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Que una suspensión vieja del freno deje de valer | El freno suspendido vuelve a frenar | «freno» sigue siendo un nombre del catálogo | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

Las 3 tareas quedaron hechas el 2026-10-09, con la versión 56.8.0. Detalle en [`funcionalidad_implementada.md`](funcionalidad_implementada.md).

**Hallazgos al ejecutar:** el formulario exigía el nombre; se dejó opcional dentro de la fase.
