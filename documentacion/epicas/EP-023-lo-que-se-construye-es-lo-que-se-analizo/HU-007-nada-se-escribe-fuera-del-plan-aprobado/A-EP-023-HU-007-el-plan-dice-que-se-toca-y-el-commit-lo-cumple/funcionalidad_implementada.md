# Funcionalidad implementada · Fase `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple` (módulo `base/`, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-007-el-plan-dice-que-se-toca-y-el-commit-lo-cumple` |
| **Módulo** | `base/`, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Los CA-01, CA-03 y CA-04 de la [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-007 (CA-01, CA-03 y CA-04) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 48.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

El plan aprobado dice quién lo aprobó, cuándo y con qué versión, y su lista de archivos lleva solo rutas exactas. Las reglas que autorizan escribir sin plan lo dicen en una línea «Autoriza escribir», y las del proyecto también pueden. El `pre-commit` rechaza el archivo que el plan de la fase no declara, que no es de la fase y que ninguna regla autoriza.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01: rutas exactas y quién aprobó | Plantilla y validador | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `validadores/flujo.py`, `validadores/plan_vs_hecho.py` | ✅ | CP-001 |
| CA-03: el commit se compara con el plan | Validador y enganche | `validadores/plan_vs_hecho.py`, `validadores/validar.py`, `validadores/instalar.py` | ✅ | CP-002 |
| CA-04: lo que autorizan las reglas, también las del proyecto | Reglas, plantilla y programa | `20·M5`, `plantillas/reglas-proyecto.md`, las diez reglas de la línea, `validadores/autorizado.py` | ✅ | CP-003 |

**Faltantes / diferimientos:** el CA-02 (el freno antes y después de escribir) va en la fase `B`, y la integración continua y el contrato del adaptador en la `C`.

### 2.2 Plan de trabajo → ejecución

Las 8 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase, que nombra la sección 3.5 de su plan de pruebas, y las de los programas que cambió.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python validadores/validar.py plan --preparados` compara lo que entra en el commit con el plan aprobado de la fase que toca; el `pre-commit` que pone el instalador lo corre. `python validadores/validar.py flujo` falla el plan aprobado desde 48.0.0 sin quién o sin fecha, o con filas que no son rutas exactas.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las rutas de la línea van separadas por coma | El punto medio sube las marcas de `00·ID8` en lo que viaja a los proyectos | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `anatomia/mapa-del-sitio.md`: el programa nuevo.
- [x] `base/mapa-de-tareas.md`: regenerado; no cambió, porque no copia la línea nueva.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 48.0.0 con el instalador, que pone el `pre-commit` nuevo.
