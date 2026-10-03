# Funcionalidad implementada · Fase `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo` (módulo `plantillas/`, `validadores/` y `base/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-suyo` |
| **Módulo** | `plantillas/`, `validadores/` y `base/` |
| **Especificación del módulo** | Los CA-01 a CA-08 de la [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-003 (CA-01 a CA-08) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 45.0.0 |
| **Commit** | `d11f0ea` |

## 1. Qué se implementó, resumen

El hallazgo trae qué pasó, por qué importa y el enlace a su pendiente; el pendiente trae de dónde sale, el problema y por qué importa. Su estado y por dónde se retoma se calculan siguiendo los enlaces. Cada pendiente nuevo vive en una carpeta `pendientes/` de su dueño, la numeración es una sola y un programa arma el índice en `documentacion/pendientes.md`. El 103 pasó a `EP-023/pendientes/`.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-01, CA-07 y CA-08: dónde vive el pendiente y `pendientes/` como historia | Regla, validador, programa e instalador | `base/20-meta-reglas/base.md`, `02·F13`, `validadores/fases.py`, `validadores/flujo.py`, `validadores/pendientes.py`, `validadores/andamio.py`, `validadores/instalar.py` | ✅ | CP-001, CP-007, CP-008 |
| CA-02: las plantillas con solo sus campos | Plantilla | `plantillas/pendiente.md`, `plantillas/pendiente-de-seguimiento.md`, `plantillas/pendiente-reportado.md`, `plantillas/sesion.md` | ✅ | CP-002 |
| CA-03 a CA-05: los validadores, el cierre calculado y el hallazgo de dos campos | Validador y regla | `validadores/pendientes.py`, `validadores/resumen.py`, `13·DOC22` | ✅ | CP-003 a CP-005 |
| CA-06: sin «Proyecto de origen» | Regla y plantilla | `02·F24`, las plantillas del pendiente | ✅ | CP-006 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 16 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `validadores/flujo.py`, que también tomaba `pendientes/` como una HU; se ajustó dentro de la T-11.

**Esfuerzo real contra estimado:** no se midió.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Pruebas: las de la fase, que nombra la sección 3.5 de su plan de pruebas.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

`python validadores/andamio.py pendiente <slug> [--hu <épica>/<HU>]` crea el pendiente como carpeta en su dueño. `python validadores/validar.py pendientes --indice` escribe el índice. El estado del hallazgo y del pendiente no se escribe: lo calculan `resumen.py` y `pendientes.py`.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El 103 pasó a `EP-023/pendientes/` | Su dueño es EP-023 y el análisis 8 pide `pendientes/` y nada más; los pendientes viejos no se tocan y pasan cuando se vayan a trabajar | Por escribir |

## 6. Deuda técnica y pendientes generados

| Deuda | Origen | Por qué |
|---|---|---|
| `cerrar.py` sigue usando «Proyecto de origen» para avisar a los proyectos de los pendientes viejos | Diferido por el plan | El plan dejó `cerrar.py` fuera de alcance |

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 45.0.0 con el instalador.
