# Análisis 2: el gasto lo carga un proceso aparte, y el tablero solo lee la base

> **Aprobado** por el usuario el 2026-10-05, en el turno 37, con la versión 54.4.0. Desde ese momento este análisis no se reescribe.

> Plantilla del análisis. Al llenarla se reemplazan los `«…»` y se borran las notas como esta, menos la tabla de reglas.
>
> Solo entra lo que ayuda a entender qué pasa y a tomar una decisión. Lo que no aporta a decidir no se escribe.
>
> Todo título y todo enlace dicen de qué se trata, nunca solo un número: «Pendiente: lo que se construye se aparta de lo aprobado», no «pendiente 103».
>
> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | Se revisó dónde más pasa: otras herramientas, proyectos que se registran con el proceso corriendo, Cimiento apagado, los demás proyectos Django y las demás tareas repetidas («Dónde más puede pasar») |
| R-2 | Se revisó lo que ya existe antes de decidir: `GuardadoDeConsumo` y `leer_consumo`, `Proyecto.relativa`, las funciones de `core/comun/consola.py`, `andamio.py` para abrir fases, el control de sesiones mezcladas del commit y `apps/ayuda` de scilit |
| R-6 | Se partió de los acuerdos del análisis 1, que el enganche entrega en cada mensaje; los acuerdos 1 y 2 reemplazan su acuerdo 9 |
| R-7 | Lo nuevo que apareció (la ayuda, cerrar fases, `hook_md.py`) se preguntó en el análisis y entró como acuerdo, no directo a la épica |
| R-8 | Cada decisión se planteó sola, con su recomendación (lección 3) |
| R-9 | El hallazgo y el pendiente V3 se pasan a sus originales antes de aprobar, con el análisis prendido |
| R-12 | La ayuda y el cierre de fase quedan para todo proyecto que herede el estándar, no solo para Cimiento |
| R-14 | El análisis lo abre el mismo H-1 del pendiente 119, con «Analicemos: el pendiente 119» (turno 20) |
| R-17 | El enganche de redacción marcó varias respuestas largas; se acortaron en el turno siguiente |
| Las demás | No aplican: no se crean ni cambian reglas del estándar (R-3, R-4), no hay piloto en curso (R-16), y lo que toca la épica se enlaza desde las HU (R-13) |

---

## Hallazgo

### H-1 · Nadie ve cuántos tokens se gastan ni puede ajustar las reglas sin tocar código

| Campo | Valor |
|---|---|
| Qué pasó | El usuario pidió ver cuántos tokens se gastan, dónde y en vivo, en todos los proyectos, para saber qué se puede pasar a un programa. Los datos existen: Claude Code anota cada llamada en los `.jsonl` de la sesión y puede mandarla por telemetría; en una sesión medida hubo 1012 llamadas y unos 450 000 tokens releídos por llamada. Pidió además administrar desde Cimiento qué tan rígida es cada regla en cada proyecto, porque hoy cada ajuste es un cambio de código |
| Por qué importa | Lo que más gasta es el contexto que se relee en cada llamada, sobre todo lo que agregan los enganches; sin medirlo no se sabe qué automatizar primero. Y una regla fija en el código puede bloquear a Cimiento para corregirse, como pasó el 2026-10-04 |

## Pendiente

**De dónde sale.** H-1 del resumen de la sesión del 2026-10-04, versión 2 según el análisis 1.

**El problema.** Cimiento no tiene administración ni muestra el gasto de tokens. Falta correr sobre MariaDB `cimiento`, con pantallas propias y entrada con usuario; registrar los proyectos; fijar por proyecto el nivel de cada regla (frena, avisa o apagada) y que el freno lo lea de la base; guardar el gasto por proyecto, sesión, enganche, archivo leído y los demás niveles; verlo en vivo, y avisar cuando un enganche o un archivo pasa de su límite.

Los datos del gasto ya existen: Claude Code anota cada llamada en los `.jsonl` de `~/.claude/projects/<proyecto>/` y puede mandarla por telemetría. En la sesión `b931dba0`, medida el 2026-10-04, hubo 1012 llamadas y unos 450 000 tokens releídos por llamada.

**Por qué importa.** Sin medir no se sabe qué automatizar primero, y Claude Code borra los `.jsonl` a los 30 días. Sin niveles por proyecto, cada ajuste de una regla es un cambio de código que afecta a todos, y una regla fija puede bloquear a Cimiento para corregirse, como pasó el 2026-10-04.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 20 · Usuario, 2026-10-05 10:17:18
> Analicemos: el pendiente 119

**Agente**, 2026-10-05 10:18:03
<!-- agente: f75203a6-a5c0-4f12-baf5-31909f992fbb -->

Quedó abierto el [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md), con el título «El gasto lo carga un proceso aparte, y el tablero solo lee la base».

**Hay tres decisiones por tomar, de a una:**
1. Cómo corre el proceso que carga la base.
2. Si la telemetría se queda como vía rápida o se quita.
3. El encargo de la otra sesión: elegir en «Proyectos» cómo muestra las rutas `hook_md.py`. Es del mismo tema, la administración de Cimiento, así que entra a este análisis.

**La primera: ¿cómo corre el proceso que carga la base?**
- **Que quede corriendo** (`manage.py vigilar_consumo`). Cada pocos segundos guarda lo nuevo de los `.jsonl`, así que el tablero va unos 5 segundos atrasado. La instalación lo arranca al iniciar sesión en Windows y guarda su número de proceso.
- **Una tarea programada cada minuto** que corre `leer_consumo`. Es más simple, porque no queda nada corriendo, pero el tablero puede ir hasta un minuto atrasado, y cada corrida tarda unos 2 segundos en arrancar Django.

**Recomiendo que quede corriendo**, porque es lo que deja el tablero en vivo.

### 21 · Usuario, 2026-10-05 10:19:48
> Pregunta: y se hace que se guarde cada se realice un consumo o se haga algo?

**Agente**, 2026-10-05 10:20:01
<!-- agente: e15686e1-6dda-4262-89c2-0833d62f597d -->

Sí se puede, y es mejor que revisar cada tantos segundos. Hay tres formas de reaccionar a cada consumo:

- **El proceso se despierta cuando cambia un `.jsonl`.** Windows avisa cuando un archivo cambia, y la librería `watchdog` de Python recibe ese aviso. Cada vez que Claude Code escribe una llamada, el proceso lee lo nuevo y lo guarda en el momento, y el resto del tiempo no hace nada. Cubre todo: llamadas, enganches, herramientas y auxiliares. Suma una dependencia nueva, `watchdog`.
- **Un enganche de Claude Code que guarde al terminar cada turno (`Stop`).** Guarda por turno, no por llamada: un turno con 50 llamadas entra todo al final. Además, suma trabajo a cada respuesta de todos los proyectos.
- **La telemetría, que ya existe.** Claude Code empuja cada llamada en cuanto ocurre, pero no trae los enganches y solo la mandan las sesiones abiertas después de activarla.

**Recomiendo la primera:** un proceso aparte que guarda en cuanto Claude Code escribe, y el tablero solo lee la base. Con eso la telemetría sobra, y esa sería la segunda decisión.

### 22 · Usuario, 2026-10-05 10:23:32
> apruebo la recomendación

**Agente**, 2026-10-05 10:24:24
<!-- agente: 40d01dbc-32a3-4e55-9756-79f15ea02bed -->

Anoto el acuerdo en el análisis 2.

Quedó anotado como acuerdo 1 del análisis 2: un proceso que se despierta cuando cambia un `.jsonl` y guarda en el momento, y el tablero solo lee la base.

**La segunda decisión: ¿la telemetría se queda o se quita?** Con el proceso nuevo, la telemetría ya no aporta:
- El proceso guarda en cuanto Claude Code escribe, así que la telemetría no llega antes de forma que se note.
- Para recibirla, Cimiento tiene que estar levantado todo el tiempo en el 8015. El proceso nuevo no lo necesita.
- Ocupa seis variables en `~/.claude/settings.json` y manda a Cimiento los comandos de cada herramienta, aunque no se guarden.
- No trae enganches, y solo la mandan las sesiones abiertas después de activarla.

**Recomiendo quitarla:** sacar de `settings.json` las seis variables que puso la instalación, que la instalación deje de ponerlas, y retirar la ruta `/v1/logs` con su código. El gasto queda con un solo camino, el `.jsonl`, que trae todo.

### 23 · Usuario, 2026-10-05 10:27:07
> Analicemos: si la telemetría no aporta entonces quitarla

**Agente**, 2026-10-05 10:27:42
<!-- agente: 0d510b72-570a-49d0-b011-10639238cd60 -->

Quedó anotado como acuerdo 2: la telemetría se quita y el gasto llega solo por el `.jsonl`. Eso deja sin efecto la HU-007.

**La tercera decisión, y la última abierta: el encargo de `hook_md.py`.**
- **Qué pasa hoy:** `hook_md.py` es el único enganche que no usa `core/`. Sus avisos muestran las rutas completas (`C:\Ing. Jose\ia\agente\base\...`), y tiene su propia copia de dos funciones que ya existen en `core/comun/consola.py`.
- **Lo que propone la otra sesión:** conectarlo a `core/`, con esas funciones compartidas, y sumar en «Proyectos» un campo «Rutas en los avisos» con dos opciones: relativas al proyecto (`base/02-...`) o completas. El enganche lo leería de la base como lee hoy los límites, sin arrancar Django. Si no hay base, usaría relativas.

**Recomiendo hacerlo así**, con relativas como valor por defecto para todos los proyectos: son más cortas y se leen mejor. Y pregunto si el campo debería servir para todos los enganches que muestran rutas, no solo para `hook_md.py`, para no tener que elegir lo mismo en otro lado después.

### 24 · Usuario, 2026-10-05 10:33:25
> Analicemos: 
> 
> Si esa configuración se necesita en otras partes, entonces debe definirse como una **configuración base de Cimiento**, para que todos los enganches que la necesiten puedan utilizarla.
>
> La idea es evitar que cada enganche tenga que configurar lo mismo por separado. Si es un comportamiento común, debe definirse una sola vez en la configuración base y ser utilizado por todos los proyectos y enganches que correspondan.
> 

**Agente**, 2026-10-05 10:34:00
<!-- agente: 2362ab42-f4ec-4fa2-bdbd-d18ea8ea6bcd -->

De acuerdo: si varios enganches lo necesitan, va una sola vez como configuración de Cimiento y no como campo de cada proyecto. Lo revisé en el código y se puede hacer así:

- **Ya existe un punto común:** `Proyecto.relativa` en `core/comun/proyecto.py` convierte una ruta a relativa. Siete enganches más (`analisis_en_curso`, `autorizado`, `aviso_resuelto`, `cargador`, `checkpoint`, `plan_vs_hecho` y `sesion`) calculan la ruta por su cuenta, y `hook_md.py` usa su propia copia.
- **La configuración base:** una pantalla «Configuración» en Cimiento, que solo cambia el administrador, con una tabla de ajustes generales. El primero sería «Rutas en los avisos: relativas al proyecto o completas». Se lee de MariaDB sin arrancar Django, como los niveles. Sin base, vale «relativas».
- **Un solo lugar que la aplica:** `Proyecto.relativa` lee el ajuste, y los ocho enganches pasan a usar esa función. Así, cambiar el ajuste cambia todos los avisos de todos los proyectos.
- **Sin campo por proyecto por ahora.** Si algún día un proyecto necesita otra cosa, se le suma una excepción, pero no se parte de eso.

¿Lo anoto así como acuerdo 3?

### 25 · Usuario, 2026-10-05 10:40:58
> Analilecemos
> 
> La idea es que **cada proyecto tenga su propia configuración**, de manera que si se realiza un cambio en un proyecto, este no afecte a los demás.
>
> Obviamente, existen configuraciones de **Cimiento que deben aplicarse a todos los proyectos**, porque hacen parte de la base común. Pero también deben existir configuraciones **individuales de cada proyecto**, cuando una necesidad específica no debe afectar a los demás.
>
> De esta manera, se mantiene una base común en Cimiento, pero cada proyecto conserva la independencia necesaria para manejar sus propias configuraciones sin generar efectos no deseados en los demás proyectos.
> 
> No veo identificados los procesos que **no consumen tokens**, ni tampoco los procesos que actualmente consumen tokens pero que **podrían convertirse en automatizaciones** para evitar ese consumo.
>
> Esto es importante porque no solo debemos identificar dónde se están utilizando tokens, sino también determinar qué procesos pueden resolverse sin ellos. De esta manera, se pueden detectar oportunidades de automatización, reducir el consumo innecesario y utilizar tokens únicamente cuando realmente sean necesarios.
> 

**Agente**, 2026-10-05 10:41:09
<!-- agente: c148031f-5e43-4147-9cb4-7420bc7cbb60 -->

«Analilecemos» no está en la lista de `01·C28`, así que no respondo todavía. Para tratar los dos puntos en el análisis, basta reenviar el mensaje empezando con «Analicemos».

### 26 · Usuario, 2026-10-05 10:42:25
> Analicemos:
> La idea es que **cada proyecto tenga su propia configuración**, de manera que si se realiza un cambio en un proyecto, este no afecte a los demás.
>
> Obviamente, existen configuraciones de **Cimiento que deben aplicarse a todos los proyectos**, porque hacen parte de la base común. Pero también deben existir configuraciones **individuales de cada proyecto**, cuando una necesidad específica no debe afectar a los demás.
>
> De esta manera, se mantiene una base común en Cimiento, pero cada proyecto conserva la independencia necesaria para manejar sus propias configuraciones sin generar efectos no deseados en los demás proyectos.
> No veo identificados los procesos que **no consumen tokens**, ni tampoco los procesos que actualmente consumen tokens pero que **podrían convertirse en automatizaciones** para evitar ese consumo.

**Agente**, 2026-10-05 10:42:48
<!-- agente: a17c05ef-e763-4239-8a75-e2b60860ef8b -->

Son dos temas. Los trato de a uno, y el segundo queda anotado como abierto.

**1. Configuración: base de Cimiento y propia de cada proyecto**

Propongo dos niveles:
- **Ajuste base de Cimiento:** vale para todos los proyectos. Se cambia en una pantalla «Configuración».
- **Ajuste del proyecto:** si un proyecto lo cambia, en «Proyectos», ese valor manda solo para él y los demás siguen con el base. Cambiar el base no pisa a los proyectos que tienen el suyo.

Los enganches leen el valor del proyecto y, si no tiene, el base, desde MariaDB y sin Django. Si no hay base de datos, usan el valor de fábrica.

Entrarían ahí «Rutas en los avisos» y también los dos límites de tokens. Los límites hoy son solo por proyecto, con 2000 y 10 000 fijos en el código; pasarían a tener su valor base en «Configuración». Los niveles de las reglas ya funcionan así: «frena» es el base y cada proyecto cambia los suyos.

**2. Procesos que no gastan tokens y los que podrían automatizarse**

Tiene razón: hoy el tablero mide el gasto, pero no separa qué corre sin modelo ni qué podría pasar a un programa. Con los datos que ya se guardan se puede:
- **Lo que no gasta tokens:** los enganches, validadores y tareas corren como programas. Su ejecución no cuesta tokens; solo cuesta lo que le entregan al modelo. Se mostrarían con cuántas veces corrieron y cuántos tokens agregaron. Si no agregaron ninguno, son gasto cero.
- **Lo que podría automatizarse,** con la evidencia de la base:
  - Archivos que se leen muchas veces, como el análisis de 1600 líneas.
  - Enganches que agregan lo mismo en cada mensaje, como «Las reglas de cada turno», con unos 2600 tokens por mensaje.
  - Comandos que el agente repite igual, como los cierres de fase que hice con guiones.
  - Pedidos de la misma palabra clave que siempre siguen los mismos pasos.

  Cada candidato saldría con los tokens que se ahorrarían.

**La pregunta de ahora: ¿anoto el punto 1 como acuerdo 3, con los dos niveles y los límites incluidos?** Después vemos el 2.

### 27 · Usuario, 2026-10-05 10:44:54
> apruebo punto 1

**Agente**, 2026-10-05 10:45:31
<!-- agente: ecf05733-a2a8-4bca-bab7-271850aeba3a -->

Quedó anotado como acuerdo 3. Queda abierto un solo tema: lo que no gasta tokens y lo que podría automatizarse.

**Propuesta: dos secciones nuevas en «Gasto»**

1. **Lo que corre sin tokens.** Hoy el lector guarda un enganche solo cuando le entrega algo al modelo. Pasaría a guardar cada ejecución, también las que no entregan nada. Así cada enganche sale con cuántas veces corrió y cuántos tokens agregó, y los de cero quedan a la vista como trabajo que ya está automatizado.
2. **Candidatos a automatizar**, cada uno con los tokens que se ahorrarían:
   - Archivos que se leen tres veces o más en el período.
   - Enganches que agregan contexto en cada mensaje, con sus tokens por mensaje y el total.
   - Comandos que el agente repite igual. Del comando se guardaría solo el programa y su orden, por ejemplo `python validadores/validar.py fases`, nunca el comando completo, que puede traer datos sensibles.

**Recomiendo empezar con esas dos secciones.** La cuarta pista, pedidos de una misma palabra clave que siempre siguen los mismos pasos, la dejaría para cuando haya más datos: detectar esos patrones es más complejo y hoy daría resultados poco confiables.

¿Lo anoto así como acuerdo 4?

### 28 · Usuario, 2026-10-05 10:47:54
> apruebo

**Agente**, 2026-10-05 10:49:08
<!-- agente: 84479162-bdfa-4954-82ae-085984ddf3d9 -->

Quedó anotado como acuerdo 4, y el análisis 2 ya no tiene decisiones abiertas.

**Lo que sigue:** escribir el resto del análisis a partir de los cuatro acuerdos: hallazgo y pendiente, lo que aporta cada parte, «Lo que se tiene que hacer» y las HU nuevas de EP-025. Serían cuatro:
1. El proceso que carga la base cuando cambia un `.jsonl`, con el tablero leyendo solo la base.
2. Quitar la telemetría.
3. La configuración en dos niveles, con «Rutas en los avisos», los límites y `hook_md.py` conectado a `core/`.
4. Las secciones «Lo que corre sin tokens» y «Candidatos a automatizar».

Cuando esté escrito, lo presento para aprobarlo con «Apruebo el análisis».

### 29 · Usuario, 2026-10-05 11:10:34
> analicemos: recuerde que ya nada de .py se escribe por fuera de cimiento y lo que esté en validadores externos y que se necesiten para cumplir con los acuerdos del análisis primero se deben pasar a core

**Agente**, 2026-10-05 11:11:15
<!-- agente: fe423b33-feae-4fbe-9c37-dd2a752a1e60 -->

Reviso qué `.py` fuera de `core/` tocan los cuatro acuerdos.

Lo anoto como acuerdo 5 del análisis 2. Revisé qué `.py` de fuera de `core/` tocan los cuatro acuerdos:

- **`validadores/instalar.py`:** ya está pasado. Quedan 20 líneas que llaman a `core/herramientas/instalar.py`, donde vive lo que hay que cambiar: quitar la telemetría y sumar el proceso que carga la base.
- **`adaptadores/claude-code/hook_md.py`:** tiene 157 líneas con lógica propia: reconocer un `.md` del proyecto, armar el aviso de marcas y sus copias de `raiz_pedida` y `archivo_editado`. Se pasa primero a `core/enganches/` y el adaptador queda solo leyendo la entrada y llamando a `core/`. Después recibe «Rutas en los avisos».
- **`adaptadores/claude-code/hook_presupuesto.py`:** el aviso por límite, que escribí en la HU-009, quedó como función del adaptador (`aviso_de_limites`). Como los límites pasan a la configuración en dos niveles, primero se pasa a `core/enganches/presupuesto.py`.

Así, cada HU nueva empieza pasando a `core/` lo que va a tocar.

**Una duda:** los guiones de apoyo de `historico-chat/scripts/`, como los `cerrar_hu_*.py` que escribí hoy, son `.py` por fuera de Cimiento. Ahí los manda `04·S18`, y el freno los exige en esa carpeta. ¿Entran en «nada de `.py` por fuera de Cimiento», o siguen ahí como registro de lo que se hizo?

### 30 · Usuario, 2026-10-05 11:13:25
> analicemos: de qué manera automatizamos esto: scripts que no se tenga que estar escribiendo un script cada que se necesite algo ?

**Agente**, 2026-10-05 11:14:05
<!-- agente: 1c985a41-e455-46a6-baa8-b44c6f16feab -->

Antes de responder, anoto en el análisis el acuerdo 5, que dije que anotaría y no lo había hecho.

Quedó anotado el acuerdo 5. Ahora la pregunta.

**Por qué terminé escribiendo guiones hoy:** fueron tareas que se repiten y que Cimiento no trae hechas.
- `cerrar_hu_006.py` a `cerrar_hu_010.py`: cinco guiones casi iguales que llenan el cierre de una fase. Marcan las estaciones del estado, arman el resultado y la funcionalidad, ponen la fila de la fase en la HU y el estado en la épica.
- `clasificar_cambios_de_la_sesion.py`: separa lo que dejó cada sesión antes de un commit, aunque el control del commit ya sabe qué archivo es de qué sesión, porque me lo avisó.

**Propuesta: lo que se repite pasa a ser una orden de Cimiento, y el guion queda solo para lo que se hace una vez.**
1. **Las órdenes que faltan, en `core/herramientas/`:**
   - `cerrar_fase «fase»`: marca las estaciones, arma las tablas del resultado y de la funcionalidad con los casos del plan de pruebas y la corrida de las pruebas, y pone las filas de la HU y de la épica. Quien cierra solo escribe lo que un programa no sabe: qué salió distinto y las decisiones. Hace con el cierre lo que `andamio.py` ya hace al abrir la fase.
   - `cambios_por_sesion`: lista y prepara para el commit lo de una sola sesión, con lo que ya sabe el control del commit.
2. **Que no vuelva a pasar:** al escribir un guion de apoyo, el freno revisa si ya hay uno del mismo tipo en `historico-chat/scripts/`, por nombre y por lo que hace. Si lo hay, avisa que esa tarea ya se repite y que va como orden de Cimiento, no como otro guion. Así el segundo guion no se escribe.
3. **Los guiones que ya existen** se quedan donde están, como registro de lo que se hizo. Esto también responde la duda del acuerdo 5: en `historico-chat/scripts/` solo queda lo que se hace una vez.

¿Lo anoto así como acuerdo 6?

### 31 · Usuario, 2026-10-05 11:21:38
> analicemos: 
> 
> Si ya se tiene definido cómo se cierra una HU, lo correcto es crear una funcionalidad en **Cimiento** que realice ese proceso automáticamente.
>
> De esta manera, en lugar de crear archivos adicionales para ejecutar cada vez el mismo procedimiento, la funcionalidad se encarga de realizar el cierre de la HU siguiendo las reglas establecidas.
>
> Así se evita saturar el proyecto con archivos innecesarios y se centraliza en Cimiento un proceso que ya está definido y que puede ser reutilizado por todos los proyectos que lo implementen.
> 

**Agente**, 2026-10-05 11:21:58
<!-- agente: 99c711dc-f835-4cb4-8a42-33d0a59c1a8e -->

Coincide con lo que propuse, y además aclara un punto: el cierre ya tiene reglas definidas, así que es una funcionalidad de Cimiento para todos los proyectos, no un archivo que se escribe en cada uno.

**Así quedaría el acuerdo 6:**
1. **Cerrar una fase es una funcionalidad de Cimiento:** `manage.py cerrar_fase «fase»`. La instalación la deja disponible para todo proyecto que herede el estándar.
   - Con el plan, el plan de pruebas y la corrida de las pruebas, llena el estado de la fase, el resultado, la funcionalidad, el cierre del plan, la fila de la HU y el estado de la épica, siguiendo las reglas del cierre (`02·F6`, `02·F7`, `13·DOC11`).
   - Quien cierra solo agrega lo que un programa no sabe: qué salió distinto y las decisiones.
2. **Separar los cambios de cada sesión para un commit también pasa a Cimiento:** `manage.py cambios_por_sesion`, con lo que ya sabe el control del commit.
3. **El freno no deja escribir un guion para algo que Cimiento ya hace.** Si el guion se parece a uno anterior, avisa que esa tarea se repite y que se agrega como funcionalidad de Cimiento.
4. **Para lo que de verdad se hace una vez** sigue rigiendo `04·S18`: el guion va en `historico-chat/scripts/`. Los `cerrar_hu_*.py` y `clasificar_cambios_de_la_sesion.py` de hoy se quedan como registro.

¿Lo anoto así como acuerdo 6?

### 32 · Usuario, 2026-10-05 11:26:35
> apruebo

**Agente**, 2026-10-05 11:27:14
<!-- agente: 9cb2b0f0-6427-4169-b44b-a574c18732e0 -->

Quedó anotado como acuerdo 6, y el análisis 2 ya no tiene decisiones abiertas.

**Los seis acuerdos:**
1. Un proceso aparte carga la base cada vez que cambia un `.jsonl`, y el tablero solo lee la base.
2. Se quita la telemetría.
3. La configuración tiene dos niveles: el base de Cimiento y el propio de cada proyecto. Ahí van «Rutas en los avisos» y los límites de tokens.
4. «Gasto» suma dos secciones: «Lo que corre sin tokens» y «Candidatos a automatizar».
5. Ningún `.py` se escribe por fuera de Cimiento. Lo de `hook_md.py` y `hook_presupuesto.py` pasa primero a `core/`.
6. Cerrar una fase y separar los cambios por sesión pasan a ser funcionalidades de Cimiento, y el freno no deja escribir un guion para lo que ya existe.

**Lo que sigue:** escribir el resto del análisis a partir de los seis acuerdos (hallazgo y pendiente, lo que aporta cada parte, «Lo que se tiene que hacer» y las HU nuevas) y presentarlo para aprobarlo con «Apruebo el análisis». Para que lo escriba, el mensaje empieza con «Hágalo» o «Escriba».

### 33 · Usuario, 2026-10-05 11:29:44
> analicemos: copiar la plantilla de tooltips y ayudas, también copiar el modelo de manual de usuario de C:\DesarrollosClaude\personales\scilit.  para cimiento

**Agente**, 2026-10-05 11:31:37
<!-- agente: 75b18d29-e692-44f2-b867-a380bc6e3013 -->

Reviso qué hay en scilit sobre tooltips, ayudas y manual de usuario.

Lo revisé en scilit. Esto es lo que hay y lo que propongo para Cimiento.

**Lo que tiene scilit:** la app `apps/ayuda`, de unas 300 líneas sin contar pruebas, construida en su EP-014.
- **Globos de ayuda:** `{% ayuda_campo %}` en cada campo y `{% ayuda_corta %}` en botones. En desarrollo muestra un «?» rojo si falta el texto, y una prueba exige que toda clave usada tenga texto.
- **Ayuda por pantalla:** `{% ayuda_pantalla %}`, con tres botones: qué es, cómo encaja en el sistema (un mapa animado) y en qué otras pantallas se usa.
- **Panel a la derecha:** el botón «Ayuda» abre la sección de la pantalla actual, y `/ayuda/` muestra el manual completo con índice y botón para imprimir.
- **El manual sigue el molde del estándar,** `plantillas/manual-usuario.md`, que Cimiento ya tiene. Lo que es de scilit son sus 20 secciones y sus textos.

**Propuesta para Cimiento:**
1. **Pasar lo reusable a `core/ayuda/`:** las etiquetas, los globos, la ayuda por pantalla, el panel, el manual imprimible y las pruebas de claves. Las secciones y los textos no se copian; se escriben para las pantallas de Cimiento (entrar, inicio, proyectos, reglas, historial, gasto y configuración) con el molde `manual-usuario.md`.
2. **Que Cimiento quede como origen:** en vez de tener la misma app copiada en scilit y en Cimiento, la versión de Cimiento sirve a todo proyecto Django que herede el estándar (recuerdo «todo multiproyecto», `07·Q4`), y scilit pasa a usarla después, en su propio trabajo.
3. **Toda pantalla nueva de Cimiento suma su sección,** con la misma prueba que en scilit: ninguna pantalla queda sin sección.

¿Lo anoto así como acuerdo 7, con Cimiento como origen de la ayuda?

### 34 · Usuario, 2026-10-05 11:35:37
> apruebo

**Agente**, 2026-10-05 11:36:18
<!-- agente: dfa87c47-df2f-49ce-9a29-246721e9a469 -->

Quedó anotado como acuerdo 7: Cimiento trae su ayuda a partir de la de scilit y queda como origen para todo proyecto Django.

El análisis 2 tiene siete acuerdos y ninguna decisión abierta. Falta escribir el resto del análisis (hallazgo y pendiente, lo que aporta cada parte, «Lo que se tiene que hacer» y las HU nuevas) para aprobarlo. Para que lo escriba, el mensaje empieza con «Hágalo» o «Escriba».

### 35 · Usuario, 2026-10-05 11:37:33
> Hágalo

**Agente**, 2026-10-05 11:43:52
<!-- agente: aa9d519e-6bbd-4208-b522-c6a13b3c3412 -->

Escribo el resto del análisis 2. Primero leo las secciones que faltan llenar.

Registro primero las lecciones como señales, para tener sus números.

Ahora lleno las secciones del análisis.

Sigo con «Lo que aportó cada parte».

Ahora la propuesta final, las lecciones y «Lo que se tiene que hacer».

Hago la fila 1: paso el hallazgo y el pendiente a su versión 3 en los originales.

Ahora corro el validador de análisis sobre el análisis 2.

El validador no le encuentra fallas al análisis 2; las dos que reporta son de análisis viejos del pendiente 103. Reviso las marcas de redacción.

Quedó escrito el [análisis 2 del pendiente 119](../../../../../historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/analisis-2.md). El validador de análisis no le encuentra fallas; las dos que reporta son de análisis viejos del pendiente 103.

**Lo que contiene:**
- **El hallazgo y el pendiente en su versión 3:** «El gasto no llega en vivo de todas las sesiones, y lo que se repite no se automatiza». Ya los pasé a sus originales (`pendiente.md` y el H-1 del resumen de la sesión 2), como manda la fila 1.
- **Ocho HU nuevas en EP-025**, en orden de construcción:
  1. HU-016: cerrar una fase y separar los cambios por sesión son funcionalidades de Cimiento. Va primero para que las fases siguientes ya se cierren con ella.
  2. HU-011: el gasto llega a la base en cuanto Claude Code lo escribe.
  3. HU-012: la telemetría se retira. La HU-007 queda sin efecto.
  4. HU-013: configuración base de Cimiento y la propia de cada proyecto.
  5. HU-014: las rutas de los avisos según la configuración, con `hook_md.py` pasado a `core/`.
  6. HU-015: «Lo que corre sin tokens» y «Candidatos a automatizar».
  7. HU-017: el freno no deja escribir un guion para lo que Cimiento ya hace.
  8. HU-018: la ayuda y el manual de Cimiento.
- **«Lo que se tiene que hacer» con 15 filas,** cada una con su acuerdo y su HU. Incluye corregir la cita equivocada de `04·S10` en el plan de la HU-006.
- **Tres lecciones** registradas como señales S-303 a S-305. Dos son de lo que falló: la telemetría que se construyó y se quita, y los cinco guiones de cierre casi iguales.

Para aprobarlo, el mensaje es «Apruebo el análisis».

### 36 · Usuario, 2026-10-05 11:51:59
> Apruebo el análisis

**Agente**, 2026-10-05 11:52:50
<!-- agente: 67379ee7-a11d-4996-9361-3a4bf1e80136 -->

El programa no aprobó el análisis por dos citas que corrijo:
- El acuerdo 1 citaba el turno 19, que quedó antes de que se prendiera el análisis. Ahora dice turnos 20 a 22.
- La fila 15 citaba la regla `04·S10` y el validador no la encuentra como regla suelta. Ahora sale del acuerdo 1, porque la corrección va dentro de la HU-011.

Corregí las dos citas. La aprobación la marca el programa cuando llega el mensaje, así que hay que mandarlo otra vez: «Apruebo el análisis».

### 37 · Usuario, 2026-10-05 12:03:51
> Apruebo el análisis

**Agente**, 2026-10-05 12:04:08
<!-- agente: 14878f11-d787-405f-9ab0-f2280258ecd4 -->

Quedó aprobado el análisis 2 del pendiente 119, con la marca del programa en el turno 37.

Con eso queda la orden de construir las ocho HU nuevas de EP-025 completas, sin volver a pedir aprobación de planes ni de fases. Arranco por la HU-016, el cierre de fase y la separación por sesión como funcionalidades de Cimiento, para que las fases siguientes ya se cierren con ella. Después siguen, en orden, la HU-011, 012, 013, 014, 015, 017 y 018.

Solo voy a preguntar el commit, lo que no se pueda deshacer y lo que salga del alcance.

> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. Cómo se carga la base: un proceso aparte, que queda corriendo, se despierta cuando Windows avisa que un `.jsonl` cambió (librería `watchdog`) y guarda lo nuevo en ese momento: llamadas, enganches, herramientas y auxiliares. El tablero solo consulta la base y deja de leer los `.jsonl` al abrirse. Reemplaza la parte del acuerdo 9 del análisis 1 que hacía correr la lectura «al abrir el tablero y una vez al día» (turnos 20 a 22).

2. Telemetría: se quita, porque con el proceso del acuerdo 1 no aporta. Se sacan de `~/.claude/settings.json` las seis variables que puso la instalación, la instalación deja de ponerlas y se retira la ruta `/v1/logs` con su código. El gasto llega por un solo camino, el `.jsonl`. Reemplaza lo que queda del acuerdo 9 del análisis 1 y deja sin efecto la HU-007 (turnos 23 y 24).

3. Configuración en dos niveles: cada ajuste tiene un valor base de Cimiento, que vale para todos los proyectos y se cambia en una pantalla «Configuración», y cada proyecto puede tener el suyo, en «Proyectos», que manda solo para él. Cambiar el base no pisa a los proyectos que tienen el suyo. Los enganches leen el del proyecto y, si no tiene, el base, desde MariaDB sin Django; sin base de datos, el de fábrica. Entran «Rutas en los avisos» (relativas al proyecto o completas), que `Proyecto.relativa` aplica para todos los enganches, incluido `hook_md.py` conectado a `core/`, y los dos límites de tokens del acuerdo 10 del análisis 1 (turnos 25 a 28).

4. Lo que no gasta tokens y lo que podría automatizarse: «Gasto» suma dos secciones. «Lo que corre sin tokens»: el lector guarda cada ejecución de un enganche, también la que no le entrega nada al modelo, y cada enganche sale con cuántas veces corrió y cuántos tokens agregó. «Candidatos a automatizar», con los tokens que se ahorrarían: archivos leídos tres veces o más en el período, enganches que agregan contexto en cada mensaje y comandos que el agente repite igual; del comando se guarda solo el programa y su orden, nunca el comando completo. Los pedidos de una misma palabra clave que siguen los mismos pasos quedan para cuando haya más datos (turnos 27 a 29).
5. Código: ningún `.py` se escribe por fuera de Cimiento. Lo que los acuerdos necesitan de afuera se pasa primero a `core/`: la lógica de `adaptadores/claude-code/hook_md.py` (reconocer el `.md`, el aviso de marcas, sus copias de `raiz_pedida` y `archivo_editado`) y el aviso por límite de `hook_presupuesto.py`; los adaptadores quedan leyendo la entrada y llamando a `core/` (turno 30).

6. Lo que se repite es una funcionalidad de Cimiento, no un guion: `manage.py cerrar_fase «fase»` cierra una fase con las reglas del cierre (`02·F6`, `02·F7`, `13·DOC11`): con el plan, el plan de pruebas y la corrida de las pruebas llena el estado de la fase, el resultado, la funcionalidad, el cierre del plan, la fila de la HU y el estado de la épica, y quien cierra solo agrega lo que un programa no sabe (qué salió distinto, las decisiones); la instalación la deja para todo proyecto que herede el estándar. `manage.py cambios_por_sesion` separa lo de cada sesión para un commit. El freno no deja escribir un guion para algo que Cimiento ya hace, y si se parece a uno anterior avisa que la tarea se repite y va como funcionalidad. Lo que se hace una vez sigue en `historico-chat/scripts/` (`04·S18`), y los guiones de hoy quedan como registro (turnos 31 a 33).
7. Ayuda de Cimiento: lo reusable de la ayuda de scilit (`apps/ayuda`, de su EP-014) pasa a `core/ayuda/`: los globos por campo y por botón con el «?» rojo en desarrollo si falta el texto, la ayuda por pantalla con sus tres botones, el panel a la derecha, el manual completo imprimible y la prueba de que toda clave usada tiene texto. Las secciones y los textos se escriben para las pantallas de Cimiento con el molde `plantillas/manual-usuario.md`, y toda pantalla nueva suma su sección. Cimiento queda como origen de la ayuda para todo proyecto Django que herede el estándar; scilit pasa a usarla después, en su propio trabajo (turnos 34 y 35).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

> Cada subsección es obligatoria: el validador detiene el cierre si falta una. Lo que aportan el usuario y Claude queda en la conversación y no se repite aquí.

### Cimiento: las reglas que aplican y las que chocan

Aplican `07·Q4` (no repetir: la ayuda se trae de scilit una vez, las rutas pasan por `Proyecto.relativa` y `hook_md.py` usa las funciones de `core/comun/consola.py`), `03·D6` (el proceso que carga la base puede leer dos veces lo mismo sin duplicar), `04·S10` (el proceso que queda corriendo guarda su número para cerrarlo por él), `10·DEP2` (`watchdog` va con versión fijada en `requirements` y en el `lock`), `02·F8` (el freno), `13·DOC11` (lo que llena `cerrar_fase`) y `20·M10` (la versión).

Chocan dos cosas, y se resuelven así:
- `04·S18` manda los guiones de apoyo a `historico-chat/scripts/`, y el acuerdo 5 pide no escribir `.py` por fuera de Cimiento. Lo resuelve el acuerdo 6: lo que se repite es una funcionalidad de Cimiento, y en `historico-chat/scripts/` solo queda lo que se hace una vez (punto 13).
- El plan de la fase de la HU-006 cita `04·S10` como «la instalación no deja procesos vivos», y esa regla dice otra cosa: no matar procesos por nombre. Se corrige en el punto 15.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Carga del gasto | `GuardadoDeConsumo` y `leer_consumo` (`core/consumo/`) leen solo lo nuevo de cada `.jsonl`; corren una vez al día con una tarea programada y al abrir «Gasto» (`Tablero.get`). Falta el proceso que guarde en cuanto Claude Code escribe |
| Telemetría | Funciona: la ruta `/v1/logs` (`core/consumo/views.py`, `telemetria.py`) y `activar_telemetria` en `core/herramientas/instalar.py`, que dejó seis variables en `~/.claude/settings.json` |
| Configuración | Los límites son campos de cada proyecto, con 2000 y 10 000 fijos en `core/proyectos/limites.py`; los niveles de las reglas ya son por proyecto con «frena» de base. No hay ajustes base ni pantalla «Configuración» |
| Rutas en los avisos | `Proyecto.relativa` existe en `core/comun/proyecto.py`; siete enganches calculan la ruta aparte, y `hook_md.py` (157 líneas, en `adaptadores/claude-code/`) tiene su lógica y sus copias de `raiz_pedida` y `archivo_editado` |
| Aviso por límite | `aviso_de_limites` quedó en `adaptadores/claude-code/hook_presupuesto.py`, fuera de `core/` |
| Gasto por enganche y por comando | `GastoDeEnganche` guarda solo lo que llega al modelo; no hay registro de las ejecuciones. `GastoDeHerramienta` guarda el nombre de la herramienta, no el comando |
| Cierre de fase | `andamio.py` abre la fase; el cierre se hace a mano o con guiones, como `cerrar_hu_006.py` a `cerrar_hu_010.py` del 2026-10-05 |
| Ayuda | Cimiento no tiene. scilit tiene `apps/ayuda` (su EP-014): globos, ayuda por pantalla, panel y manual imprimible, con el molde `plantillas/manual-usuario.md` |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| Análisis 1 del pendiente 119, acuerdo 9 | Lo contradice el uso: con la lectura «al abrir el tablero y una vez al día», lo vivo dependía de la telemetría. Lo reemplazan los acuerdos 1 y 2 |
| EP-025·HU-007 | Muestra un intento que no aportó: la telemetría no trae enganches y solo la mandan las sesiones abiertas después de activarla. Lo recoge el acuerdo 2 (lección 1) |
| H-7 del resumen del 2026-10-04, sesión 3 | Confirma que el gasto por enganche estaba incompleto (faltaban los de texto plano); el acuerdo 4 lo amplía a las ejecuciones que no gastan |
| Los guiones `cerrar_hu_*.py` del 2026-10-05 | Muestran la tarea repetida que no se automatizó; la recoge el acuerdo 6 (lección 2) |
| EP-014 de scilit | Confirma que la ayuda ya está hecha y probada con el molde del estándar; la recoge el acuerdo 7 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Versión MENOR: la ayuda y `cerrar_fase` quedan disponibles y ningún proyecto tiene que hacer nada; quitar la telemetría solo borra las seis variables que puso la instalación. `02·F22` no aplica: no se deroga ninguna regla |
| Normas y leyes | Ninguna nueva. Quitar la telemetría deja de mandar a Cimiento el correo del usuario y los comandos de cada herramienta; del comando solo se guardan el programa y su orden (acuerdo 4) |
| Herramientas | Windows avisa cuando cambia un archivo, y `watchdog` lo recibe; Claude Code escribe el `.jsonl` línea por línea, y la última puede estar a medio escribir (el lector ya la deja para después) |

### Dónde más puede pasar

> Lo que destapó el hallazgo puede pasar en otros sitios, otros proyectos u otras herramientas. Cada caso dice qué lo cubre: un punto de «Lo que se tiene que hacer», un punto de «Lo acordado» o la razón por la que no hace falta cubrirlo. Ningún caso queda sin esa columna.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Se registra un proyecto con el proceso corriendo | Cimiento | Su gasto no entra hasta reiniciar el proceso | Punto 2: el proceso vuelve a leer la lista de proyectos activos |
| MariaDB apagada o el proceso caído | Esta máquina | Lo escrito mientras tanto no entra | Punto 2: al volver, lee desde donde quedó cada archivo; nada se pierde mientras el `.jsonl` exista |
| Otra herramienta de IA | Otra herramienta | Su formato no lo lee nadie | La razón: el lector va aparte del guardado (HU-006, RN-04); otra herramienta agrega su lector |
| Varios enganches muestran rutas | Todos los proyectos | Cada uno las muestra a su modo | Acuerdo 3: todos pasan por `Proyecto.relativa` (punto 7) |
| Otros proyectos Django con ayuda propia | scilit, agro-system | La misma app copiada en cada uno | Acuerdo 7: Cimiento queda como origen; cada proyecto la adopta en su propio trabajo |
| Otras tareas repetidas | Cualquier proyecto | Más guiones casi iguales | Acuerdo 6: el freno avisa al escribir un guion parecido a uno anterior (punto 13) |

---

## Propuesta final: hallazgo y pendiente V«N+1», épica y HU

> Así quedan el hallazgo y el pendiente según lo que concluyó el análisis, con solo los campos que les corresponden. Antes de aprobar, se pasan a los originales con la conversación prendida, para que el cambio quede en el análisis: el hallazgo en el resumen de su sesión y el pendiente en su archivo. Después de aprobar no se cambia nada.

### Hallazgo V3. El gasto no llega en vivo de todas las sesiones, y lo que se repite no se automatiza

| Campo | Valor |
|---|---|
| Qué pasó | EP-025 dejó el gasto en la base y en un tablero, pero lo vivo depende de la telemetría, que no trae enganches y solo la mandan las sesiones abiertas después de activarla; el `.jsonl` se lee al abrir el tablero y una vez al día. Además, cada proyecto no tiene su configuración sobre una base común, el tablero no separa lo que corre sin tokens de lo que podría automatizarse, el cierre de cada fase se hizo con guiones casi iguales, y Cimiento no trae ayuda ni manual |
| Por qué importa | Sin ver el gasto en cuanto ocurre y sin separar lo automatizable, no se sabe qué pasar a un programa; y cada guion repetido es gasto del modelo en algo que un programa haría sin tokens |

### Pendiente V3. El gasto no llega en vivo de todas las sesiones, y lo que se repite no se automatiza

| Campo | Valor |
|---|---|
| De dónde sale | El hallazgo V3, «El gasto no llega en vivo de todas las sesiones, y lo que se repite no se automatiza» |
| El problema | Falta un proceso que guarde el gasto en cuanto Claude Code lo escribe, con el tablero leyendo solo la base y sin telemetría; configuración base de Cimiento con la propia de cada proyecto; ver lo que corre sin tokens y lo que podría automatizarse; cerrar fases y separar los cambios por sesión como funcionalidades de Cimiento; y la ayuda y el manual de Cimiento |
| Por qué importa | Lo que se repite sin automatizar gasta tokens que un programa ahorraría, y sin el gasto en vivo no se ve dónde |

### Épica y HU que salen del análisis

Las HU se suman a la épica [EP-025, Cimiento se administra y muestra el gasto de tokens en vivo](../../../../../documentacion/epicas/EP-025-cimiento-se-administra-y-muestra-el-gasto-de-tokens/epica.md). La HU-007 (telemetría) queda sin efecto con la HU-012.

> El número identifica a la HU; el orden de construcción sale de sus dependencias. Una HU no va antes de otra de la que depende, y cada puesto dice por qué va ahí.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | 016 | Cerrar una fase y separar los cambios por sesión son funcionalidades de Cimiento | El cierre de cada fase se hizo con guiones casi iguales | Ninguna | Las fases de las HU siguientes ya se cierran con ella | 11, 12 |
| 2 | 011 | El gasto llega a la base en cuanto Claude Code lo escribe | Lo vivo depende de la telemetría y el `.jsonl` se lee al abrir el tablero | HU-016 | Es lo que deja el tablero en vivo, y la HU-012 y la HU-015 dependen de ella | 2, 3, 15 |
| 3 | 012 | La telemetría se retira | La telemetría no aporta con el proceso de la HU-011 | HU-011 | Quitarla antes dejaría el gasto sin camino en vivo | 4 |
| 4 | 013 | Cada ajuste tiene su valor base de Cimiento y el propio de cada proyecto | Cada proyecto no tiene su configuración sobre una base común | HU-016 | La HU-014 guarda ahí «Rutas en los avisos» | 5, 6 |
| 5 | 014 | Los avisos muestran las rutas como lo diga la configuración | Cada enganche muestra las rutas a su modo, y `hook_md.py` vive fuera de `core/` | HU-013 | Necesita el ajuste de la HU-013 | 7, 8 |
| 6 | 015 | Se ve lo que corre sin tokens y lo que conviene automatizar | El tablero no separa lo que no gasta de lo automatizable | HU-011 | Usa lo que guarda el proceso de la HU-011 | 9, 10 |
| 7 | 017 | El freno no deja escribir un guion para lo que Cimiento ya hace | Nada impide escribir otro guion repetido | HU-016 | Necesita las funcionalidades de la HU-016 para nombrarlas | 13 |
| 8 | 018 | Cimiento trae su ayuda y su manual | Cimiento no trae ayuda ni manual | HU-013, HU-015 | Las secciones del manual cubren las pantallas que suman la HU-013 y la HU-015 | 14 |

## Lecciones aprendidas

> Salen de lo que funcionó, para repetirlo, y de lo que falló, para no repetirlo. Cada una se escribe como señal de tipo `leccion` en la base de señales (`python memoria/memoria.py add --tipo leccion`) y aquí va el número que le da. «Recomendación» dice si la lección complementa una de las [recomendaciones](«RUTA-ESTANDAR»/plantillas/recomendaciones-del-analisis.md), crea una nueva o no aplica; antes de crear una se busca si ya existe.

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Antes de sumar un segundo camino para el mismo dato, medir qué trae que el primero no: la telemetría se construyó y se quita | Falló | S-303 | complementa R-2 |
| 2 | Al segundo guion casi igual, proponer la funcionalidad en vez de escribirlo: se escribieron cinco para cerrar fases | Falló | S-304 | complementa R-12 |
| 3 | Las decisiones de a una, con recomendación, cierran el análisis sin vueltas | Funcionó | S-305 | complementa R-8 |

## Lo que se tiene que hacer

> Cada fila se convierte en un criterio de aceptación de una HU, y «Pasó a» dice cuál. Ninguna fila queda sin destino. «Sale de» cita de dónde sale, de una de tres formas: un número es un punto de «Lo acordado» de este análisis, «Análisis N, acuerdo M» es un acuerdo de otro análisis del mismo pendiente, y una regla del estándar, como `13·DOC26`, es lo que la regla exige. Lo que no tenga acuerdo no entra. La fila que se hace «de una y sin fase» nombra las rutas exactas que toca, entre comillas invertidas: mientras el análisis está prendido, el freno deja escribir esas y ninguna otra.
>
> La fila 1 va siempre, salvo en el análisis que origina el pendiente: pasar el pendiente a su versión siguiente, con el hallazgo de este análisis en «De dónde sale».

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el hallazgo y el pendiente a su versión 3 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-04/pendientes/119-se-puede-ver-cuantos-tokens-se-gastan-donde-y-en-vivo/pendiente.md`, `historico-chat/resumenes/2026-10-04/sesion-2.md`, hecho el 2026-10-05 |
| 2 | Un proceso de Cimiento (`manage.py vigilar_consumo`) que queda corriendo, se despierta cuando cambia un `.jsonl` (`watchdog`) y guarda lo nuevo con el lector y el guardado que ya existen; vuelve a leer la lista de proyectos activos y, al arrancar, lee desde donde quedó cada archivo; la instalación lo arranca al iniciar sesión, guarda su número de proceso y quita la tarea diaria | 1 | `EP-025` HU-011 |
| 3 | «Gasto» deja de leer los `.jsonl` al abrirse y solo consulta la base | 1 | `EP-025` HU-011 |
| 4 | Retirar la telemetría: la ruta `/v1/logs` y su código, `activar_telemetria` de la instalación, y las seis variables que puso en `~/.claude/settings.json` | 2 | `EP-025` HU-012 |
| 5 | Ajustes con valor base de Cimiento, en una pantalla «Configuración» que cambia el administrador, y valor propio de cada proyecto en «Proyectos»; los enganches leen el del proyecto o, si no tiene, el base, desde MariaDB sin Django; los dos límites de tokens pasan a ser ajustes | 3 | `EP-025` HU-013 |
| 6 | Pasar `aviso_de_limites` de `hook_presupuesto.py` a `core/enganches/presupuesto.py`, leyendo los límites de los ajustes | 5 | `EP-025` HU-013 |
| 7 | El ajuste «Rutas en los avisos» (relativas al proyecto o completas) lo aplica `Proyecto.relativa`, y los enganches que arman rutas pasan a usarla | 3 | `EP-025` HU-014 |
| 8 | Pasar la lógica de `hook_md.py` a `core/enganches/`, con `raiz_pedida` y `archivo_editado` de `core/comun/consola.py`; el adaptador solo lee la entrada y llama a `core/` | 5 | `EP-025` HU-014 |
| 9 | Guardar cada ejecución de un enganche, también la que no le entrega nada al modelo, y mostrar en «Gasto» la sección «Lo que corre sin tokens» | 4 | `EP-025` HU-015 |
| 10 | Guardar de cada comando solo el programa y su orden, y mostrar «Candidatos a automatizar»: archivos leídos tres veces o más, enganches que agregan contexto en cada mensaje y comandos repetidos, con los tokens que se ahorrarían | 4 | `EP-025` HU-015 |
| 11 | `manage.py cerrar_fase «fase»`: llena el estado, el resultado, la funcionalidad, el cierre del plan, la fila de la HU y el estado de la épica con el plan, el plan de pruebas y la corrida de las pruebas; la instalación la deja para todo proyecto | 6 | `EP-025` HU-016 |
| 12 | `manage.py cambios_por_sesion`: lista y prepara para el commit lo de una sola sesión | 6 | `EP-025` HU-016 |
| 13 | El freno no deja escribir un guion para lo que Cimiento ya hace, y avisa cuando un guion se parece a uno anterior | 6 | `EP-025` HU-017 |
| 14 | `core/ayuda/` con lo reusable de `apps/ayuda` de scilit; las secciones de las pantallas de Cimiento con el molde `plantillas/manual-usuario.md`, y la prueba de que ninguna pantalla queda sin sección | 7 | `EP-025` HU-018 |
| 15 | Corregir la cita de `04·S10` en el plan de la fase de la HU-006, que la da como «la instalación no deja procesos vivos» | 1 | `EP-025` HU-011 |

## Lo que aporta al análisis principal

> Todo análisis se anota en el análisis principal de su alcance, aunque no cambie el sistema ([`13·DOC25`](«RUTA-ESTANDAR»/base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md)). Al aprobar, el programa pasa tal cual lo que suma al final de la redacción del principal, y una fila con la fecha, el resultado y el enlace a su «Lista de análisis». Sin esta sección el análisis no se aprueba.

**Resultado:** cambia lo que se construye.

**Lo que suma al análisis principal:** el gasto de tokens llega a Cimiento en cuanto Claude Code lo escribe, sin telemetría; cada proyecto tiene su configuración sobre una base común; lo que se repite en el proceso es una funcionalidad de Cimiento y no un guion; y Cimiento trae la ayuda y el manual que heredan los proyectos Django.
