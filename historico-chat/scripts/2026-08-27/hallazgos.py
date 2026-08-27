# -*- coding: utf-8 -*-
import io

f = r"c:\Ing. Jose\ia\agente\historico-chat\resumenes\2026-08-22\sesion-6.md"
t = io.open(f, encoding="utf-8").read()

marca = u"## \u00bfSe puede cerrar la sesi\u00f3n?"
assert marca in t

nuevos = u"""### H-35 \u00b7 Preguntar por qu\u00e9 tantas equivocaciones dio dos patrones, y ninguno se caza releyendo

- **Qu\u00e9 pas\u00f3:** el usuario cort\u00f3 con *"por qu\u00e9 tantas equivocaciones?"*. Se miraron las seis del d\u00eda una por una en vez de responder de memoria. **Cuatro fueron leer prosa y tomarla por estado**: un documento resuelto y uno sin resolver se leen igual en el cuerpo, y la diferencia vive en un campo que no se mir\u00f3. **Dos fueron llevar un principio un paso m\u00e1s all\u00e1 de donde vale** \u2014 escribir \u00abla versi\u00f3n que declara `VERSION`\u00bb el mismo d\u00eda que se pasaron horas quitando datos duplicados.
- **Por qu\u00e9 importa:** el factor que multiplic\u00f3 el da\u00f1o no fue ninguno de los dos, sino **encadenar decisiones r\u00e1pido sin reverificar las premisas heredadas**. El error de la `HU-010` se copi\u00f3 cuatro veces porque cada fase tom\u00f3 la redacci\u00f3n de la anterior en vez de volver a la fuente, y **la repetici\u00f3n lo hizo parecer m\u00e1s s\u00f3lido, no menos**.
- **Qu\u00e9 lo soluciona:** dos eslabones, en ese orden. El usuario dijo *"vaya con esas dos"*.
- **Qu\u00e9 se decidi\u00f3:** lo peligroso es **lo reci\u00e9n aprendido**, precisamente porque est\u00e1 fresco y se aplica sin volver a mirar. Y hay una constataci\u00f3n que vale m\u00e1s que cualquier prop\u00f3sito: **ninguna de las seis se caz\u00f3 releyendo** \u2014 todas salieron de ejecutar algo, un `grep`, una resta, una corrida, un sabotaje. **Releer confirma lo que uno ya cree; medir, no.**
- **Estado:** resuelto ac\u00e1.
- **Responde a:** H-34.
- **Dispara:**
  1. Normalizar el vocabulario del estado, que es el eslab\u00f3n que va primero \u2014 sin \u00e9l, el validador nace apoyado en una lista de sin\u00f3nimos que envejece.
  2. [HU-011](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-011-molde-de-las-reglas/), fase `B`: que no se afirme sobre lo que no se ley\u00f3.
- **Orden de resoluci\u00f3n:** primero el vocabulario, despu\u00e9s la regla encima.
- **D\u00f3nde queda:** las se\u00f1ales `S-048` y `S-047`, y las dos fases que salieron de ac\u00e1.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-36 \u00b7 El desorden que se le echa a la gente estaba ense\u00f1ado por el molde

- **Qu\u00e9 pas\u00f3:** al ir a normalizar el vocabulario del estado apareci\u00f3 que **111 de 115 historias estaban fuera de cualquier vocabulario**: conviv\u00edan `Done`, `Hecha`, `Cumplida \u2014 los tres CA`, `Backlog`, `En implementaci\u00f3n`. No era descuido de 111 autores: **cuatro moldes del ciclo de vida ense\u00f1aban tres palabras distintas**, y cada uno copi\u00f3 el suyo.
- **Por qu\u00e9 importa:** cuando un desorden aparece en casi todos los casos, **la causa no est\u00e1 en los casos**. Est\u00e1 en lo que todos copiaron. Corregir uno por uno habr\u00eda dejado el molde intacto, y el desorden habr\u00eda vuelto con la siguiente historia.
- **Qu\u00e9 lo soluciona:** se resolvi\u00f3 ac\u00e1. El usuario pidi\u00f3 **traducir** en vez de agregar excepciones para las palabras en ingl\u00e9s: *"traducir"*.
- **Qu\u00e9 se decidi\u00f3:** nueve estados en espa\u00f1ol, en un solo lugar \u2014 el \u00a75 de [`base/glosario.md`](../../../base/glosario.md). **El programa los lee de ah\u00ed en tiempo de ejecuci\u00f3n**, nunca de una lista en el c\u00f3digo, para que agregar un estado no obligue a tocar un validador. Los cuatro moldes citan el glosario en vez de repetir su propia lista.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** H-35.
- **Dispara:** \u2014
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** el \u00a75 del glosario, `vocabulario_de_estados` en [validadores/fases.py](../../../validadores/fases.py), y la se\u00f1al `S-049`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-37 \u00b7 Una comprobaci\u00f3n que reporta lo que no vino a comprobar apaga las dem\u00e1s

- **Qu\u00e9 pas\u00f3:** al agregar el aviso de que falta el campo `Estado`, siete pruebas de estructura que no ten\u00edan nada que ver quedaron en rojo. La comprobaci\u00f3n estaba bien escrita; lo que estaba mal era **de qu\u00e9 hablaba**.
- **Por qu\u00e9 importa:** un validador que se sale de su tema no informa de m\u00e1s: **informa de menos**, porque quien lo corre aprende a ignorarlo. Y con \u00e9l se ignoran los hallazgos que s\u00ed eran suyos.
- **Qu\u00e9 lo soluciona:** se resolvi\u00f3 ac\u00e1, quitando el reporte fuera de tema y dejando escrito en el c\u00f3digo por qu\u00e9 se quit\u00f3.
- **Qu\u00e9 se decidi\u00f3:** cada comprobaci\u00f3n reporta **su** tema. Lo que aparece de paso se anota como deuda, no se cuela en el resultado de otra.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** H-36.
- **Dispara:** que nadie reporta el campo `Estado` faltante. **Anotado como deuda en el cierre de su fase**, no perdido.
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** la se\u00f1al `S-050`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-38 \u00b7 Un rastro fuera del repositorio no lo muestra ning\u00fan `git status`

- **Qu\u00e9 pas\u00f3:** el guion de sabotaje escrib\u00eda en la configuraci\u00f3n **global** de git y no la limpiaba entre sabotajes, as\u00ed que **contaminaba los tres siguientes**. Peor: la prueba que deb\u00eda cazar eso comparaba el antes y el despu\u00e9s **dentro de s\u00ed misma**, y pasaba en verde si otra prueba ya hab\u00eda ensuciado la configuraci\u00f3n.
- **Por qu\u00e9 importa:** el repositorio no puede mostrar lo que est\u00e1 afuera. Un rastro en la configuraci\u00f3n global, en una variable de entorno o en una carpeta temporal **no lo destapa ninguna comprobaci\u00f3n del proyecto** \u2014 y el sabotaje siguiente arranca desde un estado que nadie declar\u00f3.
- **Qu\u00e9 lo soluciona:** se resolvi\u00f3 ac\u00e1. La configuraci\u00f3n se limpia **despu\u00e9s de cada sabotaje**, no al final, y lo que se pide es `--local`, que s\u00ed vive en el repositorio.
- **Qu\u00e9 se decidi\u00f3:** un guion de sabotaje declara y limpia sus rastros **por sabotaje**, y lo que toque fuera del repositorio se nombra expl\u00edcitamente en el resultado. Una prueba que se comprueba a s\u00ed misma no comprueba nada.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** \u2014
- **Dispara:** \u2014
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** la se\u00f1al `S-051`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-39 \u00b7 Una deuda bien escrita en una fase sin cerrar es una deuda que nadie lee

- **Qu\u00e9 pas\u00f3:** al cerrar seis fases que llevaban cuatro d\u00edas ejecutadas sin su documento de cierre, apareci\u00f3 que **una ya hab\u00eda registrado, cuatro d\u00edas antes, que el enganche no viaja con el repositorio**. Eso mismo se volvi\u00f3 a descubrir por otro camino y se trat\u00f3 como hallazgo nuevo.
- **Por qu\u00e9 importa:** la deuda estaba escrita, fechada y bien redactada. **Lo que fallaba era d\u00f3nde viv\u00eda**: en el resultado de una fase que el inventario contaba entre las incompletas, y a la que nadie volv\u00eda.
- **Qu\u00e9 lo soluciona:** se resolvi\u00f3 ac\u00e1, cerrando las seis.
- **Qu\u00e9 se decidi\u00f3:** **cerrar no es papeleo: es lo que pone la deuda donde se lee.** Y hay una se\u00f1al barata de que est\u00e1 pasando \u2014 cuando un hallazgo \u00abnuevo\u00bb resulta estar escrito en un documento propio con fecha anterior, lo que fall\u00f3 no fue la memoria: fue que ese documento viv\u00eda donde nadie lo cuenta.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** \u2014
- **Dispara:** \u2014
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** los seis cierres y la se\u00f1al `S-052`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-40 \u00b7 Contar archivos presentes da por terminado un molde sin llenar

- **Qu\u00e9 pas\u00f3:** cuatro fases figuraban completas y su `estado-fase` dec\u00eda **\u00abEjecutada y cerrada\u00bb**. Su documento de cierre era **el molde en blanco**, con 31 marcadores sin reemplazar cada uno: todav\u00eda dec\u00eda `\u00ab2-4 l\u00edneas en lenguaje claro\u00bb` y `AAAA-MM-DD`.
- **Por qu\u00e9 importa:** el inventario cuenta que **el archivo exista**, no que diga algo. El andamio crea los cinco documentos vac\u00edos, as\u00ed que **una fase reci\u00e9n abierta cuenta como completa**. Es el mismo defecto del inventario a mano, un nivel m\u00e1s adentro: antes el n\u00famero se copiaba, ahora se calcula bien y cuenta lo que no debe.
- **Qu\u00e9 lo soluciona:** los cuatro cierres se escribieron. **La causa ra\u00edz sigue abierta.**
- **Qu\u00e9 se decidi\u00f3:** cuando algo se cuenta por su presencia, hay que preguntarse **qu\u00e9 pasa si est\u00e1 y est\u00e1 vac\u00edo**. La medida que lo destapa es barata: **contar los marcadores del molde que quedaron sin reemplazar**. Cuatro con 31 se separan sin falsos positivos de doce con cinco a siete, que son comillas de prosa.
- **Estado:** parcialmente resuelto. **Los cuatro documentos, escritos; el andamio sigue igual.**
- **Responde a:** H-39.
- **Dispara:** que el andamio no deje una fase contando como terminada antes de tener una l\u00ednea escrita. **Volvi\u00f3 a cobrar dos veces m\u00e1s el mismo d\u00eda** (H-42, H-43).
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** los cuatro cierres y la se\u00f1al `S-053`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** \u2014
- **Con qu\u00e9 se retoma:** contar los marcadores sin reemplazar, que es la medida que ya funciona.

### H-41 \u00b7 El inventario cuenta fases terminadas, no criterios cumplidos

- **Qu\u00e9 pas\u00f3:** al cerrar cinco fases cuyo veredicto es **\u00abNo cumple\u00bb**, el inventario baj\u00f3 de 37 incompletas a 32. Las cinco tienen sus cinco documentos, as\u00ed que cuentan como completas \u2014 **y una dice que su criterio sigue roto hoy**, con un n\u00famero que adem\u00e1s crece con cada regla nueva.
- **Por qu\u00e9 importa:** \u00abcompletas\u00bb se lee como \u00abcumplen\u00bb, y son cosas distintas. Una fase que midi\u00f3, encontr\u00f3 un rojo y lo document\u00f3 bien **est\u00e1 terminada y no resolvi\u00f3 nada**.
- **Qu\u00e9 lo soluciona:** dispar\u00f3 la [HU-021](../../../documentacion/epicas/EP-004-comprobacion-automatica/HU-021-la-cuenta-distingue-lo-terminado-de-lo-cumplido/), que se construy\u00f3 ac\u00e1.
- **Qu\u00e9 se decidi\u00f3:** un conteo de avance necesita decir **qu\u00e9 mide, en su propio nombre**. Y el patr\u00f3n que lo detecta: **si mejorar el trabajo no mueve el n\u00famero, o moverlo no mejora el trabajo, el n\u00famero mide otra cosa.** Las dos mitades pasaron el mismo d\u00eda \u2014 llenar cuatro cierres vac\u00edos no movi\u00f3 nada, y cerrar cinco fases con \u00abNo cumple\u00bb baj\u00f3 el n\u00famero en cinco.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** H-40.
- **Dispara:** la `HU-021`, construida en sus fases `A` y `B`.
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** los cinco cierres y la se\u00f1al `S-054`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-42 \u00b7 Un n\u00famero de avance necesita una prueba que lo contradiga

- **Qu\u00e9 pas\u00f3:** la cuenta dej\u00f3 de dar por hechas las fases que no cumplieron, y el n\u00famero real apareci\u00f3 al medirlo: de **85 terminadas, 51 cumpl\u00edan**. Once cerraron declarando que no, y 23 no lo dec\u00edan. **El anterior, `85 completas`, estaba sobrestimado en un 40%** \u2014 y con ese n\u00famero se decidi\u00f3 todo el trabajo de dos d\u00edas, incluida la decisi\u00f3n de construir esto.
- **Por qu\u00e9 importa:** un n\u00famero de avance que **solo puede subir** no informa: acompa\u00f1a. Y la mejor prueba de que hac\u00eda falta se dio sola \u2014 la historia que se cre\u00f3 para arreglarlo, sin una l\u00ednea de trabajo hecha, **contaba como terminada**.
- **Qu\u00e9 lo soluciona:** se resolvi\u00f3 ac\u00e1, en la fase `A` de la `HU-021`, versi\u00f3n `35.2.0`.
- **Qu\u00e9 se decidi\u00f3:** todo n\u00famero que mida avance necesita **una forma de empeorar**, y hay que buscarla a prop\u00f3sito. **La pregunta que lo destapa es qu\u00e9 tendr\u00eda que pasar para que baje** \u2014 si no hay respuesta, no sirve para decidir. Y la causa no era descuido: el molde del cierre ofrec\u00eda `Cumple / Cumple con observaciones` y **no ten\u00eda forma de decir \u00abNo cumple\u00bb**, as\u00ed que diecinueve fases lo escribieron en prosa. Se corrigi\u00f3 la regla, no la pr\u00e1ctica: **cerrar no es aprobar**, y dejar la fase abierta esconde su deuda.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** H-41.
- **Dispara:** \u2014
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** `veredicto_de` y `por_veredicto` en [validadores/fases.py](../../../validadores/fases.py), los tres moldes con un solo vocabulario, la versi\u00f3n `35.2.0` y la se\u00f1al `S-055`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

### H-43 \u00b7 Un criterio de parada con n\u00famero exacto caza lo que uno \u00abredondeado\u00bb deja pasar

- **Qu\u00e9 pas\u00f3:** el lector del veredicto reconoc\u00eda **dos de las tres formas** en que est\u00e1 escrito, defecto encontrado diez minutos despu\u00e9s de cerrar la fase `A`. Al arreglarlo, el plan exig\u00eda que las \u00abno dicen\u00bb bajaran **en siete exactamente**; bajaron seis, as\u00ed que se par\u00f3. **La base se hab\u00eda movido**: al levantar esa misma fase con el andamio, sus documentos vac\u00edos volvieron a meter su historia entre las \u00abno dicen\u00bb. La base real era 23, y 23 \u2212 7 = 16.
- **Por qu\u00e9 importa:** con un criterio que dijera \u00abque bajen unas siete\u00bb, la diferencia de uno se habr\u00eda atribuido a un error de cuenta anterior y se habr\u00eda seguido de largo. **El n\u00famero exacto convirti\u00f3 una discrepancia de una unidad en una investigaci\u00f3n**, y esa investigaci\u00f3n destap\u00f3 `S-053` por tercera vez en el d\u00eda, con el agente adentro.
- **Qu\u00e9 lo soluciona:** se resolvi\u00f3 ac\u00e1, en la fase `B` de la `HU-021`.
- **Qu\u00e9 se decidi\u00f3:** un criterio de suspensi\u00f3n sirve cuando **falla por poco**; el que dice \u00abque mejore\u00bb nunca se activa. Y cuando se mide algo mientras se trabaja sobre ello, hay que preguntar **si el propio trabajo mueve la medici\u00f3n** \u2014 abrir una fase para arreglar un conteo es, literalmente, agregarle un caso al conteo. **El caso cr\u00edtico no fue leer la forma que faltaba, sino no leer de m\u00e1s**: \u00abCumple\u00bb aparece en cada fila de criterio, y un lector que no exija el encabezado tomar\u00eda el primer criterio por el veredicto de la fase, mintiendo **en la direcci\u00f3n optimista**.
- **Estado:** resuelto ac\u00e1.
- **Responde a:** H-42.
- **Dispara:** \u2014
- **Orden de resoluci\u00f3n:** \u2014
- **D\u00f3nde queda:** `_VEREDICTO_BAJO_TITULO` en [validadores/fases.py](../../../validadores/fases.py) y la se\u00f1al `S-056`.
- **Nace en:** 2026-08-22 \u00b7 sesion-6
- **Cerrado en:** 2026-08-22 \u00b7 sesion-6
- **Con qu\u00e9 se retoma:** \u2014

---

"""

t = t.replace(marca, nuevos + marca, 1)
io.open(f, "w", encoding="utf-8", newline="\n").write(t)
print("nueve hallazgos agregados")
