# Pendiente · Lo que quedó abierto en las sesiones viejas

**Estado:** abierto · anotado 2026-08-15 · sale de escribir hacia atrás los resúmenes del [2026-08-06](../historico-chat/resumenes/2026-08-06/README.md).

## El problema

Escribir el resumen de una sesión vieja destapa lo que esa sesión dejó preguntado y nadie volvió a mirar. No son defectos nuevos: llevan nueve días ahí, invisibles porque vivían dentro de una transcripción de 90 KB.

Este archivo los junta. Cada uno dice de qué resumen sale.

## Qué falta

**1 · El validador de enlaces da por rotos los enlaces con espacios.** Un enlace a un archivo cuyo nombre lleva espacios se escribe con `%20`, y [`enlaces.py`](../validadores/enlaces.py) no lo decodifica antes de buscarlo en disco: lo reporta roto aunque el archivo esté. Se arregla con un `unquote` sobre el destino. El caso que lo destapó salió del repositorio al día siguiente, así que hoy no se ve — pero el validador sigue igual.
→ [el torniquete del histórico · H-7](../historico-chat/resumenes/2026-08-06/el-torniquete-del-historico.md).

**2 · El barrido de candidatas a regla no tiene ni plantilla ni disparador.** El 2026-08-06 se hizo una vez, a mano, y salieron 12 candidatas. Quedaron propuestas dos piezas que no se construyeron: `plantillas/candidatas-a-regla.md` —el formato del análisis— y la regla que obliga a hacer el barrido. Sin disparador, «se hace cuando el usuario lo pida» es un favor, no una norma. La recomendación de entonces: engancharlo al cierre de versión que `M10` ya define.
→ [la anatomía de la regla · H-7](../historico-chat/resumenes/2026-08-06/la-anatomia-de-la-regla.md).

**3 · Una sesión que cruza la medianoche queda con el nombre de otro día.** El enganche busca la sesión por su marca, no por la fecha, así que sigue escribiendo en el archivo del día en que empezó. La sesión más larga del histórico se llama `2026-08-06` y la mitad de su contenido es del 07. Ni el `README` de la carpeta ni la plantilla dicen qué hacer: si se parte o si se queda entera.
→ [la anatomía de la regla · H-11](../historico-chat/resumenes/2026-08-06/la-anatomia-de-la-regla.md). Para los resúmenes ya está decidido —van al día en que pasaron las cosas—; para la transcripción, no.

**4 · Renombrar una sesión deja rotos todos los enlaces que la nombran.** [`historico.py --renombrar`](../validadores/historico.py) mueve el archivo, le cambia el título, corrige su línea del índice y arrastra el resumen — pero no toca a quien la citaba desde fuera. Renombrar seis sesiones del 2026-08-06 dejó **41 enlaces rotos**, casi todos en [`prompts/`](../prompts/README.md), y se arreglaron a mano. La solución ya existe en el repositorio, aplicada a otra cosa: [`citas.py`](../validadores/citas.py) tiene un modo que **repara** las rutas cuando un capítulo se mueve.
→ salió de renombrar las sesiones para escribir sus resúmenes, el 2026-08-15.

**5 · Falta la prueba que protege el arranque.** Renombrar un archivo dejó el `GATE` de [`cargador.py`](../validadores/cargador.py) apuntando a una ruta que ya no existía, y ninguna de las 191 pruebas lo detectó: se descubrió a mano. Ese gate es lo que detiene el arranque cuando el proyecto no tiene su estructura base; si no carga, la puerta desaparece en silencio. Una prueba que compruebe que `GATE` resuelve a un archivo existente lo cierra.
→ [el capítulo 02 al molde · H-5](../historico-chat/resumenes/2026-08-07/el-capitulo-02-al-molde.md). Es lo más barato de esta lista.

**6 · Nadie revisó a qué proyectos les borró la memoria el enganche.** → **Cerrado el 2026-08-16** → [hecho/memoria-borrada-por-el-enganche.md](hecho/memoria-borrada-por-el-enganche.md). Salió de acá a pendiente propio (el 39) y se cerró el mismo día: la revisión dio que el único proyecto con el almacén enlazado por *junction* —la condición que dispara el defecto— era `agro-system`, el que lo reportó, y ya se había recuperado. Parecía lo más urgente de todo el backlog mientras vivía dentro de este archivo; leído solo, resultó estar contestado. El texto completo está allá.

**7 · Un checklist anulado que nadie volvió a aplicar.** Al reescribir [`F13`](../base/02-flujo-de-trabajo/reglas/F13-deja-la-estructura-base-puesta-antes-de-trabajar.md) el 2026-08-08, su bloque de checklist quedó anulado y se dejó anotado «a re-aplicar en el próximo repaso». No se hizo. El fondo es más grande que esa regla: **el sello caduca con el texto y nada lo comprueba**, así que un checklist puede seguir diciendo CUMPLE sobre una regla que ya no es la que se evaluó.
→ [la instalación se hace sola · H-3](../historico-chat/resumenes/2026-08-08/la-instalacion-se-hace-sola.md). Se cruza con el [pendiente 19](19-el-capitulo-20-no-se-cumple-a-si-mismo.md).

**8 · Huecos chicos que quedaron preguntados y sin respuesta.**

| Qué falta | De dónde sale |
|---|---|
| Que el instalador **agregue** al `README` heredado del proyecto las secciones nuevas, como ya hace con el `CLAUDE.md`: hoy el mecanismo replica y el texto que lo explica no | [el nombre de la sesión y las marcas de IA · H-3](../historico-chat/resumenes/2026-08-08/el-nombre-de-la-sesion-y-las-marcas-de-ia.md) |
| Si se escribe la regla del español correcto: hoy `01·C8` fija el idioma y nada más — ni variedad, ni ortografía, ni sintaxis | [el nombre de la sesión y las marcas de IA · H-6](../historico-chat/resumenes/2026-08-08/el-nombre-de-la-sesion-y-las-marcas-de-ia.md) |
| La fila de `anatomia/` en la tabla del [`CLAUDE.md`](../CLAUDE.md) §3, y decidir si el mapa del sitio se comprueba con un validador o se actualiza a mano | [qué hace el agente sin IA · H-3](../historico-chat/resumenes/2026-08-07/que-hace-el-agente-sin-ia.md) |
| Las dos comprobaciones de `M1` que ya se pueden implementar en `metareglas.py` | [reglas con expresiones regulares · H-2](../historico-chat/resumenes/2026-08-07/reglas-con-expresiones-regulares.md) |
| Si la dependencia CA→CA entra a la [plantilla de la historia](../plantillas/HU.md) §8 | [granularidad de la fase · H-2](../historico-chat/resumenes/2026-08-07/granularidad-de-la-fase.md) |
| Por qué LocalHub quedó sin sello y AgroSystem sí, en la misma corrida del instalador | [los enganches llegan a dos proyectos · H-2](../historico-chat/resumenes/2026-08-07/los-enganches-llegan-a-dos-proyectos.md) |
| **Si las fases de EP-001 son plan o retrodocumentación**: planean cosas que ya están escritas en `base/`. Bloquea escribir las seis historias que faltan — 24 documentos | [plan de trabajo de la EP-001 · H-2](../historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md) |
| Las tres dudas que dejan bloqueada la fase A de HU-002: si el preámbulo es capa, cuántas capas hay, si «opcional» es marca o capa | [plan de trabajo de la EP-001 · H-3](../historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md) |
| El aviso `DOC12` de la fase A de HU-001: dice `**Origen:**` donde la plantilla pide `**ORIGEN**` | [plan de trabajo de la EP-001 · H-5](../historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md) |
| El índice **por temáticas** del histórico: una sesión trata varios temas y por el título no se encuentran | [índice temático del histórico · H-1](../historico-chat/resumenes/2026-08-14/indice-tematico-del-historico.md) |
| Qué manda entre el brief y el histórico cuando se contradicen | [índice temático del histórico · H-5](../historico-chat/resumenes/2026-08-14/indice-tematico-del-historico.md) |
| Que `02·F20` —parar y proponer— choca con corregir el defecto que uno mismo detecta | [regla de respaldo · H-6](../historico-chat/resumenes/2026-08-12/regla-de-respaldo-de-las-reglas-de-proyecto.md) |

## El límite

Solo entra acá lo que quedó **abierto** en una sesión vieja y sigue abierto hoy. Lo que se resolvió después, aunque fuera en otra sesión, queda anotado en su resumen y no llega a este archivo.

**El [31](31-los-resumenes-de-las-sesiones-viejas.md) ya está cerrado**, así que esta lista no crece más por ese lado: son los 33 resúmenes completos. Lo que entre de aquí en adelante sale de sesiones nuevas, no de las viejas.
