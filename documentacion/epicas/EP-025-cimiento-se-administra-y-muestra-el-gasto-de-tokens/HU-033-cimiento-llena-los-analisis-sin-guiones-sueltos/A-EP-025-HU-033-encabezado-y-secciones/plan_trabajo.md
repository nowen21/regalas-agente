# Plan de Trabajo · Fase A-EP-025-HU-033-encabezado-y-secciones (módulo análisis en curso)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-033-encabezado-y-secciones` |
| **Épica** | `EP-025` |
| **HU** | [`HU-033`](../HU-033-cimiento-llena-los-analisis-sin-guiones-sueltos.md), una sola (`F12.1`) |
| **Módulo** | Análisis en curso: `proyectos/cimiento/core/enganches/` y un comando de `core/proyectos/` |
| **Especificación del módulo** | La HU-033 y la [épica EP-025](../../epica.md) |
| **Fecha apertura** | 2026-10-09 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 3 del pendiente 133](../../../../../historico-chat/resumenes/2026-10-05/pendientes/133-el-recordatorio-de-reglas-se-paga-en-cada-mensaje/analisis-3.md), el 2026-10-09, en el turno 52, con la versión 59.3.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Funcionalidad nueva: Cimiento llena el encabezado de un análisis al prenderlo y trae un comando para guardar sus secciones (análisis 3 del pendiente 133, acuerdo 1).

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-033` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-033-cimiento-llena-los-analisis-sin-guiones-sueltos.md#ca-01--al-prender-el-encabezado-queda-lleno) | ☐ |
| [CA-02](../HU-033-cimiento-llena-los-analisis-sin-guiones-sueltos.md#ca-02--un-comando-fijo-guarda-el-texto-de-una-sección) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** al prender un análisis nuevo quedan puestas las rutas, la copia del pendiente y, en el análisis 1, la copia del hallazgo; y `manage.py analisis seccion` guarda el texto de cualquier sección.

**Fuera de alcance:** pasar los análisis a la base (EP-030·HU-003) y los documentos de cierre de las fases (pendiente 147).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`AnalisisEnCurso.nuevo_analisis` (`core/enganches/analisis_en_curso.py`) copia `plantillas/analisis.md` y solo cambia el número del título. La plantilla marca con `«RUTA-ESTANDAR»` las rutas al estándar, con `analisis-«N+1»` el siguiente análisis, y con `«copia del hallazgo»` y `«copia del pendiente»` las dos copias, cada una con su nota encima. El «De dónde sale» del pendiente enlaza el hallazgo con su número, «H-N», al resumen donde nació. Los comandos de Cimiento viven en `core/*/management/commands/`; `cerrar_fase` está en `core/proyectos/`.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/enganches/llenar_analisis.py` | Crear | Lógica | Llena el encabezado y pone el texto de una sección |
| `proyectos/cimiento/core/enganches/analisis_en_curso.py` | Modificar | Lógica | `nuevo_analisis` llena el encabezado |
| `proyectos/cimiento/core/proyectos/management/commands/analisis.py` | Crear | Comando | `manage.py analisis seccion` |
| `proyectos/cimiento/core/enganches/tests_llenar_analisis.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

No aplica.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: es la consola.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La copia del hallazgo se pone solo en el análisis 1 | Copiar el último hallazgo del «De dónde sale» | Desde el análisis 2, el hallazgo que lo abre es nuevo y todavía no está en el pendiente | Propuesta del agente |
| Las copias reemplazan la nota y la marca juntas | Dejar la nota | La plantilla pide borrar las notas al llenar | Acuerdo 1 |
| La sección se busca por el comienzo de su título, sin importar mayúsculas | Pedir el título exacto | «Lo acordado» basta para encontrar la sección | Propuesta del agente |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

El comando guarda el texto anterior de la sección en su salida, para volver a ponerlo con el mismo comando. El encabezado se llena una sola vez, al crear el análisis; borrarlo es editar el análisis.

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Llenar el encabezado | Lógica | 0,5 h | — | EV-01 |
| T-02 | Poner una sección y el comando | Comando | 0,5 h | — | EV-01 |
| T-03 | Pruebas | Test | 0,5 h | T-01, T-02 | EV-01 |

**Total estimado:** 1,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Carpetas temporales con un pendiente, su resumen y la plantilla real |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `04·S18`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Llenar el encabezado falla | El análisis no se crearía | Si falla, se crea con la plantilla tal cual | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
