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
