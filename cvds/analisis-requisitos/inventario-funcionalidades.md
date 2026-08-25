# Inventario de funcionalidades — Estándar de trabajo heredable   ·   `[CAPA 3]`

**Para qué sirve este documento.** Es el alcance completo, ítem por ítem: todo lo que el producto debe tener, esté construido o no. Aprobado por el usuario, es la puerta de las épicas ([`02·F26`](../../base/02-flujo-de-trabajo/reglas/F26-el-inventario-de-funcionalidades-aprobado-es-la-puerta-de-las-epicas.md)).

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md). Sale de los catorce requisitos funcionales de [cvds/analisis-requisitos/README.md](README.md), no del repositorio. Por eso todas las fichas dicen «Definida» y «Sin verificar»: el estado que se escribe es el del alcance acordado, no el del código que ya existe.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz). Con esta aprobación se abre la puerta de las épicas.

## Las tres clases

| Clase | Qué significa |
|---|---|
| **Obligatoria** | Sin esto el producto no sirve para lo que se hizo |
| **Complementaria** | Suma valor, pero el producto arranca sin ella |
| **Futura** | Se sabe que se quiere, y se decidió que no ahora |

## Resumen

Una línea por funcionalidad, para verlas todas juntas. El detalle de cada una está en su ficha, más abajo.

| ID | Funcionalidad | Clase | Parte del sistema | Prioridad | Estado | Verificado |
|---|---|---|---|---|---|---|
| F-001 | Las reglas se cargan al abrir la sesión | Obligatoria | Cargador de sesión | Alta | Definida | Sin verificar |
| F-002 | Nada cambia de estado sin que el usuario lo autorice | Obligatoria | Enganches | Alta | Definida | Sin verificar |
| F-003 | Lo escrito se comprueba solo | Obligatoria | Comprobaciones | Alta | Definida | Sin verificar |
| F-004 | Lo que no tiene prueba se declara sin verificar | Obligatoria | Comprobaciones | Alta | Definida | Sin verificar |
| F-005 | El estándar se instala en otro proyecto | Obligatoria | Instalador | Alta | Definida | Sin verificar |
| F-006 | El proyecto se entera de que quedó atrás | Complementaria | Instalador | Media | Definida | Sin verificar |
| F-007 | Lo que la sesión deja se escribe fuera del chat | Obligatoria | Enganches | Alta | Definida | Sin verificar |
| F-008 | Ninguna credencial queda escrita | Obligatoria | Enganches | Alta | Definida | Sin verificar |
| F-009 | El documento del ciclo se exige mientras se construye | Obligatoria | Moldes del ciclo | Alta | Definida | Sin verificar |
| F-010 | El entregable de ofimática se genera desde el `.md` | Complementaria | Generador de entregables | Media | Definida | Sin verificar |
| F-011 | Se mide el tiempo que el usuario gasta revisando | Futura | Comprobaciones | Baja | Definida | Sin verificar |
| F-012 | Se ve desde una pantalla lo que hay y lo que el agente guardó | Complementaria | Interfaz local | Media | Definida | Sin verificar |
| F-013 | Lo aprendido se guarda y se recupera en otra sesión | Obligatoria | Memoria | Alta | Definida | Sin verificar |
| F-014 | Un componente nuevo no rompe lo que ya servía | Obligatoria | Comprobaciones | Alta | Definida | Sin verificar |

**Cuenta:** 10 obligatorias, 3 complementarias y 1 futura, de 14. Y aparte: 0 implementadas, 0 verificadas.

## Las funcionalidades, una por una

### Las reglas se cargan al abrir la sesión

| Campo | Valor |
|---|---|
| **Identificador** | `F-001` |
| **De qué se trata** | Al abrir una sesión de trabajo, el agente recibe las reglas del proyecto sin que nadie se las pida |
| **Para qué sirve** | Que lo acordado una vez siga valiendo, en vez de volver a explicarlo cada vez |
| **Parte del sistema** | Cargador de sesión |
| **Quién la usa** | El usuario, sin hacer nada: ocurre sola al abrir |
| **Qué recibe** | El evento de apertura de la sesión, y la ruta donde viven las reglas |
| **Qué entrega** | Las reglas cargadas, y un aviso que dice qué versión rige |
| **Reglas que debe respetar** | `RN-1` lo que se acuerda vive en el repositorio, no en el chat |
| **Depende de** | Ninguna |
| **Terminada cuando** | `CA-1` al abrir, las reglas están cargadas sin que nadie las pida · `CA-2` si no las encuentra, lo dice con la ruta que buscó y la sesión sigue · `CA-3` cargar no demora la apertura más de dos segundos |
| **Qué necesita construirse** | Tarea que corre sola al abrir, y lectura de archivos |
| **Prioridad** | Alta: sin esto, ninguna otra funcionalidad tiene efecto |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Que el agente las reciba no garantiza que las obedezca: eso lo cubre F-003 |

### Nada cambia de estado sin que el usuario lo autorice

| Campo | Valor |
|---|---|
| **Identificador** | `F-002` |
| **De qué se trata** | Toda acción que cambia archivos, datos o el repositorio se anuncia y espera aprobación |
| **Para qué sirve** | Que no aparezcan cambios que el usuario no pidió |
| **Parte del sistema** | Enganches |
| **Quién la usa** | El usuario, que aprueba o rechaza |
| **Qué recibe** | La acción que el agente va a ejecutar, antes de ejecutarla |
| **Qué entrega** | La acción ejecutada, o detenida con el motivo |
| **Reglas que debe respetar** | `RN-2` ningún cambio de estado sin aprobación explícita · `RN-3` lo que no se puede deshacer se aprueba una por una, aunque estuviera en un plan aprobado |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` una acción que borra sin aprobación queda detenida · `CA-2` la aprobación de un plan no cubre lo irreversible · `CA-3` lo que se hizo queda dicho en el reporte |
| **Qué necesita construirse** | Tarea que corre sola antes de cada acción |
| **Prioridad** | Alta: es lo que sostiene la confianza en delegar |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Pedir aprobación por todo, hasta por lo trivial, hace que se apruebe en bloque, y entonces también se aprueba lo grave |

### Lo escrito se comprueba solo

| Campo | Valor |
|---|---|
| **Identificador** | `F-003` |
| **De qué se trata** | Programas que leen lo entregado y dicen si cumple las reglas, sin opinar ni corregir |
| **Para qué sirve** | Que el cumplimiento no dependa de que el agente se acuerde |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El usuario, y el propio agente antes de entregar |
| **Qué recibe** | Los archivos del proyecto, y qué regla comprobar |
| **Qué entrega** | Lo que cumple, lo que no, y en qué línea |
| **Reglas que debe respetar** | `RN-4` no se afirma sobre lo que no se leyó |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` un documento que cumple pasa · `CA-2` uno que no cumple es rechazado, con el archivo y la línea · `CA-3` apuntada a una carpeta que no es la suya, lo dice en vez de dar veredicto |
| **Qué necesita construirse** | Lógica que corre en la máquina, sin servicio ni red |
| **Prioridad** | Alta: es lo que convierte una regla escrita en una regla vigente |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Una comprobación que reprueba de más se apaga a la semana, y entonces no queda nada vigilando |

### Lo que no tiene prueba se declara sin verificar

| Campo | Valor |
|---|---|
| **Identificador** | `F-004` |
| **De qué se trata** | El estado de una funcionalidad lo fija la prueba corrida, no la lectura del código |
| **Para qué sirve** | Que no se entregue como terminado lo que nadie comprobó |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El usuario, al leer qué está hecho de verdad |
| **Qué recibe** | El cierre de una unidad de trabajo, con sus pruebas y su evidencia |
| **Qué entrega** | El veredicto por criterio: cumple, no cumple o sin verificar |
| **Reglas que debe respetar** | `RN-5` la prueba corrida manda sobre la lectura |
| **Depende de** | F-003 |
| **Terminada cuando** | `CA-1` con prueba y evidencia, queda verificado · `CA-2` sin prueba, queda «sin verificar» y no se puede cerrar · `CA-3` con prueba fallida, queda «no cumple» con lo que falló |
| **Qué necesita construirse** | Lógica que corre en la máquina |
| **Prioridad** | Alta |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | «Sin verificar» tiene que ser una respuesta aceptable, o se falsean las pruebas para poder cerrar |

### El estándar se instala en otro proyecto

| Campo | Valor |
|---|---|
| **Identificador** | `F-005` |
| **De qué se trata** | Un programa lleva las reglas a un proyecto ajeno y anota qué versión adoptó |
| **Para qué sirve** | Que un proyecto nuevo no empiece de cero |
| **Parte del sistema** | Instalador |
| **Quién la usa** | Quien instala, con la aprobación de quien manda en ese proyecto |
| **Qué recibe** | La ruta del proyecto que va a heredar |
| **Qué entrega** | Los archivos agregados, el enganche puesto y la versión adoptada anotada |
| **Reglas que debe respetar** | `RN-2` nada se instala sin aprobación · `RN-6` no se pisa nada de lo que el proyecto ya tenía |
| **Depende de** | F-001, F-003 |
| **Terminada cuando** | `CA-1` en un proyecto vacío, queda funcionando · `CA-2` en uno con archivos propios, no sobrescribe: avisa y se detiene · `CA-3` la versión adoptada queda escrita y existe de verdad |
| **Qué necesita construirse** | Lógica que corre en la máquina, y escritura de archivos |
| **Prioridad** | Alta: es lo que separa un estándar de una preferencia personal |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Lo que demuestra que sirve no es que instale, es que alguien ajeno lo instale siguiendo solo el manual |

### El proyecto se entera de que quedó atrás

| Campo | Valor |
|---|---|
| **Identificador** | `F-006` |
| **De qué se trata** | Al abrir sesión, un proyecto que adoptó una versión vieja recibe el aviso y qué cambió |
| **Para qué sirve** | Que nadie siga una versión vieja sin saberlo |
| **Parte del sistema** | Instalador |
| **Quién la usa** | Quien trabaja en el proyecto que heredó |
| **Qué recibe** | La versión adoptada por ese proyecto y la publicada |
| **Qué entrega** | El aviso con la distancia entre las dos, empezando por lo que obliga a rehacer algo |
| **Reglas que debe respetar** | `RN-7` avisar no es actualizar: ponerse al día lo decide el proyecto |
| **Depende de** | F-005 |
| **Terminada cuando** | `CA-1` con versión anterior, avisa y dice qué cambió · `CA-2` con la misma, no molesta · `CA-3` con un número que no existe, lo dice en vez de concluir que va adelantado |
| **Qué necesita construirse** | Tarea que corre sola al abrir |
| **Prioridad** | Media: el estándar sirve sin esto, pero se desactualiza en silencio |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Un aviso que aparece siempre se vuelve ruido y se ignora |

### Lo que la sesión deja se escribe fuera del chat

| Campo | Valor |
|---|---|
| **Identificador** | `F-007` |
| **De qué se trata** | Lo hablado, lo decidido y lo aprendido en una sesión quedan en archivos del repositorio |
| **Para qué sirve** | Saber qué pasó sin releer el trabajo entero, y que la sesión siguiente lo herede |
| **Parte del sistema** | Enganches |
| **Quién la usa** | El usuario, y el agente de la sesión siguiente |
| **Qué recibe** | Cada mensaje del usuario y cada respuesta del agente, con la hora de la máquina |
| **Qué entrega** | El registro de la sesión, su resumen, las señales y los recuerdos, cada uno en su archivo |
| **Reglas que debe respetar** | `RN-1` lo que se acuerda vive en el repositorio · `RN-8` el registro no se reescribe: es lo que se dijo |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` una sesión de un solo mensaje queda registrada · `CA-2` una interrumpida conserva lo que alcanzó a escribirse · `CA-3` lo que quedó se puede leer sin el chat |
| **Qué necesita construirse** | Tarea que corre sola, y escritura de archivos |
| **Prioridad** | Alta |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | El registro literal y el resumen son cosas distintas: mezclarlos hace que ninguno sirva |

### Ninguna credencial queda escrita

| Campo | Valor |
|---|---|
| **Identificador** | `F-008` |
| **De qué se trata** | Toda clave que aparezca se tapa antes de que quede guardada en cualquier archivo |
| **Para qué sirve** | Que una clave pegada en el chat no quede para siempre en el repositorio |
| **Parte del sistema** | Enganches |
| **Quién la usa** | El usuario, sin hacer nada |
| **Qué recibe** | El texto que se va a escribir, antes de escribirlo |
| **Qué entrega** | El mismo texto con la clave tapada y el nombre de la variable intacto |
| **Reglas que debe respetar** | `RN-9` una credencial no se escribe, no se registra y no se guarda |
| **Depende de** | F-001 |
| **Terminada cuando** | `CA-1` una clave entre comillas queda tapada · `CA-2` una tecleada sin comillas también · `CA-3` una palabra que solo parece clave, como el nombre de una variable en un fragmento de programa, queda tal cual |
| **Qué necesita construirse** | Tarea que corre sola antes de guardar |
| **Prioridad** | Alta: es el único daño de esta lista que no se puede deshacer |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Tapar de más daña el registro; hay que medirlo sobre lo ya guardado antes de dejarlo corriendo |

### El documento del ciclo se exige mientras se construye

| Campo | Valor |
|---|---|
| **Identificador** | `F-009` |
| **De qué se trata** | Cada etapa tiene su documento modelo, y el trabajo no avanza sin el que le toca |
| **Para qué sirve** | Que quede documentación sin esperar al final a redactarla de memoria |
| **Parte del sistema** | Moldes del ciclo |
| **Quién la usa** | El usuario, que recibe lo construido con su explicación |
| **Qué recibe** | La unidad de trabajo que se abre o se cierra |
| **Qué entrega** | El documento que corresponde, y el rechazo si falta |
| **Reglas que debe respetar** | `RN-10` sin especificación acordada no hay código · `RN-11` lo que no aplica se escribe «no aplica» con su porqué, nunca en blanco |
| **Depende de** | F-003 |
| **Terminada cuando** | `CA-1` abrir trabajo sin su documento queda detenido · `CA-2` un documento con espacios sin llenar no se da por entregado · `CA-3` el molde sirve para cualquier proyecto, sin nombrar tecnología |
| **Qué necesita construirse** | Archivos modelo, y lógica que comprueba |
| **Prioridad** | Alta |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Exigir demasiado documento por unidad pequeña hace que se llene por cumplir, y entonces no dice nada |

### El entregable de ofimática se genera desde el `.md`

| Campo | Valor |
|---|---|
| **Identificador** | `F-010` |
| **De qué se trata** | Los documentos del ciclo, escritos en texto, se convierten en `.docx` para entregar |
| **Para qué sirve** | Entregar en el formato que el cliente espera sin mantener dos versiones del mismo texto |
| **Parte del sistema** | Generador de entregables |
| **Quién la usa** | El usuario, y quien reciba el proyecto |
| **Qué recibe** | Los `.md` del ciclo, con la distribución de las plantillas |
| **Qué entrega** | El `.docx` de cada documento, generado, nunca escrito a mano |
| **Reglas que debe respetar** | `RN-12` el `.md` es la fuente y el `.docx` una salida: una salida no se edita |
| **Depende de** | F-009 |
| **Terminada cuando** | `CA-1` un documento completo se genera con todas sus secciones · `CA-2` uno con espacios sin llenar avisa antes de generar · `CA-3` regenerar dos veces da el mismo resultado |
| **Qué necesita construirse** | Lógica que corre en la máquina, y pantalla desde donde pedirlo |
| **Prioridad** | Media: el proyecto funciona sin esto, pero no se puede entregar a un tercero |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Falta decidir si el `.docx` conserva la numeración del `.md` o la que pida el cliente. Es la pregunta P-1 |

### Se mide el tiempo que el usuario gasta revisando

| Campo | Valor |
|---|---|
| **Identificador** | `F-011` |
| **De qué se trata** | Registrar cuánto tiempo dedica el usuario a revisar lo entregado, antes y después del estándar |
| **Para qué sirve** | Saber si el proyecto cumplió su objetivo principal, en vez de suponerlo |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El usuario |
| **Qué recibe** | Lo que dura cada revisión, y cuántas correcciones se repiten |
| **Qué entrega** | La comparación entre el antes y el después |
| **Reglas que debe respetar** | `RN-13` medir no puede volverse más caro que lo que ahorra |
| **Depende de** | F-003, F-007 |
| **Terminada cuando** | `CA-1` hay una medición inicial contra la cual comparar · `CA-2` la medición no exige que el usuario anote nada a mano |
| **Qué necesita construirse** | Lógica que corre en la máquina |
| **Prioridad** | Baja: es lo último, y sin línea base inicial pierde la mitad de su valor |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | La línea base debió tomarse antes de empezar y no se tomó. Está declarado como deuda en la etapa de implementación |

### Se ve desde una pantalla lo que hay y lo que el agente guardó

| Campo | Valor |
|---|---|
| **Identificador** | `F-012` |
| **De qué se trata** | Una pantalla local que lista los documentos del ciclo, los muestra, y deja ver lo que el agente guardó en la memoria |
| **Para qué sirve** | Revisar sin abrir archivo por archivo, que es la forma en que hoy se revisa |
| **Parte del sistema** | Interfaz local |
| **Quién la usa** | El usuario |
| **Qué recibe** | Los archivos del proyecto y lo guardado en la memoria |
| **Qué entrega** | Lo que hay, en pantalla, y el `.docx` de cada documento cuando se pide |
| **Reglas que debe respetar** | `RN-14` la pantalla solo lee: lo que cambia el estado del proyecto no se hace desde ahí |
| **Depende de** | F-009, F-013 |
| **Terminada cuando** | `CA-1` lista los documentos del ciclo y los muestra · `CA-2` sin memoria disponible, muestra los documentos y avisa qué falta · `CA-3` un documento borrado del disco se reporta, no se muestra vacío · `CA-4` corre en la máquina, sin salir a la red |
| **Qué necesita construirse** | Pantalla, lógica del servidor local y almacenamiento |
| **Prioridad** | Media: el sistema funciona sin ella, pero revisar sigue costando lo mismo |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Es el componente que más puede crecer, y el que más fácil se lleva por delante a los otros. Por eso solo lee |

### Lo aprendido se guarda y se recupera en otra sesión

| Campo | Valor |
|---|---|
| **Identificador** | `F-013` |
| **De qué se trata** | Lo que se decide, se corrige o se descubre queda guardado, y la sesión siguiente lo encuentra |
| **Para qué sirve** | Que el agente no arranque en blanco cada vez, y que la corrección no se repita |
| **Parte del sistema** | Memoria |
| **Quién la usa** | El agente al abrir; el usuario cuando quiere consultar |
| **Qué recibe** | Lo que la sesión dejó: decisiones, correcciones y señales |
| **Qué entrega** | Lo guardado, buscable, y con la fecha en que se escribió |
| **Reglas que debe respetar** | `RN-1` vive en el repositorio, no en el almacén de la herramienta · `RN-9` nada de lo guardado incluye credenciales |
| **Depende de** | F-007 |
| **Terminada cuando** | `CA-1` lo guardado en una sesión se recupera en la siguiente · `CA-2` lo que dejó de ser cierto se corrige y la corrección queda · `CA-3` si no hay nada guardado del tema, lo dice en vez de inventar |
| **Qué necesita construirse** | Almacenamiento de datos y lógica que corre en la máquina |
| **Prioridad** | Alta: es la mitad del problema original |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Buscar por parecido y no por palabra exacta es la candidata C-2, y hoy choca con la restricción de correr sin dependencias de terceros |

### Un componente nuevo no rompe lo que ya servía

| Campo | Valor |
|---|---|
| **Identificador** | `F-014` |
| **De qué se trata** | Antes de publicar, se vuelve a comprobar lo que ya funcionaba |
| **Para qué sirve** | Que el sistema pueda crecer sin que cada componente nuevo se lleve por delante lo anterior |
| **Parte del sistema** | Comprobaciones |
| **Quién la usa** | El autor, al publicar; los proyectos que heredan, al actualizar |
| **Qué recibe** | La versión que se va a publicar |
| **Qué entrega** | Qué sigue sirviendo, qué se rompió, y qué obliga a rehacer algo |
| **Reglas que debe respetar** | `RN-5` lo dice la prueba corrida, no la lectura · `RN-15` lo que obliga a rehacer algo se declara antes de publicar, nunca después |
| **Depende de** | F-003 |
| **Terminada cuando** | `CA-1` una versión que rompe algo no se publica · `CA-2` una que obliga a rehacer algo lo declara · `CA-3` una que no rompe nada pasa sin trabajo manual |
| **Qué necesita construirse** | Lógica que corre en la máquina |
| **Prioridad** | Alta: es lo que permite crecer sin miedo |
| **Estado** | Definida |
| **Verificado** | Sin verificar |
| **Lo que hay que tener en cuenta** | Solo puede comprobar lo que tenga prueba: lo que nunca se probó no se sabe si se rompió |

## Lo que todavía no se sabe si entra

| # | Funcionalidad candidata | De qué se trata | Estado |
|---|---|---|---|
| C-1 | Que el agente aprenda de lo que el usuario estudia | Alimentar la memoria con lo que el usuario va aprendiendo por fuera del proyecto | **Por confirmar** (P-2) |
| C-2 | Buscar en la memoria por parecido, no por palabra exacta | Encontrar lo escrito aunque se nombre distinto | **Por confirmar** (P-3) |
| C-3 | Que la pantalla también deje editar | Cambiar los documentos desde el visor, y no solo leerlos | **Por confirmar** (P-4) |

## Preguntas: las contesta el usuario

- **P-1 · ¿El `.docx` conserva la numeración del `.md` o la que pida el cliente?** Conservarla es gratis y hace que los dos documentos se puedan citar igual; cambiarla obliga a mantener una tabla de equivalencias. Propuesta del agente: conservarla, y si un cliente exige la suya, se resuelve en ese entregable y no en el generador.
- **P-2 · ¿Entra C-1 al alcance?** Sumarla mete al estándar en terreno de memoria personal, que hoy queda fuera. Propuesta: dejarla como futura hasta que el resto esté verificado.
- **P-3 · ¿Entra C-2 al alcance?** Buscar por parecido pide una dependencia de terceros, y eso choca con la restricción de correr solo con la biblioteca estándar. Propuesta: no entra mientras esa restricción siga vigente.
- **P-4 · ¿Entra C-3 al alcance?** Editar desde la pantalla es cómodo, y rompe `RN-14`: lo que cambia el estado del proyecto pasa por aprobación, y una pantalla que edita se salta ese paso. Propuesta: no entra.

## Qué pasa cuando esto se apruebe

1. El planteamiento se revisa para que diga esto, y no lo que alguien hubiera supuesto antes.
2. El trabajo se parte en bloques a partir de esta lista, y cada bloque dice qué funcionalidades cubre por su ID.
3. Cada «Terminada cuando» se vuelve el criterio de aceptación de su historia, y de ahí salen las pruebas.
4. Cada prueba que salga bien llena su casilla de «Verificado». Ahí, y solo ahí, se sabe qué está hecho.
5. La lista se va volviendo el manual del producto, sin volver a escribirla.
