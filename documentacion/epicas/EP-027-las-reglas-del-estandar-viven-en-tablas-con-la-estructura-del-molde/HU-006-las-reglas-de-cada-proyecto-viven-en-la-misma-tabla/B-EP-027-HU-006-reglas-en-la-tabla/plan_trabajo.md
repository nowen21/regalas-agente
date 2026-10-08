# Plan de Trabajo · Fase B-EP-027-HU-006-reglas-en-la-tabla (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-027-HU-006-reglas-en-la-tabla` |
| **Épica** | `EP-027` |
| **HU** | [`HU-006`](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base: `core/estandar/` |
| **Especificación del módulo** | La HU-006, RN-01 a RN-04 |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el usuario, que aprobó el alcance de la HU-006, el 2026-10-07, con la versión 57.4.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `A-EP-027-HU-001-las-casillas` (el molde) y `A-EP-027-HU-002-el-paso` (el paso a las tablas). Depende de `A-EP-027-HU-006-version-del-proyecto`.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-02](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md#ca-02--las-reglas-del-proyecto-pasan-a-la-tabla-sin-perder-nada) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** leer las reglas de un proyecto en `##` o en `###`, guardarlas en la tabla con su proyecto y su grupo, guardar el archivo entero en la historia antes de borrarlo, y verlas y cambiarlas en Cimiento.

**Fuera de alcance:** el índice al abrir la sesión (fase C), el catálogo (fase D), la plantilla y el paso de los cinco proyectos (fase E).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`molde.partir` y `molde.leer` solo leen `## <código> · <título>`. Cuatro proyectos escriben sus reglas en `###`, agrupadas en secciones `##` (AgroSystem tiene siete); RNI las escribe en `##`. Fuera de las reglas cada archivo trae entre 212 y 2.339 caracteres, casi todo el texto de la plantilla `plantillas/reglas-proyecto.md`. `Regla.proyecto` ya existe (HU-001) y su versión es la del proyecto (fase A).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/molde.py` | Modificar | Lógica | Leer y partir reglas en `##` o `###` |
| `proyectos/cimiento/core/estandar/models.py` | Modificar | Modelo | Casilla `grupo` |
| `proyectos/cimiento/core/estandar/migrations/0007_grupo.py` | Crear | Migración | |
| `proyectos/cimiento/core/estandar/reglas.py` | Modificar | Lógica | Pasar y armar las reglas de un proyecto; el archivo a la historia |
| `proyectos/cimiento/core/estandar/management/commands/pasar_reglas_proyecto.py` | Crear | Comando | Pasa un proyecto o todos; con `--borrar`, borra el archivo |
| `proyectos/cimiento/core/estandar/management/commands/ver_regla.py` | Crear | Comando | El índice de las reglas de un proyecto, o una regla |
| `proyectos/cimiento/core/estandar/views.py` | Modificar | Vista | `ReglasDelProyecto`: ver y cambiar |
| `proyectos/cimiento/core/estandar/urls.py` | Modificar | Ruta | `proyecto/<pk>/reglas/` |
| `proyectos/cimiento/core/estandar/templates/estandar/reglas_del_proyecto.html` | Crear | Plantilla | |
| `proyectos/cimiento/core/estandar/templates/estandar/lista.html` | Modificar | Plantilla | Enlace a las reglas de cada proyecto |
| `proyectos/cimiento/core/estandar/tests_reglas_del_proyecto.py` | Crear | Test | |
| `proyectos/cimiento/core/ayuda/textos.py` | Modificar | Texto | La ayuda de la pantalla nueva y de su campo, como en la HU-004 |
| `proyectos/cimiento/core/ayuda/secciones.py` | Modificar | Texto | La pantalla nueva entra a la sección «El estándar y la memoria» del manual |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `molde.partir` y `molde.leer` | El paso de las reglas del estándar | `core.estandar` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

`estandar/proyecto/<pk>/reglas/`: toda cuenta mira; solo el grupo administrador cambia.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar → Reglas y documentos», tarjeta «Reglas de cada proyecto».

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El archivo entero queda como un cambio de la historia del proyecto | Guardar el texto que no es regla en una casilla | Es casi todo el texto de la plantilla; en la historia queda completo y con su fecha | RN-04 |
| Cambiar las reglas del proyecto se hace sobre el texto de todas, que pasa a la tabla al guardar | Un formulario por casilla | Igual que el estándar (HU-003) | HU-003 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| `pasar_reglas_proyecto --borrar` | El archivo vuelve desde la historia del proyecto: el cambio guarda su texto entero; o desde git del proyecto |
| Migración `0007_grupo` | Su reversión |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Molde con dos niveles, casilla `grupo`, pasar y armar | Lógica | 1,5 h | Ninguna | EV-01 |
| T-02 | Los dos comandos | Comando | 0,5 h | T-01 | EV-01 |
| T-03 | La pantalla | Vista | 1 h | T-01 | EV-01 |
| T-04 | Pruebas | Test | 1 h | T-03 | EV-01 |

**Total estimado:** 4 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-02 | Prueba de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django y una carpeta temporal de proyecto |
| Usuarios de prueba | Una cuenta administradora y una de consulta |
| Datos precargados | Un archivo de reglas con dos grupos en `###` y otro con reglas en `##` |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

`migrate estandar 0006` y revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditiva: una casilla vacía. Los proyectos se pasan en la fase E.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md), `20·M11`, `20·M16`.

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
