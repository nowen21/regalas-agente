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
- **What:** al copiar una plantilla, el andamio reescribe el prefijo `../…/` que desde la carpeta de la plantilla llega a la raíz del repositorio, y el marcador `«RUTA-ESTANDAR»`, con la ruta desde la carpeta de la fase. Un `../` que se queda en `plantillas/`, o que pasa de la raíz, no se toca.
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
- **Learned:** el detector fue la cadena misma: la transcripción cortada a las 9:08, las plantillas con sus `«…»` y el `VERSION` sin subir dijeron exactamente dónde quedó todo. Y la decisión sin registro se encontró porque el pendiente la dejó escrita como del usuario — lo que se anota como «es de él» se puede reclamar después.
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
