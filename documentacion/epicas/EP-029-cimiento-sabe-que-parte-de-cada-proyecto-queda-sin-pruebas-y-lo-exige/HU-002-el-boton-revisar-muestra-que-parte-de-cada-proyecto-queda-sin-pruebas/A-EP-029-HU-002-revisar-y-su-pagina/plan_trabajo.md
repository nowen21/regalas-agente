# Plan de Trabajo · Fase A-EP-029-HU-002-revisar-y-su-pagina (módulo Pruebas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-029-HU-002-revisar-y-su-pagina` |
| **Épica** | `EP-029` |
| **HU** | [`HU-002`](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md), una sola (`F12.1`) |
| **Módulo** | Pruebas de Cimiento: `core/pruebas/`, con su entrada en el menú y en la lista de proyectos |
| **Especificación del módulo** | La HU-002: sus CA y sus reglas de negocio |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 141](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md), el 2026-10-08, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Nueva funcionalidad: sale del análisis 1 del pendiente 141, puntos 4, 5, 6 y 11; la lista de migraciones sigue el acuerdo 2 del análisis 2 (R-19).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md#ca-01--cimiento-reconoce-el-lenguaje-de-cada-proyecto) | ☑ |
| [CA-02](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md#ca-02--la-revisión-guarda-qué-parte-quedó-sin-pruebas) | ☑ |
| [CA-03](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md#ca-03--el-botón-y-la-orden-de-consola-arrancan-la-revisión) | ☑ |
| [CA-04](../HU-002-el-boton-revisar-muestra-que-parte-de-cada-proyecto-queda-sin-pruebas.md#ca-04--una-página-muestra-todos-los-proyectos) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el botón «Revisar» y la orden `revisar_pruebas` revisen cualquier proyecto con la herramienta de su lenguaje, y que una página muestre el resultado de todos.

**Fuera de alcance:** poner la herramienta en el proyecto y avisar (HU-003); el navegador (HU-005).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

La HU-001 dejó `core/pruebas/` con `PruebasDelProyecto` y `Revision`. Las páginas piden entrar (`LoginRequiredMiddleware`) y lo que cambia datos lo limita `es_administrador` (`core/cuentas/permisos.py`). El menú vive en `templates/base.html`; `core/inicio/tests_menu.py` exige que toda pantalla esté en él y que cada entrada tenga icono. Las tablas siguen el patrón de List.js que exige `core/inicio/tests_tablas.py`, y cada pantalla con formulario su ayuda (`core/ayuda/tests_formularios.py`). `Proyecto.ajustes()` da los dos ajustes de la HU-001. Lo que pide Django (R-19): agregar `revisando_desde` a `PruebasDelProyecto` genera una sola migración, `pruebas/0002_revisando.py`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/pruebas/models.py` | Modificar | Modelo | `revisando_desde`, y si la revisión está al día |
| `proyectos/cimiento/core/pruebas/migrations/0002_revisando.py` | Crear | Migración | El campo nuevo |
| `proyectos/cimiento/core/pruebas/lenguaje.py` | Crear | Dominio | Reconoce el lenguaje por sus archivos |
| `proyectos/cimiento/core/pruebas/revisar.py` | Crear | Dominio | Corre la herramienta de cada lenguaje y lee su resultado |
| `proyectos/cimiento/core/pruebas/management/__init__.py` | Crear | Orden | |
| `proyectos/cimiento/core/pruebas/management/commands/__init__.py` | Crear | Orden | |
| `proyectos/cimiento/core/pruebas/management/commands/revisar_pruebas.py` | Crear | Orden | La orden de consola |
| `proyectos/cimiento/core/pruebas/views.py` | Crear | Vista | Lista, detalle, revisar y borrar |
| `proyectos/cimiento/core/pruebas/urls.py` | Crear | Ruta | |
| `proyectos/cimiento/core/pruebas/templates/pruebas/lista.html` | Crear | Plantilla | Todos los proyectos |
| `proyectos/cimiento/core/pruebas/templates/pruebas/detalle.html` | Crear | Plantilla | Un proyecto y sus archivos |
| `proyectos/cimiento/core/pruebas/tests_revisar.py` | Crear | Test | |
| `proyectos/cimiento/config/urls.py` | Modificar | Ruta | `pruebas/` |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | La entrada del menú |
| `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | Modificar | Plantilla | El enlace «Pruebas» de cada proyecto |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | La ayuda de las dos pantallas |
| `proyectos/cimiento/core/ayuda/tests_formularios.py` | Modificar | Test | Las dos pantallas en la lista |
| `proyectos/cimiento/core/inicio/tests_menu.py` | Modificar | Test | La pantalla nueva en el menú |
| `proyectos/cimiento/core/inicio/tests_tablas.py` | Modificar | Test | Las dos tablas nuevas |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | La sección del manual de las pantallas nuevas; la agregó el análisis 3 del pendiente 141, acuerdo 1 |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/pruebas.html` | Crear | Plantilla | El texto de esa sección; la agregó el análisis 3 del pendiente 141, acuerdo 1 |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| El menú de `base.html` | Toda pantalla | `core.inicio` |
| La lista de proyectos | «Proyectos» | `core.proyectos`, `core.inicio` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `pruebas/` | GET | Toda cuenta |
| `pruebas/<pk>/` | GET | Toda cuenta |
| `pruebas/<pk>/revisar/` | POST | Quien administra |
| `pruebas/revision/<pk>/borrar/` | POST | Quien administra |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

El menú «Revisión de pruebas», y el enlace «Pruebas» de cada proyecto en «Todos los proyectos».

### 2.5 Permisos / roles a sembrar

Ninguno nuevo: se usa `es_administrador`.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El botón arranca la orden `revisar_pruebas` en otro proceso | Revisar dentro de la petición | Una revisión puede tardar minutos; la página no espera | Acuerdo 11, R-01 de la épica (propuesta del agente) |
| Se usa el Python del proyecto (`.venv` o `venv`) | El de Cimiento | Las pruebas del proyecto necesitan sus propias dependencias | Propuesta del agente |
| El resultado de Angular se lee del resumen que imprime `ng test` | Leer los archivos que deja | Su configuración de fábrica solo imprime el resumen; los archivos dependen de cómo lo armó cada proyecto | Propuesta del agente |
| La revisión se corta a los 30 minutos | Sin tope | Un proyecto colgado no deja el estado en «Revisando» para siempre | RNF-02 (propuesta del agente) |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Su contraria |
|---|---|
| «Revisar» guarda una revisión | «Borrar» la quita, en el detalle del proyecto |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reconocer el lenguaje | Dominio | 1 h | Ninguna | EV-01 |
| T-02 | Revisar con la herramienta de cada lenguaje | Dominio | 3 h | T-01 | EV-01 |
| T-03 | `revisando_desde`, su migración y la orden de consola | Modelo | 1 h | T-02 | EV-01 |
| T-04 | Las pantallas, el menú, el enlace y la ayuda | Vista | 3 h | T-03 | EV-01 |
| T-05 | Pruebas y regresión | Test | 2 h | T-01 a T-04 | EV-01 |

**Total estimado:** 10 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-05, en orden.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-02 | Prueba de Django, con la herramienta simulada | EV-01 | 2026-10-08 | ☑ |
| CA-03 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |
| CA-04 | Prueba de Django | EV-01 | 2026-10-08 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta que administra y una que no |
| Datos precargados | Carpetas temporales con los archivos de cada lenguaje; la herramienta se simula, no se corre |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `manage.py migrate pruebas 0001`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: un campo nuevo que puede quedar vacío.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F30`, `08·T3`, `08·T6`, `17·I5`, `17·I7`, `00·ID7`, `20·M3`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Ninguno | | | |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** H-3 de la sesión del 2026-10-07: falta declarar `core/ayuda/secciones.py` y `core/ayuda/templates/ayuda/secciones/pruebas.html`, la sección del manual que pide toda pantalla nueva. El análisis 3 del pendiente 141 los agregó a la §2.1 y la fase siguió desde T-05.
