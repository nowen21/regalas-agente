# `recuerdos.py`

Mueve la memoria del agente desde la carpeta de la herramienta hasta el repositorio del proyecto.

## Qué hace

Claude Code guarda lo que el agente debe recordar entre sesiones en una carpeta suya, fuera del proyecto:

```
~/.claude/projects/<ruta-del-proyecto-con-guiones>/memory/
```

Ahí no sirve: no se ve en git, no se puede revisar en un cambio, no se versiona y no viaja a otra máquina.

Este archivo hace que esa carpeta quede vacía: cada recuerdo se **mueve** a `historico-chat/memory/` del proyecto.

Dos cosas importantes de cómo lo hace:

- **Mueve, no copia.** Con el tiempo, dos copias del mismo recuerdo terminan diciendo cosas distintas.
- **No borra nada, nunca.** Si en el destino ya hay un archivo con ese nombre, el que llega entra llamándose igual pero con `-local` al final, y el usuario decide cuál se queda.

Hay un caso en el que no hace nada: cuando la carpeta de la herramienta y la del proyecto son, en realidad, la misma. Eso pasa cuando alguien puso un **acceso directo**: dos nombres distintos que llevan al mismo sitio del disco. Ahí la herramienta ya está escribiendo adentro del proyecto, y mover sería mover cada archivo encima de sí mismo. Por eso todas las comprobaciones le preguntan al sistema si las dos direcciones llevan al mismo sitio, en vez de mirar si están escritas igual.

## De qué depende y quién lo usa

No usa ningún otro archivo de `validadores/`. De Python usa `os`, `re` y `shutil`.

```
recuerdos.py
   (no depende de nadie)
```

Lo usan:

```
recuerdos.py
   ▲
   ├── hook_recuerdos.py ··· mueve, al arrancar y al escribir un archivo
   ├── hook_sesion.py ······ pide el índice de la memoria al arrancar
   ├── checklist.py ········ comprueba que la memoria esté en el repositorio
   ├── instalar.py ········· crea el índice y mueve lo que haya quedado
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `CARPETA` | `historico-chat/memory`, donde debe vivir la memoria. |
| `INDICE` | `memory.md`, el archivo con la lista de recuerdos. |
| `_NO_ALFANUM` | Reconoce todo lo que no es letra ni número, para armar el nombre de carpeta que usa la herramienta. |
| `_SUFIJO` | `-local`, lo que se le agrega al final del nombre cuando ese nombre ya estaba ocupado. |

### Funciones de ubicación

**`carpeta_local(proyecto, casa=None)`**

- **Recibe:** la carpeta del proyecto y, opcionalmente, la carpeta del usuario.
- **Hace:** convierte la ruta del proyecto en el nombre que usa Claude Code, reemplazando por guiones todo lo que no sea letra o número.
- **Retorna:** la ruta de la carpeta donde la herramienta guarda la memoria de ese proyecto.

Por ejemplo, `c:\Ing. Jose\ia\agente` se convierte en `c--Ing--Jose-ia-agente`.

**`carpeta_repo(proyecto)`**

- **Retorna:** la ruta de `historico-chat/memory/` dentro del proyecto.

**`ruta_indice(proyecto)`**

- **Retorna:** la ruta del archivo `memory.md` dentro de esa carpeta.

**`indice_presente(proyecto)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** mira si existe el índice, **sin fijarse en mayúsculas ni minúsculas**. En Windows `MEMORY.md` y `memory.md` son el mismo archivo; si se preguntara por el nombre exacto, el instalador creería que falta y lo escribiría encima, borrando lo que había.
- **Retorna:** verdadero o falso.

**`_es_el_mismo(uno, otro)`**

- **Recibe:** dos rutas.
- **Hace:** le pregunta al sistema si llevan al mismo archivo o a la misma carpeta. Comparar los textos no alcanza: un acceso directo hace que dos direcciones escritas distinto lleven al mismo sitio.
- **Retorna:** verdadero o falso.

**`enlazada(proyecto, casa=None)`**

- **Retorna:** verdadero si la carpeta de la herramienta y la del proyecto son la misma.

**`sueltos(proyecto, casa=None)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** lista los archivos que quedaron en la carpeta de la herramienta. Si esa carpeta no existe, o es la misma del proyecto, retorna una lista vacía.
- **Retorna:** la lista de direcciones completas, en orden.

**`_libre(carpeta, nombre)`**

- **Recibe:** una carpeta y un nombre de archivo.
- **Hace:** si el nombre está libre lo retorna tal cual; si está ocupado prueba agregándole `-local` al final, y después `-local-2`, `-local-3`. Para comparar, da igual que esté en mayúsculas o minúsculas.
- **Retorna:** el nombre que se puede usar.

### Funciones principales

**`migrar(proyecto, aplicar=True, casa=None)`**

- **Recibe:** la carpeta del proyecto, si se mueve de verdad o solo se calcula, y opcionalmente la carpeta del usuario.
- **Hace:**
  1. Lista lo que quedó suelto. Si no hay nada, termina.
  2. Por cada archivo comprueba que el origen y el destino no sean el mismo archivo.
  3. Busca un nombre libre en el destino.
  4. Si `aplicar` es verdadero, crea la carpeta destino si falta y mueve el archivo.
- **Retorna:** una lista de pares «nombre de origen, nombre de destino».

**`pasos(movidos)`**

- **Recibe:** la lista que retorna `migrar`.
- **Retorna:** una lista de textos, uno por movimiento, avisando cuando el nombre tuvo que cambiar.

**`contexto(proyecto)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** lee el índice de la memoria.
- **Retorna:** el texto que se le entrega al agente al arrancar: el índice completo y el aviso de que tiene que abrir el recuerdo que le haga falta. Texto vacío si no hay índice.

Va el índice y no los recuerdos enteros: es corto y ya dice de qué trata cada uno.

**`revisar(proyecto, casa=None)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** mira si quedó algo en la carpeta de la herramienta.
- **Retorna:** un par «cumple, detalle». Si quedó algo, el detalle nombra hasta cuatro archivos y cuenta el resto.

## Cómo se ejecuta

Al abrir la sesión y cada vez que se escribe un archivo:

```
hook_recuerdos.py
        ↓
recuerdos.migrar(proyecto, aplicar=True)
        ↓
   sueltos() → ¿quedó algo en ~/.claude/projects/.../memory/?
        ↓ (si esa carpeta y la del proyecto son la misma, no hay nada que mover)
   por cada archivo:
        _libre() busca un nombre que no choque
        shutil.move() lo mueve a historico-chat/memory/
        ↓
recuerdos.pasos(movidos) → el aviso que se muestra
```

Al arrancar, además:

```
hook_sesion.py → recuerdos.contexto(proyecto) → el índice de la memoria
                 se le entrega al agente
```

## Ejemplos de lo que retorna

```python
carpeta_local('c:/Ing. Jose/ia/agente')
'C:\Users\user\.claude\projects\c--Ing--Jose-ia-agente\memory'
#                                     └─ la ruta con todo lo raro cambiado por guiones

carpeta_repo('c:/Ing. Jose/ia/agente')
'c:\Ing. Jose\ia\agente\historico-chat\memory'

ruta_indice('c:/Ing. Jose/ia/agente')
'c:\Ing. Jose\ia\agente\historico-chat\memory\memory.md'

indice_presente('c:/Ing. Jose/ia/agente')
True             # existe memory.md, MEMORY.md o Memory.md: da igual

enlazada('c:/Ing. Jose/ia/agente')
False            # las dos carpetas son sitios distintos

sueltos('c:/Ing. Jose/ia/agente')
['C:\Users\user\.claude\projects\c--Ing--Jose-ia-agente\memory\estilo.md',
 'C:\Users\user\.claude\projects\c--Ing--Jose-ia-agente\memory\MEMORY.md']

sueltos('c:/proyectos/limpio')
[]               # la carpeta de la herramienta está vacía: así debe estar

_libre('…/historico-chat/memory', 'estilo.md')
'estilo.md'                # el nombre estaba libre

_libre('…/historico-chat/memory', 'MEMORY.md')
'MEMORY-local.md'          # ya había un memory.md: no se pisa

migrar('c:/Ing. Jose/ia/agente', aplicar=True)
[('estilo.md', 'estilo.md'),
 ('MEMORY.md', 'MEMORY-local.md')]
#  └─ como se llamaba   └─ como quedó

migrar('c:/proyectos/limpio', aplicar=True)
[]               # no había nada que mover

pasos([('estilo.md', 'estilo.md'), ('MEMORY.md', 'MEMORY-local.md')])
['mover `estilo.md` a `historico-chat/memory/`',
 'mover `MEMORY.md` a `historico-chat/memory/MEMORY-local.md` — el nombre ya
  estaba ocupado; revisar cuál manda']

contexto('c:/Ing. Jose/ia/agente')
'''[MEMORIA DEL AGENTE — ÍNDICE, OBLIGATORIA]
Es cómo pide el usuario que se trabaje en este proyecto, y rige esta sesión
completa. Antes de tocar un tema que aparezca abajo, leer con Read el archivo
del recuerdo: el índice dice de qué trata, no qué exige.
Un recuerdo nuevo se escribe en `historico-chat/memory/`, nunca en el almacén
de la herramienta (`01·C19`).

<<< historico-chat/memory/memory.md >>>
# Memoria del agente — cómo se trabaja en este repo
… el índice completo …'''

contexto('C:/proyectos/sin-memoria')
''

revisar('c:/Ing. Jose/ia/agente')
(False, 'quedaron 2 archivo(s) en la memoria local de la herramienta
         (estilo.md, MEMORY.md) — `C:/Users/user/.claude/projects/…/memory`;
         la memoria va en `historico-chat/memory/` (`01·C19`)')

revisar('c:/proyectos/limpio')
(True, '')
```
