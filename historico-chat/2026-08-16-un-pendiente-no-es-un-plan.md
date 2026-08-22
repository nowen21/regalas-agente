<!-- sesion: 0c34a008-3e1b-4463-bc56-7969c6b6e4a7 -->
<!-- nombre: preguntado -->

# 2026-08-16 — Un pendiente no es un plan

## Conversación

### 1 · Usuario — 2026-08-16 15:01:32
> hola

**Agente** — 2026-08-16 15:02:40
<!-- agente: 6ce32596-7fa5-478d-b63f-fc9270c84bc0 -->

Hola. Estándar cargado y sesión registrada.

Lo último que quedó abierto: [por-que-dice-instalacion-incompleta.md](historico-chat/2026-08-16-por-que-dice-instalacion-incompleta.md) — el checklist marcaba «falta» por copias viejas del estándar en otros proyectos.

¿Sobre qué trabajamos?

### 2 · Usuario — 2026-08-16 15:03:17
> no entendí qué fue lo que hizo

**Agente** — 2026-08-16 15:03:25
<!-- agente: ad4eebce-5d27-4a85-8813-08d565c75190 -->

Leí las reglas del estándar antes de responder — es lo que exige el paso 0 del [CLAUDE.md](CLAUDE.md): abrir `base/` y obedecerlo. Eso fue todo: nueve archivos leídos, nada modificado.

Si lo que no entendiste es la última línea de mi mensaje —la sesión anterior sobre «instalación incompleta»— avísame y te la resumo.

### 3 · Usuario — 2026-08-16 15:13:04
> los pendientes que se han ejecutado han tenido su respectiva EP-HU-FASE?

### 4 · Usuario — 2026-08-16 15:13:36
> los de hoy

**Agente** — 2026-08-16 15:14:59
<!-- agente: 955323f2-228b-49f1-a3ec-42f870f57b27 -->

No. Ninguno de los que se cerraron hoy tuvo fase — la última fase que se abrió es del 2026-08-15.

Lo que se cerró hoy, según el propio [pendientes/README.md](pendientes/README.md):

| Cerrado hoy | ¿EP-HU-Fase? |
|---|---|
| 39 · memoria borrada por el enganche (= punto 6 del 33) | no |
| 34 · enlaces de las plantillas al estándar (v20.0.1) | no |
| 31 · los resúmenes de las 33 sesiones viejas | no |
| 29 · punto 2 · la transcripción a mano | no |

Y lo mismo pasó con las reglas que se escribieron hoy: `DOC23` (17.0.0), el planteamiento y el glosario (18.0.0), `F22` e `ID9` (20.0.0). Ninguna nació de una fase.

Esto ya está anotado como defecto: el [pendiente 38](pendientes/38-el-validador-de-la-f22-se-escribio-sin-su-fase.md) lo dice del validador de `F22`, y el [30](pendientes/30-el-checklist-no-ve-la-cadena.md) es la causa de fondo — `F0` exige la cadena `planteamiento → épica → HU → especificación → plan → código` y ningún componente la comprueba, así que el arranque sigue diciendo que todo está bien.

### 5 · Usuario — 2026-08-16 15:16:26
> mire lo que me está respondiendo un proyecto:
>
> El marcador «RUTA-ESTANDAR» es un hueco que el instalador debe rellenar con la carpeta donde vive el estándar.
>
> Cómo debería quedar en el proyecto:
>
>
> [02·F13](C:/Ing. Jose/ia/agente/base/02-flujo-de-trabajo/reglas/F13-....md)
> Cómo quedó en .agente/stack-instalacion.md:
>
>
> [02·F13](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F13-....md)
> El hueco sigue ahí. Nadie lo rellenó. Si hace clic, no llega a ninguna parte.
>
> Por qué se le pasó al instalador: ese archivo no lo arma llenando huecos, lo copia entero tal cual —«esta copia sí se reescribe: no la llena nadie»—, así que el marcador viaja intacto.
>
> Y por qué nadie avisa: al revisor de enlaces le enseñaron a saltarse todo enlace que traiga «RUTA-ESTANDAR», porque dentro del estándar es normal que esté sin rellenar. Dentro de un proyecto no lo es — pero el revisor no distingue, y calla.
>
> O sea: un enlace roto que además nadie va a ver.
>
> Eso es defecto del cimiento, igual que los otros. Mi pregunta era solo si lo reporto ahora, junto con el otro que ya me autorizó, o lo dejo para después.

### 6 · Usuario — 2026-08-16 15:17:33
> No. Ninguno de los que se cerraron hoy tuvo fase — la última fase que se abrió es del 2026-08-15.
> por qué no tuvo fase?

**Agente** — 2026-08-16 15:17:53
<!-- agente: 5a9d7b1c-86f6-4b1b-84db-17b4beb12d15 -->

Porque el repo tiene dos procedimientos para lo mismo y ninguno de los dos nombra al otro.

- [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md) dice que todo pasa por `planteamiento → épica → HU → especificación → plan → código`, sin saltar eslabones por tamaño.
- El §2 de [CLAUDE.md](CLAUDE.md) y los nueve pasos de [`20 · Meta-reglas`](base/20-meta-reglas/base.md) dicen que cambiar una regla es: buscar → enrutar → escribir en el molde → versionar. **Ni uno de los nueve menciona épica, HU ni fase.**

El trabajo de hoy salió de `pendientes/`, que es la tercera vía: un pendiente se cierra editando `base/` y anotando el CHANGELOG. Nadie escribió que un pendiente tenga que bajar a HU antes de ejecutarse.

Así que el agente siguió el procedimiento que sí estaba escrito para lo que estaba haciendo, y ese procedimiento no pide fase. Y no saltó ninguna alarma porque nada comprueba la cadena — es exactamente el [pendiente 30](pendientes/30-el-checklist-no-ve-la-cadena.md), y el [38](pendientes/38-el-validador-de-la-f22-se-escribio-sin-su-fase.md) es el mismo caso ya anotado.

Falta la decisión de fondo: o `F0` aplica también a cambiar el estándar —y entonces el §2 y los nueve pasos están incompletos— o no aplica, y hay que escribir dónde está el borde.

### 7 · Usuario — 2026-08-16 15:20:38
> es que precisamente esos pendientes son para mejorar a: Cimiento y por ende deben aplicar EE-HU-FASE
> mire precisamente lo que me responde un proyecto que ya implemento un mejora y que por no tener fase no se hizo prueba:
>
> El marcador «RUTA-ESTANDAR» es un hueco que el instalador debe rellenar con la carpeta donde vive el estándar.
>
> Cómo debería quedar en el proyecto:
>
>
> [02·F13](C:/Ing. Jose/ia/agente/base/02-flujo-de-trabajo/reglas/F13-....md)
> Cómo quedó en .agente/stack-instalacion.md:
>
>
> [02·F13](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F13-....md)
> El hueco sigue ahí. Nadie lo rellenó. Si hace clic, no llega a ninguna parte.
>
> Por qué se le pasó al instalador: ese archivo no lo arma llenando huecos, lo copia entero tal cual —«esta copia sí se reescribe: no la llena nadie»—, así que el marcador viaja intacto.
>
> Y por qué nadie avisa: al revisor de enlaces le enseñaron a saltarse todo enlace que traiga «RUTA-ESTANDAR», porque dentro del estándar es normal que esté sin rellenar. Dentro de un proyecto no lo es — pero el revisor no distingue, y calla.
>
> O sea: un enlace roto que además nadie va a ver.
>
> Eso es defecto del cimiento, igual que los otros. Mi pregunta era solo si lo reporto ahora, junto con el otro que ya me autorizó, o lo dejo para después.

**Agente** — 2026-08-16 15:21:34
<!-- agente: c2675953-88e6-4fcc-b1a4-fdf86a1f75a5 -->

Verifiqué las dos mitades del reporte contra el código. La primera es cierta; la segunda no.

**Cierto:** [instalar.py:329-333](validadores/instalar.py#L329-L333) escribe `stack-instalacion.md` como `leer(original) + sello`, sin pasar por `_rellenar()`. El marcador viaja intacto. Es el hueco que dejó el pendiente 34 al cerrarse hoy.

**No es cierto que el revisor calle:** [enlaces.py:90-92](validadores/enlaces.py#L90-L92) no salta el marcador — lo resuelve contra la raíz que está validando. Dentro de un proyecto esa raíz es el proyecto, así que busca `<proyecto>/base/…`, no lo encuentra y reporta `enlace roto`. Y `.agente/` no está en las carpetas excluidas. Vale la pena que ese proyecto corra `python validadores/enlaces.py` y pegue la salida: o su copia de `enlaces.py` es vieja, o el enlace sí está saliendo reportado y nadie lo miró.

Sobre lo de fondo, tienes razón y el caso lo prueba: el 34 se ejecutó sin fase, sin plan de pruebas y sin resultado, y por eso nadie probó lo único que había que probar — instalar en un proyecto y hacer clic en el enlace.

Lo que falta escribir es una regla: **cerrar un pendiente es una unidad de trabajo y recorre la cadena como cualquier otra** — extiende [`02·F0`](base/02-flujo-de-trabajo/reglas/F0-recorre-la-cadena-completa-sin-saltar-eslabones.md), y obliga a corregir el §2 de [CLAUDE.md](CLAUDE.md) y los nueve pasos de [`20 · Meta-reglas`](base/20-meta-reglas/base.md), que hoy autorizan lo contrario. Arrastra además retrodocumentar el 34 como fase, igual que ya pide el [pendiente 38](pendientes/38-el-validador-de-la-f22-se-escribio-sin-su-fase.md) para el validador de `F22`.

¿Lo escribo —la regla, el pendiente del marcador sin rellenar y la corrección de los dos procedimientos— o primero decides algo de eso?

### 8 · Usuario — 2026-08-16 15:23:32
> no entiendo como un proyecto va a tener una copia de la base de: Cimiento eso tiene sentido?

**Agente** — 2026-08-16 15:24:11
<!-- agente: 54c0a374-8672-45f7-adcf-57c9706e07a4 -->

No, no tiene sentido — y no la tiene. Me equivoqué en la línea anterior: dije "o su copia de `enlaces.py` es vieja" y un proyecto no tiene copia de `enlaces.py`.

El instalador no copia `base/` ni `validadores/`. Los engancha por ruta absoluta: [instalar.py:211-212](validadores/instalar.py#L211-L212) escribe el comando como `python "<ruta-del-estandar>/validadores/<guion>" --raiz "<ruta-del-proyecto>"`. El programa vive siempre en Cimiento y se le pasa el proyecto como parámetro, así que corre la versión de hoy sin que nadie actualice nada.

Lo que sí se copia a un proyecto es poco: su `CLAUDE.md`, los cuatro archivos de `.agente/`, el `stack-instalacion.md`, el README del histórico y los enganches. Esas son las copias que pueden quedar viejas — y es de lo que hablaba la sesión de esta mañana, no de `base/`.

Y ahí está el defecto real, que es distinto al que reportó el proyecto: [enlaces.py:90-91](validadores/enlaces.py#L90-L91) resuelve `«RUTA-ESTANDAR»` contra `raiz`, dando por hecho que `raiz` es Cimiento. Cuando corre con `--raiz <proyecto>` esa suposición es falsa: busca `<proyecto>/base/…`, que nunca existe. O sea que el marcador **nunca** se resuelve bien dentro de un proyecto — ni cuando está bien puesto.

### 9 · Usuario — 2026-08-16 15:28:54
> solución?

**Agente** — 2026-08-16 15:29:44
<!-- agente: 5aab5931-a67d-4c63-a764-594941632f97 -->

Tres arreglos, y el defecto es más grande de lo que reportó el proyecto: son **tres** puntos de copia, no uno.

Solo [instalar_claude_md](validadores/instalar.py#L602-L603) pasa el texto por `_rellenar()`. Los otros tres escriben la plantilla cruda:

| Dónde | Qué copia | Marcadores que arrastra |
|---|---|---|
| [instalar.py:333](validadores/instalar.py#L333) | `.agente/stack-instalacion.md` | 1 |
| [instalar.py:434](validadores/instalar.py#L434) | `historico-chat/memory/memory.md` | 2 |
| [instalar.py:708](validadores/instalar.py#L708) | los 4 archivos de `.agente/` | varios, entre ellos 5 en `reglas-proyecto.md` |

**1 · Que toda copia pase por el mismo filtro.** `_rellenar(leer(origen), _rellenos(ruta))` en los tres sitios. No afecta el sello: la huella se calcula del stack central ([checklist.py:82-84](validadores/checklist.py#L82-L84)), no del texto del archivo.

**2 · Que el marcador se resuelva contra Cimiento.** En [enlaces.py:91](validadores/enlaces.py#L91), `base = raiz` tiene que ser la carpeta del estándar, no la que se está validando. Dentro de Cimiento es lo mismo; dentro de un proyecto es la diferencia entre resolver bien y no resolver nunca. Es la red de seguridad por si mañana vuelve a escaparse un marcador.

**3 · La prueba que faltó.** Instalar en una carpeta desechable y comprobar que ningún archivo copiado conserva un `«…»`. Es lo que habría atrapado esto, y no existe porque el pendiente 34 se cerró sin fase ni plan de pruebas — justo lo que decías.

Esto va como fase de [EP-007 · HU-001](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/) para los puntos 1 y 3, y el punto 2 es de [EP-004 · HU-005](documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/). ¿Abro la fase o antes escribimos la regla de que cerrar un pendiente recorre la cadena?

### 10 · Usuario — 2026-08-16 15:31:36
> cree la regla

**Agente** — 2026-08-16 15:36:09
<!-- agente: f803c1de-b7e6-44e2-a6a2-1108f6264ba0 -->

Ejecuto el procedimiento de los nueve pasos. Empiezo por la regla.

Ahora los dos procedimientos que decían lo contrario (fila 17 del checklist).

Paso 7 (`M9`) y paso 8 (`M10`):

Regla creada, con los nueve pasos del procedimiento. Versión **21.0.0** (MAYOR).

| Archivo | Qué cambió |
|---|---|
| [F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) | nuevo · la regla, con su checklist en **CUMPLE** (19 ✅ · 1 N/A) |
| [base/02-flujo-de-trabajo/base.md](base/02-flujo-de-trabajo/base.md) | fila en el índice, conteo de 21 a 22 vigentes, y el backlog entra por el paso 0 del mapa |
| [base/20-meta-reglas/base.md](base/20-meta-reglas/base.md) | los nueve pasos dejan de ser el camino completo: si sale de un pendiente, primero la cadena |
| [CLAUDE.md](CLAUDE.md) | §2 dice lo mismo para este repo |
| [validadores/reglas-validables.md](validadores/reglas-validables.md) | 🟡 validable, falta el validador — hay que fijar antes dónde declara el pendiente su fase |
| [CHANGELOG.md](CHANGELOG.md) · [VERSION](VERSION) | entrada 21.0.0 y el número |

Lo que exige, en una línea: **un pendiente se baja a HU y se construye como fase; su archivo dice qué falta, no cómo se construye.** Hereda la excepción de `F0`, así que el pendiente que solo pide decidir algo no abre fase.

Validadores en verde: `enlaces` sin hallazgos, `estandar` con 5 avisos que ya venían de antes (ninguno en lo que toqué), `versionado` OK.

Dos cosas que quedan y no hice porque no las pediste:

1. El pendiente del marcador `«RUTA-ESTANDAR»` sin rellenar en los tres puntos de copia — hoy no está escrito en ninguna parte.
2. La fase de [EP-007 · HU-001](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/) que lo arregla, que es donde `F23` ya obliga a pasar.

¿Sigo con eso, o revisas primero la regla?

### 11 · Usuario — 2026-08-16 15:37:27
> cual es la regla?

**Agente** — 2026-08-16 15:38:38
<!-- agente: f896fc02-d397-41e0-8cc7-a71a89bbc80c -->

La regla, tal como quedó escrita:

> ## F23 · Ejecuta un pendiente como fase de una historia de usuario
>
> Un pendiente del backlog no se implementa desde su archivo: se baja a historia de usuario de la épica que le corresponda y se construye como fase de esa historia (`02·F12`), con todo lo que una fase lleva (extiende `02·F0`).
> Que la mejora ya esté acordada y escrita no salta ningún eslabón: el pendiente dice **qué falta**, no cómo se construye ni cómo se comprueba.
>
> ```
> INCORRECTO: el pendiente dice qué hay que arreglar → se edita el código, se sube
>             la versión y se marca hecho; como no hubo fase, nadie escribió el
>             plan de pruebas y el arreglo se publicó sin probarse
> CORRECTO:   el pendiente baja a HU → fase con su plan y sus pruebas → se
>             construye, se prueba, y solo entonces el pendiente se marca hecho
> ```

Vive en [base/02-flujo-de-trabajo/reglas/F23-...md](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md).

Voy a escribir el resumen de la sesión, que está vacío.

Resumen escrito: [historico-chat/resumenes/2026-08-16/sesion-5.md](historico-chat/resumenes/2026-08-16/sesion-5.md), con tres hallazgos.

| # | Hallazgo | Estado |
|---|---|---|
| H-1 | Un pendiente se ejecutaba sin bajar a HU ni a fase | resuelto → `F23` |
| H-2 | El instalador copia tres archivos sin rellenar sus marcadores | abierto |
| H-3 | El marcador nunca se resuelve bien dentro de un proyecto | abierto |

La sesión todavía no cierra: al H-2 y al H-3 les falta su pendiente y su historia escrita.

Y esta sesión se está guardando como `2026-08-16-sesion-5.md`, que no dice de qué trata. Propongo `2026-08-16-un-pendiente-no-es-un-plan.md` — *el backlog se ejecutaba sin cadena, y por eso un arreglo se publicó sin probarse*. ¿Va?

### 12 · Usuario — 2026-08-16 15:41:38
> si: 2026-08-16-un-pendiente-no-es-un-plan.md

**Agente** — 2026-08-16 15:43:39
<!-- agente: 17b7dbae-d306-41d7-b353-089f651d12fd -->

Corrijo: cuando dije "`enlaces` sin hallazgos" me apoyé en que el comando no imprimía nada. No imprime nada porque [enlaces.py](validadores/enlaces.py) no tiene bloque `__main__` — se corre con `validar.py estandar`. Ahí sí hay una falla, y la causé yo al renombrar.

Renombrado: [historico-chat/2026-08-16-un-pendiente-no-es-un-plan.md](historico-chat/2026-08-16-un-pendiente-no-es-un-plan.md), con su línea en el índice y el resumen arrastrado.

En el camino se reprodujo el [pendiente 35](pendientes/35-renombrar-una-sesion-deja-roto-el-enlace-de-su-resumen.md) por tercera vez: `historico.py --renombrar` movió el resumen pero dejó adentro el enlace viejo, y el índice del día seguía diciendo «Sin escribir todavía». Corregí los dos a mano; la causa sigue en el pendiente, que ahora entra por su HU y su fase como manda `F23`.

`validar.py estandar`: **0 fallas**, 5 avisos que ya venían de antes.

Para ponerte al día con `/rename`, pega esto en el chat:

```
/rename un-pendiente-no-es-un-plan
```

Sin commitear todavía. Lo que hay para revisar: la regla `F23` y sus cinco archivos, el resumen con tres hallazgos, y las dos correcciones del renombre. ¿Sigo con los pendientes del H-2 y el H-3, o revisas primero?

### 13 · Usuario — 2026-08-16 15:45:21
> siga con los pendientes

**Agente** — 2026-08-16 15:47:19
<!-- agente: 89a0ca05-ba8d-4fa3-bc4c-74d1544e21d1 -->

Ahora actualizo el resumen: los dos hallazgos ya tienen su pendiente.

Pendientes creados.

| # | P | Qué dice |
|---|---|---|
| [40](pendientes/40-el-instalador-copia-sin-rellenar-los-marcadores.md) | **P0** | De los cuatro puntos de copia del instalador, tres no rellenan. Cada proyecto que se instale hoy nace con las citas a las reglas muertas. |
| [41](pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md) | **P1** | `enlaces.py` resuelve el marcador contra la raíz que valida; el veredicto depende de desde dónde se corra. |

También actualicé [pendientes/README.md](pendientes/README.md): sección nueva, la dependencia dura `40 → 41`, y el conteo pasa de 30 a 32 abiertos. En el [resumen](historico-chat/resumenes/2026-08-16/un-pendiente-no-es-un-plan.md) el H-2 y el H-3 ya apuntan a su pendiente.

Validadores: `estandar` 0 fallas (los 5 avisos ya venían), `versionado` OK.

Falta una sola casilla para poder cerrar la sesión: **las tres historias de usuario que disparan los hallazgos no están escritas en su épica** — la del validador de `F23` en EP-004, y las dos fases nuevas en EP-007 · HU-001 y EP-004 · HU-005.

Ahí es donde `F23` empieza a cobrar: el 40 y el 41 no se pueden construir hasta que esas historias existan. ¿Las escribo?

### 14 · Usuario — 2026-08-16 15:49:16
> que va a escribir?

**Agente** — 2026-08-16 15:49:40
<!-- agente: c6b47b5a-dbc4-4361-8349-2094d880a78a -->

Tres cosas, ninguna es código:

**1 · Una HU nueva en EP-004** — sería la `HU-016`, para el validador de `F23`: que un programa avise cuando un pendiente se marca hecho sin nombrar la HU y la fase donde se construyó. Hoy la regla lo exige y nada lo comprueba. Va desde [plantillas/ciclo-vida-proyectos/04-HU.md](plantillas/ciclo-vida-proyectos/04-HU.md), con sus criterios de aceptación.

**2 · La fase que arregla el pendiente 40**, colgando de la [HU-001 de EP-007](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/HU-001-instalar-con-una-linea.md), que ya existe. Son dos documentos: el `plan_trabajo` con las trece preguntas de `F14`, y el `plan_pruebas` con el caso que faltó — instalar en carpeta desechable y comprobar que no queda ningún `«…»`.

**3 · La fase que arregla el pendiente 41**, colgando de la [HU-005 de EP-004](documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/HU-005-enlaces-y-citas.md). Los mismos dos documentos, para el cambio de una línea en `enlaces.py` y su caso de prueba.

Después de eso **paro y te los presento** — `F4` no deja tocar código hasta que apruebes los planes. O sea: escribo qué se va a hacer y cómo se comprueba; construir es el paso siguiente y lo autorizas tú.

Si prefieres, empiezo solo por la fase del 40 —el P0, el que está haciendo daño hoy— y las otras dos después. ¿Cuál?

### 15 · Usuario — 2026-08-16 15:51:40
> Aplique la regla: 00·ID9 para darme la respuesta

**Agente** — 2026-08-16 15:51:48
<!-- agente: faceaf8d-7427-4ad4-921c-5e6a20f271c6 -->

Tres documentos, ningún código:

1. **HU-016 en EP-004** — el validador de `F23`.
2. **Fase en EP-007 · HU-001** — plan de trabajo y plan de pruebas del [pendiente 40](pendientes/40-el-instalador-copia-sin-rellenar-los-marcadores.md).
3. **Fase en EP-004 · HU-005** — los mismos dos, del [41](pendientes/41-el-marcador-no-se-resuelve-dentro-de-un-proyecto.md).

Luego paro: `F4` no deja tocar código sin tu aprobación.

¿Las tres, o solo la del 40 (el P0)?

### 16 · Usuario — 2026-08-16 15:52:37
> las 3

**Agente** — 2026-08-16 16:01:30
<!-- agente: 725c022a-5056-49bb-aee6-35e66cc32719 -->

Empiezo por la HU nueva de EP-004.

Ahora la fase del pendiente 40 (EP-007 · HU-001).

Ahora la tercera: la fase del pendiente 41 (EP-004 · HU-005).

Falta la trazabilidad hacia arriba: las dos HU tienen que nombrar su fase (§8).

Y el resumen: los tres hallazgos ya tienen su historia escrita.

Falta el `estado-fase.md` de cada fase — es el documento que dice dónde está detenida.

Los tres documentos están escritos. Las dos fases quedaron en **estación 4 de 11: esperando tu aprobación**, sin una línea de código tocada.

| Qué | Dónde |
|---|---|
| **HU-016** — el validador de `F23` | [EP-004 · HU-016](documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/HU-016-el-pendiente-cerrado-nombra-su-fase.md) · 4 CA |
| **Fase del pendiente 40** | [A-EP-007-HU-001-rellenar-los-marcadores-al-copiar](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/) · 7 tareas, 5,5 h, 4 casos de prueba |
| **Fase del pendiente 41** | [A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar](documentacion/epicas/EP-004-comprobacion-automatica/HU-005-enlaces-y-citas/A-EP-004-HU-005-el-marcador-se-resuelve-contra-el-estandar/) · 7 tareas, 3,75 h, 4 casos |

Tres cosas de los planes que conviene que mires antes de aprobar:

1. **El caso de prueba que faltó** está escrito como `CP-001` de la fase 40: instalar en carpeta desechable y comprobar que ningún archivo copiado conserva un `«…»`. Correrlo antes de publicar la 20.0.1 habría mostrado el defecto.
2. **Un proyecto ya instalado no se arregla solo.** Los cuatro archivos de `.agente/` no se pisan una vez creados. Está declarado como riesgo `B-01` y es la duda abierta del plan.
3. **Ninguna de las dos fases escribe la especificación de su módulo** — ni instalación ni comprobación la tienen. Queda declarado como deuda, no resuelto de paso.

`estandar`, `trazabilidad` y `fases`: **0 fallas**. Los avisos que quedan sobre lo mío son los esperables — `resultado_pruebas.md` y `funcionalidad_implementada.md` nacen al ejecutar.

Nada commiteado. ¿Apruebas los dos planes para que arranque la fase del 40?

### 17 · Usuario — 2026-08-16 16:04:09
> si

**Agente** — 2026-08-16 16:39:17
<!-- agente: b5db0f6b-a06d-42da-8f1e-4a654f6acf11 -->

Aprobado. Arranca la fase del 40 — estación 6, ejecución continua.

No hay pytest ni pruebas en el repo. Uso `unittest` de la biblioteca estándar — sin instalar nada, que es el RNF de autonomía de la épica. Lo anoto en el resultado.

T-01 a T-03: los tres puntos de copia.

T-04 y T-06: la prueba que faltó.

Paro acá. La prueba encontró algo, pero no lo que buscaba — y el criterio que aprobaste está mal escrito.

**Lo bueno:** los tres puntos de copia ya rellenan. Se ve en la salida: `marco-normativo.md` llegó al proyecto con `C:/Ing. Jose/ia/agente/base/...` donde antes iba el marcador.

**El problema:** el plan §2.6 decidió comprobar que no quede **ningún** `«…»`, y eso mezcla dos cosas distintas:

| Hueco | Quién lo llena | ¿Debe sobrevivir a la copia? |
|---|---|---|
| `«RUTA-ESTANDAR»`, `«NOMBRE-PROYECTO»`, `«FECHA»`… | el instalador | **No** — es el defecto del pendiente 40 |
| `«rubro / sector»`, `«quién lo usa a diario»`… | el proyecto, después | **Sí** — son las preguntas que el agente todavía no puede responder |

Los 4 archivos de `.agente/` llegan a propósito con huecos: son formularios por llenar. La prueba los marcó como defecto y por eso da rojo en 65 líneas que están bien.

**Lo que propongo:** que la prueba compruebe solo los marcadores que `_rellenos()` sabe llenar. Es la lista que ya existe en el código, así que sigue atrapando los que se agreguen mañana — que era el motivo de la decisión original.

Eso cambia el criterio de aceptación de un plan ya aprobado, así que no lo toco sin tu OK (`F8`). ¿Lo corrijo así?

### 18 · Usuario — 2026-08-16 16:45:25
> si

### 19 · Usuario — 2026-08-16 17:14:28
> sg

**Agente** — 2026-08-16 17:35:31
<!-- agente: 9f287359-d1eb-40e2-a4a0-0350f01bbb6c -->

La prueba pasa. Compruebo que no sea una prueba vacía — que de verdad se pondría roja con el defecto:

La prueba no es vacía: con el defecto puesto se pone roja y nombra cada marcador. T-05, la documentación:

Ahora el `resultado_pruebas.md` — lo que salió al ejecutar (T-04, T-06).

19 enlaces en el proyecto instalado, **0 rotos**. El que reportó el proyecto ahora abre. Escribo el resultado.

T-07: la versión, y el aviso de qué hacer para quedar al día.

Actualizo el `estado-fase.md` y cierro con el `funcionalidad_implementada.md`.

Actualizo el pendiente 40 y el resumen: el hallazgo H-2 cerró.

Fase del 40 **cerrada**, veredicto Cumple. Estación 9 de 11: falta solo el commit, que autorizas aparte.

| Qué | Resultado |
|---|---|
| Los 3 puntos de copia | rellenan — [instalar.py](validadores/instalar.py) |
| Primera prueba del repo | [test_instalar_marcadores.py](validadores/tests/test_instalar_marcadores.py) · 6 de 6 verdes |
| El enlace que reportó el proyecto | **abre** · 19 enlaces revisados, 0 rotos |
| ¿La prueba sirve? | con el defecto puesto se pone roja y nombra cada marcador |
| Versión | 21.1.0 (MENOR) |

Dos cosas que quedan escritas, no resueltas:

1. **Un proyecto instalado antes de hoy no se arregla solo.** Los 4 archivos de `.agente/` no se pisan una vez creados. Avisado en el `CHANGELOG`.
2. **El `DEF-01` era del plan, no del código.** Está en el [resultado_pruebas](documentacion/epicas/EP-007-instalacion-y-actualizacion/HU-001-instalar-con-una-linea/A-EP-007-HU-001-rellenar-los-marcadores-al-copiar/resultado_pruebas.md) §2 y §4, con lo que pasó: la prueba salió roja, se paró, se reportó y lo aprobaste. Lo dejé escrito porque es la diferencia con la vez anterior.

`estandar`, `trazabilidad` y `versionado`: 0 fallas.

Un aviso: `pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md` aparece modificado y no lo tocó esta sesión — lo dejo fuera de cualquier commit.

¿Sigo con la fase del 41, o commiteamos primero lo de hoy?

### 20 · Usuario — 2026-08-16 17:44:16
> siga

**Agente** — 2026-08-16 18:02:45
<!-- agente: 5bebded8-211a-41c6-a7ee-7a24a6ebbf8a -->

Fase del 41. T-01: la línea base, antes de tocar nada.

T-02: el marcador se resuelve contra el estándar.

T-03 y T-04: las dos pruebas.

T-05: comparar contra la línea base, que es lo único que respalda el "acá no cambió nada".

T-06, la documentación:

T-07: la versión.

Cierro la fase: resultado, estado y cierre documental.

Cierro el pendiente 41 y actualizo el índice y el resumen.

Otra sesión abrió el **pendiente 42**, y afecta lo que cerré: reinstalar no repara los proyectos viejos. Lo tengo en cuenta.

Corrijo mi entrada del `CHANGELOG`: decía que reinstalar deja al día, y el pendiente 42 demuestra que no.

Cierro el resumen: el H-3 quedó resuelto.

Fase del 41 **cerrada**, veredicto Cumple. Los dos pendientes de hoy quedaron construidos por la cadena que `F23` exige.

| | Fase del 40 (v21.1.0) | Fase del 41 (v21.1.1) |
|---|---|---|
| Qué arregla | los 3 puntos de copia rellenan | el marcador se resuelve contra el estándar |
| Pruebas | 6 verdes | 6 verdes |
| No regresión | 19 enlaces del proyecto instalado, 0 rotos | salida sobre el estándar **idéntica** antes y después |
| ¿La prueba sirve? | roja con el defecto puesto | roja con el defecto puesto |

**Otra sesión abrió el [pendiente 42](pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md) mientras trabajaba, y contradecía algo que yo había escrito.** Mi `CHANGELOG` de la 21.1.0 decía «volver a correr la instalación» para quedar al día, y `shopnest-mesa` comprobó que no repara: la huella sale del stack central, así que el instalador dice «ya estaba al día» y no reescribe. Corregí esa línea y lo anoté como deuda no prevista en el cierre de la fase. **El arreglo llega a instalaciones nuevas, no a las viejas.**

Dos fallas en `validar.py estandar` que **no son de esta sesión**: [pendientes/44](pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md) y la fila 190 del [índice](pendientes/README.md) enlazan a `34-las-plantillas-enlazan-una-carpeta-base-que-el-proyecto-no-tiene.md`, que se movió a `hecho/`. Las dejo — son de la otra sesión, que sigue escribiendo ahí.

Todo lo demás en verde: `trazabilidad`, `versionado`, 12 pruebas.

Nada commiteado. ¿Commiteamos lo de esta sesión?

### 21 · Usuario — 2026-08-16 18:17:49
> si

**Agente** — 2026-08-16 18:19:34
<!-- agente: 82cead71-3bfb-4e8f-bee7-66caf3473fcd -->

Antes de commitear tengo que mostrarte el mensaje y los archivos (`09·G7`). Reviso qué hay.

Hay un problema que tengo que plantearte antes.

**`pendientes/README.md` mezcla mi trabajo con el de la otra sesión** — mis filas 40 y 41 conviven con las suyas (42, y el 34 pasado a «hecho a medias»). No puedo separarlas sin partir el archivo. Es literalmente el [pendiente 22](pendientes/22-dos-sesiones-versionando-a-la-vez.md).

Propongo dejar ese archivo **fuera** y que lo suba la otra sesión con lo suyo. Lo demás va en cuatro commits, uno por unidad, cada uno con su versión:

```
1 · Ejecuta un pendiente como fase de una historia de usuario (21.0.0)

   Los pendientes mejoran el cimiento, así que deben pasar por
   EP-HU-FASE como cualquier desarrollo. El usuario lo pidió al ver
   que un arreglo se publicó sin probarse por no tener fase.

   Nace 02·F23 y se corrigen los dos procedimientos que autorizaban
   lo contrario: los nueve pasos del capítulo 20 y el §2 del
   CLAUDE.md. Queda la HU-016 de EP-004 para su validador.

2 · Rellena los marcadores al copiar en la instalación (21.1.0)

   Un proyecto reportó que el enlace a la regla F13 de su
   stack-instalacion.md no abría.

   De los cuatro sitios donde el instalador copia, tres escribían
   la plantilla cruda. Los tres pasan por _rellenar(). Nace la
   primera prueba del repositorio, que instala en una carpeta
   desechable y comprueba que no quede ningún marcador del
   instalador. Fase A-EP-007-HU-001, veredicto Cumple.

3 · Resuelve el marcador contra el estándar y no contra la raíz (21.1.1)

   El mismo enlace daba un veredicto distinto según desde qué
   carpeta se corriera el revisor.

   enlaces.py lo resolvía contra la raíz que validaba, y corriendo
   sobre un proyecto esa raíz no es el estándar. Se comprobó que la
   salida sobre el propio estándar queda idéntica. Fase
   A-EP-004-HU-005, veredicto Cumple.

4 · Deja escrito lo que la sesión dejó

   La transcripción y el resumen con los tres hallazgos, sus
   pendientes y las historias que disparan.
```

Archivos, sin `pendientes/README.md` ni nada de la otra sesión:

| Commit | Archivos |
|---|---|
| 1 | `base/02-flujo-de-trabajo/` (base + F23), `base/20-meta-reglas/base.md`, `CLAUDE.md`, `validadores/reglas-validables.md`, HU-016 y los índices de EP-004, `CHANGELOG` + `VERSION` |
| 2 | `validadores/instalar.py`, `validadores/tests/test_instalar_marcadores.py`, `validadores/docs/instalar.md`, la fase A-EP-007-HU-001, HU-001 y su README, `pendientes/40`, `CHANGELOG` + `VERSION` |
| 3 | `validadores/enlaces.py`, `validadores/tests/test_enlaces_marcador.py`, `validadores/docs/enlaces.md`, la fase A-EP-004-HU-005, HU-005 y su README, `pendientes/41`, `CHANGELOG` + `VERSION` |
| 4 | `historico-chat/2026-08-16-un-pendiente-no-es-un-plan.md`, su resumen, los dos índices, y el borrado de `sesion-5.md` |

¿Le doy así, o prefieres otra división?

### 22 · Usuario — 2026-08-16 18:21:28
> si

**Agente** — 2026-08-16 18:24:40
<!-- agente: 98feb9fb-5c2a-450a-9e6c-2ed46fed4972 -->

Cuatro commits, cada uno con su versión. Sin push — eso se pide aparte.

```
bd56000  Deja escrito lo que la sesion dejo
a22f37f  Resuelve el marcador contra el estandar y no contra la raiz que revisa   21.1.1
fe6c579  Rellena los marcadores al copiar en la instalacion                       21.1.0
77db52b  Ejecuta un pendiente como fase de una historia de usuario                 21.0.0
```

Los enganches pasaron en los cuatro: versionado y mensaje, `OK: sin incumplimientos`. Las 12 pruebas siguen verdes.

Lo que quedó **sin commitear es todo de la otra sesión**, tal como acordamos:

| Archivo | Por qué |
|---|---|
| `pendientes/README.md` | mezcla mis filas 40 y 41 con las suyas |
| `pendientes/42-…md` | su pendiente, todavía sin subir |
| `pendientes/22-…md` · `pendientes/hecho/enlaces-…md` | los editó ella |
| Las dos transcripciones y resúmenes del 2026-08-16 | sus sesiones |

Vale la pena avisarle a esa sesión que el `README` la está esperando: mientras no lo suba, el cierre del 40 y del 41 no queda registrado en el índice del backlog.

### 23 · Usuario — 2026-08-16 18:29:10
> que hago?

**Agente** — 2026-08-16 18:29:23
<!-- agente: 70505c43-8285-442a-a82b-0b044120e651 -->

Tres cosas, en orden:

**1 · En la otra sesión, pídele que suba lo suyo.** Tiene `pendientes/README.md` sin commitear con mis filas adentro, su pendiente 42, y dos enlaces rotos que dejó: apunta a `34-las-plantillas-enlazan-una-carpeta-base-que-el-proyecto-no-tiene.md`, que ya se movió a `hecho/`. Mientras no lo suba, el cierre del 40 y del 41 no aparece en el índice del backlog.

**2 · Acá, decide si publicas.** Los cuatro commits están en `main` local. `git push` es acción aparte y no la he hecho.

**3 · Lo siguiente natural es el [pendiente 42](pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md)** — es `P0` y es el que deja el trabajo de hoy a medias: los proyectos nuevos nacen bien, los viejos siguen con los enlaces muertos y reinstalar no los repara.

Si me dices cuál, sigo.

### 24 · Usuario — 2026-08-16 18:30:16
> cual otra sesion?

**Agente** — 2026-08-16 18:30:42
<!-- agente: 62598274-a265-403c-8545-a6260b05d5ce -->

Es una sesión tuya de Claude Code corriendo en paralelo sobre este mismo repo. La evidencia:

**Dos commits que no hice yo**, mientras esta sesión trabajaba:

```
18:01  f19b821  Recibe dos defectos que reporta shopnest-mesa       (pendientes 43 y 44)
18:06  fc36e73  Anota que el desfase del 44 crece con cada publicacion
```

**Y dos transcripciones que siguen escribiéndose**, las dos con una pregunta abierta al final:

- [2026-08-16-que-pendientes-trabajamos.md](historico-chat/2026-08-16-que-pendientes-trabajamos.md) — *«Ese cambio del resumen quedó sin commitear, es una línea. Si querés lo sumo»*
- [2026-08-16-por-que-dice-instalacion-incompleta.md](historico-chat/2026-08-16-por-que-dice-instalacion-incompleta.md) — *«¿La subo y con eso terminamos?»*

Esa —o esas— son las que escribieron el pendiente 42 y editaron `pendientes/README.md` mientras yo lo editaba. Si están cerradas, sus archivos quedaron a medio guardar y los puedo subir yo. Si siguen abiertas en otra ventana, ahí es donde hay que contestar esas dos preguntas.

¿Las tienes abiertas todavía?

### 25 · Usuario — 2026-08-16 18:31:45
> no

**Agente** — 2026-08-16 18:32:28
<!-- agente: a266b266-14b2-457b-880a-cbb9a9e786e2 -->

Entonces sus archivos quedaron a medio guardar, y se pierden si nadie los sube. Propongo cerrarlo yo:

**1 · Arreglar los dos enlaces rotos que dejó.** Los dos apuntan a `34-las-plantillas-enlazan-una-carpeta-base-que-el-proyecto-no-tiene.md`, que ya no existe: el pendiente 34 se cerró y su archivo es [hecho/enlaces-de-las-plantillas-al-estandar.md](pendientes/hecho/enlaces-de-las-plantillas-al-estandar.md). Es cambiar el destino en [pendientes/44](pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md) y en la fila 190 del [índice](pendientes/README.md).

**2 · Subir lo que dejó**, en un commit aparte del mío para que se vea de dónde salió:

| Archivo | Qué es |
|---|---|
| `pendientes/42-…md` | el pendiente nuevo, sin subir |
| `pendientes/README.md` | sus filas 42, 43 y 44, el 34 pasado a «hecho a medias», y mis filas 40 y 41 |
| `pendientes/22-…md` · `pendientes/hecho/enlaces-…md` | lo que anotó en cada uno |
| Las dos transcripciones y sus resúmenes | el registro de esas sesiones |

Va todo junto porque es de las mismas sesiones; separarlo más no aporta.

Después de eso el repositorio queda en verde: **0 fallas**.

¿Lo hago?

### 26 · Usuario — 2026-08-16 18:42:12
> si

**Agente** — 2026-08-16 18:43:11
<!-- agente: 7f5b188c-865d-4bfc-9262-fc27b210dc16 -->

Hecho. **0 fallas** en todo el repositorio.

```
b1044ba  Rescata lo que dejaron sin guardar dos sesiones cerradas
bd56000  Deja escrito lo que la sesion dejo
a22f37f  Resuelve el marcador contra el estandar y no contra la raiz     21.1.1
fe6c579  Rellena los marcadores al copiar en la instalacion              21.1.0
77db52b  Ejecuta un pendiente como fase de una historia de usuario       21.0.0
```

Lo rescatado: el pendiente 42, lo anotado en el 22 y en el 34, las dos transcripciones con sus resúmenes, y los dos enlaces rotos corregidos. Lo único sin commitear es la transcripción de esta sesión, que el enganche sigue escribiendo mientras hablamos.

`estandar`, `versionado` y `trazabilidad` en verde; las 12 pruebas pasan.

Queda sin hacer, y no es poco:

- **[Pendiente 42](pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md), `P0`** — los proyectos ya instalados siguen con los enlaces muertos y reinstalar no los repara. Es lo que deja el trabajo de hoy a medias.
- **[Pendiente 44](pendientes/44-el-registro-de-version-no-se-escribe-si-no-cambia-una-huella.md), `P0`** — lo mismo por el lado del registro de versión.
- **`git push`** — no lo hice; se pide aparte.

### 27 · Usuario — 2026-08-16 18:44:12
> ya se solucionó?

**Agente** — 2026-08-16 18:44:21
<!-- agente: 47f19208-ce63-48dd-b694-f142d857f397 -->

Depende de qué:

**Sí quedó solucionado** — el defecto que reportó el proyecto: los tres puntos de copia rellenan, el revisor de enlaces resuelve bien, y la regla `F23` cierra el hueco de proceso que lo produjo. Todo probado y commiteado.

**No quedó solucionado** — que eso llegue a los proyectos que ya estaban instalados. Un proyecto instalado antes de hoy sigue con sus enlaces muertos, y reinstalar **no** los repara: la huella se calcula del stack central, así que el instalador dice «ya estaba al día» y no reescribe. Eso es el [pendiente 42](pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md), y sigue abierto.

O sea: **los proyectos nuevos nacen bien; los viejos siguen rotos.**

Si preguntabas por otra cosa, dime cuál.

### 28 · Usuario — 2026-08-16 18:44:42
> ningún depende eso me sirve si o no?

**Agente** — 2026-08-16 18:44:47
<!-- agente: 3d751af8-39c5-49d5-8b2c-c7719a4d95af -->

**No.**

El proyecto que lo reportó sigue con el enlace muerto. Se arregló para los que se instalen de ahora en adelante, no para los que ya estaban — y ese era el caso real.

Falta el [pendiente 42](pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md). ¿Lo trabajo?

### 29 · Usuario — 2026-08-16 18:45:06
> si

### 30 · Usuario — 2026-08-16 18:45:33
> ya podemos cerrar esta sesión?

### 31 · Usuario — 2026-08-16 18:46:01
> siga

**Agente** — 2026-08-16 18:46:24
<!-- agente: 7a014fc2-a8c1-4cae-a61d-fd6e173a9e17 -->

**Sí, la sesión cierra.** Las cuatro casillas del [resumen](historico-chat/resumenes/2026-08-16/un-pendiente-no-es-un-plan.md) están marcadas.

Lo que deja:

| | |
|---|---|
| Regla nueva | [`02·F23`](base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md) — un pendiente se ejecuta como fase de una HU |
| Pendientes cerrados | 40 y 41, los dos con su fase y veredicto Cumple |
| Historia nueva | [EP-004 · HU-016](documentacion/epicas/EP-004-comprobacion-automatica/HU-016-el-pendiente-cerrado-nombra-su-fase/), el validador de `F23` |
| Código | las primeras 12 pruebas del repositorio |
| Versión | 21.1.1 · cinco commits, del `77db52b` al `b1044ba` |

Falta commitear esa casilla que acabo de marcar, y la transcripción que el enganche sigue escribiendo. Te lo dejo en un commit cuando digas.

Y para retomar, lo primero es el [pendiente 42](pendientes/42-el-arreglo-del-40-no-llega-a-los-proyectos-ya-instalados.md): **necesita una decisión tuya**, no trabajo. Trae tres salidas escritas —que la huella mire el archivo copiado, una bandera `--forzar`, o subir la huella a mano— y sin elegir una, `shopnest-mesa` se queda con su enlace roto.
