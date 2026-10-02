# Resultado de Pruebas · Fase `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si cada criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `B-EP-023-HU-001-la-conversacion-pasa-sola-al-analisis` |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `a314271` más los cambios de la fase |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 8 | 8 | 8 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-10 · CP-001: la herramienta escribe en el análisis que nombra el estado**

**El problema que resuelve:** sin esto, la herramienta solo sirve para el análisis que alguien escribió dentro de su código, como pasó con el guion del análisis 1.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar el enganche en `adaptadores/claude-code/` | `hook_analisis.py` está ahí | Está |
| 2 | Escribir el estado con el segundo de dos análisis y correr `pasar` | Los turnos entran en el segundo y el primero no cambia | `test_cp001_escribe_en_el_analisis_del_estado` en verde |
| 3 | Buscar una ruta de análisis escrita dentro del código | No hay ninguna | No hay |

**Cómo se verificó que la pareja cumple:** el paso 2 decide; el 3 prueba que no hay una ruta fija.

**CA-03 · CP-002: lo que el usuario agregó no se toca**

**El problema que resuelve:** sin esto, cada turno nuevo borraría lo que se escribió en el análisis fuera de la conversación.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `pasar` dos veces, con un turno nuevo entre una y otra | El turno nuevo entra | Entra |
| 2 | Comparar lo que está fuera de la sección «Conversación» | Igual, letra por letra | Igual: `test_cp002_lo_agregado_a_mano_no_se_toca` en verde |

**Cómo se verificó que la pareja cumple:** el paso 2 decide.

**CA-09 y CA-13 · CP-003: sin marcas ni etiquetas en lo que escribe la herramienta**

**El problema que resuelve:** sin esto, el análisis arrastra las rayas de la transcripción y las etiquetas que la herramienta le pone al mensaje.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `pasar` sobre una transcripción con raya en los encabezados | Los encabezados llevan coma | `### 1 · Usuario, 2026` y `**Agente**, 2026` |
| 2 | Buscar las etiquetas de texto pegado y de archivo abierto | No están; las palabras del usuario sí | No están; «texto pegado» sí |
| 3 | Medir el análisis con `marcas.py` | Cero marcas | 0 |

**Cómo se verificó que la pareja cumple:** los tres pasos están en `test_cp003`, en verde.

**CA-11 · CP-004: prender, pausar, volver a prender y aprobar**

**El problema que resuelve:** sin esto, prender y apagar dependen de que alguien edite archivos a mano y se acuerde.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | «Analicemos: el pendiente 7» en el turno 2 | Se crea `analisis-1.md` desde la plantilla y el estado arranca en el turno 2 | Así |
| 2 | «Pare» en el turno 4, y «Analicemos: el pendiente 7» en el turno 6 | La línea «turnos 4 a 5 en pausa» y sin esos turnos | Así, después de corregir el defecto DEF-01 |
| 3 | «Apruebo el análisis» en el turno 7 | La marca con la fecha y el turno 7 | Así |
| 4 | Pasar la respuesta del turno 7 | El estado se borra y el turno 8 no entra | Así |
| 5 | «Analicemos por qué falla esto», sin pendiente | No se prende nada | No se prende |

**Cómo se verificó que la pareja cumple:** los cinco pasos están en `test_cp004`, en verde en el segundo intento.

**CA-14 · CP-005: no se prende otro pendiente con un análisis abierto**

**El problema que resuelve:** sin esto, quedan varios análisis abiertos sobre lo mismo y el trabajo se duplica (análisis 2, conclusión 6).

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | «Analicemos» del segundo pendiente, con el primero aprobado y su HU sin terminar | No se prende y el aviso nombra el análisis abierto | No se prende; nombra `analisis-1.md` |
| 2 | «Analicemos» del primero | Se prende su análisis siguiente | Se prende `analisis-2.md` |
| 3 | Marcar la HU como terminada y repetir el paso 1 | Se prende | Se prende |

**Cómo se verificó que la pareja cumple:** los tres pasos están en `test_cp005`, en verde. Sobre el repositorio real, `abiertos` nombra el análisis 5 del pendiente 103, porque la HU-001 no ha terminado.

**CA-12 · CP-006: el aviso de cada turno**

**El problema que resuelve:** sin esto, nadie sabe a qué análisis está entrando lo que se habla.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr el enganche con un análisis prendido | El aviso lo nombra; código 0 | Así, en `test_cp006` |
| 2 | Correr el enganche sin ninguno | Dice que ninguno está prendido; código 0 | Así, en `test_cp006`, y también en esta sesión: desde el cambio de `.claude/settings.json` cada mensaje trae «[ANÁLISIS EN CURSO] Ningún análisis está prendido» |

**Cómo se verificó que la pareja cumple:** el paso 2 se vio además en la sesión real.

**CA-15 · CP-007: el instalador registra la herramienta**

**El problema que resuelve:** sin esto, cada proyecto tendría que configurar a mano la herramienta.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validadores/instalar.py` sobre un proyecto de prueba con git | Termina sin error | Código 0 |
| 2 | Leer su `.claude/settings.json` | `hook_analisis.py` en `UserPromptSubmit` y en `Stop` | Las dos entradas |
| 3 | Leer el `.claude/settings.json` del estándar | Ya no nombra `pasar_conversacion.py` | No lo nombra; nombra dos veces `hook_analisis.py` |
| 4 | Correr `validar.py amarre` | Sin fallas | Sin fallas, después de agregar la fila de `analisis.py` (DEF-02) |

**Cómo se verificó que la pareja cumple:** los pasos 1 y 2 deciden. En el estándar no se corrió el instalador: también habría tocado archivos que el plan no declara. Las dos entradas se cambiaron a mano en `.claude/settings.json`, que sí está declarado.

**RNF-06 · CP-008: cada tarea cita su criterio**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio | Sin avisos de tareas sueltas; queda el aviso de que la especificación es la HU |

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-10 | Crítica | 2026-10-02 | Dos análisis de prueba; el turno entró solo en el que nombraba el estado | Aprobado | EV-01 | Ninguno |
| CP-002 | CA-03 | Crítica | 2026-10-02 | Una nota en «Conclusiones» siguió igual tras dos pasadas | Aprobado | EV-01 | Ninguno |
| CP-003 | CA-09, CA-13 | Media | 2026-10-02 | Transcripción con raya y etiquetas: coma, sin etiquetas, 0 marcas | Aprobado | EV-01 | Ninguno |
| CP-004 | CA-11 | Alta | 2026-10-02 | Pendiente 7 de prueba: prender, pausa 4 a 5, aprobar en el 7 y apagado | Aprobado | EV-01 | DEF-01 |
| CP-005 | CA-14 | Alta | 2026-10-02 | Pendiente 8 bloqueado por el 7 con su HU sin terminar; libre al terminarla | Aprobado | EV-01, EV-02 | Ninguno |
| CP-006 | CA-12 | Alta | 2026-10-02 | El enganche corrido con y sin análisis; código 0; el aviso en esta sesión | Aprobado | EV-01, EV-03 | Ninguno |
| CP-007 | CA-15 | Alta | 2026-10-02 | Instalador sobre un proyecto vacío con git; `amarre` sin fallas | Aprobado | EV-04 | DEF-02 |
| CP-008 | RNF-06 | Media | 2026-10-02 | `validar.py flujo` y lectura del plan | Aprobado | EV-05 | Ninguno |

**Correspondencia con el plan:** 8 casos en el plan, 8 acá.

**Qué salió distinto de lo esperado:** el CP-004 falló la primera vez por el DEF-01, y el CP-007 destapó el DEF-02. Los dos están en la sección 4.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que el enganche corra en la sesión real | Leer el aviso que llega con cada mensaje | Llega: «Ningún análisis está prendido» |
| 2 | Que las marcas nuevas sean solo las de la notación del mapa | `marcas.py` contra el commit anterior | Solo los tres semáforos de las filas nuevas del mapa del amarre, que es su notación |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | Al volver a prender después de una pausa, el estado arrancaba de nuevo porque comparaba rutas con separadores distintos | CP-004 | Alta | Corregido: las rutas del estado se normalizan | Este documento |
| DEF-02 | `validadores/analisis.py`, de la fase `A`, no estaba en el mapa del amarre | CP-007 | Media | Corregido en esta fase, por decisión del usuario | Este documento y el cierre de la fase `A` |

**Defectos abiertos que se aceptan y por qué:** ninguno.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-03 | CP-002 | Aprobado | Sí |
| CA-09 | CP-003 | Aprobado | Sí |
| CA-10 | CP-001 | Aprobado | Sí |
| CA-11 | CP-004 | Aprobado | Sí |
| CA-12 | CP-006 | Aprobado | Sí |
| CA-13 | CP-003 | Aprobado | Sí |
| CA-14 | CP-005 | Aprobado | Sí |
| CA-15 | CP-007 | Aprobado | Sí |
| RNF-06 | CP-008 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 9 de 9 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 8 de 8 | Sí |
| Tasa de aprobación | Plan §12.1 | 100% | 8 de 8 | Sí |
| Casos críticos y altos | Plan §3.4 | 100% | 6 de 6 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 1: el DEF-02, que vino de la fase `A` | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los ocho criterios de la fase y el RNF-06 tienen su caso ejecutado y aprobado; los dos defectos quedaron corregidos.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Pruebas | `validadores/tests/test_analisis_en_curso.py`, 6 de 6 en verde |
| EV-02 | Salida de `abiertos` sobre el repositorio | Transcripción de la sesión del 2026-10-01 |
| EV-03 | El aviso en la sesión real | Transcripción de la sesión del 2026-10-01 |
| EV-04 | Instalador sobre un proyecto de prueba y `validar.py amarre` | Transcripción de la sesión del 2026-10-01 |
| EV-05 | `validar.py flujo` | Transcripción de la sesión del 2026-10-01 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 8 | 0 | Primera ejecución; el CP-004 pasó en el segundo intento, tras corregir el DEF-01 |
