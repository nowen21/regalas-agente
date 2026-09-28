# Plan de Pruebas · Fase `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice cómo se comprueba que lo construido hace lo que la HU pidió: con qué casos, con qué datos, en qué ambiente y qué resultado se espera de cada paso. Su exigencia central es que ningún criterio de aceptación quede sin al menos un caso, para que nadie pueda dar por probado lo que nunca se probó. Se aprueba antes de correr la primera prueba y no se modifica al ejecutar: lo que pasó al correrlas va en el `resultado_pruebas.md` de la misma fase, para no perder la línea base aprobada. La lista de tareas vive en el `plan_trabajo` de esta misma fase.

| Campo | Valor |
|---|---|
| **Código** | PP-022-EP005 |
| **Versión** | 1.0 |
| **Alcance del plan** | HU-022 de EP-005 |
| **Fecha** | 2026-09-27 |
| **Elaborado por** | El agente |
| **Revisado por** | El usuario |
| **Aprobado por** | El usuario |
| **Estado** | Borrador |

## 3. Estrategia de pruebas

Las pruebas automáticas corren sobre copias temporales del repositorio, como las que ya existen para el andamio y el enganche: nunca crean archivos en el repositorio real. La regla `F23` y la frase del índice se leen.

| Nivel | Objetivo | Responsable | Ambiente | Automatizado |
|---|---|---|---|---|
| Unitarias | `crear_pendiente` con y sin historia; `marcar_las_fases` con el cierre en molde | El agente | Copia temporal | Sí |
| Integración | El enganche `post-commit` sobre un repositorio de git real | El agente | Repositorio temporal | Sí |
| Aceptación | Que `F23` y el índice digan el orden | El usuario | Local | No |
| Regresión | Las pruebas del andamio y de la estación 12 que ya existen | El agente | Copia temporal | Sí |

Se corren solo las suites que la fase toca (`02·F5`): las tres `test_el_andamio_*.py`, la clase `ElHashDelCommitSeAnotaSolo` de `pruebas.py`, y `validar.py metareglas`, `estandar` y `pendientes`.

## 5. Matriz de trazabilidad

| HU | CA | Caso(s) de prueba | Tipo | Prioridad | Automatizado | Estado |
|---|---|---|---|---|:--:|---|
| HU-022 | [CA-01](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-01--un-pendiente-se-anota-sin-historia) | [CP-001](#cp-001--un-pendiente-nace-sin-historia) | Funcional | Crítica | Sí | ☐ |
| HU-022 | [CA-02](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-02--con-historia-sigue-como-hoy) | [CP-002](#cp-002--con-historia-sigue-como-hoy) | Regresión | Crítica | Sí | ☐ |
| HU-022 | [CA-03](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-03--una-historia-que-no-existe-sigue-siendo-un-error) | [CP-003](#cp-003--un-hu-que-no-existe-sigue-fallando) | Funcional, error | Alta | Sí | ☐ |
| HU-022 | [CA-04](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-04--el-orden-queda-escrito-en-la-regla) | [CP-004](#cp-004--f23-nombra-el-orden) | Funcional | Alta | Parcial | ☐ |
| HU-022 | [CA-05](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-05--el-índice-dice-cuándo-vale-por-asignar) | [CP-005](#cp-005--el-índice-y-la-plantilla-dicen-cuándo-vale-por-asignar) | Funcional | Media | No | ☐ |
| HU-022 | [CA-06](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-06--un-pendiente-por-asignar-no-reprueba-la-validación) | [CP-006](#cp-006--por-asignar-no-reprueba-la-validación) | Funcional, caso borde | Media | Sí | ☐ |
| HU-022 | RNF-01 | [CP-007](#cp-007--el-cambio-queda-versionado) | Trazabilidad | Media | Parcial | ☐ |
| HU-022 | RNF-02 | [CP-002](#cp-002--con-historia-sigue-como-hoy) | Compatibilidad | Alta | Sí | ☐ |
| HU-022 | [CA-07](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md#ca-07--una-fase-recién-abierta-no-se-marca-como-commiteada) | [CP-008](#cp-008--una-fase-recién-abierta-no-se-marca) | Funcional, error | Alta | Sí | ☐ |

**Cobertura:** 9 de 9 exigencias cubiertas = 100%.

## 6. Casos de prueba

### CP-001 · Un pendiente nace sin historia

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-01 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-01 y la T-02 terminadas; una copia temporal con `pendientes/README.md` y `plantillas/pendiente.md` |
| **Datos de entrada** | `crear_pendiente(copia, "prueba-sin-historia", "", escribir=True)` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Llamar `crear_pendiente` sin historia | No falla |
| 2 | Leer el pendiente creado | La fila «Historia de usuario» dice «Por asignar» |
| 3 | Leer la tabla del índice | Tiene la fila del pendiente nuevo |
| 4 | Leer el mapa «Ningún pendiente vive suelto» | No tiene fila nueva |

**Resultado esperado final:** el pendiente queda anotado sin historia.

### CP-002 · Con historia, sigue como hoy

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-02 y RNF-02 |
| **Tipo** | Regresión |
| **Prioridad** | Crítica |
| **Precondiciones** | La T-02 terminada |
| **Datos de entrada** | Las pruebas que ya existen |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr `python -m unittest validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` | OK, incluida `test_la_llamada_de_siempre` |

**Resultado esperado final:** quien usa `--hu` no nota ningún cambio.

### CP-003 · Un `--hu` que no existe sigue fallando

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-03 |
| **Tipo** | Funcional, error |
| **Prioridad** | Alta |
| **Precondiciones** | La T-05 terminada |
| **Datos de entrada** | `crear_pendiente(copia, "prueba", "EP-001-x/HU-999-no-existe", escribir=True)` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Llamar `crear_pendiente` con la historia inexistente | Lanza `ValueError` con «no existe la historia» |
| 2 | Listar `pendientes/` de la copia | Ningún archivo nuevo |

**Resultado esperado final:** un error de tipeo no deja un pendiente suelto.

### CP-004 · `F23` nombra el orden

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-04 |
| **Tipo** | Funcional, camino feliz |
| **Prioridad** | Alta |
| **Precondiciones** | La T-06 y la T-07 terminadas |
| **Datos de entrada** | `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer el cuerpo de `F23` | Nombra hallazgo, pendiente, HU y fase, en ese orden, y la épica de la HU |
| 2 | Leer su checklist | Vuelto a aplicar, en CUMPLE |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas |

**Resultado esperado final:** el orden queda escrito en la regla.

### CP-005 · El índice y la plantilla dicen cuándo vale «Por asignar»

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-05 |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondiciones** | La T-08 y la T-09 terminadas |
| **Datos de entrada** | `pendientes/README.md` y `plantillas/pendiente.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Leer «Ningún pendiente vive suelto» | Dice que «Por asignar» vale mientras el pendiente no esté aprobado |
| 2 | Leer la nota de `plantillas/pendiente.md` | Dice que `--hu` es opcional |

**Resultado esperado final:** quien anota un pendiente sabe que puede hacerlo sin historia.

### CP-006 · «Por asignar» no reprueba la validación

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-06 |
| **Tipo** | Funcional, caso borde |
| **Prioridad** | Media |
| **Precondiciones** | Ninguna |
| **Datos de entrada** | Un pendiente de la copia del CP-001, con «Por asignar» |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Correr la validación de pendientes sobre la copia del CP-001 | Ninguna falla sobre el pendiente «Por asignar» |

**Resultado esperado final:** la validación acepta el pendiente sin historia.

### CP-007 · El cambio queda versionado

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / RNF-01 |
| **Tipo** | Trazabilidad |
| **Prioridad** | Media |
| **Precondiciones** | La T-11 terminada |
| **Datos de entrada** | `VERSION` y `CHANGELOG.md` |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Abrir `VERSION` | `38.3.0`, la siguiente a la 38.2.0 que usó HU-039 |
| 2 | Abrir `CHANGELOG.md` | La entrada `38.3.0`, marcada `**MENOR**` |
| 3 | Correr `python -m unittest -k test_toda_entrada_del_registro_declara_su_tipo validadores/pruebas.py` | OK |

**Resultado esperado final:** el cambio queda registrado con su tipo.

### CP-008 · Una fase recién abierta no se marca

| Campo | Valor |
|---|---|
| **HU / CA** | HU-022 / CA-07 |
| **Tipo** | Funcional, error |
| **Prioridad** | Alta |
| **Precondiciones** | La T-13 y la T-14 terminadas |
| **Datos de entrada** | Un repositorio de git temporal con el enganche colgado, la plantilla `11-funcionalidad-implementada.md` y una fase cuyo cierre es una copia del molde |

**Pasos**

| # | Acción | Resultado esperado |
|---|---|---|
| 1 | Commitear la fase con el cierre en molde | La estación 12 sigue vacía |
| 2 | Correr las pruebas de `ElHashDelCommitSeAnotaSolo` | OK, incluida `test_al_commitear_el_hash_queda_escrito`, que sigue marcando una fase con el cierre escrito |

**Resultado esperado final:** solo se marca la fase cuyo cierre está escrito.

## 9. Gestión de defectos

Un caso que no da lo esperado se corrige en la misma fase si está dentro de los archivos de la sección 2.1 del plan de trabajo. Si pide tocar otro archivo, se detiene el trabajo y se le pregunta al usuario (`02·F8`).

| ID | Título | CP | Severidad | Estado | Asignado | Fecha | Cierre |
|---|---|---|---|---|---|---|---|
| | Ninguno todavía | | | | | | |

## 12. Métricas e informe

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura de exigencias | (CA + RNF) con caso / (CA + RNF) totales | 100% |
| Pruebas del andamio y de la estación 12 | Aprobadas / ejecutadas | 100% |
| Archivos creados en el repositorio real por las pruebas | Conteo | 0 |

El resultado de cada métrica va en el [resultado_pruebas.md](resultado_pruebas.md).

## 15. Aprobación

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Product Owner | El usuario | | |
