# Los porqués que se recortaron al molde

**Qué es esto.** `20·M5` da cuatro líneas por regla y manda el porqué a `notas/`. Desde el 2026-08-22 (pendiente 19) las reglas que se recortan al molde dejan acá lo que sobraba: no era exigencia sino explicación, y no se pierde.

## Capítulo 00

| Regla | Lo que se recortó |
|---|---|
| `00·ID5` | Que las seis cosas quedan fuera «por definición del rol, no por falta de permiso puntual»; la regla conserva la lista y que cada una se pide aparte. |
| `00·ID7` | «E idealmente un niño», y que el ejemplo se agrega solo cuando aclara; que la documentación técnica también entra sin perder precisión ya lo dice el límite del dato exacto. |
| `00·ID8` | La enumeración «documentación, manual, informe»: lo que cuenta es que una persona lo lea como trabajo terminado. |
| `00·ID9` | «Extenderse no es explicar mejor: lo largo no se lee, y lo que no se lee no comunicó nada.» Es el porqué de toda la regla. |

## Capítulo 01

| Regla | Lo que se recortó |
|---|---|
| `01·C5` | Que una explicación larga «todavía no se entendió» quedó dicho más corto; el porqué de fondo, que lo largo no se lee, ya lo dice [`00·ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md). |
| `01·C21` | «Nunca la supongas»: suponer el dato que falta es justo lo que la regla prohíbe al pedir que se pregunte. |
| `01·C22` | El desglose de qué cuenta como reintentar; la regla conserva las dos salidas, corregir la llamada o preguntar qué cambiarle. |

## Capítulo 02

Doce reglas del flujo de trabajo pasaban del molde con el sello en ✅. Lo que salió de cada una:

| Regla | Lo que se recortó |
|---|---|
| `02·F0` | «se omite por tamaño» y «si te piden un paso»: la exigencia ya dice que ningún eslabón se salta, grande o chico. |
| `02·F8` | El nombre del archivo descubierto («el archivo Y») y «se espera OK explícito»: esperar el OK ya lo dice la frase. |
| `02·F9` | «dentro del plan»: que la subdivisión se proponga antes de aprobar la ubica sola. |
| `02·F10` | Que preguntar «¿está en prod?» solo sirva para elegir entre editar la migración original o crear una nueva; es el porqué de asumir que sí lo está. |
| `02·F11` | «el diferimiento se documenta en la especificación» y la remisión a `F12` por cuántas HU cubre una fase: eso lo fija `F12`, no esta. |
| `02·F14` | «y qué ajusta la capa 3 de cada una»: está en el capítulo, que es donde se leen las trece. |
| `02·F16` | La lista de verbos vagos («ajustar», «revisar», «mejorar») y el ejemplo de alcance abierto; el ejemplo de la regla los muestra. |
| `02·F17` | Las marcas `TBD` y `?`, y la remisión a la línea base y la matriz de dependencias del refactor, que viven en el capítulo. |
| `02·F20` | La lista de lo que «convendría» agregar se acortó, y la remisión a `01·C3`: que una pregunta no autoriza a editar ya lo dice la frase. |
| `02·F22` | «una por cada HU» quedó «una por HU», y la remisión a `F12` y a la mecánica del `CLAUDE.md`, que ya están en sus reglas. |
| `02·F23` | «con todo lo que una fase lleva» y la remisión a `F12`: qué lleva una fase lo fija el capítulo. |
| `02·F26` | «de la propuesta» y «cada épica cita los ítems que cubre», que es la otra cara de que la que no baje de ninguno no arranca. |

## Capítulos 18 y 19

| Regla | Lo que se recortó |
|---|---|
| `18·DP8` | «La identidad del agente es desarrollador senior, no SRE.» Operar el sistema vivo, vigilar tableros y responder incidentes en caliente es del humano; la regla solo conserva que lo prepara y espera la autorización. |
| `19·OB1` | «Sin estructura, un log a escala no se puede buscar ni agregar.» Es el motivo de exigir datos en vez de texto libre. |
| `19·OB3` | «Una alerta que se ignora siempre es peor que ninguna.» Es el motivo de alertar por síntoma y no por ruido: el ruido enseña a silenciar. |
| `19·OB5` | El tipo de señal sugerido (`error-resuelto` o `aprendizaje`) y el molde del postmortem; la regla conserva que se escribe y que se registra. |
| `19·OB6` | «La identidad es desarrollador senior, no SRE de guardia.» El mismo porqué de `DP8`, dicho desde la operación. |

Lo que no se recortó en ninguna: la exigencia, el ejemplo y las dependencias declaradas.
