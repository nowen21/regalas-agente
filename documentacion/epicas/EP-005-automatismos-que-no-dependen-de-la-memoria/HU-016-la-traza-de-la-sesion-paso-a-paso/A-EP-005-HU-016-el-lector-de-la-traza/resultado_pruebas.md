# Resultado de Pruebas — Fase A-EP-005-HU-016: el lector de la traza

**Para qué sirve este documento.** Registra **qué se ejecutó de verdad y con qué resultado**, y de ahí sale el **veredicto de la fase**: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección "qué se probó" del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que **no se modifica** al ejecutar: se aprobó antes y así se queda.

---

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-005-HU-016-el-lector-de-la-traza` |
| **HU** | [HU-016](../HU-016-la-traza-de-la-sesion-paso-a-paso.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-08-20 |
| **Ejecutado por** | El agente, con el plan aprobado por el usuario en la sesión 5 |
| **Ambiente y versión** | La máquina de trabajo, sobre el árbol de la 28.0.0 sin commit; Python 3.11 |

---

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno. Los CP-001 a CP-005 corren en la suite (6 casos automatizados, uno más que empareja respuestas desordenadas); CP-006 corrió sobre la transcripción real de esta sesión; CP-007 es la regresión.

---

## 2. Ejecución caso por caso

**CA-01 · CP-001 — tres pasos, uno con error**

**El problema que resuelve:** sin la fila completa (hora, herramienta, entrada, duración, estado) la traza no sirve para reconstruir cómo pasó algo.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribir una transcripción con `Read`, `Bash` (`is_error: true`) y `WebFetch`, respuestas a 2, 5 y 1 segundos, y `CENTINELA` dentro de cada resultado | El archivo existe | Existe |
| 2 | Correr `validar.py traza <archivo>` | Código 0 | 0 |
| 3 | Leer las filas | Tres, numeradas, con hora `10:00:00`, herramienta, entrada (`a.md`, `python x.py`), `2 s`, `5 s`, `1 s`, y la fila 2 con `error` | Las tres, con esos valores |
| 4 | Buscar `CENTINELA` en la salida | No aparece | No aparece |

**Cómo se verificó que la pareja cumple:** el paso 3 decide los cinco datos de la fila; el 4 es RNF-02 (privacidad) y va acá porque la centinela viaja dentro de los tres resultados. Caso `test_cp_001` de EV-01.

**CA-02 · CP-002 — el cierre**

**El problema que resuelve:** sin totales hay que contar filas a mano.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Leer las últimas líneas de CP-001 | «3 pasos», «1 error», `Bash 1`, `Read 1`, `WebFetch 1`, el más lento `Bash (5 s)`, duración total `21 s` | Todo presente |

**Cómo se verificó que la pareja cumple:** los cinco totales contra los datos sintéticos, que se conocen de antemano. Caso `test_cp_002` de EV-01.

**CA-03 · CP-003 — escribe junto al histórico e indexa una vez**

**El problema que resuelve:** una traza suelta, sin el nombre del histórico ni índice, no se encuentra.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Crear `historico-chat/2026-08-20-sesion.md` con `<!-- sesion: abc -->` y la transcripción `abc.jsonl` | Los dos existen | Existen |
| 2 | Correr con `--escribir --raiz` | Existe `historico-chat/trazas/2026-08-20-sesion.md` con las filas, y el README de `trazas/` lo enlaza con la ruta desde la raíz | Existe, con las filas y «3 pasos»; el índice con `historico-chat/trazas/2026-08-20-sesion.md` |
| 3 | Correr de nuevo | El archivo se reescribe; el índice tiene una sola línea para él | Una sola |

**Cómo se verificó que la pareja cumple:** el paso 2 decide el nombre y el índice; el 3, que repetir no duplica. Caso `test_cp_003` de EV-01.

**CA-03 · CP-004 — sin histórico no inventa**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `--escribir` sobre una carpeta sin `historico-chat/` | Una frase, código 1, nada escrito | Así salió |
| 2 | Con `historico-chat/` pero sin la marca de esa sesión | Una frase, código 1, nada escrito | Así salió |

**Cómo se verificó que la pareja cumple:** en los dos casos se comprueba además que la carpeta `trazas/` no nació. Caso `test_cp_004` de EV-01.

**CA-04 · CP-005 — lo raro**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Una línea «esto no es JSON» entre pasos válidos | La traza sale igual | 2 pasos, código 0 |
| 2 | Un `tool_use` sin su `tool_result` | Fila con `sin respuesta` y duración vacía | Así salió |
| 3 | Archivo vacío | Una frase, código 1 | Así salió, sin volcado de error |
| 4 | Ruta inexistente | Una frase, código 1, sin volcado de error | Así salió |

**Cómo se verificó que la pareja cumple:** cada rareza aislada en su paso; el volcado de error se busca en la salida de error y no está. Caso `test_cp_005` de EV-01, más `test_las_respuestas_desordenadas_no_confunden`: con dos llamadas en paralelo y las respuestas invertidas, cada duración va con su paso (6 s y 2 s), porque se empareja por identificador y no por orden.

**RNF-01 · CP-006 — una sesión real**

**El problema que resuelve:** una traza que solo funciona con transcripciones de juguete no sirve.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr sobre la transcripción de esta sesión (1 MB) midiendo el tiempo | Menos de 2 segundos | 0,69 s, 191 filas |
| 2 | Contar los `tool_use` del archivo con un conteo directo | El mismo número que «pasos» | 191 y 191 |
| 3 | Correr con `--escribir --raiz .` | Queda en `historico-chat/trazas/` con el nombre del histórico de la sesión | `historico-chat/trazas/2026-08-20-sesion-5.md`, indexada |

**Cómo se verificó que la pareja cumple:** el conteo directo es independiente del lector; que coincidan dice que ninguna fila se perdió. El cierre real: 191 pasos, 9 errores (incluye los dos borrados bloqueados y los comandos demasiado largos de esta misma sesión), el más lento `Bash (204 s)`. Salida literal en EV-02.

**No regresión · CP-007 — nada de lo que ya estaba deja de pasar**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `validadores/tests/` entera | Pasa | 488 casos; quedaron las 2 fallas ajenas de las citas de `M19` (otra sesión). Las 3 que aparecieron de esta fase (el mapa del amarre sin `traza.py` y la entrada 28.0.0 sin abrir en llano) se corrigieron y sus pruebas quedaron en verde |
| 2 | `validadores/pruebas.py` entera | Todo en verde | 365 casos; 5 fallas, todas ajenas y anteriores (HU-007 y `M19`) |
| 3 | `validar.py amarre` | `traza.py` no aparece como amarrado | OK: 24 amarradas de 69, `traza.py` libre |

**Cómo se verificó que la pareja cumple:** contra la línea base del día; ninguna falla nombra archivos de esta fase. Salidas en EV-03.

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01 | Crítica | 2026-08-20 | Transcripción sintética de 3 pasos con fechas fijas; filas con `2 s`, `5 s`, `1 s` y `error` | Aprobado | EV-01 | — |
| CP-002 | CA-02 | Alta | 2026-08-20 | El cierre de la misma: 3 pasos, 1 error, `Bash (5 s)`, `21 s` | Aprobado | EV-01 | — |
| CP-003 | CA-03 | Crítica | 2026-08-20 | `--escribir` sobre proyecto de mentira; archivo con el nombre del histórico e índice sin duplicar | Aprobado | EV-01 | — |
| CP-004 | CA-03 | Alta | 2026-08-20 | Sin `historico-chat/` y sin la marca: frase, código 1, nada escrito | Aprobado | EV-01 | — |
| CP-005 | CA-04 | Alta | 2026-08-20 | Línea ilegible, paso sin respuesta, vacío, inexistente | Aprobado | EV-01 | — |
| CP-006 | RNF-01 | Media | 2026-08-20 | La transcripción real de esta sesión: 191 pasos = conteo directo, 0,69 s | Aprobado | EV-02 | — |
| CP-007 | No regresión | Alta | 2026-08-20 | Las dos suites y `amarre`; fallas solo las ajenas | Aprobado | EV-03 | — |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá. CP-006 sumó el paso de `--escribir` real, que el plan pedía como T-07.

**Qué salió distinto de lo esperado:** dos tropiezos de cierre documental, corregidos en la misma sesión: el mapa del amarre no tenía a `traza.py` (su prueba lo atrapó) y la entrada 28.0.0 del registro abría con jerga (la prueba de `M17` lo atrapó).

---

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | Que la traza real no exponga contenido de resultados | Lectura de `historico-chat/trazas/2026-08-20-sesion-5.md`: solo entradas recortadas a 80 y estados | Sin contenido de resultados |

---

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| — | Ninguno | — | — | — | — |

**Defectos abiertos que se aceptan y por qué:** ninguno.

---

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| [CA-01](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-01--la-línea-de-tiempo-de-una-sesión) | CP-001 | Aprobado | Sí |
| [CA-02](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-02--el-cierre-dice-los-totales) | CP-002 | Aprobado | Sí |
| [CA-03](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-03--con---escribir-queda-junto-al-histórico-indexada) | CP-003, CP-004 | Aprobados | Sí |
| [CA-04](../HU-016-la-traza-de-la-sesion-paso-a-paso.md#ca-04--lo-raro-no-revienta) | CP-005 | Aprobado | Sí |
| RNF-01 · 1 MB en menos de 2 s | CP-006 | 0,69 s | Sí |
| RNF-02 · privacidad | CP-001 paso 4 y verificación manual 1 | Sin contenido copiado | Sí |

**Los que no cumplen:** ninguno.

---

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de exigencias | Plan §5 | 100% — 7 de 7 | 7 de 7 | Sí |
| Fragmentos de resultado en la salida | Plan §12 | 0 | 0 | Sí |
| Pruebas del repositorio que dejan de pasar | Plan §12 | 0 | 0 (las que quedan son ajenas y anteriores) | Sí |

**Lo que no se cumplió:** nada.

---

## 6. Veredicto de la fase

**Concepto: Cumple.**

**Justificación:** los cuatro CA y los dos RNF con caso ejecutado y aprobado (§5); la sesión real trazada con conteo verificado de forma independiente; y la escritura junto al histórico funcionando sin duplicar índices.

---

## 7. Evidencias

| ID | Tipo | Ubicación |
|---|---|---|
| EV-01 | Suite, 6 de 6 en verde | `validadores/tests/test_la_sesion_tiene_traza.py` (corrida con `-v` el 2026-08-20) |
| EV-02 | La traza real | `historico-chat/trazas/2026-08-20-sesion-5.md` (191 pasos, 0,69 s, indexada) |
| EV-03 | Salidas de regresión | 488 y 365 casos con solo las fallas ajenas; `amarre` OK, 24 de 69 |

---

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-08-20 | 7 | 0 | Primera ejecución |
