# Plan de Trabajo · Fase «A-EP-001-HU-040-c29-nombra-la-base-de-cimiento» (módulo «Capítulo 01»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-040-c29-nombra-la-base-de-cimiento` |
| **Épica** | `EP-001` |
| **HU** | [`HU-040`](../HU-040-c29-reconoce-la-base-de-cimiento.md), una sola (`F12.1`) |
| **Módulo** | Capítulo `01 · Conducta de la IA` |
| **Especificación del módulo** | [base/01-conducta.md](../../../../../base/01-conducta.md) |
| **Fecha apertura** | 2026-10-05 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto`, que creó `01·C29`. Retoma el caso que esa fase no previó: lo que la herramienta guarda afuera y no se puede corregir en su origen. Sale del [análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), acuerdo 5.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-040` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-01--la-regla-nombra-la-base-de-cimiento) | ☐ |
| [CA-02](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-02--la-regla-pasa-sus-comprobaciones) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que `01·C29` diga que lo del proyecto vive en el repositorio o en la base de datos del agente, y que lo que la herramienta guarda afuera sin poder corregirse en su origen se trae a esa base en cuanto aparece.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La regla nombra la base | Funcional | Baja |
| CA-02 | La regla pasa sus comprobaciones | Funcional | Baja |
| RNF-01 | La regla cita el acuerdo del que sale | No funcional | Baja |

**Fuera de alcance:**

- El guardado de los `.jsonl` en la base: EP-025·HU-025.
- `04·S9` y `01·C19`, que no cambian.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`01·C29` está en `base/01-conducta.md`, línea 1048, con su checklist en CUMPLE contra v39.0.0. Su cuerpo dice «vive en el repositorio» y «se corrige en su origen y no se lee de allá». La copian, generadas por `validadores/mapa_tareas.py`, `base/reglas-por-tarea/escribir-documento-1.md`, `cambiar-codigo-1.md` y `correr-comando.md`. La versión es 55.0.0.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `base/01-conducta.md` | Modificar | Regla | Cuerpo, ejemplo y checklist de `C29` |
| `base/reglas-por-tarea/escribir-documento-1.md`, `base/reglas-por-tarea/cambiar-codigo-1.md`, `base/reglas-por-tarea/correr-comando.md` | Modificar | Regla | Los regenera `mapa_tareas.py` |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 55.1.0, MENOR |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

No aplica: el título y el ancla de `C29` no cambian, así que ningún enlace se rompe.

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: es una regla.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La regla dice «la base de datos del agente» | «La base de Cimiento» | `20·M3` y la fila 5 del checklist prohíben nombres propios y herramientas en `base/` | Propuesta del agente |
| Se conserva el título y el ancla de `C29` | Cambiar el título | El ancla la citan el mapa de tareas, la memoria y otras reglas (`20·M11`) | Propuesta del agente |
| MENOR | PARCHE | Amplía dónde puede vivir lo del proyecto sin exigir nada nuevo (`20·M10`) | Análisis 1, acuerdo 5 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: la fase no agrega acciones.

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-01--la-regla-nombra-la-base-de-cimiento) · La regla nombra la base

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Reescribir cuerpo y ejemplo de `C29` | Regla | 0,5 h | — | EV-01 |
| T-02 | Regenerar las copias de `reglas-por-tarea/` | Regla | 0,2 h | T-01 | EV-01 |

### [CA-02](../HU-040-c29-reconoce-la-base-de-cimiento.md#ca-02--la-regla-pasa-sus-comprobaciones) · La regla pasa sus comprobaciones

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-03 | Volver a aplicar el checklist de `C29` | Regla | 0,3 h | T-01 | EV-01 |
| T-04 | CHANGELOG y VERSION 55.1.0 | Versión | 0,2 h | T-03 | EV-02 |
| T-05 | Correr `validar.py metareglas` y `validar.py estandar` | Test | 0,2 h | T-04 | EV-03 |

### RNF · Requisitos no funcionales

| ID | Tarea | Categoría | Est. | Ev. |
|---|---|---|:--:|---|
| T-06 | El checklist cita el acuerdo 5 del análisis | Trazabilidad | 0,1 h | EV-01 |

**Total estimado:** 1,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05
**Paralelizables:** T-06 con T-03.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Lectura de la regla | EV-01 | | ☐ |
| CA-02 | Validadores y lectura de CHANGELOG y VERSION | EV-02, EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Texto de la regla | `base/01-conducta.md`, `## C29` |
| EV-02 | Versión | `CHANGELOG.md`, `VERSION` |
| EV-03 | Salida de validadores | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | El repositorio del estándar, en la máquina local |
| Usuarios de prueba | No aplica |
| Datos precargados | No aplica |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit de la fase devuelve el texto anterior de `C29`, sus copias y la versión.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica porque es aditivo: ningún proyecto tiene que hacer nada para cumplir.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M3`, `20·M5`, `20·M10`, `20·M11`, `00·N6`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | `CHANGELOG.md` y `VERSION` tienen cambios de otra sesión sin guardar | Mezcla el versionado en el commit | Se agrega solo la entrada de esta fase y se avisa al pedir el commit | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Requisitos no funcionales validados
- [ ] Validadores en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno.
