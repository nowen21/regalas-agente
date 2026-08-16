<!-- sesion: 9e1e3677-5bf9-4852-a337-7aa604a2bf96 -->

# 2026-08-08 — El nombre de la sesion y las marcas de ia

## Conversación

### 1 · Usuario — 2026-08-08 23:01:32
> puedo hacer que cada que abra una sesion me pida el nombre como se va a guardar?

**Agente** — 2026-08-08 23:02:43
<!-- agente: e657de9c-2c8c-4daf-8cbb-16baf91d0512 -->

Sí, pero no lo puede hacer el hook: un `SessionStart` corre sin consola, no puede preguntar nada. Lo que sí puede es **inyectar la orden de que yo pregunte** en el chat antes de responder.

Hoy [historico.py:171-186](validadores/historico.py#L171-L186) crea `AAAA-MM-DD-sesionN.md` sola, y el hilo lo lleva la marca `<!-- sesion: <id> -->`, no el nombre — o sea que **el archivo se puede renombrar en cualquier momento** sin perder nada. Por eso hay tres caminos:

| Camino | Cómo se ve | Costo |
|---|---|---|
| **A** — el hook de `SessionStart` agrega "pregunta el nombre antes de responder" | primera respuesta de la sesión es una pregunta | un turno extra siempre, y al minuto cero el tema todavía no se sabe |
| **B** — el agente propone el nombre tras el primer intercambio y lo renombra si lo apruebas | "esta sesión la guardo como `2026-08-08-nombre-sesion.md`, ¿va?" | ninguno; el tema ya está claro |
| **C** — comando `/nombrar <tema>` para renombrar cuando quieras | manual | hay que acordarse |

Recomiendo **B**: es lo que arregla el problema real — en el índice hay ocho sesiones que quedaron como "sesión del 2026-08-07" porque nadie las renombró. Pedir el nombre al arrancar no lo evita, porque en ese momento ninguno de los dos sabe de qué va a tratar.

¿Cuál monto?

### 2 · Usuario — 2026-08-09 22:34:18
> B

**Agente** — 2026-08-09 22:46:43
<!-- agente: a4e9478b-57ce-4a36-9ee2-5605a5b616d7 -->

Voy con B. Reviso si hay pruebas de los validadores y escribo el mecanismo.

Ahora el enganche que lo recuerda:

Hecho y probado. Cómo queda:

**El recordatorio** — [historico.py:206](validadores/historico.py#L206) `aviso_de_nombre` y [hook_historico.py:78-81](validadores/hook_historico.py#L78-L81). Si el archivo todavía se llama `AAAA-MM-DD-sesion.md` y la sesión ya tuvo una respuesta, el enganche del `UserPromptSubmit` imprime la instrucción de proponerte nombre y resumen — lo que ese enganche imprime me llega a mí en ese turno. **Una sola vez** (queda `<!-- nombre: preguntado -->` en el archivo), nunca en el primer mensaje, y no renombra nada solo: lo apruebas tú.

**El cambio** — `--renombrar` mueve el archivo, corrige el título y arregla la línea del índice a la vez; a mano se olvidaba el índice y quedaba apuntando a un archivo que ya no está. La fecha sale del nombre viejo, no del reloj. Tildes fuera del nombre del archivo, dentro del título y del índice.

Probado en un proyecto de prueba: no avisa en el primer mensaje, avisa en el segundo, no repite, y el renombre deja archivo + índice + marca de sesión coherentes. Documentado en [plantillas/historico-chat.md](plantillas/historico-chat.md) y [validadores/README.md](validadores/README.md); `VERSION` 6.1.0 con su entrada en [CHANGELOG.md](CHANGELOG.md) (MENOR).

Esta sesión se está guardando como `2026-08-08-sesion-3.md`. La guardo como **`2026-08-08-nombrar-la-sesion.md`** — *el histórico pide su nombre dentro de la sesión: el enganche lo recuerda una vez y `--renombrar` mueve archivo, título e índice (6.1.0)*. ¿Va?

Y aparte: ¿commiteo esto? (solo lo de esta sesión — `pendientes/10-ideas.md`, `validadores/docs/` y los otros históricos son de otras sesiones y no los toco).

### 3 · Usuario — 2026-08-09 23:37:50
> y también queda marcada la pestaña con ese nombre que se le de?

**Agente** — 2026-08-09 23:38:11
<!-- agente: 3ad5cbcc-8bc2-4570-920f-5540b565a13c -->

No. Son dos cosas independientes:

- **El nombre de la pestaña** lo pone Claude Code solo: es un resumen que él genera de la conversación y lo guarda en los datos de la sesión (es el mismo que aparece en la lista de `/resume`). No sale de ningún archivo del repo.
- **El nombre del histórico** es un archivo dentro de `historico-chat/`. Renombrarlo mueve el archivo y su línea en el índice, nada más.

Un enganche tampoco puede tocar la pestaña: lo que un hook imprime entra a la conversación como contexto, no cambia el título de la sesión. Y no hay una entrada documentada para fijarlo desde afuera — por eso lo que armamos actúa donde sí se puede.

Si quieres que coincidan, la vía es al revés: yo propongo el nombre, tú lo apruebas, y la pestaña la renombras tú en VS Code si la extensión lo permite. Puedo revisar la documentación de Claude Code a ver si existe alguna forma de fijar el título de la sesión — dime y la busco antes de darlo por cerrado.

Sigue pendiente lo de antes: ¿te sirve `2026-08-08-nombrar-la-sesion.md` y commiteo?

### 4 · Usuario — 2026-08-09 23:40:59
> pero necesito que también esa pestaña se vea con el nombre para así poder identificar que se está haciendo en esa sesión

**Agente** — 2026-08-09 23:47:44
<!-- agente: 1f763d2f-1c1d-4942-bd57-d6b506bafc38 -->

Corrijo lo que dije antes: **sí existe** — `claude --name "<nombre>"` al arrancar y `/rename <nombre>` a mitad de sesión ([referencia de CLI](https://code.claude.com/docs/en/cli-reference)). El nombre sale en `/resume`, en la barra del prompt y en el título de la sesión. Lo que no puedo es escribirlo yo: `/rename` es un comando tuyo, no una herramienta mía, y ningún enganche puede fijarlo (por eso hay [varias](https://github.com/anthropics/claude-code/issues/23998) [solicitudes](https://github.com/anthropics/claude-code/issues/20441) abiertas para que el título de la pestaña siga al nombre de la sesión).

Entonces lo que sí se puede automatizar es que los dos nombres salgan de la misma propuesta y en el mismo momento. Lo agrego al recordatorio:

Listo, probado: el recordatorio ahora sale con las dos líneas.

Para esta sesión, si te sirve el nombre `nombrar-la-sesion`:

```
/rename nombrar-la-sesion
```

Pégalo y me dices si la pestaña cambió. Si en la extensión de VS Code no cambia (en la barra del prompt y en `/resume` sí debería), la otra vía es abrir la sesión ya nombrada desde el arranque: `claude --name "nombrar-la-sesion"` — la referencia de CLI dice que ese nombre sí va al título de la sesión.

Y siguen pendientes las dos aprobaciones: el histórico como **`2026-08-08-nombrar-la-sesion.md`** — *el histórico pide su nombre dentro de la sesión: el enganche lo recuerda una vez, `--renombrar` mueve archivo, título e índice, y la misma propuesta va como `/rename` (6.1.0)* — y si commiteo.

### 5 · Usuario — 2026-08-09 23:48:14
> pero eso no se replica en los proyectos?

**Agente** — 2026-08-09 23:48:59
<!-- agente: d5549edb-165c-46e5-a631-b5214968829a -->

Sí replica, y sin reinstalar nada. Los proyectos no copian los validadores: su `.claude/settings.json` llama al del estándar con la ruta absoluta —`python "C:/Ing. Jose/ia/agente/validadores/hook_historico.py" --modo usuario --raiz "<proyecto>"` ([instalar.py:203-210](validadores/instalar.py#L203-L210))—. Al cambiar el archivo aquí cambia el comportamiento en todos, y el recordatorio se arma con la ruta del propio archivo, así que el comando que propone sale correcto en cualquier proyecto.

Lo que **no** viaja es el texto: el `historico-chat/README.md` de cada proyecto es de los que el instalador no pisa ([instalar.py:417-438](validadores/instalar.py#L417-L438) — solo le refresca el sello). Los proyectos nuevos nacen con la plantilla nueva; los que ya existen se quedan con su redacción vieja. No afecta el funcionamiento: el recordatorio llega completo, con la orden y la ruta puestas, sin depender de que ese README lo cuente.

Y `/rename` lo pega el usuario, en cualquier proyecto igual — no hay forma de fijarlo desde un enganche.

Si quieres que el texto también viaje, se puede hacer que el instalador **agregue** al README del proyecto la sección que la plantilla sumó, sin tocar el resto — es lo que ya hace con el `CLAUDE.md`. Dime si lo hago ahora o lo dejo en `pendientes/`.

### 6 · Usuario — 2026-08-10 00:24:52
> suba a git todo

**Agente** — 2026-08-10 00:35:06
<!-- agente: 475a601e-74dc-4621-8939-042fb3da8479 -->

`pendientes/10-ideas.md` (de otra sesión) trae justo esta idea como ítem 2 — «que se abra una sesión pida el nombre con el que se va a guardar». Le pongo su línea en el índice, que es lo único que hoy hace fallar al validador:

Subido: `ab314a1` en `main`, 26 archivos.

Fue **un solo commit** y no dos, porque en el árbol estaba sin commitear la v6.0.0 de otra sesión y comparte `CHANGELOG.md` y `VERSION` conmigo — separarlos habría exigido partir esos dos archivos por mitades. Va todo dicho en el cuerpo del commit: primero lo tuyo (6.1.0), después lo que arrastraba el árbol (6.0.0, `base/README.md`, las transcripciones, `pendientes/10-ideas.md`).

Dos cosas que hice sobre trabajo ajeno, para que las revises:

- **`pendientes/README.md`** — le puse la línea de índice a `10-ideas.md`, que faltaba y hacía fallar al validador `estandar`. Ahí anoté que su idea 2 quedó hecha con esto.
- Nada más se tocó de las otras sesiones.

Quedó pendiente lo que no aprobaste: el histórico de esta sesión sigue llamándose `2026-08-08-sesion-3.md`. Cuando digas, corro el renombre a `2026-08-08-nombrar-la-sesion.md` — y de paso me cuentas si `/rename` sí cambió la pestaña.

### 7 · Usuario — 2026-08-12 12:44:33
> en qué archivo dice que sobre los caracteres de ia?

**Agente** — 2026-08-12 12:45:22
<!-- agente: 6fa94fd3-6ffb-4b89-bb65-34ee2365a728 -->

No hay ningún archivo que hable de "caracteres de IA" (la raya `—`, emojis, comillas curvas o lo que delata que un texto lo escribió una IA). Eso no está escrito en el repo.

Lo que sí existe con la palabra *caracteres* es esto — dime cuál buscabas:

| Qué dice | Dónde |
|---|---|
| El asunto del commit va breve; el tope de 72 lo pone el validador, no la regla | [base/09-git.md:16](base/09-git.md#L16) (`09·G2`) · el número, en [validadores/commits.py](validadores/commits.py) (`LARGO_MAXIMO`) · explicado en [validadores/docs/commits.md](validadores/docs/commits.md) |
| Las tildes y eñes se guardaban rotas en el histórico, y por qué se leen como UTF-8 a mano | [validadores/hook_historico.py:45-60](validadores/hook_historico.py#L45-L60) · [validadores/docs/hook_historico.md](validadores/docs/hook_historico.md) |
| Un nombre de tabla o columna de más de 64 caracteres | [validadores/esquema.py:106](validadores/esquema.py#L106) |

Si era otra cosa —por ejemplo una regla sobre cómo debe escribir el agente para no sonar a IA—, lo más cercano es [`00·ID7`](base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md), que manda escribir en palabras de todos los días, pero no menciona caracteres.

### 8 · Usuario — 2026-08-12 12:46:48
> no hay un historico de claude donde lo haya generado?

**Agente** — 2026-08-12 12:50:28
<!-- agente: bb2336e3-ffd5-44ae-9dd8-e2804bae8314 -->

Sí — hay dos históricos: el del repo (`historico-chat/`) y el crudo de Claude Code (`~/.claude/projects/`), que guarda todas las sesiones aunque no se hayan transcrito. Busco en los dos:

Está, pero **en otro proyecto** — por eso no aparecía buscando aquí:

[Marcadores de texto redactado por IA.md](../../Escom/Especialización%20en%20ciberseguridad/MODULO%202.%20SEGURIDAD%20DE%20DATOS/gestion%20de%20servicios%20tecnologicos/Marcadores%20de%20texto%20redactado%20por%20IA.md) — en `C:\Ing. Jose\Escom\Especialización en ciberseguridad\MODULO 2. SEGURIDAD DE DATOS\gestion de servicios tecnologicos\`.

Lo que buscabas es su sección **2 · Puntuación y tipografía**, que abre así: *«La raya larga (—) usada como inciso, y muy seguido. Es el delator número uno en español»*. El archivo tiene seis secciones —léxico y muletillas, puntuación, estructura, contenido y tono, metadatos del archivo, y la más difícil de disimular— ordenadas de la señal más superficial a la menos.

Lo encontré en el histórico crudo de Claude Code (`~/.claude/projects/`), que guarda las 29 sesiones de este proyecto y las de todos los demás, no solo lo transcrito en `historico-chat/`. En el repo del estándar no hay nada de esto: aquí *caracteres* solo aparece por el tope del asunto del commit y por las tildes rotas del histórico.

Dos cosas por si te sirven: puedo traer esa guía a `base/` como regla de redacción (sería el complemento de `00·ID7`, que hoy manda escribir claro pero no dice nada de la raya larga), o dejarla donde está. Y sigue abierto el renombre del histórico de esta sesión.

### 9 · Usuario — 2026-08-12 12:51:09
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\plantillas\estado-fase.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> pasar al agente ese archivo en dentro de una carpeta

**Agente** — 2026-08-12 12:52:25
<!-- agente: f9ef8b6d-4792-4c82-893e-e9eda31521b9 -->

Copiado en [notas/marcadores-de-texto-redactado-por-ia.md](notas/marcadores-de-texto-redactado-por-ia.md), con su línea en el índice de [notas/README.md](notas/README.md). El validador de coherencia pasa.

Tres cosas del cómo:

- **Va en `notas/`** porque ahí es donde el repo guarda lo que explica y documenta sin ser regla; `base/` es solo para lo que se exige.
- **Es copia, no traslado.** El original sigue en `Escom\…\gestion de servicios tecnologicos\`, y lo tiene que seguir estando: el `CLAUDE.md` de ese proyecto lo cita por nombre como su guía de estilo. Moverlo lo habría roto.
- **El texto quedó literal**, sin una palabra cambiada. De dónde salió lo dice la línea del índice.

Ojo con lo que esto implica: en `notas/` es material de consulta, no obliga a nada — ningún agente lo va a leer solo. Si quieres que de verdad cambie cómo escribe, tiene que ser regla en `base/` (capítulo `00`, junto a `ID7`), y ahí hay un choque que vale la pena mirar antes: el propio estándar usa la raya larga y el punto medio por todas partes, que son los marcadores 1 y 3 de la sección de puntuación. Sería regla para lo que el agente le entrega al usuario, no para las reglas mismas.

Dime si la subo a `base/` o la dejo como nota. Y sigue sin commitear esto y sin renombrar el histórico de la sesión.

### 10 · Usuario — 2026-08-12 12:54:39
> listo entonces ahora crea una regla para que todo documento, manual, etc debe evitar todo esos marcadores que dice: marcadores-de-texto-redactado-por-ia y la idea es que todos los proyectos lo repliquen

### 11 · Usuario — 2026-08-12 12:55:16
> la regla debe cumplir el stándard que ya tenemos

**Agente** — 2026-08-12 13:04:53
<!-- agente: 6b938947-5d9e-4306-a352-c73bf1db0750 -->

Sigo el procedimiento de `20·base.md`. La lista tiene que vivir en `base/` — `notas/` no viaja a los proyectos —, así que va como anexo del capítulo y la regla lo cita:

Ahora el índice del capítulo, el registro de validables y la versión:

Verifico que de verdad llegue a los proyectos: el capítulo `00` se carga literal en cada sesión, pero el anexo es un archivo aparte.

Hecho, siguiendo el procedimiento de `20 · Meta-reglas` paso por paso.

**La regla** — [`00·ID8 · Escribe sin las marcas que delatan generación automática`](base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md). Alcanza a documentación, manuales, informes y a cualquier texto que una persona lea como trabajo terminado. `extiende 00·ID7`. Cierra con su checklist aplicado: **CUMPLE**, 19 ✅ y 1 N/A (no tiene excepción).

**La lista** — [`base/00-identidad-y-rol/marcadores-de-ia.md`](base/00-identidad-y-rol/marcadores-de-ia.md), anexo del capítulo con las seis secciones del documento que trajiste, cada marca con qué escribir en su lugar. Va como anexo porque el cuerpo de una regla son cuatro líneas (`20·M5`), y va en `base/` por lo que preguntaste antes: `notas/` no viaja a los proyectos.

**Cómo replica** — comprobado, no supuesto: el cargador mete el capítulo `00` **literal** en el contexto de cada sesión, y ahí entran la regla y el anexo completo. Ningún proyecto tiene que reinstalar ni leer nada a mano. El contexto de arranque pasa de 51 a 59 KB.

Tres decisiones que tomé y conviene que revises:

- **Borré la copia de `notas/`.** Dos copias de la misma lista se desincronizan (`20·M2`); ahora la fuente única es el anexo. El original tuyo en `Escom\` sigue intacto.
- **Qué no cuenta como marca:** la notación que el propio estándar define (`NN·ID`, `[BLINDADA]`, los bloques `INCORRECTO / CORRECTO`), los bloques de código y la salida de herramientas. Sin eso, la regla se chocaba con `20·M4` y `20·M5` desde el primer día.
- **Queda validable parcial** en [`validadores/reglas-validables.md`](validadores/reglas-validables.md): un script puede contar rayas largas, comillas curvas y muletillas de lista cerrada; si el documento suena a máquina lo decide quien lo lee. El validador todavía no existe.

`VERSION` sube a **7.0.0** — es MAYOR: obliga a un proyecto al día a releer contra la lista lo que entregue. Los dos validadores pasan.

Lo que **no** hice y hay que decidir: el texto ya escrito del repo (`base/`, `plantillas/`, los README) usa la raya larga como inciso en todas partes, así que el estándar hoy no cumple su propia regla nueva. Por la cláusula de retroactividad rige para lo que se escriba desde ahora, y limpiar lo anterior es un trabajo aparte. Queda anotado en el `CHANGELOG`. ¿Lo abro como pendiente numerado, o lo hago?

Y sin commitear, como quedamos.

### 12 · Usuario — 2026-08-12 13:08:04
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\00-identidad-y-rol\reglas\ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> faltan más detectores de IA acá:
> marcadores-de-ia?

**Agente** — 2026-08-12 13:08:59
<!-- agente: b80f28e7-ed26-4533-8d0f-f1247b4a9ea5 -->

Sí, faltan. Revisé la lista contra lo que de verdad delata a un texto en español y encontré cuatro huecos grandes y una sección que no existe:

| Dónde | Qué falta |
|---|---|
| **1 · Palabras** | Conectores cultos de relleno: *Asimismo, Por ende, En definitiva, Sin lugar a dudas, Cabe resaltar*. Duplas sinónimas: *claro y conciso, rápido y eficiente, sólido y confiable*. La construcción *«No es X, es Y»* y *«Más que X, es Y»*. Verbos calcados del inglés: *implementar, optimizar, maximizar, impulsar, profundizar en*. El eufemismo *desafío* por problema y *oportunidad de mejora* por defecto. El cierre servicial: *«Espero que esto te sirva»*, *«¡Éxitos!»*. Y el subtítulo en forma de pregunta retórica: *«¿Qué significa esto?»*, *«¿Por qué importa?»* |
| **2 · Tipografía** | La flecha `→` y el visto `✓` como viñeta. Los puntos suspensivos como carácter único (`…`) en vez de tres puntos. Comillas angulares `« »` mezcladas con las otras. Títulos con Mayúscula En Cada Palabra, que es calco del inglés. Negrita sobre frases enteras en vez de sobre una palabra. Separador `---` entre todas las secciones |
| **3 · Estructura** | Listas numeradas para cosas que no llevan orden. El trío *Introducción / Desarrollo / Conclusión* completo. Índice o resumen ejecutivo en un documento de una página. Cerrar siempre con *«Próximos pasos»* |
| **4 · Contenido** | Repetir la pregunta antes de responderla. Neutralidad de oficina: ventajas y desventajas siempre en el mismo número. Cifras redondas sin fuente (*«mejora un 30%»*). Ejemplos de manual: *Juan Pérez, empresa XYZ, ejemplo.com*. Advertencias genéricas del tipo *«consulta a un profesional»* |
| **7 · (sección nueva)** | **Marcas invisibles**, que no se ven leyendo y se encuentran buscando: espacio duro (`U+00A0`), caracteres de ancho cero, guion suave. Son las que sobreviven a cualquier reescritura, y son justo las que un script sí puede contar |

La séptima es la que más valor agrega: es la única categoría que un validador detecta sin equivocarse, y hoy la regla dice que su parte mecánica es validable.

Ojo con una consecuencia si las agrego: la lista pasa de 30 a unas 60 marcas, y varias de las nuevas aparecen en el propio repo. La flecha `→` está en las tablas de `validadores/`, y `«Próximos pasos»` es un encabezado que usan las plantillas de fase. Habría que decidir caso por caso si entran a la lista o a la excepción de notación definida.

¿Las agrego? Si sí, sube a **7.1.0** (aditivo: la regla no cambia, crece su instrumento) y hay que rehacer el checklist de `ID8`, porque editar el anexo no anula el resultado pero conviene revisar la fila 17 con las marcas nuevas.

### 13 · Usuario — 2026-08-12 13:15:27
> los texto deben ser redactados en español colombiano teniendo en cuenta las normas ortográficas, estructuras gramaticales, sintaxis, etc. Eso se está teniendo en cuenta?

### 14 · Usuario — 2026-08-12 13:16:33
> por ahora no modifique la regla, estamos construyendo este documento:
> marcadores-de-ia

**Agente** — 2026-08-12 13:19:27
<!-- agente: b423ac24-d9d7-46b8-8224-86a92e43c5a2 -->

No, no se está teniendo en cuenta. Lo único que hay hoy es [`01·C8 · Habla el idioma del proyecto`](base/01-conducta.md#c8--habla-el-idioma-del-proyecto), que fija **el idioma** y nada más: no dice variedad, ni ortografía, ni gramática, ni sintaxis. Exigir español de Colombia con norma correcta necesita regla propia, y eso lo dejo para cuando me digas que puedo tocar `reglas/`.

Lo que sí cabe en este documento es la otra cara: el español neutro de traducción y el léxico de España son de los delatores más fuertes acá. Lo agrego junto con lo que faltaba:

El documento pasó de 30 marcas en 6 secciones a **62 en 8**. Lo que entró:

- **1 · Palabras** — conectores cultos (*Asimismo, Por ende, Sin lugar a dudas*), duplas sinónimas, la construcción *«No es X, es Y»*, eufemismos de oficina, subtítulos en pregunta retórica y el cierre servicial.
- **3 · Marcas invisibles** *(sección nueva)* — espacio duro, ancho cero, guion suave, `…` como carácter único, semiraya. Es la única categoría que un script cuenta sin equivocarse, y va temprano por eso.
- **4 · Estructura** — listas numeradas para lo que no lleva orden, el trío *Introducción / Desarrollo / Conclusión*, índice en un documento de una página, *«Próximos pasos»* automático.
- **5 · El español que no es de acá** *(sección nueva)* — responde tu pregunta por el lado que sí cabe acá: léxico de España, *vosotros*, pretérito compuesto donde va el simple, mezclar *usted* y *tú*, calcos del inglés y el español neutro sin acento de ninguna parte.
- **6 · Contenido** — repetir la pregunta antes de responder, cifras redondas sin fuente, ejemplos de manual (*Juan Pérez, empresa XYZ*), advertencias genéricas.

Dos cosas que resolví al escribirlo, por si no estás de acuerdo:

**Reescribí la marca «cero errores».** Como estaba, chocaba de frente con lo que me preguntaste: si la norma exige ortografía correcta, no se puede pedir que el texto traiga errores. Ahora dice que lo que delata es el alisado —densidad pareja, ninguna frase que se salga— y deja escrito que no se meten errores a propósito.

**La flecha `→` y «Próximos pasos» quedaron en la excepción**, no en la lista: cuando son notación de una tabla o sección que pide una plantilla, se usan. Lo que delata es ponerlas de adorno.

Al final agregué **«Lo que este anexo no cubre»**, que deja por escrito el hueco: la norma del español no está en el estándar. `01·C8` fija el idioma y nada más. Eso pide regla propia.

No toqué `ID8` ni la versión, como pediste. Cuando digas, la regla y el `CHANGELOG` quedan al día en un solo paso — hoy el `CHANGELOG` de la 7.0.0 dice "seis secciones" y ya son ocho.

### 15 · Usuario — 2026-08-12 13:23:41
> listo siga

**Agente** — 2026-08-12 13:25:20
<!-- agente: 04184db6-2a39-4d68-a220-d5a92ecc5c66 -->

Cerrado el bloque de la 7.0.0. Lo que faltaba:

- **La excepción que se me había pasado.** El checklist del estándar obliga a poner ✅ ❌ N/A en la tabla de resultado de cada regla, y la sección 2 marca los emojis en documento formal. Chocaban. Ahora los ✅ ❌ de esa tabla están nombrados en «Lo que no es un marcador», junto con los `[BLINDADA]` y los bloques `INCORRECTO / CORRECTO`.
- **`CHANGELOG` al día.** Corregí la entrada de la 7.0.0 en vez de abrir una 7.1.0: la 7.0.0 nació en esta sesión y todavía no está commiteada, así que no hay versión publicada que enmendar. Ahora dice 62 marcas en ocho secciones, nombra las dos secciones nuevas y deja escrito el hueco de la norma del español.
- **Nuevo pendiente [11](pendientes/11-limpiar-marcadores-de-ia-del-texto-del-estandar.md)**, con su línea en el índice: limpiar del propio estándar las marcas que `ID8` prohíbe. Dice qué contar, por dónde empezar (`base/` y `plantillas/`, que son lo que se hereda), qué no tocar (el histórico es transcripción literal) y que reescribir una regla anula su checklist. Depende del validador mecánico de `ID8`: a mano sobre 200 archivos no se hace.

`ID8` quedó igual, como pediste. Su checklist sigue válido: lo que se editó fue el anexo, y el resultado caduca con el texto de la regla.

Los dos validadores pasan. El aviso de `CLAUDE.md` es de siempre: este repo es el estándar y no declara versión adoptada.

Sin commitear. El árbol tiene 9 archivos, todos de esta sesión: la 7.0.0 completa más el histórico. ¿Los subo?
