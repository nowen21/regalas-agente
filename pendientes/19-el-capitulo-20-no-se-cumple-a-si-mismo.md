# Pendiente · El capítulo de meta-reglas no se cumple a sí mismo

**Estado:** abierto, con una de sus tres deudas cerrada · anotado 2026-08-14 · nace del hallazgo H-6 de [2026-08-14](../historico-chat/resumenes/2026-08-14/hu-de-la-comprobacion-automatica.md).

| | |
|---|---|
| **Historia de usuario** | [EP-001 · HU-009 — Poner al día las reglas que no pasan su propio checklist](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/HU-009-reglas-sin-checklist-al-dia.md) — es exactamente lo que esa historia pide, ya medido |

## El problema

El validador de meta-reglas midió por primera vez el propio cuerpo de reglas. De **188 reglas**:

| Qué | Cuántas |
|---|---|
| Sin bloque de checklist | 129 |
| Publicadas con el checklist en "no cumple" | 7 |
| Sin clasificar en `reglas-validables.md` | 33 |

Las siete en "no cumple" son `F4`, `F5`, `F12`, `M2`, `M4`, `M7` y `M8`. `M14` dice que sin CUMPLE una regla no se publica, y están publicadas.

Las 33 sin clasificar incluyen los capítulos `18` y `19` completos, que ese archivo no menciona.

## Qué falta

**1. Decidir qué se hace con las siete.** Tres caminos: corregirlas, derogarlas, o aceptar que el checklist no aplica hacia atrás y dejarlo escrito.

**2. Clasificar las 33.** ✅ **Hecho el 2026-08-16** (v23.1.1), en la fase [`A-EP-001-HU-009`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-009-reglas-sin-checklist-al-dia/A-EP-001-HU-009-clasificar-las-que-faltan/). Bajaron a cero.

**Y cambió el diagnóstico:** quince de las 33 **ya estaban clasificadas**. El registro decía `C1–C17`, un rango, y el programa busca cada identificador literal. Las que faltaban de verdad eran 18 — los capítulos `18` y `19` completos, más `G9`, `M15`, `F4` y `F12`.

**3. Las 121 sin bloque** (eran 129 cuando se anotó). Aplicarles el checklist es trabajo largo y con criterio. Conviene por capítulo, no de a una.

## El límite

El validador dice cuáles faltan, no si la regla está bien escrita. Eso lo decide quien la lee.

## La medición vuelve a ser posible — 2026-08-17

Este pendiente citaba una medición hecha con `metareglas.py` el 2026-08-14, y desde entonces **no se podía repetir**: el programa no tenía subcomando en `validar.py`. Al cerrar el [53](hecho/ningun-validador-termina-en-silencio.md) lo ganó.

```
$ python validadores/validar.py metareglas
7 falla(s), 229 aviso(s).
```

**Ese es el tamaño real de este pendiente, medido hoy y repetible.**

Y llegó con un defecto que hay que resolver acá, el `D-02`: **una regla nueva sin clasificar sale como `AVISO`, y un aviso no detiene la publicación**. El `CA-03` de esa historia pide que la detenga. La prueba que lo denunciaba estaba marcada como fallo esperado por dos motivos —el subcomando y el aviso—; el subcomando se arregló, así que ahora **pasa con la mitad hecha**. Se le escribió encima qué no comprueba, para que nadie la lea como que el `CA-03` está cubierto.

## Lo que le agrega el cierre del 52 — 2026-08-18

**Una cuarta deuda, medida hoy: 36 sellos vencidos de 73.** Un sello vencido dice que la regla, tal como está escrita hoy, pasó las veinte filas — y no es cierto. Es peor que no tener sello. Se cuentan con `validar.py metareglas`.

**Y una regla más en NO CUMPLE: `F13`, ahora son ocho.** No es que haya empeorado: decía «pendiente de aplicar», una forma que el validador no reconocía, así que figuraba como «no trae su bloque» —un aviso— cuando era una regla publicada sin sello válido. Se le aplicó el checklist y reprueba por **una sola fila, la 10**: el cuerpo mide 631 caracteres y el molde da 320. Su bloque deja escrito qué falla, para no volver a medirlo.

**Recortar `F13` es trabajo de este pendiente**, no del 52: es un cambio de regla y va con el repaso del capítulo `02`.

## Los dos primeros capítulos con su checklist aplicado — 2026-08-18

El punto 3 pedía hacerlo **por capítulo, no de a una**. Van dos, empezando por los más chicos.

| Capítulo | Reglas | CUMPLE | NO CUMPLE |
|---|---|---|---|
| `14` Estructura del código | 3 | `EST1`, `EST3` | `EST2` |
| `15` Registros inmutables | 5 | `IM1`, `IM4`, `IM5` | `IM2`, `IM3` |
| `11` Configuración y entornos | 4 | `CFG1`, `CFG2`, `CFG4` | `CFG3` |
| `12` Privacidad y datos personales | 5 | `PR1`, `PR2`, `PR5` | `PR3`, `PR4` |
| `10` Dependencias de terceros | 5 | `DEP1`, `DEP2`, `DEP4`, `DEP5` | `DEP3` |
| `05` Errores y logging | 5 | `E1`, `E3`, `E5` | `E2`, `E4` |
| **`06` Rendimiento y eficiencia** | 6 | **los seis** | — |
| `07` Calidad de código | 7 | `Q1` a `Q6` | `Q7` |
| `08` Estrategia de pruebas | 7 | `T2`, `T3`, `T5`, `T6` | `T1`, `T4`, `T7` |
| `17` Interfaz | 6 | `I2`, `I4`, `I5`, `I6` | `I1`, `I3` |
| **`03` Datos** | 8 | `D2` | **`D1`, `D3`, `D4`, `D5`, `D6`, `D7`, `D8`** |
| **`04` Seguridad** | 11 | `S8` | **`S1` a `S7`, `S9`, `S10`, `S11`** |
| `09` Git | 9 | `G1` a `G5` | `G6`, `G7`, `G8`, `G9` |
| **`00` Núcleo blindado** | 6 | `N2`, `N3`, `N5` | **`N1`, `N4`, `N6`** |
| `18` Despliegue · opt-in | 8 | — | los ocho |
| `19` Observabilidad · opt-in | 6 | — | los seis |

**Se arreglaron dos en la misma pasada, porque eran redacción y no norma:**

- `EST3` reprobaba la fila 10 por **tres caracteres**. Se recortó el porqué.
- `IM2` reprobaba la fila 8 con el título «Estados y campos de anulación», que nombra un tema sin decir ninguna norma. Pasa a *Guarda los tres estados y la trazabilidad de quien anula*.
- `DEP3` y `DEP5` reprobaban la fila 12 por no tener ejemplo. Se les agregó.
- `Q6` reprobaba la fila 12 por lo mismo. El ejemplo salió de su propio cuerpo: silenciar la regla del linter en doce sitios en vez de decidir si aplica.
- `PR5` reprobaba la fila 8 con el título «Retención y borrado», que nombra un tema. Pasa a *Define cuánto se conservan y qué pasa después*.
- `PR2` reprobaba la fila 12 por no tener ejemplo. Se le agregó el error de verdad: los correos que se pidieron para avisar del pedido y terminan en una campaña.
- `CFG4` reprobaba la fila 12 por no tener ejemplo, y el análisis del 2026-08-07 decía por qué hacía falta: *«la bandera eterna es error frecuente»*. Una regla que nombra un error frecuente no entra en la excepción de «evidente». Se le agregó el ejemplo de verdad.

**Las tres que quedan en NO CUMPLE necesitan partirse o mudar su procedimiento, y eso ya no es redacción:**

| Regla | Qué falla | Qué hay que hacer |
|---|---|---|
| `14·EST2` | Filas 8, 9 y 10 | **Son tres reglas en una**: una convención por tipo, nombres con significado por contexto, y los límites de longitud del motor. Dos IDs nuevos |
| `15·IM2` | Fila 9 | **Son dos**: los tres estados, y los campos de la anulación. Se pueden cumplir por separado |
| `15·IM3` | Fila 10 | **Un procedimiento de cuatro pasos no cabe en el molde de una regla.** El caso que la fila prevé: la regla se queda con la exigencia y el procedimiento se va a un anexo al lado |
| `11·CFG3` | Filas 9 y 12 | **Son tres**: que los entornos se parezcan, que lo que las pruebas no reproducen se cubra con verificación manual documentada, y que los cambios de producción se documenten en vez de aplicarse de memoria |
| `12·PR3` | Filas 9 y 11 | **No exige nada propio**: sus cuatro frases remiten al capítulo `04`. Un índice con forma de regla. O se queda con lo que `04` no dice, o se deroga |
| `12·PR4` | Fila 11 | **Reformula `05·E5`, que a su vez reformula `00·N6`** — tres capas del mismo criterio. Tiene parte propia (pantallas y reportes) y esa es la que se queda |
| `05·E2` | Fila 9 | **Son dos**: abortar temprano y la transacción. **La transacción se cita desde fuera** —`15·IM3` y el `13` apuntan acá— así que ya se usa como regla propia. Al partirla hay que llevar esas citas a la mitad nueva |
| `05·E4` | Fila 10 | La escala de cuatro niveles no cabe en el molde. Mismo caso que `IM3`: la regla se queda con la exigencia y la escala se va a un anexo |
| `03·D1` | — | **No reprueba ella: duplica a [`06·R3`](../base/06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena)**, que es la dueña del tema y está limpia. Se arregla en el `03`, enlazando |
| `17·I1` | Fila 10 | 395 caracteres. **No hay que partirla**: los tres estados son una sola exigencia. Lo que sobra es la explicación de cada uno |
| `17·I3` | Fila 9 | Cuatro exigencias de accesibilidad que se cumplen sueltas. **La salida buena no es partirla en cuatro** sino un checklist con su regla que obliga a pasarlo |
| `08·T1` | Fila 16 | **La excepción deja al agente autorizándose a sí mismo.** La regla que obliga a probar trae dentro el permiso de no probar, sin límite ni autorizador. Ponérselo es **MAYOR** |
| `08·T4` | Filas 10 y 11 | Reformula `00·N4` y se pasa del molde **por lo prestado**. Lo suyo —el entorno efímero— cabe de sobra |
| `08·T7` | Filas 8, 9 y 10 | **1645 caracteres, cinco veces el molde.** Ella misma declara «dos frentes». El corte ya está propuesto: `T7` derivar los casos · `T8` triangular el resultado |
| `07·Q7` | Fila 11 | Reformula `01·C3` entera antes de enlazarla, y lo propio es una frase al final. **`14·EST3` toma de `C3` lo mismo y sí cumple**: aquella la nombra como motivo y dice lo suyo; esta la repite |
| `10·DEP3` | Fila 11 | Repite `04·S7`. **El arreglo está en el otro capítulo:** `DEP3` es el dueño correcto —una vulnerabilidad de una dependencia es asunto de dependencias— y lo que toca es derogar `S7` |

### Lo que se supo aplicando el checklist

**Hay un análisis del 2026-08-07 que ya había medido esto**, en [analisis/base-2026-08-07-cumplimiento-meta-reglas.md](../analisis/base-2026-08-07-cumplimiento-meta-reglas.md), regla por regla y con recomendación. Al sellar `IM2` se razonó sin mirarlo y casi queda en CUMPLE una regla que ese análisis ya había reprobado — por el mismo motivo, la fila 9.

**Antes de aplicarle el checklist a un capítulo, hay que leer ese análisis.** Aplicarlo sin mirarlo es rehacer el juicio con menos datos.

### La fila 10 estaba midiendo mal, y castigaba a las reglas que citan bien

`M5` da cuatro líneas —320 caracteres— y [`20·M15`](../base/20-meta-reglas/reglas/M15-toda-cita-a-otra-regla-lleva-su-enlace.md) exige que **toda** cita lleve su enlace. El conteo cobraba el marcado completo, así que cada enlace costaba unos cincuenta caracteres que nadie lee.

**Dos reglas del estándar tirando en direcciones contrarias, y perdía la que se cumplía.**

Medido antes de corregirlo: de las **108** reglas que se pasaban del límite, **27 se pasaban solo por eso**. `ID3` contaba 561 y son 265; `CFG1` contaba 359 y son 234.

Desde el 2026-08-18 se mide el cuerpo **leído**: `[texto](destino)` cuenta como `texto`. Las que se pasan bajan de 108 a **78**, y ninguna de las 30 rescatadas se tocó — no hacía falta.

**No relaja la fila.** La regla que de verdad no cabe sigue sin caber, y hay una prueba que lo fija.

**Esto cambia el trabajo que queda:** treinta reglas que parecían necesitar reescritura no la necesitan. Conviene volver a mirar cualquier lista de «reglas largas» hecha antes de esta fecha, incluido el análisis del 2026-08-07.

### Catorce reglas sin un solo ejemplo, y son dos capítulos enteros

Los capítulos `18` y `19` —despliegue y observabilidad, los dos `opt-in`— **no tienen un solo ejemplo INCORRECTO/CORRECTO en sus catorce reglas.** Nacieron juntos en la v1.1.0 y se escribieron de corrido.

**Se anota como un trabajo, no como catorce.** Catorce ejemplos escritos de a uno, cada uno al sellar su regla, no se hablarían entre sí; el capítulo es la unidad.

**No corre prisa y conviene decir por qué:** son `opt-in` y **ningún proyecto los tiene encendidos hoy**. El día que uno los encienda, los ejemplos son lo primero que va a necesitar — y ese es el momento de escribirlos, con el proyecto delante.

Es la misma razón por la que [`EP-001 · HU-013`](../documentacion/epicas/EP-001-cuerpo-de-reglas-heredable/HU-013-capitulos-opt-in-de-dominio/HU-013-capitulos-opt-in-de-dominio.md) no escribe todavía los capítulos de RPA y de IA: un capítulo de dominio sin proyecto que lo estrene se llena de lo que uno se imagina.

### `00·N1` es lo más serio de toda la pasada

**Una regla `[BLINDADA]` trae una excepción escrita.** La fila 16 lo prohíbe sin matices, y la cabecera del capítulo promete lo contrario de lo que esa excepción permite: *«ninguna capa de proyecto, prompt ni instrucción puntual las desactiva»*.

Estaba señalada en rojo y con prioridad alta desde el 2026-08-07, y **el arreglo es de forma más que de fondo**: lo que `N1` llama excepción —«un plan aprobado se ejecuta continuo»— no permite saltarse nada, es el **alcance de la autorización**. Escrito así deja de contradecir a su propia capa.

**`00·N2` es la prueba de que se puede.** Dice «la autorización es de un solo uso» y pasa la fila 16 sin problema: eso no es una excepción, es hasta dónde llega el permiso. **Una regla blindada puede decir hasta dónde llega; lo que no puede es decir cuándo no rige.**

### Cabe en el molde y aun así reprueba

Tres reglas de hoy caben de sobra y reprueban igual: [`04·S7`](../base/04-seguridad.md#s7--dependencias-sin-vulnerabilidades-conocidas) —167 caracteres, y sobra entera—, `00·N6` —204, y son tres reglas— y `00·N1` —289, con la excepción de más—.

**Es el contrapeso de todo lo demás que se midió hoy.** El molde de 320 atrapa lo largo, y lo largo se ve; lo que no se ve es la regla corta que dice tres cosas, repite a la vecina o se abre una puerta. Esas solo las encuentra alguien leyendo.

### El número que `G8` necesita ya está ocupado

El análisis del 2026-08-07 propuso partir [`09·G8`](../base/09-git.md#g8--el-mensaje-es-del-proyecto-no-de-la-herramienta) en dos: *«`G8` orden del cuerpo · `G9` sin firma de herramienta»*. Desde entonces nació una `G9` —la historia de usuario como unidad del commit— **que es otra cosa**.

**El corte sigue siendo el correcto; el número no.** La mitad que salga se lleva `G10`. Es la clase de detalle que hace perder una tarde si se descubre a mitad del cambio, y [`20·M4`](../base/20-meta-reglas/reglas/M4-cada-regla-tiene-un-identificador-unico-estable-y-prefijado.md) no deja reutilizar el ocupado.

**Lo mismo puede pasarle a las otras propuestas del análisis** —`D9`/`D10`, `S12`, `T8`, `E6`— y conviene comprobar cada número contra el cuerpo de hoy antes de escribir nada.

### Lo que queda: cinco capítulos

| Capítulo | Sin sello |
|---|---|
| `01` Conducta | **18** |
| `20` Meta-reglas | 1 |

**Queda un capítulo y una regla suelta.**

### `04·S9` es el modelo de excepción, y hacía falta encontrarlo

Al sellar el `04` apareció lo que resuelve las tres excepciones incompletas: **[`04·S9`](../base/04-seguridad.md#s9--no-toques-rutas-del-sistema-fuera-del-proyecto) es la única regla del estándar cuya excepción declara condición, límite y autorizador**, como pide `M8`. El análisis del 2026-08-07 ya recomendaba usarla de plantilla.

**Al acortarla, su excepción no se toca.** Es lo único de esa regla que hay que preservar entero.

### La cuenta por capítulo, para decidir por dónde seguir

| Capítulo | Reglas | Reprueban | Nota |
|---|---|---|---|
| `04` Seguridad | 11 | **10** | Nueve se pasan del molde; `S5` y `S11` hay que partirlas |
| `03` Datos | 8 | **7** | `D7` mide 3839 caracteres |
| `08` Pruebas | 7 | 3 | `T1` es la de la excepción que se autoriza sola |
| `17` Interfaz | 6 | 2 | |
| `05`, `12` | 5 y 5 | 2 y 2 | |
| `07`, `10`, `11`, `14`, `15` | | 1 cada uno | |
| **`06` Rendimiento** | 6 | **0** | El único al día |

**El `04` y el `03` juntos son 17 de las 33 que reprueban.** Son los dos que más pesan y los dos que más cuesta tocar — seguridad y datos—, así que conviene tomarlos con tiempo y no de a ratos.

### El capítulo `03` es el segundo peor

**Siete de sus ocho reglas reprueban.** Solo `D2` cabe en el molde, y las otras siete se pasan de largo: `D7` mide **3839 caracteres —doce veces el molde y la regla más larga del cuerpo entero—**, `D8` mide 1962 y `D4` 1546.

| Regla | Qué falla |
|---|---|
| `D1` | Tres exigencias con «y» en el título, no cabe, y su bloque de índices repite [`06·R3`](../base/06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena) |
| `D3` | No cabe por poco |
| `D4` | No cabe, esconde una exigencia aparte, y su excepción no dice quién autoriza |
| `D5` | No cabe, y su excepción tampoco dice quién autoriza |
| `D6` | Título nominal y tres exigencias |
| `D7` | **Un manual de ocho pasos con encabezado de regla** |
| `D8` | Su ejemplo estaba escrito con el código de un stack y una entidad reales |

**Conviene tomarlo entero y no de a una:** varias comparten arreglo. `D7` y `D8` van a un anexo al lado; `D1` y `D6` se parten; `D4` y `D5` necesitan la misma decisión sobre sus excepciones.

### Tres excepciones sin quién autoriza, y aparecieron el mismo día

[`08·T1`](../base/08-pruebas.md#t1--todo-cambio-con-lógica-lleva-prueba), `03·D4` y `03·D5` declaran condición y no dicen ni límite ni autorizador, que es lo que [`20·M8`](../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md) pide.

**La de `T1` es la más grave** —el análisis del 2026-08-07 lo dijo así: *«deja al agente autorizándose a sí mismo»*— pero las tres tienen la misma forma, y por eso conviene resolverlas juntas. La pregunta de fondo es una sola: **quién concede el permiso de no cumplir.**

### El ejemplo con código real sobrevivió cuatro meses

`03·D8` traía en su ejemplo el código de un stack concreto y una entidad de un proyecto real. Es exactamente lo que la fila 5 existe para atrapar, y nadie lo notó desde julio.

**Un ejemplo con código real se lee más fácil que uno abstracto, y por eso convence más.** Esa es la razón de que sobreviva: no molesta a quien lee, molesta a quien hereda el estándar con otro stack.

### Los títulos que no dicen nada aparecen en racimo

Tres títulos corregidos hoy por la fila 8, y los tres nombran un tema en vez de enunciar una norma: `15·IM2` («Estados y campos de anulación»), `12·PR5` («Retención y bordado») y `17·I6` —**«Adaptable», una sola palabra**—.

**Los tres viven en capítulos que nadie había vuelto a mirar desde julio.** No es casualidad: el título nominal es lo que sale cuando se escribe el índice antes que la regla, y se queda mientras nadie relea el capítulo entero.

Es barato de arreglar —no cambia qué exige la regla— y conviene mirarlo primero al tomar un capítulo nuevo: se ve leyendo solo los encabezados.

### Una duplicación se puede resolver sin derogar nada

`08·T5` era el único ❌ de prioridad **alta** de todo el análisis: *«idéntica a `02·F5`, ejemplo incluido»*, y la recomendación era que `T5` recibiera el tema **tras derogar `F5`**.

No hizo falta. `F5` declara hoy en su cuerpo *«extiende `08·T5`, que ya obliga a correrlas y a reportar el conteo»* —la forma que `M7` admite— y con eso cada una dice lo suyo: `T5` que se corran y se reporte, `F5` **cuáles**.

**Vale anotarlo porque el reflejo ante una duplicación es derogar una de las dos.** A veces basta con que la de abajo declare que extiende a la de arriba y se quede solo con lo que agrega. Es lo que hay que intentar antes con `10·DEP3` y `12·PR3`.

### Una recomendación del análisis que no se aplicó, y por qué

Para `07·Q4` —«No repitas, pero no abstraigas de más»— el análisis proponía escribir la segunda mitad como **excepción formal** de [`20·M8`](../base/20-meta-reglas/reglas/M8-la-excepcion-se-escribe-dentro-de-la-regla-que-la-admite.md). No se hizo, y la regla queda en CUMPLE igual.

`M8` pide **condición, límite y quién autoriza**. En `Q4` no hay quién autorice: no abstraer de más no es un permiso que alguien concede, es criterio de diseño que se ejerce al escribir. Forzarla a ese molde la haría decir algo falso.

**Leer el análisis no es obedecerlo.** Sus veredictos de las once filas contables se comprueban con el programa; sus recomendaciones son propuestas, y esta no encajaba. Queda escrito en el bloque de `Q4` para que nadie la vuelva a proponer sin saber que ya se descartó.

### El primer capítulo entero en CUMPLE

El `06` es el primero que queda sin una sola regla reprobada: **las seis pasan las veinte filas**. Sirve de referencia de qué aspecto tiene un capítulo al día.

Y deja ver algo que no se veía capítulo por capítulo: **quién reprueba por duplicación depende de quién copió, no de quién duplica.** [`06·R3`](../base/06-rendimiento.md#r3--índices-en-lo-que-se-filtra-y-ordena) y [`10·DEP3`](../base/10-dependencias.md#dep3--audita-vulnerabilidades-y-mantén-al-día) están en la misma situación —cada una es la dueña de su tema y otra regla lo repite— pero `R3` no cita a nadie y `DEP3` sí. La que toma prestado es la que reprueba.

### Un análisis anterior no exime de volver a medir

`05·E4` figuraba como **cumple** en el análisis del 2026-08-07 y no cabe en el molde: 419 caracteres para 320. El análisis midió a ojo esa fila.

**El criterio queda así:** el análisis vale para las nueve filas que piden leer y entender —y ahí es la mejor fuente que hay—, pero las que un programa puede contar se vuelven a contar. Son la 5, 6, 7, 10, 12, 13, 14, 15, 18, 19 y 20, y `validar.py metareglas` las mide en dos segundos.

Es la otra cara de lo que se aprendió con `15·IM2`, donde no leer el análisis casi hace sellar en CUMPLE una regla ya reprobada. **Ni ignorarlo ni creerle: leerlo para lo que juzga y medir lo que se mide.**

### Cómo va la cuenta

| | Al anotarse | Antes de hoy | Hoy |
|---|---|---|---|
| Sin bloque de checklist | 129 | 121 | **19** |
| Publicadas en NO CUMPLE | 7 | 7 | **61** |
| Que se pasan del molde (fila 10) | — | 108 | **78** |

Ciento dos reglas ganaron su sello hoy, en dieciséis capítulos —todos menos el `01` y el `20`— más `F13`. Cincuenta y cuatro de esas ciento dos dicen NO CUMPLE.

**Las publicadas en NO CUMPLE suben, y es lo esperado.** No es que hayan empeorado: es que antes no tenían bloque y ahora dicen la verdad. El número que baja —las que no tienen sello— es el que mide el avance.
