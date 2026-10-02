# Funcionalidad implementada · Fase `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis` (módulo `validadores/` y el adaptador)   ·   `[CAPA 3]`

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (identificador · `02·F12.6`) | `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis` |
| **Módulo** | `validadores/` y el adaptador de la herramienta |
| **Especificación del módulo** | Las reglas de negocio RN-04 a RN-06 de la [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de trabajo** | [`plan_trabajo.md`](plan_trabajo.md) |
| **HU / CA cubiertas** | HU-001 (CA-03, CA-09, CA-10, CA-11, CA-12, CA-13, CA-14, CA-15) |
| **Fecha de cierre** | 2026-10-02 |
| **Versión del estándar al cerrar** | 40.1.0 |
| **Commit** | Se completa al commitear |

## 1. Qué se implementó, resumen

La conversación pasa sola al análisis prendido. Se prende con «Analicemos: el pendiente N», se pausa con «Pare» y se apaga con «Apruebo el análisis», y cada mensaje dice a qué análisis está entrando. No se prende el de otro pendiente mientras uno siga abierto. El instalador lo lleva a cada proyecto.

## 2. Trazabilidad  ·  `13·DOC11`

### 2.1 Especificación → implementación

| Ítem de la especificación | Categoría | Ubicación (archivo real) | Estado | Evidencia |
|---|---|---|---|---|
| RN-04: el análisis arranca donde se dice «Analicemos: el pendiente N» | Servicio | `validadores/analisis_en_curso.py` (`prender`) | ✅ | CP-004 |
| RN-05: primero los originales, después la aprobación y por último el apagado | Servicio | `validadores/analisis_en_curso.py` (`aprobar`, `pasar`) | ✅ | CP-004 |
| RN-06: un solo análisis abierto | Servicio | `validadores/analisis_en_curso.py` (`abiertos`) | ✅ | CP-005 |

**Faltantes / diferimientos:** ninguno.

### 2.2 Plan de trabajo → ejecución

| Tarea | Qué era | Estado | Dónde quedó | Evidencia |
|---|---|---|---|---|
| T-01 | Estado y `pasar` | ✅ hecha | `validadores/analisis_en_curso.py` | CP-001, CP-002 |
| T-02 | Coma en los encabezados y sin etiquetas | ✅ hecha | `validadores/analisis_en_curso.py` | CP-003 |
| T-03 | Prender, pausar y aprobar | ✅ hecha | `validadores/analisis_en_curso.py` | CP-004 |
| T-04 | Análisis abiertos | ✅ hecha | `validadores/analisis_en_curso.py` | CP-005 |
| T-05 | El aviso y el enganche | ✅ hecha | `adaptadores/claude-code/hook_analisis.py` | CP-006 |
| T-06 | Instalador, `.claude/settings.json` y mapas | ✅ hecha | `validadores/instalar.py`, `.claude/settings.json`, `anatomia/` | CP-007 |
| T-07 | Las pruebas | ✅ hecha | `validadores/tests/test_analisis_en_curso.py` | 6 de 6 |
| T-08 | Versión y CHANGELOG | ✅ hecha | `VERSION`, `CHANGELOG.md` | `metareglas` sin fallas |

**Correspondencia con el plan:** 8 tareas en el plan, 8 acá.

**Tareas que no se hicieron:** ninguna.

**Archivos tocados que el plan no declaraba** (`02·F8`): ninguno. En `anatomia/que-esta-amarrado-a-la-herramienta.md`, que sí está declarado, se agregó también la fila de `validadores/analisis.py`, de la fase `A`; lo autorizó el usuario el 2026-10-02.

**Esfuerzo real contra estimado:** no se midió. El plan estimaba 9,8 horas.

## 3. Qué se probó  ·  `08` / `02·F5`

| Campo | Valor |
|---|---|
| **Fuente** | [`resultado_pruebas.md`](resultado_pruebas.md) |
| **Veredicto** | Cumple |

- Suites ejecutadas: `test_analisis_en_curso.py` (6 de 6), `test_analisis.py` (6 de 6) y las cuatro que dependen del instalador (50 de 50); `validar.py metareglas`, `amarre`, `estandar` y `analisis` sin fallas.
- Verificaciones manuales: el aviso llega en la sesión real.
- Defectos abiertos que se aceptaron: ninguno.

## 4. Cómo se usa / puntos de entrada  ·  `13·DOC1`

- «Analicemos: el pendiente N» prende el análisis siguiente de ese pendiente.
- «Pare» lo pausa; volver a decir «Analicemos: el pendiente N» lo reanuda.
- «Apruebo el análisis» pone la marca y lo apaga al terminar la respuesta.

## 5. Decisiones no obvias  ·  `13·DOC2` / `13·DOC5`

| Decisión | Por qué (y qué se descartó) | Señal registrada |
|---|---|---|
| Un análisis sigue abierto mientras alguna HU de su «Pasó a» no esté terminada | Es como se sabe que su plan se cumplió, con enlaces que ya existen (análisis 3, punto 4) | Por escribir |
| En el estándar las entradas se cambiaron a mano y no con el instalador | El instalador también habría tocado la versión adoptada y el `CLAUDE.md`, que el plan no declara | Por escribir |
| Las palabras copiadas del usuario y del agente no se corrigen | La conversación no se edita; `00·ID8` se cumple en lo que escribe la herramienta | Por escribir |

## 6. Deuda técnica y pendientes generados

| Descripción | Origen | Destino |
|---|---|---|
| `historico-chat/scripts/2026-09-30/pasar_conversacion.py` sigue en su carpeta, sin registrar | Diferido por el plan | Se conserva como guion de apoyo (`04·S18`) |

## 7. Índices y mapas actualizados  ·  `13·DOC9` / `13·DOC13`

- [x] Mapa del sitio: el enganche y el módulo.
- [x] Mapa del amarre: el enganche, el módulo y `analisis.py`.
- [ ] Mapa de dependencias: N/A, el estándar no lo mantiene.

## 8. Despliegue, si aplica  ·  `13·DOC4`

Llega a los proyectos que heredan con la versión 40.1.0, al volver a correr el instalador.
