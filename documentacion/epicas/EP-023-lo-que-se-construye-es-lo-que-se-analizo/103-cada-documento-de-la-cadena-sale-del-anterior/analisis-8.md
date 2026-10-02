# Análisis 8: el freno de las escrituras solo mira algunas herramientas

> **Aprobado** por el usuario el 2026-10-02, en el turno 182. Desde ese momento este análisis no se reescribe.

> Este análisis se redacta aplicando estas reglas.
>
> | Regla | Qué exige |
> |---|---|
> | [`00·ID8`](../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Viene del [análisis 7](analisis-7.md), aprobado el 2026-10-02. Trata solo lo que falló y sus implicaciones sobre lo ya hecho (conclusión 19 del análisis 1).

---

## Hallazgo

### H-8. El freno de las escrituras solo mira algunas herramientas

| Campo | Valor |
|---|---|
| Qué pasó | El 2026-10-02, al cerrar la fase `A` de la HU-002 de EP-023, el agente escribió fuera del proyecto dos veces: redirigió la salida de las pruebas a la carpeta temporal de la herramienta y corrió la suite en segundo plano, que deja su salida en esa misma carpeta. `04·S9` lo prohíbe, y el freno `hook_antes.py` no lo detuvo porque solo se engancha a `Write`, `Edit`, `MultiEdit` y `NotebookEdit`. El CA-02 de la [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md), que es el freno que viene, dice «escribir un archivo» sin nombrar los demás canales. |
| Por qué importa | Una regla rige en todas partes, no solo donde un programa la mira. Cimiento lo heredan proyectos con otras herramientas y otros agentes, y cada uno escribe por canales distintos: consola, programas, segundo plano, subagentes y servicios externos. Si el freno cubre solo algunos, la regla se rompe por los demás. |

## Pendiente

### Pendiente. Lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 3, del [análisis 2](analisis-2.md).

| Campo | Valor |
|---|---|
| De dónde sale | [H-13 de la sesión del 2026-09-28](../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13, y [H-2 de la sesión del 2026-09-30](../../../../historico-chat/resumenes/2026-09-30/sesion.md) |
| El problema | No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior. Nada detiene al agente cuando trabaja fuera del plan aprobado. La plantilla del plan no permite comprobarlo con un programa. Y lo que pasa la conversación al análisis hay que configurarlo a mano para cada análisis. |
| Por qué importa | Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más. |

---

## Conversación

> La pasa el enganche desde la [transcripción del día](../../../../historico-chat/2026-10-01-sesion.md), a partir del turno 141, donde empezó la discusión; el análisis se prendió en el turno 146.

### 141 · Usuario, 2026-10-02 08:45:04
> 
> Analicemos: correr en segundo plano claude debe cumplir las reglas y para eso se creo una regla que prohibe hacer eso

**Agente**, 2026-10-02 08:45:47
<!-- agente: f456cad7-91f5-4aff-942d-7f0f27406014 -->

Lo que dice el usuario es correcto. Revisé qué hay hoy y dónde está el hueco.

- **La regla:** `04·S9` prohíbe escribir por fuera del proyecto, y `01·C29` pide que todo lo del proyecto viva en el repositorio. No hay una regla que nombre «segundo plano», pero `S9` lo cubre: correr en segundo plano hace que la herramienta escriba la salida en `AppData/Local/Temp/...`.
- **El freno:** `hook_antes.py` revisa, antes de cada escritura, que el archivo quede dentro del proyecto. Pero en `.claude/settings.json` solo se engancha a `Write`, `Edit`, `MultiEdit` y `NotebookEdit`.
- **El hueco:** el freno no revisa la herramienta `Bash`. Por eso pasaron las dos cosas de hoy: la redirección `> .../scratchpad/pruebas.txt` y el `run_in_background`. La regla existe, pero el programa no detiene esa forma de romperla, y yo la rompí.

**Propuesta:**
1. Ampliar `hook_antes.py` a `Bash`.
   - Si la orden trae `run_in_background`, la detiene y explica que la corrida va en primer plano.
   - Si redirige la salida a una ruta por fuera del proyecto, también la detiene.
2. Anotar el hallazgo (H-8) en el resumen de la sesión, porque esto no lo previó ningún análisis.

Si el usuario lo quiere como mejora del estándar, la cadena pide pendiente, análisis, HU y fase. Para analizarlo con su archivo, primero hace falta el pendiente.

¿Lo anoto como H-8 y abro el pendiente?

### 142 · Usuario, 2026-10-02 08:51:34
> Analicemos: No se trata de que la regla diga “segundo plano”; se trata de que existe una regla y esta debe cumplirse en todas partes. ¿O es necesario crear una nueva regla que diga exactamente lo mismo para cada caso?

**Agente**, 2026-10-02 08:51:44
<!-- agente: bfb4c1c7-a956-4128-9de8-a77e3fd2c6c7 -->

No hace falta una regla nueva. `04·S9` ya dice «escribir fuera del proyecto, no», y eso vale para cualquier forma de escribir: con `Write`, con una redirección en `Bash` o con una corrida en segundo plano. Escribir otra regla para cada caso sería duplicar, y `20·M12` dice que la duplicación es el defecto más caro.

Lo que falló fue cumplirla: la regla me llegó con el mensaje y aun así escribí afuera. El error es mío, no de la regla.

Ampliar el freno a `Bash` no crea otra regla: hace que la misma `S9` la detenga un programa en un caso más, en vez de depender de que yo me acuerde. Recomiendo hacerlo, porque hoy fallé con la regla delante.

¿Se anota como hallazgo (H-8) y se abre el pendiente para ampliar el freno?

### 143 · Usuario, 2026-10-02 08:53:30
> Pregunta: pero ese freno ya no se analizó luego?

**Agente**, 2026-10-02 08:54:01
<!-- agente: 94893347-a2e4-4298-9c33-402e7ce50d19 -->

Sí, se analizó, pero para un caso distinto.

- **Antes, en EP-005, HU-023:** nació `hook_antes.py`, después de que el agente escribiera guiones en la carpeta temporal el 2026-09-28. Quedó enganchado solo a `Write` y `Edit`.
- **Después, en el análisis 1 (punto 26):** se decidió un freno más amplio: «antes de cada escritura y antes de correr pruebas», que compare con el plan aprobado. Quedó en el CA-02 de la HU-007 de EP-023, que todavía no se construye.

Ninguno de los dos dice que el freno revise las escrituras que se hacen por `Bash`, como una redirección o la salida de una corrida en segundo plano. El CA-02 de la HU-007 dice «escribir un archivo», y al construirlo se podría volver a dejar solo en `Write` y `Edit`.

**Recomendación:** no abrir un pendiente nuevo. El hueco cabe en la HU-007, que ya trata del freno. Se anota como H-8, y cuando se trabaje la HU-007 su análisis decide si el CA-02 dice expresamente que cubre todas las formas de escribir, incluida `Bash`.

¿Se anota así?

### 144 · Usuario, 2026-10-02 08:59:45
> Analicemos: Entienda que Cimiento es la base de todos los proyectos que lo implementan. Por lo tanto, los análisis deben realizarse considerando todas las posibilidades que puedan presentarse, y no pensando únicamente en un caso particular.
>
> En los análisis sí puede proponer todo lo que considere necesario, precisamente porque esta es la etapa en la que se deben discutir, evaluar y aprobar las diferentes posibilidades antes de definir cómo se va a proceder.

**Agente**, 2026-10-02 09:00:16
<!-- agente: 4b25303c-e855-459f-9b02-b4d1927e37ce -->

Entendido. Cimiento lo heredan proyectos con otras herramientas, otros agentes y otros sistemas, así que el análisis tiene que cubrir todas las formas en que el agente puede escribir, y no solo la que falló hoy.

**Por dónde puede escribir el agente:**

| # | Canal | Ejemplo | ¿Lo ve hoy el freno? |
|---|---|---|---|
| 1 | Herramienta de escritura | `Write`, `Edit`, cuaderno | Sí |
| 2 | Redirección en la consola | `>`, `>>`, `tee` | No |
| 3 | Orden de consola que crea, copia, mueve o borra | `cp`, `mv`, `rm`, `mkdir`, `sed -i`, `git` | No |
| 4 | Programa que escribe por dentro | `python -c "open(...,'w')"`, un guion | No, y leyendo la orden no se puede saber |
| 5 | Corrida en segundo plano | La herramienta guarda la salida en su carpeta temporal | No |
| 6 | Subagentes y flujos de varios agentes | Un agente lanzado por otro | Depende de si heredan los enganches |
| 7 | Servicios externos | Publicar un documento, una página o un comentario | No |
| 8 | Almacenes propios de la herramienta | Memoria, planes y transcripciones en `~/.claude` | Solo la memoria, con `hook_recuerdos.py` |
| 9 | Otra herramienta u otro agente que no es Claude Code | Cada una con sus propios canales | Solo si su adaptador los engancha |

**Propuestas:**
1. **El freno mira el efecto, no el nombre de la herramienta.** Se engancha a toda acción y la clasifica: escribe, borra, ejecuta o publica. `S9` y el plan aprobado se aplican igual a todas.
2. **Para la consola, dos controles:**
   - Antes de correr la orden, detiene las redirecciones y las órdenes conocidas que escriben fuera del proyecto o fuera del plan.
   - Después de correrla, compara el estado de git con el plan. Así se ve lo que escribió por dentro un programa (canal 4), aunque solo dentro del proyecto.
3. **Segundo plano prohibido por el freno.** La salida de las pruebas es evidencia del proyecto (`01·C29`), y la herramienta la deja afuera. Lo largo corre en primer plano.
4. **Subagentes y servicios externos.**
   - Los subagentes quedan bajo el mismo freno; si la herramienta no se lo pasa, se declara en el mapa del amarre.
   - Publicar afuera se pide cada vez (`00·N1`, acción que no se deshace).
5. **Un contrato por adaptador.** Cimiento define la lista de canales, y cada adaptador dice cómo cubre cada uno o por qué no puede. Un validador revisa que ningún canal quede sin respuesta. Así sirve para cualquier herramienta (`20·M3`).
6. **Dónde queda.** Todo esto amplía el CA-02 de la HU-007, que es el freno.
   - El paso es anotar el hallazgo (H-8) y abrir el análisis 8 del pendiente 103 para reescribir la HU-007 antes de construirla.
   - Si alcanza para más de una HU, el análisis decide repartirla.

Además, propongo guardar como recuerdo esta indicación: el análisis cubre todos los casos que pueden pasar en cualquier proyecto, y en él se propone todo lo que haga falta discutir.

¿Se anota el H-8, se abre el análisis 8 y se guarda el recuerdo?

### 145 · Usuario, 2026-10-02 09:01:44
> Hagalo

**Agente**, 2026-10-02 09:03:15
<!-- agente: 5b588a96-28af-40d1-9126-e60f8fa512d3 -->

Ya abrí el análisis 8. Lleno su encabezado con el hallazgo y el pendiente.

Ahora el recuerdo.

Listo, quedaron hechas las tres cosas:

1. **H-8** anotado en el resumen de la sesión: el freno de las escrituras solo mira algunas herramientas.
2. **[Análisis 8](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md)** prendido. Su conversación arranca en el turno 141, donde empezó esta discusión, así que ya entran la tabla de los nueve canales y las seis propuestas.
3. **Recuerdo** [El análisis cubre todos los casos](../../../../historico-chat/memory/el-analisis-cubre-todos-los-casos.md), con su línea en el índice de la memoria.

`validar.py estandar` no muestra incumplimientos.

Lo que falta decidir en el análisis 8 son las seis propuestas: aprobarlas, cambiarlas o agregar otras.

### 146 · Usuario, 2026-10-02 09:38:00
> Analicemos: 
> 
> Es importante que en la plantilla quede un apartado que indique que **el análisis debe realizarse desde todas las perspectivas**, ya que una situación que se presenta en un caso particular puede presentarse en muchos otros.
>
> En otras palabras, el análisis no debe estar cerrado a un único caso, sino que debe considerar las diferentes posibilidades que puedan surgir.
> 

**Agente**, 2026-10-02 09:38:20
<!-- agente: 38eaa8b1-a3e2-427b-a52d-07e203da352e -->

Propuesta para la plantilla del análisis:

1. **Una sección obligatoria nueva, «Dónde más puede pasar»**, entre «Lo que aportó cada parte» y «Conclusiones». La tabla tiene tres columnas: el caso, dónde se presenta (otra herramienta, otro agente, otro proyecto, otro sistema) y la propuesta que lo cubre.
   - Si un caso queda sin propuesta, se dice por qué.
   - Arriba de la tabla va una nota: el análisis se hace desde todas las perspectivas, porque lo que pasa en un caso puede pasar en muchos otros.
2. **El validador `analisis.py` la exige**, igual que hoy exige las cuatro partes: un análisis aprobado sin esa sección no cierra. Así se cumple en cualquier proyecto que herede Cimiento, sin depender de que el agente se acuerde.
3. **¿Dónde se pide?** Hay dos caminos:
   - **A, recomendado:** una fase D de la HU-001, porque la plantilla y el validador del análisis son de esa HU (CA-02 y CA-06). Requiere reabrirla y sumarle un criterio.
   - **B:** una HU-008 nueva en EP-023.
4. **Este mismo análisis 8 la aplica desde ya:** la tabla de los nueve canales que se discutió es justo esa sección.

¿Se hace así, y por cuál camino, A o B?

### 147 · Usuario, 2026-10-02 09:43:07
> Analicemos: En el análisis no está quedando registrada la última respuesta del agente, sino la última intervención que escribió el usuario. Por ejemplo, la respuesta que me dé en esta interacción debería quedar registrada para que, cuando yo vuelva a escribir, sea esa la que aparezca como referencia.

**Agente**, 2026-10-02 09:43:48
<!-- agente: 992d1521-4901-4af1-85e7-411e2bc45a72 -->

Es cierto, y lo confirmé con el archivo: el análisis 8 tiene mi respuesta al turno 146, pero solo apareció cuando el usuario escribió el 147. Mientras el usuario lee una respuesta, esa respuesta todavía no está en el análisis.

**Causa:** es el mismo defecto del H-6, del que yo solo corregí la mitad.
- Al terminar cada respuesta corren dos enganches al mismo tiempo: `hook_historico.py`, que escribe la respuesta en la transcripción, y `hook_analisis.py`, que copia la transcripción al análisis.
- El segundo copia antes de que el primero escriba, así que la respuesta queda por fuera.
- La corrección del H-6 solo hizo que esa copia se repita al llegar el mensaje siguiente. Por eso la respuesta aparece tarde.

**Propuestas, pensando en cualquier herramienta y proyecto:**
1. **Recomendada: un solo programa escribe las dos cosas.**
   - `hook_historico.py`, apenas escribe la respuesta en la transcripción, llama él mismo a copiarla al análisis.
   - El enganche del análisis deja de correr al cierre, y como el orden queda fijo, no hay carrera.
   - Sirve con cualquier herramienta, porque no depende de en qué orden lance los enganches.
2. **Que el enganche del análisis espere** hasta que la respuesta aparezca en la transcripción, con un límite de unos segundos. Es más sencillo, pero si la herramienta tarda más que ese límite, vuelve a fallar.
3. **Pruebas:** en cualquiera de los dos casos, se agrega la prueba que hoy falta, la de la respuesta que llega después.

Esto sería el hallazgo H-9 y entra al análisis 8, junto con el freno, porque los dos son casos en que el programa no cubre todo lo que pasa en la realidad.

¿Se anota el H-9 y se toma la propuesta 1?

### 148 · Usuario, 2026-10-02 09:45:55
> No. corrija de una porque este es el análisis piloto y todo lo que salga se tiene que corregir en los que salgan despues de que se implemente esta mejora si se debe hacer así

**Agente**, 2026-10-02 09:53:11
<!-- agente: d4ac3622-0cf7-4a63-96e1-4a79c2fcd862 -->

Lo corrijo con la propuesta 1. Primero leo cómo escribe la respuesta `hook_historico.py`.

Ya moví la copia al análisis dentro de `hook_historico.py` y quité el enganche del cierre. Ahora agrego la prueba del H-9 y corro las pruebas.

Ya está corregido. Desde esta respuesta, la del agente debe quedar en el análisis 8 apenas termina, sin esperar al siguiente mensaje del usuario.

**Qué cambié:**
- **[hook_historico.py](../../../../adaptadores/claude-code/hook_historico.py):** después de escribir la respuesta en la transcripción, la pasa él mismo al análisis prendido. El orden queda fijo y ya no hay dos programas compitiendo.
- **[instalar.py](../../../../validadores/instalar.py) y `.claude/settings.json`:** el enganche del análisis ya no corre al cerrar el turno. Al llegar cada mensaje sí sigue corriendo, porque es el que prende, pausa y apaga el análisis.
- **Prueba nueva:** la del H-9 está en [test_analisis_en_curso.py](../../../../validadores/tests/test_analisis_en_curso.py). Las 23 pruebas del análisis pasan.
- **Suite del estándar:** pasan 570 de 571. La que falla ya fallaba antes, por el pendiente 103 al que le falta la fila «Historia de usuario».
- **Resumen de la sesión:** el H-9 quedó anotado como resuelto.

La comprobación de verdad es el análisis 8: cuando el usuario lo abra después de esta respuesta, ella ya debe estar ahí.

### 149 · Usuario, 2026-10-02 09:55:26
> Ok en dónde habíamos quedado?

**Agente**, 2026-10-02 09:55:32
<!-- agente: 6c2c3ec2-f7ec-48b0-b67f-a0bc26aee3f9 -->

Falta la palabra que dice qué se espera, por ejemplo «Pregunta».

### 150 · Usuario, 2026-10-02 09:56:05
> Pregunta: Ok en dónde habíamos quedado?

**Agente**, 2026-10-02 09:56:19
<!-- agente: 5dcd0872-97e2-404f-aedc-843a6b887a26 -->

Seguimos en el análisis 8, que está prendido. Quedan dos decisiones abiertas:

1. **El freno (H-8):** las seis propuestas para que `04·S9` se haga cumplir por todos los canales de escritura, en cualquier herramienta. Falta que el usuario las apruebe, las cambie o agregue otras.
2. **La sección «Dónde más puede pasar» en la plantilla del análisis:** falta elegir el camino.
   - **A, recomendado:** una fase D de la HU-001.
   - **B:** una HU-008 nueva.

El H-9, la respuesta que entraba tarde al análisis, ya quedó corregido.

Después de esas dos decisiones se escriben las conclusiones del análisis 8, se aprueba y se reescribe la HU-007 con su resultado. Lo pendiente de commit es la corrección del H-9, el análisis 8 y el recuerdo.

### 151 · Usuario, 2026-10-02 09:58:05
> 00 id9

**Agente**, 2026-10-02 09:58:10
<!-- agente: b7d242b9-f64a-4fee-aca0-300af0ebd32f -->

En el análisis 8 faltan dos decisiones:

1. Las seis propuestas del freno (H-8).
2. Por dónde va la sección «Dónde más puede pasar»: A, una fase D de la HU-001 (recomendada), o B, una HU-008.

### 152 · Usuario, 2026-10-02 10:04:46
> 1. Solo se presentan esa cituaciones?
> 2. A. 
> 
> Que quede claro que el análisis debe contemplar y abrir todas las posibilidades posibles para minimizar los riesgos y evitar que queden situaciones sin considerar.
>
> Además, desde el análisis debe surgir la propuesta de creación de las HU, de manera que se pueda identificar claramente la dependencia entre ellas. Actualmente se les asigna un número, pero el orden en que se solucionan puede ser diferente. Si se les asigna una numeración, debe quedar claro qué representa ese número y cuál es el orden que se debe seguir para su ejecución.
> 

**Agente**, 2026-10-02 10:04:56
<!-- agente: 406d808a-a134-49bd-8767-bafab4f6dee3 -->

Falta la palabra que dice qué se espera. Si es para seguir el análisis, «Analicemos».

### 153 · Usuario, 2026-10-02 10:06:21
> Analicemos:
> Respustas al punto 150
> 
> 1. Solo se presentan esa cituaciones?
> 2. A.
> Que quede claro que el análisis debe contemplar y abrir todas las posibilidades posibles para minimizar los riesgos y evitar que queden situaciones sin considerar.
>
> Además, desde el análisis debe surgir la propuesta de creación de las HU, de manera que se pueda identificar claramente la dependencia entre ellas. Actualmente se les asigna un número, pero el orden en que se solucionan puede ser diferente. Si se les asigna una numeración, debe quedar claro qué representa ese número y cuál es el orden que se debe seguir para su ejecución.
> 

**Agente**, 2026-10-02 10:06:50
<!-- agente: 78506088-feec-45dc-8b52-d307137e58c6 -->

**1. No, hay más situaciones.** Esta es la lista ampliada de las formas en que una regla del estándar se puede romper por donde el freno no mira:

| Grupo | Situaciones |
|---|---|
| Escribir o borrar fuera del plan, dentro del proyecto | `rm`, `mv`, `git checkout --`, `git clean`, `git reset` |
| Escribir fuera del proyecto | Instalar paquetes, que van a carpetas del sistema; cachés; descargas con `curl`; la configuración global (`git config --global`, variables de entorno, el registro de Windows) |
| Rutas que engañan | `..`, `~`, `%TEMP%`, `$HOME`; enlaces simbólicos que apuntan afuera; mayúsculas distintas en Windows; rutas de red |
| Acciones que siguen después del turno | Servidores o procesos que quedan corriendo; tareas programadas |
| Otros sistemas | Bases de datos reales (`04·S11`), procesos ajenos (`04·S10`), máquinas remotas, despliegues |
| Almacenes de la herramienta | Planes, listas de tareas, artefactos publicados, documentos en servicios externos |
| Herramientas sin enganches | Otros agentes que no tienen freno antes de actuar |

**Propuesta para cubrirlas todas: el freno en cuatro capas.** Ninguna capa sola alcanza.
1. **Antes de actuar:** el freno sobre toda acción, por su efecto.
2. **Después de actuar:** comparar el estado de git con el plan, para lo que escribió un programa por dentro.
3. **Al guardar el commit:** el enganche de git rechaza lo que no está en el plan. Esta capa sirve para cualquier herramienta, aunque no tenga enganches.
4. **En la integración continua:** la misma revisión, por si algo saltó las capas anteriores.

Además, el contrato del adaptador dice qué capas cubre en cada herramienta.

**2. Camino A, con dos cosas más para la plantilla del análisis:**
- **Abrir todas las posibilidades.** La sección «Dónde más puede pasar» suma una columna de riesgo: qué pasa si ese caso queda sin cubrir. El validador no deja cerrar el análisis si un caso queda sin propuesta ni razón.
- **Las HU con su dependencia y su orden.**
  - La tabla de HU de la propuesta final lleva estas columnas: número, título, de qué HU depende, orden de ejecución y por qué va en ese orden.
  - El número identifica a la HU y no cambia. El orden de ejecución es otro dato, y sale de las dependencias.
  - El validador revisa que ninguna HU vaya antes de una de la que depende, y que cada puesto tenga su razón.
  - La hoja de ruta de la épica copia ese orden.

Como este análisis es el piloto, propongo aplicarlo desde ya: rehacer aquí el orden de las HU que quedan de EP-023 (003, 004, 006 y 007) con sus dependencias. Ese orden quedó sin razones en el análisis 1.

¿Se toman las cuatro capas, las dos cosas para la plantilla y el orden de EP-023 en este análisis?

### 154 · Usuario, 2026-10-02 10:08:36
> 00 id9

**Agente**, 2026-10-02 10:08:43
<!-- agente: 77a7d9d6-71ac-486e-a887-4a9da4374979 -->

**1. Hay más situaciones**, además de los nueve canales: borrar o mover archivos con la consola o con git, instalar paquetes o tocar la configuración global, rutas que engañan (`..`, `~`, enlaces que apuntan afuera), procesos que siguen corriendo después del turno, bases de datos o máquinas remotas, y herramientas que no tienen enganches.

Propongo cubrirlas con un freno en cuatro capas: antes de actuar, después de actuar, al guardar el commit y en la integración continua.

**2. Camino A, más dos cosas para la plantilla del análisis:**
- La sección «Dónde más puede pasar» lleva una columna de riesgo, y el análisis no cierra si un caso queda sin cubrir.
- La tabla de HU lleva de qué HU depende cada una, su orden de ejecución y por qué. El número solo identifica a la HU; el orden es otro dato.

Además, rehacer aquí el orden de las HU 003, 004, 006 y 007 de EP-023.

¿Se toma todo eso?

### 155 · Usuario, 2026-10-02 10:12:49
> Hágalo

**Agente**, 2026-10-02 10:16:06
<!-- agente: 67f96458-c620-4fbe-9412-12a7cfcacee7 -->

El texto rompió el comando de la consola. Lo paso por un guion dentro del repositorio, como pide `04·S18`.

Ya escribí lo que faltaba del [análisis 8](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md):

- **Las cuatro partes**, y **la sección «Dónde más puede pasar»** puesta a prueba aquí mismo: 12 casos, cada uno con su riesgo y con lo que lo cubre.
- **Ocho conclusiones**: el freno en cuatro capas, la sección nueva, las HU con su dependencia y su orden, y la fase D de la HU-001, entre otras.
- **El orden de las HU que siguen, cada una con su razón**: HU-001 fase D, HU-003, HU-006, HU-004 y HU-007.
- **Cuatro puntos en «Lo que se tiene que hacer»**: reescribir la HU-007, dos criterios para la HU-001 y la hoja de ruta de EP-023.

`validar.py estandar` y `origen` pasan sin incumplimientos, y lo escrito no tiene marcas de `00·ID8`.

Para cerrarlo: «Apruebo el análisis».

### 156 · Usuario, 2026-10-02 10:17:34
> Analicemos:
> 
> Al inicio de la plantilla debe existir un apartado de **recomendaciones**, que se irá alimentando con los diferentes análisis que se realicen. Sin embargo, no se deben agregar recomendaciones simplemente por agregarlas; primero se debe revisar si ya existe alguna que pueda complementarse o si realmente es necesario crear una nueva.
>
> De esta manera, cuando se esté realizando un análisis, se podrán consultar las recomendaciones existentes para tener claro cómo se deben hacer las cosas.
> 

**Agente**, 2026-10-02 10:17:54
<!-- agente: e3c46c8c-d7a1-42be-9389-112380d1a753 -->

Propuesta, pensando en cualquier proyecto que herede Cimiento:

1. **Dónde viven.** En un solo archivo, `plantillas/recomendaciones-del-analisis.md`, y no copiadas dentro de cada análisis: dos copias terminan diciendo cosas distintas.
   - La plantilla abre con una sección «Recomendaciones» que lo enlaza.
   - En esa sección, el análisis dice cuáles aplican a su caso.
2. **Dos niveles.**
   - Las de Cimiento sirven a todos los proyectos, viajan con el estándar y llevan versión.
   - Cada proyecto tiene además las suyas, en su propio archivo.
   - Una recomendación del proyecto que sirva a todos sube a Cimiento.
3. **Cómo se alimentan.** De las lecciones de cada análisis. La tabla de lecciones suma una columna que dice qué pasó con cada una: complementa la recomendación R-N, crea una nueva o no aplica. Antes de crear una se busca si ya existe, como manda `20·M12`.
4. **Forma de cada recomendación:** número, qué se hace, por qué y de qué análisis sale, con su enlace (`02·F27`).
5. **Qué la separa de lo demás:**
   - Una regla se exige y se puede comprobar.
   - Una recomendación es cómo se hace bien un análisis.
   - Un recuerdo es una preferencia del usuario.

   Si una recomendación se vuelve exigible, sube a regla y queda el registro de dónde salió. El recuerdo «El análisis cubre todos los casos» pasa a ser la R-1.
6. **El validador revisa** tres cosas: que cada recomendación cite su análisis, que no haya dos iguales y que cada análisis aprobado diga cuáles consultó.
7. **Dónde se pide:**
   - La sección y el archivo van en la fase D de la HU-001, junto con lo demás de la plantilla.
   - Alimentarlas desde las lecciones va en la HU-006, que trata de las lecciones. Así la HU-006 pasa a depender de la fase D.
8. **Arranque:** el archivo nace con las recomendaciones que ya dejaron las lecciones de los análisis 1 a 8. Por ejemplo, revisar qué reglas citan lo que se deroga, revisar las plantillas que tienen que llevar un campo nuevo, medir antes de escribir el plan y explicar con un ejemplo sencillo.

¿Se toma así?

### 157 · Usuario, 2026-10-02 10:21:30
> hágalo

**Agente**, 2026-10-02 10:22:40
<!-- agente: a889e043-3749-45ef-9dca-2b31beff6c3c -->

The HU-006 folder name differs from what I wrote (`…las-lecciones`); I fix the link.

Ya agregué al [análisis 8](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md) lo de las recomendaciones:

- **Conclusión 9:** dónde viven las recomendaciones, sus dos niveles y su forma, la búsqueda antes de crear una, el validador y las de arranque.
- **Conclusión 10:** se alimentan de las lecciones. Eso va en la HU-006, que por eso pasa a depender de la fase D de la HU-001.
- **«Dónde más puede pasar»** suma el caso de la recomendación repetida o sin origen.
- **«Lo que se tiene que hacer»** suma los puntos 5 y 6: un criterio para la fase D de la HU-001 y otro para la HU-006.

Un enlace a la HU-006 quedó con el nombre mal escrito y ya lo corregí. `validar.py estandar` y `origen` no muestran incumplimientos.

Para cerrarlo: «Apruebo el análisis».

### 158 · Usuario, 2026-10-02 10:23:43
> Pregunta: hay algo más que se pueda trabajar en este análisis teniendo en cuenta toda la discusión que hemos tenido?

**Agente**, 2026-10-02 10:24:04
<!-- agente: 2491d609-3f2b-40d5-9ec2-06b87386b82e -->

Sí, revisando toda la conversación quedan cinco cosas que este análisis podría tomar:

1. **El análisis principal está atrasado.** `13·DOC25` pide que cada análisis que cambia lo que se construye sume su línea a la lista de cambios de [`analisis/proyecto-2026-10-02-analisis-principal.md`](../../../../analisis/proyecto-2026-10-02-analisis-principal.md). Los análisis 6 y 7 no la sumaron, y el 8 tampoco la tiene. Propongo sumar las tres y que el validador avise cuando un análisis aprobado cambia una HU y no aparece en esa lista.
2. **Las respuestas a una pregunta del agente se bloquean.** Hoy, «sí», «A», «00 id9» y «explique para niño» se detuvieron por `01·C28` aunque eran respuestas claras. Propongo que, cuando el agente acaba de hacer una pregunta, una respuesta corta del usuario cuente como respuesta, y que «00 id9», o cualquier cita de una regla, valga como «aplique esa regla».
3. **El largo de las respuestas solo se mide después.** `00·ID9` se incumplió muchas veces hoy, porque la medida llega en el turno siguiente. Propongo que se vuelva recomendación del análisis medir la respuesta antes de entregarla. Además, que «00 id9» repetido varias veces en una sesión quede como lección.
4. **Los hallazgos al escribir el plan.** El H-5 y el H-7 salieron al escribir el plan, y cada uno costó un análisis. Propongo como recomendación de arranque revisar, antes de cerrar un análisis, qué reglas, plantillas y validadores toca cada punto de «Lo que se tiene que hacer».
5. **Las lecciones «Por escribir» se acumulan.** Ya van más de veinte entre los análisis 1 y 8. Lo resuelve la HU-006, y por eso el orden ya la pone en tercer lugar.

Además, hay cambios sin commit: la corrección del H-9, el análisis 8, el recuerdo y el estado de la fase de la HU-002.

¿Cuáles se suman al análisis?

### 159 · Usuario, 2026-10-02 10:46:59
> 1. Aceptada la propuesta
> 2. Si, explique para niño, cuando escribo el id de la regla no es para que la explique sino para que la aplique. Cuando escribí A era diciendo que escogía esa opción entonces no se si sea correcto manejarla como una respuesta corta
> 3. Aceptada la propuesta
> 4. O sea, lo que se propone es volver a analizar lo que está definido en **“Lo que se tiene que hacer”**. De hecho, por eso fue que surgió **“Lo que aportó cada parte”**, con el propósito de que el análisis pudiera revisarse desde diferentes ángulos. Precisamente, de ahí surgió el hallazgo que desencadenó este análisis.
> 5. No entiendo
> Que se debe hacer con el H-9?

**Agente**, 2026-10-02 10:47:09
<!-- agente: c496e617-276f-492b-b05b-3d8868a4c227 -->

Falta la palabra que dice qué se espera, por ejemplo «Analicemos». Es justo el caso del punto 2.

### 160 · Usuario, 2026-10-02 10:47:50
> Analicemos:
> 
> 1. Aceptada la propuesta
> 2. Si, explique para niño, cuando escribo el id de la regla no es para que la explique sino para que la aplique. Cuando escribí A era diciendo que escogía esa opción entonces no se si sea correcto manejarla como una respuesta corta
> 3. Aceptada la propuesta
> 4. O sea, lo que se propone es volver a analizar lo que está definido en **“Lo que se tiene que hacer”**. De hecho, por eso fue que surgió **“Lo que aportó cada parte”**, con el propósito de que el análisis pudiera revisarse desde diferentes ángulos. Precisamente, de ahí surgió el hallazgo que desencadenó este análisis.
> 5. No entiendo
> Que se debe hacer con el H-9?
> 

**Agente**, 2026-10-02 10:48:13
<!-- agente: bcf563bf-9fd7-48e0-9a41-61fd210db06b -->

**2. Explicado para un niño.** Hoy pasan tres cosas distintas con los mensajes cortos:
- **«00 id9»** quiere decir «aplique esa regla a lo que acaba de responder», no «explíquela». El agente debe rehacer su última respuesta cumpliendo la regla.
- **«A»** quiere decir «escojo la opción A». Es una decisión, no una respuesta corta cualquiera.
- **«sí»** después de una pregunta del agente quiere decir «se acepta lo que propuso».

Propuesta: que el programa reconozca esos tres casos.
- Un mensaje que es solo el número de una regla equivale a «aplique esa regla».
- Si el último mensaje del agente terminó en una pregunta, la opción o el «sí» del usuario quedan como su decisión.

Escribir o cambiar archivos sigue pidiendo su palabra.

**4. Tiene razón.** Para eso ya existe «Lo que aportó cada parte», así que retiro la propuesta. Lo que falló en el H-5 y el H-7 fue que esas cuatro partes se hicieron por encima, sin revisar contra cada punto de «Lo que se tiene que hacer». Eso queda como lección del análisis, no como algo nuevo.

**5. Más sencillo.** Cada análisis tiene una tabla de lecciones, y en la columna «Señal» casi todas dicen «Por escribir»: la lección quedó anotada, pero todavía no está guardada en el lugar de las lecciones. Ese lugar lo crea la HU-006. En este análisis no hay que hacer nada más con eso, así que lo retiro.

**H-9.** Ya está corregido, y figura en la conclusión 7. Le faltan dos cosas:
- El commit.
- Su línea en el CHANGELOG con la versión que corresponda: cambió `instalar.py`, que viaja a los proyectos, y eso pide `20·M10`.

¿Se suman al análisis los puntos 1, 2 y 3, la lección del punto 4 y lo del H-9?

### 161 · Usuario, 2026-10-02 10:50:44
> si

**Agente**, 2026-10-02 10:50:54
<!-- agente: 99ca633d-b796-4275-82a1-d80557b9a2eb -->

Queda acordado. Para escribirlo en el análisis 8 falta «Hágalo», que es justo el caso del punto 2 que se está resolviendo.

### 162 · Usuario, 2026-10-02 10:51:05
> Hágalo

**Agente**, 2026-10-02 10:53:15
<!-- agente: 9880b7ad-0779-466d-a014-3544ee9c6012 -->

Ya está escrito en el [análisis 8](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md):

- **Conclusiones 11 a 15:**
  - El análisis principal se pone al día.
  - El programa reconoce las respuestas cortas.
  - Medir el largo de la respuesta antes de entregarla queda como recomendación.
  - Revisar lo que se tiene que hacer queda como lección, sin nada nuevo.
  - La corrección del H-9 entra con su versión.
- **Dos lecciones nuevas:** las cuatro partes se hicieron por encima en los análisis 1 a 5, y hubo que pedir «00 id9» muchas veces.
- **Tres casos más en «Dónde más puede pasar».**
- **Lo que se tiene que hacer pasa a 10 puntos.** El 8 va a la HU-036 de EP-001, que es la dueña de `01·C28`. El 10 se cumple en el commit que suba la corrección del H-9.

`validar.py estandar` y `origen` no muestran incumplimientos, y lo escrito no tiene marcas de `00·ID8`.

Para cerrarlo: «Apruebo el análisis».

### 163 · Usuario, 2026-10-02 10:58:23
> ya no hay nada más que sea competencia de este análisis?

**Agente**, 2026-10-02 10:58:30
<!-- agente: 203c7404-8085-48ee-a6c4-bb76de162dad -->

Falta la palabra que dice qué se espera, por ejemplo «Pregunta».

### 164 · Usuario, 2026-10-02 11:01:17
> Pregunta: ya no hay nada más que sea competencia de este análisis?

**Agente**, 2026-10-02 11:01:31
<!-- agente: 8c4f1b95-5b50-496b-bb16-0003c73c4874 -->

Quedan dos cosas, y las dos son de este análisis:

1. **Los análisis ya aprobados.** Cuando el validador de la fase D exija «Dónde más puede pasar», las recomendaciones y la tabla de HU con su orden, los análisis 1 a 7 van a fallar, porque nacieron antes de esa exigencia. Propongo que solo se exija a los análisis que se aprueben desde la versión que lo trae, como ya hace `02·F27` con las épicas anteriores (`20·M10`).
2. **El destino del punto 8.** Las respuestas cortas van a la HU-036 de EP-001, que es dueña de `01·C28`, pero esa HU ya está terminada y no es de EP-023. Hay dos caminos:
   - Reabrirla con una fase nueva. Es el que recomiendo, porque es la dueña de la regla.
   - Abrir un pendiente aparte.

Fuera de esos dos, no veo nada más: el resto de lo que se habló ya tiene su conclusión y su destino.

¿Se suman los dos, con la HU-036 reabierta?

### 165 · Usuario, 2026-10-02 11:04:21
> Pregunta: el punto 8 impida que se siga con la epica 23?

**Agente**, 2026-10-02 11:04:27
<!-- agente: c4db1e4d-42d8-491d-87aa-8ea3ba089ebf -->

No. Ninguna HU de EP-023 depende del punto 8, así que la épica puede seguir con su orden sin esperarlo.

Lo único que cuesta mientras no se resuelva son turnos: respuestas como «sí», «A» o «00 id9» se seguirán deteniendo y habrá que repetirlas con su palabra.

### 166 · Usuario, 2026-10-02 11:06:01
> pregunta: sino impide por qué surgió acá?

**Agente**, 2026-10-02 11:06:17
<!-- agente: 236a10d8-b83c-4f71-a96b-5d04b9445689 -->

Surgió porque yo lo traje. El usuario preguntó qué más se podía trabajar teniendo en cuenta toda la discusión, y yo incluí algo que se vio durante la conversación pero que no es parte del problema de este análisis.

El análisis 8 trata el H-8 y lo que sale de él (conclusión 19 del análisis 1). Las respuestas cortas que se detienen son otro hallazgo, con su propio origen en `01·C28`. Meterlo aquí fue agregar lo que no se pidió (`01·C30`).

**Propuesta:**
- Quitar del análisis 8 la conclusión 12, el punto 8 de «Lo que se tiene que hacer» y su caso en «Dónde más puede pasar».
- Anotarlo como H-10 en el resumen de la sesión, con su propio pendiente, para que siga su cadena por la dueña de la regla, la HU-036.

¿Se hace así?

### 167 · Usuario, 2026-10-02 11:13:38
> Hagalo

**Agente**, 2026-10-02 11:15:26
<!-- agente: b3622587-797f-4325-981a-082d28d23495 -->

Ya existe el pendiente 106, «La cita "00 id9" trae la regla», que toca parte de esto. Lo leo antes de crear uno nuevo.

El 106 trata de que la regla citada llegue, y en su límite dice que no cambia `01·C28`. Lo del H-10 queda fuera de él, así que va en un pendiente nuevo, el 108, que lo enlaza.

Ahora anoto el H-10 y creo el pendiente 108.

Ya está hecho:

- **[Análisis 8](../../../../documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/103-cada-documento-de-la-cadena-sale-del-anterior/analisis-8.md):** saqué la conclusión de las respuestas cortas, su punto de «Lo que se tiene que hacer» y su caso en «Dónde más puede pasar». Quedan 14 conclusiones y 9 puntos, numerados de nuevo y con sus citas al día.
- **H-10** anotado en el resumen de la sesión.
- **Pendiente 108 (`pendientes/108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta.md`, ya no está ahí)** creado con su línea en el índice. Lo asigné a la HU-036 de EP-001, que es la dueña de `01·C28`. Enlaza el pendiente 106 en vez de repetirlo, porque el 106 solo trata de que la cita traiga el texto de la regla.

`validar.py estandar`, `origen` y `pendientes` no muestran fallas nuevas. La única falla que queda es la de siempre, el pendiente 103 sin su fila «Historia de usuario».

Queda abierta la propuesta de no exigir las secciones nuevas a los análisis 1 a 7, que ya están aprobados. Si se acepta, se suma al análisis antes de aprobarlo.

### 168 · Usuario, 2026-10-02 11:17:37
> 
> Pregunta: pero por qué lo está agregando a los pendientes si ya se acordó que allá no van y para eso se creo una estructura

**Agente**, 2026-10-02 11:17:50
<!-- agente: af8f8721-ce97-48f7-9440-01af0ac43cf3 -->

Por error mío. El análisis 1 lo decidió y quedó aprobado: cada pendiente vive dentro de lo que lo genera, y la carpeta `pendientes/` ya no recibe pendientes nuevos (conclusión 11 y puntos 7 y 21). Como la HU-003, que construye esa estructura, todavía no está hecha, seguí con la costumbre vieja en vez de aplicar lo aprobado.

**Propuesta para corregirlo:**
- Mover el pendiente a `documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta/pendiente.md`, junto a la HU-036, que es la dueña de `01·C28`. Así quedó el pendiente 103 dentro de EP-023.
- Quitar su línea del índice de `pendientes/` y apuntar el enlace del H-10 a la ruta nueva.
- **Lo que hay que saber:** `validar.py fases` va a marcar esa carpeta igual que marca hoy la del 103, porque todavía exige que dentro de una épica solo haya HU. Esa falla la resuelve la HU-003.

¿Lo corrijo así?

### 169 · Usuario, 2026-10-02 11:19:00
> Hágalo pero es que es pendiente no es de la épica sino de la HU y eso también se acordó

**Agente**, 2026-10-02 11:21:03
<!-- agente: ad190fd9-25dd-4742-a514-069c01c46b0f -->

Quedó corregido:

- **El pendiente** está ahora en la carpeta de la HU-036: `EP-001/HU-036-…/108-la-respuesta-corta-…/pendiente.md` (`documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta/pendiente.md`, ya no está ahí). Ajusté sus enlaces, quité su línea del índice de `pendientes/` y el H-10 apunta a la ruta nueva.
- **Un enlace roto en el análisis 8.** Al mover el archivo se rompió un enlace de mi respuesta copiada en la conversación del análisis. Corregí el programa que la copia: un enlace cuyo destino ya no existe pasa como texto con la ruta y la aclaración «ya no está ahí». Agregué su prueba y las 10 pruebas pasan.
- `validar.py estandar` no muestra incumplimientos.
- `validar.py fases` marca la carpeta nueva, igual que la del 103, porque todavía exige que dentro de una HU o de una épica solo haya lo de antes. Esa falla la resuelve la HU-003.

Sigue abierta la propuesta de no exigir las secciones nuevas a los análisis 1 a 7, que ya están aprobados.

### 170 · Usuario, 2026-10-02 11:21:20
> Pregunta: cuál fue la estructura que se acordó para los pendientes?

**Agente**, 2026-10-02 11:21:54
<!-- agente: e40e26c7-4fe1-4e66-b9ba-4220f6899876 -->

Según el análisis 1 (conclusiones 11, 15, 20 y 36):

- **Dónde va:** cada pendiente es una carpeta dentro de lo que lo genera. Si nace de una conversación y todavía no se sabe a dónde va, vive en la carpeta del resumen del día. La carpeta `pendientes/` desaparece.
- **Qué tiene la carpeta:** `pendiente.md` con la versión vigente y `analisis-1.md`, más `analisis-2.md` y los siguientes si aparecen hallazgos al ejecutar.
- **Qué tiene `pendiente.md`:** solo «De dónde sale», «El problema» y «Por qué importa». La HU que dispara y dónde vive lo decide el análisis. Sobra «Proyecto de origen», porque el enlace de «De dónde sale» ya lo dice.
- **Cuándo cierra:** cuando cierra el plan que salió de él. Ni el pendiente ni el hallazgo dicen que algo cerró.

Con esa vara, el pendiente 108 que escribí está mal en tres cosas:
1. **El lugar.** Nació de una conversación y ningún análisis ha decidido a dónde va, así que no le corresponde la carpeta de la HU-036. Le corresponde la carpeta del resumen del día, `historico-chat/resumenes/2026-10-01/`.
2. **Los campos.** Usé la plantilla vieja: estado, HU, proyecto de origen, qué falta, el límite y cómo se sabrá que cerró. Solo van los tres de arriba.
3. **El análisis.** Le falta su `analisis-1.md`, donde se decide la HU.

¿Lo corrijo así?

### 171 · Usuario, 2026-10-02 11:23:30
> deme el mapa de la estructura que definimos

**Agente**, 2026-10-02 11:23:36
<!-- agente: 6ef49934-359a-4de6-8d1c-0931b82e8b62 -->

Falta la palabra que dice qué se espera, por ejemplo «Explique».

### 172 · Usuario, 2026-10-02 11:23:58
> Explique

**Agente**, 2026-10-02 11:24:16
<!-- agente: e7128e24-6023-4e3a-bd02-7c95860457af -->

Este es el mapa de lo que se definió en el análisis 1 (conclusiones 11, 20 y 32):

```
proyecto/
├── planteamiento.md
├── analisis/
│   └── <...>-analisis-principal.md      ← se reescribe con su lista de cambios (13·DOC25)
├── documentacion/epicas/
│   └── EP-NNN-<épica>/
│       ├── epica.md
│       ├── NNN-<pendiente>/             ← pendiente que generó la épica
│       │   ├── pendiente.md             ← De dónde sale · El problema · Por qué importa
│       │   ├── analisis-1.md            ← nunca se reescribe
│       │   └── analisis-2.md …          ← uno más por cada hallazgo al ejecutar
│       └── HU-NNN-<historia>/
│           ├── HU-NNN-<historia>.md
│           ├── NNN-<pendiente>/         ← pendiente que generó la HU (misma estructura)
│           └── A-…-<fase>/              ← plan, pruebas, resultado, estado
└── historico-chat/resumenes/AAAA-MM-DD/
    ├── sesion.md                        ← hallazgos: Qué pasó · Por qué importa
    └── NNN-<pendiente>/                 ← pendiente que nace de una conversación,
                                            mientras su análisis no decide a dónde va
```

**Las tres reglas del mapa:**
1. La carpeta del pendiente es siempre igual: `pendiente.md` más sus análisis. Lo único que cambia es dónde queda.
2. Queda dentro de lo que lo genera. Si nace de una conversación, queda en la carpeta del resumen del día hasta que su análisis decida si amplía el planteamiento o crea una épica o una HU.
3. `pendientes/` desaparece. Los que ya están ahí quedan como historia, y no entra ninguno nuevo.

Con este mapa, el pendiente 108 va en `historico-chat/resumenes/2026-10-01/108-…/`, con `pendiente.md` de tres campos y su `analisis-1.md`.

### 173 · Usuario, 2026-10-02 11:27:19
> Analicemos: La carpeta `pendientes` debe estar siempre dentro de la carpeta que la origina. Dentro de ella debe quedar cada pendiente junto con sus respectivos análisis.

**Agente**, 2026-10-02 11:27:43
<!-- agente: e26337ca-e4d1-4ca3-b3ea-376098800c14 -->

Queda así. El mapa cambia en un punto: dentro de lo que origina el pendiente no va su carpeta suelta, sino una carpeta `pendientes/`, y dentro de ella cada pendiente con sus análisis.

```
documentacion/epicas/EP-NNN-<épica>/
├── epica.md
├── pendientes/
│   └── NNN-<pendiente>/
│       ├── pendiente.md          ← De dónde sale · El problema · Por qué importa
│       ├── analisis-1.md
│       └── analisis-2.md …
└── HU-NNN-<historia>/
    ├── HU-NNN-<historia>.md
    ├── pendientes/
    │   └── NNN-<pendiente>/ …
    └── A-…-<fase>/
historico-chat/resumenes/AAAA-MM-DD/
├── sesion.md
└── pendientes/
    └── NNN-<pendiente>/ …        ← mientras su análisis no decide a dónde va
```

**Lo que propongo además, pensando en cualquier proyecto:**
1. **Numeración única en todo el proyecto.** El número sigue siendo uno solo para todos los pendientes, estén donde estén. Así no hay dos «108», y las citas que ya existen no cambian.
2. **Un índice que se arma solo.** Como los pendientes quedan repartidos, un programa los lista todos con su número, dónde viven y si su plan ya cerró. Nadie lo mantiene a mano.
3. **El validador de fases** acepta una carpeta `pendientes/` dentro de una épica, de una HU o de un resumen del día, y nada más. Eso resuelve la falla que hoy deja la carpeta del 103.
4. **Mover, no copiar.** Cuando el análisis decide a dónde va el pendiente, la carpeta se mueve desde el resumen del día a su destino, y lo que la enlazaba se actualiza.
5. **Dónde se pide.** Esto precisa la conclusión 11 del análisis 1 y es de la HU-003, que construye la estructura de los pendientes. Entra a este análisis como una conclusión más y como un punto de «Lo que se tiene que hacer» para la HU-003.
6. **El pendiente 108 ahora:** va a `historico-chat/resumenes/2026-10-01/pendientes/108-…/`, con `pendiente.md` de tres campos y su `analisis-1.md` por hacer.

¿Se toma así?

### 174 · Usuario, 2026-10-02 11:30:52
> 6. por qué va ahí si ya se sabe a quién pertenece?

**Agente**, 2026-10-02 11:30:58
<!-- agente: b9a81783-2a4b-4d6c-bbad-af8b42d6f582 -->

Falta la palabra que dice qué se espera, por ejemplo «Pregunta».

### 175 · Usuario, 2026-10-02 11:31:18
> Pregunta: 6. por qué va ahí si ya se sabe a quién pertenece?

**Agente**, 2026-10-02 11:31:26
<!-- agente: 7ca764fd-b17f-4b66-9061-daf11f8f51a1 -->

No tiene por qué ir ahí. La carpeta del resumen del día es solo para cuando todavía no se sabe a quién pertenece el pendiente. En este caso ya se sabe: el usuario lo decidió en este análisis, y es de la HU-036, dueña de `01·C28`.

Entonces va en la carpeta de pendientes de esa HU:

```
documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/
└── pendientes/
    └── 108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta/
        ├── pendiente.md      ← De dónde sale · El problema · Por qué importa
        └── analisis-1.md     ← se abre cuando se trabaje
```

El punto 6 queda así. ¿Se toman los seis puntos con este cambio?

### 176 · Usuario, 2026-10-02 11:31:58
> si

**Agente**, 2026-10-02 11:32:07
<!-- agente: 5ad889e6-981e-4119-8b78-ed17451f6409 -->

Queda acordado. Para escribirlo en el análisis 8 y mover el pendiente 108 falta «Hágalo».

### 177 · Usuario, 2026-10-02 11:32:52
> Hágalo

**Agente**, 2026-10-02 11:34:33
<!-- agente: 8a80e39f-e15e-4437-8440-24f62a581626 -->

Es el mismo caso de antes: un enlace de la conversación copiada apunta a la ruta vieja. Hago que el programa vuelva a copiar la conversación, para que lo pase como texto.

Listo:

- **Pendiente 108**: quedó en [`HU-036/pendientes/108-…/pendiente.md`](../../../../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-036-el-pedido-dice-que-se-espera/pendientes/108-la-respuesta-corta-a-una-pregunta-cuenta-como-respuesta/pendiente.md), solo con sus tres campos: «De dónde sale», «El problema» y «Por qué importa». El H-10 apunta a esa ruta.
- **Análisis 8**:
  - La conclusión 15 dice dónde vive el pendiente: la carpeta `pendientes/` dentro de lo que lo origina, la numeración única, el índice que se arma solo, el validador de fases y el traslado.
  - El punto 10 de «Lo que se tiene que hacer» pasa todo eso a la HU-003.
- **Un enlace de la conversación copiada** volvió a quedar roto por el traslado. El programa lo pasó como texto al copiar de nuevo la conversación.

`validar.py estandar`, `origen` y `analisis` no muestran incumplimientos, y los textos nuevos no tienen marcas de `00·ID8`.

Sigue abierta la propuesta de no exigir las secciones nuevas a los análisis 1 a 7.

### 178 · Usuario, 2026-10-02 11:36:09
> Pregunta: Qué sigue?

**Agente**, 2026-10-02 11:36:18
<!-- agente: fa33128b-db2d-4c8a-af28-ab3b18cccce4 -->

Para cerrar el análisis 8 faltan dos pasos:

1. **Decidir lo único abierto:** que las secciones nuevas de la plantilla («Dónde más puede pasar», las recomendaciones y la tabla de HU con su orden) se exijan solo a los análisis que se aprueben desde la versión que las trae. Los análisis 1 a 7 ya están aprobados y no se reabren (`20·M10`).
2. **Aprobarlo** con «Apruebo el análisis».

Después:
- Pasar sus puntos a las HU: reescribir la HU-007, sumar los criterios de la fase D de la HU-001, de la HU-003 y de la HU-006, y poner al día la hoja de ruta de EP-023.
- Hacer el commit de lo pendiente: la corrección del H-9 con su versión, los análisis, el pendiente 108, el recuerdo y los guiones.
- Seguir con la fase D de la HU-001, que va primera en el orden nuevo.

¿Se toma la decisión del punto 1?

### 179 · Usuario, 2026-10-02 11:43:24
> 00 id9

**Agente**, 2026-10-02 11:43:30
<!-- agente: 4f58f06f-b5f3-43e5-a926-2c45921ed6e3 -->

Falta decidir una sola cosa antes de aprobar el análisis 8: si las secciones nuevas se exigen solo a los análisis que se aprueben desde ahora, sin tocar los análisis 1 a 7. ¿Se toma?

### 180 · Usuario, 2026-10-02 11:43:48
> si

**Agente**, 2026-10-02 11:43:54
<!-- agente: d6b5c8a1-c25c-4dee-bf54-5c8462318104 -->

Queda decidido. Para escribirlo en el análisis falta «Hágalo».

### 181 · Usuario, 2026-10-02 11:44:17
> Hágalo

**Agente**, 2026-10-02 11:44:59
<!-- agente: 75284f45-bfb8-4af1-80ea-eee6a754da14 -->

Ya está escrito en el análisis 8:

- **Conclusión 16:** las secciones nuevas se exigen solo a los análisis que se aprueben desde la versión que las trae, y los análisis 1 a 7 no se reabren. Al principio la escribí citando los turnos 183 a 186 y la corregí a los correctos, del 178 al 181.
- **Punto 11 de «Lo que se tiene que hacer»:** pasa esa condición al validador, en la fase D de la HU-001.

`validar.py estandar` y `origen` no muestran incumplimientos. No queda nada abierto.

Para cerrarlo: «Apruebo el análisis».

### 182 · Usuario, 2026-10-02 11:45:35
> Apruebo el análisis

**Agente**, 2026-10-02 11:45:56
<!-- agente: b46708c0-7dae-4515-8125-b1ced755fc50 -->

El análisis 8 quedó aprobado: la marca está en el turno 182 y `validar.py analisis` no muestra incumplimientos. Se apaga al terminar esta respuesta.

Lo que sigue:
1. **Pasar sus 11 puntos** a donde van:
   - Reescribir la HU-007.
   - Los criterios nuevos de la fase D de la HU-001, de la HU-003 y de la HU-006.
   - La hoja de ruta de EP-023.
   - Las líneas de los análisis 6, 7 y 8 en el análisis principal.
2. **Hacer el commit de lo pendiente**: la corrección del H-9 con su versión, los análisis 7 y 8, el pendiente 108, el recuerdo y los guiones.

Para el paso 1: «Escriba».

> acá termina la conversación

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican `04·S9` (escribir solo dentro del proyecto), `01·C29` (todo lo del proyecto vive en el repositorio), `20·M12` (no se duplica una regla), `20·M3` (la base sirve a cualquier herramienta), `00·N1` (lo que no se deshace se pide cada vez), `04·S10` y `04·S11` (procesos ajenos y datos reales). No hace falta una regla nueva: `S9` ya rige en todas partes, y lo que falta es que un programa la haga cumplir por todos los canales (turno 142).

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| `adaptadores/claude-code/hook_antes.py` | Freno antes de escribir, enganchado solo a `Write`, `Edit`, `MultiEdit` y `NotebookEdit`; nació en EP-005, HU-023 |
| CA-02 de la [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) | El freno que compara con el plan; dice «escribir un archivo», sin nombrar los demás canales |
| `plantillas/analisis.md` y `validadores/analisis.py` | De la [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md): la plantilla no pide considerar otros casos ni las dependencias de las HU; el validador mira cuatro secciones |
| Hoja de ruta de EP-023 | Orden con razón solo en tres puestos; los demás dicen «sigue el orden de la propuesta final» |
| Enganche del análisis | La respuesta entraba un turno tarde; corregido en este análisis (H-9) |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| H-6 y H-9 | Dos veces el programa no cubrió lo que pasa en la realidad: un análisis aprobado que seguía recibiendo turnos y una respuesta que entraba tarde. Lo recoge la conclusión 7 |
| Lecciones de los análisis 6 y 7 | Se decidió sin revisar todo lo que la decisión toca. Lo recogen las conclusiones 4 y 5 |
| El orden de las HU dado por claro en el análisis 3 | Un número no dice en qué orden se construye. Lo recoge la conclusión 5 |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | Usan otras herramientas y otros agentes, algunos sin enganches; el freno tiene que funcionar también al guardar el commit y en la integración continua. Los cambios en la plantilla y el validador del análisis son MAYOR |
| Normas y leyes | Ninguna aplica |
| Herramientas | Claude Code corre a la vez los enganches de un mismo evento y deja la salida del segundo plano en su carpeta temporal |

### Dónde más puede pasar

> El análisis se hace desde todas las perspectivas: lo que pasa en un caso puede pasar en muchos otros. Este análisis es el piloto de la sección.

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Herramienta de escritura | Cualquier agente | Escribe fuera del proyecto o del plan | Capa 1 |
| Redirección, copiar, mover o borrar por consola, git | Cualquier proyecto con consola | Lo mismo, sin que nadie lo vea | Capas 1 y 2 |
| Programa que escribe por dentro | Guiones, pruebas, instaladores | No se ve al leer la orden | Capa 2 dentro del proyecto; afuera queda sin cubrir y lo declara el contrato del adaptador |
| Segundo plano | Herramientas que guardan la salida afuera | La evidencia queda fuera del repositorio | Capa 1 lo detiene |
| Instalar paquetes, cachés, configuración global, variables de entorno, registro | Cualquier sistema | Cambia la máquina, no solo el proyecto | Capa 1, con autorización de la ruta exacta (`S9`) |
| Rutas que engañan: `..`, `~`, variables, enlaces que apuntan afuera, mayúsculas | Windows, Linux, macOS | El freno cree que es adentro | Capa 1 resuelve la ruta real antes de comparar |
| Procesos que siguen después del turno, tareas programadas | Servidores de desarrollo | Actúan sin que nadie mire | Capa 1 los detiene salvo autorización (`S10`) |
| Bases de datos reales, máquinas remotas, despliegues | Proyectos con servicios | Daño que no se deshace | `S11` y `00·N1`: se pide cada vez |
| Subagentes y flujos de varios agentes | Herramientas que los permiten | Escriben sin freno | El mismo freno; si la herramienta no lo pasa, lo declara el contrato |
| Servicios externos y almacenes de la herramienta | Documentos, artefactos, memoria, planes | Lo del proyecto queda fuera de él | `00·N1` y `C29`; la memoria ya la mueve `hook_recuerdos.py` |
| Herramienta sin enganches | Otros agentes | Ninguna capa antes de actuar | Capas 3 y 4 |
| Recomendación repetida o sin origen | Cualquier proyecto que acumule análisis | Dos recomendaciones dicen distinto lo mismo, o nadie sabe de dónde salió una | El validador busca repetidas y exige el análisis de origen |
| Análisis aprobado que no suma su línea al análisis principal | Cualquier proyecto con análisis | Nadie sabe por qué cambió lo que se construye | El validador avisa |
| Respuesta del agente más larga de lo que pide `00·ID9` | Cualquier agente | El usuario tiene que pedir que la acorte, una y otra vez | Recomendación: medirla antes de entregarla |
| Respuesta que entra tarde al análisis | Cualquier herramienta que corra enganches a la vez | El análisis no tiene lo último | Resuelto: un solo programa escribe las dos cosas |

---

## Conclusiones

| # | Tema | Conclusión | Sale de |
|---|---|---|---|
| 1 | Una regla rige en todas partes | No se crea una regla por cada canal: `04·S9` ya cubre toda escritura fuera del proyecto, y lo que falta es que un programa la haga cumplir por todos | Turno 142 |
| 2 | Dónde queda el freno | En la HU-007, que ya trata del freno; no nace un pendiente aparte | Turnos 143 y 145 |
| 3 | El freno en cuatro capas | Antes de actuar, sobre toda acción y por su efecto; después de actuar, comparando el estado de git con el plan; al guardar el commit; y en la integración continua. Cada adaptador declara qué capas cubre en su herramienta y por qué no las demás | Turnos 144, 153 y 155 |
| 4 | El análisis abre todas las posibilidades | La plantilla del análisis lleva la sección «Dónde más puede pasar», con el caso, dónde se presenta, el riesgo si queda sin cubrir y lo que lo cubre; el validador no deja cerrar un análisis con un caso sin cubrir ni razón | Turnos 146, 152, 153 y 155 |
| 5 | Las HU con su dependencia y su orden | La tabla de HU de la propuesta final lleva de qué HU depende cada una, su orden de ejecución y por qué. El número identifica a la HU y no cambia; el orden sale de las dependencias. El validador revisa que ninguna vaya antes de una de la que depende y que cada puesto tenga razón. La hoja de ruta de la épica copia ese orden | Turnos 152, 153 y 155 |
| 6 | Dónde se pide lo de la plantilla | En una fase D de la HU-001, que es dueña de la plantilla y del validador del análisis | Turno 152 |
| 7 | La respuesta entraba tarde al análisis | `hook_historico.py` la pasa apenas la escribe; ya se corrigió (H-9), porque este análisis es el piloto | Turno 148 |
| 8 | El orden de EP-023 | Primero la fase D de la HU-001, porque todo análisis que venga usa la plantilla. Después la HU-003, que da la forma del hallazgo y del pendiente y resuelve las dos fallas que hoy dejan los validadores. La HU-006 no depende de ninguna y frena las lecciones que se acumulan «por escribir». La HU-004 depende de la HU-003. La HU-007 va al final: depende de la HU-003 y de la HU-004, porque el freno anota el hallazgo y vuelve al análisis | Turnos 153 y 155 |
| 9 | Las recomendaciones del análisis | Viven en un solo archivo, `plantillas/recomendaciones-del-analisis.md`, y la plantilla abre con una sección que lo enlaza y dice cuáles aplican. Hay dos niveles: las de Cimiento, que viajan con el estándar y llevan versión, y las de cada proyecto, en su archivo; la del proyecto que sirva a todos sube a Cimiento. Cada una dice qué se hace, por qué y de qué análisis sale. Antes de crear una se busca si ya existe (`20·M12`). Si se vuelve exigible, sube a regla. El validador revisa el origen, que no haya repetidas y que cada análisis aprobado diga cuáles consultó. Arranca con las que dejaron las lecciones de los análisis 1 a 8, y el recuerdo «El análisis cubre todos los casos» pasa a ser la R-1 | Turnos 156 y 157 |
| 10 | Cómo se alimentan | De las lecciones de cada análisis: su tabla suma una columna que dice si la lección complementa una recomendación, crea una nueva o no aplica. Es de la HU-006, que trata de las lecciones, y por eso la HU-006 depende de la fase D de la HU-001 | Turnos 156 y 157 |
| 11 | El análisis principal al día | Los análisis 6, 7 y 8 suman su línea a la lista de cambios del análisis principal (`13·DOC25`), y el validador avisa cuando un análisis aprobado cambia una HU y no aparece en esa lista | Turnos 158 y 159 |
| 12 | El largo de la respuesta | Medir la respuesta contra `00·ID9` antes de entregarla queda como recomendación de arranque | Turnos 159 y 161 |
| 13 | Revisar lo que se tiene que hacer | No nace nada nuevo: para eso existe «Lo que aportó cada parte». Lo que falló en el H-5 y el H-7 fue hacer esas partes por encima, sin revisarlas contra cada punto de «Lo que se tiene que hacer»; queda como lección | Turnos 159 y 160 |
| 14 | La corrección del H-9 | Cambió `validadores/instalar.py`, que viaja a los proyectos: entra con su línea en el CHANGELOG y su versión (`20·M10`) en el commit que la sube | Turnos 160 y 161 |
| 15 | Dónde vive el pendiente | Dentro de lo que lo origina va una carpeta `pendientes/`, y dentro de ella cada pendiente en su carpeta, con `pendiente.md` y sus análisis. La numeración sigue siendo una sola en todo el proyecto. Un programa arma el índice de todos, con su número, dónde viven y si su plan cerró. El validador de fases acepta `pendientes/` dentro de una épica, de una HU o de un resumen del día. Cuando el análisis decide a dónde va un pendiente que esperaba en el resumen del día, la carpeta se mueve y sus enlaces se actualizan. Si ya se sabe a quién pertenece, nace allá: el 108 va en `pendientes/` de la HU-036. Precisa la conclusión 11 del análisis 1 | Turnos 173 a 177 |
| 16 | Los análisis ya aprobados | Las secciones nuevas de la plantilla («Dónde más puede pasar», las recomendaciones y la tabla de HU con su orden) se exigen solo a los análisis que se aprueben desde la versión que las trae. Los análisis 1 a 7 no se reabren (`20·M10`) | Turnos 178 a 181 |

Siguen abiertas: ninguna.

## Propuesta final: hallazgo y pendiente

> El H-8 no cambia. El pendiente sigue en la V3. EP-023 no suma HU.

### HU que siguen, con su dependencia y su orden

| Orden | HU | Depende de | Por qué en ese orden |
|---|---|---|---|
| 1 | HU-001, fase D | Ninguna | Todo análisis que venga usa la plantilla |
| 2 | HU-003 | HU-001 | Da la forma del hallazgo y del pendiente que usan la HU-004 y la HU-007; resuelve las fallas de `fases` y de `pendientes` |
| 3 | HU-006 | HU-001, fase D | Las lecciones alimentan las recomendaciones que crea la fase D; cada análisis suma lecciones que hoy no tienen dónde quedar |
| 4 | HU-004 | HU-003 | Detener la ejecución necesita la forma del hallazgo |
| 5 | HU-007 | HU-003, HU-004 | El freno anota el hallazgo y vuelve al análisis |

## Lecciones aprendidas

| # | Lección | Tipo | Señal |
|---|---|---|---|
| 1 | El agente propuso cubrir solo el canal que falló; el usuario pidió considerar todos los casos de todos los proyectos | Falló | Por escribir |
| 2 | Listar todos los canales en una tabla mostró los huecos antes de decidir | Funcionó | Por escribir |
| 3 | Corregir en el piloto lo que falla del propio enganche evita que falle en los análisis siguientes | Funcionó | Por escribir |
| 4 | Las cuatro partes de «Lo que aportó cada parte» se hicieron por encima en los análisis 1 a 5, sin revisarlas contra cada punto de «Lo que se tiene que hacer», y por eso salieron el H-5 y el H-7 al escribir los planes | Falló | Por escribir |
| 5 | El usuario tuvo que pedir «00 id9» muchas veces en la misma sesión: el largo se medía después de entregar | Falló | Por escribir |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de la conclusión | Pasó a |
|---|---|---|---|
| 1 | Reescribir el CA-02 de la HU-007 con el freno en cuatro capas y el contrato de cada adaptador, y repartirlo en las fases que haga falta | 1, 2, 3 | EP-023, [HU-007](../HU-007-nada-se-escribe-fuera-del-plan-aprobado/HU-007-nada-se-escribe-fuera-del-plan-aprobado.md) |
| 2 | Sumar a la HU-001 el criterio de la sección «Dónde más puede pasar», en la plantilla y en el validador | 4, 6 | EP-023, [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), fase D |
| 3 | Sumar a la HU-001 el criterio de la tabla de HU con dependencia, orden de ejecución y razón, en la plantilla del análisis, la hoja de ruta de la épica y el validador | 5, 6 | EP-023, [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), fase D |
| 4 | Reescribir la hoja de ruta de EP-023 con el orden de este análisis | 8, 10 | EP-023, [épica](../epica.md) |
| 5 | Sumar a la HU-001 el criterio de las recomendaciones: el archivo con su forma y sus dos niveles, la sección que lo enlaza al inicio de la plantilla, el validador, y las recomendaciones de arranque | 9 | EP-023, [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), fase D |
| 6 | Sumar a la HU-006 el criterio de alimentar las recomendaciones desde las lecciones, con la columna nueva en su tabla | 10 | EP-023, [HU-006](../HU-006-lo-aprendido-incluye-las-lecciones/HU-006-lo-aprendido-incluye-las-lecciones.md) |
| 7 | Sumar las líneas de los análisis 6, 7 y 8 a la lista de cambios del análisis principal, y el criterio de que el validador avise cuando falte la de un análisis aprobado | 11 | EP-023, [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), fase D |
| 8 | Sumar a las recomendaciones de arranque medir la respuesta contra `00·ID9` antes de entregarla | 12 | EP-023, [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), fase D |
| 9 | Subir la corrección del H-9 con su línea en el CHANGELOG y su versión | 14 | Este análisis, en el commit que la sube |
| 10 | Sumar a la HU-003 la carpeta `pendientes/` dentro de lo que origina cada pendiente, con la numeración única, el índice que se arma solo, el validador de fases y el traslado de los pendientes de `pendientes/` y del 103 | 15 | EP-023, [HU-003](../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md) |
| 11 | Que el validador del análisis exija las secciones nuevas solo a los análisis aprobados desde la versión que las trae | 16 | EP-023, [HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md), fase D |
