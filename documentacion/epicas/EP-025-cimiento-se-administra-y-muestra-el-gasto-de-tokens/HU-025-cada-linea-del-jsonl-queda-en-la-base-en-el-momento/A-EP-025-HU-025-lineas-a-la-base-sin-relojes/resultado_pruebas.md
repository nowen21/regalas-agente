# Resultado de Pruebas · Fase A-EP-025-HU-025-lineas-a-la-base-sin-relojes   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `A-EP-025-HU-025-lineas-a-la-base-sin-relojes` |
| **HU** | [HU-025](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md) |
| **Ciclo** | 1 |
| **Fecha de ejecución** | 2026-10-06 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | Cimiento local con MariaDB, sobre el commit `f624d73` con los cambios de la fase sin guardar, versión 55.2.0 |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 7 | 7 | 7 | 0 | 0 | 0 |

**Casos no ejecutados y por qué:** ninguno.

## 2. Ejecución caso por caso

**[CA-01](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-01--la-línea-queda-en-la-base-sin-claves-y-una-sola-vez) con CP-001, CP-002 y CP-003, que la línea quede en la base sin claves y una sola vez**

**El problema que resuelve:** sin esto, lo que pasó en cada sesión se pierde a los 30 días, o queda con claves, o se guarda repetido.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | En `proyectos/cimiento/`, correr `.venv/Scripts/python manage.py test core.consumo.tests_lineas` | Las pruebas de líneas pasan | `Ran 5 tests ... OK` |
| 2 | Leer `test_cada_linea_queda_con_la_clave_tapada` | Una fila por línea, la clave no aparece y sí la marca, siguen 2 llamadas | Pasó: 8 líneas, `«enmascarado»` en vez de la clave, 2 llamadas |
| 3 | Leer `test_leer_otra_vez_no_duplica` y `test_desde_cero_trae_lo_que_ya_estaba_sin_duplicar` | Las mismas cantidades al leer otra vez | Pasaron |
| 4 | Leer `test_un_archivo_reescrito_conserva_las_dos_versiones` | Las líneas de antes más la nueva | Pasó |

**Cómo se verificó que la pareja cumple:** el paso 2 decide el tapado y el conteo de líneas; el 3, que no se duplica; el 4, el caso borde de la reescritura.

**[CA-02](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-02--el-vigilante-guarda-en-el-momento-del-aviso) y [CA-03](../HU-025-cada-linea-del-jsonl-queda-en-la-base-en-el-momento.md#ca-03--un-proyecto-nuevo-entra-con-su-primer-aviso) con CP-004 y CP-005, que el vigilante guarde en el aviso y sin relojes**

**El problema que resuelve:** con relojes, lo en vivo llega tarde y se aparta de lo acordado; sin releer la lista, el gasto de un proyecto nuevo se ignora.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Correr `manage.py test core.consumo.tests_vigilante` | Pasan | Incluidas en `Ran 27 tests ... OK` |
| 2 | Leer `test_cada_aviso_guarda_en_el_acto_sin_duplicar` | `avisar` deja las llamadas guardadas al volver | Pasó |
| 3 | Leer `test_lo_escrito_llega_solo` | Con `watchdog` de verdad, las llamadas llegan sin pedirlas y el hilo para con su evento | Pasó; el hilo terminó |
| 4 | Buscar `sleep(`, `CADA` y `time.monotonic` en `core/consumo/vigilante.py` | Ninguno | `0` coincidencias, y `test_no_tiene_relojes` pasó |
| 5 | Leer `test_un_proyecto_nuevo_entra_con_su_primer_aviso` | Relee la lista y guarda las 2 llamadas del proyecto nuevo | Pasó |

**Cómo se verificó que la pareja cumple:** el paso 4 decide «sin relojes»; el 2 y el 3, que se guarda en el aviso; el 5 cubre CA-03.

**RNF-02 con CP-006, la migración y la lectura desde cero sobre la base real**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `manage.py migrate consumo` | Aplica `0005` | `Applying consumo.0005_lineas_de_sesion... OK` |
| 2 | `manage.py migrate consumo 0004` | Quita la tabla | `Unapplying consumo.0005_lineas_de_sesion... OK` |
| 3 | `manage.py migrate consumo` | La vuelve a poner | `Applying consumo.0005_lineas_de_sesion... OK` |
| 4 | `manage.py leer_consumo --desde-cero` | Termina y cuenta líneas | Terminó en 7 min 2 s sobre 438 MB; 102 478 líneas, 51 con claves tapadas, 0 llamadas nuevas |

**CA-04 con CP-007, el README**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Buscar `/v1/logs` en `proyectos/cimiento/README.md` | No aparece | `0` |
| 2 | Leer el párrafo del gasto | Nombra al vigilante y la base | «El gasto de tokens llega a la base en cuanto Claude Code lo escribe...», con `vigilar_consumo` y `leer_consumo --desde-cero` |

| Caso | CA | Prioridad (del plan) | Fecha | Con qué se probó | Resultado | Evidencia | Defecto |
|---|---|---|---|---|---|---|---|
| CP-001 | CA-01, RNF-01 | Crítica | 2026-10-06 | `.jsonl` de muestra más una línea con una clave `ghp_...` armada al correr: 8 líneas guardadas, clave tapada, 2 llamadas | Aprobado | EV-01 | DEF-01 |
| CP-002 | CA-01 | Crítica | 2026-10-06 | Avance en cero y segunda lectura: mismas líneas y llamadas | Aprobado | EV-01 | — |
| CP-003 | CA-01 | Alta | 2026-10-06 | Archivo vaciado y reescrito con `m-9`: una línea más | Aprobado | EV-01 | — |
| CP-004 | CA-02 | Crítica | 2026-10-06 | `avisar` y `watchdog` real; ninguna palabra de reloj en el código | Aprobado | EV-02 | — |
| CP-005 | CA-03 | Alta | 2026-10-06 | Proyecto «dos» registrado después de leer la lista: 2 llamadas suyas | Aprobado | EV-02 | — |
| CP-006 | RNF-02 | Alta | 2026-10-06 | Migración de ida, vuelta e ida; lectura desde cero en 7 min | Aprobado | EV-03 | — |
| CP-007 | CA-04 | Media | 2026-10-06 | Sin `/v1/logs`; el párrafo nombra al vigilante y la base | Aprobado | EV-04 | — |

**Correspondencia con el plan:** 7 casos en el plan, 7 acá.

**Qué salió distinto de lo esperado:** ver DEF-01 y DEF-02.

## 3. Verificaciones manuales  ·  [`08·T4`](../../../../../base/08-pruebas.md#t4--protege-los-datos-reales-al-probar)

| # | Qué se verificó | Cómo | Resultado |
|---|---|---|---|
| 1 | La lectura desde cero no cambia los conteos que ya había | Salida de `leer_consumo --desde-cero` | `0 llamada(s)` nuevas en cada proyecto; aparecieron 70 archivos leídos que la lectura por partes no había registrado |

## 4. Defectos encontrados

| ID | Título | Caso que lo destapó | Severidad | Estado | Dónde quedó registrado |
|---|---|---|---|---|---|
| DEF-01 | El `Enmascarador` no tapa claves `sk-ant-...` ni `ANTHROPIC_API_KEY=...` | CP-001 | Alta | Abierto, fuera de esta fase | H-3 del resumen de la sesión y [pendiente 129](../../../EP-005-automatismos-que-no-dependen-de-la-memoria/HU-002-enmascarar-claves/pendientes/129-el-enmascarador-no-reconoce-las-claves-de-anthropic/pendiente.md) |
| DEF-02 | Cambiar la frase de `leer_consumo` rompía una prueba existente | Suite `core.consumo.tests` | Baja | Corregido | §8 |

**Defectos abiertos que se aceptan y por qué:** DEF-01 no es de esta fase: el tapado es de EP-005·HU-002, y esta fase cumple su exigencia, que lo guardado pase por él. Queda como pendiente 129 para que el usuario decida cuándo.

## 5. Veredicto por criterio de aceptación y requisito no funcional

| Exigencia de la HU (`CA-0N` · `RNF-0N`) | Casos que la cubren | Resultado | Cumple |
|---|---|---|---|
| CA-01 | CP-001, CP-002, CP-003 | Aprobados | Sí |
| CA-02 | CP-004 | Aprobado | Sí |
| CA-03 | CP-005 | Aprobado | Sí |
| CA-04 | CP-007 | Aprobado | Sí |
| RNF-01 | CP-001 | Aprobado | Sí |
| RNF-02 | CP-006 | Aprobado | Sí |

## 5.1 Lo que el plan exigía

| Lo que el plan exige | Dónde lo dice | Meta | Resultado | Cumple |
|---|---|---|---|---|
| Cobertura de criterios y requisitos no funcionales | Plan §5 | 100 % | 6 de 6 | Sí |
| Casos críticos y altos ejecutados | Plan §5 | 100 % | 6 de 6 | Sí |

## 6. Veredicto de la fase

**Concepto:** Cumple.

**Justificación:** los cuatro criterios y los dos requisitos no funcionales tienen sus casos aprobados. DEF-01 es del tapado, no de esta fase, y queda como pendiente 129.

## 7. Evidencias

| ID | Tipo | Dónde está |
|---|---|---|
| EV-01 | Salida de `manage.py test core.consumo.tests_lineas` | §2 de este documento |
| EV-02 | Salida de `manage.py test core.consumo.tests_vigilante` | §2 de este documento |
| EV-03 | Salida de `migrate` y `leer_consumo --desde-cero` | §2 de este documento |
| EV-04 | Texto | `proyectos/cimiento/README.md` |

## 8. Ciclos anteriores

| Ciclo | Fecha | Aprobados | Fallidos | Qué cambió entre ciclos |
|---|---|---:|---:|---|
| 1 | 2026-10-06 | 7 | 0 | En las corridas previas, CP-001 falló con una clave `sk-ant-...` (DEF-01, se cambió a una forma conocida) y `core.consumo.tests` falló por la frase de `leer_consumo` (DEF-02, se conservó la frase de antes) |
