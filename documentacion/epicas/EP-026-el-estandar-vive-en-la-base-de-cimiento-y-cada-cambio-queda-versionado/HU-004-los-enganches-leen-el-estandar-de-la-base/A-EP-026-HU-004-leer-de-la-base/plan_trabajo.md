# Plan de Trabajo · Fase A-EP-026-HU-004-leer-de-la-base (módulo Estándar en la base)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-026-HU-004-leer-de-la-base` |
| **Épica** | `EP-026` |
| **HU** | [`HU-004`](../HU-004-los-enganches-leen-el-estandar-de-la-base.md), una sola (`F12.1`) |
| **Módulo** | Estándar en la base, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-004 y la [épica EP-026](../../epica.md) |
| **Fecha apertura** | 2026-10-06 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 132](../../../../../historico-chat/resumenes/2026-10-06/pendientes/132-la-pantalla-de-cimiento-es-el-estandar-y-versiona-cada-cambio/analisis-1.md), el 2026-10-06, con la versión 56.0.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Modifica fase(s): las que escribieron los lectores del estándar (`EP-005·HU-023` para `recuperar.py` y el mapa, `EP-023·HU-007` para el freno). Sale del análisis 1 del pendiente 132, acuerdos 5 y 9.

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-004` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-004-los-enganches-leen-el-estandar-de-la-base.md#ca-01--las-reglas-salen-de-la-base) | ☐ |
| [CA-02](../HU-004-los-enganches-leen-el-estandar-de-la-base.md#ca-02--sin-base-se-dice-y-el-freno-no-deja-modificar) | ☐ |
| [CA-03](../HU-004-los-enganches-leen-el-estandar-de-la-base.md#ca-03--mismas-reglas-que-antes) | ☐ |
| [CA-04](../HU-004-los-enganches-leen-el-estandar-de-la-base.md#ca-04--la-base-se-pone-al-día-con-git) | ☐ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** que los enganches lean el estándar de la base, con los mismos lectores, y que sin base no se trabaje.

**Fuera de alcance:** editar desde la pantalla (HU-005) y congelar `base/` (HU-006). Los validadores que se corren a mano siguen leyendo los archivos que se les den.

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

Recorren `base/`: `CuerpoDeReglas.leer` y `_definidas_arriba` (`core/validadores/metareglas.py`, con `Proyecto.recorrer_md`), `Autorizaciones.de_la_base` (`core/enganches/autorizado.py`, con `os.walk`), `Cargador.reglas` (`core/enganches/cargador.py`, con `os.walk`) y `MapaDeTareas.archivos_de` (`core/herramientas/mapa_tareas.py`, con `os.path.isfile`). Todos leen con `Archivos.leer`. `RecuperadorDeReglas` (`core/herramientas/recuperar.py`) arma `Archivos()` si no le dan uno. El freno ya detiene lo que modifica cuando la base no responde (`Freno.con_nivel`). En git, desde la importación, cambiaron `base/01-conducta/palabras-clave.md` y otros de la fase C de `EP-001·HU-036` («Liste» y «OK»).

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/en_base.py` | Crear | Lógica | El lector desde la base, sin Django |
| `proyectos/cimiento/core/estandar/importar.py` | Modificar | Lógica | `sincronizar` con lo guardado en git |
| `proyectos/cimiento/core/estandar/management/commands/sincronizar_estandar.py` | Crear | Orden | |
| `proyectos/cimiento/core/estandar/tests_en_base.py` | Crear | Test | |
| `proyectos/cimiento/core/validadores/metareglas.py` | Modificar | Lógica | Recorre con el lector que le den |
| `proyectos/cimiento/core/herramientas/mapa_tareas.py` | Modificar | Lógica | `archivos_de` pregunta al lector |
| `proyectos/cimiento/core/herramientas/recuperar.py` | Modificar | Lógica | Usa la base; sin base, lo dice |
| `proyectos/cimiento/core/enganches/autorizado.py` | Modificar | Lógica | Lee de la base |
| `proyectos/cimiento/core/enganches/cargador.py` | Modificar | Lógica | Lee de la base |

### 2.2 Matriz de dependencias del refactor  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

| Lo que cambia | Quién lo usa | Se prueba con |
|---|---|---|
| `CuerpoDeReglas.leer` | validadores, `catalogo.py` de niveles, `recuperar.py`, `mapa_tareas.py` | `core.validadores`, `core.niveles`, `core.herramientas.tests_respondo` |
| `MapaDeTareas.archivos_de` | `recuperar.py` | `core.herramientas.tests_respondo` |
| `Autorizaciones.de_la_base` | el freno, el `pre-commit` | `core.enganches.tests_freno` |
| `Cargador.reglas` | el arranque | `core.enganches.tests_sesion` |

### 2.3 Rutas / endpoints y control de acceso

No aplica.

### 2.4 Punto de entrada en la UI

No aplica.

### 2.5 Permisos / roles a sembrar

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Un lector con la cara de `Archivos` que sirve `base/` desde la base | Reescribir cada lector contra tablas | Los lectores no cambian lo que entienden, solo de dónde leen | Propuesta del agente |
| Solo para la carpeta del estándar | Para toda carpeta | Las pruebas y los proyectos tienen sus propios archivos | Propuesta del agente |
| Sin la tabla del estándar, el disco | Detener todo | Es el paso de una fuente a otra; sin base que responda, sí se detiene | Acuerdos 5 y 9 |
| Sincronizar con lo que dice git (`HEAD`), no con la carpeta | La carpeta | La carpeta puede tener cambios sin aprobar de otra sesión | Hallazgo del turno de la HU-003 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| Sincronizar la base con git | Deshacer cada cambio desde «Historia» |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | Lector desde la base | Lógica | 1 h | — | EV-01 |
| T-02 | Los cuatro lectores lo usan | Lógica | 1 h | T-01 | EV-01 |
| T-03 | Sin base, el enganche de reglas lo dice | Lógica | 0,5 h | T-01 | EV-01 |
| T-04 | `sincronizar_estandar` | Lógica | 1 h | — | EV-01 |
| T-05 | Pruebas y regresión | Test | 1,5 h | T-01 a T-04 | EV-01 |
| T-06 | Sincronizar la base real | Datos | 0,2 h | T-05 | EV-02 |

**Total estimado:** 5,2 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04, T-05, T-06

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | | ☐ |
| CA-02 | Pruebas de Django | EV-01 | | ☐ |
| CA-03 | Pruebas de Django | EV-01 | | ☐ |
| CA-04 | Pruebas de Django y sincronización real | EV-01, EV-02 | | ☐ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |
| EV-02 | Salida de la sincronización real | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django y el estándar real |
| Usuarios de prueba | Ninguno |
| Datos precargados | Ninguno |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit: los lectores vuelven al disco. La base sigue con el estándar y se puede vaciar con `manage.py migrate estandar zero`.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

Se enciende al quedar el código: la base ya tiene el estándar. Antes, `sincronizar_estandar` la pone al día con git, y `base/` tiene que estar sin cambios ajenos sin guardar.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `02·F7`, `20·M10`, `01·C29`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Otra sesión edita `base/` después de encender la lectura | Su cambio no rige | Se sincroniza antes y la HU-006 congela `base/` | Abierto |

## 11. Definition of Done

- [ ] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [ ] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
