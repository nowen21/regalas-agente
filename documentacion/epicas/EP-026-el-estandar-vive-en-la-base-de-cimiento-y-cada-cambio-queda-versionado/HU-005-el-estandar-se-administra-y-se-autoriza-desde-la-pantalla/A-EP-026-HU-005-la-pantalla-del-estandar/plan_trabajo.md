# Plan de Trabajo · Fase A-EP-026-HU-005-la-pantalla-del-estandar (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-005-la-pantalla-del-estandar` |
| **Épica** | `EP-026` |
| **HU** | [`HU-005`](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-005 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-026-HU-003-la-importacion` y `A-EP-026-HU-004-leer-de-la-base`. Sale del análisis 1 del pendiente 132, acuerdos 2, 3, 10 y 17.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-005` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md#ca-01--el-administrador-cambia-un-documento-y-queda-versionado) | ☐ |
| [CA-02](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md#ca-02--crear-y-quitar-un-documento) | ☐ |
| [CA-03](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md#ca-03--la-memoria-de-cada-proyecto-en-la-pantalla-y-en-el-arranque) | ☐ |
| [CA-04](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md#ca-04--lo-que-propone-el-agente-se-aprueba-en-la-pantalla) | ☐ |
| [CA-05](../HU-005-el-estandar-se-administra-y-se-autoriza-desde-la-pantalla.md#ca-05--consulta-solo-mira-y-el-agente-lee-con-una-orden) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** administrar el estándar y la memoria desde la pantalla, aprobar ahí lo que propone el agente, y que el agente lea de la base.

**Fuera de alcance:** congelar `base/` (HU-006).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

El estándar está en `estandar_documento` y la memoria en `estandar_recuerdo` (HU-003); los enganches leen de ahí (HU-004). El mapa y las reglas por tarea los arma `MapaDeTareas.armar` y `armar_por_tarea` (`core/herramientas/mapa_tareas.py`). El arranque lee la memoria con `Recuerdos.contexto` (`core/enganches/recuerdos.py`) desde `historico-chat/memory/`. Las dos preguntas y la versión ya las ponen el middleware y `_tipo_de_version.html` (HU-002).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/models.py` | Modificar | Modelo | `Propuesta` |
| `proyectos/cimiento/core/estandar/migrations/0002_propuesta.py` | Crear | Migración | Aditiva |
| `proyectos/cimiento/core/estandar/cambios.py` | Crear | Lógica | Guardar, quitar, armar el mapa, aplicar propuestas |
| `proyectos/cimiento/core/estandar/views.py` | Crear | Vista | |
| `proyectos/cimiento/core/estandar/urls.py` | Crear | Rutas | |
| `proyectos/cimiento/core/estandar/templates/estandar/_mensajes.html` | Crear | Plantilla | Los mensajes de las pantallas del estándar |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/documento.html` | Crear | Plantilla | Ver y editar |
| `proyectos/cimiento/core/estandar/templates/estandar/recuerdos.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/recuerdo.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/propuestas.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/management/commands/proponer.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/management/commands/ver_estandar.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/management/commands/ver_recuerdo.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/tests_pantalla.py` | Crear | Test | |
| `proyectos/cimiento/core/enganches/recuerdos.py` | Modificar | Lógica | El índice de la memoria sale de la base |
| `proyectos/cimiento/core/historia/versiones.py` | Modificar | Lógica | Una propuesta tiene historia pero no sube versión: no cambia nada hasta aprobarse |
| `proyectos/cimiento/config/urls.py` | Modificar | Rutas | |
| `proyectos/cimiento/templates/base.html` | Modificar | Plantilla | Entrada «Estándar» del menú |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Ayuda | |
| `proyectos/cimiento/core/ayuda/templates/ayuda/secciones/estandar.html` | Crear | Ayuda | |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `Recuerdos.contexto` | el arranque (`hook_sesion.py`) | `core.enganches.tests_sesion` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

| Ruta | Método | Quién |
|---|---|---|
| `/estandar/` | GET | Toda cuenta |
| `/estandar/documento/<id>/` | GET; POST cambia | Toda cuenta mira; administrador cambia |
| `/estandar/nuevo/` | GET, POST | Administrador |
| `/estandar/documento/<id>/quitar/` | POST | Administrador |
| `/estandar/memoria/<proyecto>/` | GET | Toda cuenta |
| `/estandar/memoria/<proyecto>/<id>/` y `/nuevo/` | GET; POST cambia | Toda cuenta mira; administrador cambia |
| `/estandar/propuestas/` | GET | Toda cuenta |
| `/estandar/propuestas/<id>/aprobar/` y `/rechazar/` | POST | Administrador |

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

Menú lateral → «Estándar», con enlaces a la memoria de cada proyecto y a las propuestas.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno nuevo.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Se edita el documento entero como markdown | Un formulario por regla | Es como está guardado (HU-003); el molde de la regla no cambia | Propuesta del agente |
| El mapa y las reglas por tarea se arman en la base al guardar | Dejarlos viejos | Son derivados: si no se arman, el agente recibe reglas de antes | Propuesta del agente |
| La propuesta guarda el texto completo que propone | Un parche | Se ve qué queda y se aplica sin calcular nada | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Guardar, crear o quitar un documento o un recuerdo | Deshacer el cambio desde «Historia» |
| Proponer | Rechazar la propuesta |
| Aprobar una propuesta | Deshacer el cambio que dejó |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Guardar, quitar y armar el mapa en la base | Lógica | 1,5 h | — | EV-01 |
| T-02 | Pantallas del estándar | Vista | 2 h | T-01 | EV-01 |
| T-03 | Memoria en la pantalla y en el arranque | Vista | 1,5 h | — | EV-01 |
| T-04 | Propuestas y sus órdenes | Lógica | 1,5 h | T-01 | EV-01 |
| T-05 | `ver_estandar` y `ver_recuerdo` | Orden | 0,5 h | — | EV-01 |
| T-06 | Ayuda, menú y pruebas | Test | 1,5 h | T-01 a T-05 | EV-01 |

**Total estimado:** 8,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-04, T-06. **Paralelizables:** T-03 y T-05.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |
| CA-04 | Pruebas de Django | EV-01 | | ☐ |
| CA-05 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django con el estándar importado en la prueba |
| Usuarios de prueba | Una cuenta administradora y una de consulta |
| Datos precargados | Un proyecto con recuerdos |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit y `manage.py migrate estandar 0001`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: una tabla nueva.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `00·N1`, `20·M10`, `20·M11`, `01·C19`, `02·F30`.

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
