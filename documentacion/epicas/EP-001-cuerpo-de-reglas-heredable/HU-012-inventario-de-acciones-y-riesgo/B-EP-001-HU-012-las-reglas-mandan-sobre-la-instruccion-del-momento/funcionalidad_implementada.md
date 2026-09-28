# Funcionalidad implementada · Fase `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-012-las-reglas-mandan-sobre-la-instruccion-del-momento` |
| **Módulo** | Cuerpo de reglas, capítulo 00, núcleo blindado |
| **Especificación del módulo** | La regla de negocio RN-06 de [HU-012](../HU-012-inventario-de-acciones-y-riesgo.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-012 (CA-05) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.0.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Existe la regla blindada `00·N10`, «Una regla escrita manda sobre la instrucción del momento». Cuando lo que pide el usuario choca con una regla escrita, el agente cumple la regla, dice cuál es y no hace lo pedido; la regla se cambia por su procedimiento, no se salta. La precedencia del `CLAUDE.md` de cada proyecto la nombra.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-06 · la regla escrita gana; el agente dice cuál es y no hace lo pedido; la regla se cambia por el capítulo 20 | doc | `base/00-nucleo-blindado.md`, `## N10` | ✅ | CP-001, CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Escribir `N10` en el núcleo | ✅ hecha | `base/00-nucleo-blindado.md`, línea 343 | CP-001 |
| T-02 | Aplicar el checklist y dejarlo en CUMPLE | ✅ hecha | La misma regla, 17 ✅ y 3 N/A | CP-001 |
| T-03 | Nombrar `N10` en la precedencia | ✅ hecha | `plantillas/CLAUDE.md.plantilla`, punto 4 | CP-002 |
| T-04 | Anotar en el recuerdo que subió a regla | ✅ hecha | `historico-chat/memory/reglas-son-decision-del-usuario.md` | CP-003 |
| T-05 | Versión 39.0.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-003 |
| T-06 | Cerrar el pendiente 98 y actualizar HU-012 | ✅ hecha | `pendientes/98-...md`, `pendientes/README.md` y HU-012 | — |

**Correspondencia con el plan:** 6 tareas en el plan, 6 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `validadores/reglas-validables.md`. La fila 18 del checklist exige registrar la regla ahí para dejarlo en CUMPLE, así que es parte de la T-02; el plan no lo nombró en su lista de archivos.

**Esfuerzo real contra estimado:** cerca de 1 h contra 1,7 h del plan.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: `metareglas` y `estandar` sin incumplimientos, `versionado` y `pendientes` sin fallas, `test_la_entrada_del_registro_se_entiende` en OK.
- Verificaciones manuales: ninguna.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Punto de entrada: la regla le llega al agente con el núcleo, y la precedencia del `CLAUDE.md` de cada proyecto la nombra.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La regla va en HU-012 y no en una historia nueva | HU-012 es la historia dueña del núcleo, y todo cambio del capítulo baja por ella. El usuario había pedido una HU nueva; se le dijo y aceptó | En la bitácora de HU-012 y en el pendiente 98 |
| Va en la capa 1 | Decisión del usuario: una regla que manda sobre las demás no puede quedar entre las que un proyecto ajusta | En la fila 3 del checklist de la regla |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Registro de reglas comprobables actualizado.
- [x] Índice de pendientes con el 98 cerrado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: la regla entra con la versión 39.0.0, y los proyectos la reciben al actualizar el estándar.
