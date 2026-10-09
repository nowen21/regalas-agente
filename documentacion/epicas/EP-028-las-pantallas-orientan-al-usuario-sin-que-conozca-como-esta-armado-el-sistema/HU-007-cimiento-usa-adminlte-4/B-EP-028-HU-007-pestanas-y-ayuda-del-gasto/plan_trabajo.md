# Plan de Trabajo · Fase B-EP-028-HU-007-pestanas-y-ayuda-del-gasto (módulo Las pantallas de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-028-HU-007-pestanas-y-ayuda-del-gasto` |
| **Épica** | `EP-028` |
| **HU** | [`HU-007`](../HU-007-cimiento-usa-adminlte-4.md), una sola (`F12.1`) |
| **Módulo** | Las pantallas de Cimiento: la pantalla del gasto (`core/consumo/templates/consumo/`) y la ayuda (`core/ayuda/`) |
| **Especificación del módulo** | La HU-007 y la guía de diseño de pantallas (`base/17-guia-de-pantallas.md`) |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | El usuario, con la corrección de las pestañas y la ayuda del gasto, el 2026-10-08, con la versión 58.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Corrige la fase `A-EP-028-HU-007-adminlte`: con AdminLTE, las pestañas del gasto dejaron de funcionar.
- Completa `EP-028·HU-005`: la ayuda llegó a los formularios, no al contenido de las pestañas del gasto.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-007` que cierra esta fase | Estado |
|---|---|
| [CA-04](../HU-007-cimiento-usa-adminlte-4.md#ca-04--las-pestañas-del-gasto-funcionan) | ☐ |
| [CA-05](../HU-007-cimiento-usa-adminlte-4.md#ca-05--las-pestañas-del-gasto-tienen-su-ayuda) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que al pulsar una pestaña del gasto se vea su contenido y quede marcada, y que cada título, cifra y columna de las pestañas tenga su «?» con la explicación.

**Fuera de alcance:** cambiar qué cifras muestra cada pestaña.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

El servidor responde bien: `/gasto/` y las cinco pestañas devuelven 200, y los estáticos (AdminLTE, Bootstrap, htmx, ApexCharts, la ayuda) cargan. La falla está en el navegador y se busca con Chrome sin ventana. Las pestañas parciales no tienen ningún `ayuda_campo`; `ayuda.js` activa los globos solo al cargar la página, así que un «?» que llega por htmx quedaría sin globo.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `documentacion/epicas/EP-028-las-pantallas-orientan-al-usuario-sin-que-conozca-como-esta-armado-el-sistema/HU-007-cimiento-usa-adminlte-4/HU-007-cimiento-usa-adminlte-4.md` | Modificar | Documento | CA-04 y CA-05, y la fase B |
| `proyectos/cimiento/core/consumo/templates/consumo/tablero.html` | Modificar | Plantilla | Las pestañas |
| `proyectos/cimiento/core/consumo/templates/consumo/_resumen.html` | Modificar | Plantilla | Su ayuda |
| `proyectos/cimiento/core/consumo/templates/consumo/_donde.html` | Modificar | Plantilla | Su ayuda |
| `proyectos/cimiento/core/consumo/templates/consumo/_contexto.html` | Modificar | Plantilla | Su ayuda |
| `proyectos/cimiento/core/consumo/templates/consumo/_ahorro.html` | Modificar | Plantilla | Su ayuda |
| `proyectos/cimiento/core/consumo/templates/consumo/_actividad.html` | Modificar | Plantilla | Su ayuda |
| `proyectos/cimiento/core/consumo/templates/consumo/_franja.html` | Modificar | Plantilla | Su ayuda |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Lógica | Los textos de cada «?» del gasto |
| `proyectos/cimiento/core/ayuda/static/ayuda/ayuda.js` | Modificar | Script | Activa los globos de lo que llega por htmx |
| `proyectos/cimiento/static/cimiento.css` | Modificar | Estilo | Si AdminLTE tapa o desacomoda las pestañas |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | Si la falla está en el orden de los scripts |
| `proyectos/cimiento/core/consumo/tests_pestanas.py` | Crear | Test | |
| `historico-chat/scripts/2026-10-08/ver_pestanas.mjs` | Crear | Guion de apoyo | Abre el gasto en Chrome sin ventana, pulsa cada pestaña y cuenta lo que se ve |
| `historico-chat/scripts/2026-10-08/salida_ver_pestanas.txt` | Crear | Evidencia | La salida del guion antes y después |
| `historico-chat/scripts/2026-10-08/pestanas.png` | Crear | Evidencia | Cómo se ve la pantalla con una pestaña escogida |
| `historico-chat/scripts/2026-10-08/README.md` | Crear | Índice | La fila de cada guion del día (`04·S18`) |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `ayuda.js` y `textos.py` | Todas las pantallas con ayuda | `core.ayuda` |
| Las plantillas del gasto | La pantalla del gasto | `core.consumo` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna nueva.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú → Gasto.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La ayuda de las pestañas usa el mismo «?» (`ayuda_campo`) de los formularios | Un texto fijo debajo de cada tabla | El «?» es el componente de la guía para explicar algo de la pantalla (`17·I7`) | La corrección del usuario |
| `ayuda.js` activa los globos después de cada cambio de htmx | Activarlos en cada plantilla parcial | Una sola parte común (`17·I5`, guía §12) | |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No hay acciones nuevas.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Encontrar en el navegador por qué fallan las pestañas y corregirlo | Plantilla | 1 h | Ninguna | EV-01, EV-02 |
| T-02 | El «?» en títulos, cifras y columnas de cada pestaña, con sus textos | Plantilla | 1 h | Ninguna | EV-01 |
| T-03 | Los globos se activan en lo que llega por htmx | Script | 0,25 h | T-02 | EV-01, EV-02 |
| T-04 | Pruebas | Test | 0,5 h | T-03 | EV-01 |

**Total estimado:** 2,75 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-04 | Prueba de Django y Chrome sin ventana | EV-01, EV-02 | | ☐ |
| CA-05 | Prueba de Django y Chrome sin ventana | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida del guion en el navegador | `historico-chat/scripts/2026-10-08/salida_ver_pestanas.txt` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django; Cimiento en http://127.0.0.1:8015 para el navegador |
| Usuarios de prueba | Una cuenta administradora |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Sin migración. Basta con recargar la pantalla.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `17·I1`, `17·I5`, `17·I7`.

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

**Reabierta** el 2026-10-08: El usuario reporta htmx:targetError #pestana al pulsar los botones de Dónde se gasta: heredan hx-swap outerHTML y borran #pestana.

Cerrada otra vez el 2026-10-08, con la versión 58.0.0. Los botones de agrupar dicen `hx-swap="innerHTML"`, y la prueba `test_lo_que_carga_en_pestana_desde_adentro_no_la_reemplaza` lo vigila.
