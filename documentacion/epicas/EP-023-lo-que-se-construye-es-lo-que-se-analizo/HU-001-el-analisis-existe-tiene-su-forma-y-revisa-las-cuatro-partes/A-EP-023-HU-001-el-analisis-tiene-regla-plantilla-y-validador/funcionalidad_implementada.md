# Funcionalidad implementada · Fase `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador` (módulo Cuerpo de reglas, plantillas y validadores)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `A-EP-023-HU-001-el-analisis-tiene-regla-plantilla-y-validador` |
| **Módulo** | Cuerpo de reglas, `plantillas/` y `validadores/` |
| **Especificación del módulo** | Las reglas de negocio RN-01 a RN-06 de la [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-001 (CA-01, CA-02, CA-04, CA-05, CA-06, CA-07, CA-16) |
| **Fecha de cierre** | 2026-10-01 |
| **Versión del estándar al cerrar** | 40.0.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

El análisis quedó en el estándar como eslabón de la cadena: `02·F0` lo pide en los tres puntos de reparto y `02·F23` antes de que un pendiente baje a la HU. `13·DOC8` quedó derogada y la reemplazan `13·DOC24` y `13·DOC25`. Hay plantilla del análisis y un validador que no deja pasar un análisis aprobado sin sus cuatro partes.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-01: un análisis en cada punto donde algo se reparte | Regla | `base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md` | ✅ | CP-001 |
| RN-02: una sección para Cimiento, el proyecto, lo aprendido y el entorno | Validador | `validadores/analisis.py` | ✅ | CP-005 |
| RN-03: el principal se reescribe; el individual no | Regla | `base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md` y `DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md` | ✅ | CP-003 |
| RN-04: el análisis arranca donde se dice «Analicemos: el pendiente N» | Herramienta | Fase `B` | N/A: va en la fase `B` | Ninguna |
| RN-05: el orden al cerrar | Herramienta | Fase `B` | N/A: va en la fase `B` | Ninguna |
| RN-06: un solo análisis abierto | Herramienta | Fase `B` | N/A: va en la fase `B` | Ninguna |

**Faltantes / diferimientos:** RN-04 a RN-06 son de la herramienta y van en la fase `B`.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | El análisis en `F0`, acortada y vuelta a sellar | ✅ hecha | `F0-recorre-la-cadena-completa-sin-saltar-eslabones.md` | CP-001 |
| T-02 | El análisis en `F23`, acortada y vuelta a sellar | ✅ hecha | `F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` | CP-002 |
| T-03 | `DOC24` y `DOC25`, en el índice y en las validables | ✅ hecha | `base/13-documentacion/reglas/`, `base/13-documentacion/base.md`, `validadores/reglas-validables.md` | CP-003 |
| T-04 | `DOC8` derogada y sus citas cambiadas | ✅ hecha | `DOC8`, `estructura-base.md`, `retrodocumentacion.md`, `glosario.md`, `07-plan-trabajo.md`, `cierre-analisis.md` | CP-003 |
| T-05 | La plantilla del análisis, registrada | ✅ hecha | `plantillas/analisis.md`, `validadores/plantillas.py` | CP-004 |
| T-06 | El validador, su subcomando y su línea en el mapa del sitio | ✅ hecha | `validadores/analisis.py`, `validadores/validar.py`, `anatomia/mapa-del-sitio.md` | CP-005 |
| T-07 | Las pruebas del validador | ✅ hecha | `validadores/tests/test_analisis.py` | CP-005 |
| T-08 | Reglas por tarea, `VERSION` y CHANGELOG | ✅ hecha | `base/reglas-por-tarea/`, `base/mapa-de-tareas.md`, `VERSION`, `CHANGELOG.md` | CP-006 |

**Correspondencia con el plan:** 8 tareas en el plan, 8 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno.

**Esfuerzo real contra estimado:** no se midió. El plan estimaba 7,4 horas.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas: `test_analisis.py` (6 de 6), `test_encuadre_de_la_plantilla.py` y `test_plantillas_origen_regla.py` (14 de 14); `validar.py metareglas`, `estandar`, `tareas`, `analisis` y `sitio` sin fallas.
- Verificaciones manuales: el mapa del sitio nombra el validador; ningún archivo cambiado sumó marcas.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- `python validadores/validar.py analisis`: revisa los análisis aprobados del repositorio.
- `plantillas/analisis.md`: el molde de todo análisis nuevo.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| `DOC8` se reemplaza con dos reglas | Una sola regla con las dos exigencias no pasaba la fila 9 del checklist (análisis 5) | Por escribir |
| El validador solo mira los análisis aprobados | El abierto todavía se está llenando; exigirle las secciones sería una alarma falsa | Por escribir |
| `reglas-antes-de-la-accion.md` no se tocó | Es una foto fechada del 2026-09-16, no una cita viva de `DOC8` | Por escribir |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| El plan de pruebas nombraba tres subcomandos equivocados | No previsto | La lección queda en el estado de la fase |
| `validadores/analisis.py` quedó fuera de `anatomia/que-esta-amarrado-a-la-herramienta.md`, y `validar.py amarre` fallaba; esta fase no declaró ese mapa | No previsto | Corregido en la fase `B` (DEF-02), por decisión del usuario el 2026-10-02 |

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa del sitio: `analisis.py` agregado.
- [x] Índice del capítulo 13: `DOC24` y `DOC25`, y `DOC8` derogada.
- [x] Mapa de tareas y reglas por tarea, vueltos a escribir.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Llega a los proyectos que heredan con la versión 40.0.0, por el instalador.
