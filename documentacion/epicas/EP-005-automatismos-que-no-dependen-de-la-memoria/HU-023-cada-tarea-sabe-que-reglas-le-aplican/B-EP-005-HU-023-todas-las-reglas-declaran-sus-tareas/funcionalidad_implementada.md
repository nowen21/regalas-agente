# Funcionalidad implementada · Fase `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` (módulo Cuerpo de reglas y validadores)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-005-HU-023-todas-las-reglas-declaran-sus-tareas` |
| **Módulo** | Cuerpo de reglas, `validadores/` y el adaptador |
| **Especificación del módulo** | Las reglas de negocio RN-04 a RN-06 de [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Plan de trabajo** | [plan_trabajo.md](plan_trabajo.md), versión 2 |
| **HU / CA cubiertas** | HU-023 (CA-04, CA-05, CA-06, CA-07) |
| **Fecha de cierre** | 2026-09-28 |
| **Versión del estándar al cerrar** | 39.3.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

Las 252 reglas vigentes dicen a qué tareas aplican, y el mapa las junta. Con cada mensaje del usuario, el recuperador reconoce las tareas que el mensaje pide y le entrega al agente sus reglas: completas mientras caben, nombradas las que no, y siempre las de pedido y respuesta. El recuperador quedó conectado en el estándar. Un validador exige la línea de tareas antes de cada publicación, y el del amarre ya no da por clasificado lo que solo se nombra.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-04 · el validador falla con lo que no cuadra y corre solo antes de publicar | código | `validadores/mapa_tareas.py` (`validar`), `validadores/validar.py` (`tareas`), `validadores/instalar.py` y `.githooks/pre-push` | ✅ | CP-001, CP-002 |
| RN-05 · el amarre clasifica solo por tabla o lista de nombres, y todo programa queda clasificado | código | `validadores/amarre.py` y `anatomia/que-esta-amarrado-a-la-herramienta.md` | ✅ | CP-003 |
| RN-06 · el recuperador trae las reglas de las tareas del mensaje, y siempre las de pedido y respuesta, sin excluir capítulos | código | `validadores/recuperar.py`, `base/tareas.md` y `.claude/settings.json` | ✅ | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | La función que reporta lo que no cuadra | ✅ hecha | `validadores/mapa_tareas.py` | CP-001 |
| T-02 | El subcomando `tareas` | ✅ hecha | `validadores/validar.py` | CP-001 |
| T-03 | `tareas` en el `pre-push` | ✅ hecha | `validadores/instalar.py` y `.githooks/pre-push` | CP-001 |
| T-04 | Las pruebas del validador | ✅ hecha | 7 pruebas nuevas | CP-001 |
| T-05 | Decidir las tareas de las 242 reglas | ✅ hecha | `historico-chat/scripts/2026-09-28/clasificacion-de-tareas.tsv` | CP-002 |
| T-06 | Poner las 242 líneas | ✅ hecha | 99 archivos de `base/` | CP-002 |
| T-07 | Volver a escribir el mapa y validar | ✅ hecha | `base/mapa-de-tareas.md` | CP-002 |
| T-08 | Corregir `amarre.py` | ✅ hecha | `validadores/amarre.py` | CP-003 |
| T-09 | Sus pruebas | ✅ hecha | 2 nuevas y 1 corregida | CP-003 |
| T-10 | Clasificar `hook_reglas.py` y `recuperar.py` | ✅ hecha | El mapa del amarre | CP-003 |
| T-11 | Versión 39.3.0 | ✅ hecha | `CHANGELOG.md` y `VERSION` | CP-004 |
| T-12 | Cerrar la HU, el pendiente y los hallazgos | ✅ hecha | HU-023, el pendiente 100 y el resumen de la sesión | — |
| T-13 | La columna de palabras de cada tarea | ✅ hecha | `base/tareas.md` y `mapa_tareas.py` (`palabras`, `siempre`, `reglas_por_tarea`) | CP-005 |
| T-14 | El recuperador por tareas | ✅ hecha | `validadores/recuperar.py` | CP-005 |
| T-15 | Los casos del recuperador | ✅ hecha | `validadores/pruebas.py`, 19 casos | CP-005 |
| T-16 | Conectar el enganche en el estándar | ✅ hecha | `.claude/settings.json` | CP-005 |

**Correspondencia con el plan:** 16 tareas en el plan, 16 aquí.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): `historico-chat/scripts/README.md`, el índice de los guiones, al que se le sumó el día. El plan declaraba la carpeta del día y su `README.md`, no el índice de arriba.

**Esfuerzo real contra estimado:** cerca de 5 h contra 13 h del plan. La clasificación de las reglas tomó menos de lo previsto porque se leyeron en una sola lista.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [resultado_pruebas.md](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas y resultado: `tareas`, `metareglas`, `estandar`, `ejecutable` y `amarre` sin incumplimientos; `versionado` sin fallas; 191 pruebas de los módulos que la fase toca o que dependen de lo tocado, y 21 casos del recuperador, en OK.
- Verificaciones manuales: la ubicación de las líneas en dos reglas, y el tamaño de lo que inyecta el enganche real.
- Defectos abiertos que se aceptaron: ninguno. Salieron seis y se corrigieron en la fase.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- Con cada mensaje, el enganche `hook_reglas.py` llama al recuperador y le pasa al agente las reglas.
- Una regla nueva lleva su línea `**Aplica a:**` con tareas de `base/tareas.md`, y después se corre `python validadores/mapa_tareas.py`. Si no, `python validadores/validar.py tareas` falla, y el `pre-push` no deja publicar.
- Permisos o datos base sembrados: no aplica.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Las reglas de todo mensaje llegan por su título, y las de la tarea del mensaje completas | Completas, las de todo mensaje pesan 19,7 KB, el doble del tope: con todas completas no entraría ninguna otra | En el comentario de `recuperar.py` y en el CP-005 |
| El tope del recuperador es 10 KB menos 1,5 KB | La herramienta corta lo que pase de 10 KB en total, y el enganche suma su recordatorio y la medición | En el comentario de `TOPE` |
| «regla», «reglas» y otras palabras que están en todas partes no cuentan para el orden | Ponían delante reglas del capítulo 20 en un pedido de redacción | En el comentario de `_GENERICAS` |
| El recordatorio fijo de `hook_reglas.py` no se tocó | Estaba fuera del alcance del plan; repite los títulos de seis reglas de todo mensaje | Queda en la deuda de la sección 6 |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino (fase futura / ticket / `pendientes/`) |
|---|---|---|
| El recordatorio fijo de `hook_reglas.py` repite los títulos que ya trae el bloque de todo mensaje, y ocupa 785 bytes que podrían dejar entrar completa otra regla | CP-005, paso 2 | Ninguno: se le muestra al usuario en el reporte de cierre para que decida |

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] `base/mapa-de-tareas.md`, escrito por el programa.
- [x] El mapa del amarre, con las tres piezas.
- [x] El índice de los guiones, con el día.
- [x] Índice de pendientes con el 100 cerrado.

## 8. Despliegue, si aplica  ·  `13·DOC4`

No aplica: entra con la versión 39.3.0, y los proyectos lo reciben al actualizar el estándar.
