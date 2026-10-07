# Plan de Trabajo · Fase A-EP-026-HU-009-vista-previa-y-opt-in (módulo Proyectos y Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-009-vista-previa-y-opt-in` |
| **Épica** | `EP-026` |
| **HU** | [`HU-009`](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md), una sola (`F12.1`) |
| **Módulo** | Proyectos y Estándar en la base, `proyectos/cimiento/core/proyectos/` y `core/estandar/` |
| **Especificación del módulo** | La HU-009 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que escribió los capítulos opt-in apagados (`RecuperadorDeReglas.opt_in_apagados`) y la de las tres capas de ajustes (`EP-025·HU-013`). Sale del análisis 1 del pendiente 132, acuerdos 5, 10 y 11.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-009` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md#ca-01--los-opt-in-son-ajustes-del-proyecto) | ☐ |
| [CA-02](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md#ca-02--las-reglas-se-eligen-con-los-opt-in-de-la-base) | ☐ |
| [CA-03](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md#ca-03--lo-que-dice-el-claudemd-pasa-a-la-base) | ☐ |
| [CA-04](../HU-009-la-pantalla-muestra-que-reglas-llegarian-con-un-mensaje-y-prende-los-capitulos-opt-in.md#ca-04--la-vista-previa) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que los capítulos opt-in de cada proyecto se prendan y apaguen en la pantalla, que las reglas se elijan con lo que diga la base, y que una pantalla muestre qué reglas llegarían con un mensaje.

**Fuera de alcance:** quitar la sección 5.1 de la plantilla del `CLAUDE.md`, que sigue sirviendo a los proyectos sin registro.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`RecuperadorDeReglas.opt_in_apagados` (`core/herramientas/recuperar.py`) lee las líneas «Patrón opt-in `NN`» del `CLAUDE.md` del proyecto; lo usan `elegir` y `ReglasQueAutorizan.de_la_base` (`core/enganches/autorizado.py`). Los ajustes de tres capas están en `core/proyectos/ajustes.py` (`AJUSTES`), se guardan en `AjusteBase` y `AjusteDelProyecto`, el formulario del proyecto y el de «Configuración» los ofrecen todos, y los enganches los leen sin Django con `ConfiguracionDelProyecto` (`core/enganches/configuracion.py`). `AjusteDelProyecto` ya sube la versión del proyecto (`core/historia/versiones.py`).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/proyectos/ajustes.py` | Modificar | Lógica | Los siete opt-in como ajustes |
| `proyectos/cimiento/core/proyectos/opt_in.py` | Crear | Lógica | Leer el `CLAUDE.md` y pasarlo a la base |
| `proyectos/cimiento/core/proyectos/migrations/0005_opt_in.py` | Crear | Migración | Opciones nuevas y paso de lo que dice cada `CLAUDE.md` |
| `proyectos/cimiento/core/proyectos/tests_opt_in.py` | Crear | Test | |
| `proyectos/cimiento/core/enganches/configuracion.py` | Modificar | Lógica | Dice si el proyecto está registrado |
| `proyectos/cimiento/core/herramientas/recuperar.py` | Modificar | Lógica | `opt_in_apagados` lee la base |
| `proyectos/cimiento/core/estandar/views.py` | Modificar | Vista | Vista previa |
| `proyectos/cimiento/core/estandar/urls.py` | Modificar | Rutas | |
| `proyectos/cimiento/core/estandar/templates/estandar/vista_previa.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | Enlace |
| `proyectos/cimiento/core/estandar/tests_vista_previa.py` | Crear | Test | |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Ayuda | El «?» de cada opt-in |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/estandar.html` | Modificar | Ayuda | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `opt_in_apagados` | `elegir`, `de_la_base` del freno | `core.herramientas`, `core.enganches` |
| `AJUSTES` | formularios, copia `.agente/configuracion.md`, tablero de consumo | `core.proyectos`, `core.consumo` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `/estandar/vista-previa/` | GET | Toda cuenta con sesión |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar» → «Vista previa»; los opt-in, en «Proyectos» → editar y en «Configuración».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Los opt-in son ajustes de las tres capas | Una tabla propia | Ya tienen pantalla, historia, versión y copia en el proyecto | Acuerdo 10 |
| Sin registro o sin base, se lee el `CLAUDE.md` | No apagar nada | Una carpeta suelta conserva lo que declaró | RN-03 |
| La migración pasa lo que dice cada `CLAUDE.md` | Arrancar todos en «no» | Nada cambia el día del paso | RN-04 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Prender un opt-in | Apagarlo en la misma pantalla, o deshacer el cambio desde «Historia» |
| Pasar los opt-in a la base | `manage.py migrate proyectos 0004` |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Los opt-in como ajustes | Lógica | 0,5 h | — | EV-01 |
| T-02 | `opt_in_apagados` lee la base | Lógica | 1 h | T-01 | EV-01 |
| T-03 | Migración que pasa el `CLAUDE.md` a la base | Migración | 1 h | T-01 | EV-01 |
| T-04 | Vista previa | Vista | 1 h | — | EV-01 |
| T-05 | Pruebas y regresión | Test | 1 h | T-01 a T-04 | EV-01 |

**Total estimado:** 4,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-05. **Paralelizable:** T-04.

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
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Un proyecto registrado con su `CLAUDE.md` |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `manage.py migrate proyectos 0004`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: opciones nuevas y filas de ajustes.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F29`, `20·M10`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión escribe en la misma carpeta y el freno se lo cobra a esta | Detiene órdenes de consola | Se anota y se sigue | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
