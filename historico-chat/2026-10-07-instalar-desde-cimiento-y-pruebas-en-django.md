<!-- sesion: 63aeada8-3454-4d0e-89aa-ae32efe5c0fa -->
<!-- nombre: preguntado -->

# 2026-10-07 — Instalar desde cimiento y pruebas en django

## Conversación

### 1 · Usuario — 2026-10-07 12:46:38
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\base\02-flujo-de-trabajo\reglas\F30-toda-accion-trae-su-contraria.md in the IDE. This may or may not be related to the current task.</ide_opened_file>
> Pregunta: Si configuro un proyecto desde configuración de proyectos en cimiento, ya no tendría que crear la carpeta, copiar y pegar la plantilla de claude.md.plantilla sino que con darle la ruta cimiento ya hace todo el proceso de instalación?

**Agente** — 2026-10-07 12:47:44
<!-- agente: 66686466-6dde-47f1-807a-11da4f4e90e5 -->

Now the project-configuration screen: does it call the installer?

No. Hoy la pantalla de configuración de proyectos de Cimiento no instala nada: ninguna vista ni acción del administrador llama al instalador. La relación va al revés: es el instalador el que da de alta el proyecto en Cimiento ([registrar.py](proyectos/cimiento/core/proyectos/management/commands/registrar.py)).

Tampoco hace falta copiar y pegar la plantilla a mano. Eso ya lo hace el instalador:

1. Crear la carpeta del proyecto. El instalador no la crea: si la ruta no existe, se detiene, porque casi siempre es un error al escribirla ([instalar.py:1258](proyectos/cimiento/core/herramientas/instalar.py#L1258)).
2. Correr `python validadores/instalar.py «ruta» --aplicar`. Este paso:
   - crea `CLAUDE.md` a partir de `plantillas/CLAUDE.md.plantilla`, con las rutas y la versión de la máquina ([instalar.py:839](proyectos/cimiento/core/herramientas/instalar.py#L839));
   - pone los enganches;
   - registra el proyecto en Cimiento.

Para que la ruta escrita en la pantalla bastara, haría falta que la pantalla llame al instalador (y que cree la carpeta si no existe). Hoy esa función no existe.

### 2 · Usuario — 2026-10-08 12:41:10
> preguta como estamos utilizando django que sistemas prebas le podemos implementar ?

**Agente** — 2026-10-08 12:42:25
<!-- agente: 4280b3e7-8e1f-4170-9d56-01eead28b811 -->

Tomé «preguta» como «Pregunta».

Cimiento ya tiene un sistema de pruebas: el de Django (`manage.py test`, construido sobre `unittest`). Son 87 archivos `tests*.py`. Lo que falta es medir y probar las pantallas.

| Sistema | Para qué le sirve a Cimiento | Instalar |
|---|---|---|
| **coverage.py** | Muestra qué líneas del código no se ejecutan en ninguna prueba. Es la base para saber qué falta. | `pip install coverage` |
| **Cliente de pruebas de Django** (`django.test.Client`) | Prueba vistas, el administrador y las respuestas de htmx sin abrir un navegador. Hoy casi no se usa. | Viene con Django |
| **Playwright** con `StaticLiveServerTestCase` | Abre un navegador real: botones, htmx, list.js, gráficos de ApexCharts. | `pip install playwright` |
| **pytest + pytest-django** | Corre las mismas pruebas sin reescribirlas, con mejores reportes y pruebas en paralelo (`pytest-xdist`). | `pip install pytest pytest-django` |
| **factory_boy** | Arma datos de prueba (proyectos, reglas, versiones) sin repetir código. | `pip install factory-boy` |
| **Hypothesis** | Genera miles de entradas al azar. Sirve para lo que transforma texto: rellenar la plantilla, sellos, sincronizar secciones. | `pip install hypothesis` |
| **mutmut** | Mete errores a propósito en el código y revisa si alguna prueba los detecta. Mide si las pruebas sirven, no solo si existen. | `pip install mutmut` |

Mi recomendación, en orden: primero coverage.py y el cliente de Django, que cuestan poco y muestran los huecos. Después Playwright para las pantallas. Si alguno entra, va a `requirements/` como dependencia de desarrollo (`10·DEP2`).

Propongo guardar esta sesión como `2026-10-08-instalar-desde-cimiento-y-pruebas-en-django.md`: «si la pantalla de Cimiento instala proyectos, y qué sistemas de pruebas sirven en Django». ¿Le sirve ese nombre?

### 3 · Usuario — 2026-10-08 12:47:58
> explique aplicando 00 id7 y 00 id9

**Agente** — 2026-10-08 12:48:08
<!-- agente: 3d29725d-aee8-4f73-98ab-83ff76324491 -->

Una prueba es un programa pequeño que revisa si otro programa hace lo que debe. Cimiento ya tiene 87 archivos de pruebas. Lo que les falta es saber qué partes no se revisan y probar las pantallas.

Las herramientas que sirven, de la más útil a la menos:

1. **coverage.py**: dice qué partes del código ninguna prueba revisa. Muestra dónde faltan pruebas.
2. **Cliente de pruebas de Django**: hace como si alguien entrara a una página de Cimiento y revisa lo que esta contesta, sin abrir un navegador. Ya viene con Django.
3. **Playwright**: abre un navegador de verdad y da clic en los botones como lo haría una persona.
4. **pytest**: corre las mismas pruebas que ya existen y muestra los resultados más claros y más rápido.
5. **factory_boy**: arma los datos falsos que necesitan las pruebas, como un proyecto o una regla, para no escribirlos a mano cada vez.
6. **Hypothesis**: le da al programa miles de entradas al azar para encontrar la que lo hace fallar.
7. **mutmut**: daña el código a propósito y mira si alguna prueba se da cuenta. Así se sabe si las pruebas sirven.

Recomiendo empezar por las dos primeras, que cuestan poco, y seguir con Playwright.

### 4 · Usuario — 2026-10-08 12:49:16
> pregunta a qué se refiere con que cuestan poco?

**Agente** — 2026-10-08 12:49:27
<!-- agente: 9f3a527b-a8ee-4861-9946-8775f2634c69 -->

«Cuestan poco» quiere decir poco trabajo, no poco dinero: las siete herramientas son gratis.

- **coverage.py** se instala con un solo comando y corre las pruebas que ya existen. No hay que escribir nada nuevo para ver el resultado.
- **El cliente de Django** ya viene con Django, así que no se instala nada. Las pruebas se escriben igual que las que Cimiento ya tiene.
- **Playwright** pide más trabajo. Hay que descargar navegadores, que pesan varios cientos de megas, y sus pruebas son más lentas. Además se dañan cuando cambia el diseño de una pantalla, aunque Cimiento siga funcionando bien.

### 5 · Usuario — 2026-10-08 13:03:13
> apruebo

**Agente** — 2026-10-08 13:03:22
<!-- agente: d83d82d7-4f6b-4f8d-bd2d-cc8ad1b72d30 -->

Hay dos propuestas abiertas. ¿Cuál aprueba?

1. **El nombre de la sesión**: `2026-10-08-instalar-desde-cimiento-y-pruebas-en-django.md`. Si es esta, la renombro de una vez.
2. **Empezar con coverage.py y el cliente de pruebas de Django en Cimiento**. Si es esta, el primer paso es un análisis, como pide la cadena de `02·F0` (análisis → épica → HU → especificación → plan → código). No se instala nada antes de ese análisis.

### 6 · Usuario — 2026-10-08 13:06:53
> Respondo
> 1. apruebo
> 2. explique

**Agente** — 2026-10-08 13:07:34
<!-- agente: 7333c978-b3fb-4a0e-a078-8293c6a4b9f9 -->

Renombro la sesión.

La sesión empezó el 7, así que el archivo es el del 7.

**1.** La sesión quedó guardada como `historico-chat/2026-10-07-instalar-desde-cimiento-y-pruebas-en-django.md`, y el índice ya tiene su línea. Lleva la fecha del 7 porque la sesión empezó ese día. Para que la pestaña de Claude Code tenga el mismo nombre, toca pegar este comando, que solo usted puede escribir:

```
/rename instalar-desde-cimiento-y-pruebas-en-django
```

**2.** El estándar no deja instalar una herramienta y empezar a usarla de una vez. Antes hay que poner por escrito qué se busca, para que el cambio quede justificado y se pueda revisar. Aplicado a coverage.py y al cliente de pruebas de Django, los pasos son estos:

1. **Análisis**: revisar qué prueban hoy los 87 archivos, qué pantallas no tienen pruebas y qué se gana con cada herramienta.
2. **Épica**: el objetivo grande, por ejemplo «Cimiento sabe qué parte de su código no está probada y prueba sus pantallas».
3. **Historias de usuario**: las piezas de ese objetivo. Una para medir con coverage.py y otra para probar las pantallas con el cliente de Django.
4. **Especificación**: qué debe cumplir cada pieza para darla por terminada.
5. **Plan**: los pasos de trabajo y sus pruebas.
6. **Código**: instalar, configurar y escribir las pruebas.

Usted aprueba cada paso antes de seguir con el siguiente. Si aprueba el análisis, los demás pasos se hacen sin volver a pedirle permiso.

### 7 · Usuario — 2026-10-08 13:16:25
> apruebo

**Agente** — 2026-10-08 13:19:15
<!-- agente: 03c80c7f-00d2-468c-9ded-6c9deaee8da0 -->

Aprobó arrancar la cadena, así que empiezo por el análisis. Primero reviso cómo se crea uno en este repositorio.

El proceso es: primero el hallazgo en el resumen de la sesión, después el pendiente y dentro de él el análisis. Busco la herramienta que los arma (el andamio) y un ejemplo reciente.

Escribo el hallazgo en el resumen de la sesión y armo el pendiente con el andamio.

Antes de escribir el problema, verifico cuánto se usa hoy el cliente de pruebas de Django.

Encontré un error mío: dije que el cliente de pruebas de Django «casi no se usa», pero ya lo usan 27 de los 87 archivos de pruebas. Lo corrijo en el pendiente.

Quedó listo lo que va antes del análisis:

- **Hallazgo H-1**, anotado en el [resumen de la sesión](historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md).
- **Pendiente 141**, armado con el andamio: [Cimiento no mide qué código queda sin probar ni prueba sus pantallas en un navegador](historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md).
- **El índice de resúmenes** ya incluye el día 2026-10-08. El control de enlaces lo exigió porque el pendiente quedó en esa carpeta.

Corrijo algo que dije antes: el cliente de pruebas de Django sí se usa, en 27 de los 87 archivos de pruebas. Lo que falta de verdad es medir qué código no prueba ninguna prueba (coverage.py) y probar en un navegador real (Playwright). El pendiente quedó escrito así.

El análisis no lo puedo abrir yo: se abre cuando usted escribe esto en el chat, y desde ese momento la conversación pasa sola al análisis:

```
Analicemos: el pendiente 141
```

Falta, en orden:
1. Hacer el análisis.
2. Aprobarlo.
3. Épica, HU, especificación, plan y código.
4. Su aprobación para el commit.

### 8 · Usuario — 2026-10-08 13:20:07
> Analicemos: el pendiente 141

**Agente** — 2026-10-08 13:24:58
<!-- agente: 1cd0fa55-f567-40eb-a16b-03dc45d6a08f -->

El análisis quedó abierto. Antes de escribir, reúno lo que piden las recomendaciones R-1 y R-2: qué dicen las reglas de pruebas, qué existe y quién hereda.

Estoy llenando las partes del análisis que salen de revisar el repositorio. Las decisiones quedan para después, en el chat.

Ahora las recomendaciones, las dos copias y lo que aporta cada parte.

El análisis 1 del pendiente 141 está abierto y ya tiene lo que salió de revisar el repositorio: [analisis-1.md](historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md). Lo que sigue depende de tres decisiones, cada una con mi recomendación.

Algo sale del estándar mismo: la regla `20·M3` prohíbe nombrar coverage.py o Playwright en `base/`, porque solo sirven para un tipo de proyecto. Por eso solo pueden ir en Cimiento o en lo que cada proyecto declara en su archivo `.agente/stack.md`.

**1. ¿Hasta dónde llega el cambio?**
- a) Solo Cimiento.
- b) Cimiento, y además la plantilla `stack.md` gana una línea que pregunte cómo mide cada proyecto la cobertura y si prueba en navegador. Así cada proyecto, sea de Django, Laravel o Angular, declara su propia herramienta.

Recomiendo **b**: sirve a todos los proyectos sin romper `20·M3`.

**2. ¿Playwright entra ahora o después?**
- a) Ahora, en la misma épica, como una HU que va después de la de coverage.py.
- b) En otro análisis, cuando la cobertura muestre qué pantallas lo necesitan.

Recomiendo **a**: ya está aprobado seguir con Playwright, y ponerlo después de coverage.py deja ese orden escrito.

**3. ¿Dónde se ve el reporte de cobertura?**
- a) En la consola, al correr las pruebas.
- b) También en una pantalla de Cimiento.

Recomiendo **a** por ahora. La pantalla puede pedirse más adelante si hace falta.

Hay algo que no pregunto porque ya lo decide la regla `08·T6`: no se exige un porcentaje mínimo. La cobertura sirve para encontrar huecos, no para cumplir un número.

### 9 · Usuario — 2026-10-08 13:28:14
> Respondo: 
> 1. no entiendo la pregunta
> 2. qué recomienda
> 3. no entiendo la pregunta

**Agente** — 2026-10-08 13:28:28
<!-- agente: faf30234-c293-4113-9c37-6d0d5e2fa8a3 -->

**1. ¿Solo Cimiento o todos los proyectos?**

Instalar coverage.py en Cimiento le dice a Cimiento qué código suyo no tiene pruebas. Pero shopnest-mesa, AgroSystem y los otros proyectos seguirían sin saberlo del suyo.

- a) Arreglarlo solo en Cimiento.
- b) Arreglarlo en Cimiento y, además, que cada proyecto nuevo tenga que decir qué herramienta usa para eso. Shopnest-mesa, que es Django, diría coverage.py. AgroSystem, que es Laravel, diría la suya.

Recomiendo **b**.

**2. Playwright**

Recomiendo meterlo en este mismo trabajo, pero de último: primero coverage.py y después Playwright. Así no se pierde y queda en orden.

**3. ¿Dónde se mira el resultado?**

coverage.py entrega una lista como esta:

```
core/proyectos/registro.py     80% probado
core/herramientas/andamio.py   45% probado
```

- a) La lista sale en la ventana negra donde se corren las pruebas.
- b) La lista sale también en una página de Cimiento, como «Gasto».

Recomiendo **a**: es más sencilla, y la página se puede pedir después.

### 10 · Usuario — 2026-10-08 13:30:31
> Respondo:
> 1. eso se puede detectar desde cimiento sin importar el stack
> 2. aprobado
> 3. b

**Agente** — 2026-10-08 13:32:03
<!-- agente: 28d72642-951f-4789-88c8-8a1d61e8a344 -->

Antes de anotar el acuerdo 1, busco si Cimiento ya sabe reconocer el stack de un proyecto.

Cimiento ya reconoce el stack por sus archivos: [dependencias.py](proyectos/cimiento/core/validadores/dependencias.py#L17) busca `composer.json`, `package.json` y otros. Anoto los tres acuerdos.

Quedan tres preguntas abiertas.

**4. ¿Con qué mide Cimiento los proyectos que no son Django?**

Cada lenguaje tiene su propia herramienta:

| Stack | Proyecto | Herramienta |
|---|---|---|
| Python o Django | Cimiento, shopnest-mesa, RNI back | coverage.py |
| Laravel (PHP) | AgroSystem | PHPUnit con PCOV, una extensión de PHP que hay que instalar |
| Angular | RNI front | `ng test --code-coverage`, que ya viene incluida |

Recomiendo empezar con esas tres, que son las de los proyectos que ya están registrados. Si llega un stack que no está en la lista, la página lo muestra como «sin medición» en vez de fallar.

**5. ¿Qué proyectos muestra la página?**

- a) Solo Cimiento.
- b) Todos los proyectos registrados, una fila por proyecto, como en «Gasto».

Recomiendo **b**, porque ya está acordado que la medición llega a todos.

**6. ¿Playwright llega a todos los proyectos?**

Playwright prueba páginas web sin importar en qué lenguaje están hechas. Pero las pruebas de cada pantalla las tiene que escribir cada proyecto, porque Cimiento no conoce esas pantallas.

Recomiendo que Cimiento deje Playwright instalado y sepa correr las pruebas de cualquier proyecto que las tenga. Escribir esas pruebas sería trabajo de cada proyecto.

### 11 · Usuario — 2026-10-08 13:39:12
> 4. apruebo
> 5. todos los proyectos la idea es que cimiento los administre todos por eso es la línea base
> 6. apruebo

**Agente** — 2026-10-08 13:39:47
<!-- agente: 4c8320a5-2c22-403d-9bdf-770f6f133d3b -->

Anoto los acuerdos 4 a 6.

Queda una pregunta antes de armar la propuesta final.

**7. ¿Cuándo se mide?**

Medir la cobertura obliga a correr todas las pruebas del proyecto, y eso puede tardar varios minutos.

- a) Cuando alguien da clic en un botón «Medir» al lado de cada proyecto en la página. El mismo botón sirve para correr las pruebas de Playwright.
- b) Sola, cada vez que se corren las pruebas.

Recomiendo **a**. Con **b**, cada corrida de pruebas se vuelve más lenta aunque nadie vaya a mirar la cobertura en ese momento.

### 12 · Usuario — 2026-10-08 13:42:25
> Respondo:
> cimiento debe obligar a cada proyecto tener una parte a que mida eso y se lo avise así como le avisa la instalación

**Agente** — 2026-10-08 13:42:48
<!-- agente: 7e45ba80-c7c3-448b-a77c-7beabef7c995 -->

Reviso cómo avisa hoy Cimiento lo de la instalación, para entender bien la respuesta.

Entiendo la respuesta así. Al abrir una sesión, Cimiento ya revisa si el proyecto está instalado y avisa, por ejemplo: «falta el enganche pre-commit — correr instalar.py». Con la medición pasaría lo mismo: el instalador le pone a cada proyecto la parte que mide la cobertura, y esa parte es obligatoria.

Lo que no tengo claro es qué debe decir el aviso al abrir la sesión:

- a) Solo si falta la parte que mide: «este proyecto no mide su cobertura — correr instalar.py».
- b) También el resultado de la última medición: «hay 12 archivos sin probar», o «la última medición es de hace 20 días».

Recomiendo **a y b juntas**. La a es igual a la de instalación. La b hace que el aviso sirva para algo más que confirmar que la parte está instalada.

Sigue sin responder la 7: si la medición arranca con un botón o sola cada vez que se corren las pruebas. Con la b, recomiendo el botón y que el aviso diga cuándo se midió por última vez.

### 13 · Usuario — 2026-10-08 13:47:14
> Respondo: Desde la configuración de cada proyecto simiento sabe el estado y eso es lo que debe hacer que se cumpla.  Qué propone ahí

**Agente** — 2026-10-08 13:48:14
<!-- agente: 65818992-bb2b-46db-a028-74a9bfc613d2 -->

Antes de proponer, reviso qué guarda hoy la configuración de cada proyecto en Cimiento.

Hoy la configuración de cada proyecto en Cimiento ya tiene dos piezas que sirven para esto:

- **Ajustes**, en tres capas: un valor común para todos los proyectos que cada uno puede cambiar para sí.
- **Nivel de cada regla**: *Frena*, *Avisa* o *Apagada*.

Propongo usar esas dos piezas en lugar de crear una nueva:

1. **Dos ajustes nuevos** en la configuración:
   - «Medir cobertura»: con qué nivel se exige (*Frena*, *Avisa* o *Apagada*). Por defecto, *Avisa*.
   - «Días máximos sin medir»: por defecto, 7.
2. **El estado de cada proyecto queda guardado en la base de Cimiento**: si tiene instalada la parte que mide, cuándo se midió por última vez, el resultado archivo por archivo y si pasaron las pruebas de navegador.
3. **Cimiento compara el estado con los ajustes** al abrir la sesión, igual que con la instalación:
   - Si falta la parte que mide: «este proyecto no mide su cobertura — correr instalar.py».
   - Si la última medición pasó del máximo de días: «la última medición es de hace 12 días — medir».
   - Con *Avisa*, solo muestra el aviso. Con *Frena*, no deja guardar en git hasta que se mida.
4. **La medición arranca con el botón «Medir»** en la página, o con una orden de consola que hace lo mismo. Esto responde la pregunta 7.

¿Así le sirve, o cambia algo?

### 14 · Usuario — 2026-10-08 13:54:53
> respondo: humanice lo que propone y cuando se apliquen esos cambios debe ser humanizado para eso está la regla 00 id7

**Agente** — 2026-10-08 13:55:39
<!-- agente: 95ccf6d2-1470-4d59-ba9e-8b7efb12dd21 -->

Releo la lista de marcas de `00·ID8`, porque el control encontró dos en mi respuesta anterior.

Quedó anotado como acuerdo 8: todo lo que salga de este análisis (avisos, página y botones) se escribe para quien no sabe del tema. La propuesta, contada de forma sencilla:

Cimiento ya sabe muchas cosas de cada proyecto, como su nombre, dónde está guardado y qué tan estricta es cada regla. Ahora va a saber dos cosas más: si el proyecto puede revisar qué partes de su programa no tienen pruebas, y cuándo lo revisó por última vez.

En la página de configuración de cada proyecto aparecen dos opciones nuevas:

- Qué tan estricto ser con esa revisión: solo avisar, no dejar guardar los cambios hasta que se haga, o no hacer nada. Si nadie la cambia, queda en «solo avisar».
- Cada cuántos días hay que revisar. Si nadie lo cambia, cada 7 días.

Cada vez que alguien abre una sesión en un proyecto, Cimiento mira esas dos opciones y avisa lo que falte, con mensajes como estos:

- «Este proyecto todavía no puede revisar qué partes no tienen pruebas. Para arreglarlo, hay que volver a instalar Cimiento en él.»
- «La última revisión fue hace 12 días. Toca hacer otra con el botón Revisar.»

La revisión arranca cuando alguien da clic en «Revisar», en la página del proyecto. Al terminar, la página muestra qué partes quedaron sin pruebas y si las pantallas funcionaron bien en el navegador.

¿Se aprueba así, o hay algo que cambiar?

### 15 · Usuario — 2026-10-08 14:29:15
> respondo cada proyecto que lo implente debe saber suconfiguración de cimiento he irla complementando

**Agente** — 2026-10-08 14:29:44
<!-- agente: 37112326-37a8-4116-8ca0-102d49612459 -->

Reviso qué recibe hoy un proyecto de su configuración en Cimiento.

Hoy cada proyecto ya tiene una copia de su configuración: Cimiento la escribe sola en `.agente/configuracion.md` cada vez que algo cambia ([copia.py](proyectos/cimiento/core/proyectos/copia.py)). Esa copia dice qué ajustes tiene el proyecto y qué reglas están suspendidas. No dice qué tan estricta es cada regla, ni nada sobre las pruebas.

Su frase la entiendo de dos maneras, y necesito saber cuál es:

- a) **El proyecto lee su configuración.** Esa copia suma la parte de las pruebas: qué tan estricto ser, cada cuántos días revisar, cuándo se revisó por última vez y qué salió. Así el proyecto sabe lo que Cimiento le exige, sin tener que abrir la página.
- b) **La configuración crece con cada cosa nueva.** Cada vez que Cimiento gana una función, como esta de las pruebas, la opción aparece sola en la configuración de todos los proyectos, con su valor por defecto, y cada uno la va ajustando.

Recomiendo **a y b juntas**. La b ya existe para los ajustes: uno nuevo aparece en todos los proyectos con el valor común. Lo que falta es la a: que la copia también lleve la parte de las pruebas.

### 16 · Usuario — 2026-10-08 14:31:51
> respondo: hoy cada proyecto la tiene pero lo se busca es que todo eso lo administre Cimiento y cada proyecto consulta su configuración para funcionar

**Agente** — 2026-10-08 14:32:39
<!-- agente: 0d9717ae-a820-487c-857c-49f5ba2dcc37 -->

Reviso si hoy los proyectos leen la configuración de la base de Cimiento o de la copia.

Quedó anotado como acuerdo 9: Cimiento guarda en su base toda la configuración de cada proyecto, y cada proyecto la consulta ahí cuando la necesita.

Parte de esto ya funciona así. El freno le pregunta a la base de Cimiento, en cada acción, qué tan estricta es cada regla en ese proyecto ([niveles.py](proyectos/cimiento/core/enganches/niveles.py)). En cambio, la copia `.agente/configuracion.md` se sigue escribiendo, pero ningún programa la lee.

La propuesta queda así:

- Las dos opciones nuevas (qué tan estricto ser y cada cuántos días revisar) y el resultado de cada revisión se guardan en la base de Cimiento.
- Al abrir una sesión, el proyecto le pregunta a la base cómo va su revisión y muestra el aviso si hace falta.
- La revisión se hace con el botón «Revisar».

Para cerrar este punto necesito dos respuestas:

1. ¿Se aprueba la propuesta así?
2. Sobre la copia `.agente/configuracion.md`, que nadie lee y que va en contra del acuerdo 9, ¿qué se hace? Recomiendo quitarla en esta misma épica: si se deja, alguien puede creer que es la configuración de verdad y confiar en datos viejos.

### 17 · Usuario — 2026-10-08 14:39:27
> respondo: humanice la respuesta y las preguntas

**Agente** — 2026-10-08 14:39:40
<!-- agente: 240fdb5a-f98e-41b8-8375-b8872b5db6e7 -->

Lo dejo en palabras sencillas.

Cimiento va a ser el único lugar donde se guarda cómo debe trabajar cada proyecto. Ningún proyecto tendrá su propia libreta de apuntes: cuando necesite saber algo, le pregunta a Cimiento.

Con las pruebas funcionaría así:

- En Cimiento, cada proyecto tiene dos opciones: qué tan estricto ser con la revisión de pruebas y cada cuántos días hay que hacerla.
- Cuando alguien empieza a trabajar en un proyecto, el proyecto le pregunta a Cimiento cómo va su revisión. Si hace falta, avisa, por ejemplo: «La última revisión fue hace 12 días. Toca hacer otra.»
- La revisión se hace con el botón «Revisar», en la página del proyecto dentro de Cimiento.

Hay un detalle. Hoy cada proyecto guarda una copia de sus opciones en una carpeta propia, pero ningún programa la usa. Si se deja, alguien la puede abrir, creer que está al día y equivocarse.

Necesito dos respuestas:

1. ¿Está de acuerdo con que funcione así?
2. ¿Se borra esa copia que nadie usa? Recomiendo borrarla.

### 18 · Usuario — 2026-10-08 14:51:55
> 1. qué funcione cómo?
> 2. si

**Agente** — 2026-10-08 14:52:05
<!-- agente: 45a0a606-e264-485f-b161-709e206e9318 -->

Le falta la palabra que dice qué espera (por ejemplo «Respondo»). Quedo atento a que la agregue para seguir.

### 19 · Usuario — 2026-10-08 14:53:21
> Respondo:
> 1. qué funcione cómo?
> 2. si

**Agente** — 2026-10-08 14:53:52
<!-- agente: 27f8cc17-0e54-437f-bcd0-e66e77980bc3 -->

Anotado: la copia que nadie usa se borra.

La pregunta 1 era confusa; la hago de nuevo. Se trata de la revisión de pruebas, es decir, de saber qué partes de cada programa no tienen quién las revise. La propuesta tiene tres pasos:

1. En la página de cada proyecto, dentro de Cimiento, se eligen dos cosas: qué tan estricto ser y cada cuántos días revisar. Si nadie las cambia, queda en «solo avisar» y «cada 7 días».
2. Cuando alguien empieza a trabajar en un proyecto, Cimiento mira esas dos opciones. Si la revisión está vencida, avisa: «La última revisión fue hace 12 días. Toca hacer otra.»
3. La revisión se hace con el botón «Revisar» en esa misma página. Al terminar, muestra qué partes quedaron sin pruebas.

¿Aprueba esos tres pasos, o cambia alguno?

### 20 · Usuario — 2026-10-08 14:57:11
> apruebo

**Agente** — 2026-10-08 15:05:17
<!-- agente: 187bc848-d1a1-41c3-91ac-b09edf52f55b -->

Anoto el acuerdo 11. Con eso no queda ninguna pregunta abierta, así que paso a escribir la propuesta final.

Tomo como modelo el análisis aprobado más reciente.

Escribo las dos lecciones en la base de señales.

Ahora escribo la propuesta final, las lecciones, lo que se tiene que hacer y el aporte al análisis principal.

Actualizo el tipo de versión, que antes dependía del alcance y ya quedó decidido. Después paso el hallazgo y el pendiente a su V2 en los archivos originales (fila 1).

Borro las notas de la plantilla que ya se cumplieron, como pide la misma plantilla.

El análisis 1 del pendiente 141 está completo y listo para aprobar: [analisis-1.md](historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md).

El trabajo queda en una épica nueva, la EP-029, con cinco partes. Van en este orden porque cada una necesita la anterior:

1. La página de cada proyecto gana dos opciones: qué tan estricto ser con la revisión de pruebas y cada cuántos días hacerla.
2. El botón «Revisar» muestra qué partes de cada proyecto no tienen pruebas, usando la herramienta que corresponde a su lenguaje. Una sola página muestra todos los proyectos.
3. Cuando alguien empieza a trabajar, Cimiento avisa si la revisión falta o está vencida. El instalador pone en cada proyecto la parte que revisa, y el desinstalador la quita.
4. Cada proyecto le pregunta su configuración a Cimiento, y se borra la copia que nadie usa.
5. Cimiento corre las pruebas en navegador de cualquier proyecto que las tenga. Va de última, como se acordó.

Todo lo que se vea en pantalla se escribe para quien no sabe del tema.

El hallazgo y el pendiente ya quedaron actualizados con lo que se decidió. Las dos lecciones del análisis quedaron guardadas (S-350 y S-351). La principal: las preguntas deben ir sin palabras técnicas desde la primera vez.

Hay que tener en cuenta que esto obliga a volver a instalar Cimiento en todos los proyectos. Por eso el cambio de versión es mayor.

El freno detuvo dos órdenes mientras escribía el análisis. La primera fue culpa mía: quise usar un archivo de apoyo fuera del repositorio. La segunda es un defecto del freno que ya estaba anotado: tomó una palabra suelta, «Antes», como si fuera un archivo. No se perdió nada, porque terminé con el editor.

Para aprobar, escriba en el chat:

```
Apruebo el análisis
```

Falta, en orden:
1. Aprobar el análisis.
2. Construir las cinco HU, cada una con su especificación, su plan y sus pruebas.
3. Su aprobación para el commit.

### 21 · Usuario — 2026-10-08 15:08:21
> Apruebo el análisis

**Agente** — 2026-10-08 15:09:59
<!-- agente: e0d7d256-c555-467b-9072-efc3dcc61a09 -->

La aprobación no pasó: el acuerdo 11 cita el turno 22, y ese turno no está en la conversación del análisis. Reviso cómo quedaron numerados los turnos.

Numeré mal los turnos: los conté a ojo y no los saqué de la conversación. Leo qué dijo el usuario en cada uno para corregir las citas.

Hay que corregir cuatro citas: el acuerdo 8 es del turno 14, el 9 de los turnos 15 y 16, el 10 del turno 19 y el 11 del turno 20.

El análisis todavía no queda aprobado. El programa que aprueba lo rechazó porque cuatro acuerdos citaban turnos de la conversación equivocados: los numeré contando a ojo en lugar de copiarlos del análisis.

Ya los corregí:

| Acuerdo | Turno |
|---|---|
| 8 | 14 |
| 9 | 15 y 16 |
| 10 | 19 |
| 11 | 20 |

También agregué esto como lección 3 (S-352).

Para aprobarlo, escriba otra vez:

```
Apruebo el análisis
```

### 22 · Usuario — 2026-10-08 15:10:32
> liste los acuerdos que se van aprobar

**Agente** — 2026-10-08 15:10:45
<!-- agente: da79cefb-7fdc-4f45-8d22-a1c06433ea66 -->

Son 11 acuerdos:

1. Cimiento revisa qué partes del programa no tienen pruebas en todos los proyectos, no solo en él mismo. Reconoce solo en qué lenguaje está hecho cada proyecto.
2. Las pruebas en navegador (Playwright) entran en este mismo trabajo, de últimas.
3. El resultado de la revisión se ve también en una página de Cimiento, no solo en la consola.
4. Cada lenguaje se revisa con su herramienta: coverage.py para Python y Django, PHPUnit para Laravel y la que trae Angular. Si un proyecto está en otro lenguaje, la página dice «sin medición» y no falla.
5. La página muestra todos los proyectos, uno por fila.
6. Cimiento deja instalado Playwright y corre las pruebas en navegador del proyecto que las tenga. Escribir esas pruebas le toca a cada proyecto.
7. Revisar es obligatorio para todo proyecto. Cimiento avisa cuando falta, igual que avisa cuando falta la instalación.
8. Avisos, página y botones se escriben para que los entienda quien no sabe del tema.
9. Cimiento guarda la configuración de todos los proyectos, y cada proyecto la consulta ahí.
10. Se borra la copia de la configuración que cada proyecto tiene en su carpeta y que nadie usa.
11. En la página de cada proyecto se elige qué tan estricto ser (solo avisar, no dejar guardar los cambios hasta revisar, o nada) y cada cuántos días revisar. Si nadie lo cambia, queda en «solo avisar» y cada 7 días. Cuando alguien empieza a trabajar y la revisión está vencida, Cimiento avisa. La revisión se hace con el botón «Revisar».

Si está de acuerdo, escriba «Apruebo el análisis».

### 23 · Usuario — 2026-10-08 15:12:00
> Apruebo el análisis

**Agente** — 2026-10-08 15:28:21
<!-- agente: 112e1652-4be4-4c04-9def-02cb42bf0a2a -->

El análisis quedó aprobado. Según el acuerdo de trabajo, aprobar es la orden de dejarlo funcionando, así que arranco con la épica EP-029. Primero reviso cómo se crea una épica y cómo quedó la más reciente.

Sigo revisando el código que va a cambiar: ahora cómo los enganches leen la configuración desde la base y qué muestran al abrir la sesión.

Escribo la épica EP-029 siguiendo el modelo de la EP-028.

Creo las cinco HU con el andamio.

Agrego la EP-029 al índice de épicas.

Ahora diseño la HU-001. Primero reviso cómo aparecen los ajustes en el formulario del proyecto y si su texto de ayuda sale solo del catálogo.

Escribo la HU-001.

Abro la fase A de la HU-001 con el andamio.

Lleno los documentos de la fase A: el plan de trabajo con los archivos exactos que el freno va a dejar tocar, el plan de pruebas y el estado.

Reviso cómo decide el freno que una fase está en curso y que su plan está aprobado, para dejar el estado de la fase como lo espera.

Lleno el estado de la fase y paso al código.

Ahora el código. Primero los dos ajustes.

Ahora la app `core/pruebas/` con sus modelos.

El cambio parecido anterior (la `0006`) sí estaba declarado en su plan. Esta vez se me pasó a mí. Lo anoto en el resumen de la sesión, en el plan y en el estado de la fase.

Me detuve por un hallazgo.

**Qué pasó.** Las dos opciones nuevas de la configuración obligan a Django a crear un archivo de base de datos que el plan de la HU-001 no nombra: `core/proyectos/migrations/0007_…py`. Las reglas no dejan escribir lo que el plan no nombra. En un caso igual de la EP-028 ese archivo sí estaba en el plan; esta vez se me pasó al escribirlo. Lo anoté como H-2 en el resumen de la sesión, y en el plan y el estado de la fase.

**Qué quedó hecho:**
- La épica EP-029 y sus cinco HU, con el índice al día.
- La HU-001 con su fase A abierta y sus planes.
- Las dos opciones nuevas («qué tan estricto ser» y «cada cuántos días») con su ayuda en palabras sencillas.
- La app nueva donde se guarda cada revisión, todavía sin sus archivos de base de datos.

No se ha corrido ninguna prueba.

**Qué propongo.** Abrir el análisis 2 del pendiente 141, solo para este caso: agregar ese archivo al plan de la HU-001. En el mismo análisis revisaría si a las otras cuatro HU les puede pasar lo mismo, para que no vuelva a detenerse por lo mismo.

Para abrirlo, escriba:

```
Analicemos: el pendiente 141
```

Falta, en orden:
1. El análisis 2 y su aprobación.
2. Terminar la HU-001 y correr sus pruebas.
3. Construir las HU-002 a HU-005.
4. Su aprobación para el commit.

### 24 · Usuario — 2026-10-08 15:28:46
> Analicemos: el pendiente 141

**Agente** — 2026-10-08 15:30:39
<!-- agente: 74fb8c3d-d83d-494d-b086-a857a1760dfa -->

El análisis 2 quedó abierto y ya tiene lo que encontré: [analisis-2.md](historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-2.md).

Una explicación corta del problema. Cuando cambia lo que se guarda en la base de datos, Django pide un archivo nuevo que describe ese cambio, llamado migración. El plan de la HU-001 nombró la migración de la parte nueva, pero no la de las opciones de configuración, que también cambiaron.

Necesito dos respuestas:

1. **¿Se agrega al plan de la HU-001 el archivo que falta?** Así la fase puede seguir donde quedó. Recomiendo que sí.
2. **¿Cómo evitar que vuelva a pasar?** Antes de escribir el plan de una fase que cambie la base de datos, preguntarle a Django qué archivos va a pedir y ponerlos todos en el plan. Esto serviría para las HU-002 a HU-005 y para cualquier fase futura de cualquier proyecto. Recomiendo que sí, y que quede como una recomendación nueva para todos los análisis.

### 25 · Usuario — 2026-10-08 20:07:44
> <ide_opened_file>The user opened the file c:\Ing. Jose\ia\agente\proyectos\cimiento\core\__init__.py in the IDE. This may or may not be related to the current task.</ide_opened_file>
> explique: aplicando 00 id7 y 00 id9

**Agente** — 2026-10-08 20:07:58
<!-- agente: 532206dc-55ed-4011-81f7-037da97f1f42 -->

Lo explico con un ejemplo de la casa.

Cimiento guarda sus datos en una base de datos, que funciona como un archivador con cajones. Cada vez que cambia la forma de un cajón, hay que dejar una nota que diga «a este cajón se le agregaron dos divisiones». Django, el programa sobre el que está hecho Cimiento, exige esa nota. Sin ella, el archivador y lo que el programa cree que tiene dejan de coincidir.

Antes de trabajar, se escribe un plan con la lista de archivos que se van a tocar, y Cimiento no deja tocar ninguno que no esté en esa lista. Al agregar las dos opciones nuevas (qué tan estricto ser y cada cuántos días revisar), cambió un cajón, y su nota no estaba en la lista. Por eso el trabajo se detuvo.

**Pregunta 1.** ¿Se agrega esa nota a la lista del plan? Así el trabajo sigue donde quedó. Recomiendo que sí.

**Pregunta 2.** ¿Cómo evitar que se repita? Antes de escribir un plan, se le pregunta a Django qué notas va a pedir y se ponen todas en la lista desde el principio. Recomiendo hacerlo así siempre, en este proyecto y en los demás.

### 26 · Usuario — 2026-10-08 20:10:35
> apruebo

**Agente** — 2026-10-08 20:15:33
<!-- agente: 161e8acf-2055-49e1-be90-824db4be0a6b -->

Anoto los dos acuerdos. Primero tomo el número de turno de la conversación del análisis, sin contarlo a ojo.

Hago ya lo que el análisis manda «de una»: el pendiente pasa a su V3, el hallazgo H-2 a su V2, y se agrega la recomendación R-19.

El análisis 2 está completo y listo para aprobar: [analisis-2.md](historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-2.md).

Queda así:
- La HU-001 suma a su plan el archivo que faltaba y sigue donde quedó.
- La recomendación nueva, la R-19, ya está escrita: antes de hacer un plan que cambie la base de datos, se le pregunta al programa qué archivos va a pedir.
- El pendiente y el hallazgo ya quedaron actualizados.

Encontré otra falla mía, del análisis 1. Sus tres lecciones dicen que «complementan» las recomendaciones R-2, R-10 y R-18, pero no agregué esas lecciones al origen de cada una, como pide el archivo de recomendaciones. Recomiendo corregirlo dentro de este análisis. ¿Lo agrego?

Si lo aprueba todo, escriba:

```
Apruebo el análisis
```

### 27 · Usuario — 2026-10-08 20:16:00
> pregunta ya quedó claro todo el análisis?

**Agente** — 2026-10-08 20:16:11
<!-- agente: dcbeccb1-9725-4de7-a269-7ae310f00f09 -->

Casi todo. Los dos puntos que usted aprobó ya están escritos en el análisis, y lo que había que hacer de inmediato ya se hizo.

Queda una sola pregunta abierta: corregir una falla del análisis 1. Sus tres lecciones debían quedar anotadas como origen de las recomendaciones que complementan (R-2, R-10 y R-18), y no lo hice. Corregirlo es agregar esa referencia en el archivo de recomendaciones. Recomiendo hacerlo dentro de este análisis.

Si responde que sí, lo anoto y el análisis queda listo para aprobar. Si responde que no, el análisis ya está listo como está.

### 28 · Usuario — 2026-10-08 20:17:33
> respondo: necesito respuestas claras casi todo no me sirve. La respuesta debe ser SI o NO y si es no por qué?

**Agente** — 2026-10-08 20:17:41
<!-- agente: d7560663-1dc0-4cd8-ae11-08a42dba9889 -->

NO. Falta una decisión: si se corrige o no una falla del análisis 1.

La falla es esta: el análisis 1 sacó tres lecciones que completan las recomendaciones R-2, R-10 y R-18, pero esas lecciones no quedaron anotadas en el archivo de recomendaciones como origen de cada una.

Si la respuesta es «sí», se corrige en este análisis y queda listo para aprobar. Si es «no», el análisis ya está listo para aprobar como está.

### 29 · Usuario — 2026-10-08 20:22:24
> hágalo: si

**Agente** — 2026-10-08 20:23:19
<!-- agente: 326ebb4b-0a36-4849-a404-62e23401d2ce -->

La corrección quedó hecha. Las tres lecciones del análisis 1 aparecen ahora como origen de las recomendaciones R-2, R-10 y R-18, y el análisis 2 la registra como acuerdo 3.

El análisis 2 ya no tiene preguntas abiertas. Para aprobarlo, escriba:

```
Apruebo el análisis
```

### 30 · Usuario — 2026-10-08 20:24:28
> Apruebo el análisis

**Agente** — 2026-10-08 20:54:47
<!-- agente: fd4f8dd6-2347-44d9-bc48-bc25b9cf80dd -->

El análisis 2 quedó aprobado, así que retomo la HU-001 donde quedó. Primero sumo al plan la migración que faltaba, comprobada con Django.

Las dos migraciones están creadas y Django no pide ninguna más. Ahora escribo las pruebas de la HU-001.

Pasan 594 de 595 pruebas. Falla una del freno sobre capítulos opt-in. Reviso si la causa es mi cambio o si ya fallaba antes.

No hay un catálogo de módulos de Cimiento que nombre sus apps, así que no hay índice que actualizar. Escribo el resultado y la funcionalidad de la fase.

Pongo al día el estado de la fase, el plan, la HU y la épica.

La HU-001 quedó terminada y probada. Ahora diseño la HU-002: el botón «Revisar», la revisión según el lenguaje de cada proyecto y la página con todos los proyectos.

Escribo la HU-002 y abro su fase.

Ahora el código de la HU-002. Primero el campo nuevo, y compruebo que Django pida solo la migración que el plan declara.

Escribo el reconocimiento del lenguaje y la revisión.

Escribo las vistas, las rutas y las dos pantallas.

Agrego la ayuda de las dos pantallas y el enlace «Pruebas» en la lista de proyectos.

Ahora agrego las pantallas nuevas a las pruebas que ya existen (menú, tablas y ayuda) y escribo las pruebas de la HU-002.

Las 25 pruebas de la app pasan. Corro la regresión de las suites que toca la fase.

Apareció otro archivo que el plan no nombra. Antes de detenerme, reviso exactamente qué exige.

Me detuve otra vez por un hallazgo. Ya está anotado como H-3 en el resumen de la sesión y en el estado de la fase.

**Qué pasó.** Cada pantalla nueva de Cimiento tiene que tener su capítulo en el manual de ayuda. El plan de la HU-002 incluyó el menú, las tablas y la ayuda de la pantalla, pero no el manual. Faltan dos archivos: `core/ayuda/secciones.py` y el texto de la sección. La recomendación R-19 del análisis 2 solo cubría los archivos de la base de datos, así que no lo previno.

**Qué quedó hecho en la HU-002:**
- El reconocimiento del lenguaje de cada proyecto.
- La revisión con la herramienta de cada lenguaje.
- La orden de consola.
- La página con todos los proyectos y la página de cada uno.
- El enlace en el menú y en la lista de proyectos.

Sus 25 pruebas pasan.

**Otra falla, ajena a esta épica.** Una prueba de la guía de pantallas falla desde la EP-028. No la toqué. La anoté como H-4, con su pendiente 143 en la EP-028.

**Qué propongo para el análisis 3:**
1. Agregar al plan de la HU-002 los dos archivos del manual.
2. Ampliar la R-19. Antes de escribir un plan, se pregunta qué archivos pide el cambio. Eso incluye las migraciones y también las piezas que las pruebas le exigen a toda pantalla nueva: menú, tablas, ayuda y manual.

Para abrirlo, escriba:

```
Analicemos: el pendiente 141
```

### 31 · Usuario — 2026-10-08 21:03:35
> Analicemos: el pendiente 141

**Agente** — 2026-10-08 21:05:24
<!-- agente: 483fcad6-50fb-4a4d-b33f-58d236f4a381 -->

El análisis 3 está abierto: [analisis-3.md](historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-3.md).

Cimiento tiene pruebas que revisan que toda pantalla nueva tenga cuatro cosas: un lugar en el menú, tablas que se puedan ordenar, su ayuda y un capítulo en el manual. El plan de la HU-002 olvidó el capítulo del manual, y por eso el trabajo se detuvo.

Necesito dos respuestas, cada una con SÍ o NO:

1. ¿Se agregan al plan de la HU-002 los dos archivos del manual, para que el trabajo siga? Recomiendo SÍ.
2. ¿Se amplía la R-19? Hoy solo pide revisar los archivos de la base de datos. La propuesta es que también pida revisar estas cuatro cosas cada vez que un plan cree una pantalla, en cualquier proyecto. Recomiendo SÍ.

### 32 · Usuario — 2026-10-08 21:05:53
> respondo: SI

**Agente** — 2026-10-08 21:07:43
<!-- agente: 0ce387a3-4a5c-4c47-8e45-c3995acc1ff2 -->

Hago ya lo que se manda «de una»: el pendiente pasa a su V4, el hallazgo H-3 a su V2 y la R-19 se amplía.

Quedaron anotados los dos acuerdos. El pendiente pasó a su V4, el hallazgo H-3 a su V2 y la R-19 ya incluye también las piezas que toda pantalla nueva necesita. El análisis 3 no tiene preguntas abiertas.

Para aprobarlo, escriba:

```
Apruebo el análisis
```

### 33 · Usuario — 2026-10-08 21:10:22
> Apruebo el análisis

**Agente** — 2026-10-08 22:15:23
<!-- agente: 5e74d6eb-3ecb-4bbf-b486-3ac1c9e4cabe -->

El análisis 3 quedó aprobado. Sigo con la HU-002: primero sumo los dos archivos del manual al plan, y después escribo la sección.

Las 120 pruebas de las suites de la fase pasan. Cierro los documentos de la fase A de la HU-002.

Sigo revisando qué piezas pide un subcomando nuevo de validación, para declararlas todas en el plan de la HU-003.

Primero agrego al modelo el dato que necesita el desinstalador y compruebo qué migración pide Django, antes de escribir el plan (R-19).

Ya tengo la lista completa de lo que pide la HU-003. Escribo la HU y abro su fase.

El aviso de enlace roto es del pendiente 142, que escribió otra sesión. No lo toco, porque es trabajo de otra sesión; lo menciono al final. Sigo con el plan de la HU-003.

Ahora el código. Primero la migración declarada y el aviso, que lee la base sin arrancar Django.

La base guarda las fechas en UTC, así que el aviso tiene que compararlas con la hora UTC y no con la local.

Conecto el aviso al arranque de la sesión.

Ahora el subcomando `pruebas` de `validar.py` y su línea en el `pre-commit`.

Ahora `parte.py`, la que pone y quita la herramienta según el lenguaje sin depender de Django, y la orden `marcar_pruebas`.

Agrego el paso al instalador y su contrario al desinstalador.

Escribo las pruebas de la HU-003. Antes reviso cómo se arma `ArranqueDeSesion`.

Las 41 pruebas de la app pasan. Corro la regresión de las suites que toca la HU-003: enganches y herramientas.

Hay 5 problemas. Uno ya se conocía (pendiente 140). Reviso los otros cuatro para saber si los causa este cambio.

Dos fallas son de `validar.py`: el subcomando `estandar` ahora sale con código 1. Lo corro para ver qué reporta.

Esta sí la causa mi cambio: mis pruebas sin Django vacían la base al terminar, y eso choca con lo que prepara `tests_reglas_del_proyecto`. Reviso cómo resolvió esto el resto del código.

The convention in Cimiento is `serialized_rollback = True`, so the database is restored after each test. I'll add it to my test classes.

Ya pasan. Las fallas que quedan en la regresión son ajenas a esta HU: la del pendiente 140 y las dos que causa el enlace roto del pendiente 142, de otra sesión. Cierro los documentos de la HU-003.

La orden falló por cómo la consola leyó el texto largo; no alcanzó a cambiar nada. Escribo los dos documentos con el editor y hago aparte los reemplazos cortos.

Cimiento tiene la orden `cerrar_fase`. Reviso qué hace antes de seguir marcando los documentos a mano.

Solo tocaría el estado de la fase, el plan de pruebas, la HU y la épica; no reescribe lo que ya escribí. La aplico.

La HU-003 quedó cerrada. Sigo con la HU-004, que quita la copia de la configuración. Según la R-19, primero busco todo lo que la nombra, para declararlo en el plan.

Ahora el código de la HU-004. Reviso las cuatro llamadas en las vistas.

Ahora la ayuda, que deja de nombrar la copia, y el paso del instalador que borra la copia vieja.

La HU-004 pasa: 299 pruebas en verde y ningún archivo sigue usando la copia. Escribo su cierre.

Para fijar versiones exactas sin instalar nada, le pido a pip que resuelva Playwright 1.63.0 en modo de prueba.

Pip resolvió las versiones exactas: playwright 1.63.0, greenlet 3.5.6, pyee 13.0.1 y typing_extensions 4.16.0. Con eso cumplo `10·DEP2`. Escribo la HU-005.

Esos enlaces rotos son de la EP-026·HU-011, en la que otra sesión está trabajando ahora mismo. No los toco. Escribo el plan de la HU-005.

Ahora el código de la HU-005: el módulo que encuentra y corre las pruebas de navegador.

Escribo las pruebas de la HU-005.

La HU-005 pasa: 313 pruebas en verde. Cierro su fase.

Cerré las cinco HU. Dejo la épica con un estado uniforme y reviso si quedaron marcadores sin llenar en sus archivos.

Pongo al día el índice de épicas. Después reviso cómo registró su versión la épica anterior, porque la regla `20·M10` exige versionar todo cambio.

Las cuatro migraciones quedaron aplicadas. Hago una prueba real, con un proyecto registrado, para ver el mensaje que recibe quien usa Cimiento cuando a un proyecto le falta la herramienta.

Ahora registro la versión del estándar en la base. Es MAYOR porque obliga a volver a instalar Cimiento en cada proyecto.

La versión quedó registrada: el estándar pasa a la 59.0.0, MAYOR. Reviso si hay una herramienta para cerrar el pendiente 141, ahora que sus tres análisis están construidos.

El pendiente 141 no se cierra a mano: su estado sale solo de los enlaces, y su épica ya está terminada. Lleno la sección de cierre del resumen de la sesión.

Reúno la lista de lo que cambió esta sesión, para separarlo del trabajo de las otras antes de preguntar por el commit.

La EP-029 quedó construida completa: las cinco HU, cada una con su plan, sus pruebas y su cierre.

**Qué quedó funcionando:**
- En la página de cada proyecto se elige qué tan estricto ser con la revisión de pruebas y cada cuántos días hacerla.
- La página «Revisión de pruebas» muestra todos los proyectos. El botón «Revisar» revisa con la herramienta del lenguaje de cada uno e incluye las pruebas de navegador.
- Al empezar a trabajar, Cimiento avisa si la revisión falta o está vencida. Con la opción «no dejar guardar», además no deja guardar los cambios.
- El instalador pone la herramienta que revisa, y el desinstalador la quita.
- La copia de la configuración que nadie usaba ya no existe.
- La base de Cimiento ya tiene las tablas nuevas. El estándar pasó a la versión 59.0.0, que es MAYOR.

**Lo que no salió perfecto:**
- La ejecución se detuvo dos veces por archivos que el plan no nombraba. Se resolvió con los análisis 2 y 3, y la recomendación R-19 quedó para que no se repita.
- Al cerrar encontré y corregí un defecto mío: la revisión dejaba un archivo suelto dentro del proyecto revisado.
- La herramienta `cerrar_fase` deja sin marcar los criterios que tienen dos casos (pendiente 139). Los marqué a mano.

**Lo que es de otras sesiones y no toqué:**
- Hay enlaces rotos en el pendiente 142 y en la EP-026·HU-011, y fallan pruebas por ellos y por el pendiente 140.
- `tests_freno.py` lo cambió otra sesión.
- El análisis principal mezcla líneas mías y de otras sesiones.

Falta, en orden:
1. Su aprobación del commit.
2. Volver a instalar Cimiento en cada proyecto, porque es una versión MAYOR.
3. Dar clic en «Revisar» en cada proyecto.

¿Hago el commit, SÍ o NO? Sería uno solo para toda la épica, como en la EP-028, y solo con los archivos de esta sesión.

### 34 · Usuario — 2026-10-08 22:17:24
> hágalo: haga comit y suba
