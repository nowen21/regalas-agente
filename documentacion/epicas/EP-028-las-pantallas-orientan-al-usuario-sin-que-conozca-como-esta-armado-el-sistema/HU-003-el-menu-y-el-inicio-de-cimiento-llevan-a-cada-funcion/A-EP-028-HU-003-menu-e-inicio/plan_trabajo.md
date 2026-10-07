# Plan de Trabajo · Fase A-EP-028-HU-003-menu-e-inicio (módulo Inicio de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-003-menu-e-inicio` |
| **Épica** | `EP-028` |
| **HU** | [`HU-003`](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md), una sola (`F12.1`) |
| **Módulo** | Inicio de Cimiento: `templates/base.html` y `core/inicio/` |
| **Especificación del módulo** | La HU-003 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`, §4 y §7) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 137](../../../../../historico-chat/resumenes/2026-10-07/pendientes/137-las-pantallas-de-cimiento-no-orientan-al-usuario/analisis-1.md), el 2026-10-07, con la versión 57.1.1 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que hizo el menú y el inicio de Cimiento (EP-025). Sale del análisis 1 del pendiente 137, punto 5.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-003` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md#ca-01--toda-pantalla-está-en-el-menú) | ☐ |
| [CA-02](../HU-003-el-menu-y-el-inicio-de-cimiento-llevan-a-cada-funcion.md#ca-02--el-inicio-muestra-lo-que-espera-una-decisión) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que toda pantalla de Cimiento esté en el menú, agrupada por tarea, y que el menú y el inicio muestren lo que espera una decisión.

**Fuera de alcance:** la pantalla de propuestas en sí (HU-004).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`templates/base.html` trae un `navbar-vertical` de Tabler con seis entradas sueltas, sin submenús ni entrada activa. `core/inicio/views.py` muestra solo el nombre de la base. Las pantallas sin entrada son `estandar:propuestas`, `estandar:reportes`, `estandar:vista_previa`, `estandar:git`, `historia:versiones`, `proyectos:registrar` y `ayuda:manual`. Los procesadores de contexto están en `config/settings/base.py`. La ayuda del inicio está en `core/ayuda/templates/ayuda/secciones/inicio.html`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | Menú por tareas con `dropdown`, entrada activa y contadores |
| `proyectos/cimiento/core/inicio/pendientes.py` | Crear | Lógica | Procesador de contexto: lo que espera una decisión |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Configuración | Registra el procesador |
| `proyectos/cimiento/core/inicio/templates/inicio/inicio.html` | Modificar | Plantilla | Tarjetas de lo pendiente y de las tareas |
| `proyectos/cimiento/core/inicio/tests_menu.py` | Crear | Test | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/inicio.html` | Modificar | Ayuda | El inicio nuevo |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `base.html` | Toda pantalla de Cimiento | `core.inicio`, `core.ayuda`, `core.estandar.tests_pantalla` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

El menú de la izquierda y el inicio.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Los contadores salen de un procesador de contexto | Calcularlos en cada vista | Están en todas las pantallas; una sola fuente | Guía §12 |
| Submenús `dropdown` del `navbar-vertical` de Tabler | Un menú propio | Lo trae la plantilla instalada | `17·I5`, acuerdo 3 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas: el menú y el inicio solo llevan a pantallas que ya existen.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Menú por tareas, entrada activa y contadores | Plantilla | 1 h | Ninguna | EV-01 |
| T-02 | Inicio con lo pendiente y las tareas, y su ayuda | Plantilla | 1 h | T-01 | EV-01 |
| T-03 | Pruebas y regresión | Test | 0,5 h | T-02 | EV-01 |

**Total estimado:** 2,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Dos propuestas pendientes y un reporte abierto |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I5`, `17·I7`, guía §4 y §7.

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
