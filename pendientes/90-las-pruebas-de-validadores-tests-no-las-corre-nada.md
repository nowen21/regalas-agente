# Pendiente · Las 650 pruebas de `validadores/tests/` no las corre nada

| Items | Lo que se debe hacer |
|---|---|
| **Historia de usuario** | [EP-005 · HU-021 — Las pruebas que existen se corren](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-021-las-pruebas-que-existen-se-corren/HU-021-las-pruebas-que-existen-se-corren.md) |

**Prioridad:** `P0` — se está perdiendo algo, y el daño se sigue produciendo cada día.

**De dónde sale:** el 2026-08-28, buscando qué prueba debía haber cazado que la lista de exentos del detector de secretos estuviera seis días vieja. La prueba existe y está escrita hace diez días: `test_el_estandar_no_se_reporta_a_si_mismo`. **Nunca se corrió.**

## Qué pasa

`validadores/tests/` tiene **67 archivos y 650 pruebas**. Ningún comando del repositorio los ejecuta.

| Quién podría correrlos | Qué hace en realidad |
|---|---|
| `python validadores/pruebas.py` | Corre sus **515 propias** pruebas. No descubre la carpeta |
| `python -m unittest discover -s validadores/tests` | **Se cae antes de correr nada**: `ImportError: Start directory is not importable`, porque falta el `__init__.py`. Es la orden que el registro de cambios documenta desde la primera prueba del repositorio |
| `validar.py suite` | Busca `pytest`, `phpunit` o `npm test` en el proyecto. Ninguno aplica acá |
| El enganche de `pre-commit` | Corre comprobadores, no pruebas |

**Así que hay dos suites y el repositorio solo conoce una.** Cada fase cierra diciendo «la suite completa, en verde» y eso es cierto de las 515; de las otras 650 nadie afirmó nada, ni para bien ni para mal.

## Lo que se encontró al correrlas a mano

**61 archivos en verde, 6 en rojo.** Corridos uno por uno, y también los 650 juntos en un solo proceso: **los mismos seis**, 8 fallas, 0 errores. **No se estorban entre ellos**, así que un corredor puede cargarlos todos junto sin darle a cada uno su propio proceso.

| Archivo en rojo | Qué está diciendo |
|---|---|
| `test_el_texto_del_enlace_dice_donde_vive` | **98 enlaces entre carpetas mal escritos**, donde el criterio exige 0 |
| `test_la_frontera_del_adaptador` | `hook_estacion.py` se quedó en `validadores/` y su sitio es `adaptadores/` |
| `test_ninguno_termina_en_silencio` | 3 fallas: códigos de salida, y módulos que no dicen por dónde se corren |
| `test_el_mapa_del_amarre_no_envejece` | El recuento del programa no coincide con el del mapa |
| `test_el_andamio_levanta_la_historia_y_el_pendiente` | El andamio escribe contenido donde el criterio pide que no |
| `test_la_corrida_completa_en_una_linea` | 1 falla |

**Varias son de trabajo de estos días.** Ninguna se vio.

## Por qué importa

Una prueba que nadie corre **es peor que no tenerla**: figura como cobertura. Las 650 aparecen en el `CHANGELOG` fase tras fase —«9 casos», «23 casos», «15 casos»— como evidencia de que algo quedó comprobado, y esa evidencia lleva semanas sin ejecutarse.

**Y el daño ya se midió.** La lista de exentos de `secretos.py` quedó vieja el 2026-08-22 y `validar.py todo` estuvo **seis días en rojo** diciendo «posible secreto en el código» — el mismo mensaje que daría una fuga real. La prueba que lo cazaba estaba escrita. Es `S-075`.

## Qué habría que arreglar

Tres cosas, y la tercera es la que evita que vuelva:

1. **Que la carpeta se pueda correr con una orden**, y que esa orden sea la que está documentada.
2. **Que la corrida esté colgada de algo**, no de que alguien se acuerde. Sin esto, el punto 1 dura hasta la próxima semana ocupada.
3. **Que los seis rojos se arreglen o se declaren.** Un rojo que se arrastra sin decisión escrita vuelve a apagar el semáforo, que es de donde venimos.

**Lo que no se debe hacer:** meter las 650 dentro de `pruebas.py`. `02·F5` dice que una fase corre las suites que toca, **no la suite completa**, y juntar las dos empujaría a lo contrario. Lo que falta no es correr más en cada fase: es que exista la orden, y que alguien la corra entre commit y commit.

## Regla que esto toca

`08·T5` — ejecuta y reporta. Y `02·F5`, que hoy no se puede cumplir sobre esta carpeta porque no hay forma de seleccionar un subconjunto de una suite que no carga.

## Cómo se midió

[historico-chat/scripts/2026-08-28/](../historico-chat/scripts/2026-08-28/) — `corren-las-pruebas-de-tests.py` (uno por uno) y `todos-en-un-proceso.py` (los 650 juntos, para decidir si se estorban).
