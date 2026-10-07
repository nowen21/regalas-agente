# Plan de Trabajo · Fase A-EP-026-HU-006-congelar-base (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-006-congelar-base` |
| **Épica** | `EP-026` |
| **HU** | [`HU-006`](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-006 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las que escribieron el freno (`EP-023·HU-007`) y el control de versión del commit (`EP-005·HU-005`). Sale del análisis 1 del pendiente 132, acuerdos 15 y 20.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-006` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md#ca-01--el-freno-no-deja-tocar-base) | ☐ |
| [CA-02](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md#ca-02--el-commit-no-deja-pasar-base-y-pide-la-versión-de-las-plantillas-en-la-base) | ☐ |
| [CA-03](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md#ca-03--congelar-y-descongelar) | ☐ |
| [CA-04](../HU-006-los-archivos-de-base-quedan-quietos-en-la-version-55-1-0.md#ca-04--el-agente-lee-las-reglas-completas-de-la-base) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** congelar `base/`, `VERSION` y `CHANGELOG.md` con una orden, que el freno y el commit lo respeten, y que el agente lea las reglas completas de la base.

**Fuera de alcance:** otros proyectos.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`Freno.motivo` (`core/enganches/freno.py`) decide si una ruta se deja escribir. `VersionDelCambio` (`core/validadores/guardian_version.py`) exige `VERSION` y `CHANGELOG.md` cuando el commit trae `base/` o `plantillas/`. `Cargador.instruccion` y `RecuperadorDeReglas.bloque_descartadas` y `bloque_siempre` dicen que las reglas completas están en archivos de `base/`. Los ajustes comunes viven en `proyectos_ajustebase`. La base va en 56.2.0 y `VERSION` en 56.8.0.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/congelado.py` | Crear | Lógica | La marca, leer sin Django, la última versión del estándar |
| `proyectos/cimiento/core/estandar/management/commands/congelar_base.py` | Crear | Orden | Y su contraria |
| `proyectos/cimiento/core/estandar/management/commands/registrar_version.py` | Crear | Orden | Versión del estándar sin cambio de documentos |
| `proyectos/cimiento/core/estandar/tests_congelado.py` | Crear | Test | |
| `proyectos/cimiento/core/estandar/tests_en_base.py` | Modificar | Test | «Mismas reglas» compara sin el aviso de `ver_estandar`, que solo lleva el texto de la base |
| `proyectos/cimiento/core/enganches/freno.py` | Modificar | Lógica | No deja escribir lo congelado |
| `proyectos/cimiento/core/validadores/guardian_version.py` | Modificar | Lógica | Con el estándar congelado |
| `proyectos/cimiento/core/enganches/cargador.py` | Modificar | Lógica | Dice `ver_estandar` |
| `proyectos/cimiento/core/herramientas/recuperar.py` | Modificar | Lógica | Dice `ver_estandar` |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `Freno.motivo` | el freno antes y después de cada acción | `core.enganches.tests_freno` |
| `VersionDelCambio` | el `pre-commit` | `core.validadores` |
| `Cargador.instruccion`, `bloque_*` | el arranque y el enganche de reglas | `core.enganches.tests_sesion`, `core.herramientas.tests_respondo` |

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la UI

No aplica: `manage.py congelar_base`, `congelar_base --deshacer` y `registrar_version`.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| La marca es un ajuste común, `base_congelada`, y queda en la historia | Una tabla nueva | Ya existe la capa común y se lee sin Django | Propuesta del agente |
| Congelar alinea la versión de la base con la de `VERSION` | Dejarlas distintas | Desde ahí el número sigue en la base sin retroceder | Propuesta del agente |
| `plantillas/` sigue en git y su versión se registra en la base | Congelarlas también | Las plantillas siguen en archivos | Acuerdo 5 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| `congelar_base` | `congelar_base --deshacer` |
| `registrar_version` | Ninguna: una versión no se borra (`20·M11`) |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | La marca, congelar y descongelar | Lógica | 1 h | — | EV-01 |
| T-02 | El freno respeta la marca | Lógica | 0,5 h | T-01 | EV-01 |
| T-03 | El commit respeta la marca; `registrar_version` | Lógica | 1 h | T-01 | EV-01 |
| T-04 | Los textos dicen `ver_estandar` | Lógica | 0,5 h | — | EV-01 |
| T-05 | Pruebas y regresión | Test | 1 h | T-01 a T-04 | EV-01 |
| T-06 | Congelar en la base real | Datos | 0,2 h | T-05 | EV-02 |

**Total estimado:** 4,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01 a T-06, en orden.

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django y congelar la base real | EV-01, EV-02 | | ☐ |
| CA-04 | Pruebas de Django | EV-01 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de `congelar_base` real | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django y el estándar real |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

`congelar_base --deshacer` y revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Se enciende con `congelar_base` cuando `base/`, `VERSION` y `CHANGELOG.md` no tienen cambios sin guardar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `20·M10`, `20·M11`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión tiene cambios de `base/` sin guardar al congelar | Quedan fuera | `congelar_base` se niega si `base/`, `VERSION` o `CHANGELOG.md` tienen cambios sin guardar | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
