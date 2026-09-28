# Funcionalidad implementada · Fase `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` (módulo Automatismos)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` |
| **Módulo** | Automatismos: `validadores/andamio.py`, `validadores/estacion_commit.py` y la regla `02·F23` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-06 de [HU-022](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-022 de EP-005 (CA-01 a CA-07) |
| **Fecha de cierre** | 2026-09-27 |
| **Versión del estándar al cerrar** | 38.3.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

`andamio.py pendiente` anota un pendiente sin historia, con la ficha en «Por asignar», y un `--hu` que no existe sigue siendo un error. `02·F23` escribe el orden hallazgo, pendiente, HU y fase. El enganche `post-commit` ya no marca como commiteada una fase recién abierta.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01 · el pendiente se anota antes que su HU | servicio | `validadores/andamio.py`, `crear_pendiente` y `--hu` | ✅ | CP-001 |
| RN-02 · toda HU es hija de una épica | doc | `base/02-flujo-de-trabajo/reglas/F23-…md` | ✅ | CP-004 |
| RN-03 · «Por asignar» mientras no esté aprobado | servicio y doc | `andamio.py`, `pendientes/README.md`, `plantillas/pendiente.md` | ✅ | CP-001, CP-005 |
| RN-04 · la herramienta hace cumplir el mismo orden que la regla | servicio | `andamio.py` | ✅ | CP-001, CP-003 |
| RN-05 · el orden escrito en una regla | doc | `F23` | ✅ | CP-004 |
| RN-06 · la estación 12 solo en una fase con el cierre escrito | servicio | `validadores/estacion_commit.py`, `cierre_escrito` | ✅ | CP-008 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | `--hu` opcional | ✅ hecha | `validadores/andamio.py` | CP-001 |
| T-02 | Sin historia, «Por asignar» y sin tocar el mapa | ✅ hecha | `crear_pendiente` | CP-001 |
| T-03 | Prueba del modo sin historia | ✅ hecha | `test_el_andamio_levanta_la_historia_y_el_pendiente.py` | CP-001 |
| T-04 | Correr las pruebas que ya existen | ✅ hecha | La misma suite | CP-002 |
| T-05 | Prueba del `--hu` inexistente | ✅ hecha | La misma suite | CP-003 |
| T-06 | Precisar `F23` | ✅ hecha | El archivo de `F23` | CP-004 |
| T-07 | Volver a aplicar su checklist | ✅ hecha | El mismo archivo | CP-004 |
| T-08 | La frase del índice | ✅ hecha | `pendientes/README.md` | CP-005 |
| T-09 | La nota de la plantilla | ✅ hecha | `plantillas/pendiente.md` | CP-005 |
| T-10 | Correr la validación de pendientes | ✅ hecha | `validar.py pendientes` | CP-006 |
| T-11 | Versión 38.3.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-007 |
| T-12 | Cerrar el pendiente 97 y actualizar HU-022 | ✅ hecha | `pendientes/97-…md`, `pendientes/README.md` y HU-022 | — |
| T-13 | `marcar_las_fases` exige el cierre escrito | ✅ hecha | `validadores/estacion_commit.py` | CP-008 |
| T-14 | Prueba de la fase con el cierre en molde | ✅ hecha | `validadores/pruebas.py` | CP-008 |

**Correspondencia con el plan:** 14 tareas en el plan, 14 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** cerca de 2 h reales contra 3,9 h del plan.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: las tres `test_el_andamio_*.py` en OK (12 pruebas en la principal), `ElHashDelCommitSeAnotaSolo` con 17 pruebas en OK, y `metareglas`, `estandar`, `pendientes` y `ejecutable` sin fallas.
- Verificaciones manuales:
  - Las pruebas no crearon archivos en el repositorio real.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Punto de entrada: `python validadores/andamio.py pendiente <slug>`, con `--hu <épica>/<HU>` si la historia ya existe.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Un pendiente sin historia no entra al mapa | El mapa cruza historias con pendientes; se descartó una fila «Por asignar» que no cruza nada | En el plan §2.6 |
| El cierre se compara contra el molde del proyecto, y si no hay, contra el del estándar | En un proyecto que hereda, las plantillas viven en el estándar; sin molde con qué comparar no se afirma y se marca como antes | En el docstring de `cierre_escrito` |
| El enganche `post-commit` entra en esta fase | El usuario pidió resolverlo en la misma fase en vez de anotarlo como pendiente | En el `estado-fase.md` §2 |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Índice de pendientes con el 97 cerrado y la frase sobre «Por asignar».
- [x] Nota de la plantilla del pendiente.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: el cambio entra con la versión 38.3.0, y los proyectos lo reciben al actualizar el estándar.
