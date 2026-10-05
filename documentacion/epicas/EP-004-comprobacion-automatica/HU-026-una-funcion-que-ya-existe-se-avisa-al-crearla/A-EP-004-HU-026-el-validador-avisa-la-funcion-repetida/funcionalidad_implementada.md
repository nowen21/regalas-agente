# Funcionalidad implementada · Fase `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida` (módulo `proyectos/cimiento/core/validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-004-HU-026-el-validador-avisa-la-funcion-repetida` |
| **Módulo** | `proyectos/cimiento/core/validadores/` |
| **Especificación del módulo** | Los CA de la [HU-026](../HU-026-una-funcion-que-ya-existe-se-avisa-al-crearla.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 1 |
| **HU / CA cubiertas** | HU-026 (CA-01 a CA-05) |
| **Fecha de cierre** | 2026-10-04 |
| **Versión del estándar al cerrar** | 54.1.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

`validar.py repetidas` avisa, sin frenar, la función que hace lo mismo que otra aunque tenga otro nombre; con `--preparados`, solo las nuevas del commit. La separación de funciones quedó una sola vez, en `Funciones`, y la usan este validador y el de `07·Q3`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01 | Programa | `proyectos/cimiento/core/validadores/codigo.py`, `calidad.py` | ✅ | CP-001 |
| CA-02 | Programa | `proyectos/cimiento/core/validadores/repetidas.py` | ✅ | CP-002 |
| CA-03 | Programa | `proyectos/cimiento/core/validadores/repetidas.py` | ✅ | CP-003 |
| CA-04 | Programa | `repetidas.py` y `proyectos/cimiento/core/herramientas/validar.py` | ✅ | CP-004 |
| CA-05 | Programa | `proyectos/cimiento/core/validadores/repetidas.py` | ✅ | CP-005 |

**Faltantes / diferimientos:** sumar el aviso al enganche `pre-commit` del instalador quedó fuera de alcance, como dice el plan.

### 2.2 Plan de trabajo → ejecución

Las 4 tareas del plan quedaron hechas.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python validadores/validar.py repetidas [--raiz <proyecto>] [--preparados]`, parado en el proyecto o pasándole su raíz.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Se compara por trozos de cinco fichas con un índice, no par por par | Par por par tardaba más de diez minutos en agro-system | En el código |
| Un aviso por copia, que nombra la primera | Ocho copias daban veintiocho avisos | En el código |
| Umbral 0,80 | Con 0,90 se perdía `raiz_pedida` (83 %) | En el comentario de `UMBRAL` |

## 6. Deuda técnica y pendientes generados

Ninguno. Las copias que el aviso encuentra hoy en Cimiento son las que el análisis 1 del pendiente 116 junta en otra épica (acuerdo 2).

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `validadores/reglas-validables.md`: `07·Q4` pasa a tener programa.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 54.1.0.
