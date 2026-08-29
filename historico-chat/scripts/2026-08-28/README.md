# Programas de un solo uso · 2026-08-28

Lo que el agente escribió el 2026-08-28, en la jornada de la `HU-020`. **No se vuelven a correr**: llevan dentro la ruta de la máquina donde corrieron, y miden contra un historial que ya avanzó.

De qué sesión salen: [2026-08-22 · sesion-6](../../2026-08-22-sesion-6.md), que cruzó varios días.

## Qué hizo cada uno

| Programa | Qué hizo |
|---|---|
| `medir-sin-registro.py` | **Mató el arreglo obvio antes de escribirlo.** Midió, sobre los últimos doce commits, en cuántos avisaría una comprobación que hablara de los archivos sin registro: **siete de doce, con hasta 31 archivos de una vez**. Es la medición de `S-072` |
| `t06-cuanto-hablaria.py` | La misma pregunta para el diseño que sí se construyó: **0 de 12**. Imprime su propio límite —hoy hay una sola conversación viva—, para que el cero no se lea de más |
| `sabotajes-hu020.py` | Rompió el registro de siete formas distintas y miró si las pruebas lo cazaban. **Dos se colaron**, y de ahí salieron tres defectos: uno real (escribía carpetas fuera de todo proyecto), una línea muerta y una aserción pegada en la prueba de otro enganche. Son `S-073` y `S-074` |

## La `HU-021` · las 650 pruebas que nada corría

| Programa | Qué hizo |
|---|---|
| `corren-las-pruebas-de-tests.py` | Corrió los 67 archivos **uno por uno**, porque la orden documentada se caía antes de correr nada. **61 en verde, 6 en rojo.** Con `--todos` deja la lista completa: sin los nombres, un rojo nuevo no se distingue de uno de siempre |
| `todos-en-un-proceso.py` | La pregunta que decidió el diseño: **cargados juntos dan las mismas fallas en los mismos archivos**, así que no se estorban y el corredor puede cargarlos de una vez en lugar de arrancar Python 67 veces |
| `t04-donde-cuelga.py` | **Tumbó el enganche que se planeaba.** 9,6 minutos × 245 commits en 14 días = 39,3 horas. Ninguna opción que *corriera* las pruebas cabía en el umbral, así que se cuelga el reclamo |
| `sabotajes-hu021.py` | Los once sabotajes, **cazados los once**. Dos estaban mal armados y uno de esos destapó una prueba que **no podía fallar** |

| Salida | Qué es |
|---|---|
| `linea-base-t00.txt` | El 61/6 **antes** de tocar nada, con los 67 nombrados |
| `t01-con-init.txt` | Lo mismo **con el `__init__.py` puesto**: los mismos 6. La única diferencia era `corredor.py`, que acababa de nacer |
| `salida-internas.txt` | Las 650 al cerrar la fase |

## Las dos salidas guardadas

| Archivo | Qué es |
|---|---|
| `salida-suite.txt` | La corrida completa de las pruebas al cerrar la fase. Es la evidencia `EV-05` del [resultado de pruebas](../../../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-020-el-registro-de-la-sesion-no-depende-de-la-herramienta/A-EP-005-HU-020-el-turno-anota-lo-que-cambio/resultado_pruebas.md) |
| `salida-validar.txt` | La corrida de todos los comprobadores sobre el repositorio, en el mismo momento |

**Van recortadas a lo que alguien lee** —el resumen y lo que falló— y cada una dice con qué comando se reproduce. Enteras pesaban 71 KB y 334 KB, casi todo líneas de avisos de otras fases: **versionar el volcado completo es guardar ruido y llamarlo evidencia.**

**Se guardan porque las tres fallas de la primera corrida enseñaron algo:** las tres venían de un solo enlace roto —un documento que apuntaba a otros dos que todavía no existían—, y sin la salida escrita eso se cuenta de memoria.
