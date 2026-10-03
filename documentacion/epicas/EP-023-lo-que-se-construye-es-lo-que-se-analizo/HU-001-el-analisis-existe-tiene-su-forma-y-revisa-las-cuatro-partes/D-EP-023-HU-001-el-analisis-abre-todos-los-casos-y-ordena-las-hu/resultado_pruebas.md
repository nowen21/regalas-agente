# Resultado de Pruebas · Fase `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Dice qué pasó al correr los casos del plan de pruebas de esta fase, caso por caso, y si el criterio quedó cumplido. Va aparte del plan para no perder la línea base que se aprobó.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `D-EP-023-HU-001-el-analisis-abre-todos-los-casos-y-ordena-las-hu` |
| **HU** | [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md) |
| **Plan de pruebas de origen** | [`plan_pruebas.md`](plan_pruebas.md), versión 2.0 |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-02 |
| **Ejecutado por** | Claude |
| **Ambiente y versión** | Repositorio del estándar en la máquina local, rama `main`, sobre el commit `8383963` más los cambios de la fase, versión 44.0.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 11 | 11 | 11 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**CA-17 · CP-001: «Dónde más puede pasar»**

**El problema que resuelve:** sin esto, el análisis se queda en el caso que destapó el hallazgo y los demás vuelven por otro lado.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer la plantilla del análisis | Tiene la sección, con su nota y sus cuatro columnas | Está al final de «Lo que aportó cada parte», con su nota y caso, dónde se presenta, riesgo y lo que lo cubre |
| 2 | Validar un análisis con la sección completa | Ninguna falla | Ninguna (`test_cp001_el_completo_pasa`) |
| 3 | Validar uno sin la sección | Una falla | Una (`test_cp001_sin_donde_mas_falla`) |
| 4 | Validar uno con una fila sin lo que la cubre | Una falla que nombra el caso | Una, que nombra «Otro canal» |

**CA-18 · CP-002: la tabla de HU con su dependencia y su orden**

**El problema que resuelve:** sin esto, las HU se construyen en un orden que nadie decidió y una arranca antes de la que necesita.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer la plantilla del análisis y la de la épica | Las dos piden orden, dependencia y razón | La del análisis: orden, HU, título, parte del problema, depende de, por qué y puntos. La de la épica: orden, HU, depende de, por qué y estado |
| 2 | Validar una tabla bien ordenada | Ninguna falla | Ninguna |
| 3 | Validar una donde una HU va antes de la que depende | Una falla que nombra las dos HU | «la HU 2 va antes de la HU 1, de la que depende» |
| 4 | Validar una con un puesto sin razón | Una falla | «la HU 2 no dice por qué va en su puesto» |

**CA-19 · CP-003: las recomendaciones**

**El problema que resuelve:** sin esto, lo aprendido en un análisis no llega al siguiente.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `plantillas/recomendaciones-del-analisis.md` | Su forma, sus dos niveles y las de arranque, cada una con su origen | 17 recomendaciones que juntan las 36 lecciones de los análisis 1 a 8, cada una con su análisis y su lección |
| 2 | Leer la plantilla del análisis | Abre con «Recomendaciones», que enlaza los dos archivos y pide decir cuáles aplican | Así |
| 3 | Validar una recomendación sin origen y dos con el mismo «qué se hace» | Una falla por cada una | Dos fallas (`test_cp003_recomendacion_sin_origen_y_repetida`) |
| 4 | Validar un análisis aprobado con 44.0.0 que no dice cuáles consultó | Una falla | Una |
| 5 | Leer los análisis 1 a 9 del pendiente 103 | Cada uno tiene «Recomendaciones», con la nota del piloto | Los nueve, con las que salieron de sus lecciones |
| 6 | Correr `validar.py plantilla` sobre el archivo | Sin fallas | 0 fallas; 1 aviso por la nota de plantilla, que es su forma |
| 7 | Leer el recuerdo | Enlaza la R-1 y conserva que el usuario lo pidió | Así; el índice de la memoria lo dice |

**CA-20 · CP-004: el análisis principal al día**

**El problema que resuelve:** sin esto, el principal solo nombra los análisis que cambiaron algo y se pierde lo que los demás confirmaron.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer el análisis principal | Su contenido es la redacción que forman los aportes, sin «Qué se construye hoy» | La redacción une la frase inicial con lo que suman los diez análisis, tal cual |
| 2 | Leer la «Lista de análisis» | Los diez análisis, con fecha, resultado y enlace | Diez filas, del 2026-08-07 al 2026-10-02 |
| 3 | Validar con un análisis aprobado que no aparece en la lista | Un aviso, aunque se haya aprobado antes de 44.0.0 | Un aviso, sobre un análisis sin versión en la marca |

**CA-21 · CP-005: medir la respuesta antes de entregarla**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer las recomendaciones de arranque | Una dice que la respuesta se mide contra `00·ID9` antes de entregarla, con su origen | La R-17, del análisis 8, lección 5 |

**CA-22 · CP-006: lo nuevo no reabre lo aprobado**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Aprobar un análisis de prueba | La marca dice la fecha, el turno y la versión, y la siguen encontrando `aprobado()` y `turno_aprobado()` | «en el turno 7, con la versión 44.0.0.», y las dos la encuentran |
| 2 | Correr `validar.py analisis` sobre el repositorio | Los análisis 1 a 9 pasan sin lo que exige la 44.0.0 | `OK: sin incumplimientos` |
| 3 | Validar uno aprobado con 44.0.0 sin las secciones | Falla | Dos fallas; con 43.0.0 o sin versión, ninguna |

**RNF-06 · CP-007: cada tarea cita su criterio**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `validar.py flujo` y leer el plan | Ninguna tarea sin su criterio | Sin avisos de tareas sueltas; queda el aviso de que la especificación es la HU, que ya tenía la versión 1 |

**CA-23 · CP-008: `DOC25` anota todo análisis aprobado**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer `13·DOC25` | Pide anotar cada análisis aprobado, aunque no cambie el sistema, con lo que aportó tal cual | Así, con un ejemplo de un análisis que solo ratifica |
| 2 | Leer su checklist | Cumple, contra 44.0.0 | Cumple, contra 44.0.0; `validar.py estandar` sin fallas |

**CA-24 · CP-009: lo que suma pasa tal cual al principal**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer la plantilla del análisis | Termina con «Lo que aporta al análisis principal», con el resultado y lo que suma | Así |
| 2 | Aprobar un análisis de prueba | Lo que suma queda, letra por letra, al final de la redacción, y su fila al final de la lista | Así, con el enlace «Análisis 1 del pendiente 7» |
| 3 | Aprobar uno dentro de un módulo con principal propio | Queda en el del módulo y no en el del proyecto | Así |
| 4 | Cambiar una palabra en el principal y correr el validador | Una falla que nombra el análisis | «lo que suma no está tal cual en analisis/proyecto-analisis-principal.md» |
| 5 | Correr `validar.py analisis` sobre el repositorio | Los diez análisis del piloto pasan | Pasan |

**CA-25 · CP-010: sin filas no se aprueba**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Aprobarlo | Sin la marca, y el aviso dice que falta al menos una fila | Sin la marca; el enganche dice «No se aprobó: falta al menos una fila en «Lo que se tiene que hacer»» |

**CA-26 · CP-011: sin «Lo que aporta» no se aprueba**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Aprobar uno sin la sección y otro sin lo que suma | Ninguno queda aprobado, y el aviso dice qué falta | Ninguno; el motivo nombra la sección |

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-17 | Alta | 2026-10-02 | Lectura y `test_analisis.py` | Aprobado | EV-01, EV-02 | Ninguno |
| CP-002 | CA-18 | Alta | 2026-10-02 | Lectura y `test_analisis.py` | Aprobado | EV-01, EV-02 | Ninguno |
| CP-003 | CA-19 | Alta | 2026-10-02 | Lectura, `test_analisis.py` y `validar.py plantilla` | Aprobado | EV-01, EV-02 | Ninguno |
| CP-004 | CA-20 | Media | 2026-10-02 | Lectura y `test_analisis.py` | Aprobado | EV-01, EV-02 | Ninguno |
| CP-005 | CA-21 | Media | 2026-10-02 | Lectura | Aprobado | EV-01 | Ninguno |
| CP-006 | CA-22 | Alta | 2026-10-02 | `test_analisis.py`, `test_analisis_en_curso.py` y `validar.py analisis` | Aprobado | EV-02 | Ninguno |
| CP-007 | RNF-06 | Media | 2026-10-02 | `validar.py flujo` | Aprobado | EV-03 | Ninguno |
| CP-008 | CA-23 | Media | 2026-10-02 | Lectura y `validar.py estandar` | Aprobado | EV-01, EV-03 | Ninguno |
| CP-009 | CA-24 | Alta | 2026-10-02 | Lectura, `test_analisis_en_curso.py` y `test_analisis.py` | Aprobado | EV-01, EV-02 | Ninguno |
| CP-010 | CA-25 | Alta | 2026-10-02 | `test_analisis_en_curso.py`, también por el enganche | Aprobado | EV-02 | Ninguno |
| CP-011 | CA-26 | Alta | 2026-10-02 | `test_analisis_en_curso.py` | Aprobado | EV-02 | Ninguno |

**Correspondencia con el plan:** 11 casos en el plan, 11 acá.

**Qué salió distinto de lo esperado:** el primer aviso del CA-20 tomó como análisis los archivos de `prompts/analisis/`, que guardan palabras del usuario. Se corrigió dentro de la tarea T-11: la forma anterior solo cuenta en la carpeta `analisis/` que tiene su principal, y lo prueba `test_los_prompts_no_son_analisis`.

## 3. Verificaciones manuales  ·  `08·T4`

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la redacción del principal sea, letra por letra, lo que suma cada análisis | La armó un guion leyendo cada sección; `validar.py analisis` lo compara | Iguales |
| 2 | Marcas de `00·ID8` en lo que escribió la fase | `marcas.py` | Ninguna nueva; las tres viñetas que salieron en las recomendaciones pasaron a una tabla |

## 4. Defectos encontrados

Ninguno de la fase. La suite completa, 832 pruebas corridas por partes y en primer plano, deja 5 fallas que ya estaban antes de la fase:

| Prueba | Qué dice | De dónde viene |
|---|---|---|
| `test_citas_y_enlaces_de_ejemplo` | Los enlaces con ancla de `base/mapa-de-tareas.md` | Commit `e4de142` |
| `test_el_mapa_del_amarre_no_envejece` | El recuento de `anatomia/` dice 30 de 89 y el programa cuenta 32 de 93 | Fases anteriores |
| `test_el_texto_del_enlace_dice_donde_vive` | 18 enlaces entre carpetas sin la ruta en su texto; ninguno de esta fase | Fases anteriores |
| `test_ninguno_termina_en_silencio` (2) | El código de salida de `mapa_tareas.py` y de `analisis_en_curso.py` | Fases anteriores |

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-17 | CP-001 | Aprobado | Sí |
| CA-18 | CP-002 | Aprobado | Sí |
| CA-19 | CP-003 | Aprobado | Sí |
| CA-20 | CP-004 | Aprobado | Sí |
| CA-21 | CP-005 | Aprobado | Sí |
| CA-22 | CP-006 | Aprobado | Sí |
| CA-23 | CP-008 | Aprobado | Sí |
| CA-24 | CP-009 | Aprobado | Sí |
| CA-25 | CP-010 | Aprobado | Sí |
| CA-26 | CP-011 | Aprobado | Sí |
| RNF-06 | CP-007 | Aprobado | Sí |

**Los que no cumplen:** ninguno.

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §12.1 | 100% | 11 de 11 | Sí |
| Casos ejecutados | Plan §12.1 | 100% | 11 de 11 | Sí |
| Hallazgos al ejecutar | Plan §12.1 | Los que no se podían prever | 0 | Sí |

**Lo que no se cumplió:** nada.

## 6. Veredicto de la fase

**Concepto:** Cumple. Aprobada por el usuario el 2026-10-02.

**Justificación:** los CA-17 a CA-26 y el RNF-06 tienen sus casos ejecutados y aprobados, y la suite completa no tiene fallas nuevas.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Plantillas, recomendaciones, `DOC25` y análisis principal | `plantillas/analisis.md`, `plantillas/recomendaciones-del-analisis.md`, `plantillas/ciclo-vida-proyectos/03-epica.md`, `base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md`, `analisis/proyecto-2026-10-02-analisis-principal.md` |
| EV-02 | Pruebas de la fase | `validadores/tests/test_analisis.py` (22) y `validadores/tests/test_analisis_en_curso.py` (18) |
| EV-03 | Salida de `validar.py estandar`, `origen`, `analisis` y `flujo`, de la suite y de `marcas.py` | Transcripción de la sesión del 2026-10-01 |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-02 | 11 | 0 | Primera ejecución |
