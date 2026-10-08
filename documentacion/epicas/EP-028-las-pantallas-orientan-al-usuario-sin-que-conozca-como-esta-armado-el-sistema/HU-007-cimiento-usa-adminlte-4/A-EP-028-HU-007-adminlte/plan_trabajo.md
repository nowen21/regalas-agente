# Plan de Trabajo · Fase A-EP-028-HU-007-adminlte (módulo Las pantallas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-028-HU-007-adminlte` |
| **Épica** | `EP-028` |
| **HU** | [`HU-007`](../HU-007-cimiento-usa-adminlte-4.md), una sola (`F12.1`) |
| **Módulo** | Las pantallas de Cimiento: `templates/`, las plantillas de cada app, `static/` y la configuración de estáticos |
| **Especificación del módulo** | La HU-007 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`) |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, con «Hágalo si la reemplaza», el 2026-10-07, con la versión 58.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): todas las que hicieron pantallas de Cimiento con Tabler (EP-025, EP-026, EP-027, EP-028), y `B-EP-028-HU-003-iconos-del-menu`, cuyos íconos SVG reemplaza.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-007` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-007-cimiento-usa-adminlte-4.md#ca-01--las-pantallas-usan-adminlte) | ☐ |
| [CA-02](../HU-007-cimiento-usa-adminlte-4.md#ca-02--el-menú-y-sus-submenús-llevan-íconos) | ☐ |
| [CA-03](../HU-007-cimiento-usa-adminlte-4.md#ca-03--ninguna-clase-de-tabler-queda) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que todas las pantallas de Cimiento usen AdminLTE 4, con su menú lateral e íconos de Bootstrap Icons en cada entrada y submenú, y que Tabler salga.

**Fuera de alcance:** cambiar lo que hace cada pantalla.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

AdminLTE 4.10.0 ya está en `node_modules/admin-lte/` (lo instaló el usuario el 2026-10-07); pide Bootstrap 5.3.8. Cimiento sirve `node_modules/@tabler/core/dist` como estáticos (`config/settings/base.py`) y de ahí toma también List.js (`libs/list.js`). Cotejadas las clases de las plantillas contra `adminlte.css`, faltan unas 20 propias de Tabler (`empty`, `card-table`, `table-vcenter`, `bg-*-lt`, `form-hint`, `btn-list`, `page-*`, `navbar-vertical`, `nav-link-icon`...); las `t-*`, `table-sort` y `table-tbody` son ganchos de `static/tablas.js` y se quedan. `ayuda.css` y `estandar.css` usan variables `--tblr-*`. `presentar.py` escribe clases de Tabler en el HTML del estándar.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/package.json` | Modificar | Dependencias | AdminLTE, Bootstrap, Bootstrap Icons y List.js; sale Tabler |
| `proyectos/cimiento/package-lock.json` | Modificar | Dependencias | |
| `proyectos/cimiento/config/settings/base.py` | Modificar | Configuración | Los estáticos de AdminLTE, Bootstrap, Bootstrap Icons y List.js |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | El esqueleto de AdminLTE, con su menú lateral e íconos |
| `proyectos/cimiento/templates/includes/icono.html` | Borrar | Plantilla | Los SVG de Tabler Icons: los reemplaza Bootstrap Icons |
| `proyectos/cimiento/core/cuentas/templates/cuentas/entrar.html` | Modificar | Plantilla | La página de entrada de AdminLTE |
| `proyectos/cimiento/core/cuentas/templates/cuentas/sin_permiso.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/inicio/templates/inicio/base_apagada.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/inicio/templates/inicio/inicio.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/campo.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/ayuda/static/ayuda/ayuda.css` | Modificar | Estilo | Las variables de Bootstrap en lugar de las de Tabler |
| `proyectos/cimiento/core/consumo/templates/consumo/_actividad.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/_ahorro.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/_contexto.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/_donde.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/_franja.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/consumo/templates/consumo/_resumen.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/presentar.py` | Modificar | Lógica | Las clases que escribe en el HTML del estándar |
| `proyectos/cimiento/core/estandar/templates/estandar/_relacion.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/documento.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/propuestas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/reglas_del_proyecto.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/reportes.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/vista_previa.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/_tipo_de_version.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/lista.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/historia/templates/historia/versiones.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/niveles/templates/niveles/historial.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/niveles/templates/niveles/reglas.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/configuracion.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/formulario.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/lista.html` | Modificar | Plantilla | |
| `proyectos/cimiento/core/proyectos/templates/proyectos/suspensiones.html` | Modificar | Plantilla | |
| `proyectos/cimiento/static/estandar.css` | Modificar | Estilo | Las variables de Bootstrap |
| `proyectos/cimiento/static/cimiento.css` | Crear | Estilo | Lo poco que ni Bootstrap ni AdminLTE traen: el asterisco del campo obligatorio, el botón de ordenar de las tablas |
| `proyectos/cimiento/core/inicio/tests_adminlte.py` | Crear | Test | |
| `proyectos/cimiento/core/inicio/tests_menu.py` | Modificar | Test | Los íconos son de Bootstrap Icons |
| `proyectos/cimiento/core/inicio/tests.py` | Modificar | Test | Esperaba los archivos y el menú de Tabler |
| `proyectos/cimiento/core/inicio/tests_tablas.py` | Modificar | Test | List.js se sirve desde su paquete |
| `proyectos/cimiento/core/estandar/tests_vista_estandar.py` | Modificar | Test | Las tarjetas del ejemplo y la tabla con clases de AdminLTE |
| `proyectos/cimiento/core/consumo/tests_tablero.py` | Modificar | Test | El nombre del menú va en `p` |
| `historico-chat/scripts/2026-10-07/tabler_a_adminlte.py` | Crear | Guion de apoyo | Cambia las clases de Tabler en las plantillas |
| `historico-chat/scripts/2026-10-07/pruebas_a_adminlte.py` | Crear | Guion de apoyo | Pone al día las pruebas que buscaban rastros de Tabler |
| `historico-chat/scripts/2026-10-07/salida_pruebas_adminlte.txt` | Crear | Evidencia | La salida de la regresión |
| `historico-chat/scripts/2026-10-07/propuesta_guia_adminlte.py` | Crear | Guion de apoyo | Arma el borrador de la propuesta de la guía |
| `documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-007-cimiento-usa-adminlte-4/A-EP-028-HU-007-adminlte/propuestas/guia-de-pantallas.txt` | Crear | Borrador | La guía dice que Cimiento usa AdminLTE 4 |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `base.html` y los estáticos | Todas las pantallas | Todas las suites con pantallas: `core.inicio`, `core.estandar`, `core.historia`, `core.proyectos`, `core.niveles`, `core.consumo`, `core.ayuda`, `core.cuentas` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Todas las pantallas.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cada clase de Tabler se cambia por la de Bootstrap o AdminLTE | Una hoja que imite las clases de Tabler | La plantilla instalada se usa a fondo (`17·I5`) | Acuerdo 3 del análisis 137, RN-01 |
| Bootstrap Icons | Seguir con los SVG de Tabler Icons | Es el juego de íconos de AdminLTE | RN-02 |
| List.js con npm, aparte | Dejar Tabler solo por List.js | Tabler sale entero | RN-03, RN-04 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas para el usuario. La instalación se deshace con `npm install @tabler/core@1.6.1` y revirtiendo el commit.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Dependencias y estáticos | Configuración | 0,5 h | Ninguna | EV-01 |
| T-02 | `base.html`, entrada y Cimiento apagado | Plantilla | 1,5 h | T-01 | EV-01 |
| T-03 | Las clases de Tabler en plantillas, estilos y `presentar.py` | Plantilla | 1 h | T-01 | EV-01 |
| T-04 | Pruebas y regresión de todas las apps con pantallas | Test | 1 h | T-03 | EV-01 |
| T-05 | La propuesta de la guía (§13: la plantilla de Cimiento) | Borrador | 0,5 h | T-04 | EV-02 |

**Total estimado:** 4,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Prueba de Django | EV-01 | | ☐ |
| CA-02 | Prueba de Django | EV-01 | | ☐ |
| CA-03 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | La propuesta de la guía | «Estándar → Propuestas por aprobar» |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `npm install`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración de datos. Al recargar Cimiento se ve con AdminLTE.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `10·DEP2`, `17·I3`, `17·I5`, `17·I7`.

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
