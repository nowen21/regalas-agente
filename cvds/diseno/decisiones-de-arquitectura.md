# Decisiones de arquitectura   ·   `[CAPA 3]`

**Para qué sirve este documento.** Las decisiones que cuestan caro de revertir, cada una con las alternativas que se descartaron y por qué. Sin las alternativas, una decisión no se puede defender ni revisar después: solo se puede obedecer o romper.

> **Escrito desde la propuesta**, igual que el resto de [cvds/](../README.md). Reescrito el 2026-08-24, cuando el producto pasó a ser una plataforma que administra proyectos. Las ocho decisiones anteriores describían un estándar que viajaba dentro de cada proyecto.

**Cómo se citan.** Cada decisión lleva un número que empieza por `DA`, de **decisión de arquitectura**: `DA-01`, `DA-02`. Ese número se usa para nombrarla en cualquier otro documento, y no se le da a otra decisión aunque esta se cambie después.

**Estado: APROBADO** (2026-08-24, por Ing. José Dúmar Jiménez Ruíz).

---

## Decisiones

### La fuente es texto versionado, y la base es un índice

| Campo | Valor |
|---|---|
| **Identificador** | `DA-01` |
| **Qué se decide** | Todo lo que la plataforma guarda se escribe como texto en el repositorio. La base de datos solo guarda lo que hace falta para buscar, y se puede reconstruir desde el texto |
| **Qué exige** | RNF-04, RN-7 |
| **Alternativas descartadas** | Guardar todo en la base y respaldarla con volcados periódicos, porque el respaldo siempre iría un paso atrás del último cambio y habría que resolver el orden, el tamaño y los conflictos. Guardar solo en texto y buscar leyendo archivos, porque con miles de anotaciones cada búsqueda leería el disco entero |
| **Por qué esta** | El respaldo pasa a ser el propio repositorio: si se pierde la máquina, se clona y se reconstruye el índice. Y lo guardado se puede leer sin la plataforma |
| **Qué se pierde** | Consultas que no se puedan resolver con un índice sencillo |
| **Cuándo se revisaría** | Si aparece un dato que no quepa en texto, o una consulta que el índice no pueda responder |

### La documentación de todos los proyectos vive en el repositorio de la plataforma

| Campo | Valor |
|---|---|
| **Identificador** | `DA-02` |
| **Qué se decide** | Una carpeta por proyecto dentro del repositorio de la plataforma. El proyecto administrado se queda solo con su código |
| **Qué exige** | RF-01, RF-25, y el alcance de la etapa 1 |
| **Alternativas descartadas** | Que cada proyecto guarde su documentación adentro, porque es lo que impide consultarlos de conjunto y auditarlos, y es el problema declarado. Un repositorio por proyecto administrado, porque habría que clonar y sincronizar tantos repositorios como proyectos, y se pierde la vista de conjunto que se está buscando |
| **Por qué esta** | Se clona la plataforma y está todo: los proyectos, su historia y sus aprobaciones |
| **Qué se pierde** | Un proyecto entregado a un cliente se queda sin su historia, salvo que se le genere el expediente |
| **Cuándo se revisaría** | Si un cliente exige quedarse con la documentación viva de su proyecto, y no con una copia generada |

### La plataforma corre en la máquina de quien trabaja

| Campo | Valor |
|---|---|
| **Identificador** | `DA-03` |
| **Qué se decide** | Se levanta en la máquina del usuario, sin depender de nadie. Lo que se construya no puede impedir que mañana corra en un servidor |
| **Qué exige** | RNF-03, RNF-09 |
| **Alternativas descartadas** | Un servicio en línea desde el principio, porque habría que sostener infraestructura y la información de los clientes saldría de la máquina del usuario. Atarla a la máquina de forma que no pueda moverse, porque cierra una puerta que el usuario quiere dejar abierta |
| **Por qué esta** | Es la única forma de arrancar sin gasto y sin sacar los datos de donde están, y deja el camino abierto |
| **Qué se pierde** | Trabajar desde otra máquina exige llevarse el repositorio |
| **Cuándo se revisaría** | Cuando alguien más tenga que usarla, que es cuando el servidor deja de ser opcional |

### El agente recibe las reglas de la plataforma, y si no responde lee la fuente

| Campo | Valor |
|---|---|
| **Identificador** | `DA-04` |
| **Qué se decide** | Al abrir sesión en un proyecto, la plataforma le entrega al agente las reglas que rigen ahí. Si la plataforma no está disponible, el agente lee la fuente en texto y avisa que trabaja sin ella |
| **Qué exige** | RF-09, RNF-03 |
| **Alternativas descartadas** | Que el agente se detenga si la plataforma no responde, porque una herramienta que impide trabajar cuando falla se termina desactivando. Que cada proyecto guarde su copia de las reglas, porque entonces la plataforma deja de gobernar y vuelve el problema de tener la verdad en varios sitios |
| **Por qué esta** | La plataforma gobierna cuando está, y no bloquea cuando no está |
| **Qué se pierde** | Lo que se trabaje sin ella no queda auditado, y hay que reconciliarlo después |
| **Cuándo se revisaría** | Si trabajar sin ella se vuelve la costumbre en vez de la excepción |

### Una regla, un archivo, y un número que no se reutiliza

| Campo | Valor |
|---|---|
| **Identificador** | `DA-05` |
| **Qué se decide** | Cada regla tiene su archivo y su número propio, y ese número no se le da nunca a otra, ni cuando la regla deja de regir |
| **Qué exige** | RF-06, RN-6 |
| **Alternativas descartadas** | Juntar las reglas de un tema en un archivo, porque al cambiar una las demás se corren de sitio y quien las citó por su posición ya no las encuentra. Renumerar al reordenar, porque los documentos y trabajos cerrados citan esos números, y todos quedarían apuntando a otra cosa |
| **Por qué esta** | Un documento escrito hace un año tiene que seguir sirviendo, y para eso el número no puede cambiar de dueño |
| **Qué se pierde** | Muchos archivos pequeños, que hay que indexar |
| **Cuándo se revisaría** | Si tantos archivos llegaran a hacer lenta la entrega de reglas al abrir la sesión |

### Las comprobaciones leen y avisan, pero no corrigen

| Campo | Valor |
|---|---|
| **Identificador** | `DA-06` |
| **Qué se decide** | Cada regla que se pueda revisar sin criterio humano tiene un programa que la revisa. Dice qué está mal y dónde, y no toca nada |
| **Qué exige** | RF-20, RN-4 |
| **Alternativas descartadas** | Confiar en que el agente se acuerde, que es el problema que originó todo. Que el programa arregle lo que encuentra, porque estaría cambiando el proyecto sin que el usuario lo apruebe |
| **Por qué esta** | Lo que depende de la memoria del agente se incumple sin que nadie se entere, y lo que se arregla solo se salta a quien debía decidir |
| **Qué se pierde** | Lo que la comprobación encuentra hay que arreglarlo a mano |
| **Cuándo se revisaría** | Si aparecen tantos hallazgos iguales que arreglarlos a mano deje de tener sentido |

### La aprobación se ata al texto exacto, y caduca si el texto cambia

| Campo | Valor |
|---|---|
| **Identificador** | `DA-07` |
| **Qué se decide** | Aprobar guarda quién, cuándo y una huella del texto aprobado. Si el documento cambia, la aprobación deja de valer y se dice |
| **Qué exige** | RF-15, RF-17, RN-8 |
| **Alternativas descartadas** | Guardar solo que el documento está aprobado, porque entonces cualquier cambio posterior queda cubierto por una firma que nadie dio sobre ese texto. Guardar una copia entera del documento aprobado, porque duplica todo y obliga a decidir cuál de las dos manda |
| **Por qué esta** | Permite demostrar meses después qué se autorizó exactamente, sin duplicar la fuente |
| **Qué se pierde** | Corregir una coma en un documento aprobado obliga a volver a aprobarlo |
| **Cuándo se revisaría** | Si hay que volver a aprobar tanto que la firma pierda sentido: ahí habrá que distinguir el cambio de forma del de fondo |

### La auditoría registra acciones, no conversación, y no se edita

| Campo | Valor |
|---|---|
| **Identificador** | `DA-08` |
| **Qué se decide** | Se registra cada acción que cambia algo: quién, cuándo, sobre qué y qué cambió. Lo registrado no se puede modificar ni borrar |
| **Qué exige** | RF-18, RNF-12 |
| **Alternativas descartadas** | Registrar cada mensaje de cada sesión, porque pesa mucho, se llena de ruido y termina sin consultarse. Dejar que se pueda corregir el registro, porque un registro editable no sirve para demostrar nada |
| **Por qué esta** | Lo que importa demostrar es qué se hizo, no qué se dijo mientras se hacía |
| **Qué se pierde** | El porqué de una acción no queda en la auditoría: queda en el documento y en la memoria |
| **Cuándo se revisaría** | Si aparece una discusión sobre qué se decidió que la auditoría de acciones no pueda resolver |

### El entregable se genera desde el texto, y la salida no se edita

| Campo | Valor |
|---|---|
| **Identificador** | `DA-09` |
| **Qué se decide** | El archivo de ofimática se produce a partir de los documentos en texto, cuantas veces haga falta, y nunca al contrario |
| **Qué exige** | RF-26, RN-7 |
| **Alternativas descartadas** | Escribir directo en ofimática, porque ese formato no deja ver qué cambió de una versión a otra. Mantener los dos y sincronizarlos, porque cuando difieren nadie sabe cuál manda |
| **Por qué esta** | Lo que se genera se rehace; un segundo original hay que mantenerlo para siempre |
| **Qué se pierde** | Quien recibe el entregable no puede devolver correcciones escritas encima: tiene que pedirlas |
| **Cuándo se revisaría** | Si un cliente exige trabajar sobre el entregable como documento vivo |

### Traer un proyecto no modifica el proyecto de origen

| Campo | Valor |
|---|---|
| **Identificador** | `DA-10` |
| **Qué se decide** | Incorporar un proyecto copia lo que tenga escrito, y no toca ni mueve nada en su carpeta |
| **Qué exige** | RF-27, RN-2 |
| **Alternativas descartadas** | Mover la documentación del proyecto a la plataforma, porque si algo sale mal el proyecto se queda sin lo suyo. Dejar una copia enlazada en los dos sitios, porque vuelven a existir dos versiones que divergen |
| **Por qué esta** | Traer tiene que poder deshacerse sin daño: el proyecto de origen queda tal como estaba |
| **Qué se pierde** | Durante un tiempo hay dos copias, y hay que decir cuál manda |
| **Cuándo se revisaría** | Si los proyectos empiezan a editarse en los dos sitios a la vez |

### Cada componente entra sin obligar a tocar los otros

| Campo | Valor |
|---|---|
| **Identificador** | `DA-11` |
| **Qué se decide** | Cada componente es un archivo aparte, y agregar uno no obliga a editar ninguno de los otros: la plataforma los recoge todos sin saber de antemano cuáles son |
| **Qué exige** | RF-22, RNF-10, RNF-11 |
| **Alternativas descartadas** | Un componente central que llame a los demás por su nombre, porque cada vez que se agrega algo hay que editarlo, y ahí es donde se rompe lo que ya funcionaba. Que los componentes se registren entre ellos, porque el resultado empieza a depender del orden en que se cargan y ese orden no lo controla nadie |
| **Por qué esta** | El problema declarado dice que cada cosa nueva se llevaba por delante lo anterior. Esta es la forma de que deje de pasar |
| **Qué se pierde** | No se puede dar por sentado en qué orden corren: cuando el orden importe, hay que escribirlo |
| **Cuándo se revisaría** | Si aparece un componente cuyo resultado dependa del orden y no se pueda declarar |

### La pantalla administra, y todo cambio queda firmado y registrado

| Campo | Valor |
|---|---|
| **Identificador** | `DA-12` |
| **Qué se decide** | Desde la interfaz se crea, se edita y se publica. Todo cambio de estado queda en la auditoría, y lo que exige aprobación no avanza sin ella |
| **Qué exige** | RF-05, RF-11, RF-14, RN-2 |
| **Alternativas descartadas** | Que la pantalla solo deje mirar, que era la decisión anterior: quien ve un error quiere corregirlo, y salir a otro sitio para hacerlo termina en que nadie use la pantalla. Que la pantalla haga todo sin registrar, porque entonces se pierde lo único que permite auditar |
| **Por qué esta** | La plataforma nació para administrar. Lo que la hace segura no es prohibir el cambio: es que todo cambio quede firmado y registrado |
| **Qué se pierde** | Más superficie donde algo puede salir mal, y más que auditar |
| **Cuándo se revisaría** | Si el registro crece tanto que deje de poderse consultar |

---

## Lo que tienen en común

**Cinco descartan lo mismo por lo mismo:** cualquier cosa que dependa de un servicio ajeno o que saque la información de la máquina del usuario. Es la restricción de la etapa 1 hecha diseño.

**Tres se sostienen en la misma idea:** el texto es la verdad, y todo lo demás se reconstruye. De ahí salen el respaldo, la recuperación y que todo se pueda leer sin la plataforma.

**La que más cambió respecto de ayer es `DA-12`:** antes la pantalla solo dejaba mirar, y ahora administra. Lo que la mantiene segura no es prohibir, es registrar.
