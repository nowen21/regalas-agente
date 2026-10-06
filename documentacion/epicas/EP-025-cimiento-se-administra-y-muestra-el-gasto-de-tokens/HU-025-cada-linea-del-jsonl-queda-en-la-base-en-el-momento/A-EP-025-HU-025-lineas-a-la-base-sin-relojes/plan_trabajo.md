# Plan de Trabajo · Fase «A-EP-025-HU-025-lineas-a-la-base-sin-relojes» (módulo «Cimiento, consumo»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-025-HU-025-lineas-a-la-base-sin-relojes` |
| **Épica** | `EP-025` |
| **HU** | [`HU-025`](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/consumo/` |
| **Especificación del módulo** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) y la docstring de [vigilante.py](../../../../../proyectos/cimiento/core/consumo/vigilante.py) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 124](../../../../../historico-chat/resumenes/2026-10-05/pendientes/124-la-pantalla-gasto-no-dice-por-donde-empezar/analisis-1.md), el 2026-10-05, con la versión 55.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Híbrido: modifica `A-EP-025-HU-011-el-vigilante`, que dejó dos relojes sin acuerdo (2 y 60 segundos), y suma algo nuevo, el guardado de cada línea del `.jsonl` en la base. Sale del análisis 1 del pendiente 124, acuerdos 4, 5 y 6.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-025` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-01--la-línea-queda-en-la-base-sin-claves-y-una-sola-vez) | ☐ |
| [CA-02](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-02--el-vigilante-guarda-en-el-momento-del-aviso) | ☐ |
| [CA-03](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-03--un-proyecto-nuevo-entra-con-su-primer-aviso) | ☐ |
| [CA-04](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-04--el-readme-dice-cómo-llega-el-gasto) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que cada línea de los `.jsonl` de los proyectos activos quede en la base de Cimiento, sin claves, en el aviso de Windows que la trae, y que el vigilante no tenga relojes.

**Resumen de CA a cubrir:**

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-01 | La línea queda en la base, sin claves y una sola vez | Funcional | Media |
| CA-02 | El vigilante guarda en el momento del aviso | Funcional | Media |
| CA-03 | Un proyecto nuevo entra con su primer aviso | Funcional | Baja |
| CA-04 | El README dice cómo llega el gasto | Documental | Baja |
| RNF-01 | Lo que entra pasa por el `Enmascarador` | No funcional | Baja |
| RNF-02 | Releer desde cero no agota la memoria | No funcional | Media |

**Fuera de alcance:**

- Avisarle a la pantalla: EP-025·HU-027.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`GuardadoDeConsumo.leer_archivo` ([guardar.py](../../../../../proyectos/cimiento/core/consumo/guardar.py)) lee desde el byte guardado en `AvanceDeLectura` con `LectorDeClaudeCode`, que toma solo líneas completas, y guarda conteos en una transacción. `VigilanteDeConsumo` anota en `cambiados` cada aviso y guarda cada 2 segundos (`CADA`); relee los proyectos cada 60 (`LISTA_CADA`). `Enmascarador.enmascarar(texto)` en `core/enganches/enmascarar.py` devuelve `(texto, cuántas)`. La última migración de `consumo` es `0004_tercera_tanda`. `~/.claude/projects/` pesa 438 MB.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/consumo/models.py` | Modificar | Modelo | `LineaDeSesion` |
| `proyectos/cimiento/core/consumo/migrations/0005_lineas_de_sesion.py` | Nuevo | BD | |
| `proyectos/cimiento/core/consumo/lector.py` | Modificar | Servicio | Líneas crudas con su posición |
| `proyectos/cimiento/core/consumo/guardar.py` | Modificar | Servicio | Guarda las líneas tapadas |
| `proyectos/cimiento/core/consumo/vigilante.py` | Modificar | Servicio | Sin relojes |
| `proyectos/cimiento/core/consumo/management/commands/vigilar_consumo.py` | Modificar | Comando | Espera sin reloj |
| `proyectos/cimiento/core/consumo/management/commands/leer_consumo.py` | Modificar | Comando | `--desde-cero` |
| `proyectos/cimiento/core/consumo/tests_lineas.py` | Nuevo | Test | |
| `proyectos/cimiento/core/consumo/tests_vigilante.py` | Modificar | Test | |
| `proyectos/cimiento/README.md` | Modificar | Doc | |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 55.2.0, MENOR |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `core/consumo/vigilante.py` | `avisar` guarda en el acto; salen `guardar_lo_cambiado`, `CADA` y `LISTA_CADA`; `correr` recibe un evento de parada | `tests_vigilante.py`, `vigilar_consumo.py` | Llaman `guardar_lo_cambiado` y `correr(mientras=…)` |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

No aplica: las líneas se guardan sin pantalla; las muestra la HU-026 a través de sus conteos.

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Cada línea es única por archivo y huella (SHA-1 del texto crudo) | Única por archivo y posición | Si Claude Code reescribe el archivo, la misma posición trae otra línea y se perdería una de las dos | Propuesta del agente |
| Los conteos salen de la línea original y la base guarda la tapada | Contar sobre la tapada | El tapado puede cambiar un valor dentro del JSON | Análisis 1, acuerdo 5 |
| `avisar` guarda en el hilo de `watchdog`, con un candado | Una cola y un hilo que la revisa | La cola necesita revisarse cada cierto tiempo: es un reloj | Análisis 1, acuerdo 4 |
| `correr` espera un evento sin tiempo; se para con `--parar` | Despertar cada N segundos a ver si hay que parar | Un despertar periódico es un reloj | Análisis 1, acuerdo 4 |
| `leer_consumo --desde-cero` trae lo que ya está en los `.jsonl` | Dejar solo lo que llegue desde hoy | Lo que ya está se perdería a los 30 días | Análisis 1, acuerdo 5 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción nueva | Su contraria | Prueba |
|---|---|---|
| Migración `0005` crea la tabla | `migrate consumo 0004` la quita | CP-006 |
| `leer_consumo --desde-cero` relee | No tiene vuelta ni la necesita: leer dos veces deja la base igual | CP-002 |

## 3. Desglose de tareas por criterio de aceptación

### [CA-01](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-01--la-línea-queda-en-la-base-sin-claves-y-una-sola-vez) · La línea queda en la base

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Modelo `LineaDeSesion` y migración `0005` | BD | 0,5 h | — | |
| T-02 | El lector devuelve las líneas crudas con su posición | Servicio | 0,5 h | — | |
| T-03 | `leer_archivo` guarda las líneas tapadas en la misma transacción | Servicio | 1 h | T-01, T-02 | EV-01 |
| T-04 | `leer_consumo --desde-cero` | Comando | 0,5 h | T-03 | EV-01 |
| T-05 | `tests_lineas.py` | Test | 1 h | T-03 | EV-01 |

### [CA-02](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-02--el-vigilante-guarda-en-el-momento-del-aviso) y [CA-03](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-03--un-proyecto-nuevo-entra-con-su-primer-aviso) · El vigilante sin relojes

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-06 | `avisar` guarda en el acto; relee la lista ante una carpeta desconocida | Servicio | 1 h | — | EV-02 |
| T-07 | `correr` y `vigilar_consumo` esperan sin reloj | Comando | 0,5 h | T-06 | EV-02 |
| T-08 | Ajustar `tests_vigilante.py` | Test | 1 h | T-06 | EV-02 |

### [CA-04](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-04--el-readme-dice-cómo-llega-el-gasto) · README

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-09 | Reescribir el párrafo del gasto en el README | Doc | 0,2 h | — | EV-03 |
| T-10 | CHANGELOG y VERSION 55.2.0 | Versión | 0,2 h | T-09 | EV-03 |

**Total estimado:** 6,4 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-05, T-06, T-08.
**Paralelizables:** T-09 y T-10 con el resto.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | `tests_lineas` | EV-01 | | ☐ |
| CA-02 | `tests_vigilante` y búsqueda de `sleep` | EV-02 | | ☐ |
| CA-03 | `tests_vigilante` | EV-02 | | ☐ |
| CA-04 | Lectura del README | EV-03 | | ☐ |

**Registro de evidencias:**

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `manage.py test core.consumo.tests_lineas` | `resultado_pruebas.md` |
| EV-02 | Salida de `manage.py test core.consumo.tests_vigilante` | `resultado_pruebas.md` |
| EV-03 | Texto | `proyectos/cimiento/README.md`, `CHANGELOG.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | Base de pruebas que crea `manage.py test` en MariaDB local |
| Usuarios de prueba | No aplica |
| Datos precargados | `.jsonl` de muestra que arman las pruebas en una carpeta temporal; la clave de prueba se arma en tiempo de ejecución, sin secretos literales |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

`python manage.py migrate consumo 0004` quita la tabla, y revertir el commit devuelve el vigilante anterior.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditivo: tabla nueva. Después de migrar, `python manage.py leer_consumo --desde-cero` una vez trae lo que ya está en los `.jsonl`, y hay que reiniciar el vigilante (`vigilar_consumo --parar` y arrancarlo).

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`01·C29`](../../../../../base/01-conducta.md#c29--guarda-dentro-del-repositorio-todo-lo-del-agente-y-del-proyecto), [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada), [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md), [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | En Windows, Ctrl+C no corta una espera sin tiempo | `vigilar_consumo` en una consola no se detiene con Ctrl+C | Se detiene con `--parar`, que es como lo detiene la instalación | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Requisitos no funcionales validados
- [ ] Pruebas de la fase en verde, solo las suites que la fase toca ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** 1, el tapado no conoce las claves de Anthropic: H-3 del resumen de la sesión del 2026-10-05, pendiente 129. No obligó a tocar nada fuera del plan.
