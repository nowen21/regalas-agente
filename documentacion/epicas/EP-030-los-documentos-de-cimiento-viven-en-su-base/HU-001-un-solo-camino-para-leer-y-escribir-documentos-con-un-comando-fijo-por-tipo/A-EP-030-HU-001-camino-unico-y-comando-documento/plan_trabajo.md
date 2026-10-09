# Plan de Trabajo · Fase A-EP-030-HU-001-camino-unico-y-comando-documento (módulo Estándar de Cimiento)   ·   `[CAPA 3]`

**Para qué sirve este documento.** Explica qué se va a hacer en esta fase, en qué orden, sobre qué archivos y cómo se comprueba cada criterio de aceptación. El requisito vive en la HU y las pruebas en el `plan_pruebas` de la misma fase.

## 0. Identificación y origen  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q1-Q2 · [`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-030-HU-001-camino-unico-y-comando-documento` |
| **Épica** | `EP-030` |
| **HU** | [`HU-001`](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md), una sola (`F12.1`) |
| **Módulo** | Estándar de Cimiento, `proyectos/cimiento/core/estandar/` |
| **Especificación del módulo** | La HU-001 y la [épica EP-030](../../epica.md) |
| **Fecha apertura** | 2026-10-08 |
| **Aprobación** ([`02·F4`](../../../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md)) | [Análisis 1 del pendiente 142](../../../../../historico-chat/resumenes/2026-10-08/pendientes/142-los-documentos-de-cimiento-viven-en-la-base/analisis-1.md), el 2026-10-08, en el turno 49, con la versión 56.8.0 |
| **Rama** | `main` |

**ORIGEN** ([`13·DOC12`](../../../../../base/13-documentacion/reglas/DOC12-declara-el-origen-de-cada-fase-al-abrirla.md)):

- Fase nueva. Sale del análisis 1 del pendiente 142, acuerdos 1, 2, 3 y 5, punto 1 de «Lo que se tiene que hacer».

**CA de la HU que cubre esta fase** (trazabilidad [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)):

| CA de `HU-001` que cierra esta fase | Estado |
|---|---|
| [CA-01](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md#ca-01--un-comando-fijo-crea-muestra-edita-y-lista-un-documento) | ☑ |
| [CA-02](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md#ca-02--todo-programa-lee-y-escribe-documentos-por-el-mismo-camino) | ☑ |
| [CA-03](../HU-001-un-solo-camino-para-leer-y-escribir-documentos-con-un-comando-fijo-por-tipo.md#ca-03--cada-cambio-queda-en-la-historia) | ☑ |

## 1. Objetivo y alcance  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q4

**Objetivo:** un solo camino en Cimiento para leer y escribir documentos, con un registro de tipos, y un comando fijo `manage.py documento listar|ver|crear|editar|quitar <tipo>` que reemplaza los guiones sueltos.

**Alcance de esta fase:** los dos tipos que ya están en la base: los documentos del estándar (`Documento`) y los recuerdos (`Recuerdo`). Cada HU siguiente registra su tipo en el mismo camino.

**Fuera de alcance:** las tablas de los demás tipos (HU-003 a HU-006) y la pantalla de revisión general (HU-002).

## 2. Análisis previo, línea base verificada  ·  [`02·F17`](../../../../../base/02-flujo-de-trabajo/reglas/F17-verifica-contra-el-proyecto-real-todo-lo-que-el-plan-afirma.md)

`ver_estandar` y `ver_recuerdo` leen `Documento` y `Recuerdo` cada uno por su cuenta. `proponer` crea una `Propuesta` que se aprueba en «Estándar → Propuestas» antes de cambiar nada (EP-026·HU-005). `historia/registro.py` anota en `Cambio` todo lo que se guarda, con el antes y el después, por señales de Django: lo que pase por el ORM ya queda en la historia.

### 2.1 Archivos que se crean o modifican  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q9

| Archivo (ruta real verificada) | Tipo | Capa | Nota |
|---|---|---|---|
| `proyectos/cimiento/core/estandar/documentos.py` | Crear | Lógica | El registro de tipos y el camino único: listar, ver y proponer |
| `proyectos/cimiento/core/estandar/management/commands/documento.py` | Crear | Orden | El comando fijo |
| `proyectos/cimiento/core/estandar/management/commands/ver_estandar.py` | Modificar | Orden | Lee por el camino único |
| `proyectos/cimiento/core/estandar/management/commands/ver_recuerdo.py` | Modificar | Orden | Lee por el camino único |
| `proyectos/cimiento/core/estandar/management/commands/proponer.py` | Modificar | Orden | Propone por el camino único |
| `proyectos/cimiento/core/estandar/tests_documentos.py` | Crear | Test | |

### 2.2 Matriz de dependencias del refactor

| Lo que cambia | Quién lo usa |
|---|---|
| `ver_estandar`, `ver_recuerdo`, `proponer` | El aviso de cada sesión y Claude; los argumentos no cambian |

### 2.3 Rutas / endpoints y control de acceso  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q6

No aplica.

### 2.4 Punto de entrada en la UI  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q7

La consola: `manage.py documento`. Lo que se crea, edita o quita se aprueba en «Estándar → Propuestas».

### 2.5 Permisos / roles a sembrar  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q8

Ninguno.

### 2.6 Decisiones técnicas

| Decisión | Alternativa descartada | Justificación | Sale de |
|---|---|---|---|
| Crear, editar y quitar dejan una propuesta que se aprueba en la pantalla | Escribir directo en la tabla | Nada cambia sin revisarse en la pantalla | Acuerdo 5 |
| El camino vive en `core/estandar/`, sin una app nueva | Una app `core/documentos/` | No toca `INSTALLED_APPS`, que hoy cambia otra sesión; se puede mover después | Propuesta del agente |
| Cada tipo se registra con su modelo, sus campos de clave y sus campos de texto | Un modelo genérico único | Cada tipo va partido en sus propios campos | Acuerdo 2 |

### 2.7 Dudas por resolver antes de codificar

Ninguna.

### 2.8 La contraria de cada acción nueva  ·  [`02·F30`](../../../../../base/02-flujo-de-trabajo/reglas/F30-toda-accion-trae-su-contraria.md)

| Acción | Contraria |
|---|---|
| `documento crear` | `documento quitar` |
| Proponer | Rechazar la propuesta en la pantalla |

## 3. Desglose de tareas por criterio de aceptación

| ID | Tarea | Capa | Est. | Depende de | Ev. |
|---|---|---|:--:|---|---|
| T-01 | El registro de tipos y el camino único | Lógica | 1 h | — | EV-01 |
| T-02 | El comando `documento` | Orden | 1 h | T-01 | EV-01 |
| T-03 | `ver_estandar`, `ver_recuerdo` y `proponer` usan el camino | Orden | 0,5 h | T-01 | EV-01 |
| T-04 | Pruebas | Test | 1 h | T-01 a T-03 | EV-01 |

**Total estimado:** 3,5 h

## 4. Secuencia de ejecución

**Ruta crítica:** T-01, T-02, T-03, T-04

## 5. Verificación de criterios de aceptación  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q10

| CA | Método de verificación | Evidencia | Verificado | Estado |
|---|---|---|---|---|
| CA-01 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |
| CA-02 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |
| CA-03 | Pruebas de Django | EV-01 | 2026-10-09 | ☑ |

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Salida de las pruebas | `resultado_pruebas.md` de esta fase |

## 6. Datos y ambiente de prueba

| Elemento | Detalle |
|---|---|
| Ambiente | La base de pruebas de Django |
| Usuarios de prueba | Ninguno |
| Datos precargados | Un documento del estándar, un proyecto y un recuerdo, creados por la prueba |

## 7. Reversión / rollback  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q11

Revertir el commit.

## 8. Producción y migración incremental  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q12 · [`02·F10`](../../../../../base/02-flujo-de-trabajo/reglas/F10-planifica-la-migracion-en-vez-de-postergar-por-produccion.md)

No aplica: no cambia la base.

## 9. Reglas del estándar y del proyecto aplicadas  ·  [`02·F14`](../../../../../base/02-flujo-de-trabajo/reglas/F14-responde-las-trece-preguntas-en-todo-plan-de-trabajo.md) Q13

- Base: [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md), `08·T1`, `02·F30`.

## 10. Riesgos y bloqueos

| ID | Riesgo o bloqueo | Impacto | Acción | Estado |
|---|---|---|---|---|
| B-01 | Cambiar `ver_estandar` daña el aviso de cada sesión | Ninguna sesión lee las reglas | Los argumentos y la salida no cambian; una prueba lo compara | Abierto |

## 11. Definition of Done

- [x] Todos los CA de la sección 0 verificados con evidencia en la sección 5
- [x] Pruebas en verde
- [ ] Rama lista para el commit único de la fase ([`09·G1`](../../../../../base/09-git.md#g1--commits-atómicos-un-solo-propósito))

## 13. Cierre

**Hallazgos al ejecutar:** ninguno todavía.
