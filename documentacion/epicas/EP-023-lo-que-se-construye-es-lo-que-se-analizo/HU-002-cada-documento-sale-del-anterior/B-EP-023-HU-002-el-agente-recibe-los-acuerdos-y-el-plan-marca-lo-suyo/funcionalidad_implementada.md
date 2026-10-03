# Funcionalidad implementada · Fase `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo` (módulo `validadores/`, `adaptadores/claude-code/` y `plantillas/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-002-el-agente-recibe-los-acuerdos-y-el-plan-marca-lo-suyo` |
| **Módulo** | `validadores/`, `adaptadores/claude-code/` y `plantillas/` |
| **Especificación del módulo** | Los CA-04 y CA-05 de la [HU-002](../HU-002-cada-documento-sale-del-anterior.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-002 (CA-04 y CA-05) |
| **Fecha de cierre** | 2026-10-03 |
| **Versión del estándar al cerrar** | 50.0.0 |
| **Commit** | Por hacer |

## 1. Qué se implementó, resumen

Con cada mensaje, el agente recibe los acuerdos de los que sale lo que trabaja: los de la fase en curso, siguiendo el «Sale de» de sus criterios, y los de los análisis aprobados del pendiente del análisis prendido. Cada decisión del plan dice de qué acuerdo sale o que es propuesta del agente, y la revisión de origen detiene la que no dice ninguna de las dos.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-04: los acuerdos llegan con cada mensaje | Programa, enganche e instalador | `validadores/acuerdos.py`, `adaptadores/claude-code/hook_acuerdos.py`, `validadores/instalar.py` | ✅ | CP-001, CP-002 |
| CA-05: la decisión del plan dice de dónde sale | Plantilla y validador | `plantillas/ciclo-vida-proyectos/07-plan-trabajo.md`, `validadores/origen.py` | ✅ | CP-003 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 6 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

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

El enganche corre solo con cada mensaje, una vez que el instalador lo registra. `python validadores/validar.py origen` revisa las decisiones de los planes aprobados desde 50.0.0.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| La fase vieja cerrada se reconoce por su cierre y por no traer la aprobación con versión | 105 de 240 fases cerraron antes de que se anotara el commit; sin esto quedarían en curso para siempre | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [x] `anatomia/mapa-del-sitio.md`: el programa nuevo.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 50.0.0 con el instalador, que registra el enganche nuevo.
