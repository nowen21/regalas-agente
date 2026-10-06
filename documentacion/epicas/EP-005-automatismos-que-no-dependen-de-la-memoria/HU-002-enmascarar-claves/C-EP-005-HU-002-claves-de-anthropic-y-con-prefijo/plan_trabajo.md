# Plan de Trabajo · Fase «C-EP-005-HU-002-claves-de-anthropic-y-con-prefijo» (módulo «Cimiento, tapado de claves»)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación antes de darlo por cumplido. Se escribe antes de tocar nada y se aprueba antes de empezar: quien lo aprueba acepta el alcance y el costo. El requisito vive en la HU, el detalle de las pruebas en el `plan_pruebas` de la misma fase, y lo que quedó hecho en el `funcionalidad_implementada.md` del cierre.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `C-EP-005-HU-002-claves-de-anthropic-y-con-prefijo` |
| **Épica** | `EP-005` |
| **HU** | [`HU-002`](../HU-002-enmascarar-claves.md), una sola (`F12.1`) |
| **Módulo** | Cimiento, `core/validadores/secretos.py` y `core/enganches/enmascarar.py` |
| **Especificación del módulo** | [HU-002](../HU-002-enmascarar-claves.md) y las docstrings de los dos archivos |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 129](../pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/analisis-1.md), el 2026-10-06, con la versión 55.2.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): `B-EP-005-HU-002-la-clave-sin-comillas-tambien-se-tapa`, que sumó la clave sin comillas pero dejó fuera las variables con prefijo. Suma la forma de Anthropic. Sale del análisis 1 del pendiente 129, acuerdos 1 y 3. El análisis la llamó «fase B»; la B ya existía, así que es la C.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-002` que cierra esta fase | Estado |
|---|---|
| [CA-03](../HU-002-enmascarar-claves.md#ca-03--las-claves-de-anthropic-y-las-variables-con-prefijo-también-se-tapan) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que el tapado y el validador de secretos reconozcan las claves `sk-ant-` y toda variable que termine en `_API_KEY`, `_TOKEN`, `_SECRET` o `_PASSWORD`, sin tocar lo que lee del entorno.

| CA | Escenario | Tipo | Complejidad |
|---|---|---|---|
| CA-03 | Claves de Anthropic y variables con prefijo | Funcional | Baja |

**Fuera de alcance:**

- Volver a tapar lo ya guardado: EP-025·HU-025, fase B.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`SEGUROS` trae ocho formas sin Anthropic. `ASIGNA` empieza con `\b` antes de `api_key`, y `_ASIGNA_SIN_COMILLAS` igual, así que `ANTHROPIC_API_KEY` no entra: entre `_` y `A` no hay límite de palabra. Medido el 2026-10-06 sobre la base y el repositorio: no hay claves reales de Anthropic en claro.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/validadores/secretos.py` | Modificar | Servicio | Forma de Anthropic y nombre con prefijo en `ASIGNA` |
| `proyectos/cimiento/core/enganches/enmascarar.py` | Modificar | Servicio | Nombre con prefijo en `_ASIGNA_SIN_COMILLAS` |
| `proyectos/cimiento/core/enganches/tests_claves_con_prefijo.py` | Nuevo | Test | |
| `documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/HU-002-enmascarar-claves.md` | Modificar | Doc | CA-03 y la fila de la fase |
| `CHANGELOG.md`, `VERSION` | Modificar | Versión | 55.3.0, MENOR |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Archivo a refactorizar | Cambio de contrato | Archivos que dependen (rompen) | Dónde rompe |
|---|---|---|---|
| `secretos.py` (`ASIGNA`, `SEGUROS`) | Reconoce más: el grupo `clave` puede traer un prefijo | `enmascarar.py`, `validar.py secretos`, control de commits | No rompen: el grupo `valor` sigue igual; solo detectan más |

### 2.3 a 2.5

No aplica: sin rutas, sin pantalla, sin permisos.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La forma de Anthropic es `sk-ant-` seguido de 20 o más letras, números, `_` o `-` | Exigir el formato completo `sk-ant-api03-...` | Anthropic tiene más de un tipo de clave con ese comienzo | Análisis 1, acuerdo 1 |
| El prefijo se admite solo con `_`: `ALGO_API_KEY`, `ALGO_TOKEN` | Aceptar cualquier palabra pegada | Con `_` es el nombre de una variable; sin él, se taparía texto común | Análisis 1, acuerdo 1 |
| Las pruebas comparan con `assertFalse(clave in texto, mensaje)` | `assertNotIn` | `assertNotIn` repite la clave al fallar (señal S-315) | Análisis 1, lección 1 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

No aplica: la fase no agrega acciones, amplía lo que el tapado reconoce.

## 3. Desglose de tareas por criterio de aceptación

### [CA-03](../HU-002-enmascarar-claves.md#ca-03--las-claves-de-anthropic-y-las-variables-con-prefijo-también-se-tapan)

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Forma de Anthropic en `SEGUROS` | Servicio | 0,2 h | — | EV-01 |
| T-02 | Nombre con prefijo en `ASIGNA` | Servicio | 0,3 h | — | EV-01 |
| T-03 | Nombre con prefijo en `_ASIGNA_SIN_COMILLAS` | Servicio | 0,3 h | — | EV-01 |
| T-04 | `tests_claves_con_prefijo.py` | Test | 0,7 h | T-01 a T-03 | EV-01 |
| T-05 | Correr las suites del tapado y del validador | Test | 0,3 h | T-04 | EV-02 |
| T-06 | Correr `validar.py secretos` sobre el repositorio | Test | 0,2 h | T-02 | EV-03 |
| T-07 | CHANGELOG y VERSION 55.3.0 | Versión | 0,2 h | T-05 | |

**Total estimado:** 2,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05, T-06, T-07.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-03 | Pruebas y validador sobre el repositorio | EV-01, EV-02, EV-03 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de `tests_claves_con_prefijo` | `resultado_pruebas.md` |
| EV-02 | Salida de `tests_sesion` y `core.validadores` | `resultado_pruebas.md` |
| EV-03 | Salida de `validar.py secretos` | `resultado_pruebas.md` |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | `manage.py test` local |
| Datos | Claves armadas al correr, nunca escritas enteras en el archivo |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit de la fase.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Aditivo. Un proyecto que tenga escrita una clave con esas formas verá que su control de commits la señala: es lo que se busca.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`00·N6`](../../../../../base/00-nucleo-blindado.md#n6--una-credencial-no-se-escribe-no-se-registra-y-no-se-guarda-blindada), `04·S4`, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), [`02·F11`](../../../../../base/02-flujo-de-trabajo/reglas/F11-una-fase-solo-modifica-codigo-de-su-propio-modulo.md).

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Un nombre como `MAX_TOKEN = "algo"` se tapa sin ser clave | Texto tapado de más | El valor tiene que pasar `_parece_secreto` y, sin comillas, `_parece_clave_tecleada`; ante la duda se tapa (RNF de la HU) | Abierto |

## 11. Definition of Done

- [ ] CA-03 verificado con evidencia
- [ ] Suites del tapado y del validador en verde ([`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md))
- [ ] Rama lista para el commit único de la fase

## 13. Cierre

**Hallazgos al ejecutar:** ninguno.
