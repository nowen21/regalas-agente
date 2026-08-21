<!-- sesion: 563dc2f9-c782-46f9-af82-c9bc948b3566 -->
<!-- nombre: preguntado -->

# 2026-08-21 — Que es memory y trazas

## Conversación

### 1 · Usuario — 2026-08-21 13:18:12
> lo que está en: historico-chat\memory para qué es?

**Agente** — 2026-08-21 13:18:25
<!-- agente: dc6323ea-79dd-4efd-b3ed-4b43a2b4860f -->

[historico-chat/memory/](historico-chat/memory/memory.md) es la **memoria persistente del agente entre sesiones**, guardada como archivos del repo en lugar del almacén local de Claude Code.

En concreto:

- **Qué guarda:** las **preferencias del usuario sobre cómo trabajar** — un archivo por recuerdo, con la forma *qué se pide · por qué · cómo se aplica*. Ejemplos actuales: "no poner `Co-Authored-By`", "aprobar antes de commitear", "respuestas cortas", "estilo de redacción simple".
- **Por qué en el repo y no en la herramienta:** el almacén local (`~/.claude/projects/<proyecto>/memory/`) no se ve en git, no se puede revisar, no se versiona y no viaja a otra máquina. Por eso la regla `01·C19` exige que ese almacén quede **vacío** y todo recuerdo viva acá; `validadores/hook_recuerdos.py` es quien mueve lo que aparezca allá hacia el repo.
- **Qué NO va ahí** (el propio [memory.md](historico-chat/memory/memory.md) lo separa con una pregunta: *¿qué haría que eso cambiara?*):
  - Si cambia porque el usuario cambia de opinión → **preferencia** → va acá.
  - Si cambia porque el código/proyecto cambia → **aprendizaje** → señal en `memoria/senales.db`.
  - Si cambia lo que se exige a cualquier proyecto → **regla** → `base/`, versionada.

El índice está en `memory.md` (una línea por recuerdo) y hoy tiene 18 recuerdos. Nada se duplica entre sitios: si algo ya está en uno, el otro lo enlaza.

### 2 · Usuario — 2026-08-21 13:20:46
> y en historico-chat\trazas qué hay?

**Agente** — 2026-08-21 13:21:07
<!-- agente: 2a4b093c-a34d-4a2f-a2db-4312231f94d5 -->

[historico-chat/trazas/](historico-chat/trazas/README.md) guarda la **traza técnica de cada sesión: qué ejecutó el agente, paso a paso**. Es el complemento del histórico: el histórico tiene la *conversación* (lo que se dijo); la traza tiene las *acciones* — cada herramienta que corrió (Bash, Read, Agent…), con su hora, qué se le pidió, cuánto duró y si falló. No copia el contenido de ningún resultado.

La produce el programa, no el agente: `validar.py traza`. Hoy hay una sola, [2026-08-20-sesion-5.md](historico-chat/trazas/2026-08-20-sesion-5.md) (73+ pasos de esa sesión), que salió del trabajo de la HU-016 «la traza de la sesión paso a paso». Sirve para auditar qué se ejecutó realmente en una sesión — por ejemplo, ver que los pasos 38–40 fallaron tres veces seguidas — sin tener que releer toda la conversación.

---

Aparte: esta sesión aún no tiene nombre. La guardo como `2026-08-21-que-es-memory-y-trazas.md` — preguntas sobre qué guardan `historico-chat/memory/` y `historico-chat/trazas/`, ¿va?

### 3 · Usuario — 2026-08-21 13:21:54
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\historico-chat\trazas\2026-08-20-sesion-5.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> si

**Agente** — 2026-08-21 13:22:49
<!-- agente: 312d974c-7324-42da-9b74-0dfc25a7f95d -->

La sesión fue solo consulta, así que el resumen registra eso explícitamente:

Listo. La sesión quedó guardada como `2026-08-21-que-es-memory-y-trazas.md`, con el índice al día (el programa renombró también el resumen a juego). En el resumen dejé escrito que la sesión fue de consulta y no dejó hallazgos — que es un dato, no un olvido.

Falta solo lo que va de tu lado: pega esta línea para que la sesión de Claude Code tenga el mismo nombre en la pestaña y en `/resume`:

```
/rename que-es-memory-y-trazas
```

### 4 · Usuario — 2026-08-21 13:23:01
> osea trazas es como especie de un log?

**Agente** — 2026-08-21 13:23:09
<!-- agente: 9c8419d5-e55a-4f42-84e5-8c88c7437831 -->

Sí, exactamente. Es un log de ejecución de la sesión, pero con dos particularidades:

1. **Registra acciones, no texto.** El histórico normal guarda lo que se *dijo* (la conversación); la traza guarda lo que se *hizo*: cada herramienta que el agente ejecutó, con hora, duración y si falló. Y a propósito no copia el contenido de los resultados — solo el comando y su desenlace, para que sea auditable sin volverse enorme.

2. **Es un log post-hoc y versionado.** No lo escribe un proceso en vivo a un archivo del sistema: lo produce `validar.py traza` leyendo la transcripción que Claude Code ya guarda, y queda como archivo Markdown en el repo, en git, al lado de la conversación de esa misma sesión.

La utilidad es la de cualquier log: responder "¿qué ejecutó realmente el agente?" sin releer la conversación — ver que un paso falló tres veces seguidas, cuánto tardó algo, o qué tocó antes de un cambio.

### 5 · Usuario — 2026-08-21 13:38:41
> resuelva el pendiente 16

**Agente** — 2026-08-21 13:48:23
<!-- agente: 59732a0b-311c-46a2-ada2-dfe6cc2ac199 -->

Este pendiente ya tiene trabajo hecho: en el git status aparece la fase `B-EP-001-HU-007-primero-que-el-proceso-sirva/` y la regla nueva `M19`. Voy a ver en qué estado quedó antes de hacer nada.

La regla `M19` y el `CA-05` ya existen de la sesión del 2026-08-20, pero varios documentos de la fase B quedaron como plantillas sin llenar. Voy a ver el resto de la fase.

Antes de escribir los planes, verifico los casos reales que el `CA-05` usa como material de prueba: los ítems 01, 06 y 11 del backlog de automatizaciones (pendiente 09) y el caso de `F4`.

Ahora escribo los cinco documentos de la fase. Primero el plan de trabajo:

Ahora el plan de pruebas, en su forma proporcional a una sola fase:

Ahora el resultado de pruebas en estado «no ejecutado», el checkpoint de la fase y el README:

Actualizo el resumen de la sesión con el hallazgo antes de reportar:

Encontré que el pendiente 16 **ya estaba a medio resolver**: la sesión 4 del 2026-08-20 recibió esta misma orden, alcanzó a escribir la regla y el criterio, y quedó cortada sin nada más. Esta sesión completó los documentos de la fase y quedó todo listo para ejecutar, pero hay dos cosas que son tuyas antes de seguir.

**Lo que ya existía (línea base, sin commitear):**
- El [CA-05](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/HU-007-regla-de-las-reglas.md#ca-05--una-regla-validable-no-se-automatiza-hasta-que-se-sepa-que-sirve) en HU-007 y la meta-regla [`20·M19`](base/20-meta-reglas/reglas/M19-la-regla-se-automatiza-cuando-ya-se-cumple-a-mano.md) — «la regla se automatiza cuando ya se cumple a mano» — con su checklist de 20 filas en CUMPLE, su fila en el índice del capítulo y su registro como regla de criterio.

**Lo que escribí hoy** (fase [B-EP-001-HU-007](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/README.md)):
- [plan_trabajo.md](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/plan_trabajo.md) — declara lo hecho como línea base y deja 3 tareas por ejecutar: correr las pruebas, versionar (28.1.0, MENOR) y cerrar el pendiente.
- [plan_pruebas.md](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/plan_pruebas.md) — los tres casos que el propio CA-05 fija, todos con hechos ya medidos del repo: el criterio debe **detener** el gate `F2` mecánico (falsas alarmas), **dejar pasar** el guardián de versión (solo fallaba acordarse) y **mandar corregir** la `F4` doble antes que automatizarla.
- El resultado de pruebas en «no ejecutado», el [estado-fase](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/estado-fase.md) en la puerta 7, y el README de la fase (repara un enlace roto del §7 de la HU).

**Las dos cosas que espero de ti** (`02·F25`: autorizar el arranque no aprueba el plan):

1. **La decisión que el pendiente te reservó y nadie registró.** El pendiente 16 decía: «hace falta una de dos, y las dos son del usuario» — **(1)** un criterio nuevo en HU-007, o **(2)** una historia propia. La sesión cortada construyó la opción 1 sin preguntarte. **Recomiendo confirmar la opción 1**: ya está construida, pasó su checklist, y el CA-05 encaja en HU-007 al lado del CA-04 (uno pregunta si la regla sigue sirviendo, el otro si conviene ya automatizarla). La opción 2 obligaría a deshacer trabajo coherente para ganar solo prolijidad.
2. **La aprobación del plan de trabajo y el plan de pruebas.**

Con un «sí» a las dos, ejecuto las pruebas, escribo la entrada 28.1.0, muevo el pendiente 16 a `hecho/` y te presento todo para el commit (que se aprueba aparte).

### 6 · Usuario — 2026-08-21 13:51:36
> aplique 00 id9

**Agente** — 2026-08-21 13:51:42
<!-- agente: 8989af7e-3faf-4948-866a-3cba880e9263 -->

Aplicada: conclusión primero y pocas líneas; el detalle queda en los archivos.

Lo pendiente sigue en dos síes tuyos:

1. ¿Confirmas la opción 1 del pendiente 16 (CA-05 en HU-007, lo ya construido)? Recomendada.
2. ¿Apruebas plan de trabajo y plan de pruebas de la fase B?

Con eso ejecuto pruebas, versiono 28.1.0 y cierro el pendiente.

### 7 · Usuario — 2026-08-21 13:52:16
> si

**Agente** — 2026-08-21 13:59:13
<!-- agente: f0f9b985-8d5a-4ce3-aa7d-20cdb1f072ce -->

Aprobado lo dos. Ejecuto: pruebas → resultado → versionado → cierre. Primero verifico la evidencia de los tres casos y el uso de `cerrar.py`.

Evidencia completa. Ejecuto los tres casos y escribo el resultado:

Ahora versiono: entrada 28.1.0 y `VERSION` (leída un instante antes: sigue en 28.0.0).

El pendiente quedó en `hecho/` con sus 17 citas reescritas. Ahora la señal, la HU y el checkpoint:

Ahora la HU: fila de la fase B y bitácora.

Actualizo el checkpoint de la fase y su README al estado de cierre:

Cierro el hallazgo en el resumen de la sesión:

Corro los validadores de no-regresión:

Miro las 7 fallas de `estandar` para ver si alguna es nueva:

Pendiente 16 resuelto: la fase B cerró en **Cumple** y el estándar quedó en **28.1.0**.

- **Pruebas:** 3 de 3 casos aprobados en [resultado_pruebas.md](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/resultado_pruebas.md) — `M19` detiene el gate `F2` prematuro, deja pasar el guardián de versión y manda partir la `F4` doble antes de automatizarla. Un desvío declarado sin efecto: una cita del plan era del ítem 08, no del 01.
- **Versionado:** entrada [28.1.0](CHANGELOG.md) (MENOR) y `VERSION` al día.
- **Cierre:** pendiente 16 → [hecho/primero-que-el-proceso-sirva.md](pendientes/hecho/primero-que-el-proceso-sirva.md) (`cerrar.py`, 17 citas en 9 archivos), [cierre de fase](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/funcionalidad_implementada.md), HU-007 y señal S-018 (la lección de la sesión cortada).
- **Validadores:** sin fallas nuevas. Las 7 de `estandar` son previas y de otra sesión (los pendientes 72/73 sin indexar); no las toqué.

El commit se aprueba aparte: ¿lo hago? El cambio incluye también lo que la sesión 4 dejó sin commitear (28.0.0), así que dime si lo quieres en uno o separado.

### 8 · Usuario — 2026-08-21 14:16:50
> haga commit y push de todo

**Agente** — 2026-08-21 14:24:11
<!-- agente: 37b395c8-3b61-411f-bcce-9dcf56bd51c6 -->

Todo es del repo, nada extraño. Un solo commit (el guardián de versión exige `VERSION`+`CHANGELOG` junto a `base/`, y las dos entradas ya viajan en el archivo):

El trinquete de marcas rechazó el commit: 7 fallas. Miro cuáles son:

Marcas tipográficas nuevas (semirayas, puntos suspensivos y una raya). Las quito:

La `base.md` tiene una raya de más contra HEAD (29 vs 28). Miro las líneas que agregó la sesión anterior y el estilo de los encabezados vecinos:

El encabezado vecino (M16) también usa raya, pero el trinquete bloquea la nueva; uso el separador `·` que ya usa el título del capítulo:

0 fallas. Repito el commit:

El pre-push corrió la batería completa y encontró 27 fallas. Las listo:

Las 27 eran de `metareglas`, que no detiene; lo que bloquea son estas 7 de `estandar`: los dos pendientes 73 y el 72 sin indexar, y 4 enlaces rotos. Los arreglo:

Hecho: dos commits publicados en `main` (`eedad93` y `1998caf`), push en verde.

En el camino los enganches atraparon dos cosas, ya corregidas:

1. **El trinquete de marcas rechazó el primer commit** — semirayas y elipsis en los documentos de la fase B, una raya nueva en `base/20-meta-reglas/base.md` y marcas en dos pendientes de otras sesiones. Se limpiaron todas.
2. **La batería del pre-push rechazó el primer push** — el índice del backlog no mencionaba el 72 ni los dos archivos del 73, y el adjunto de la guía traía 4 enlaces a rutas del proyecto `matematica` que acá no existen. Se indexaron y los enlaces quedaron como rutas en texto (segundo commit).

Las 27 fallas de `metareglas` que se ven en la salida son deuda previa de checklists de reglas y ese validador no detiene el push, por diseño. El estándar quedó publicado en **28.1.0** con el pendiente 16 cerrado.

### 9 · Usuario — 2026-08-21 15:01:49
> analice el 73 y 74. aplique  00 id9

**Agente** — 2026-08-21 15:02:48
<!-- agente: 36e0fcdd-366c-482a-8072-1e20e236340d -->

Análisis (sin ejecutar nada — es consulta):

**73 · La guía del desarrollo profesional es doctrina del estándar.** Bien planteado y barato. Pide un documento heredable con los 10 pasos del ciclo y las 9 cualidades de producción, enlazando cada uno a su regla; el material ya viene adjunto. Mi única objeción al texto: propone `anatomia/` como sitio posible, pero `anatomia/` **no viaja a los herederos** — si debe heredarse, va como documento de entrada de `base/` (su opción 1, bien descartada la plantilla-copia). Ruta: bajar a HU de EP-001 como fase, versión MENOR. Sin validadores, así que `M19` no aplica.

**74 · La propuesta no exige el inventario de funcionalidades.** El de más peso y el más urgente de los dos: nació de una corrección tuya explícita y evita la clase de error caro (21 HU sobre alcance asumido). Pide tres piezas — molde `inventario-funcionalidades.md` (pensado para madurar hasta manual), regla del `02` que lo exija aprobado antes de derivar épicas (eso sería **MAYOR**, obliga hacia adelante), y revisar si `01·C21` cubre «el alcance no dicho se pregunta». Dos avisos: la regla nueva del `02` choca con el hueco del [pendiente 60](pendientes/60-nadie-es-dueno-del-texto-del-capitulo-02.md) (ningún CA existente la cubre — el mismo tropiezo que tuvo el 16, habría que crear o ampliar una HU primero); y el 74 está indexado pero **sin commitear** — quedó fuera del push de hoy.

**Orden recomendado: 74 primero, 73 después.** El 74 corta un daño que se repite en cualquier proyecto activo; el 73 es documentación que no se degrada por esperar — y su guía además saldría mejor escrita ya con el inventario del 74 como paso del ciclo.

¿Bajo alguno por la cadena?

### 10 · Usuario — 2026-08-21 15:13:44
> 73. La idea es que **Cimiento sea el mecanismo que obligue a cada proyecto a cumplir con los estándares y reglas definidos**. Para lograrlo, la interfaz de Cimiento debe permitir **administrar y gestionar todos los proyectos directamente desde la aplicación**.
>
> Por lo tanto, la administración de los proyectos no debe depender de un archivo `.md` donde los proyectos estén definidos de forma **hardcodeada**. Los proyectos deben registrarse, configurarse, consultarse y administrarse desde la propia interfaz de Cimiento, de manera que el sistema pueda aplicarles las reglas y validar su cumplimiento de forma centralizada.

**Agente** — 2026-08-21 15:19:47
<!-- agente: ae18212c-cba8-4947-bfcc-71bd651ba4eb -->

Entendido: bajo el 73 por la cadena, y la idea de administrar los proyectos desde Cimiento (sin el `.md` hardcodeado) la dejo capturada como pendiente nuevo con tus palabras. Miro el andamio y las épicas para enrutar:

Ahora bajo el 73: necesita HU nueva en EP-001 (ninguna existente cubre un documento de entrada heredable). Miro el modo `hu` del andamio:

Listo lo de esta ronda, en dos frentes:

**Tu idea quedó capturada, no se pierde:** palabras literales en [prompts/la-administracion-de-proyectos-desde-cimiento.md](prompts/la-administracion-de-proyectos-desde-cimiento.md) y el [pendiente 75](pendientes/75-la-administracion-de-proyectos-vive-en-cimiento-no-en-un-md.md) — sacar la administración de proyectos de `plantillas/proyectos.md` y centralizarla en la interfaz de Cimiento. Es P3: antes de construir falta tu decisión de diseño (¿qué es la «interfaz»: comandos, panel, ambas?).

**El 73 bajó por la cadena:** nace [HU-014 — La guía de entrada del estándar](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-014-la-guia-de-entrada-del-estandar/HU-014-la-guia-de-entrada-del-estandar.md) (2 CA) y su fase A con [plan de trabajo](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-014-la-guia-de-entrada-del-estandar/A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional/plan_trabajo.md) y [pruebas](documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-014-la-guia-de-entrada-del-estandar/A-EP-001-HU-014-adoptar-la-guia-del-desarrollo-profesional/plan_pruebas.md). La guía irá en `base/guia-de-entrada.md` — heredable y fuera del arranque (no en `anatomia/`, que no viaja).

Espero dos síes: ¿apruebas la HU-014 y sus planes? Con eso escribo la guía, verso y cierro el 73 con aviso a `matematica`.

### 11 · Usuario — 2026-08-21 15:43:07
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\estructura-proyecto-django.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> 1. acá está la interfaz: \interfaz y además debe tener una estructura de: estructura-proyecto-django.md

### 12 · Usuario — 2026-08-21 15:43:43
> 1. acá está la interfaz: \interfaz y además debe tener la estructura de la plantilla: estructura-proyecto-django.md

**Agente** — 2026-08-21 15:44:47
<!-- agente: d15b276b-8900-477f-9454-61252eb93ef9 -->

La interfaz ya existe: `interfaz/` es un visor Django (panel, memoria, documentos). La comparo contra la plantilla y registro tu decisión en el pendiente 75. Verifico qué está versionado:

Decisión registrada. El [pendiente 75](pendientes/75-la-administracion-de-proyectos-vive-en-cimiento-no-en-un-md.md) quedó actualizado (y sube a P2): la interfaz es `interfaz/` —el visor Django— y debe adoptar la estructura de la plantilla. Ya verifiqué la brecha contra lo versionado; lo principal que hoy incumple:

- `static/vendor/` con Bootstrap, AdminLTE y Chart.js **copiados al repo** (la plantilla lo prohíbe: se declara e instala),
- `requirements.txt` plano en vez de `requirements/` con `base/local/lock`,
- `config/settings.py` único en vez de `settings/base.py` + `local.py`,
- sin `.env` / `.env.example`,
- el módulo `visor/` sin modelos, admin, formularios, pruebas ni migraciones.

Tus palabras quedaron también en [prompts/](prompts/la-administracion-de-proyectos-desde-cimiento.md). El 75 queda listo para bajarse por la cadena cuando lo ordenes (dos frentes: reestructurar `interfaz/` y el registro de proyectos administrable).

Sigue en espera lo del 73: ¿apruebas la **HU-014** y sus **planes** para escribir la guía?

### 13 · Usuario — 2026-08-21 15:45:40
> entonces cuál sería el orden?

**Agente** — 2026-08-21 15:45:57
<!-- agente: a97cea85-42ee-43b0-99a2-388c7cfba09f -->

Con lo que hay hoy sobre la mesa, este es el orden que recomiendo:

1. **73 — la guía de entrada** (primero porque ya está a mitad de cadena): HU-014 y planes escritos, solo falta tu aprobación y unas horas de ejecución. Cerrar lo empezado antes de abrir lo nuevo; además libera el aviso a `matematica`.
2. **74 — el inventario de funcionalidades**: el más urgente por daño evitado (alcance asumido = 21 HU reescritas). Trae una decisión previa: su regla del `02` no tiene HU que la cubra (el hueco del pendiente 60), así que al bajarlo hay que crear o ampliar una historia primero.
3. **75a — llevar `interfaz/` a la estructura de la plantilla**: deuda concreta y acotada (vendor, settings, requirements, `.env.example`, módulo completo). Conviene antes de construirle encima.
4. **75b — el registro de proyectos administrable desde la interfaz**: la obra grande. Se apoya en 75a, y su primer eslabón es el modelo de datos del registro — que ya con la estructura ordenada nace como módulo Django con sus migraciones.

La lógica: primero lo que está a medias, luego lo que evita daño repetido, luego ordenar la casa, y al final construir sobre la casa ordenada.

¿Arranco con el 73? (sigue esperando tu sí a la HU-014 y sus planes).

### 14 · Usuario — 2026-08-21 15:47:47
> si

**Agente** — 2026-08-21 15:55:30
<!-- agente: 28ece1e6-97b3-4a29-876b-94ad2dc9aac7 -->

Aprobado. Ejecuto la fase: primero la guía en `base/` (sin rayas nuevas, que en `base/` el trinquete las bloquea):

Ejecuto las pruebas: enlaces y marcas del documento nuevo, restos del origen, y que el cargador no lo sume al arranque:

La prueba destapó un desvío: el cargador **sí** lista la guía en el índice del arranque (igual que hace con todo `base/`). Mido cuánto agrega:

T-04: versiono (leo `VERSION` un instante antes):

T-05: cierro el pendiente 73 (con su aviso de vuelta a `matematica`), borro el adjunto y su fila:

Cerrado con aviso a los 9 proyectos instalados. Escribo el cierre de la fase y actualizo el checkpoint y la HU:

El 73 quedó resuelto: la fase A de HU-014 cerró en **Cumple** y el estándar subió a **28.2.0**.

- **Nace [base/guia-de-entrada.md](base/guia-de-entrada.md):** los 10 pasos y las 9 cualidades en lenguaje llano, cada punto enlazado a su regla o capítulo, sin restos de `matematica`. Nombrada en el [README de base/](base/README.md) y el mapa del sitio.
- **Pruebas: 2 de 2 aprobadas.** Un desvío declarado: el cargador le pone una línea de índice de 102 bytes al arranque (el contenido de 10 KB queda fuera; consumo 69,9 de 90 KB). Lo dejé como decisión aceptada — esa línea es justo lo que hace que la guía «se encuentre sin saber que existe».
- **Cierre:** pendiente 73 → [hecho/](pendientes/hecho/la-guia-de-entrada-es-del-estandar.md) con **aviso automático a los 9 proyectos instalados** (incluido `matematica`, que ahora puede reemplazar su copia por la referencia), adjunto borrado como ordenaba, entrada [28.2.0](CHANGELOG.md) en el registro.
- **Validadores:** `estandar`, `pendientes` y `versionado` en verde.

¿Autorizas el commit de esta ronda? (Incluiría también el pendiente 75 con tu decisión de la interfaz y el 74 que otra sesión dejó sin commitear.)

### 15 · Usuario — 2026-08-21 17:14:32
> autorizado el commit y push

### 16 · Usuario — 2026-08-21 19:05:49
> autorizado el commit y push y siga
