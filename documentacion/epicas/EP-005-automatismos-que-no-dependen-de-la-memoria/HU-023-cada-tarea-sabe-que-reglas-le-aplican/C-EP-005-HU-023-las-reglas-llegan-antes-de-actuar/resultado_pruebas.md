# Resultado de Pruebas · Fase `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar`   ·   `[CAPA 3]`

**Para qué sirve este documento.** Registra qué se ejecutó de verdad y con qué resultado, y de ahí sale el **veredicto** de la fase: si cada criterio de aceptación quedó cumplido o no. Es lo que alimenta el `estado-fase.md` para pasar la puerta de verificación, y la fuente de la sección *Qué se probó* del `funcionalidad_implementada.md`. El diseño de los casos vive en el `plan_pruebas.md` de esta misma fase, que no se modifica al ejecutar: se aprobó antes y así se queda.

## 0. Identificación

| Campo | Valor |
|---|---|
| **Fase** (`02·F12.6`) | `C-EP-005-HU-023-las-reglas-llegan-antes-de-actuar` |
| **HU** | [HU-023](../HU-023-cada-tarea-sabe-que-reglas-le-aplican.md) |
| **Plan de pruebas de origen** | [plan_pruebas.md](plan_pruebas.md), versión 1.0 |
| **Ciclo** | 4 |
| **Fecha de ejecución** | 2026-09-28 |
| **Ejecutado por** | El agente |
| **Ambiente y versión** | El repositorio del estándar, rama `main`, versión 39.6.0 sin commit; carpetas temporales |

## 1. Resumen de la ejecución

| Ciclo | Diseñados | Ejecutados | Aprobados | Fallidos | Bloqueados | No ejecutados |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 4 | 4 | 4 | 0 | 0 | 0 |
| 2 | 10 | 10 | 10 | 0 | 0 | 0 |
| 3 | 10 | 10 | 10 | 0 | 0 | 0 |
| 4 | 10 | 10 | 10 | 0 | 0 | 0 |

## 2. Ejecución caso por caso

**CA-08 · CP-001, que la palabra clave elija las tareas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | «Suba» | `tocar-git` | `tocar-git` |
| 2 | «es sencillo debe entender las reglas no lo que le parezca» | Ninguna más que las de siempre | Ninguna |
| 3 | «como así que entendió que yo quería cambiar el estándar?» | Ninguna más que las de siempre | Ninguna |
| 4 | «Escriba el plan del estándar» | `escribir-documento` | `escribir-documento` |
| 5 | «Apruebo los dos planes. Hágalo» | `trabajar-cadena` | `trabajar-cadena` |
| 6 | Lo que no cupo nombra su archivo | La ruta de `base/reglas-por-tarea/` | `base/reglas-por-tarea/correr-comando.md` (`test_lo_que_no_cupo_dice_en_que_archivo_esta_completo`) |

**CA-09 · CP-002, que ninguna acción pase sin sus reglas leídas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `git commit` sin lecturas | Se detiene y nombra los dos archivos | Cumple |
| 2 | Leídos, repetir | Pasa | Cumple |
| 3 | `python -m unittest pruebas` sin leer | Se detiene; el archivo trae `02·F5` | Cumple |
| 4 | `.md` en `documentacion/epicas/` | `escribir-documento` y `trabajar-cadena` | Cumple |
| 5 | Un `.py` | `cambiar-codigo` | Cumple |
| 6 | `WebFetch` | `ir-afuera` | Cumple |
| 7 | Tarea partida con una parte leída | Pide la que falta | Cumple |
| 8 | Resumen de la conversación | Se vuelve a detener | Cumple |
| 9 | Respuesta sin leer | Se detiene una vez | Cumple |
| 10 | Acción que no calza | Cae en comando o código | Cumple |

**Prueba real en esta sesión:** con el enganche conectado, el primer comando del agente se detuvo pidiendo el archivo de `correr-comando`. El agente lo leyó, con `02·F5` adentro, y el comando pasó y corrió solo las suites de la fase. Lo mismo pasó antes de escribir estos documentos, con `escribir-documento` y `trabajar-cadena`.

**CA-10 · CP-003, que los archivos por tarea no envejezcan**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Escribirlos y correr `validar.py tareas` | Sin fallas | `OK: sin incumplimientos` |
| 2 | En una copia, cambiar una regla sin reescribirlos | Falla nombrando el archivo | Cumple (`test_el_mapa_viejo_falla`); también el archivo que sobra (`test_el_archivo_que_sobra_falla`) |
| 3 | Leer cada parte en una lectura | Cabe | Cumple: la más grande tiene 40.896 caracteres |
| 4 | Contar las reglas de cada archivo | Las del mapa | 18, 14, 51, 127 (70 + 57), 18, 18, 18, 5, 25 y 42 |

**RNF · CP-004, versionado, amarre y pruebas**

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | `VERSION` y `CHANGELOG.md` | `39.6.0`, MENOR | Cumple; `test_la_entrada_del_registro_se_entiende` en OK |
| 2 | `estandar`, `tareas`, `amarre`, `versionado` | Sin fallas | Sin fallas; el amarre cuenta 30 de 90 |
| 3 | Las pruebas de la fase | OK | 157 en OK |

## 2.1 Ciclo 2 · la corrección

El ciclo 1 se cerró con tres cosas que el usuario no autorizó: los archivos por tarea quedaron en la raíz y no en `base/reglas-por-tarea/` como decía el plan; lo leído se olvidaba solo al resumirse la conversación y no en cada interacción; y H-1 se dio por cerrado. Aparecieron además dos defectos: una lectura de un pedazo del archivo contaba como completa, y el agente escribió guiones en la carpeta temporal de la herramienta, fuera del repositorio. El usuario pidió corregir todo.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Los archivos por tarea | En `base/reglas-por-tarea/`, y la carpeta de la raíz ya no existe | Cumple; `comun.EXCLUIDAS` los saca de los recorridos y `validar.py estandar` no los cuenta como repetidos |
| 2 | Un mensaje nuevo del usuario después de leer | Se vuelve a detener | Cumple (`test_con_cada_mensaje_del_usuario_se_vuelve_a_pedir`) |
| 3 | El instalador | `hook_antes.py --modo olvido` en `UserPromptSubmit` | Cumple (`test_el_instalador_olvida_con_cada_mensaje`); también en `.claude/settings.json` del estándar |
| 4 | Leer solo un pedazo | Se sigue deteniendo | Cumple (`test_la_lectura_parcial_no_cuenta`) |
| 5 | Escribir en la carpeta temporal del sistema, con las reglas leídas | Se detiene y dice dónde va el guion | Cumple (`test_escribir_fuera_del_proyecto_se_detiene`) |
| 6 | Escribir en una carpeta hermana con el mismo comienzo de nombre | Cuenta como afuera | Cumple (`test_la_carpeta_hermana_con_el_mismo_comienzo_es_afuera`) |
| 7 | Escribir dentro del proyecto | La ruta no lo detiene | Cumple (`test_escribir_dentro_del_proyecto_no_se_detiene_por_la_ruta`) |
| 8 | Los guiones que quedaron afuera | En `historico-chat/scripts/2026-09-28/`, cada uno con su fila en el README | Cumple |
| 9 | Las pruebas que la corrección toca | OK | 84 en `validadores/tests/` y 79 en `pruebas.py` (`Instalador`, `LasReglasQuePideLaSolicitud`, `ElGuionSeQuedaEnElRepositorio`, `ElTurnoAnotaLoQueCambio`) |
| 10 | `estandar`, `tareas`, `amarre`, `versionado` | Sin fallas | Sin fallas |

**Prueba real en esta sesión:** al resumirse la conversación, el enganche detuvo la primera edición y pidió `base/reglas-por-tarea/cambiar-codigo-1.md`, `-2.md` y `cambiar-estandar.md`; leídos completos, la edición pasó.

## 2.2 Ciclo 3 · la lectura que no traía el texto

Con el ciclo 2 cerrado, el usuario preguntó por qué no funcionaba. La herramienta de lectura no vuelve a mandar un archivo que no cambió: devuelve el aviso «el archivo no cambió desde la última lectura», sin el texto. El enganche lo contaba como lectura y dejaba pasar. El usuario aprobó el arreglo.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Una lectura que devuelve el aviso sin texto | No cuenta | Cumple (`test_el_aviso_de_que_no_cambio_no_cuenta`) |
| 2 | El comando de lectura, sin reglas leídas | Pasa: leer las reglas no pide reglas | Cumple (`test_el_comando_de_lectura_pasa_sin_reglas_leidas`) |
| 3 | Lo que imprime el comando | El archivo entero, entre su marca de inicio y la de fin | Cumple (`test_el_comando_de_lectura_imprime_el_archivo_entero`) |
| 4 | Leer por comando y repetir la acción | Queda anotado y la acción pasa | Cumple (`test_lo_leido_por_comando_se_anota`) |
| 5 | Una salida cortada | No cuenta | Cumple (`test_la_salida_cortada_no_cuenta`) |
| 6 | El comando de lectura con otro encadenado | Se trata como un comando cualquiera | Cumple (`test_un_comando_encadenado_no_es_lectura`) |
| 7 | Cada archivo por tarea | Menos de 30.000 caracteres | Cumple; ahora tienen como máximo 25.000 (`test_cada_archivo_cabe_en_la_salida_de_un_comando`) |
| 8 | El instalador | Anota lo leído con la herramienta de lectura y con los comandos | Cumple (`test_el_instalador_anota_lo_leido_por_comando`) |
| 9 | Las pruebas que el ciclo toca | OK | 63 en `validadores/tests/` y 48 en `pruebas.py` (`Instalador`, `LasReglasQuePideLaSolicitud`) |
| 10 | `estandar`, `tareas`, `amarre`, `versionado` | Sin fallas | Sin fallas |

**Defecto encontrado en el ciclo:** la primera versión buscaba las marcas en la respuesta pasada a JSON, donde las barras de una ruta de Windows salen dobles, y no anotaba nada. Se corrigió buscando en los textos tal como llegan.

**Prueba real en esta sesión:** con el mensaje del usuario se borró lo leído. El agente corrió el comando de lectura de `tocar-git` y quedó anotado en `historico-chat/.leido/`.

## 2.3 Ciclo 4 · sin lectura obligatoria

El usuario descartó el 2026-09-29 la lectura obligatoria: llenaba la conversación de lecturas y no hacía cumplir nada. Pidió que, sin la palabra de `01·C28`, el agente la recuerde y espere, y que las reglas salgan de la respuesta sin que el agente muestre que las lee. Los ciclos 2 y 3 quedan como registro: el enganche que obligaba a leer ya no existe.

| # | Qué hacer | Qué tiene que pasar | Qué salió |
|---|---|---|---|
| 1 | Un mensaje sin palabra de `01·C28` | El aviso con la lista completa y ninguna orden de leer | Cumple (`test_sin_palabra_llega_el_aviso_con_la_lista`) |
| 2 | «Suba» | Las reglas de `tocar-git`, con `00·N2`, sin el aviso | Cumple (`test_con_palabra_llegan_las_reglas_y_no_el_aviso`) |
| 3 | La palabra con tilde o sin ella, y abriendo una frase | Cuenta; en medio de la frase no cuenta | Cumple (`test_la_palabra_cuenta_con_tilde_o_sin_ella_y_al_abrir_una_frase`) |
| 4 | Lo que agrega el editor al mensaje | No cuenta como palabra | Cumple (`test_lo_que_agrega_el_editor_no_cuenta_como_palabra`) |
| 5 | «qué dice 02·F24?», sin palabra | El aviso y el texto de `02·F24` | Cumple (`test_la_regla_citada_en_el_mensaje_llega_entera`) |
| 6 | Escribir fuera del proyecto, en una carpeta hermana y dentro | Se detienen las dos primeras; la tercera pasa | Cumple (tres casos de `NingunaEscrituraSaleDelProyecto`) |
| 7 | Un comando | Pasa sin detenerse | Cumple (`test_un_comando_no_se_detiene`) |
| 8 | El instalador | Solo el freno de escritura de `hook_antes.py` | Cumple (`test_el_instalador_solo_pone_el_freno_de_escritura`) |
| 9 | Las pruebas que el ciclo toca | OK | 63 en `validadores/tests/` y 58 en `pruebas.py` (`Instalador`, `LasReglasQuePideLaSolicitud`, `EngancheDelResumenPorElCaminoReal`) |
| 10 | `estandar`, `tareas`, `amarre`, `versionado` | Sin fallas | Sin fallas; el amarre cuenta 30 de 89 |

**Prueba real en esta sesión:** «ya?» y «vale» recibieron el aviso de `01·C28`, y el agente solo recordó la palabra. «Explique lo que hizo» recibió sus reglas sin ninguna orden de leer archivos. «00·ID9» recibió el aviso y el texto de la regla.

**Defecto encontrado:** «00 id9», escrito con espacio y en minúscula, no trae el texto de la regla; el recuperador solo reconoce la forma `00·ID9`. Queda como pendiente.

## 3. Veredicto

| CA | Veredicto |
|---|---|
| CA-08 | Cumple |
| CA-09 | Cumple, en su versión del ciclo 4 |
| CA-10 | Cumple |

**Concepto de la fase:** Cumple. **Defectos abiertos:** uno, fuera de los CA de la fase: la cita «00 id9» escrita con espacio no trae la regla. Va como pendiente.
