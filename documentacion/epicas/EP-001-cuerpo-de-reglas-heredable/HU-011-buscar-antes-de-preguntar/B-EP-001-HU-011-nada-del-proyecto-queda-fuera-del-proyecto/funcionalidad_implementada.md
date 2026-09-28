# Funcionalidad implementada · Fase `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto` (módulo Cuerpo de reglas)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-001-HU-011-nada-del-proyecto-queda-fuera-del-proyecto` |
| **Módulo** | Cuerpo de reglas, capítulo 01, conducta |
| **Especificación del módulo** | La regla de negocio RN-06 de [HU-011](../HU-011-buscar-antes-de-preguntar.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-011 (CA-04) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.1.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Existe la regla `01·C29`, «Guarda dentro del repositorio todo lo del agente y del proyecto». A su contenido se llega por un enlace, y lo que la herramienta guarde afuera se corrige en su origen, no se lee de allá. `01·C19` la extiende: la memoria es un caso del principio. `04·S9` no cambia; la regla nueva la enlaza.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-06 · todo lo del agente y del proyecto en el repositorio, con enlace; lo guardado afuera se corrige en su origen | doc | `base/01-conducta.md`, `## C29` | ✅ | CP-001, CP-002 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Escribir `C29` | ✅ hecha | `base/01-conducta.md`, línea 939 | CP-001 |
| T-02 | Checklist de `C29` y su registro | ✅ hecha | La misma regla y `validadores/reglas-validables.md` | CP-001 |
| T-03 | `C19` extiende `C29`, con su checklist vuelto a aplicar | ✅ hecha | `base/01-conducta.md`, `## C19`, 314 caracteres | CP-002 |
| T-04 | Anotar en el recuerdo que subió a regla | ✅ hecha | `historico-chat/memory/nada-del-proyecto-queda-en-la-herramienta.md` | CP-003 |
| T-05 | Versión 39.1.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-003 |
| T-06 | Cerrar el pendiente 99 y actualizar HU-011 | ✅ hecha | `pendientes/99-...md`, `pendientes/README.md` y HU-011 | — |

**Correspondencia con el plan:** 6 tareas en el plan, 6 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** cerca de 1 h contra 2 h del plan.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: `metareglas` y `estandar` sin incumplimientos, `versionado` y `pendientes` sin fallas, `test_la_entrada_del_registro_se_entiende` en OK.
- Verificaciones manuales: ninguna.
- Defectos abiertos que se aceptaron: ninguno. Los tres que salieron se corrigieron en la fase.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Punto de entrada: la regla le llega al agente con el capítulo 01 de `base/`.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La regla va en HU-011 y no en una historia nueva | HU-011 es la historia dueña del capítulo 01, y todo cambio del capítulo baja por ella | En la bitácora de HU-011 y en el pendiente 99 |
| `S9` no se cambió | Su capítulo tiene historia dueña, HU-017. La regla nueva la enlaza y resuelve en su propio texto el choque con «Leer fuera sí» | En la fila 17 del checklist de `C29` |
| La línea de quién la hace cumplir va con la forma exacta del validador | `metareglas.py` solo la saca del cuerpo si empieza con «Nadie la hace cumplir:»; con otra forma cuenta para la fila 10 | En DEF-02 del resultado de pruebas |

## 6. Deuda técnica y pendientes generados

Ninguno.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Registro de reglas comprobables actualizado.
- [x] Índice de pendientes con el 99 cerrado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: la regla entra con la versión 39.1.0, y los proyectos la reciben al actualizar el estándar.
