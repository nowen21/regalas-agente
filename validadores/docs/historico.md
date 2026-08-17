# `historico.py`

Escribe la conversación de la sesión en la carpeta `historico-chat/`: el mensaje del usuario cuando lo envía, y la respuesta del agente cuando termina.

## Qué hace

Este archivo **escribe**, no revisa. Es una de las dos excepciones de la carpeta.

Se usa en dos momentos de la conversación:

- **El mensaje del usuario**, que se anota apenas se envía.
- **La respuesta del agente**, que se anota apenas termina. Se lee del archivo donde Claude Code va guardando todo lo que pasa en la conversación.

La hora sale del reloj de la máquina, en el momento exacto en que ocurre cada cosa.

Cada conversación tiene un número largo que la identifica. Ese número queda escrito en la primera línea del archivo, en una nota que no se ve al leerlo. El archivo se busca por esa nota y no por su nombre, así se le puede cambiar el nombre para ponerle el tema del que se habló sin que se pierda el hilo.

Además arma el índice de sesiones que se le entrega al agente al arrancar.

## De qué depende y quién lo usa

No usa ningún otro archivo de `validadores/`. De Python usa `json`, `os`, `re` y `datetime`.

```
historico.py
   (no depende de nadie)
```

Lo usan:

```
historico.py
   ▲
   ├── hook_historico.py ··· anota el mensaje y la respuesta
   ├── hook_sesion.py ······ pide el índice de sesiones al arrancar
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `CARPETA` | `historico-chat`. |
| `INDICE` | `README.md`, el archivo con la lista de sesiones. |
| `LIMITE` | `40`. Cuántas sesiones se listan al arrancar. Las viejas siguen en el índice del README. |
| `_NUMERO` | Reconoce el número con que va marcado cada mensaje dentro del archivo de la conversación. |
| `_LINEA` | Reconoce una línea del índice: el enlace al archivo y el tema. |
| `_FECHA` | Reconoce la fecha con la que empieza el nombre de un archivo de sesión. |
| `RESUMENES` | `resumenes`, la carpeta donde vive el resumen de cada sesión. |
| `HACIA_HISTORICO` | `../../`. Cómo se sube desde un resumen hasta la transcripción, que está dos carpetas más arriba. |

### Funciones principales

**`anotar_usuario(raiz, sesion, mensaje)`**

- **Recibe:** la carpeta del proyecto, el número que identifica la conversación y el mensaje del usuario.
- **Hace:**
  1. Si el mensaje está vacío, no hace nada.
  2. Busca el archivo de esta sesión; si no existe, lo crea.
  3. Calcula el número que le toca al mensaje.
  4. Escribe el mensaje como cita, con la fecha y la hora.
  5. Comprueba que la sesión esté en el índice del README, y la agrega si falta.
- **Retorna:** la ruta del archivo escrito, o texto vacío si no aplicaba.

El paso 5 se hace en cada mensaje y no solo al crear el archivo. Es inofensivo repetirlo: si la línea ya está, no hace nada.

**`anotar_agente(raiz, sesion, transcript)`**

- **Recibe:** la carpeta del proyecto, el número que identifica la conversación y dónde está el archivo en que Claude Code la va guardando.
- **Hace:**
  1. Saca de ahí la última respuesta del agente y el número que la identifica.
  2. Busca el archivo de esta conversación; **no lo crea** si no existe, porque sin un mensaje anterior no hay dónde escribir.
  3. Si esa respuesta ya estaba anotada, no hace nada.
  4. Escribe la respuesta con la fecha, la hora y una nota que no se ve con su número.
- **Retorna:** la ruta del archivo escrito, o texto vacío.

**`ultima_respuesta(transcript)`**

- **Recibe:** dónde está el archivo en que Claude Code guarda la conversación.
- **Hace:** lo lee línea por línea —cada línea es un dato suelto, escrito en JSON—, lo recorre de atrás hacia adelante y va juntando los pedazos de texto del agente hasta llegar a un mensaje escrito de verdad por la persona. Deja fuera lo que hicieron los ayudantes del agente.
- **Retorna:** un par «texto de la respuesta, número que la identifica».

Que el mensaje sea «escrito de verdad por la persona» importa: los resultados de las herramientas viajan por el mismo camino y parecen mensajes suyos. Si se cortara ahí, se guardaría solo el último pedazo de una respuesta larga. Tampoco se guarda lo que el agente pensó por dentro ni lo que retornaron las herramientas.

**`sesiones(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** lee el índice del README y saca sus líneas.
- **Retorna:** una lista de pares «nombre de archivo, de qué se trató», en orden.

Se lee del índice y no de la carpeta porque el índice es lo que dice de qué trató cada sesión.

**`contexto(raiz, limite=LIMITE)`**

- **Recibe:** la carpeta del proyecto y cuántas sesiones listar.
- **Hace:** toma las últimas sesiones y arma el bloque de texto que se le entrega al agente al arrancar, con la advertencia de que ahí solo está el índice y de que hay que abrir la sesión que corresponda.
- **Retorna:** ese texto, o texto vacío si no hay sesiones.

**`renombrar(archivo, tema, resumen="")`**

- **Recibe:** la transcripción, el tema con el que se la quiere nombrar y, opcional, de qué se trató.
- **Hace:**
  1. Le cambia el título al archivo, dejándole la misma fecha.
  2. Arrastra el resumen de esa sesión al nombre nuevo, y le deja al día el enlace que apunta de vuelta a la transcripción.
  3. Renombra la transcripción.
  4. Corrige su línea en el índice.
- **Retorna:** la ruta nueva de la transcripción.

La fecha nunca sale del reloj: sale del nombre viejo. Una sesión que se nombra al otro día sigue siendo la del día en que ocurrió.

### Funciones de apoyo

**`_es_usuario(dato)`**

- **Recibe:** una línea del archivo de la conversación.
- **Retorna:** verdadero solo si es un mensaje escrito por la persona, y no el resultado de una herramienta.

**`_bloques(dato)`**

- **Recibe:** una línea del archivo de la conversación.
- **Retorna:** los pedazos de contenido de ese mensaje.

**`_archivo(raiz, sesion, crear)`**

- **Recibe:** la carpeta, el número que identifica la conversación y si se permite crear el archivo.
- **Hace:** recorre los `.md` de la carpeta buscando el que lleva esa nota.
- **Retorna:** la ruta encontrada; si no la encuentra y se permite crear, la del archivo nuevo; si no, texto vacío. Si el proyecto no tiene carpeta `historico-chat/`, retorna texto vacío sin crear nada.

**`_crear(carpeta, sesion)`**

- **Hace:** crea el archivo con el nombre `AAAA-MM-DD-sesion.md`, agregándole un número si ya hubo conversaciones ese día, y le escribe la nota que la identifica, el título y el encabezado. Después lo agrega al índice.
- **Retorna:** la ruta creada.

**`_indexar(carpeta, nombre, fecha)`**

- **Hace:** agrega la línea de la sesión al README, si no estaba ya. Si no hay README, no hace nada.

**`_mover_resumen(carpeta, viejo, nuevo)`**

- **Hace:** le pone el nombre nuevo al resumen de esa sesión, si ya existe, corrige su línea en el índice del día y le deja al día el enlace de adentro. Va **antes** de mover la transcripción: si algo falla, lo que queda mal es el resumen —que se puede volver a mover— y no el índice, que es por donde la próxima sesión llega a esta.

**`_reenlazar(resumen, carpeta, viejo, nuevo)`**

- **Hace:** dentro del resumen, deja con el nombre nuevo el enlace que apunta de vuelta a la transcripción. Cambia las dos partes, el texto que se ve y el destino: un enlace que abre pero se anuncia con el nombre viejo también miente (`13·DOC14`).
- Se reemplaza el par exacto y no toda aparición del nombre viejo, porque un resumen puede nombrar otras sesiones y a esas no hay que tocarles nada.

**`_fecha_de(nombre)`**

- **Retorna:** la fecha con la que empieza el nombre del archivo, o la de hoy.

**`_siguiente_numero(texto)`**

- **Retorna:** el número que le toca al próximo mensaje.

**`_ahora()`**

- **Retorna:** la fecha y la hora del reloj de la máquina, como `AAAA-MM-DD HH:MM:SS`.

**`_leer(ruta)`**

- **Retorna:** el contenido del archivo, o texto vacío si no se puede leer.

**`_agregar(ruta, texto)`**

- **Hace:** agrega el texto al final del archivo.

**`_anotar(ruta, bloque)`**

- **Hace:** mete el bloque al final de la **conversación**, no al final del archivo. Si el archivo tiene una sección `## Abierto` al final, el bloque va antes de ella; si no, va al final.

## Cómo se ejecuta

```
el usuario envía un mensaje
        ↓
hook_historico.py --modo usuario
        ↓
historico.anotar_usuario(carpeta, sesion, mensaje)
        ↓
   busca el archivo por la marca <!-- sesion: ... -->
   si no existe, lo crea y lo agrega al índice
        ↓
   escribe "### 3 · Usuario — 2026-08-08 22:42:46" y el mensaje citado


el agente termina de responder
        ↓
hook_historico.py --modo agente
        ↓
historico.anotar_agente(carpeta, sesion, donde_esta_la_conversacion)
        ↓
   ultima_respuesta() la lee de atrás hacia adelante
        ↓
   si esa respuesta ya estaba, no hace nada
        ↓
   escribe "**Agente** — 2026-08-08 22:45:10" y el texto
```

## Ejemplos de lo que retorna

```python
anotar_usuario('C:/proyectos/pos', '69ebc47d-…', 'Documente los validadores.')
'C:/proyectos/pos\historico-chat\2026-08-09-sesion.md'

anotar_usuario('C:/proyectos/pos', '69ebc47d-…', '   ')
''               # mensaje vacío: no hace nada

anotar_usuario('C:/proyectos/sin-historico', '69ebc47d-…', 'Hola')
''               # el proyecto no lleva histórico

# y lo que quedó escrito en el archivo:
### 3 · Usuario — 2026-08-09 22:42:46
> Documente los validadores.

anotar_agente('C:/proyectos/pos', '69ebc47d-…', 'C:/…/transcript.jsonl')
'C:/proyectos/pos\historico-chat\2026-08-09-sesion.md'

anotar_agente(...)   # la segunda vez, con la misma respuesta
''               # ya estaba anotada: no la duplica

# y lo que quedó escrito:
**Agente** — 2026-08-09 22:45:10
<!-- agente: 8f21ac30-1b4e-4f77-9c02-5db1e6a44f10 -->

Listo. 40 documentos en validadores/docs/…

ultima_respuesta('C:/…/transcript.jsonl')
('Listo. 40 documentos en validadores/docs/…\n\nY el resumen final.',
 '8f21ac30-1b4e-4f77-9c02-5db1e6a44f10')
#  └─ el texto ya unido                     └─ el identificador de la respuesta

ultima_respuesta('C:/ruta/que/no/existe.jsonl')
('', '')

_es_usuario({'type': 'user', 'message': {'content': 'Hola'}})
True
_es_usuario({'type': 'user', 'message': {'content': [{'type': 'tool_result'}]}})
False            # es el resultado de una herramienta, no una persona

_archivo('C:/proyectos/pos', '69ebc47d-…', crear=False)
'C:/proyectos/pos\historico-chat\2026-08-09-sesion.md'

_crear('C:/proyectos/pos/historico-chat', '69ebc47d-…')
'C:/proyectos/pos\historico-chat\2026-08-09-sesion-2.md'
# el -2 aparece porque ya había una sesión ese día

_fecha_de('2026-08-09-documentar-validadores.md')
'2026-08-09'

_siguiente_numero('### 1 · Usuario — …\n### 2 · Usuario — …\n')
3

_ahora()
'2026-08-09 22:42:46'

sesiones('C:/proyectos/pos')
[('2026-08-06-historico-chat.md', 'se crea esta carpeta; queda el trabajo previo.'),
 ('2026-08-09-sesion.md',         'sesión del 2026-08-09.')]
#  └─ archivo                      └─ de qué se trató

contexto('C:/proyectos/pos')
'''[HISTÓRICO DE SESIONES — NO ESTÁ CARGADO, SOLO EL ÍNDICE]
Cada sesión con este proyecto quedó transcrita literal. Antes de retomar un
tema, leer con Read la sesión que lo trató: ahí está qué se decidió y por qué.
No suponer qué dice una sesión por su título.
Se listan las últimas 40 de 47; el resto, en historico-chat/README.md.

  historico-chat/2026-08-06-historico-chat.md — se crea esta carpeta; …
  historico-chat/2026-08-09-sesion.md — sesión del 2026-08-09.'''

contexto('C:/proyectos/nuevo')
''               # todavía no hay ninguna sesión
```
