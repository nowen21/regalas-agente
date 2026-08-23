# Inventario de módulos y su funcionalidades   ·   `[CAPA 3]`

> Plantilla. Se copia a la carpeta de la propuesta del proyecto, se reemplazan los `«…»` y se borra esta caja.
> **Se llena con todo lo que ya se sabe del proyecto, y se escribe como si nada estuviera construido:**
> sin fechas, sin estado de trámite, sin contar qué se preguntó y qué se contestó.
> **La prueba de que quedó bien escrita: un niño la lee y entiende qué hace el producto.**
> Vale para el documento entero: el nombre, la descripción y el objetivo de cada funcionalidad.
> Si para entender algo hay que saber del proyecto, está escrito para adentro y se rehace.
> **Claro no es infantil:** se usan palabras comunes y frases cortas, no se rodea lo que se quiere decir
> ni se explica de más. Se dice qué hace, en el tono con que se le explica algo a un adulto que no es del oficio
> ([`00·ID7`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID7-escribe-para-que-lo-entienda-quien-no-sabe-del-tema.md),
> [`00·ID9`](«RUTA-ESTANDAR»/base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)).
> **Nada de acá nombra un lenguaje, un framework ni una herramienta.** «Necesita pantalla» sí; «necesita React» no.
> Eso vive en la capa del proyecto y en su ficha de tecnología.
> Sin esta lista aprobada por el usuario no se parte el trabajo en bloques
> ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).
> En un proyecto chico son diez fichas: lo que manda es que el usuario la apruebe, no el tamaño.
> Lo que quede acá se replica a todo proyecto que herede el estándar: lo que sobre, sobra en todos.

Esta es la lista completa de lo que «el producto» debe hacer. De acá salen después los bloques de trabajo, las historias, las tareas, las pruebas y el manual: si algo no está en esta lista, no se construye.

## Cómo se lee

**Están todas: las hechas y las que faltan.** Ninguna se saca porque ya exista, porque ya se haya hablado de ella o porque aparezca en otro papel. Esta lista no dice qué falta: dice qué es el producto.

**No dice cuándo ni quién.** Sin fechas, sin quién decidió qué, sin las preguntas que ya se contestaron. Eso se guarda en otros papeles del proyecto. Una pregunta contestada deja de ser pregunta: sube a funcionalidad, o se va.

**Estado y Verificado no son lo mismo, y por eso hay dos casillas.** «Estado» es lo que alguien dice que va pasando. «Verificado» es lo único que prueba que está hecho, y solo lo llena una prueba corrida. Una funcionalidad puede estar «implementada» y **sin verificar**: quiere decir que se construyó y que nadie lo ha demostrado.

**Cada funcionalidad tiene un número que no se repite ni se reutiliza.** Aunque se descarte, su número queda quemado: hay planes, tareas y pruebas que la nombran por ahí.

## Las tres clases

| Clase | Qué quiere decir |
|---|---|
| **Obligatoria** | Sin esto el producto no sirve para lo que se hizo |
| **Complementaria** | Suma valor, pero el producto arranca sin ella |
| **Futura** | Se sabe que se quiere, y se decidió que no ahora |

Lo que **no se sabe todavía si entra** no es una clase: es una pregunta, y vive en su propia sección más abajo.

## Resumen

> Una línea por funcionalidad, para verlas todas juntas. El detalle de cada una está en su ficha. Los valores de «Estado» son cuatro y ninguno más: **Definida**, **En desarrollo**, **Implementada**, **Descartada**.

| ID | Funcionalidad | Clase | Parte del sistema | Prioridad | Estado | Verificado |
|---|---|---|---|---|---|---|
| F-001 | «El nombre, en palabras que cualquiera entienda» | Obligatoria | «Módulo o proceso» | Alta | Definida | Sin verificar |
| F-002 | «…» | «…» | «…» | «…» | «…» | «…» |

**Cuenta:** «cuántas obligatorias, cuántas complementarias, cuántas futuras, de cuántas». Y aparte: «cuántas implementadas, cuántas verificadas». Así se ve de un vistazo el tamaño del alcance y cuánto de él está demostrado.

## Las funcionalidades, una por una

> Una ficha por cada línea del resumen, en el mismo orden. Un campo que no aplique se escribe «no aplica» y se dice por qué en una línea: en blanco no se distingue de olvidado.

### F-001 · «El nombre, en palabras que cualquiera entienda»

| Campo | Qué dice |
|---|---|
| **De qué se trata** | «Qué hace, dicho a quien va a usarlo» |
| **Para qué sirve** | «Qué problema resuelve o qué permite lograr. Si no se puede escribir, la funcionalidad no está justificada» |
| **Parte del sistema** | «El módulo, proceso o componente al que pertenece, tomado de la lista de partes del proyecto» |
| **Quién la usa** | «Los roles que interactúan con ella, y qué hace cada uno. Si es el sistema solo, se dice» |
| **Qué recibe** | «Los datos o eventos que la disparan, y de dónde vienen» |
| **Qué entrega** | «El resultado: lo que se ve, lo que se guarda, lo que se manda» |
| **Reglas que debe respetar** | «Las condiciones del negocio que la gobiernan, numeradas `RN-1`, `RN-2`. Lo que la funcionalidad no puede hacer aunque técnicamente pueda» |
| **Depende de** | «Las funcionalidades que tienen que existir antes, por su ID. `Ninguna` si arranca sola» |
| **Terminada cuando** | «Las condiciones que se comprueban para darla por hecha, numeradas `CA-1`, `CA-2`. Cada una redactada de forma que se pueda responder con sí o no. De acá salen las pruebas» |
| **Qué necesita construirse** | «Pantalla, lógica del servidor, almacenamiento de datos, conexión con un sistema de afuera, tarea que corre sola. Se marca lo que aplique, sin nombrar tecnología» |
| **Prioridad** | «Alta, Media o Baja, y en una línea por qué» |
| **Estado** | «Definida, En desarrollo, Implementada o Descartada» |
| **Verificado** | «Sin verificar», o «✅ «qué prueba», «cuándo»», o «❌ «qué prueba», «cuándo», y qué le falta» |
| **Lo que hay que tener en cuenta** | «Restricciones, riesgos, casos raros y lo que se decidió dejar por fuera. `Ninguna` si no hay» |

### F-002 · «…»

«Se repite la ficha por cada funcionalidad.»

## Lo que todavía no se sabe si entra

> Nada de acá está decidido: cada línea es una de las preguntas de abajo. La duda es si entra o no al producto, nunca si está construido. La que el usuario acepte pasa a funcionalidad con su ficha completa; la que descarte se borra.

| # | Funcionalidad candidata | De qué se trata | Estado |
|---|---|---|---|
| C-1 | «…» | «…» | **Por confirmar** (P-«n») |

## Preguntas: las contesta el usuario

> Solo las que siguen sin respuesta, numeradas `P-1`, `P-2` y las que sigan. Cada una con las opciones y lo que cuesta cada una, y si el agente tiene una favorita, la dice como propuesta. Una pregunta sin contestar detiene solo las funcionalidades que la nombran, no el resto. La contestada se borra de acá: su respuesta ya está en la ficha que subió, o en la candidata que se fue.

- **P-1 · «¿La pregunta, completa?»** «Las opciones, con lo que cuesta cada una. Propuesta del agente: «cuál y por qué».»

## Qué pasa cuando esto se apruebe

1. El papel donde se pidió el proyecto se revisa para que diga esto, y no lo que alguien hubiera supuesto antes.
2. El trabajo se parte en bloques a partir de esta lista, y cada bloque dice qué funcionalidades cubre por su ID ([`02·F26`](«RUTA-ESTANDAR»/base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).
3. Cada «Terminada cuando» se vuelve el criterio de aceptación de su historia, y de ahí salen las pruebas. No se inventan aparte.
4. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
5. La lista se va volviendo el manual del producto, sin volver a escribirla.
