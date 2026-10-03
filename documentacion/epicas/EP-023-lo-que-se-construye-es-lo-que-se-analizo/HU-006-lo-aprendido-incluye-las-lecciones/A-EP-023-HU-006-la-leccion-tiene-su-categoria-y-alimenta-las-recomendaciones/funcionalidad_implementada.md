# Funcionalidad implementada · Fase `A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones` (módulo `memoria/`, `plantillas/` y `validadores/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-006-la-leccion-tiene-su-categoria-y-alimenta-las-recomendaciones` |
| **Módulo** | `memoria/`, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Los CA-01 y CA-02 de la [HU-006](../HU-006-lo-aprendido-incluye-las-lecciones.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-006 (CA-01 y CA-02) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 46.0.0 |
| **Commit** | `d5e33a3` |

## 1. Qué se implementó, resumen

El almacén de señales acepta el tipo `leccion`. La tabla de lecciones del análisis enlaza la señal de cada una y dice qué recomendación complementa o crea. El validador lo exige a los análisis aprobados desde la 46.0.0.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01: la lección tiene su categoría y el análisis la enlaza | Programa, plantilla y validador | `memoria/memoria.py`, `memoria/esquema.sql`, `documentacion/senales.md`, `plantillas/analisis.md`, `validadores/analisis.py` | ✅ | CP-001, CP-003 |
| CA-02: las lecciones alimentan las recomendaciones | Plantilla y validador | `plantillas/analisis.md`, `validadores/analisis.py` | ✅ | CP-002, CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): Ninguno.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase, que nombra la sección 3.5 de su plan de pruebas.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python memoria/memoria.py add --tipo leccion ...` guarda la lección; la tabla de lecciones enlaza su `S-NNN` y dice «complementa R-n», «nueva R-n» o «no aplica».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El tipo se llama `leccion`, sin tilde | Los tipos del almacén se escriben sin tilde, como `decision` y `restriccion` | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 46.0.0 con el instalador.
