# Análisis 1: Cimiento no mide qué código queda sin probar ni prueba sus pantallas en un navegador

> **Aprobado** por el usuario el 2026-10-08, en el turno 23, con la versión 56.8.0. Desde ese momento este análisis no se reescribe.

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
> | [`00·ID8`](../../../../../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md) | Escribir sin las marcas que delatan generación automática |
> | [`00·ID9`](../../../../../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md) | Decir lo mismo en menos palabras |
> | [`00·ID11`](../../../../../base/00-identidad-y-rol/reglas/ID11-el-agente-agrega-informacion-irrelevante-al-asunto.md) | Escribir solo lo pertinente al asunto |
> | [`00·ID12`](../../../../../base/00-identidad-y-rol/reglas/ID12-el-agente-no-conserva-el-espanol-colombiano.md) | Seguir la norma del español de Colombia, si el proyecto la declara |

> Un análisis aprobado no se reescribe. Si al ejecutar el plan aparece un hallazgo que obliga a tocar algo que el plan no declara, se abre `analisis-«N+1»`.md, que trata solo lo que falló y sus implicaciones sobre lo ya hecho. El hallazgo que no obliga a eso no abre análisis: se anota con su pendiente donde pertenece y el plan continúa.

---

## Recomendaciones

Se leyeron las [recomendaciones de Cimiento](../../../../../plantillas/recomendaciones-del-analisis.md); el proyecto no tiene `analisis/recomendaciones.md`.

| Recomendación | Cómo se aplica en este análisis |
|---|---|
| R-1 | «Dónde más puede pasar» revisa los proyectos Django que heredan, los de otro stack y la plantilla `stack.md` |
| R-2 | Se revisaron `08·T6`, `20·M3`, la plantilla `stack.md`, las 87 pruebas de Cimiento, sus dependencias, la configuración de cada proyecto y su copia local |
| R-7 | Se preguntaron el alcance, la página, cómo se exige y la copia local; el umbral no se preguntó porque `08·T6` ya lo decide |
| R-8 | «Analicemos» autoriza este archivo y nada más: no se instaló ni se configuró nada |
| R-10 | Se aplicó tarde: tres preguntas no se entendieron hasta reescribirlas sin términos técnicos (lección 1) |
| R-17 | Cada respuesta se midió contra `00·ID9` antes de entregarla |
| R-18 | «Lo acordado» se escribió en el turno en que el usuario respondió |
| Las demás | No aplican: no se cambia ninguna regla (R-3, R-4), es el análisis 1 (R-6), no hay piloto (R-16) |

---

## Hallazgo

### H-1 · Cimiento no sabe qué parte de su código no prueba ninguna prueba

| Campo | Valor |
|---|---|
| Qué pasó | El usuario preguntó qué sistemas de pruebas sirven en Django. Cimiento tiene 87 archivos de pruebas y 27 abren sus páginas con el cliente de Django, pero nada mide qué código queda sin probar y ninguna prueba usa un navegador real. El usuario aprobó empezar por coverage.py y el cliente de Django, y seguir con Playwright, recorriendo la cadena desde el análisis |
| Por qué importa | Un hueco sin medir no se ve, y lo que corre en el navegador (htmx, list.js, ApexCharts) puede dañarse sin que falle ninguna prueba |
| Pendiente | [Pendiente 141: Cimiento no mide qué código queda sin probar ni prueba sus pantallas en un navegador](pendiente.md) |

## Pendiente

**De dónde sale:** H-1 · Cimiento no sabe qué parte de su código no prueba ninguna prueba, en el resumen de la sesión del 2026-10-07.

**El problema.** Cimiento tiene 87 archivos de pruebas en `proyectos/cimiento/core/`, que corren con `manage.py test`. De ellos, 27 abren sus páginas con el cliente de pruebas de Django (`self.client`), sin navegador. Faltan dos cosas:

- **Medir qué código no se prueba.** `requirements/` no trae coverage.py ni otra herramienta que diga qué líneas no ejecuta ninguna prueba. Hoy no se sabe dónde están los huecos.
- **Probar en un navegador.** Ninguna prueba usa `LiveServerTestCase` ni un navegador real. Lo que pasa en la página después de cargarla (htmx, list.js, los gráficos de ApexCharts) no lo revisa nada.

**Por qué importa.** Sin medir, una parte del código puede no tener ninguna prueba y nadie se da cuenta. Lo que corre en el navegador puede dañarse y las pruebas siguen pasando. Y como Cimiento es la base de los proyectos que lo heredan, lo que se decida aquí sirve también para ellos.

---

## Conversación

> La escribe el enganche en tiempo real, turno por turno, desde la transcripción de la sesión. No se escribe a mano.

### 8 · Usuario, 2026-10-08 13:20:07
> Analicemos: el pendiente 141

**Agente**, 2026-10-08 13:24:58
<!-- agente: 1cd0fa55-f567-40eb-a16b-03dc45d6a08f -->

El análisis quedó abierto. Antes de escribir, reúno lo que piden las recomendaciones R-1 y R-2: qué dicen las reglas de pruebas, qué existe y quién hereda.

Estoy llenando las partes del análisis que salen de revisar el repositorio. Las decisiones quedan para después, en el chat.

Ahora las recomendaciones, las dos copias y lo que aporta cada parte.

El análisis 1 del pendiente 141 está abierto y ya tiene lo que salió de revisar el repositorio: [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md). Lo que sigue depende de tres decisiones, cada una con mi recomendación.

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

### 9 · Usuario, 2026-10-08 13:28:14
> Respondo: 
> 1. no entiendo la pregunta
> 2. qué recomienda
> 3. no entiendo la pregunta

**Agente**, 2026-10-08 13:28:28
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

### 10 · Usuario, 2026-10-08 13:30:31
> Respondo:
> 1. eso se puede detectar desde cimiento sin importar el stack
> 2. aprobado
> 3. b

**Agente**, 2026-10-08 13:32:03
<!-- agente: 28d72642-951f-4789-88c8-8a1d61e8a344 -->

Antes de anotar el acuerdo 1, busco si Cimiento ya sabe reconocer el stack de un proyecto.

Cimiento ya reconoce el stack por sus archivos: [dependencias.py](../../../../../proyectos/cimiento/core/validadores/dependencias.py#L17) busca `composer.json`, `package.json` y otros. Anoto los tres acuerdos.

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

### 11 · Usuario, 2026-10-08 13:39:12
> 4. apruebo
> 5. todos los proyectos la idea es que cimiento los administre todos por eso es la línea base
> 6. apruebo

**Agente**, 2026-10-08 13:39:47
<!-- agente: 4c8320a5-2c22-403d-9bdf-770f6f133d3b -->

Anoto los acuerdos 4 a 6.

Queda una pregunta antes de armar la propuesta final.

**7. ¿Cuándo se mide?**

Medir la cobertura obliga a correr todas las pruebas del proyecto, y eso puede tardar varios minutos.

- a) Cuando alguien da clic en un botón «Medir» al lado de cada proyecto en la página. El mismo botón sirve para correr las pruebas de Playwright.
- b) Sola, cada vez que se corren las pruebas.

Recomiendo **a**. Con **b**, cada corrida de pruebas se vuelve más lenta aunque nadie vaya a mirar la cobertura en ese momento.

### 12 · Usuario, 2026-10-08 13:42:25
> Respondo:
> cimiento debe obligar a cada proyecto tener una parte a que mida eso y se lo avise así como le avisa la instalación

**Agente**, 2026-10-08 13:42:48
<!-- agente: 7e45ba80-c7c3-448b-a77c-7beabef7c995 -->

Reviso cómo avisa hoy Cimiento lo de la instalación, para entender bien la respuesta.

Entiendo la respuesta así. Al abrir una sesión, Cimiento ya revisa si el proyecto está instalado y avisa, por ejemplo: «falta el enganche pre-commit — correr instalar.py». Con la medición pasaría lo mismo: el instalador le pone a cada proyecto la parte que mide la cobertura, y esa parte es obligatoria.

Lo que no tengo claro es qué debe decir el aviso al abrir la sesión:

- a) Solo si falta la parte que mide: «este proyecto no mide su cobertura — correr instalar.py».
- b) También el resultado de la última medición: «hay 12 archivos sin probar», o «la última medición es de hace 20 días».

Recomiendo **a y b juntas**. La a es igual a la de instalación. La b hace que el aviso sirva para algo más que confirmar que la parte está instalada.

Sigue sin responder la 7: si la medición arranca con un botón o sola cada vez que se corren las pruebas. Con la b, recomiendo el botón y que el aviso diga cuándo se midió por última vez.

### 13 · Usuario, 2026-10-08 13:47:14
> Respondo: Desde la configuración de cada proyecto simiento sabe el estado y eso es lo que debe hacer que se cumpla.  Qué propone ahí

**Agente**, 2026-10-08 13:48:14
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

### 14 · Usuario, 2026-10-08 13:54:53
> respondo: humanice lo que propone y cuando se apliquen esos cambios debe ser humanizado para eso está la regla 00 id7

**Agente**, 2026-10-08 13:55:39
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

### 15 · Usuario, 2026-10-08 14:29:15
> respondo cada proyecto que lo implente debe saber suconfiguración de cimiento he irla complementando

**Agente**, 2026-10-08 14:29:44
<!-- agente: 37112326-37a8-4116-8ca0-102d49612459 -->

Reviso qué recibe hoy un proyecto de su configuración en Cimiento.

Hoy cada proyecto ya tiene una copia de su configuración: Cimiento la escribe sola en `.agente/configuracion.md` cada vez que algo cambia ([copia.py](../../../../../proyectos/cimiento/core/proyectos/copia.py)). Esa copia dice qué ajustes tiene el proyecto y qué reglas están suspendidas. No dice qué tan estricta es cada regla, ni nada sobre las pruebas.

Su frase la entiendo de dos maneras, y necesito saber cuál es:

- a) **El proyecto lee su configuración.** Esa copia suma la parte de las pruebas: qué tan estricto ser, cada cuántos días revisar, cuándo se revisó por última vez y qué salió. Así el proyecto sabe lo que Cimiento le exige, sin tener que abrir la página.
- b) **La configuración crece con cada cosa nueva.** Cada vez que Cimiento gana una función, como esta de las pruebas, la opción aparece sola en la configuración de todos los proyectos, con su valor por defecto, y cada uno la va ajustando.

Recomiendo **a y b juntas**. La b ya existe para los ajustes: uno nuevo aparece en todos los proyectos con el valor común. Lo que falta es la a: que la copia también lleve la parte de las pruebas.

### 16 · Usuario, 2026-10-08 14:31:51
> respondo: hoy cada proyecto la tiene pero lo se busca es que todo eso lo administre Cimiento y cada proyecto consulta su configuración para funcionar

**Agente**, 2026-10-08 14:32:39
<!-- agente: 0d9717ae-a820-487c-857c-49f5ba2dcc37 -->

Reviso si hoy los proyectos leen la configuración de la base de Cimiento o de la copia.

Quedó anotado como acuerdo 9: Cimiento guarda en su base toda la configuración de cada proyecto, y cada proyecto la consulta ahí cuando la necesita.

Parte de esto ya funciona así. El freno le pregunta a la base de Cimiento, en cada acción, qué tan estricta es cada regla en ese proyecto ([niveles.py](../../../../../proyectos/cimiento/core/enganches/niveles.py)). En cambio, la copia `.agente/configuracion.md` se sigue escribiendo, pero ningún programa la lee.

La propuesta queda así:

- Las dos opciones nuevas (qué tan estricto ser y cada cuántos días revisar) y el resultado de cada revisión se guardan en la base de Cimiento.
- Al abrir una sesión, el proyecto le pregunta a la base cómo va su revisión y muestra el aviso si hace falta.
- La revisión se hace con el botón «Revisar».

Para cerrar este punto necesito dos respuestas:

1. ¿Se aprueba la propuesta así?
2. Sobre la copia `.agente/configuracion.md`, que nadie lee y que va en contra del acuerdo 9, ¿qué se hace? Recomiendo quitarla en esta misma épica: si se deja, alguien puede creer que es la configuración de verdad y confiar en datos viejos.

### 17 · Usuario, 2026-10-08 14:39:27
> respondo: humanice la respuesta y las preguntas

**Agente**, 2026-10-08 14:39:40
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

### 18 · Usuario, 2026-10-08 14:51:55
> 1. qué funcione cómo?
> 2. si

**Agente**, 2026-10-08 14:52:05
<!-- agente: 45a0a606-e264-485f-b161-709e206e9318 -->

Le falta la palabra que dice qué espera (por ejemplo «Respondo»). Quedo atento a que la agregue para seguir.

### 19 · Usuario, 2026-10-08 14:53:21
> Respondo:
> 1. qué funcione cómo?
> 2. si

**Agente**, 2026-10-08 14:53:52
<!-- agente: 27f8cc17-0e54-437f-bcd0-e66e77980bc3 -->

Anotado: la copia que nadie usa se borra.

La pregunta 1 era confusa; la hago de nuevo. Se trata de la revisión de pruebas, es decir, de saber qué partes de cada programa no tienen quién las revise. La propuesta tiene tres pasos:

1. En la página de cada proyecto, dentro de Cimiento, se eligen dos cosas: qué tan estricto ser y cada cuántos días revisar. Si nadie las cambia, queda en «solo avisar» y «cada 7 días».
2. Cuando alguien empieza a trabajar en un proyecto, Cimiento mira esas dos opciones. Si la revisión está vencida, avisa: «La última revisión fue hace 12 días. Toca hacer otra.»
3. La revisión se hace con el botón «Revisar» en esa misma página. Al terminar, muestra qué partes quedaron sin pruebas.

¿Aprueba esos tres pasos, o cambia alguno?

### 20 · Usuario, 2026-10-08 14:57:11
> apruebo

**Agente**, 2026-10-08 15:05:17
<!-- agente: 187bc848-d1a1-41c3-91ac-b09edf52f55b -->

Anoto el acuerdo 11. Con eso no queda ninguna pregunta abierta, así que paso a escribir la propuesta final.

Tomo como modelo el análisis aprobado más reciente.

Escribo las dos lecciones en la base de señales.

Ahora escribo la propuesta final, las lecciones, lo que se tiene que hacer y el aporte al análisis principal.

Actualizo el tipo de versión, que antes dependía del alcance y ya quedó decidido. Después paso el hallazgo y el pendiente a su V2 en los archivos originales (fila 1).

Borro las notas de la plantilla que ya se cumplieron, como pide la misma plantilla.

El análisis 1 del pendiente 141 está completo y listo para aprobar: [analisis-1.md](../../../../../historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/analisis-1.md).

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

### 21 · Usuario, 2026-10-08 15:08:21
> Apruebo el análisis

**Agente**, 2026-10-08 15:09:59
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

### 22 · Usuario, 2026-10-08 15:10:32
> liste los acuerdos que se van aprobar

**Agente**, 2026-10-08 15:10:45
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

### 23 · Usuario, 2026-10-08 15:12:00
> Apruebo el análisis

**Agente**, 2026-10-08 15:28:21
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

**Qué pasó.** Las dos opciones nuevas de la configuración obligan a Django a crear un archivo de base de datos que el plan de la HU-001 no nombra: `core/proyectos/migrations/0007_...py`. Las reglas no dejan escribir lo que el plan no nombra. En un caso igual de la EP-028 ese archivo sí estaba en el plan; esta vez se me pasó al escribirlo. Lo anoté como H-2 en el resumen de la sesión, y en el plan y el estado de la fase.

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

> acá termina la conversación

---

## Lo acordado

1. Alcance: la cobertura se mide en todo proyecto, no solo en Cimiento. Cimiento reconoce el stack de cada proyecto por sus archivos y usa la herramienta que le corresponde; el proyecto no tiene que declararla (turno 10).
2. Playwright: entra en esta misma épica, como la última HU, después de la medición de cobertura (turno 10).
3. Dónde se ve: el resultado de la cobertura se muestra también en una página de Cimiento, no solo en la consola (turno 10).

4. Herramienta por stack: Python y Django con coverage.py, Laravel con PHPUnit y PCOV, Angular con `ng test --code-coverage`. El stack que no esté en esa lista se muestra como «sin medición» y no falla (turno 11).
5. Qué proyectos: la página muestra todos los proyectos registrados, uno por fila, porque Cimiento los administra a todos (turno 11).
6. Playwright: Cimiento lo deja instalado y corre las pruebas de navegador de cualquier proyecto que las tenga; escribir esas pruebas es trabajo de cada proyecto (turno 11).

7. Obligatorio: Cimiento obliga a cada proyecto a tener la parte que mide y le avisa como le avisa hoy lo de la instalación. Lo hace cumplir desde la configuración de cada proyecto, que es donde Cimiento conoce su estado (turnos 12 y 13).
8. Cómo se escribe: los avisos, la página y los botones que salgan de este análisis se escriben para quien no sabe del tema, como exige `00·ID7` (turno 14).

9. Dónde vive la configuración: Cimiento administra en su base todo lo de cada proyecto, también lo de la medición, y cada proyecto consulta ahí su configuración para funcionar, en vez de tener su propia copia (turnos 15 y 16).

10. La copia local: se quita `.agente/configuracion.md`, que Cimiento escribe en cada proyecto y ningún programa lee (turno 19).

11. Cómo se exige y cómo arranca: en la página de cada proyecto se eligen qué tan estricto ser con la revisión (solo avisar, no dejar guardar los cambios hasta revisar, o nada) y cada cuántos días revisar, con «solo avisar» y 7 días si nadie los cambia. Al empezar a trabajar en un proyecto, Cimiento compara esas opciones con la última revisión y avisa si está vencida. La revisión arranca con el botón «Revisar» de la página del proyecto y al terminar muestra qué partes quedaron sin pruebas (turno 20).

Siguen abiertas: ninguna.

---

## Lo que aportó cada parte

### Cimiento: las reglas que aplican y las que chocan

Aplican:

- `08·T6`: la cobertura se mide con criterio, no por porcentaje. coverage.py sirve para ver los huecos en la lógica, las reglas y los caminos de error, no para exigir un número.
- `08·T5`: las pruebas se corren y se reporta el resultado. El reporte de cobertura se suma a ese resultado.
- `08·T8`: el resultado esperado no sale del código que se prueba. Una línea cubierta no es una línea bien probada.
- `10·DEP2`: toda dependencia nueva va con su versión exacta en `requirements/lock.txt`.

Choca:

- `20·M3`: `base/` no nombra herramientas de un stack. Su ejemplo INCORRECTO es justamente «usar pytest con cobertura mínima de 80%». coverage.py y Playwright no pueden entrar a `base/`. Van en Cimiento y, para los proyectos que heredan, en lo que el proyecto declara en `.agente/stack.md`.

### El proyecto: lo que existe, lo que funciona y lo que falta

| Qué | Lo que hay hoy |
|---|---|
| Pruebas | 87 archivos `tests*.py` en `proyectos/cimiento/core/`: 121 clases sobre `unittest.TestCase`, 54 sobre `TestCase`, 27 sobre `SimpleTestCase` y 11 sobre `TransactionTestCase`. Se corren con `python manage.py test core` (`proyectos/cimiento/README.md`) |
| Pruebas de páginas | 27 archivos usan `self.client`: abren la página y revisan la respuesta, sin ejecutar su JavaScript |
| Navegador | Ninguna prueba usa `LiveServerTestCase` ni `StaticLiveServerTestCase` |
| Medir cobertura | No hay nada: `requirements/base.txt` y `local.txt` no traen coverage.py |
| Lo que corre en el navegador | htmx 2.0.11, list.js 2.3.1, ApexCharts 7.8.0, AdminLTE 4.10.0 (`proyectos/cimiento/package.json`) |
| Integración continua | El repositorio no tiene `.github/workflows` ni `.gitlab-ci.yml` |
| Plantilla `stack.md` | Tiene la fila «Correr las pruebas» y la sección «Entorno de pruebas», pero ningún campo para medir cobertura ni para pruebas en navegador |

### Lo aprendido: señales, lecciones y análisis anteriores

| Fuente | Qué aporta |
|---|---|
| S-164 · Un caso de prueba que no puede fallar no es un caso de prueba | Confirma `08·T8`: medir cobertura no prueba que las pruebas sirvan. Lo recoge «Lo acordado» si se decide el alcance de la medición |
| S-300 · El MariaDB de WAMP crea las tablas con MyISAM | Las pruebas en navegador corren contra la base de pruebas de MariaDB; el arreglo ya está en `config/settings/base.py` y vale también para ellas |
| Búsqueda de «cobertura», «coverage», «playwright», «selenium» | No hay intentos anteriores en la base de señales |

### El entorno: normas, herramientas y proyectos que heredan

| Qué | Efecto |
|---|---|
| Proyectos que heredan | MAYOR (`20·M10`): por el acuerdo 7, todo proyecto tiene que volver a instalar para recibir la parte que revisa |
| Normas y leyes | Ninguna |
| Herramientas | coverage.py se suma a `manage.py test` sin cambiar las pruebas. Playwright necesita bajar navegadores (varios cientos de megas) y corre en Windows; sus pruebas usan `StaticLiveServerTestCase` y la base de pruebas de MariaDB |

### Dónde más puede pasar

| Caso | Dónde se presenta | Riesgo si queda sin cubrir | Lo cubre |
|---|---|---|---|
| Cimiento no mide cobertura | `proyectos/cimiento/` | Huecos sin probar que nadie ve | Acuerdo 1 |
| Proyectos Django que heredan | shopnest-mesa, Gestión de Servicios Tecnológicos, LocalHub | El mismo hueco en cada uno | Acuerdo 1 |
| Proyectos de otro stack | AgroSystem (Laravel), RNI (Angular y Python) | Cada stack tiene su herramienta | Acuerdos 1 y 4. `20·M3` no choca: la herramienta vive en Cimiento, no en `base/` |
| La plantilla `stack.md` no pregunta cómo se mide la cobertura | `plantillas/stack.md` | Ninguno | No hace falta: por el acuerdo 1, Cimiento lo detecta y el proyecto no lo declara |

---

## Propuesta final: hallazgo y pendiente V2, épica y HU

### Hallazgo V2. Cimiento no sabe qué parte del programa de cada proyecto queda sin pruebas, ni lo exige

| Campo | Valor |
|---|---|
| Qué pasó | Al preguntar qué sistemas de pruebas sirven en Django, salió que ni Cimiento ni los proyectos que administra miden qué parte de su programa queda sin pruebas, que ninguna prueba usa un navegador real y que la configuración de cada proyecto no exige nada de eso |
| Por qué importa | Cimiento es la línea base de todos los proyectos: un hueco que no se mide no se ve en ninguno, y lo que corre en el navegador se puede dañar sin que falle ninguna prueba |

### Pendiente V2. Cimiento revisa qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración

| Campo | Valor |
|---|---|
| De dónde sale | Hallazgo V2: Cimiento no sabe qué parte del programa de cada proyecto queda sin pruebas, ni lo exige |
| El problema | Ningún proyecto mide qué parte de su programa queda sin pruebas; la configuración de cada proyecto no lo exige ni guarda el estado; ninguna prueba usa un navegador real; y cada proyecto tiene una copia de su configuración, `.agente/configuracion.md`, que ningún programa lee |
| Por qué importa | Un hueco sin medir no se ve, una exigencia que no está en la configuración no se cumple, y una copia que nadie lee termina con datos viejos que alguien puede creer ciertos |

### Épica y HU que salen del análisis

Épica nueva: **EP-029, Cimiento sabe qué parte de cada proyecto queda sin pruebas y lo exige desde su configuración**.

| Orden | HU | Título | Parte del problema que resuelve | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|---|
| 1 | EP-029·HU-001 | La configuración de cada proyecto dice qué tan estricta es la revisión de pruebas y cada cuántos días toca | La configuración no lo exige ni guarda el estado | Ninguna | Las demás leen estas opciones | 2, 3, 11 |
| 2 | EP-029·HU-002 | El botón «Revisar» muestra qué parte de cada proyecto queda sin pruebas, con la herramienta de su lenguaje | Ningún proyecto mide qué parte queda sin pruebas | EP-029·HU-001 | Guarda el resultado donde lo dejó la HU-001 | 4, 5, 6, 11 |
| 3 | EP-029·HU-003 | Al empezar a trabajar, Cimiento avisa si falta la revisión o si está vencida, y el instalador pone la parte que revisa | Nada obliga a revisar | EP-029·HU-001, EP-029·HU-002 | Compara las opciones de la HU-001 con el resultado de la HU-002 | 7, 8, 11 |
| 4 | EP-029·HU-004 | Cada proyecto consulta su configuración en Cimiento y la copia local desaparece | La copia que ningún programa lee | EP-029·HU-001 | Sale cuando la configuración nueva ya vive en la base | 9, 11 |
| 5 | EP-029·HU-005 | Cimiento corre las pruebas de navegador de cualquier proyecto que las tenga | Ninguna prueba usa un navegador real | EP-029·HU-002 | Acuerdo 2: va de última, y muestra su resultado en la página de la HU-002 | 10, 11 |

## Lecciones aprendidas

| # | Lección | Tipo | Señal | Recomendación |
|---|---|---|---|---|
| 1 | Las preguntas del análisis se escriben sin términos técnicos desde la primera vez: el usuario pidió tres veces que se humanizaran | Falló | S-350 | Complementa R-10 |
| 2 | Se mide antes de afirmar cuánto se usa algo en el código: se dijo que el cliente de Django casi no se usaba, y lo usan 27 de 87 archivos | Falló | S-351 | Complementa R-2 |
| 3 | El turno de cada acuerdo se copia de la conversación, no se cuenta a ojo: cuatro citas estaban mal y la aprobación se rechazó | Falló | S-352 | Complementa R-18 |

## Lo que se tiene que hacer

| # | Lo que se tiene que hacer | Sale de lo acordado | Pasó a |
|---|---|---|---|
| 1 | Pasar el pendiente a su versión siguiente y el hallazgo a su V2 | `13·DOC26` | Este análisis, de una y sin fase: `historico-chat/resumenes/2026-10-08/pendientes/141-cimiento-no-mide-que-codigo-queda-sin-probar-ni-prueba-sus-pantallas/pendiente.md` y `historico-chat/resumenes/2026-10-07/instalar-desde-cimiento-y-pruebas-en-django.md`, hecho el 2026-10-08 |
| 2 | Dos ajustes nuevos en la configuración de cada proyecto, con valor común y valor propio: qué tan estricta es la revisión (solo avisar, no dejar guardar los cambios, o nada; por defecto, solo avisar) y cada cuántos días toca (por defecto, 7) | 7, 11 | EP-029·HU-001 |
| 3 | La base de Cimiento guarda, por proyecto, si tiene la parte que revisa, la fecha de la última revisión, el resultado archivo por archivo y el de las pruebas de navegador | 3, 9 | EP-029·HU-001 |
| 4 | Cimiento reconoce el lenguaje de cada proyecto por sus archivos y revisa con su herramienta: coverage.py para Python y Django, PHPUnit con PCOV para Laravel, `ng test --code-coverage` para Angular; el lenguaje que no esté en la lista se muestra como «sin medición» y no falla | 1, 4 | EP-029·HU-002 |
| 5 | Un botón «Revisar» en la página de cada proyecto, y una orden de consola que hace lo mismo, arrancan la revisión | 11 | EP-029·HU-002 |
| 6 | Una página de Cimiento muestra todos los proyectos registrados, uno por fila, con qué parte quedó sin pruebas y cuándo se revisó | 3, 5 | EP-029·HU-002 |
| 7 | Al empezar a trabajar en un proyecto, Cimiento compara sus opciones con la última revisión y avisa si falta la parte que revisa o si la revisión está vencida; con «no dejar guardar los cambios», el freno no deja hacer commit hasta revisar | 7, 11 | EP-029·HU-003 |
| 8 | El instalador pone en cada proyecto la parte que revisa, y el desinstalador la quita | 7, `02·F30` | EP-029·HU-003 |
| 9 | Cada proyecto consulta su configuración en la base de Cimiento; se quita la copia `.agente/configuracion.md` y lo que la escribe | 9, 10 | EP-029·HU-004 |
| 10 | Cimiento deja instalado Playwright y corre las pruebas de navegador de cualquier proyecto que las tenga; el resultado sale en la página de la HU-002. Escribir esas pruebas es trabajo de cada proyecto | 2, 6 | EP-029·HU-005 |
| 11 | Los avisos, la página, las opciones y los botones se escriben para quien no sabe del tema | 8, `00·ID7` | EP-029·HU-001 a EP-029·HU-005 |

## Lo que aporta al análisis principal

**Resultado:** amplía la idea y cambia lo que se construye.

**Lo que suma al análisis principal:** Cimiento sabe qué parte del programa de cada proyecto queda sin pruebas: la revisa con la herramienta del lenguaje de cada uno, la muestra en su página, la exige desde la configuración de cada proyecto, que vive solo en su base y que cada proyecto consulta para funcionar, y corre las pruebas de navegador de los proyectos que las tengan.
