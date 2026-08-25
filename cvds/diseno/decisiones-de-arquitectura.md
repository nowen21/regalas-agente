# Decisiones de arquitectura   ·   `[CAPA 3]`

**Para qué sirve este documento.** Las decisiones que cuestan caro de revertir, cada una con las alternativas que se descartaron y por qué. Sin las alternativas, una decisión no se puede defender ni revisar después: solo se puede obedecer o romper.

> **Escrito como si no hubiera nada construido**, igual que el resto de [cvds/](../README.md). Sale de los módulos de [cvds/diseno/README.md](README.md).

**Estado: BORRADOR** (2026-08-24, sin aprobar).

**Cómo se citan.** Cada decisión lleva un número que empieza por `DA`, de **decisión de arquitectura**: `DA-01`, `DA-02`. Ese número se usa para nombrarla en cualquier otro documento, y no se le da a otra decisión aunque esta se cambie después.

---

## Decisiones

### Las reglas son archivos de texto en el repositorio

| Campo | Valor |
|---|---|
| **Identificador** | `DA-01` |
| **Qué se decide** | Cada regla se escribe en un archivo de texto, y ese archivo vive dentro del proyecto |
| **Qué exige** | RF-01, RF-05, RNF-02 |
| **Alternativas descartadas** | • Una base de datos, porque no se lee sin abrir un programa<br>• Un servidor que las entregue, porque sin internet no habría reglas<br>• La configuración de la herramienta, porque se queda en esa máquina |
| **Por qué esta** | El texto se lee sin instalar nada, se ve qué cambió en cada versión línea por línea, y viaja con el proyecto cuando alguien se lo lleva |
| **Qué se pierde** | Preguntar cosas como «cuántas reglas hablan de pruebas» exige leer los archivos, no consultarlos |
| **Cuándo se revisaría** | Cuando las reglas sean tantas que encontrar una a ojo deje de ser posible |

### Una regla, un archivo, y un número que no se reutiliza

| Campo | Valor |
|---|---|
| **Identificador** | `DA-02` |
| **Qué se decide** | Cada regla tiene su propio archivo y su propio número, y ese número no se le da nunca a otra, ni siquiera cuando la regla deja de regir |
| **Qué exige** | RN-6, RF-09 |
| **Alternativas descartadas** | • Varias reglas en un mismo archivo, porque cambiar una corre a las demás<br>• Renumerar al reordenar, porque las citas viejas quedarían apuntando a otra cosa |
| **Por qué esta** | Un documento escrito hace un año tiene que seguir sirviendo, y para eso el número que cita no puede haber cambiado de dueño |
| **Qué se pierde** | Quedan muchos archivos pequeños, y hay que mantener un índice para poder recorrerlos |
| **Cuándo se revisaría** | Si tantos archivos llegaran a hacer lenta la apertura de la sesión, que es lo que mide RNF-01 |

### Las comprobaciones leen y avisan, pero no corrigen

| Campo | Valor |
|---|---|
| **Identificador** | `DA-03` |
| **Qué se decide** | Cada regla que se pueda revisar sin criterio humano tiene un programa que la revisa. El programa dice qué está mal y dónde, y no toca nada |
| **Qué exige** | RF-03, RF-04, RN-4 |
| **Alternativas descartadas** | • Confiar en que el agente se acuerde, que es el problema original<br>• Que el programa corrija lo que encuentra, porque cambiaría el proyecto sin aprobación |
| **Por qué esta** | Lo que depende de la memoria del agente se incumple sin que nadie se entere; lo que se arregla solo se salta a quien debía decidir |
| **Qué se pierde** | Lo que la comprobación encuentra hay que arreglarlo a mano |
| **Cuándo se revisaría** | Si aparecieran tantos hallazgos iguales, una y otra vez, que arreglarlos a mano dejara de tener sentido |

### El texto es la fuente, y el entregable se genera desde él

| Campo | Valor |
|---|---|
| **Identificador** | `DA-04` |
| **Qué se decide** | Los documentos se escriben en texto. El archivo de ofimática que recibe el cliente se produce a partir de ese texto, y nunca al contrario |
| **Qué exige** | RF-10, RN-12 |
| **Alternativas descartadas** | • Escribir directo en ofimática, porque ese formato no deja ver qué cambió<br>• Mantener los dos archivos, porque cuando difieren nadie sabe cuál manda |
| **Por qué esta** | Un archivo que se genera se puede rehacer cuantas veces haga falta; un segundo original hay que mantenerlo al día para siempre |
| **Qué se pierde** | Quien recibe el documento no puede devolver correcciones escritas encima: tiene que pedirlas |
| **Cuándo se revisaría** | Si un cliente exigiera trabajar sobre el archivo de ofimática como si fuera el documento vivo |

### Instalar deja una copia, y anota qué versión se adoptó

| Campo | Valor |
|---|---|
| **Identificador** | `DA-05` |
| **Qué se decide** | Al instalar, el proyecto que hereda recibe su propia copia del estándar, y queda escrito qué versión adoptó |
| **Qué exige** | RF-05, RF-06 |
| **Alternativas descartadas** | • Apuntar a una carpeta común, porque el proyecto cambiaría sin que nadie lo decida<br>• Traer la última versión al abrir, porque se actualizaría sin aprobación |
| **Por qué esta** | Un proyecto tiene derecho a quedarse en la versión que ya conoce, y a enterarse de que quedó atrás cuando le convenga |
| **Qué se pierde** | Hay una copia por cada proyecto, y ponerse al día es algo que alguien tiene que decidir y hacer |
| **Cuándo se revisaría** | Si los proyectos que heredan llegaran a ser tantos que actualizarlos uno por uno no se sostenga |

### La pantalla corre en la máquina de quien trabaja, y solo deja mirar

| Campo | Valor |
|---|---|
| **Identificador** | `DA-06` |
| **Qué se decide** | La interfaz muestra los documentos y lo que el agente guardó. Desde ahí no se modifica nada |
| **Qué exige** | RF-12, RN-14, RNF-02 |
| **Alternativas descartadas** | • Ponerla en línea, porque habría que sostener un servidor<br>• Dejar editar desde la pantalla, porque el cambio se haría sin aprobación |
| **Por qué esta** | Mirar no arriesga nada y es barato de construir. Cambiar es lo que pide aprobación, y esa conversación ocurre con el agente, no en una pantalla |
| **Qué se pierde** | Ver un error en pantalla y no poder corregirlo ahí mismo |
| **Cuándo se revisaría** | Si se encuentra una forma de editar desde la pantalla que siga pidiendo aprobación en cada cambio |

### La memoria del agente vive dentro del proyecto

| Campo | Valor |
|---|---|
| **Identificador** | `DA-07` |
| **Qué se decide** | Lo que el agente aprende se guarda en el repositorio del proyecto, no en el almacén de recuerdos de la herramienta |
| **Qué exige** | RF-13, RN-1 |
| **Alternativas descartadas** | • El almacén de la herramienta, porque lo guardado se queda en esa máquina<br>• Una memoria común a todos, porque mezcla proyectos que no se parecen |
| **Por qué esta** | Lo que se aprendió trabajando en un proyecto es parte de ese proyecto, y tiene que poder leerse aunque mañana se use otra herramienta |
| **Qué se pierde** | Lo aprendido en un proyecto no llega solo a los demás: para que llegue hay que subirlo al estándar como regla |
| **Cuándo se revisaría** | Si aparece algo aprendido que sirva a todos los proyectos y no quepa escrito como regla |

### Un componente nuevo no obliga a tocar los que ya estaban

| Campo | Valor |
|---|---|
| **Identificador** | `DA-08` |
| **Qué se decide** | Cada componente del sistema es un archivo aparte. Para agregar uno no hay que editar ninguno de los otros: el cargador las recoge todas sin saber de antemano cuáles son |
| **Qué exige** | RF-14, RNF-08, RNF-09 |
| **Alternativas descartadas** | • Un componente central que los llame a todos, porque agregar obliga a editarlo y ahí se rompe lo anterior<br>• Que los componentes se registren entre ellos, porque el orden pasa a importar |
| **Por qué esta** | El problema declarado dice que cada cosa nueva se llevaba por delante lo anterior. Esta es la forma de que eso deje de pasar |
| **Qué se pierde** | No se puede dar por sentado en qué orden corren los componentes: cuando el orden importe, hay que escribirlo |
| **Cuándo se revisaría** | Si aparece un componente cuyo resultado dependa del orden y ese orden no se pueda declarar |

---

## Lo que tienen en común

Cinco descartan lo mismo por lo mismo: **lo que vive fuera del repositorio no viaja con el proyecto**. Por eso no hay servidor, ni base compartida, ni configuración en la herramienta.

**La que más va a incomodar es DA-06:** quien ve un error en la pantalla va a querer corregirlo ahí. Su ficha ya dice qué la haría cambiar.
