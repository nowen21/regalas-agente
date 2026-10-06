# Funcionalidad implementada · Fase A-EP-001-HU-041-las-reglas-nombran-la-base (módulo Capítulos 01 y 20)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-001-HU-041-las-reglas-nombran-la-base` |
| **Módulo** | Capítulos `01 · Conducta de la IA` y `20 · Meta-reglas` |
| **Especificación del módulo** | [base/01-conducta.md](../../../../../base/01-conducta.md) y [base/20-meta-reglas/base.md](../../../../../base/20-meta-reglas/base.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | [HU-041](../HU-041-las-reglas-reconocen-la-base-de-cimiento-como-fuente-del-estandar.md) (CA-01, CA-02, CA-03) |
| **Fecha de cierre** | 2026-10-06 |
| **Versión del estándar al cerrar** | 56.0.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

`20·M10` exige que todo cambio, del estándar o de la configuración de un proyecto, suba su versión y deje registro de quién, cuándo, antes, después y por qué, en la base de datos del agente; mientras ella no guarde el estándar, en `CHANGELOG.md` y `VERSION`. El tipo sale de dos preguntas. `01·C19` pone la memoria en esa base. La nota y la restricción de EP-016 que decían «la fuente es el texto» quedan derogadas, y `CLAUDE.md` lo dice.

## 2. Trazabilidad  ·  [`13·DOC11`](../../../../../base/13-documentacion/reglas/DOC11-usa-la-tabla-canonica-de-cinco-columnas-para-la-trazabilidad.md)

### 2.1 Especificación → implementación

| Ítem del especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01: todo cambio sube una versión y queda registrado | doc | `M10-…md` | ✅ | CP-001 |
| RN-02: versión del proyecto o del estándar | doc | `base/20-meta-reglas/base.md`, sección «M10» | ✅ | CP-001 |
| RN-03: las dos preguntas | doc | `base/20-meta-reglas/base.md`, sección «M10» | ✅ | CP-001 |
| RN-04: la memoria en la base | doc | `base/01-conducta.md`, `## C19` | ✅ | CP-002 |
| RN-05: se deroga «la fuente es el texto» | doc | `notas/la-fuente-de-las-reglas-es-el-texto.md`, EP-016 | ✅ | CP-002 |
| RN-06: el commit desde la pantalla | doc | `CLAUDE.md`, sección 4 | ✅ | CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Reescribir `M10` | ✅ hecha | `M10-…md` | CP-001 |
| T-02 | Las dos preguntas en `base.md` | ✅ hecha | `base/20-meta-reglas/base.md` | CP-001 |
| T-03 | Reescribir `C19` | ✅ hecha | `base/01-conducta.md` | CP-002 |
| T-04 | Derogar la nota y la restricción de EP-016 | ✅ hecha | La nota y `EP-016/epica.md` | CP-002 |
| T-05 | Ajustar `CLAUDE.md` | ✅ hecha | `CLAUDE.md`, secciones 2 y 4 | CP-002 |
| T-06 | Checklist de `M10` y `C19` | ✅ hecha | Las dos reglas | CP-001 |
| T-07 | Regenerar el mapa y las copias | ✅ hecha | `base/reglas-por-tarea/cambiar-estandar.md`, `escribir-documento-1.md` | Verificación manual 1 |
| T-08 | CHANGELOG y VERSION 56.0.0 | ✅ hecha | `CHANGELOG.md`, `VERSION` | CP-004 |
| T-09 | Correr los validadores | ✅ hecha | `resultado_pruebas.md` §2 | CP-003 |

**Correspondencia con el plan:** 9 tareas en el plan, 9 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba**, [`02·F8`](../../../../../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md): ninguno. `escribir-documento-2.md` y `mapa-de-tareas.md` no cambiaron. `CHANGELOG.md` y `VERSION` traen además la 56.1.0 de otra sesión, que no es de esta fase.

**Esfuerzo real contra estimado:** 2,5 h contra 2,3 h.

## 3. Qué se probó  ·  `08` / [`02·F5`](../../../../../base/02-flujo-de-trabajo/reglas/F5-corre-solo-las-suites-que-la-fase-toca.md)

| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

| Qué | Resultado |
|---|---|
| Suites ejecutadas | `validar.py metareglas` sin fallas y `validar.py estandar` sin incumplimientos |
| Verificaciones manuales | Las copias quedaron iguales a las reglas; el ancla de la sección «M10» se conservó |
| Defectos abiertos aceptados | Ninguno |

## 4. Cómo se usa / puntos de entrada  ·  [`13·DOC1`](../../../../../base/13-documentacion/reglas/DOC1-persiste-el-trabajo-de-cada-unidad-completada.md)

Las reglas llegan a cada proyecto con `base/` y las recupera el enganche de reglas en las tareas cambiar-estandar y escribir-documento.

## 5. Decisiones no obvias  ·  [`13·DOC2`](../../../../../base/13-documentacion/reglas/DOC2-documenta-las-decisiones-no-obvias-y-su-porque.md) / [`13·DOC5`](../../../../../base/13-documentacion/reglas/DOC5-registra-como-senal-lo-que-no-se-recupera-del-codigo.md)

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Mientras la base no guarde el estándar, siguen `CHANGELOG.md` y `VERSION` | Sin EP-026 construida no hay dónde registrar; se descartó dejar los archivos ya | S-329 |
| Se conservan los títulos y las anclas de `M10`, `C19` y la sección «M10» | Los citan análisis aprobados que no se reescriben | S-329 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  [`13·DOC9`](../../../../../base/13-documentacion/reglas/DOC9-consulta-el-mapa-de-dependencias-antes-de-planificar.md) / [`13·DOC13`](../../../../../base/13-documentacion/reglas/DOC13-registra-cada-modulo-nuevo-en-el-catalogo-de-modulos.md)

- [x] `base/mapa-de-tareas.md` y `base/reglas-por-tarea/` regenerados.

## 8. Despliegue, si aplica  ·  [`13·DOC4`](../../../../../base/13-documentacion/reglas/DOC4-documenta-lo-que-produccion-necesita.md)

No aplica: las reglas llegan a los proyectos con la próxima actualización del estándar.
