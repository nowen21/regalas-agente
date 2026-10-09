# Plan de Trabajo · Fase A-EP-029-HU-004-sin-copia-local (módulo Proyectos de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-004-sin-copia-local` |
| **Épica** | `EP-029` |
| **HU** | [`HU-004`](../HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md), una sola (`F12.1`) |
| **Módulo** | Proyectos de Cimiento: `core/proyectos/`, con su ayuda y el paso del instalador |
| **Especificación del módulo** | La HU-004: sus CA y sus reglas de negocio |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), el 2026-10-08, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la de la copia de la configuración (EP-025·HU-013). Sale del análisis 1 del pendiente 141, punto 9; la lista de archivos sigue la R-19.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md#ca-01--cimiento-ya-no-escribe-la-copia) | ☑ |
| [CA-02](../HU-004-cada-proyecto-consulta-su-configuracion-en-cimiento-y-la-copia-local-desaparece.md#ca-02--volver-a-instalar-borra-la-copia-vieja) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que Cimiento deje de escribir `.agente/configuracion.md` y que volver a instalar borre la que quedó.

**Fuera de alcance:** cómo leen la base los enganches, que no cambia.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`core/proyectos/copia.py` escribe la copia; la llaman cuatro lugares de `core/proyectos/views.py`. La prueban `tests_configuracion.py` y `tests_opt_in.py`. La nombran `core/ayuda/textos.py` y las secciones `configuracion.html` y `registrar.html` del manual. Ningún programa la lee. Lo que pide el cambio (R-19): ninguna migración, ninguna pantalla nueva.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/copia.py` | Borrar | Dominio | La copia |
| `proyectos/cimiento/core/proyectos/views.py` | Modificar | Vista | Sin sus llamadas |
| `proyectos/cimiento/core/proyectos/tests_configuracion.py` | Modificar | Test | Prueba que ya no se escribe |
| `proyectos/cimiento/core/proyectos/tests_opt_in.py` | Modificar | Test | Sin la copia |
| `proyectos/cimiento/core/proyectos/tests_sin_copia.py` | Crear | Test | Volver a instalar la borra |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | Sin nombrar la copia |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/configuracion.html` | Modificar | Ayuda | Sin nombrar la copia |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/registrar.html` | Modificar | Ayuda | Sin nombrar la copia |
| `proyectos/cimiento/core/herramientas/instalar.py` | Modificar | Instalador | Borra la copia vieja |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| Las vistas de «Proyectos» y «Configuración» | Sus pantallas | `core.proyectos` |
| Los pasos del instalador | Toda instalación | `core.herramientas` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Ninguno nuevo.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La copia vieja la borra el instalador | Una orden aparte | Volver a instalar ya es obligatorio con esta épica (versión MAYOR) | Acuerdo 10 (propuesta del agente) |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

Borrar la copia no tiene contraria: lo que decía está en la base y se ve en «Proyectos» → «Editar».

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Quitar la copia, sus llamadas y su ayuda | Vista | 1 h | Ninguna | EV-01 |
| T-02 | Borrar la copia vieja al instalar | Instalador | 0,5 h | Ninguna | EV-01 |
| T-03 | Pruebas y regresión | Test | 1 h | T-01, T-02 | EV-01 |

**Total estimado:** 2,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta que administra |
| Datos precargados | Un proyecto en una carpeta temporal |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración. Hasta volver a instalar, la copia vieja queda en la carpeta del proyecto, sin que nada la lea.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F30`, `00·ID7`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
