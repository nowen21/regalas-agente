# Plan de Trabajo · Fase E-EP-027-HU-006-la-plantilla-y-el-paso (módulo Plantillas e instalación)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `E-EP-027-HU-006-la-plantilla-y-el-paso` |
| **Épica** | `EP-027` |
| **HU** | [`HU-006`](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md), una sola (`F12.1`) |
| **Módulo** | Plantillas del estándar (`plantillas/`) e instalación (`core/herramientas/`) |
| **Especificación del módulo** | La HU-006, RN-08 y RN-09 |
| **Fecha apertura** | 2026-10-07 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 136](../../../../../historico-chat/resumenes/2026-10-06/pendientes/136-el-estandar-en-la-pantalla-se-lista-por-ruta-y-no-por-titulo/analisis-1.md) y el usuario, que aprobó el alcance de la HU-006, el 2026-10-07, con la versión 57.4.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): la que hizo la plantilla `CLAUDE.md` y su punto 5.2. Depende de las fases B, C y D de esta HU.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-05](../HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla.md#ca-05--la-plantilla-y-el-instalador-dicen-dónde-viven) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que la plantilla `CLAUDE.md` diga dónde viven las reglas del proyecto, proponer el cambio de los cinco documentos del estándar que nombran el archivo, y pasar las reglas de los proyectos a la tabla, borrando su archivo.

**Fuera de alcance:** commits en los repositorios de los proyectos; renumerar la P45 de AgroSystem (H-26), que decide el usuario.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`plantillas/CLAUDE.md.plantilla` nombra el archivo en la sección 2.1, en el paso 4 de cada sesión y en el punto 5.2. El instalador no crea el archivo (`core/herramientas/instalar.py` solo llena el marcador del punto 5.2). Cada proyecto corre el instalador al abrir su sesión (paso 1 de su `CLAUDE.md`), que pone al día lo que la plantilla cambió. El archivo es local y no se versiona (`plantillas/reglas-proyecto.md`): el paso guarda su texto entero en la historia de Cimiento antes de borrarlo. Cinco documentos de `base/` nombran el archivo: `02-flujo-de-trabajo/estructura-base.md`, `20-meta-reglas/base.md`, `20-meta-reglas/desempate.md`, `20-meta-reglas/estructura-regla.md` y `glosario.md`; el estándar se cambia por propuesta.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `plantillas/CLAUDE.md.plantilla` | Modificar | Plantilla | 2.1, paso 4 y 5.2: las reglas del proyecto registrado viven en Cimiento |
| `plantillas/reglas-proyecto.md` | Modificar | Plantilla | Su nota dice que es solo para el proyecto que Cimiento no tiene registrado |
| `proyectos/cimiento/core/herramientas/tests_reglas_en_cimiento.py` | Crear | Test | |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/E-EP-027-HU-006-la-plantilla-y-el-paso/propuestas/estructura-base.txt` | Crear | Borrador | Propuesta de `base/02-flujo-de-trabajo/estructura-base.md` |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/E-EP-027-HU-006-la-plantilla-y-el-paso/propuestas/meta-reglas-base.txt` | Crear | Borrador | Propuesta de `base/20-meta-reglas/base.md` |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/E-EP-027-HU-006-la-plantilla-y-el-paso/propuestas/desempate.txt` | Crear | Borrador | Propuesta de `base/20-meta-reglas/desempate.md` |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/E-EP-027-HU-006-la-plantilla-y-el-paso/propuestas/estructura-regla.txt` | Crear | Borrador | Propuesta de `base/20-meta-reglas/estructura-regla.md` |
| `documentacion/epicas/EP-027-las-reglas-del-estandar-viven-en-tablas-con-la-estructura-del-molde/HU-006-las-reglas-de-cada-proyecto-viven-en-la-misma-tabla/E-EP-027-HU-006-la-plantilla-y-el-paso/propuestas/glosario.txt` | Crear | Borrador | Propuesta de `base/glosario.md` |
| `historico-chat/scripts/2026-10-07/propuestas_reglas_proyecto.py` | Crear | Guion de apoyo | Arma los cinco borradores desde la base |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| La plantilla `CLAUDE.md` | El instalador de cada proyecto | `core.herramientas` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

Ninguna.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

«Estándar → Propuestas por aprobar», para las cinco propuestas.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| El `CLAUDE.md` de cada proyecto se pone al día solo, con el instalador de su próxima sesión | Correr el instalador en los cinco proyectos desde aquí | Es el camino de siempre y no toca otros repositorios | RN-09 |
| Los documentos del estándar cambian por propuesta | Cambiarlos directo | El estándar se cambia así (EP-026) | `20·M10` |
| El cambio de la plantilla sube versión MAYOR | MENOR | Cada proyecto tiene que ponerse al día | RN-09 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Borrar el archivo de reglas de un proyecto | Su texto entero está en la historia del proyecto en Cimiento, y `ver_regla --todas` lo da armado |
| Las propuestas | Rechazarlas en la pantalla |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La plantilla y su prueba | Plantilla | 1 h | Ninguna | EV-01 |
| T-02 | Las cinco propuestas | Borrador | 1 h | T-01 | EV-02 |
| T-03 | El paso de los proyectos, la copia y la versión | Datos | 0,5 h | T-01 | EV-02 |

**Total estimado:** 2,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-05 | Prueba de Django y el paso en la base viva | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida del paso y de las propuestas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La plantilla rellenada como la deja el instalador; después, la base viva |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit; el texto de cada archivo borrado se recupera de la historia del proyecto.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Copia de la base antes y después del paso (`00·N7`). El paso borra, con `pasar_reglas_proyecto --todos --borrar` y aprobado por el usuario el 2026-10-07, el archivo `.agente/reglas-proyecto.md` de dp_card (`C:/DesarrollosClaude/dp_card`), Gestión de Servicios Tecnológicos, LocalHub (`C:/DesarrollosClaude/personales/localhub`) y RNI (`C:/DesarrollosClaude/dp`); el de AgroSystem queda (H-26). No los edita la fase: los borra el comando, después de guardar cada texto en la historia. Mientras un proyecto no abra sesión, su `CLAUDE.md` dice «si existe el archivo, leerlo»: como ya no existe, no lo lee, y el arranque le entrega el índice desde la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `00·N7`, `20·M10`, `13·DOC10`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | AgroSystem no pasa por la P45 repetida | Sigue con su archivo | Lo decide el usuario | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
