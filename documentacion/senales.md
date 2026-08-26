# Señales del estándar del agente  ·  `[CAPA 3 · memoria por señales]`

Conocimiento de alto valor que **no se recupera leyendo el código ni las reglas**: decisiones, errores resueltos, patrones y aprendizajes. Se guardan señales, no la conversación (`13·DOC5`). La conversación entera vive en [historico-chat/README.md/](../historico-chat/README.md).

Una señal revertida no se borra: se marca `reemplazada` y se enlaza la nueva. Antes de confiar en una vieja, comprobar que sigue vigente.

## Tipos

`decisión` · `error-resuelto` · `patrón` · `aprendizaje` · `alternativa-descartada` · `supuesto` · `restricción` · `pregunta-abierta` · `gotcha` · `deuda-técnica`

**Estado:** `activa` · `reemplazada` · `revertida`.

---

## Señales

## S-001 · El estándar escribía en inglés lo que exige escribir en español  ·  aprendizaje · activa
- **What:** el estándar usaba "spec" en 53 archivos, y su propia regla `01·C8` manda escribir en el idioma del proyecto.
- **Why:** nadie lo notó porque el término se leía como jerga técnica normal. Salió a la luz cuando el usuario preguntó qué significaba.
- **Where:** [base/01-conducta.md](../base/01-conducta.md) · regla `C20`.
- **Learned:** el estándar no se audita a sí mismo con sus propias reglas. Lo que se exige por escrito hay que comprobarlo también sobre el propio texto.
- **When/Who:** 2026-08-14 · usuario + agente.
- **Scope:** estándar.
- **Rel:** —

## S-002 · Escribir código sin haber recorrido la cadena  ·  error-resuelto · activa
- **What:** se escribieron cinco validadores nuevos desde el pendiente 01, sin épica, sin historia de usuario y sin plan aprobado.
- **Why:** el pendiente describía el trabajo con tanto detalle que pareció suficiente para arrancar. Un pendiente no es una historia de usuario: dice qué falta, no qué se acepta como cumplido.
- **Where:** [documentacion/epicas/EP-004-comprobacion-automatica/README.md/](epicas/EP-004-comprobacion-automatica/README.md).
- **Learned:** el pendiente es el origen, no el permiso. Lo escrito quedó como línea base verificada, no como trabajo hecho.
- **When/Who:** 2026-08-14 · usuario.
- **Scope:** estándar.
- **Rel:** —

## S-003 · `F2` está escrita para construir software, no para escribir reglas  ·  pregunta-abierta · activa
- **What:** dos fases seguidas se abrieron declarando que no tienen especificación aparte, porque su entregable es texto normativo o programas cortos.
- **Why:** `F2` da por hecho que lo que se construye es código de un módulo. Cuando el entregable es el propio texto, una especificación aparte diría lo mismo dos veces.
- **Where:** [base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md](../base/02-flujo-de-trabajo/reglas/F2-sin-especificacion-acordada-no-hay-codigo.md).
- **Learned:** una regla que se incumple dos veces seguidas con buenos motivos necesita decir cuándo no aplica, o se vuelve costumbre incumplirla.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendiente 21.

## S-004 · Lo que un validador encuentra sobre el propio estándar no es ruido  ·  aprendizaje · activa
- **What:** al escribir los validadores nuevos aparecieron 354 enlaces que incumplen `DOC14`, 129 reglas sin bloque de checklist, 7 publicadas en "no cumple" y 33 sin clasificar.
- **Why:** son incumplimientos reales del propio estándar, no falsos positivos del validador. Se descubrieron porque nadie los había comprobado nunca.
- **Where:** [validadores/reglas-validables.md](../validadores/reglas-validables.md).
- **Learned:** escribir el validador es la única forma de saber cuánto se incumplía. Antes de tenerlo, el número era cero por falta de medición, no por cumplimiento.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendientes 18 y 19.

## S-005 · Dos sesiones versionando el mismo archivo a la vez  ·  gotcha · activa
- **What:** mientras esta sesión escribía la versión 10.0.0, otra subió la 9.0.0, la 9.1.0 y dejó escrita la 9.2.0 sin guardar. Al final quedaron dos numeraciones vivas.
- **Why:** `VERSION` y el `CHANGELOG` son un archivo único y ninguna sesión sabe qué está haciendo la otra.
- **Where:** [CHANGELOG.md](../CHANGELOG.md) · [VERSION](../VERSION).
- **Learned:** la regla de que cada sesión sube lo suyo se rompe en los archivos que las dos tocan. Hace falta decidir quién manda sobre la versión.
- **When/Who:** 2026-08-14 · agente.
- **Scope:** estándar.
- **Rel:** pendiente 22.

## S-006 · Mover un archivo que los proyectos llaman por ruta rompe el propio aviso de rotura  ·  error-resuelto · activa
- **What:** la 26.0.0 movió los ocho `hook_*.py` de `validadores/` a `adaptadores/claude-code/` sin dejar nada en la ruta vieja. Los proyectos instalados seguían llamando la ruta vieja: Python salía con código 2, que en el enganche del mensaje **bloquea el mensaje del usuario**, y todos los proyectos quedaron mudos.
- **Why:** el plan de recuperación —«hook_checklist.py lo reclama en el primer mensaje»— corría por el mismo enganche roto. El aviso de desfase viaja por el canal que la mudanza rompe: no puede avisar de su propia caída.
- **Where:** [CHANGELOG.md](../CHANGELOG.md) (26.0.1) · puentes en `validadores/hook_*.py` · [validadores/instalar.py](../validadores/instalar.py).
- **Learned:** lo que otros llaman por ruta absoluta no se muda sin puente en la ruta vieja, y el puente se prueba con el código de salida: para la herramienta, salir con 2 no es fallar — es bloquear al usuario.
- **When/Who:** 2026-08-19 · usuario (reportó el bloqueo) + agente.
- **Scope:** estándar y todos los proyectos instalados.
- **Rel:** S-001 (el estándar no se audita a sí mismo con sus propias reglas).

## S-007 · El enganche de apertura nunca le cargó las reglas al propio estándar  ·  error-resuelto · activa
- **What:** `hook_sesion.py` salía antes de llamar al cargador cuando la carpeta era la del estándar, desde su primera versión (2026-08-05). 30 de 30 aperturas de sesión de este repositorio sin el bloque de reglas; los proyectos herederos sí lo recibían.
- **Why:** la excepción «el propio estándar no se revisa a sí mismo» se escribió para la revisión de instalación y se llevó las reglas por delante. Y nadie lo midió porque las reglas viajan por el canal que no se dibuja: en pantalla se ven los mensajes de estado de los enganches, no lo que llega.
- **Where:** [adaptadores/claude-code/hook_sesion.py](../adaptadores/claude-code/hook_sesion.py) · fase `B-EP-005-HU-009` · caso `arranque-reglas-en-el-estandar` en `evals/`.
- **Learned:** lo que llega por un canal invisible necesita una medición que lo mire, o falta sin que nadie se entere. Y el `CLAUDE.md` §0 de este repositorio lo mandaba por escrito: mandarlo no lo hizo pasar, igual que con el histórico.
- **When/Who:** 2026-08-20 · usuario (preguntó por qué el agente hacía cosas que las reglas no dicen) + agente.
- **Scope:** estándar.
- **Rel:** S-001 · S-006.

## S-008 · El checkpoint se reclama comparando fechas, no leyendo el estado  ·  decisión · activa
- **What:** el enganche del checkpoint decide «falta» o «atrasado» con la fecha de escritura del `estado-fase.md` contra la del documento de puerta recién escrito. No lee ninguno de los dos.
- **Why:** leer el checkpoint y buscar la estación es opinar sobre el texto, y decir en qué estación va la fase es criterio del agente. Dos fechas del sistema de archivos no cuestan nada y no dependen de la redacción.
- **Where:** [validadores/checkpoint.py](../validadores/checkpoint.py) · fase `A-EP-005-HU-013`.
- **Learned:** el aviso se repite mientras el checkpoint siga atrás, a propósito: la marca de «ya avisé» exigiría escribir en un archivo del agente, que es justo lo que este enganche no hace. Solo tres documentos disparan, así que no es ruido.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario en el plan.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-007.

## S-009 · El tramo de consumo es un millón y se decide sin estado  ·  decisión · activa
- **What:** el aviso de consumo a mitad de sesión sale una vez por cada millón de fichas (entrada más salida, sin caché) cruzado, y el cruce se decide comparando el total con el último turno contra el total sin él.
- **Why:** ocho sesiones reales medidas el 2026-08-20 fueron de 144 mil a 12,7 millones: con 200 mil (el tope de la nota de arquitectura) avisaría en todas, y un aviso que sale siempre se deja de leer. Sin estado compartido porque el enganche no tiene archivo propio en el proyecto donde marcar, y crear uno para esto es más estado del que la información vale.
- **Where:** [validadores/presupuesto.py](../validadores/presupuesto.py) · fase `A-EP-005-HU-014`.
- **Learned:** el comando de cierre instalado no se tocó: el modo nuevo entra por un argumento y el viejo es el que corre sin ninguno. Vencer un comando instalado es lo que la 26.0.1 pagó.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario en el plan.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-006.

## S-010 · El andamio traslada solo el enlace que llega exactamente a la raíz  ·  decisión · activa
- **What:** al copiar una plantilla, el andamio reescribe el prefijo `../.../` que desde la carpeta de la plantilla llega a la raíz del repositorio, y el marcador `«RUTA-ESTANDAR»`, con la ruta desde la carpeta de la fase. Un `../` que se queda en `plantillas/`, o que pasa de la raíz, no se toca.
- **Why:** siete fases nacieron hoy con el mismo enlace roto, corregido siete veces con `sed`. Reescribir cualquier `../` habría roto los que no iban a la raíz; las plantillas usan dos formas (`../../` y el marcador) y el andamio atiende las dos para no tocar las plantillas.
- **Where:** [validadores/andamio.py](../validadores/andamio.py) `_reenlazar` · fase `C-EP-004-HU-005`.
- **Learned:** lo que un programa copia de una plantilla hereda la perspectiva de la plantilla, no la del destino. El prefijo se calcula con `relpath`, nunca se escribe fijo.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar.
- **Rel:** S-012.

## S-011 · Un índice que escribe un programa se corrige en el programa, no en el índice  ·  error-resuelto · activa
- **What:** `historico.py` y `resumen.py` escribían el texto del enlace igual al destino (`[2026-08-20/](2026-08-20/)`), y `13·DOC14` pide la ruta desde la raíz. La suite reprobaba cuatro enlaces, dos de ellos nuevos cada sesión.
- **Why:** corregir solo los cuatro habría dejado que la próxima sesión agregara el quinto. La forma del enlace la decide el programa que lo escribe.
- **Where:** [validadores/historico.py](../validadores/historico.py) `_enlace_al_resumen` · [validadores/resumen.py](../validadores/resumen.py) `_indexar_dias` · fase `C-EP-004-HU-008`.
- **Learned:** una suite en rojo por causas viejas esconde la falla nueva; hoy hubo que leer siete fallas para separar tres. El vecino de la misma carpeta sigue por su nombre, que es la excepción que la regla escribe.
- **When/Who:** 2026-08-20 · agente.
- **Scope:** estándar y proyectos instalados (sus índices nuevos nacen bien).
- **Rel:** S-010.

## S-012 · La historia toma el número siguiente al mayor; la fase, el primer hueco  ·  decisión · activa
- **What:** `andamio.py hu` numera la historia con el siguiente al mayor que exista en la épica, como los pendientes; `andamio.py` para la fase sigue tomando la primera letra libre.
- **Why:** la historia se cita por número desde fases, pendientes, commits y el mapa del backlog; un hueco puede ser una historia que se movió, y reutilizarlo haría que «HU-002» apuntara a dos cosas según cuándo se lea. La letra de la fase vive solo dentro de su historia. Un caso lo atrapó: la primera versión tomaba el hueco.
- **Where:** [validadores/andamio.py](../validadores/andamio.py) `siguiente_hu` · fase `B-EP-007-HU-003`.
- **Learned:** los enlaces de la plantilla se trasladan **antes** de poner los propios; al revés, el `../epica.md` recién puesto se trasladaba también. Y la fila del backlog va a «Sin agrupar todavía»: agrupar es criterio y el andamio no lo tiene.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar.
- **Rel:** S-010.

## S-013 · El veredicto se copia solo con concepto escrito, y nunca al checkpoint  ·  decisión · activa
- **What:** `veredicto.py` copia el §6 del resultado a la fila de la historia y a los dos README únicamente cuando el concepto es «cumple» o «no cumple», y no toca el `estado-fase.md`.
- **Why:** un resultado a medio escribir no es un veredicto: propagarlo pondría «no ejecutado» en la historia a cada guardado. El checkpoint es criterio del agente (HU-013). Se reutilizan las expresiones de `fases.py` porque es la que decide la puerta, y dos lecturas del mismo texto se desincronizan.
- **Where:** [validadores/veredicto.py](../validadores/veredicto.py) · [validadores/cerrar.py](../validadores/cerrar.py) `_fila_hecha` · fase `C-EP-005-HU-003`.
- **Learned:** doce copias a mano en un día, y el programa que ya sabía el veredicto solo lo comprobaba después. Se estrenó cerrando sus propias cuatro fases.
- **When/Who:** 2026-08-20 · agente, aprobado por el usuario.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-008.

## S-014 · El agente describió lo que Cimiento no tiene sin buscar en el repositorio  ·  error-resuelto · activa
- **What:** al comparar `notas/estructura.md` con Cimiento, el agente respondió que no había memoria semántica vectorial ni política de carga del contexto. Las dos existen: [memoria/semantica.py](../memoria/semantica.py) (FTS5 ∪ `model2vec`, EP-006 · HU-004, cerrada el 2026-08-06) y [validadores/cargador.py](../validadores/cargador.py) (núcleo `00`+`01` literal y sin sellos, el resto como índice, techo de 90 KB vigilado por `pruebas.py`). Se corrigió al tropezar con el 05 en `pendientes/hecho/`, ya con la orden de abrir un pendiente.
- **Why:** se iba a abrir un pendiente por algo construido hace dos semanas. La comparación se hizo sobre lo que el agente había leído en la sesión, no sobre el repositorio; `20·M12` manda buscar antes de crear, y eso vale también para afirmar que algo falta.
- **Where:** [historico-chat/resumenes/2026-08-20/sesion-5.md](../historico-chat/resumenes/2026-08-20/sesion-5.md) H-3 y H-4.
- **Learned:** antes de decir «Cimiento no tiene X», `grep` sobre el repositorio y una pasada por `pendientes/hecho/`. Medido hoy el arranque: 53,9 KB de reglas literales + 14,1 de índice = 68 KB de los 90 del techo; con memoria e histórico, 84 KB. El núcleo pasó de 52 KB el 19-08 a 54 el 20-08.
- **When/Who:** 2026-08-20 · agente, destapado al ejecutar lo que el usuario autorizó.
- **Scope:** estándar.
- **Rel:** S-001.

## S-015 · `sqlite3.connect` crea el archivo si no existe  ·  gotcha · activa
- **What:** para ver qué tablas tenía `senales.db` se abrió con `sqlite3.connect('documentacion/senales.db')`; el archivo no estaba ahí (vive en `memoria/`) y la llamada dejó uno vacío de 0 bytes. Git no lo vio porque `*.db` está ignorado.
- **Why:** una lectura que escribe pasa por inocente. En una carpeta con seguimiento habría aparecido como archivo nuevo; en una ignorada, nadie lo nota.
- **Where:** `documentacion/senales.db` (residuo, pendiente de borrar a mano) · la base real es [memoria](../memoria/) (975 KB).
- **Learned:** abrir en solo lectura, `sqlite3.connect('file:ruta?mode=ro', uri=True)`, que falla si el archivo no existe en vez de crearlo. Y comprobar la ruta antes: el `ls` del mismo comando ya decía que no estaba.
- **When/Who:** 2026-08-20 · agente.
- **Scope:** estándar.
- **Rel:** S-014.

## S-016 · El portero agrega contexto; no reemplaza el resultado de la herramienta  ·  decisión · activa
- **What:** `hook_externo.py` marca lo que una herramienta trae de afuera devolviendo un sobre como contexto adicional del agente (`additionalContext`), y decide por el nombre de la herramienta y sus argumentos, nunca por el resultado. La alternativa de envolver el resultado (`updatedToolResponse`) se descartó.
- **Why:** agregar contexto está en la documentación oficial y no depende de la forma del resultado, que cambia por herramienta y no está documentada; de reemplazarlo la documentación no dice qué herramientas lo aceptan. Y `Read` cuenta como externo solo fuera de la raíz del proyecto: adentro el archivo es del usuario (`04·S9` dibuja la misma frontera).
- **Where:** [validadores/externo.py](../validadores/externo.py) · [adaptadores/claude-code/hook_externo.py](../adaptadores/claude-code/hook_externo.py) · fase `A-EP-005-HU-015`.
- **Learned:** una guarda se diseña sobre lo que se puede probar, no sobre lo más fuerte. Y el mapa del amarre cuenta `hook_` dentro de los docstrings: un módulo agnóstico no nombra a su enganche ni en el comentario, o pasa a amarrado.
- **When/Who:** 2026-08-20 · agente, plan aprobado por el usuario.
- **Scope:** estándar y proyectos instalados.
- **Rel:** S-014.

## S-017 · La traza es un lector a demanda y no copia resultados  ·  decisión · activa
- **What:** `validar.py traza` saca la línea de tiempo de una sesión leyendo la transcripción cuando alguien lo pide; no es un enganche, no copia el contenido de ningún resultado, se nombra igual que el histórico de su sesión y empareja llamada con respuesta por identificador, no por orden.
- **Why:** un enganche habría tocado nueve proyectos para algo que se necesita cuando algo salió mal, no en cada respuesta; en los resultados viajan claves y datos; y con llamadas en paralelo las respuestas llegan desordenadas — la primera traza real lo confirmó.
- **Where:** [validadores/traza.py](../validadores/traza.py) · fase `A-EP-005-HU-016` · la primera traza: [historico-chat/trazas/2026-08-20-sesion-5.md](../historico-chat/trazas/2026-08-20-sesion-5.md).
- **Learned:** la sesión que construyó la traza quedó trazada por ella: 191 pasos, 9 errores — y los errores son los tropiezos reales del día (borrados bloqueados, comandos demasiado largos). La medida nació con su primer dato.
- **When/Who:** 2026-08-20 · agente, plan aprobado por el usuario.
- **Scope:** estándar; sirve a cualquier proyecto con histórico.
- **Rel:** S-016.

## S-018 · Una sesión cortada deja artefactos sin cadena: se retoman como línea base, no se rehacen ni se dan por buenos  ·  decisión · activa
- **What:** la sesión que recibió «resuelva el pendiente 16» murió a medias: dejó la regla `M19` y el `CA-05` escritos y sellados, pero la fase con sus cinco documentos en plantilla vacía, sin versión, sin prueba y con una decisión reservada al usuario tomada sin registro. La sesión siguiente no rehizo lo escrito ni lo dio por cerrado: lo declaró línea base en el plan de la fase, sometió a aprobación lo que faltaba, preguntó la decisión pendiente y recién entonces ejecutó pruebas, versión y cierre.
- **Why:** las otras dos salidas pierden algo. Rehacer repite trabajo sin cambiar el resultado; dar por bueno deja una regla que no se puede citar como cumplida (sin prueba ni versión) y normaliza que el orden de `02·F4` se invierta en silencio.
- **Where:** [plan de la fase B](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-007-regla-de-las-reglas/B-EP-001-HU-007-primero-que-el-proceso-sirva/plan_trabajo.md), §0 «Cómo llega este plan» y riesgo B-01.
- **Learned:** el detector fue la cadena misma: la transcripción cortada a las 9:08, las plantillas con sus `«...»` y el `VERSION` sin subir dijeron exactamente dónde quedó todo. Y la decisión sin registro se encontró porque el pendiente la dejó escrita como del usuario — lo que se anota como «es de él» se puede reclamar después.
- **When/Who:** 2026-08-21 · agente; opción y planes confirmados por el usuario en el chat.
- **Scope:** estándar; aplica a cualquier proyecto donde una sesión muera a mitad de una fase.
- **Rel:** S-002.

## S-019 · Las pruebas de las vistas escribían el registro real de proyectos  ·  error-resuelto · activa
- **What:** `plantillas/proyectos.md` quedó vacío tres veces en una noche y nadie veía quién lo vaciaba. Eran las pruebas de la interfaz: las vistas llaman `exportar()`, las pruebas llamaban a las vistas con la base de pruebas (vacía tras una baja), y `exportar()` volcaba esa base sobre el archivo real. Un proyecto bien registrado reprobaba «registro» en cada mensaje (pendiente 76, reportado por otra sesión).
- **Why:** una prueba que toca un archivo real del sistema no es una prueba: es un proceso con efectos que corre cuando nadie mira. Y un exportador que escribe cero filas sin preguntarse si antes había algo convierte cualquier base equivocada o vacía en una pérdida de datos.
- **Where:** [interfaz/cimiento/proyectos/core.py](../interfaz/cimiento/proyectos/core.py) (`exportar` con `RegistroVacio`; `registrar`) · [tests.py](../interfaz/cimiento/proyectos/tests.py) (todas con el .md apuntando a una carpeta temporal) · `manage.py registrar` y `validadores/instalar.py` (el alta entra al registro).
- **Learned:** el que lo detectó fue un proyecto instalado, por el checklist que corre en cada mensaje: el estándar se vigiló a sí mismo desde afuera. La regla de oro que queda: toda prueba que escriba, escribe en temporal, y todo exportador se niega a vaciar lo que tenía contenido.
- **When/Who:** 2026-08-22 · agente; el usuario pidió revisar el 76.
- **Scope:** estándar (la interfaz y el instalador).
- **Rel:** S-018.

## S-020 · Un sí dado sobre un diagnóstico viejo se vuelve a verificar contra el estado de hoy  ·  decisión · activa
- **What:** el pendiente 19 pedía cuatro decisiones y el usuario dijo que sí a las cuatro. Al ejecutarlas se encontró que el diagnóstico era del 2026-08-14 y el repositorio ya no era ese: 23 de las 26 particiones estaban hechas desde el 18, dos reglas se habían resuelto sin partirse, y `12·PR3`, que estaba en la lista de derogaciones por «no exigir nada propio», había sido reescrita y hoy exige lo que ninguna otra dice.
- **Why:** ejecutar el sí al pie de la letra habría borrado una exigencia viva (que el dato personal es sensible por defecto) y habría partido reglas ya partidas. La autorización era genuina; lo que había caducado era el diagnóstico sobre el que se dio.
- **Where:** [pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md](../pendientes/hecho/ninguna-regla-reprueba-su-propio-checklist.md), sección «Lo que queda, y es del usuario» · el sello de [`12·PR3`](../base/12-privacidad-datos.md).
- **Learned:** el trabajo de la ronda no fue partir sino **medir de nuevo antes de ejecutar**, y devolverle al usuario las dos que habían cambiado de sentido. Un pendiente con diagnóstico fechado se relee contra el estado actual antes de tocar nada, y lo que cambió se muestra en vez de ejecutarse.
- **When/Who:** 2026-08-22 · agente; las dos decisiones (`17·I3` como una regla, `12·PR3` queda) las tomó el usuario.
- **Scope:** estándar; aplica a cualquier proyecto donde un pendiente viejo se ejecute tal cual.
- **Rel:** S-018.

## S-021 · Un recuerdo que se cumple a medias se sigue incumpliendo, y el hueco es siempre el mismo  ·  error-resuelto · activa
- **What:** el 2026-08-20 quedó escrito el recuerdo «los guiones de apoyo van dentro del repositorio», después de que el usuario preguntara por qué el agente escribía en la carpeta temporal de la herramienta. El 2026-08-22 el agente escribió **31 guiones** en esa misma carpeta durante una jornada entera, y el usuario volvió a preguntar lo mismo.
- **Why:** el recuerdo decía «dentro del repositorio (en una carpeta temporal ignorada por git) **o no se escribe**», y esa puerta —la carpeta temporal— dejaba el cumplimiento a interpretación. El agente leyó «temporal» y usó la de la herramienta. Y el daño no era el sitio: era que **el resultado quedaba versionado y el cómo se perdía**; a la pregunta «¿con qué se recortaron esas treinta reglas?» no había respuesta en ninguna parte.
- **Where:** el recuerdo [guiones-de-apoyo-dentro-del-repo.md](../historico-chat/memory/guiones-de-apoyo-dentro-del-repo.md), reescrito sin la puerta · la carpeta nueva [historico-chat/scripts/](../historico-chat/scripts/README.md), con los 31 de esa jornada.
- **Learned:** un recuerdo con una alternativa («esto o aquello») se cumple por la alternativa más cómoda. Y la prueba de que un recuerdo funciona no es que esté escrito: es que el usuario no tenga que repetirlo. Cuando lo repite, lo que hay que arreglar es **el texto del recuerdo**, no la conducta de esa vez.
- **When/Who:** 2026-08-22 · usuario: «nada se debe escribir por fuera, todo debe quedar en historico-chat».
- **Scope:** estándar; aplica a cualquier proyecto donde el agente escriba guiones de apoyo.
- **Rel:** S-020.

## S-022 · El inventario dice lo que el proyecto debe tener; quién dice si ya está hecho es la prueba  ·  decisión · activa
- **What:** el agente armó el inventario de Cimiento como una foto de lo construido: 22 de 27 filas marcadas «Existe» por afirmación suya, y decidía si una funcionalidad entraba según si ya estaba hecha o ya estaba decidida. El usuario lo corrigió en dos frases: «el inventario es todo lo que el proyecto debe tener sin importar si ya está hecho» y «cuando se hagan las pruebas es que se sabe si ya se hizo».
- **Why:** son dos errores encadenados. El primero **recorta el inventario**: si una fila se omite porque «eso ya existe», el documento deja de ser la lista de lo que el producto debe tener y se vuelve una lista de trabajo pendiente — y como el inventario madura hasta ser el manual del producto, el manual nace con huecos justo en lo que sí está construido. El segundo **falsifica el estado**: «Existe» dicho por el agente es una opinión sobre código que leyó por encima, y una opinión no es evidencia. El estado sale de la prueba ejecutada, no de la lectura.
- **Where:** [prompts/cimiento-inventario-funcionalidades.md](../prompts/cimiento-inventario-funcionalidades.md) (las 22 filas «Existe» quedan sin respaldo hasta que se prueben) · la plantilla [`02-inventario-funcionalidades.md`](../plantillas/ciclo-vida-proyectos/02-inventario-funcionalidades.md), que define los cuatro estados sin decir quién los fija · [`02·F26`](../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md).
- **Also:** el mismo día el usuario quitó del molde toda la historia que arrastraba: la sección «Lo que el usuario ya definió», la fecha del estado, el registro de las preguntas contestadas y la firma del final. Su frase fue «el documento debe quedar como si no hubiera nada desarrollado, pero se debe utilizar la información que ya se tiene para llenarlo». El agente tuvo que oírla tres veces: quitó la sección, después las fechas, después el resto.
- **Learned:** el inventario tiene dos ejes que se estaban mezclando en una sola columna. Uno es **qué debe tener el producto** — completo, y no se poda por nada: ni porque ya esté construido, ni porque ya se haya decidido, ni porque ya aparezca en otra fila. El otro es **qué tan probado está** — y ese lo llena la evidencia de la prueba, con su resultado, no el agente. Mientras no haya prueba, el estado honesto es «sin verificar», que no es lo mismo que «no existe».
- **When/Who:** 2026-08-22 · usuario: «no se debe colocar lo que ya se decidió, el inventario es todo lo que el proyecto debe tener sin importar si ya está hecho» y «cuando se hagan las pruebas es que se sabe si ya se hizo».
- **Scope:** estándar; aplica a todo proyecto que arme su inventario bajo `02·F26`.
- **Rel:** S-020 (medir contra el estado real antes de dar algo por cierto).

## S-023 · Lo que falta no siempre es un pendiente: si el producto debe tenerlo, es una fila del inventario  ·  decisión · activa
- **What:** el agente encontró dos huecos mientras trabajaba el inventario de Cimiento, la lista de partes del proyecto que exige `13·DOC13` y la épica que recoja las funcionalidades de la interfaz, y ofreció anotarlos como pendientes. El usuario paró: «¿pero para qué pendiente si estamos trabajando sobre ese documento?».
- **Why:** un pendiente es para lo que **no** se está haciendo. Abrir uno mientras se tiene el documento abierto convierte un renglón de dos minutos en un trámite de tres pasos, y encima lo saca del sitio donde alguien lo va a buscar. El backlog crece con cosas que ya estaban al alcance de la mano.
- **Where:** el inventario [prompts/cimiento-inventario-funcionalidades.md](../prompts/cimiento-inventario-funcionalidades.md), fila 2.6, escrita en el momento en vez de anotada.
- **Learned:** ante un hueco hay tres destinos y se eligen por lo que el hueco **es**, no por las ganas de dejarlo anotado. Si es algo que el producto debe tener, es una **fila del inventario**, aunque todavía no exista. Si es el paso siguiente de un camino que ya está escrito, no se anota en ninguna parte: se hace cuando toque. Y solo lo que hay que hacer y no cabe en el trabajo de hoy es un **pendiente**. El agente por defecto tiraba todo al tercero, que es el más caro de los tres.
- **When/Who:** 2026-08-22 · usuario, corrigiendo al agente dos veces en la misma sesión (antes ya había dicho «no hay que abrir pendiente, se debe corregir de una»).
- **Scope:** estándar; aplica a cualquier proyecto donde el agente proponga anotar en vez de resolver.
- **Rel:** S-022.

## S-024 · Guardar lo que se hizo y guardar lo que se conversó son dos cosas, y mezclarlas rompe una regla ya aprobada  ·  decisión · activa
- **What:** el usuario pidió que las conversaciones completas entraran a la base «porque eso va a permitir sacar estadísticas y encontrar soluciones: algo que se repita mucho es porque el agente no lo está contemplando». Eso choca de frente con `RN-4` de la especificación de Auditoría, aprobada el mismo día: «se registra la acción, no la conversación», con su razón escrita: la transcripción pesa, se llena de ruido y arrastra credenciales.
- **Why:** el choque era aparente, y el agente estuvo a punto de resolverlo por el camino caro: cambiar la especificación aprobada y la regla. Lo que había era **otra funcionalidad**. La auditoría responde *qué se hizo* y sirve para demostrar; el índice de conversaciones responde *qué se conversó* y sirve para descubrir lo que nadie escribió. Dos preguntas, dos almacenamientos, y ninguna regla que tocar.
- **Also:** la razón que motivaba `RN-4` ya no aplicaba, y comprobarlo tomó un `grep`: [validadores/historico.py:82](../validadores/historico.py#L82) enmascara el mensaje y la respuesta antes de escribir, así que el texto del histórico ya está sin claves. El riesgo que la regla evitaba estaba resuelto desde el pendiente 84.
- **Where:** [pendientes/85](../pendientes/85-las-conversaciones-completas-no-se-pueden-analizar.md) · épica [EP-011](epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md) · `F-033` y `F-034` del inventario · sección 14.1 del [análisis](../cvds/analisis-requisitos/README.md).
- **Learned:** cuando una petición del usuario choca con algo ya aprobado, la primera pregunta no es «¿cambio lo aprobado?» sino «¿es lo mismo que lo aprobado, o es otra cosa?». Casi siempre es otra cosa, y entonces no hay conflicto: hay una funcionalidad que faltaba. Cambiar la línea base es lo último que se intenta, no lo primero.
- **When/Who:** 2026-08-25 · usuario: «la idea es que todo ese historial también se vaya guardando en la DB».
- **Scope:** estándar; aplica a cualquier petición que parezca contradecir un documento aprobado.
- **Rel:** S-023 (elegir el destino por lo que la cosa es).

## S-025 · Una corrección que se repite no es un descuido del usuario: es una regla que falta  ·  aprendizaje · activa
- **What:** en una sola sesión el usuario tuvo que pedir «español colombiano» tres veces antes de que quedara escrito como recuerdo, y citar `00·ID9` cuatro veces sobre respuestas distintas del agente. Las dos terminaron en algo escrito, pero porque insistió.
- **Why:** el daño no es la corrección: es que el patrón se pierde. Se atiende el caso, la sesión cierra, y nadie cuenta cuántas veces hizo falta decirlo. La transcripción tiene el dato desde el primer día y nadie lo ha leído nunca con esa pregunta.
- **Where:** [EP-011](epicas/EP-011-lo-que-se-repite-sale-a-la-luz/epica.md), que existe para hacer visible ese conteo. Su métrica de éxito no es que el reporte exista: es que de él salga al menos una regla nueva.
- **Learned:** la señal de que falta una regla no es que algo salga mal una vez. Es que el usuario tenga que decir lo mismo dos veces. Y eso se puede contar, porque está escrito.
- **When/Who:** 2026-08-25 · agente, contando sobre la propia sesión.
- **Scope:** estándar.
- **Rel:** S-021 (un recuerdo que se cumple a medias se sigue incumpliendo).

## S-026 · El orden de las fases lo fija la versión, no el número de la épica  ·  gotcha · activa
- **What:** cerrada la fase A, el paso obvio parecía la fase B, conectar un proyecto. La correcta era la D, la auditoría: lo dice el orden aprobado en la etapa de implementación, «registrar desde el primer día evita tener un tramo sin historia». El agente alcanzó a marcar la B como abierta antes de releerlo.
- **Why:** las épicas están numeradas por tema y las fases por letra, y ninguna de las dos numeraciones es el orden de ejecución. El orden vive en un tercer documento, y si nadie lo mira, se ejecuta en el orden que parece natural.
- **Also:** la dependencia parecía circular: la historia de auditoría declara que depende de la de proyectos, y la de proyectos exige que su conexión quede auditada. Se rompe por lo que la especificación ya decía: una acción sin proyecto se registra igual, con el campo vacío.
- **Where:** [cvds/implementacion/README.md](../cvds/implementacion/README.md) §5 · el [índice de épicas](epicas/README.md), que ahora lo dice en una línea.
- **Learned:** antes de abrir la fase siguiente se mira el orden de la versión, no la letra que sigue. Y una dependencia que parece circular casi siempre se rompe con un caso vacío que la especificación ya contempló.
- **When/Who:** 2026-08-25 · agente, al abrir la fase después de cerrar la A.
- **Scope:** producto Cimiento, y cualquier proyecto con versiones que reordenen sus fases.
- **Rel:** —

## S-027 · El caso de «que NO pase» fue el único que encontró el defecto, y los otros seis estaban en verde  ·  aprendizaje · activa
- **What:** en la fase D, seis de los siete casos del plan pasaron a la primera. `CP-007`, el que dice «que NO pase: que algo cambie sin quedar registrado», falló: `almacen.guardar` se podía llamar directo y el archivo cambiaba sin dejar registro. Con ese camino abierto, `CA-01` no se cumplía y la fase habría cerrado en «No cumple».
- **Why:** los seis casos que pasaron probaban **que la auditoría funciona**. Ninguno podía ver que existía un camino que la esquivaba, porque todos entraban por la puerta correcta. El caso de «que NO pase» es el único que mira el conjunto en vez de la parte, y por eso es el que encuentra lo que nadie pensó.
- **Also:** corregirlo obligaba a tocar `plataforma/nucleo/almacen/`, que el plan aprobado no declaraba. La fase **se detuvo y se pidieron dos opciones con su costo** en vez de ampliar el plan por iniciativa, que es lo que pide [`02·F8`](../base/02-flujo-de-trabajo/reglas/F8-edita-solo-los-archivos-que-el-plan-aprobado-declara.md). El usuario autorizó cerrar el hueco, y la razón que inclinó la balanza fue medible: hoy no hay un solo llamador de esa función fuera de las pruebas, y con la fase B encima ya serían varios.
- **Where:** [resultado_pruebas.md de la fase D](epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/resultado_pruebas.md), `DEF-01` y los dos ciclos · la ampliación autorizada, sección 2.1 del plan.
- **Learned:** un plan de pruebas sin al menos un caso de «que NO pase» puede salir entero en verde sobre una implementación con un hueco. Y cuando ese caso encuentra algo fuera de lo que el plan declaraba, lo correcto es parar y presentar opciones con su costo, no arreglarlo callado: la ampliación queda escrita y con nombre de quien la autorizó.
- **When/Who:** 2026-08-25 · agente y usuario.
- **Scope:** estándar; aplica a cualquier fase con plan de pruebas.
- **Rel:** S-022 (el estado sale de la prueba, no de la lectura).

## S-028 · Treinta y siete pruebas en verde no dicen nada hasta que se saboteó el código  ·  patrón · activa
- **What:** la fase D terminó con 37 comprobaciones automáticas pasando a la primera. En vez de darlo por bueno, se rompió el código a propósito cuatro veces: ejecutar antes de registrar, escribir sin tapar claves, dejar editar una fila del índice, y quitar la exigencia de constancia. Las cuatro veces fallaron las pruebas correctas, y solo entonces se dio el verde por bueno.
- **Why:** una prueba que pasa puede estar probando otra cosa, o nada. Es el mismo defecto que ya se documentó en el estándar: un caso que decía «correr el enganche» corrió la función que el enganche usa, y tres criterios quedaron en «cumple» sin estar probados.
- **Also:** el sabotaje también sirvió para elegir qué prueba escribir. `CP-003` tenía tres pasos que mostraban que ante la falla nada cambia, pero eso pasaría igual con un código que ejecuta primero y revierte después. Hubo que agregar un paso que **espía el orden real**: `["constancia", "efecto"]`.
- **Where:** [evidencias/EV-02](epicas/EP-009-todo-lo-que-se-hace-queda-registrado/HU-001-registrar-cada-accion/D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), con los cuatro sabotajes y qué prueba cazó cada uno.
- **Learned:** antes de reportar una suite en verde, romper a propósito lo que la suite promete cuidar. Si nada falla, la prueba no estaba probando eso. Cuesta minutos y es la diferencia entre «pasa» y «está probado».
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que reporte pruebas.
- **Rel:** S-027.

## S-029 · Una especificación puede decidir cómo se comporta algo que ningún requisito pidió, y entonces nadie lo construye  ·  error-resuelto · activa
- **What:** al ver la primera pantalla de la plataforma, el usuario preguntó «pero eso no tiene administración?». Buscando la respuesta apareció esto: la especificación del módulo Proyectos decidía en su §7 que **desconectar** pide confirmación, y en su §12 que **desconectar no borra la documentación**, con su alternativa descartada y su porqué. Y no existía ninguna funcionalidad `F-` ni requisito `RF-` que lo pidiera. Su propia §1, la de alcance, no lo nombraba.
- **Why:** una decisión escrita en una especificación **no construye nada**. Lo que baja a fase es el inventario, y si la funcionalidad no está ahí, ninguna fase la va a hacer. El documento queda prometiendo un comportamiento que nadie va a implementar, y el hueco no se ve leyendo la especificación: se ve usando el producto, que es tarde.
- **Also:** el daño concreto era que conectar no tenía reversa. Un proyecto registrado con el nombre o la ruta equivocados quedaba así para siempre, y el arreglo era editar a mano el texto que la plataforma administra. Se comportaba como una acción **que no se deshace** cuando debía ser de las que se deshacen solas.
- **Where:** [pendientes/86](../pendientes/86-conectar-un-proyecto-no-tiene-reversa.md) · `F-035` y `RF-35` · [HU-004](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/HU-004-administrar-un-proyecto-conectado.md) · la §15 de la [especificación de Proyectos](proyectos/spec.md), donde quedó anotado el cambio.
- **Learned:** al cerrar una especificación, contrastar sus secciones de comportamiento y de decisiones contra su propia sección de alcance, y contra el inventario. Todo lo que la especificación **describe cómo se comporta** tiene que tener una fila en el inventario, o no se va a construir. Y al revés: una decisión tomada sobre algo que no está pedido es la señal de que falta pedirlo.
- **When/Who:** 2026-08-25 · usuario, con una sola pregunta sobre la pantalla.
- **Scope:** estándar; aplica a cualquier proyecto que escriba especificaciones de módulo.
- **Rel:** S-023 (si el producto debe tenerlo, es una fila del inventario), S-027.

## S-030 · Un guion de sabotaje que restaura con el control de versiones no restaura lo que todavía no está versionado  ·  gotcha · activa
- **What:** para comprobar que las pruebas de la fase B servían, se saboteó el código cinco veces. Cuatro de los cinco archivos se restauraban con una copia guardada; uno se restauraba con el control de versiones, y ese archivo era nuevo y todavía no estaba versionado. Quedó saboteado, y solo se notó al final, cuando la corrida limpia salió en rojo con cuatro errores.
- **Why:** el sabotaje existe para confiar en las pruebas. Un guion que no restaura bien hace lo contrario: deja el código roto y las pruebas fallando por una razón que no es la que se estaba investigando. Si el paso final no hubiera corrido la suite completa, el sabotaje se habría quedado dentro del commit.
- **Where:** [evidencias/EV-02 de la fase B](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-001-conectar-un-proyecto/B-EP-008-HU-001-se-conecta-un-proyecto/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), que ahora lo dice en su cabecera.
- **Learned:** el sabotaje se restaura con una copia del archivo, nunca con el control de versiones, porque lo que se está probando suele ser código recién escrito. Y el guion **siempre termina corriendo la suite completa**: si esa última corrida no sale limpia, algo quedó saboteado.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028 (romper a propósito lo que la suite promete cuidar).

## S-031 · Un sabotaje que pasa en verde no siempre significa que falte una prueba  ·  gotcha · activa
- **What:** validando las pruebas de la fase H se saboteó el código seis veces. Cinco fallaron las pruebas correctas; el primero pasó en verde. La lectura inmediata fue «falta una prueba que cubra esto». Era falso: ese sabotaje **borraba la ficha del proyecto y la reescribía enseguida**, así que no cambiaba nada observable. No había hueco: el sabotaje no saboteaba.
- **Why:** el sabotaje existe para medir las pruebas, y también hay que mirarlo a él. Dar por bueno el diagnóstico fácil habría llevado a escribir una prueba que no protege de nada, y a creer que la suite es más fuerte de lo que es.
- **Also:** el sabotaje corregido —borrar la documentación del proyecto al desconectar, que es justo lo que `CA-01` promete que no pasa— sí falló, y falló en las dos pruebas que tenían que fallar.
- **Where:** [evidencias/EV-02 de la fase H](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt), que lo dice en el comentario del propio guion.
- **Learned:** cuando un sabotaje pasa en verde, la primera pregunta es **si de verdad cambia el comportamiento**, no si falta una prueba. Un sabotaje válido tiene que romper algo que alguien pueda observar desde afuera: un archivo distinto, una respuesta distinta, un dato distinto. Si el resultado final es idéntico, no era un sabotaje.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028, S-030.

## S-032 · Una confirmación que no dice qué NO va a pasar obliga a adivinar  ·  decisión · activa
- **What:** la fase H tuvo que construir la confirmación de cuatro acciones, entre ellas desconectar un proyecto. La primera forma obvia es preguntar «¿seguro?». Se descartó: lo que el usuario necesita saber antes de desconectar no es que se va a desconectar, sino **si va a perder su documentación**.
- **Why:** una confirmación que solo dice qué va a pasar deja fuera justo lo que da miedo. El usuario que no sabe si va a perder algo, o no confirma, o confirma cruzando los dedos. Ninguna de las dos es una decisión.
- **Also:** por lo mismo se decidió **no preguntar por todo**. Conectar una carpeta nueva no pide confirmación; reconectar una que ya tuvo un proyecto sí, porque ahí sí hay algo que se recibe sin haberlo pedido. Preguntar por todo entrena a confirmar sin leer, y entonces la pregunta deja de proteger.
- **Where:** `CONFIRMACIONES` en [views.py de proyectos](../plataforma/nucleo/proyectos/views.py) y la plantilla `confirmar.html` · `CP-005` del [plan de pruebas](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-004-administrar-un-proyecto-conectado/H-EP-008-HU-004-un-proyecto-conectado-se-administra/plan_pruebas.md).
- **Learned:** toda confirmación de una acción que cambia estado lleva dos listas: **qué va a pasar** y **qué NO va a pasar**. La segunda es la que convierte la pregunta en una decisión. Y se pregunta solo donde hay algo que perder o que recibir sin querer, no en cada botón.
- **When/Who:** 2026-08-25 · agente, construyendo `00·N1` en una pantalla.
- **Scope:** estándar; aplica a cualquier proyecto con acciones que cambian estado.
- **Rel:** —

## S-033 · Cuando un sabotaje pasa en verde hay dos diagnósticos, y hay que distinguirlos  ·  aprendizaje · activa
- **What:** en la fase C uno de los seis sabotajes pasó en verde, igual que había pasado en la fase H. En la H el diagnóstico fue «el sabotaje no saboteaba». Acá se aplicó la misma pregunta y la respuesta fue la contraria: **sí saboteaba**. El sabotaje hacía que corregir la ruta guardara la versión nueva en el índice y dejara la vieja en la ficha, así que al rehacer el índice volvía la vieja.
- **Why:** los dos casos se ven idénticos desde afuera —una suite en verde con el código roto— y llevan a acciones opuestas. Si se diagnostica mal, o se escribe una prueba que no protege de nada, o se deja pasar un defecto real creyendo que el sabotaje era malo.
- **Also:** lo que distinguió los dos casos fue **correr el escenario a mano y mirar el estado final**, no razonar sobre el código. En la fase H el archivo quedaba idéntico; acá quedaba distinto, y se vio en tres líneas de salida.
- **Where:** [evidencias/EV-02 de la fase C](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt) · la prueba reforzada, `test_corregir_la_ruta_relee_la_version_de_reglas`, que ahora borra el índice y comprueba contra el texto.
- **Learned:** ante un sabotaje en verde, **no se decide leyendo el código: se corre el escenario y se mira el estado final**. Si el estado quedó igual, el sabotaje era malo. Si quedó distinto, es una prueba floja. Y la forma más común de prueba floja es mirar **lo que devuelve la función** en vez de lo que quedó guardado: la función puede devolver lo correcto y haber escrito otra cosa.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028, S-030, S-031.

## S-034 · Una fase puede llegar medio construida por fases anteriores, y hay que decirlo antes de planearla  ·  patrón · activa
- **What:** al planear la fase C apareció que dos de sus tres criterios ya estaban casi construidos. `ruta_viva` y el aviso de la lista habían salido de la fase B, porque el modelo de datos pedía la ruta viva como campo calculado. Ninguna de las dos fases estaba pensando en la historia de la ruta perdida.
- **Why:** el riesgo no es haberlo construido antes: es **darlo por probado**. Ese código nunca se había ejecutado contra los criterios de esta historia, así que estaba sin verificar aunque funcionara. Un plan que solo mirara lo nuevo habría cerrado la fase dejando dos criterios sin una sola prueba.
- **Also:** decirlo antes también evitó lo contrario, que es rehacer lo que ya estaba. La sección 2 del plan lo puso en una tabla de tres columnas: qué pide la historia, qué hay hoy, qué falta.
- **Where:** [plan_trabajo.md de la fase C](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-002-avisar-la-ruta-perdida/C-EP-008-HU-002-la-ruta-perdida-se-avisa/plan_trabajo.md) §2 · su plan de pruebas §3.2, que exige probar también lo que ya estaba.
- **Learned:** al abrir una fase, mirar qué de sus criterios ya está construido **por otras fases que no se lo proponían**, y escribirlo en el plan antes de empezar. Lo que aparezca así entra igual al plan de pruebas: construido no es probado, y el estado honesto de ese código es «sin verificar».
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier proyecto que ejecute historias por fases.
- **Rel:** S-022 (el estado sale de la prueba, no de la lectura).

## S-035 · Un sabotaje que escribe fuera del código deja restos que restaurar el archivo no limpia  ·  gotcha · activa
- **What:** en la fase E, uno de los ocho sabotajes hacía que traer escribiera un archivo **dentro de la carpeta del proyecto de origen**, que es justo lo que la fase promete que nunca pasa. La prueba lo cazó y el guion restauró el código. Pero el archivo que ese sabotaje alcanzó a escribir —973 líneas en la raíz del repositorio— **se quedó ahí**, y el guion terminó diciendo que todo estaba bien.
- **Why:** restaurar con copia protege el código, no el mundo. Un sabotaje que solo toca el archivo saboteado se deshace con la copia; uno que escribe, borra o mueve algo afuera deja un rastro que ninguna restauración de código va a limpiar. Y como la suite final salía en verde, el guion no tenía cómo notarlo.
- **Also:** se descubrió por casualidad, en la corrida real: una comprobación que preguntaba «¿hay rastro dentro del repositorio?» salió en verdadero cuando debía salir en falso. Sin esa línea, el archivo se habría ido en el commit.
- **Where:** el guion de sabotaje de la fase E, que ahora declara sus `RASTROS` y los limpia al terminar, nombrando lo que borró · [evidencias/EV-02](epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/evidencias/EV-02-las-pruebas-cazan-el-sabotaje.txt).
- **Learned:** antes de escribir un sabotaje, preguntarse **qué deja fuera del archivo que se está saboteando**. Si escribe, borra o mueve algo, el guion tiene que declararlo y limpiarlo al final, y decir qué limpió. La suite en verde no prueba que el sabotaje se deshizo: prueba que el código volvió a su sitio.
- **When/Who:** 2026-08-25 · agente.
- **Scope:** estándar; aplica a cualquier fase que valide sus pruebas con sabotaje.
- **Rel:** S-028, S-030, S-031, S-033.

## S-036 · Traer un documento «tal cual» transformaba los saltos de línea, y el texto se veía idéntico  ·  error-resuelto · activa
- **What:** el módulo que trae la documentación de un proyecto leía cada archivo con la apertura normal de texto. En Python eso hace traducción automática de saltos de línea: un documento escrito en Windows entraba a la plataforma con saltos de Unix. El texto se ve exactamente igual, y `CA-5` de la especificación dice que **nada se transforma sin que el usuario lo diga**.
- **Why:** es la clase de defecto que ninguna revisión encuentra, porque el documento se lee igual. Lo que cambia es el archivo, y eso aparece después: en un control de versiones que marca las 973 líneas como modificadas, o en una comparación que no cuadra.
- **Also:** lo cazó una prueba que compara **byte por byte**, no como texto. La prueba escrita de la forma cómoda —leer los dos y comparar cadenas— habría pasado en verde, porque al leer los dos con la misma traducción los dos salen iguales.
- **Where:** el `newline=""` de `traer`, en [nucleo/importacion/core.py](../plataforma/nucleo/importacion/core.py), con su porqué escrito al lado para que nadie lo quite por parecer de más.
- **Learned:** cuando algo promete copiar «tal cual», la prueba compara **los bytes**, no el texto. Leer los dos lados con la misma función esconde exactamente las transformaciones que esa función hace: codificación, saltos de línea, espacios del final.
- **When/Who:** 2026-08-25 · agente, en la fase E.
- **Scope:** estándar; aplica a cualquier proyecto que copie o importe archivos.
- **Rel:** S-033 (mirar el estado final, no lo que devuelve la función).

## S-037 · Una fase puede probar todo lo que promete y aun así no cumplir lo que declaró  ·  error-resuelto · activa
- **What:** la fase E declaraba en su plan que recorría «la documentación del ciclo de vida». Pasó sus nueve casos y sus ocho sabotajes, y cerró. Al planear la fase G se descubrió que **no recorría las etapas del ciclo**, que en este proyecto viven en `cvds/`. Peor: esa carpeta tampoco estaba en la lista de las que la fase declara como no miradas, así que **se saltaba en silencio**, contra la regla del propio módulo que dice que nada se pierde sin decirlo.
- **Why:** los nueve casos comprobaban que se trajera lo que se decía traer. **Ninguno preguntaba si lo que se decía traer era todo.** Es un punto ciego que ninguna cantidad de sabotajes cubre, porque el sabotaje rompe el comportamiento y acá el comportamiento estaba bien: lo que faltaba era el alcance.
- **Also:** lo encontró la primera fase que necesitó **usar** lo traído para responder una pregunta concreta. Mientras nadie lo usara, el hueco no se veía.
- **Where:** la sección 5.1 del [cierre de la fase E](epicas/EP-010-lo-escrito-entra-a-la-plataforma/HU-001-traer-un-proyecto/E-EP-010-HU-001-se-trae-un-proyecto-con-lo-que-tenga-escrito/funcionalidad_implementada.md), que lo anota sin reabrir la fase · corregido en la tarea 1 de la [fase G](epicas/EP-008-los-proyectos-se-administran-desde-un-solo-lugar/HU-003-ver-el-estado-de-un-proyecto/G-EP-008-HU-003-se-ve-el-estado-de-un-proyecto/README.md), con su caso `CP-001`.
- **Learned:** cuando una fase declara que recorre, cubre o abarca algo, hace falta **un caso que compruebe el alcance y no solo el comportamiento**: contar lo que se encontró contra lo que debía encontrarse. Y la prueba más dura de una fase que produce datos es la fase siguiente que los consume: hasta que alguien los use, el hueco no aparece.
- **When/Who:** 2026-08-25 · agente, al planear la fase G.
- **Scope:** estándar; aplica a cualquier fase que declare un alcance de recorrido o cobertura.
- **Rel:** S-034 (construido no es probado), S-027.

## S-038 · Lo que no se puede leer se cuenta aparte, nunca se reparte entre las otras dos cuentas  ·  decisión · activa
- **What:** al calcular en qué va un proyecto, la plataforma tiene que decir cuántas fases siguen abiertas. Contando los 125 estados de fase de este repositorio aparecieron **doce formas distintas** de escribir la línea que dice en qué estación va una fase, y **cinco que no se dejan leer**.
- **Why:** las dos salidas fáciles mienten. Contar las ilegibles como cerradas da 41 abiertas; contarlas como abiertas da 46. Ninguna de las dos cifras es verdad, y las dos se ven igual de creíbles en la pantalla.
- **Also:** la forma de resolverlo fue que la función devuelva **dos** valores: si la fase está abierta, y **si se pudo saber**. Un solo valor obliga a inventar una respuesta para el caso que no se pudo leer.
- **Where:** `_esta_abierta` en [nucleo/proyectos/estado.py](../plataforma/nucleo/proyectos/estado.py) · `CP-004` de la fase G, que prueba el caso de una fase ilegible sola: ni abierta ni cerrada.
- **Learned:** cuando algo se cuenta en dos categorías y hay casos que no se pueden clasificar, **la tercera cuenta no es opcional**: es la que hace verdaderas a las otras dos. Y se nombra con su ruta, porque un número de ilegibles sin decir cuáles no se puede corregir.
- **When/Who:** 2026-08-25 · agente, en la fase G.
- **Scope:** estándar; aplica a cualquier proyecto que calcule métricas leyendo texto escrito por personas.
- **Rel:** S-036, S-033.

## S-039 · El caso donde una funcionalidad no hace nada es donde más falta hace que deje constancia  ·  error-resuelto · activa
- **What:** el módulo que trae la documentación de un proyecto se salía temprano cuando no reconocía **ningún** documento: `if not hallazgo.cuantos: return`. Con eso no escribía el reporte de lo que no entró, y **tampoco dejaba registro en la auditoría**. Alguien traía un proyecto, no entraba nada, y no quedaba constancia de que se hubiera intentado ni de por qué.
- **Why:** la salida temprana parece razonable —«no hay nada que hacer, me voy»— y es exactamente al revés: **cuando el resultado es cero es cuando más falta hace explicarlo**. Un usuario que trae un proyecto y no ve nada necesita saber si la plataforma falló, si la carpeta estaba vacía, o si nada seguía un molde conocido. Sin reporte, las tres se ven igual.
- **Also:** lo cazó el caso de «que NO pase», probando con un proyecto donde **nada** se reconoce. Los demás casos usaban proyectos que traían al menos un documento, y con eso el defecto era invisible.
- **Where:** el comentario en `traer`, en [nucleo/importacion/core.py](../plataforma/nucleo/importacion/core.py) · `CP-008` de la fase F.
- **Learned:** una salida temprana por «no hay nada que hacer» hay que mirarla dos veces: si la función deja constancia, registro o reporte, **el caso vacío también tiene que dejarlo**. Y las pruebas necesitan al menos un caso donde el resultado sea cero, porque el camino del cero casi nunca se recorre con datos de prueba normales.
- **When/Who:** 2026-08-25 · agente, en la fase F.
- **Scope:** estándar; aplica a cualquier operación que produzca registro o reporte.
- **Rel:** S-038 (la tercera cuenta no es opcional).

## S-040 · Un registro que dice cuántos sin decir cuáles no demuestra nada  ·  decisión · activa
- **What:** después de traer 994 documentos, el registro de auditoría decía: «994 reconocidos, 1 sin reconocer». Para saber **cuál** era ese uno había que volver a traer el proyecto entero. El registro cumplía su formato y aun así no servía para lo que la auditoría existe: demostrar meses después qué pasó.
- **Why:** un número es un resumen, y un resumen no es una prueba. El propósito escrito de la auditoría es poder rastrear cualquier cambio hasta su origen; con un conteo, el rastro se corta en el propio registro.
- **Also:** la salida fácil era meter la lista completa en el registro, y se descartó por dos razones. Un proyecto que siga el estándar a medias puede dejar cientos de rutas, y el registro quedaría ilegible **justo cuando más falta hace**. Y ya estaba decidido que la auditoría guarda **la acción**, no el contenido.
- **Where:** el reporte como documento propio, con su fecha, en [nucleo/importacion/core.py](../plataforma/nucleo/importacion/core.py) · el registro que lo **enlaza**: «1 sin reconocer. El detalle, en proyectos/.../reportes/2026-08-25-205102-lo-que-no-entro.md».
- **Learned:** cuando un registro resume algo que tiene detalle, el detalle va **en un documento aparte y el registro lo enlaza**. No se copia en los dos sitios: dos copias de lo mismo se separan con el tiempo. Y la prueba de que el enlace sirve tiene dos mitades: que el registro **no** repita la lista, y que desde su ruta **sí** se llegue al detalle.
- **When/Who:** 2026-08-25 · agente y usuario, en la fase F.
- **Scope:** estándar; aplica a cualquier proyecto con registro de auditoría.
- **Rel:** S-024 (guardar la acción y guardar el contenido son cosas distintas).

## S-041 · Un validador que lo recorre todo termina juzgando lo que no es suyo  ·  decisión · activa
- **What:** la plataforma trajo 1005 documentos de un proyecto y los dejó dentro del repositorio. Los validadores del estándar los revisaron como si fueran documentación propia y reportaron **3840 enlaces rotos**. Ninguno lo estaba: son enlaces relativos que resuelven en el proyecto de origen y no en la copia. El validador no encontró un defecto, encontró que estaba mirando el árbol equivocado.
- **Why:** la pregunta que abrió esto era otra —«¿lo traído se versiona?»— y parecía de arquitectura. No lo era: [`DA-02`](../cvds/diseno/decisiones-de-arquitectura.md) ya dice que **se clona la plataforma y está todo**, y [`DA-10`](../cvds/diseno/decisiones-de-arquitectura.md) ya aceptó la duplicación como costo declarado. Lo traído se versiona porque está decidido desde antes. Lo que faltaba decidir era **hasta dónde llega un validador**.
- **Also:** el arreglo fácil era sacar lo traído del control de versiones, y contradice las dos decisiones aprobadas. El segundo arreglo fácil era saltar toda carpeta llamada `datos`, y **esconde documentación de verdad**: cualquier proyecto puede darle ese nombre a una carpeta suya. Se salta por **ruta**, no por nombre.
- **Also (2):** el filtro sobre el recorrido del disco **no alcanzó**. El trinquete de marcas no recorre el disco: lee **lo preparado en git**, y por ahí volvió a entrar lo traído. Se vio por el reloj antes que por el veredicto — el enganche de guardar se quedó minutos, porque compara contra el historial **una llamada a git por archivo**: mil documentos ajenos, mil llamadas. Con el corte puesto, dos segundos. **Un mismo error de categoría entra por tantas puertas como formas haya de listar archivos**, y arreglar una no arregla las otras.
- **Where:** `EXCLUIDAS_POR_RUTA`, `es_ruta_de_datos` y `es_dato_de_la_plataforma` en [validadores/comun.py](../validadores/comun.py), usados por los cuatro caminos que llegaban hasta ahí: `recorrer_md`, [cerrar.py](../validadores/cerrar.py), [expediente.py](../validadores/expediente.py) y el trinquete de [marcas.py](../validadores/marcas.py).
- **Learned:** un validador tiene un **dominio**, y conviene escribirlo antes de que un directorio nuevo se lo amplíe solo. Lo que otro proyecto escribió no se juzga con las reglas de este: ni sus enlaces, porque resuelven en otra parte, ni sus marcas, porque `00·ID8` habla de lo que **el agente entrega**. Y una falla de 3840 no es 3840 problemas: casi siempre es uno.
- **When/Who:** 2026-08-25 · agente y usuario, al decidir si lo traído se versiona.
- **Scope:** estándar; aplica a cualquier proyecto cuyos validadores recorran el repositorio entero.
- **Rel:** S-037 (una fase puede probar todo lo que promete y aun así no cumplir lo que declaró).

## S-042 · Anidar la documentación de un proyecto dentro de otro la empuja fuera del tope de Windows  ·  error-resuelto · activa
- **What:** al guardar lo que la plataforma trajo, `git add` se negó: **`Filename too long`**. Anidar la documentación de un proyecto bajo `plataforma/datos/proyectos/<identificador>/traido/` le suma 54 caracteres a cada ruta, y eso empujó **59 archivos** por encima del tope de 260 de Windows — el más largo llegó a **307**. En su sitio de origen las mismas rutas caben sin problema.
- **Why:** el que se pasa no es el archivo, es **la suma**: una carpeta de historia de usuario con nombre descriptivo, más una de fase que repite el identificador, más el prefijo de la plataforma. Cada tramo por separado es razonable y el total no lo es. Y no aparece al escribir —la plataforma copió los 1005 archivos sin quejarse— sino al **guardar**, que es cuando ya se decidió todo lo demás.
- **Also:** se activó `core.longpaths` en el repositorio, y con eso entró. **No es una solución completa y conviene no creer que lo sea:** es configuración local, así que quien clone en Windows tiene que activarla también o le faltarán esos 59 archivos — justo lo que `DA-02` promete al decir que se clona la plataforma y está todo.
- **Where:** `git config core.longpaths true` en este repositorio · el commit que guardó lo traído lo deja dicho en su cuerpo.
- **Measured:** la primera explicación —«el prefijo de la plataforma es muy largo»— se midió y **resultó falsa**. El prefijo son 55 caracteres y acortarlo al mínimo razonable ahorra 15: la ruta más larga pasaría de 307 a 292, **sigue sin caber**. Lo que de verdad consume el presupuesto es este repositorio en su propio sitio: su ruta más larga mide **252 caracteres sin prefijo ninguno**, a ocho del tope, y **81 archivos** están a menos de 55 del límite antes de que nadie los anide. La carpeta de fase repite el identificador completo de la épica y de la historia que ya vienen en las dos carpetas de encima.
- **Learned:** una ruta que cabe deja de caber al anidarse, y es tentador culpar al prefijo porque es lo último que se agregó. **Medir dice otra cosa**: el que no deja margen es el árbol de origen. Por eso `core.longpaths` no es aquí un parche sino la única salida barata — las otras dos son renombrar la convención de carpetas del estándar entero, o dejar de anidar, que es el diseño. Y de paso: **cuando una explicación de un tope numérico suena obvia, se resta antes de creerla.**
- **When/Who:** 2026-08-25 · agente, al guardar lo traído.
- **Scope:** estándar; aplica a cualquier proyecto que copie árboles de documentación dentro de sí mismo y se trabaje en Windows.
- **Rel:** S-041 (lo traído se versiona, y por eso llega a git).

## S-043 · Una comprobación puede estar bien escrita y no estar conectada, y sus pruebas no lo notan  ·  error-resuelto · activa
- **What:** la fase construyó una comprobación con seis pruebas que la cubrían. Un sabotaje la **descolgó de la corrida** —le quitó la llamada desde `validar`— y **las seis siguieron en verde**. La función existía, funcionaba, y por el comando que la gente corre no salía nada.
- **Why:** las seis pruebas llamaban a la función **directo**, que es lo natural al escribirlas: se prueba lo que se acaba de escribir. Ninguna preguntaba si alguien la llama. Una comprobación que no sale por el comando que la gente corre es una comprobación que no existe, y este es el modo de fallar que las pruebas de la propia función no pueden ver **por construcción**.
- **Also:** el mismo sabotaje trajo el caso contrario y conviene no confundirlos. Otro sabotaje también pasó en verde y ahí **la prueba tenía razón**: reemplazaba una de las tres veces que el pendiente nombra el comando, así que el archivo seguía diciéndolo. Es `S-033` otra vez, y solo se distinguen corriendo el escenario y mirando el estado final.
- **Where:** `test_el_aviso_sale_en_la_corrida_de_fases` en [validadores/pruebas.py](../validadores/pruebas.py), que busca el aviso **a través de `validar`** y no llamando a la función · `DEF-01` de la fase `A-EP-004-HU-019`.
- **Learned:** toda comprobación nueva necesita **una prueba que la busque por el punto de entrada de verdad**, no por su nombre. Las pruebas de la función dicen que hace bien lo suyo; solo esa dice que alguien la llama. Y la forma de descubrir que falta es sabotear la conexión, no el cuerpo.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-019.
- **Scope:** estándar; aplica a cualquier proyecto donde una comprobación se sume a un recorrido que ya existía.
- **Rel:** S-033 (un sabotaje en verde tiene dos diagnósticos opuestos).

## S-044 · Un guion de sabotaje dijo «suite completa en verde» sin haber corrido una sola prueba  ·  error-resuelto · activa
- **What:** el guion terminaba corriendo la suite entera, que es lo que dice si algo quedó saboteado. Usaba `unittest discover` sobre la carpeta, **encontró cero pruebas**, y reportó `OK`. La salida decía `Ran 0 tests in 0.000s` seguida de `OK`, y se lee como éxito.
- **Why:** el veredicto que cierra una fase salía de una corrida vacía. Dos ciclos antes se habría leído como «todo bien» y la fase habría cerrado sobre nada. **Cero pruebas y `OK` no son lo mismo, y el formato de salida los muestra igual.**
- **Also:** el guion existe justamente para no confiar en que las pruebas sirven. Que él mismo mintiera sobre su corrida final es el mismo error un nivel más arriba: quien vigila también necesita que lo vigilen.
- **Where:** el guion lanza `pruebas.py` como programa en vez de `discover`, y **se cae con error si la corrida final no dice `OK` o dice `Ran 0`** · `DEF-02` de la fase `A-EP-004-HU-019`.
- **Learned:** una corrida de pruebas se valida por **dos** cosas, no una: que no haya fallas **y que haya corrido algo**. Cualquier automatismo que decida sobre una suite tiene que mirar el conteo, porque el caso «no corrió nada» sale con el mismo `OK` que el caso bueno.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-019.
- **Scope:** estándar; aplica a cualquier automatismo que lea el resultado de una suite.
- **Rel:** S-043 (una comprobación que nadie llama), S-035 (los rastros que un sabotaje deja fuera).

## S-045 · Un estándar puede arreglar algo para sí mismo y seguir repartiendo el defecto  ·  decisión · activa
- **What:** el estándar le quitó a su inventario de historias la cuenta escrita a mano, después de que se le desfasara tres veces. **La plantilla que reparte a los proyectos seguía enseñando exactamente eso** — los tres campos por llenar, la tabla de una fila por historia, y seis pasos titulados «Cómo se llena la tabla». Y la comprobación que impedía que la copia volviera miraba `pendientes/48-inventario-hu.md`, escrito fijo: en un proyecto el inventario vive en `documentacion/`, así que no veía nada. **La guardia protegía al estándar y a nadie más.**
- **Why:** arreglar algo puertas adentro se siente terminado, porque la molestia desaparece. Pero un estándar tiene dos superficies —lo que hace y lo que reparte— y **la segunda se multiplica**: cada proyecto que instale la plantilla hereda el defecto entero. El costo del descuido no es uno, es uno por proyecto.
- **Also:** las dos mitades no se descubrieron igual. La de la plantilla quedó declarada en el cierre de la fase anterior, porque apareció mientras se escribía. **La de la ruta fija no la vio nadie**: salió de preguntarse, al abrir la historia siguiente, si un proyecto podía siquiera correr el comando. La pregunta era sobre otra cosa.
- **Where:** [plantillas/inventario-hu.md](../plantillas/inventario-hu.md) reescrita, y `CARPETAS_DEL_INVENTARIO` con `_donde_puede_estar_el_inventario` en [validadores/fases.py](../validadores/fases.py) · versión 34.2.0.
- **Learned:** al cerrar algo que el estándar arregló para sí, la pregunta que falta es **«¿y lo que reparto?»** — plantillas, moldes, instaladores. Y la que la acompaña: **«¿la comprobación que lo vigila mira una ruta fija?»** Una guardia atada a la ruta del propio estándar es una guardia que no viaja.
- **When/Who:** 2026-08-26 · agente y usuario, en la fase A de la HU-020.
- **Scope:** estándar; aplica a cualquier proyecto que reparta plantillas o moldes.
- **Rel:** S-043 (una comprobación que nadie llama).

## S-046 · El mismo defecto tiene dos formas, y una sola expresión no caza las dos  ·  error-resuelto · activa
- **What:** la comprobación busca el rótulo de la cuenta **con un número al lado** — `| **Total de HU** | 113 |` — porque en un inventario de verdad el defecto es un número escrito. Un sabotaje devolvió el campo a la **plantilla** y la suite quedó en verde: en una plantilla el mismo defecto viene como `| **Total de HU** | «N» |`, con el hueco por llenar. Sin número, no había coincidencia.
- **Why:** la plantilla es lo que se copia, así que un defecto ahí se multiplica. Y era invisible **justo en el archivo donde más caro sale**. El sabotaje sí saboteaba; la prueba era la que miraba mal.
- **Also:** conviene no arreglarlo haciendo la expresión más laxa. Que el inventario de verdad exija un número **es correcto**: la narrativa del propio inventario tiene cifras, y marcarlas volvería el aviso ruido. Son dos comprobaciones con dos formas, no una comprobación mal escrita.
- **Where:** `test_la_plantilla_no_trae_campos_de_cuenta` en [validadores/pruebas.py](../validadores/pruebas.py), que busca **el rótulo como campo, valga lo que valga** · el sabotaje 5 de la fase `A-EP-004-HU-020`.
- **Learned:** un defecto que puede aparecer en un archivo lleno **y** en la plantilla de la que ese archivo sale tiene **dos formas**: el valor puesto y el hueco por llenar. Reconocer una y creer que se cubrió el caso es lo fácil. Y la plantilla es la que hay que cubrir primero, porque es la que se reparte.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-020.
- **Scope:** estándar; aplica a cualquier comprobación que valga tanto para un documento como para su plantilla.
- **Rel:** S-045 (lo que el estándar reparte se multiplica), S-033 (los dos diagnósticos de un sabotaje en verde).

## S-047 · «No dupliques lo derivable» no aplica a un hecho histórico  ·  error-resuelto · activa
- **What:** al cerrar una fase se escribió, en el campo «Versión del estándar al cerrar», **«la que declara `VERSION`»** en vez del número. Parecía lo correcto —no duplicar un dato que vive en otro archivo—, y venía de haber pasado el día entero quitando copias. Al subir `VERSION` a la 34.2.0, ese cierre pasó a afirmar que había cerrado bajo una versión que **todavía no existía** cuando cerró.
- **Why:** es el error **inverso** al que se acababa de arreglar, cometido por aplicar bien la regla en el sitio equivocado. La cuenta de historias es derivable: se recalcula del árbol y siempre da lo de hoy. **La versión al cerrar es una foto**: su valor es justamente el de aquel momento, y un puntero al valor de hoy lo destruye.
- **Also:** lo cazó el validador que exige el sello de versión en cada cierre, no una lectura. Y lo cazó **una hora después**, cuando el número cambió: mientras `VERSION` no se movió, el puntero decía lo correcto por casualidad.
- **Where:** el campo del cierre de la fase `A-EP-004-HU-019`, con su número literal.
- **Learned:** antes de reemplazar un dato por un puntero, la pregunta es **si el dato es una foto o una cuenta**. Una cuenta se recalcula y el puntero la mejora; una foto se fecha, y el puntero la falsifica el día que la fuente cambie. Y el síntoma es traicionero: **mientras la fuente no cambie, el puntero parece correcto**.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-020, sobre lo escrito en la fase anterior.
- **Scope:** estándar; aplica a todo campo que registre el estado de algo en un momento dado.
- **Rel:** S-040 (un registro que resume enlaza el detalle) — esta señal marca **dónde deja de valer** aquella.

## S-048 · Se citó cuatro veces una historia como «abierta» sin leer su estado, y estaba cerrada  ·  error-resuelto · activa
- **What:** cuatro fases seguidas declararon no llevar especificación aparte, y las cuatro lo justificaron diciendo que la [EP-001 · HU-010](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-010-cuando-no-aplica-la-especificacion/HU-010-cuando-no-aplica-la-especificacion.md) **estaba abierta esperando escribir esa regla**. Sobre esa base se levantó un hallazgo entero, `H-34`, que decía «cuatro ya no es un caso suelto: es la regla que falta». **Era falso.** Esa historia dice `Estado: Done`, cerró el 2026-08-18 con su commit, y su pendiente está en `pendientes/hecho/`.
- **Why:** peor todavía, cerró **diciendo justamente lo contrario**: «nada nuevo, y ese es el resultado». La regla ya existía dos reglas más abajo en el mismo capítulo — [`02·F19`](../base/02-flujo-de-trabajo/reglas/F19-implementa-literal-el-criterio-de-aceptacion.md), *«la redacción del CA es la especificación funcional»*—, y en su momento se intentó agregar otra que decía lo mismo y **chocaba con `02·F0`**. Se citó como pendiente algo que ya se había resuelto, y se propuso rehacer un trabajo que además se había descartado con razón.
- **Also:** el error se cometió una vez y se **copió** tres. Cada fase nueva tomó la redacción de la anterior sin volver a la fuente, y **la repetición hizo la afirmación más creíble**, no menos: para la cuarta, «es la regla que falta» se leía como un hecho establecido por acumulación. Lo que se leyó de la historia fue su **narrativa**, que describe el problema en presente porque se escribió antes de resolverlo. Nadie miró el campo `Estado`, que está en la primera tabla.
- **Where:** los cinco documentos corregidos, cada uno diciendo qué afirmaba y por qué era falso · el hallazgo `H-34` del resumen, reescrito.
- **Learned:** **el estado de un documento se lee en su campo de estado, no en su narrativa.** Una historia sin resolver y una resuelta se leen igual en el cuerpo: las dos describen el problema en presente. Y hay una comprobación barata que habría bastado: si la historia dice que falta una regla, **buscar la regla**. Estaba a un `grep` del capítulo que la historia misma nombraba.
- **When/Who:** 2026-08-26 · agente, al ir a construir lo que creía pendiente.
- **Scope:** estándar; aplica a toda cita de un documento como pendiente o abierto.
- **Rel:** S-026 (marcar como siguiente una fase que no lo era) — el mismo error de leer el cuerpo y no el estado.

## S-049 · El desorden que se le echa a la gente suele estar enseñado por el molde  ·  decisión · activa
- **What:** 111 de 115 historias declaraban su estado con una palabra que su propio molde no decía. La lectura fácil era descuido acumulado. **No lo era:** cuatro moldes del estándar enseñaban tres palabras distintas para «terminado» —`Completada` en la épica, `Done` en la historia, `Hecha` en la tarea— y la lista de la épica estaba escrita **dos veces sin coincidir**, con `Cancelada` en una y no en la otra. Quien escribía una historia justo después de una épica repetía lo que acababa de leer.
- **Why:** si el diagnóstico hubiera sido «descuido», el arreglo habría sido corregir 111 documentos y pedir más cuidado — y en seis meses estarían otra vez repartidos, porque los moldes seguirían enseñando lo mismo. **El diagnóstico decide el arreglo**, y el barato es siempre culpar a quien escribe.
- **Also:** el número se movió de 51 a 111 al mirarlo bien. Con el vocabulario que cada molde traía, 63 «cumplían»; contra un vocabulario único y en español, solo 4. **Lo que parecía menos de la mitad era casi todo**, y la diferencia era qué se tomaba por correcto.
- **Where:** la sección 5 de [base/glosario.md](../base/glosario.md), única definición · los cuatro moldes citándola · `vocabulario_de_estados` en [validadores/fases.py](../validadores/fases.py) · versión 35.0.0.
- **Learned:** ante muchos documentos que incumplen lo mismo, la primera pregunta no es quién se descuidó sino **qué les enseñó a hacerlo**. Un incumplimiento repartido y constante casi nunca es descuido: es un molde. Y la prueba está en contar cuántas fuentes distintas dicen la misma cosa — si son más de una, ahí está.
- **When/Who:** 2026-08-26 · agente y usuario, en la fase A de la HU-012.
- **Scope:** estándar; aplica a cualquier proyecto con documentos modelo.
- **Rel:** S-040 (dos copias de un dato se separan) — acá eran cuatro copias de un vocabulario.

## S-050 · Una comprobación que reporta lo que no vino a comprobar apaga las demás  ·  error-resuelto · activa
- **What:** la comprobación del vocabulario reportaba también las historias **sin campo de estado**. El plan lo pedía. Al correr la suite completa, dejó **siete pruebas de estructura en rojo**: sus árboles de mentira no traen ese campo porque no están probando eso.
- **Why:** el rojo no era de las siete: era de haber ampliado el alcance de la comprobación un paso más allá de su tema. Y en un proyecto habría hecho lo mismo con **cualquier historia mínima** — un aviso permanente sobre documentos que están bien para lo que son. **Un aviso que no se puede atender se aprende a ignorar, y el que aprende a ignorarlo ignora también los buenos.**
- **Also:** que el campo falte **sí es** un problema, y no desaparece por sacarlo de acá: pasa a quien comprueba que un documento traiga sus campos, que es otra cosa. Sacarlo no es taparlo; es ponerlo donde se puede atender.
- **Where:** el comentario junto al `continue` en `estado_fuera_del_vocabulario`, en [validadores/fases.py](../validadores/fases.py), diciendo qué decidió y por qué · `test_limites_sin_campo_de_estado_no_lo_reporta_esta_comprobacion`.
- **Learned:** una comprobación tiene **un tema**, y lo que reporte fuera de él sale caro en ruido. La señal de que se pasó es barata de leer: **si al agregarla se ponen en rojo pruebas que no hablan de su tema, el alcance se fue de más** — no las pruebas.
- **When/Who:** 2026-08-26 · agente, en la fase A de la HU-012.
- **Scope:** estándar; aplica a cualquier comprobación que se sume a un recorrido compartido.
- **Rel:** S-043 (una comprobación que nadie llama), S-046 (el mismo defecto con dos formas).
