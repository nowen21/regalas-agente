# Funcionalidad implementada · Fase `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu` (módulo `plantillas/`, `validadores/`, `analisis/` y `base/13-documentacion/`)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu` |
| **Módulo** | `plantillas/`, `validadores/`, `analisis/` y `base/13-documentacion/` |
| **Especificación del módulo** | Los CA-17 a CA-26 de la [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-001 (CA-17 a CA-26) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 44.0.0 |
| **Commit** | `79356eb` |

## 1. Qué se implementó, resumen

Todo análisis nuevo consulta las recomendaciones, considera dónde más puede pasar lo mismo, ordena sus HU por su dependencia y dice lo que suma al análisis principal. Aprobar un análisis pone la versión en la marca, no aprueba sin filas ni sin «Lo que aporta», y pasa lo que suma al principal. El análisis principal es la redacción que forman los aportes de los diez análisis.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| CA-17 a CA-19: «Dónde más puede pasar», la tabla de HU con su orden y las recomendaciones | Plantilla y validador | `plantillas/analisis.md`, `plantillas/recomendaciones-del-analisis.md`, `plantillas/ciclo-vida-proyectos/03-epica.md`, `validadores/analisis.py` | ✅ | CP-001 a CP-003 |
| CA-20 y CA-24: el análisis principal y lo que suma cada análisis | Documento, programa y validador | `analisis/proyecto-2026-10-02-analisis-principal.md`, `validadores/analisis_en_curso.py`, `validadores/analisis.py` | ✅ | CP-004, CP-009 |
| CA-21: medir la respuesta antes de entregarla | Documento | `plantillas/recomendaciones-del-analisis.md`, R-17 | ✅ | CP-005 |
| CA-22: lo nuevo no reabre lo aprobado | Validador | `validadores/analisis.py`, `validadores/analisis_en_curso.py` | ✅ | CP-006 |
| CA-23: `DOC25` anota todo análisis aprobado | Regla | `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md` | ✅ | CP-008 |
| CA-25 y CA-26: sin filas o sin «Lo que aporta» no se aprueba | Programa | `validadores/analisis_en_curso.py`, `adaptadores/claude-code/hook_analisis.py` | ✅ | CP-010, CP-011 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

Las 21 tareas del plan quedaron hechas; cada una está en la tabla del plan con su archivo y su caso de prueba, y el [`resultado_pruebas.md`](resultado_pruebas.md) dice qué salió de cada caso.

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

Al aprobar un análisis con «Apruebo el análisis», el programa revisa que tenga filas en «Lo que se tiene que hacer» y la sección «Lo que aporta», y pasa lo que suma al análisis principal. `python validadores/validar.py analisis` revisa lo que exige la 44.0.0 y avisa del análisis que no está en la «Lista de análisis».

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| El principal de su alcance se busca subiendo de carpeta | Cubre el módulo con principal propio sin pedir otro dato; se descartó pedir el alcance en cada análisis | Por escribir |

## 6. Deuda técnica y pendientes generados

Ninguna. Salió el hallazgo H-12 (las pruebas de la plataforma escriben en el registro real de auditoría), anotado en el resumen de la sesión.

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `CHANGELOG.md` y `VERSION`.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Cada proyecto lo recibe al adoptar la 44.0.0 con el instalador.
