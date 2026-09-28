# Resultado de Pruebas · Fase `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-022-andamio-impone-un-orden-de-trabajo-incorrecto` |
| **HU** | [HU-022](../HU-022-andamio-impone-un-orden-de-trabajo-incorrecto.md) de EP-005 |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-09-27 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Copias temporales del repositorio y un repositorio de git temporal; versión 38.3.0 sin commitear |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-01 · CP-001, que un pendiente nazca sin historia**

**El problema que resuelve:** para anotar un pendiente había que inventarle antes su historia.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Llamar `crear_pendiente(copia, "prueba-sin-historia", "", escribir=True)` | No falla | No falló |
| 2 | Leer el pendiente creado | «Historia de usuario» dice «Por asignar» | «Por asignar: nace al aprobarse este pendiente» |
| 3 | Leer la tabla del índice | Tiene la fila del pendiente | La tiene, apuntando a `02-prueba-sin-historia.md` |
| 4 | Leer el mapa de historias | Sin fila nueva | Igual que antes |

**Cómo se verificó que la pareja cumple:** la prueba `test_cp_001_sin_historia_dice_por_asignar_y_no_toca_el_mapa` hace los cuatro pasos y pasó. `test_sin_hu_por_la_linea_de_ordenes` confirma lo mismo por la línea de órdenes.

**CA-02 y RNF-02 · CP-002, que con historia siga como hoy**

**El problema que resuelve:** el cambio no puede romper a quien ya usa `--hu`.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `python -m unittest validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py` | OK, incluida `test_la_llamada_de_siempre` | `Ran 12 tests ... OK`: las 8 que ya había y las 4 nuevas |

**Cómo se verificó que la pareja cumple:** las pruebas que ya existían pasan sin cambios.

**CA-03 · CP-003, que un `--hu` que no existe siga fallando**

**El problema que resuelve:** un error de tipeo no puede dejar un pendiente suelto.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Llamar `crear_pendiente` con `HU-999-no-existe` | `ValueError` con «no existe la historia» | Eso |
| 2 | Listar `pendientes/` de la copia | Ningún archivo nuevo | Ninguno |

**Cómo se verificó que la pareja cumple:** la prueba `test_cp_003_una_historia_que_no_existe_sigue_fallando` pasó; por la línea de órdenes también dio el error.

**CA-04 · CP-004, que `F23` nombre el orden**

**El problema que resuelve:** el orden completo no estaba escrito en ninguna regla.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el cuerpo de `F23` | Hallazgo, pendiente, HU y fase, en ese orden, y la épica de la HU | «Un hallazgo se anota como pendiente; el pendiente aprobado baja a una historia de usuario hija de la épica que le corresponda, y se construye como fase de esa historia» |
| 2 | Leer su checklist | Vuelto a aplicar, en CUMPLE | Contra v38.3.0, 2026-09-27, 19 ✅ y 1 N/A |
| 3 | Correr `python validadores/validar.py metareglas` | 0 fallas | `0 falla(s), 1 aviso(s)`; el aviso es el de `M17`, de la línea base |

**Cómo se verificó que la pareja cumple:** el cuerpo nombra los cuatro eslabones y cabe en el molde, con 318 caracteres leídos.

**CA-05 · CP-005, que el índice y la plantilla digan cuándo vale «Por asignar»**

**El problema que resuelve:** quien anota un pendiente no sabía que podía hacerlo sin historia.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer «Ningún pendiente vive suelto» | La frase sobre «Por asignar» | «Mientras el pendiente no esté aprobado, esa fila dice «Por asignar»», al comienzo de la frase nueva |
| 2 | Leer la nota de `plantillas/pendiente.md` | `--hu` es opcional | «Sin `--hu`, la historia queda «Por asignar» hasta que el pendiente se apruebe» |

**Cómo se verificó que la pareja cumple:** las dos frases están.

**CA-06 · CP-006, que «Por asignar» no repruebe la validación**

**El problema que resuelve:** si la validación lo rechazara, el modo nuevo no serviría.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `pendientes.abierto_nombra_su_historia` sobre la copia del CP-001 | Ninguna falla sobre el pendiente nuevo | Ninguna |

**Cómo se verificó que la pareja cumple:** la prueba `test_cp_006_por_asignar_no_reprueba_la_validacion` pasó, y `validar.py pendientes` sobre el repositorio real dio 0 fallas.

**RNF-01 · CP-007, que el cambio quede versionado**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Abrir `VERSION` | `38.3.0` | `38.3.0` |
| 2 | Abrir `CHANGELOG.md` | La entrada `38.3.0`, marcada `**MENOR**` | Está |
| 3 | Correr la prueba del tipo del registro | OK | OK |

**Cómo se verificó que la pareja cumple:** los tres pasos dan lo esperado.

**CA-07 · CP-008, que una fase recién abierta no se marque**

**El problema que resuelve:** el enganche daba por commiteada una fase que solo tenía su plan de trabajo.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Commitear, en un repositorio temporal con el enganche, una fase cuyo cierre es copia del molde | La estación 12 sigue vacía | Siguió vacía |
| 2 | Correr las pruebas de `ElHashDelCommitSeAnotaSolo` | OK, y la fase con el cierre escrito se sigue marcando | `Ran 17 tests ... OK` |
| 3 | Quitar la condición nueva de `estacion_commit.py` y correr la prueba del paso 1 | La prueba falla | `FAILED (failures=1)`; con la condición de vuelta, OK |

**Cómo se verificó que la pareja cumple:** el paso 3 prueba que la prueba detecta el defecto y no pasa por casualidad.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-09-27 | `crear_pendiente` sin historia: «Por asignar», fila en el índice, mapa igual | Aprobado | EV-01 | — |
| CP-002 | CA-02 y RNF-02 | Crítica | 2026-09-27 | Las 12 pruebas del andamio, OK | Aprobado | EV-01 | — |
| CP-003 | CA-03 | Alta | 2026-09-27 | `HU-999-no-existe`: `ValueError` y ningún archivo nuevo | Aprobado | EV-01 | — |
| CP-004 | CA-04 | Alta | 2026-09-27 | El cuerpo nuevo de `F23`, su checklist y `metareglas` | Aprobado | EV-02 | — |
| CP-005 | CA-05 | Media | 2026-09-27 | La frase del índice y la nota de la plantilla | Aprobado | EV-03 | — |
| CP-006 | CA-06 | Media | 2026-09-27 | `abierto_nombra_su_historia` sin fallas sobre el pendiente nuevo | Aprobado | EV-01 | — |
| CP-007 | RNF-01 | Media | 2026-09-27 | `VERSION` 38.3.0, entrada `**MENOR**`, prueba del tipo OK | Aprobado | EV-04 | — |
| CP-008 | CA-07 | Alta | 2026-09-27 | Fase con el cierre en molde: estación 12 vacía; sabotaje de la condición: la prueba falla | Aprobado | EV-05 | — |

**Correspondencia con el plan:** 8 casos en el plan, 8 aquí.

**Qué salió distinto de lo esperado:** la primera corrida de la prueba del CP-008 dio error porque usaba un nombre que `pruebas.py` no define; se corrigió y pasó. No fue un defecto del código de la fase.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que las pruebas no crearan archivos en el repositorio real | `git status` después de correrlas | Ningún archivo nuevo en `pendientes/` |

## 4. Defectos encontrados

Ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001 | Aprobado | Sí |
| CA-02 | CP-002 | Aprobado | Sí |
| CA-03 | CP-003 | Aprobado | Sí |
| CA-04 | CP-004 | Aprobado | Sí |
| CA-05 | CP-005 | Aprobado | Sí |
| CA-06 | CP-006 | Aprobado | Sí |
| CA-07 | CP-008 | Aprobado | Sí |
| RNF-01 | CP-007 | Aprobado | Sí |
| RNF-02 | CP-002 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100% | 9 de 9 con caso | Sí |
| Pruebas del andamio y de la estación 12 | Plan §12 | 100% | 12 de 12 y 17 de 17 | Sí |
| Archivos creados en el repositorio real por las pruebas | Plan §12 | 0 | 0 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple

**Justificación:** las nueve exigencias de la HU, CA-01 a CA-07, RNF-01 y RNF-02, cumplen con su caso ejecutado (§5).

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de pruebas | `validadores/tests/test_el_andamio_levanta_la_historia_y_el_pendiente.py`, clase `HU022ElPendienteNaceSinHistoria` |
| EV-02 | Archivo resultante y salida de `metareglas` | `base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md` |
| EV-03 | Archivos resultantes | `pendientes/README.md` y `plantillas/pendiente.md` |
| EV-04 | Archivos resultantes y prueba | `VERSION`, `CHANGELOG.md` y `test_toda_entrada_del_registro_declara_su_tipo` |
| EV-05 | Salida de pruebas | `validadores/pruebas.py`, `test_una_fase_recien_abierta_no_se_marca` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-09-27 | 8 | 0 | Primera ejecución |
