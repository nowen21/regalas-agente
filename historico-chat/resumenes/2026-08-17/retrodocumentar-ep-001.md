# 2026-08-17 · lo que quedó

Hallazgos de la sesión transcrita en [historico-chat/2026-08-17-retrodocumentar-ep-001.md](../../2026-08-17-retrodocumentar-ep-001.md). Cómo se llena está en [historico-chat/README.md](../../README.md). La conversación está allá; acá queda lo que la sesión dejó.

**El nombre quedó corto:** la sesión se guardó como «retrodocumentar EP-001» cuando iba por esa épica, y terminó cubriendo **las 51 filas** de las siete. Se dejó el nombre para no romper las citas que ya lo usan.

**Viene de:** el [inventario de HU del 2026-08-16](../2026-08-16/el-inventario-de-hu.md), que dejó el paso 2 del pendiente [48](../../../pendientes/48-inventario-hu.md) sin decidir y las 51 filas sin arrancar.

---

## Hallazgos de esta sesión

### H-1 · Ninguna fase estaba sin `plan_trabajo`: lo que faltaba era la fase entera

- **Qué pasó:** se pidió el `plan_trabajo` «de las fases que no lo tienen». Contadas contra el disco, las diecinueve fases que existían **ya lo tenían todas**. Lo que falta es distinto: 51 HU no tienen ninguna carpeta de fase, y tres tienen la fase sin su `funcionalidad_implementada`.
- **Por qué importa:** el pedido no tenía destino literal, y ejecutarlo tal cual habría sido no hacer nada. El destino real es la columna `plan_trabajo` de las 51 filas del [48](../../../pendientes/48-inventario-hu.md) — abrir la fase y escribirle el plan.
- **Qué se decidió:** llenar la columna en el orden del tablero, empezando por EP-001, y que cada carpeta de fase nazca con su `plan_trabajo.md` adentro. Se hicieron las **siete** filas de EP-001: HU-003 a HU-008 y HU-010.
- **Estado:** resuelto acá. La primera tanda fue EP-001; las otras 44 filas se hicieron en la misma sesión, y quedan cero.
- **Dónde queda:** siete carpetas de fase nuevas bajo [EP-001](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/), cada una con su `plan_trabajo.md` y su `README.md` (`13·DOC17`); la §8 de cada HU nombra su fase; las casillas **Fase** y **`plan_trabajo`** marcadas en el [48](../../../pendientes/48-inventario-hu.md).
- **Nace en:** 2026-08-17
- **Con qué se retoma:** la columna `plan_pruebas` de las 51 filas, esa sí fila por fila.

### H-2 · El paso 2 del inventario quedó decidido, y el llenado pasó de fila a columna

- **Qué pasó:** la sesión anterior dejó abierta la pregunta de con qué archivo se hace visible una fase recién abierta, porque git no guarda carpetas vacías. La instrucción de esta sesión la resuelve: el `plan_trabajo` se escribe de una, así que **no hay momento en que la carpeta exista vacía**. Es la tercera de las tres salidas.
- **Por qué importa:** desbloquea las 51 filas, que estaban detenidas esperando esa decisión. Y cambia el orden: el paso 1 pide una fila a la vez, y pedir el `plan_trabajo` de todas es recorrer la columna.
- **Qué lo soluciona:** el paso 2 de la plantilla [`inventario-hu.md`](../../../plantillas/inventario-hu.md) todavía dice «se crea la carpeta y se marca Fase», sin más. Ponerlo al día es cambio de `plantillas/`: entrada en el `CHANGELOG` y subida de `VERSION` (`20·M10`).
- **Qué se decidió:** registrar la decisión y el cambio de orden en el propio [48](../../../pendientes/48-inventario-hu.md), con su costo dicho: cada fila queda a medias hasta que le entren los otros cuatro documentos, y mientras no exista su `estado-fase`, lo que dice qué falta es el `README.md` de la carpeta. La plantilla **no se tocó**, porque sube versión y eso se aprueba aparte.
- **Estado:** resuelto acá, con la plantilla pendiente.
- **Dónde queda:** pendiente [48](../../../pendientes/48-inventario-hu.md), reemplazando el bloque de las tres salidas.
- **Nace en:** 2026-08-16 · el inventario de HU
- **Cerrado en:** 2026-08-17
- **Con qué se retoma:** ¿se pone al día el paso 2 de la plantilla en la próxima subida de versión, o se hace ya con su propia entrada?

### H-3 · `metareglas.py` tampoco tiene punto de entrada — y es el que más pesa

- **Qué pasó:** al verificar la línea base de HU-003 se escribió que `metareglas.py` comprueba que ninguna regla normal mande sobre una `[BLINDADA]`. Se fue a correrlo: `python validadores/metareglas.py` no imprime nada y sale con código 0, y `validar.py` no tiene subcomando para él. La afirmación era falsa y se corrigió en el plan antes de seguir.
- **Por qué importa:** es el segundo caso del pendiente [53](../../../pendientes/hecho/ningun-validador-termina-en-silencio.md) y pesa más que el primero. Es el único programa que decide once de las veinte filas del checklist del estándar —incluida la 5, que sostiene `M3`, y la 15, que protege el núcleo— y además `M16`, el respaldo de toda regla de proyecto. El pendiente [19](../../../pendientes/19-el-capitulo-20-no-se-cumple-a-si-mismo.md) cita una medición hecha con él el 2026-08-14: hoy no se puede repetir desde la línea de comandos.
- **Qué lo soluciona:** ya está escrito en el punto 2 del 53. No hace falta pendiente nuevo: sería el tercero sobre lo mismo.
- **Qué se decidió:** anotarlo como segundo caso en el 53, y que los planes de HU-006, HU-007 y HU-008 digan qué mitad de su comprobación no se puede correr, en vez de darla por hecha.
- **Estado:** anotado
- **Dónde queda:** pendiente [53 · punto 2](../../../pendientes/hecho/ningun-validador-termina-en-silencio.md)
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿se revisan los treinta programas de una, o se le pone punto de entrada solo a los que alguien cita como comprobación?

### H-4 · El CA-02 de HU-010 hablaba de dos fases; son diecisiete

- **Qué pasó:** [HU-010](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) y el pendiente [20](../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md) dicen que hay **dos** fases abiertas sin especificación aparte. Contada la casilla de las veinticinco fases que hay hoy: **nueve** se apoyan en su historia de usuario y **ocho** declararon que no existe y la anotaron como deuda.
- **Por qué importa:** seis de esas nueve nacieron en esta misma sesión. Retro-documentar EP-001 multiplicó por cuatro el caso que `02·F2` no cubre, y con un criterio que ninguna regla respalda todavía. Un criterio que se repite nueve veces ya no es una excepción: es costumbre.
- **Qué lo soluciona:** la fase que se abrió para HU-010, [`A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion`](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/A-EP-001-HU-010-cuando-la-historia-hace-de-especificacion/plan_trabajo.md), con la cuenta al día y las tres dudas que la bloquean.
- **Qué se decidió:** corregir la cuenta en la §8 de la HU y dejarla medida en el plan de la fase. **El pendiente 20 no se tocó:** su decisión de fondo —excepción a `F2` o aceptar que la historia hace de especificación— es del usuario, y es la duda 1 de esa fase.
- **Estado:** abierto, con su fase escrita
- **Dónde queda:** §8 de [HU-010](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) y §2 del plan de su fase
- **Nace en:** 2026-08-14 · pendiente [20](../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md)
- **Con qué se retoma:** ¿`F2` lleva excepción con sus tres partes, o acepta en su texto que la historia hace de especificación cuando el entregable no es código?

### H-5 · Dos de las siete HU no eran retro-documentación

- **Qué pasó:** el inventario dice «casi todo es retrodocumentación». Verificando fila por fila salió que no todas: en [HU-004](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-004-conducta-de-la-ia/HU-004-conducta-de-la-ia.md), dos de sus siete reglas de negocio **no son regla del estándar** —viven como preferencia del usuario en [`historico-chat/memory/`](../../memory/memory.md)—, y [HU-010](../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) no tiene nada construido.
- **Por qué importa:** escribir un `plan_trabajo` que diga «esto ya está» sobre algo que no está es el mismo defecto que el trabajo viene a corregir, al revés. Y un recuerdo no viaja: un proyecto que hereda recibe `base/`, no `historico-chat/`.
- **Qué se decidió:** cada plan declara su origen con lo que de verdad es — cinco retro-documentan, HU-004 es híbrido y HU-010 es funcionalidad nueva. Subir los dos recuerdos a regla es cambio de `base/`, y quedó como duda 1 del plan de HU-004: la decide el usuario.
- **Estado:** resuelto acá
- **Dónde queda:** el campo ORIGEN de los siete planes, y el `README.md` de cada carpeta de fase
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿la pregunta que no es orden y el defecto que se corrige sin preguntar suben a regla del capítulo `01`?

### H-6 · La suite está roja por trabajo de otra sesión sin guardar

- **Qué pasó:** `python validadores/pruebas.py` da **3 fallas de 246** y `validar.py estandar` da 3 fallas más un aviso. Ninguna es de esta sesión: el índice de `pendientes/README.md` no menciona los pendientes 42 y 44, el 44 tiene un enlace roto a otro repositorio, y `estructura-regla.md` cita `G9` sin enlace. Vienen del cambio sin guardar que dejó la sesión del 2026-08-16.
- **Por qué importa:** con la suite roja de antemano, el verde de lo nuevo no se puede leer. Se midió el estado **antes** de escribir, y después: los mismos números, ni una falla ni un aviso nuevo por los catorce archivos de esta sesión.
- **Qué se decidió:** no tocarlo. Es trabajo de otra sesión sin commitear, y pisarlo es el defecto del H-2 del [2026-08-16](../2026-08-16/las-hu-sin-su-fase.md).
- **Estado:** anotado
- **Dónde queda:** acá, como el estado de partida contra el que se comparó
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿se guarda o se descarta lo que quedó suelto de la sesión anterior antes de seguir con EP-002?

### H-7 · Las 51 filas quedaron con su fase abierta y su plan escrito

- **Qué pasó:** después de EP-001, el usuario pidió completar la tarea sin más preguntas. Se abrieron las **44 filas restantes** —EP-002 (6), EP-003 (6), EP-004 (13), EP-005 (8), EP-006 (7) y EP-007 (4)—, cada una con su carpeta de fase, su `plan_trabajo.md` y su `README.md`.
- **Por qué importa:** `validar.py fases` pasó de **19 HU sin ninguna fase a cero**. Los 54 avisos que quedan ya no dicen «sin fases»: dicen qué documento le falta a cada fase — 51 con sus cuatro pendientes y 3 con solo el cierre.
- **Qué se decidió:** de la sexta fila en adelante los planes se escribieron con un molde común y el contenido verificado de cada HU puesto a mano. El molde es lo repetido —las catorce secciones de `F14`, las respuestas que no cambian—; la línea base de cada una se verificó contra el repositorio, una por una.
- **Estado:** resuelto acá
- **Dónde queda:** 51 carpetas de fase nuevas, la §8 de las 51 HU y las 68 filas del [48](../../../pendientes/48-inventario-hu.md) con **Fase** y **`plan_trabajo`** marcadas
- **Nace en:** 2026-08-17
- **Con qué se retoma:** la columna siguiente es `plan_pruebas`, y esa sí conviene ir por fila: un plan de pruebas sin su corrida no sirve de nada.

### H-8 · Catorce de las 51 no eran retro-documentación

- **Qué pasó:** el inventario dice «casi todo es retrodocumentación». Verificando fila por fila salió la cuenta real: **37 retro-documentan** lo que ya corre, y **14 construyen algo que no existe** — entre ellas el enmascarado de claves, el conteo de hallazgos por regla, la corrida completa, quién manda sobre la versión y el aviso del número de pendiente repetido.
- **Por qué importa:** un `plan_trabajo` que dijera «esto ya está» sobre algo que no está es el mismo defecto que este trabajo viene a corregir, al revés. Cada plan declara en su ORIGEN lo que de verdad es: retro-documentación, construcción o híbrido.
- **Qué se decidió:** que la cuenta quede escrita acá, porque el inventario la afirma al revés.
- **Estado:** resuelto acá
- **Dónde queda:** el campo ORIGEN de los 51 planes
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿se corrige la frase del [48](../../../pendientes/48-inventario-hu.md) para que diga 37 y 14 en vez de «casi todo»?

### H-9 · Cinco huecos que aparecieron al verificar, sin pendiente propio

- **Qué pasó:** verificar la línea base de 51 HU destapó cinco cosas que nadie había escrito:
  1. **Nada comprueba `20·M10`** al guardar: ningún enganche corre en el commit, y la fila 19 del checklist vive en el programa que no se puede correr.
  2. **Las señales viven en una base binaria.** Está en el repositorio y en el historial se ve que cambió, no qué cambió.
  3. **Ningún modelo de cierre pide la versión** bajo la que cerró la fase, así que el sello se escribe cuando alguien se acuerda.
  4. **La lista de puntos de aprobación no está en `base/`:** vive en la tabla de estaciones del director, así que un proyecto que hereda recibe las reglas sueltas y no la lista.
  5. **El aviso de desfase no dice qué cambió** entre las dos versiones, que es la tercera parte de su regla de negocio.
- **Por qué importa:** los cinco son huecos de fondo, y ninguno tenía dónde estar escrito. Ahora cada uno vive en el plan de la fase que le toca, con su línea base medida.
- **Qué se decidió:** no abrir pendientes nuevos. Cada hueco quedó en el `plan_trabajo` de su fase, que es donde `02·F23` dice que se trabaja.
- **Estado:** anotado
- **Dónde queda:** los planes de EP-002 · HU-004 y HU-005, EP-003 · HU-008, EP-004 · HU-011 y EP-006 · HU-002
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿alguno de los cinco sube de prioridad por encima de llenar el resto del tablero?

### H-10 · El plan de trabajo no crea nada, y sin su plan de pruebas no se puede aprobar

- **Qué pasó:** el usuario preguntó si el `plan_trabajo` se encarga de crear el `plan_pruebas` y los demás. No: es un documento que dice qué se va a hacer, y cada uno de los otros cuatro lo escribe quien ejecuta la fase, en su momento.
- **Por qué importa:** [`02·F4`](../../../base/02-flujo-de-trabajo/reglas/F4-todo-plan-lleva-su-plan-de-pruebas-y-su-aprobacion-explicita.md) pide **los dos documentos juntos** —plan de trabajo y plan de pruebas— y después la pausa y el visto bueno. Llenar la columna `plan_trabajo` de las 51 filas dejó cada una **un documento antes de poder aprobarse**: no es que falte para después, es que la aprobación es de los dos.
- **Qué lo soluciona:** escribir el `plan_pruebas` de cada fase antes de pedir su aprobación. Y el orden de columnas del [48](../../../pendientes/48-inventario-hu.md) —paso 3: los documentos se escriben en el orden de las columnas— no dice que las dos primeras se aprueban juntas.
- **Qué se decidió:** sin decidir. Se le pasaron al usuario las dos salidas —los 51 planes de pruebas también por columna, o de acá en adelante fila por fila— con la segunda recomendada. Nada se escribió mientras tanto.
- **Estado:** abierto
- **Responde a:** el H-2, que ya dejó dicho el costo de recorrer la columna en vez de la fila.
- **Dónde queda:** acá, y el paso 3 del [48](../../../pendientes/48-inventario-hu.md) cuando se decida
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿el `plan_pruebas` se escribe por columna o fila por fila, junto a su plan, para poder aprobar los dos?

### H-11 · El primer commit se llevó nueve archivos de la otra sesión, y se rehízo

- **Qué pasó:** el commit se preparó agregando la carpeta `documentacion/epicas` completa. Mientras esta sesión escribía, **otra sesión abierta hoy** —la de [historico-chat/2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md](../../2026-08-17-plan-de-pruebas-y-estado-de-las-51-fases.md), que entonces se llamaba `2026-08-17-sesion-2.md`— estaba escribiendo el `plan_pruebas.md` y el `estado-fase.md` de varias fases de EP-001. Se excluyeron a mano los tres de `A-EP-001-HU-003`, los únicos que se habían visto, y **nueve entraron**.
- **Por qué importa:** es el tercer caso vivo del pendiente [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md): para guardar lo propio se arrastró lo ajeno. Y se vio de inmediato que la carpeta ajena seguía creciendo — cuando se rehizo el commit, esa sesión ya había escrito esos documentos en más de veinte fases.
- **Qué se decidió:** el usuario pidió subir **solo lo propio**. El commit no estaba publicado, así que se deshizo y se rehizo enumerando los archivos de esta sesión: los nueve volvieron a quedar sin guardar, intactos en el disco, para que los suba su sesión. Nada se borró y no se reescribió historia publicada.
- **La lección, para el 22:** con dos sesiones abiertas, agregar una carpeta al commit no es seguro **ni revisando antes** — lo que se agrega cambia entre que se mira y que se guarda. La única forma es enumerar los archivos propios.
- **Estado:** resuelto acá
- **Dónde queda:** el commit de esta sesión, con 163 archivos, y este hallazgo para sumar al pendiente [22](../../../pendientes/22-dos-sesiones-versionando-a-la-vez.md)
- **Nace en:** 2026-08-17
- **Con qué se retoma:** ¿el acuerdo del 22 escribe «se enumeran los archivos, nunca la carpeta» cuando hay otra sesión abierta?

---

## ¿Se puede cerrar la sesión?

Se cierra cuando **ningún hallazgo queda a medias**. Un hallazgo está terminado de una de dos formas, y las dos valen igual:

- **Resuelto acá**, con lo que se hizo escrito en el campo de dónde queda.
- **Anotado**, con su pendiente creado y su historia de usuario disparada escrita. Anotar no es decir "quedó pendiente": es dejar el archivo.

| Para cerrar | Estado |
|---|---|
| Todo hallazgo resuelto tiene su decisión escrita | ☑ · H-1, H-2 y H-5 dicen qué se hizo y dónde quedó |
| Todo hallazgo abierto tiene su pendiente creado | ☑ · el H-10 queda con su decisión pasada al usuario, el H-3 en el [53](../../../pendientes/hecho/ningun-validador-termina-en-silencio.md), el H-4 en el [20](../../../pendientes/hecho/cuando-la-historia-hace-de-especificacion.md) con su fase abierta, el H-6 acá |
| Toda historia disparada está escrita en su épica | ☑ · ninguna historia nueva: las siete ya estaban escritas y lo que faltaba era su fase |
| Lo que se hizo está aprobado y guardado | ☑ · un commit con los 163 archivos propios, después de rehacerlo por el H-11. La **aprobación no es de esta sesión**: el usuario decidió el 2026-08-17 que cada plan se aprueba cuando se vaya a ejecutar su fase. Queda solo guardar |

**Los 51 planes quedan escritos y sin aprobar, y así está bien.** El usuario decidió que la aprobación no es de esta sesión: cada plan se aprueba cuando se vaya a ejecutar su fase, que es cuando `02·F4` pide la pausa — con su plan de pruebas al lado. Escribir los planes y aprobarlos dejaron de ser el mismo momento.

**El tablero quedó con su primera columna llena:** las 51 filas tienen su fase abierta y su plan escrito, y las 68 de la tabla muestran **Fase** y **`plan_trabajo`** en ☑. Ninguna fila está completa todavía: a cada fase le faltan sus otros cuatro documentos, y eso son 51 filas a medias — el costo del cambio de orden que el H-2 deja dicho.

Con las cuatro marcadas, el tema cerró: la sesión se cierra y lo que siga se abre en otra, con el tema que salió de estos hallazgos.

Mientras alguna quede sin marcar, cerrar significa perderla: nadie va a releer la transcripción para encontrarla.

---

_(Si la sesión no dejó nada, se escribe "nada": es un dato, no un olvido.)_

<!-- aviso: falta decir si la sesión se puede cerrar -->
