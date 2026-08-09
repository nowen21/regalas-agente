# `checklist.py`

Revisa, pieza por pieza, qué le falta a un proyecto para que el agente quede bien instalado.

## Qué hace

Existe una lista de todo lo que un proyecto debe tener. Esa lista **no está en este archivo**: está en `plantillas/stack-instalacion.md` y se lee de ahí. Este archivo pone, para cada cosa de la lista, la comprobación que responde sí o no.

Por cada una retorna una ficha `Punto` que dice si cumple, y si no cumple, por qué y cómo se arregla.

Además escribe o borra el archivo `.agente/INSTALACION-INCOMPLETA.md`. Mientras falte algo, ese archivo está ahí con el detalle. Cuando ya no falta nada, se borra solo: que no exista es la señal de que todo está completo.

## De qué depende y quién lo usa

```
checklist.py
   ├── instalar.py ··· la lista de archivos de .agente/, los enganches
   │                   esperados, los repositorios git y la revisión de F13
   ├── recuerdos.py ·· si la memoria está en el repositorio y solo ahí
   ├── sesion.py ····· la revisión del CLAUDE.md y de los enganches de git
   ├── version.py ···· la versión del estándar y la que declara el proyecto
   ├── versiones.py ·· las huellas y el registro de versiones
   └── comun.py ······ FALLA, RAIZ y leer
```

De Python usa `json`, `os`, `re` y `datetime`.

Lo usan:

```
checklist.py
   ▲
   ├── hook_checklist.py ··· lo corre en cada mensaje del usuario
   ├── validar.py ·········· cuando alguien pide revisar "checklist"
   ├── instalar.py ········· al terminar, para comprobar cómo quedó
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `PLANTILLA` | Dónde está la lista central: `plantillas/stack-instalacion.md`. |
| `COPIA` | Dónde va la copia dentro del proyecto: `.agente/stack-instalacion.md`. |
| `MARCA` | Dónde se escribe el aviso: `.agente/INSTALACION-INCOMPLETA.md`. |
| `CONFIG_AGENTE` | Los cuatro archivos de `.agente/`. Se toma de `instalar.py` para que no queden dos listas que después digan cosas distintas. |
| `_FILA` | Reconoce una fila de la tabla de piezas de la lista central. |
| `_STACK` | La pieza «lista de instalación», tomada de `versiones.py`. |
| `COMPROBACIONES` | Qué función comprueba cada pieza: al nombre corto de la pieza le corresponde una función. |

### La ficha `Punto`

Una pieza a instalar y cómo quedó al revisarla.

**`__init__(id, componente, arreglo, cumple, detalle="")`**

- **Recibe:** el nombre corto, la descripción de la pieza, el texto de cómo se instala, si cumple o no, y el detalle del problema.
- **Hace:** guarda los cinco valores.
- **Retorna:** la ficha.

**`__str__()`**

- **Retorna:** `[ok] id — descripción` o `[FALTA] id — detalle`.

### Funciones que leen la lista

**`ruta_plantilla(estandar=None)`**

- **Recibe:** opcionalmente la carpeta del estándar.
- **Retorna:** la ruta completa de `plantillas/stack-instalacion.md`.

**`componentes(estandar=None)`**

- **Recibe:** opcionalmente la carpeta del estándar.
- **Hace:** lee la plantilla y saca las filas de la tabla.
- **Retorna:** una lista de tríos: identificador, descripción del componente y cómo se instala. Si la plantilla no existe, retorna una lista vacía.

**`huella(estandar=None)`**

- **Retorna:** la **huella** de la lista central: una marca corta que cambia cada vez que la lista cambia. Comparando huellas se sabe si una copia quedó vieja, sin tener que leer los dos archivos enteros.

**`huella_instalada(proyecto)`**

- **Retorna:** la huella marcada en la copia que tiene el proyecto, o texto vacío.

**`sello(estandar=None)`**

- **Retorna:** la línea de marca que se agrega a la copia para poder compararla después.

### Las comprobaciones

Todas reciben la carpeta del proyecto y la del estándar, y retornan un par «cumple, detalle».

| Función | Qué comprueba |
|---|---|
| `_f13` | Que exista la carpeta `proyectos/`, donde va el código. |
| `_claude_md` | Que el `CLAUDE.md` exista, no tenga huecos sin llenar y su huella sea la misma del molde central. |
| `_gitignore` | Que la lista de archivos que git debe ignorar incluya `CLAUDE.md` y `.agente/`. |
| `_agente_config` | Que estén los cuatro archivos de `.agente/`. |
| `_stack_instalacion` | Que el proyecto tenga su copia de la lista de instalación y que la huella sea la misma de la central. |
| `_documentacion` | Que exista la carpeta `documentacion/`. |
| `_historico` | Que exista `historico-chat/README.md` y que su huella esté al día. |
| `_recuerdos` | Que el índice de la memoria esté en el repositorio y que la memoria de la herramienta haya quedado vacía. |
| `_versiones` | Que la carpeta donde se anota cada instalación diga lo mismo que está puesto. |
| `_enganches_git` | Que los enganches de git estén puestos y apunten a este estándar y no a otro. |
| `_enganches_claude` | Que los siete enganches de Claude Code estén en el archivo de ajustes, con la orden exacta que les toca. |
| `_registro` | Que el proyecto aparezca en la lista central `plantillas/proyectos.md`. |
| `_version` | Que el proyecto diga qué versión del estándar sigue. Cuál sea ese número no reprueba. |

### Funciones principales

**`revisar(proyecto, estandar=None)`**

- **Recibe:** la carpeta del proyecto y opcionalmente la del estándar.
- **Hace:** recorre la lista de piezas; por cada una busca su comprobación y la corre. Si una pieza no tiene comprobación conocida, la deja marcada como pendiente y lo dice. Si una comprobación se rompe, atrapa el error y también la deja pendiente, para que una que falle no tumbe a las demás.
- **Retorna:** una lista de fichas `Punto`, en el mismo orden de la lista.

**`pendientes(puntos)`**

- **Recibe:** la lista de puntos.
- **Retorna:** solo los que no cumplen.

**`resumen(proyecto, puntos)`**

- **Recibe:** la carpeta y la lista de puntos.
- **Retorna:** una línea para mostrar en pantalla: si está completa, cuántos de cuántos; si no, cuáles faltan (hasta cuatro por nombre y el resto contados).

**`detalle(puntos)`**

- **Recibe:** la lista de puntos.
- **Retorna:** el texto con lo que falta y cómo se arregla, dos líneas por componente. Texto vacío si no falta nada.

**`escribir_marca(proyecto, puntos)`**

- **Recibe:** la carpeta y la lista de puntos.
- **Hace:** si no falta nada, borra `.agente/INSTALACION-INCOMPLETA.md`. Si falta algo, lo escribe con la fecha, el conteo, el detalle y la línea que resuelve todo.
- **Retorna:** la ruta del archivo escrito, o texto vacío si no había nada que marcar.

## Cómo se ejecuta

En cada mensaje del usuario, a través del enganche:

```
el usuario escribe un mensaje
        ↓
hook_checklist.py
        ↓
checklist.revisar(proyecto)
        ↓
   lee plantillas/stack-instalacion.md
        ↓
   por cada fila, ejecuta su comprobación
        ↓
   [Punto, Punto, Punto, ...]
        ↓
checklist.escribir_marca(...)   escribe o borra el aviso
        ↓
si falta algo → se lo muestra al usuario y se lo pasa al agente
si no falta nada → no dice nada
```

A mano:

```
python validadores/validar.py checklist --raiz "C:/ruta/proyecto"
```

## Ejemplos de lo que retorna

```python
ruta_plantilla()
'c:\Ing. Jose\ia\agente\plantillas\stack-instalacion.md'

componentes()
[('f13',        'La estructura base del proyecto', 'correr instalar.py --aplicar'),
 ('claude-md',  'El CLAUDE.md del proyecto',       'correr instalar.py --aplicar'),
 ('gitignore',  'El .gitignore con la config local', 'correr instalar.py --aplicar'),
 ('version',    'La versión del estándar adoptada', 'fijarla en el CLAUDE.md')]
#  └─ id         └─ qué es                          └─ cómo se arregla

huella()
'7b12ee90aa31'

huella_instalada('C:/proyectos/pos')
'7b12ee90aa31'    # o '' si el proyecto no tiene la copia

sello()
'\n<!-- huella: 7b12ee90aa31 · estandar 5.0.0 -->\n'

# Cada comprobación retorna el par «cumple, detalle»:
_f13('C:/proyectos/pos', estandar)
(True, 'falta la carpeta `proyectos/` — el proyecto no está instalado')
#      └─ el detalle solo se usa cuando cumple es False

_gitignore('C:/proyectos/pos', estandar)
(False, 'al .gitignore le faltan: CLAUDE.md, .agente/')

_version('C:/proyectos/pos', estandar)
(True, '')

Punto('gitignore', 'El .gitignore', 'correr instalar.py', False,
      'al .gitignore le faltan: CLAUDE.md')
   .id        →  'gitignore'
   .cumple    →  False
   .detalle   →  'al .gitignore le faltan: CLAUDE.md'
   str(...)   →  '[FALTA] gitignore — al .gitignore le faltan: CLAUDE.md'

revisar('C:/proyectos/pos')
[Punto('f13',       ..., cumple=True),
 Punto('claude-md', ..., cumple=True),
 Punto('gitignore', ..., cumple=False, detalle='al .gitignore le faltan: ...'),
 Punto('version',   ..., cumple=False, detalle='el proyecto no declara ...')]

pendientes(puntos)
[Punto('gitignore', ...), Punto('version', ...)]     # solo los que no cumplen

resumen('C:/proyectos/pos', puntos)
'INSTALACIÓN INCOMPLETA · pos · 11 de 13 · falta: gitignore, version'

resumen('C:/proyectos/listo', puntos)
'Instalación del agente completa · listo · 13 de 13'

detalle(puntos)
'- **gitignore** — al .gitignore le faltan: CLAUDE.md, .agente/
   Se arregla así: correr instalar.py --aplicar
 - **version** — el proyecto no declara qué versión del estándar sigue
   Se arregla así: fijarla en el CLAUDE.md'

escribir_marca('C:/proyectos/pos', puntos)
'C:/proyectos/pos\.agente\INSTALACION-INCOMPLETA.md'

escribir_marca('C:/proyectos/listo', puntos)
''               # no faltaba nada: borró el archivo y no escribió ninguno
```
