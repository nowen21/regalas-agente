# Plan de Trabajo · Fase A-EP-029-HU-005-pruebas-de-navegador (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-005-pruebas-de-navegador` |
| **Épica** | `EP-029` |
| **HU** | [`HU-005`](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md), una sola (`F12.1`) |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/`, con el instalador y las dependencias de Cimiento |
| **Especificación del módulo** | La HU-005: sus CA y sus reglas de negocio |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), el 2026-10-08, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Nueva funcionalidad: sale del análisis 1 del pendiente 141, punto 10; la lista de archivos sigue la R-19.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-005` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md#ca-01--la-revisión-corre-las-pruebas-de-navegador) | ☑ |
| [CA-02](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md#ca-02--el-resultado-sale-en-la-página) | ☑ |
| [CA-03](../HU-005-cimiento-corre-las-pruebas-de-navegador-de-cada-proyecto.md#ca-03--cimiento-deja-instalado-playwright) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que la revisión corra las pruebas de navegador del proyecto que las tenga, que su resultado salga en la página y que Cimiento deje instalado Playwright.

**Fuera de alcance:** escribir pruebas de navegador para algún proyecto.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`Revision` ya trae `navegador` y `navegador_detalle` (HU-001), y el detalle del proyecto ya los muestra (HU-002). `Revisor.revisar` (`core/pruebas/revisar.py`) arma los campos de cada revisión. El instalador prepara Cimiento en `Instalador.preparar_cimiento`, solo en la carpeta del propio estándar. `requirements/base.txt` lista lo de Cimiento y `requirements/lock.txt` sus versiones exactas. `pip install playwright==1.63.0 --dry-run` resuelve greenlet 3.5.6, playwright 1.63.0, pyee 13.0.1 y typing_extensions 4.16.0. Lo que pide el cambio (R-19): ninguna migración; ninguna pantalla nueva, solo una columna en la lista.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/pruebas/navegador.py` | Crear | Dominio | Encuentra y corre las pruebas de navegador |
| `proyectos/cimiento/core/pruebas/revisar.py` | Modificar | Dominio | Suma el navegador a cada revisión |
| `proyectos/cimiento/core/pruebas/templates/pruebas/lista.html` | Modificar | Plantilla | La columna «Navegador» |
| `proyectos/cimiento/core/pruebas/tests_navegador.py` | Crear | Test | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/pruebas.html` | Modificar | Ayuda | Lo que dice la columna nueva |
| `proyectos/cimiento/core/herramientas/instalar.py` | Modificar | Instalador | Instala Playwright y Chromium en Cimiento |
| `proyectos/cimiento/core/herramientas/desinstalar.py` | Modificar | Instalador | Quita los navegadores de Playwright |
| `proyectos/cimiento/requirements/base.txt` | Modificar | Dependencias | `playwright` |
| `proyectos/cimiento/requirements/lock.txt` | Modificar | Dependencias | Las cuatro versiones exactas |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `Revisor.revisar` | El botón y la orden de consola | `core.pruebas` |
| Los pasos del instalador y el desinstalador | Toda instalación | `core.herramientas` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

La columna «Navegador» de «Revisión de pruebas».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Las pruebas de navegador se corren con lo del proyecto | Correrlas con el Playwright de Cimiento | Cada proyecto las escribió con sus dependencias | Acuerdo 6 (propuesta del agente) |
| En Django, las pruebas de navegador se corren aparte, aunque `manage.py test` ya las incluya | Sacar el resultado de la corrida de coverage.py | Aparte se sabe cuáles fallaron, sin mezclarlas con las demás | Propuesta del agente |
| El desinstalador quita los navegadores y deja el paquete | Quitar también el paquete | El paquete es una dependencia declarada de Cimiento | `10·DEP2` |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Su contraria |
|---|---|
| El instalador baja Chromium para Playwright | El desinstalador lo quita (`playwright uninstall --all`) |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Encontrar y correr las pruebas de navegador | Dominio | 2 h | Ninguna | EV-01 |
| T-02 | La columna, la ayuda y la revisión | Plantilla | 1 h | T-01 | EV-01 |
| T-03 | Playwright en Cimiento: dependencias, instalar y quitar | Instalador | 1 h | Ninguna | EV-01 |
| T-04 | Pruebas y regresión | Test | 1,5 h | T-01 a T-03 | EV-01 |

**Total estimado:** 5,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django, con las órdenes simuladas | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-03 | Prueba de Django, con las órdenes simuladas | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta que administra |
| Datos precargados | Carpetas temporales; `npx`, pip y Playwright se simulan |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit; en la máquina, `python -m playwright uninstall --all` y `pip uninstall playwright`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: una dependencia nueva y una columna.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F30`, `08·T3`, `10·DEP2`, `00·ID7`, `20·M3`.

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
