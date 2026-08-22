# Pendiente · Lo que quedó abierto en las sesiones viejas

**Estado:** **decidido** el 2026-08-22, con la orden «haga los dos»; abierto hasta que lo que quedó por construir se construya · anotado 2026-08-15 · sale de escribir hacia atrás los resúmenes del [2026-08-06](../historico-chat/resumenes/2026-08-06/README.md).

| | |
|---|---|
| **Historia de usuario** | No es un ítem, son siete. Cada punto nombra su historia en su párrafo. |

## El problema

Escribir el resumen de una sesión vieja destapa lo que esa sesión dejó preguntado y nadie volvió a mirar. No son defectos nuevos: llevan nueve días ahí, invisibles porque vivían dentro de una transcripción de 90 KB.

Este archivo los junta. Cada uno dice de qué resumen sale.

## Qué falta

**1 · ~~El validador de enlaces da por rotos los enlaces con espacios.~~ · CERRADO el 2026-08-17**, junto con el [55](hecho/los-enlaces-de-ejemplo-no-son-enlaces.md): `enlaces.py` decodifica el destino antes de buscarlo, y hay dos casos que lo fijan — el archivo con espacios resuelve, y el que de verdad no existe se sigue reportando.

~~**1 · El validador de enlaces da por rotos los enlaces con espacios.**~~ Un enlace a un archivo cuyo nombre lleva espacios se escribe con `%20`, y [`enlaces.py`](../validadores/enlaces.py) no lo decodifica antes de buscarlo en disco: lo reporta roto aunque el archivo esté. Se arregla con un `unquote` sobre el destino. **Vive en** [EP-004 · HU-005 — Enlaces y citas](../documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md), su `RN-01`; se hace junto con el [55](hecho/los-enlaces-de-ejemplo-no-son-enlaces.md), que es el mismo falso positivo por el otro lado. El caso que lo destapó salió del repositorio al día siguiente, así que hoy no se ve — pero el validador sigue igual.
→ [el torniquete del histórico · H-7](../historico-chat/resumenes/2026-08-06/el-torniquete-del-historico.md).

**2 · El barrido de candidatas a regla no tiene ni plantilla ni disparador.** El 2026-08-06 se hizo una vez, a mano, y salieron 12 candidatas. Quedaron propuestas dos piezas que no se construyeron: `plantillas/candidatas-a-regla.md` —el formato del análisis— y la regla que obliga a hacer el barrido. Sin disparador, «se hace cuando el usuario lo pida» es un favor, no una norma. La recomendación de entonces: engancharlo al cierre de versión que `M10` ya define. **Vive en** [EP-001 · HU-007 — La regla de las reglas](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md): el barrido es parte de cómo nace una regla.
→ [la anatomía de la regla · H-7](../historico-chat/resumenes/2026-08-06/la-anatomia-de-la-regla.md).

> **Dónde se atascó, medido el 2026-08-18.** No es que falte trabajo: es que la pieza que falta es **una regla nueva en `base/`**, y por [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) eso se construye como fase de su historia. La fase `A` de `EP-001·HU-007` es **retrodocumentación** y excluye escribir reglas nuevas en su propio alcance, así que hace falta una **fase `B`** con su plan aprobado. **Es el mismo sitio donde quedó atascado el [pendiente 16](hecho/primero-que-el-proceso-sirva.md)**, que también pide una meta-regla.
>
> **Y al ir a escribir esa fase, el 2026-08-18, apareció que tampoco cabe ahí.** Los tres criterios de `HU-007` son enrutar al capítulo, rechazar lo atado a un stack y partir la que exige dos cosas. **Ninguno cubre el barrido.** Por `02·F19` el criterio **es** la especificación, así que no falta una fase: falta un criterio, o una historia propia. Las dos son decisión del usuario, y están escritas en el 16.
>
> **Y escribir solo la plantilla no sirve:** este punto dice que sin disparador el barrido *«es un favor, no una norma»*. Una plantilla sin regla que la exija reproduce exactamente el defecto que el punto describe.

**3 · ~~Una sesión que cruza la medianoche queda con el nombre de otro día.~~ · CERRADO el 2026-08-18** — **se queda entera**, y estaba decidido por la máquina desde el principio: el enganche busca la sesión por su marca `<!-- sesion: id -->`, nunca por fecha, así que partirla dejaría media conversación sin marca y la siguiente sesión no la encontraría. Faltaba escribirlo, y ahora está en [`plantillas/historico-chat.md`](../plantillas/historico-chat.md) y en el [README de la carpeta](../historico-chat/README.md). Cada turno lleva su hora real; el resumen sí va al día en que pasaron las cosas, y esa asimetría es a propósito.

~~**3 · Una sesión que cruza la medianoche queda con el nombre de otro día.**~~ El enganche busca la sesión por su marca, no por la fecha, así que sigue escribiendo en el archivo del día en que empezó. La sesión más larga del histórico se llama `2026-08-06` y la mitad de su contenido es del 07. Ni el `README` de la carpeta ni la plantilla dicen qué hacer: si se parte o si se queda entera. **Vive en** [EP-005 · HU-001 — Transcripción de la sesión](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md), que es la historia del archivo que se parte o no.
→ [la anatomía de la regla · H-11](../historico-chat/resumenes/2026-08-06/la-anatomia-de-la-regla.md). Para los resúmenes ya está decidido —van al día en que pasaron las cosas—; para la transcripción, no.

**4 · ~~Renombrar una sesión deja rotos todos los enlaces que la nombran.~~ · CERRADO el 2026-08-17** con el [54](hecho/cerrar-un-pendiente-arrastra-sus-citas.md): [validadores/cerrar.py](../validadores/cerrar.py) arrastra las citas al mover cualquier `.md`, en las dos direcciones. Queda fuera lo que esté fuera del repositorio, que no tiene arreglo desde acá.

~~**4 · Renombrar una sesión deja rotos todos los enlaces que la nombran.**~~ [`historico.py --renombrar`](../validadores/historico.py) mueve el archivo, le cambia el título, corrige su línea del índice y arrastra el resumen — pero no toca a quien la citaba desde fuera. Renombrar seis sesiones del 2026-08-06 dejó **41 enlaces rotos**, casi todos en [`prompts/`](../prompts/README.md), y se arreglaron a mano. La solución ya existe en el repositorio, aplicada a otra cosa: [`citas.py`](../validadores/citas.py) tiene un modo que **repara** las rutas cuando un capítulo se mueve. **Vive en** [EP-005 · HU-008 — Enganche del resumen](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-008-enganche-del-resumen/HU-008-enganche-del-resumen.md), que es donde se cerró el de adentro; el de fuera es su otra mitad.
→ salió de renombrar las sesiones para escribir sus resúmenes, el 2026-08-15.

**5 · ~~Falta la prueba que protege el arranque.~~ · CERRADO el 2026-08-17** — [validadores/tests/test_el_gate_del_arranque_resuelve.py](../validadores/tests/test_el_gate_del_arranque_resuelve.py), tres casos: que el archivo del gate exista, que sea de verdad `F13` —un renombre podría dejarlo apuntando a otra regla y mostrar la orientación equivocada— y que la puerta devuelva algo **por el camino real**, que es la diferencia que importa: la constante puede estar bien y el recorrido no encontrarla igual, que es exactamente cómo se rompió.

~~**5 · Falta la prueba que protege el arranque.**~~ Renombrar un archivo dejó el `GATE` de [`cargador.py`](../validadores/cargador.py) apuntando a una ruta que ya no existía, y ninguna de las 191 pruebas lo detectó: se descubrió a mano. Ese gate es lo que detiene el arranque cuando el proyecto no tiene su estructura base; si no carga, la puerta desaparece en silencio. Una prueba que compruebe que `GATE` resuelve a un archivo existente lo cierra. **Vive en** [EP-005 · HU-009 — Lo que rige cada frase llega puesto](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-009-lo-que-rige-cada-frase-llega-puesto/HU-009-lo-que-rige-cada-frase-llega-puesto.md), que es la historia de ese arranque.
→ [el capítulo 02 al molde · H-5](../historico-chat/resumenes/2026-08-07/el-capitulo-02-al-molde.md). Es lo más barato de esta lista.

**6 · Nadie revisó a qué proyectos les borró la memoria el enganche.** → **Cerrado el 2026-08-16** → [pendientes/hecho/memoria-borrada-por-el-enganche.md](hecho/memoria-borrada-por-el-enganche.md). Salió de acá a pendiente propio (el 39) y se cerró el mismo día: la revisión dio que el único proyecto con el almacén enlazado por *junction* —la condición que dispara el defecto— era `agro-system`, el que lo reportó, y ya se había recuperado. Parecía lo más urgente de todo el backlog mientras vivía dentro de este archivo; leído solo, resultó estar contestado. El texto completo está allá.

**7 · Un checklist anulado que nadie volvió a aplicar.** → **Promovido a pendiente propio el 2026-08-16** → [52 · El sello del checklist caduca con el texto](hecho/el-sello-del-checklist-se-comprueba.md). Salió de acá porque leído solo se ve lo que dentro de esta lista no se veía: no es que a `F13` le falte su checklist, es que **el sello caduca con el texto y nada lo comprueba**, y nadie sabe cuántos más están vencidos. Allá quedan las dos salidas evaluadas y cuál conviene.
→ [la instalación se hace sola · H-3](../historico-chat/resumenes/2026-08-08/la-instalacion-se-hace-sola.md). Se cruza con el [pendiente 19](hecho/ninguna-regla-reprueba-su-propio-checklist.md).

**8 · Huecos chicos que quedaron preguntados y sin respuesta.**

| Qué falta | De dónde sale | Historia donde vive |
|---|---|---|
| Que el instalador **agregue** al `README` heredado del proyecto las secciones nuevas, como ya hace con el `CLAUDE.md`: hoy el mecanismo replica y el texto que lo explica no | [el nombre de la sesión y las marcas de IA · H-3](../historico-chat/resumenes/2026-08-08/el-nombre-de-la-sesion-y-las-marcas-de-ia.md) | [EP-007 · HU-005](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) |
| Si se escribe la regla del español correcto: hoy `01·C8` fija el idioma y nada más — ni variedad, ni ortografía, ni sintaxis | [el nombre de la sesión y las marcas de IA · H-6](../historico-chat/resumenes/2026-08-08/el-nombre-de-la-sesion-y-las-marcas-de-ia.md) | [EP-001 · HU-004](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/HU-004-conducta-de-la-ia.md) |
| ~~La fila de `anatomia/` en la tabla del [`CLAUDE.md`](../CLAUDE.md) §3~~ · **puesta el 2026-08-18**. **Sigue abierto** si el mapa del sitio se comprueba con un validador o se actualiza a mano | [qué hace el agente sin IA · H-3](../historico-chat/resumenes/2026-08-07/que-hace-el-agente-sin-ia.md) | [EP-005 · HU-011](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) |
| ~~La comprobación de `M1` que se podía implementar~~ · **CERRADA el 2026-08-18** — ver abajo. **Sigue abierta** la otra: exige que el proyecto declare su ajuste de capa 3 con una marca fija, y eso cambia el estándar | [reglas con expresiones regulares · H-2](../historico-chat/resumenes/2026-08-07/reglas-con-expresiones-regulares.md) | [EP-004 · HU-011](../documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/HU-011-molde-de-las-reglas.md) |
| Si la dependencia CA→CA entra a la [plantilla de la historia](../plantillas/ciclo-vida-proyectos/04-HU.md) §8 | [granularidad de la fase · H-2](../historico-chat/resumenes/2026-08-07/granularidad-de-la-fase.md) | [EP-003 · HU-002](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) |
| Por qué LocalHub quedó sin sello y AgroSystem sí, en la misma corrida del instalador | [los enganches llegan a dos proyectos · H-2](../historico-chat/resumenes/2026-08-07/los-enganches-llegan-a-dos-proyectos.md) | [EP-007 · HU-007](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/HU-007-revisar-que-falta.md) |
| **Si las fases de EP-001 son plan o retrodocumentación**: planean cosas que ya están escritas en `base/`. Bloquea escribir las seis historias que faltan — 24 documentos | [plan de trabajo de la EP-001 · H-2](../historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md) | [EP-004 · HU-017](../documentacion/epicas/EP-004-comprobacion-automatica/HU-017-inventario-de-hu-sin-fase/HU-017-inventario-de-hu-sin-fase.md) |
| Las tres dudas que dejan bloqueada la fase A de HU-002: si el preámbulo es capa, cuántas capas hay, si «opcional» es marca o capa | [plan de trabajo de la EP-001 · H-3](../historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md) | [EP-001 · HU-002](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-002-capas-y-precedencia/HU-002-capas-y-precedencia.md) |
| ~~El aviso `DOC12` de la fase A de HU-001~~ · **CERRADO el 2026-08-18** — decía `**Origen:**` y ahora dice `**ORIGEN**` con su enlace a `DOC12` y su marca de funcionalidad nueva | [plan de trabajo de la EP-001 · H-5](../historico-chat/resumenes/2026-08-14/plan-de-trabajo-de-la-ep-001.md) | [EP-004 · HU-004](../documentacion/epicas/EP-004-comprobacion-automatica/HU-004-forma-de-los-documentos/HU-004-forma-de-los-documentos.md) |
| El índice **por temáticas** del histórico: una sesión trata varios temas y por el título no se encuentran | [índice temático del histórico · H-1](../historico-chat/resumenes/2026-08-14/indice-tematico-del-historico.md) | [EP-005 · HU-001](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md) |
| Qué manda entre el brief y el histórico cuando se contradicen | [índice temático del histórico · H-5](../historico-chat/resumenes/2026-08-14/indice-tematico-del-historico.md) | [EP-001 · HU-002](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-002-capas-y-precedencia/HU-002-capas-y-precedencia.md) |
| ~~Que `02·F20` —parar y proponer— choca con corregir el defecto que uno mismo detecta.~~ **CERRADO el 2026-08-18** — [`02·F24`](../base/02-flujo-de-trabajo/reglas/F24-el-defecto-del-estandar-se-reporta-no-se-corrige.md) dice a dónde va lo propuesto cuando es del estándar: `F20` para, `F24` enruta | [regla de respaldo · H-6](../historico-chat/resumenes/2026-08-12/regla-de-respaldo-de-las-reglas-de-proyecto.md) | [EP-007 · HU-008](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-008-el-proyecto-reporta-al-estandar/HU-008-el-proyecto-reporta-al-estandar.md) |

## El límite

Solo entra acá lo que quedó **abierto** en una sesión vieja y sigue abierto hoy. Lo que se resolvió después, aunque fuera en otra sesión, queda anotado en su resumen y no llega a este archivo.

**El [31](hecho/los-resumenes-de-las-sesiones-viejas.md) ya está cerrado**, así que esta lista no crece más por ese lado: son los 33 resúmenes completos. Lo que entre de aquí en adelante sale de sesiones nuevas, no de las viejas.


---

# La comprobación de `M1` — hecha el 2026-08-18

**`20·M1` dice que un nivel nunca contradice al de arriba.** Eso no lo puede juzgar un programa: exige leer las dos reglas y entenderlas.

**Lo que sí se puede juzgar es la marca.** Una regla que se declara `[BLINDADA]` **viviendo fuera del capítulo `00`** no está contradiciendo un nivel: se lo está **saltando**. Queda por encima de las demás sin haber pasado por el núcleo, y eso se ve sin entender qué dice.

Está en `validar.py metareglas`, y hoy da cero: las seis `[BLINDADA]` viven donde deben.

## El ancla, que es lo que decide si el control sirve

La sesión del [2026-08-07](../historico-chat/resumenes/2026-08-07/reglas-con-expresiones-regulares.md) ya había dejado escrito el detalle, y por eso no hubo que redescubrirlo:

> La palabra `BLINDADA` sale en **seis archivos**, casi siempre en prosa. Anclando al **encabezado de la regla** se descartan todos los falsos positivos de una.

**Y el porqué, que vale más que el arreglo:** *«un validador que reporta de más se termina apagando, y un control apagado es peor que ninguno porque figura como cubierto»*. Hay un caso de prueba dedicado a eso: la palabra en la prosa **no** dispara nada.

## Lo que no se hizo, y por qué

La otra mitad —que la capa 3 declare su ajuste con una marca fija— **cambia el estándar**: obliga a los proyectos a escribir algo que hoy no escriben. Es decisión del usuario y sigue abierta.


---

# Lo que quedaba, resuelto  ·  2026-08-22

El usuario ordenó resolverlo. **Lo primero fue volver a medir**, porque este archivo se escribió el 2026-08-15 y el repositorio cambió desde entonces (es la lección de la señal [S-020](../documentacion/senales.md)). De los once puntos abiertos, **siete estaban contestados por lo que ya está escrito o construido**; los otros cuatro piden trabajo, y va cada uno con su decisión.

## Las que el repositorio ya contesta

| # | Duda | Qué dice el repositorio hoy |
|---|---|---|
| **Capas · 1** | ¿El preámbulo es una capa? | **No.** Los dos capítulos de preámbulo (`00 · Identidad y rol` y `20 · Meta-reglas`) llevan su propia marca `[PREÁMBULO]` en la cabecera, y el `20` declara su límite: *«son de procedimiento, nunca de fondo; no autorizan nada ni relajan nada»*. Una capa ordena qué gana ante un choque; el preámbulo no entra en ese orden porque no exige fondo |
| **Capas · 2** | ¿Cuántas capas hay? | **Cuatro niveles**, y ya está escrito en [`20·M1`](../base/20-meta-reglas/reglas/M1-la-jerarquia-tiene-cuatro-niveles-y-un-solo-orden.md) y en la tabla de [`base/README.md`](../base/README.md): `[CAPA 1]` núcleo, `[CAPA 2]` convenciones, `[CAPA 2 · opt-in]` y `[CAPA 3]` proyecto. La duda nació cuando la capa del proyecto no existía; hoy existe |
| **Capas · 3** | ¿«Opcional» es marca o capa? | **Marca dentro de la capa 2**, y así está construido: los capítulos `17`, `18`, `19`, `21` y `22` llevan `[CAPA 2 · opt-in]`. No es otra capa porque no cambia quién gana ante un choque: cambia si la regla aplica |
| **EP-001** | ¿Las fases de EP-001 son plan o retrodocumentación? | **Retrodocumentación**, y las fases lo dicen en su propio nombre: `A-EP-001-HU-003-retrodocumentar-el-nucleo-blindado` y así las demás. Lo que sigue vivo no es la pregunta: es que 34 de esas fases están detenidas, y eso es el [59](59-las-42-dudas-que-detienen-26-fases.md) |
| **Español correcto** | ¿Se escribe la regla? | **No hace falta una regla nueva.** [`01·C8`](../base/01-conducta.md#c8--habla-el-idioma-del-proyecto) fija el idioma, [`01·C20`](../base/01-conducta.md#c20--la-palabra-de-otro-idioma-se-traduce-y-si-no-se-puede-se-explica) exige traducir el término que no esté en él, y [`00·ID7`](../base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md) exige que se entienda. Una regla de ortografía y sintaxis correctas es de las que [`20·M19`](../base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) desaconseja: no hay forma de comprobarla y ya se cumple |
| **LocalHub sin sello** | ¿Por qué quedó sin sello y AgroSystem sí? | **No se puede investigar desde acá y ya no hace falta.** El registro de proyectos vive hoy en la base de datos de la interfaz, y el sello lo pone `instalar.py` al correr; cualquier proyecto sin sello se resuelve volviendo a correr el instalador, que es lo que la [HU-007 de EP-007](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-007-revisar-que-falta/HU-007-revisar-que-falta.md) ya comprueba con `validar.py checklist` |
| **`M1` · marca de capa 3** | ¿Se exige que el proyecto marque su ajuste? | **No se agrega la exigencia.** Obligaría a todos los proyectos instalados a escribir algo que hoy no escriben, a cambio de comprobar algo que ya se ve: un ajuste de capa 3 vive en el catálogo del proyecto y [`20·M16`](../base/20-meta-reglas/reglas/M16-toda-regla-de-proyecto-nombra-la-regla-de-base-que-concreta.md) ya obliga a que nombre la regla de base que concreta. La marca sería una segunda forma de decir lo mismo |

## Las cuatro que piden trabajo, con su decisión

| # | Qué falta | Decisión | Dónde se construye |
|---|---|---|---|
| **2** | El barrido de candidatas a regla no tiene ni molde ni disparador | **Se construye, y el disparador es el cierre de versión**, que es donde el barrido tiene sentido: lo que el usuario pidió dos veces en el tramo se mira antes de publicar. Nace el molde y la meta-regla que lo exige | Fase `C` de [EP-001 · HU-007](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md) |
| **8a** | El instalador no agrega al `README` heredado las secciones nuevas, como sí hace con el `CLAUDE.md` | **Se construye igual que el del `CLAUDE.md`**: aditivo, preserva lo propio y reporta qué agregó. Es el mismo mecanismo, aplicado al otro archivo | Fase de [EP-007 · HU-005](../documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-005-no-pisar-lo-escrito/HU-005-no-pisar-lo-escrito.md) |
| **8b** | El mapa del sitio de [`anatomia/`](../anatomia/mapa-del-sitio.md) se actualiza a mano | **Se comprueba con un validador**, no se actualiza a mano: un mapa que envejece en silencio es peor que no tenerlo, y el precedente está construido (`test_el_mapa_del_amarre_no_envejece.py` hace exactamente eso con el otro mapa) | Fase de [EP-005 · HU-011](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-011-donde-termina-el-estandar/HU-011-donde-termina-el-estandar.md) |
| **8c** | Si la dependencia CA→CA entra a la plantilla de la historia | **Entra, como columna opcional de la tabla de fases**, no como sección nueva: una historia con criterios independientes deja la columna vacía y no paga nada | Fase de [EP-003 · HU-002](../documentacion/epicas/EP-003-documentos-modelo-y-procedimientos/HU-002-modelos-del-encargo/HU-002-modelos-del-encargo.md) |
| **8d** | Qué manda entre el brief y el histórico cuando se contradicen | **Manda el brief**, y el histórico dice de dónde salió: el brief es lo acordado hoy y el histórico es lo que se dijo alguna vez. Cuando chocan, lo que hay es un brief desactualizado o una decisión sin registrar, y las dos se arreglan escribiendo el brief. No necesita regla nueva: es el mismo orden que [`20·M6`](../base/20-meta-reglas/reglas/M6-ante-un-conflicto-el-desempate-es-este-y-en-este-orden.md) fija, con lo específico ganándole a lo general | Se escribe al construir el 8a |
| **8e** | El índice por temáticas del histórico | **Se construye**, generado, no a mano: el índice por título ya existe y el temático se saca leyendo los resúmenes, que es donde están los temas | Fase de [EP-005 · HU-001](../documentacion/epicas/EP-005-automatismos-que-no-dependen-de-la-memoria/HU-001-transcripcion-de-la-sesion/HU-001-transcripcion-de-la-sesion.md) |

**Ninguna de estas seis se anota y se deja:** se bajan a fase y se construyen, que es lo que [`02·F23`](../base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) pide. Lo que quede sin construir al cerrar la sesión queda dicho acá, con su nombre.
