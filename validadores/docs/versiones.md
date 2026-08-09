# `versiones.py`

Le pone una marca a cada documento que el proyecto copió del estándar, para poder decir después si quedó viejo. Y lleva el registro de cada actualización.

## Qué hace

Un proyecto hereda cuatro documentos del estándar. Con el tiempo el estándar los cambia, y hay que poder saber cuáles quedaron desactualizados.

La solución de este archivo es la **huella**: al final de cada documento copiado se escribe una línea con un código corto. Ese código no describe al documento: describe al **molde del que salió**. Comparando ese código con el del molde de hoy se sabe si el documento quedó viejo.

Se usa la huella y no otra cosa por dos motivos. Las fechas no sirven: cuando alguien se baja una copia del proyecto, todos los archivos quedan con la fecha de ese momento. Y comparar los textos tampoco: cada proyecto llena su documento con lo suyo, así que nunca son iguales.

Además escribe, en `documentacion/versiones/`, un archivo por cada actualización: de qué versión venía, a cuál pasó, qué documentos cambiaron y qué se aplicó.

## De qué depende y quién lo usa

```
versiones.py
   └── comun.py ··· RAIZ y leer
```

De Python usa `hashlib`, `os`, `re` y `datetime`.

Lo usan:

```
versiones.py
   ▲
   ├── checklist.py ··· lee las huellas para decidir qué reprueba
   ├── instalar.py ···· pone las huellas y escribe los registros
   ├── validar.py ····· cuando alguien pide revisar "versiones"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `CARPETA` | `documentacion/versiones`. Va ahí y no en `.agente/` porque a `.agente/` git lo ignora, y esta historia sí tiene que viajar con el proyecto. |
| `_SELLO` | Reconoce la línea de la huella dentro de un archivo. Al leerla, la versión del estándar puede faltar, para que una huella vieja se siga entendiendo. |
| `_REGISTRO` | Reconoce el nombre de un archivo de registro, con su fecha, su versión y el número que se le agrega si hubo dos el mismo día. |
| `COMPONENTES` | Los cuatro documentos que el proyecto recibe del estándar. |
| `POR_ID` | Los mismos, ordenados por su nombre corto para poder buscarlos rápido. |
| `AL_DIA`, `VIEJO`, `SIN_SELLO`, `FALTA` | Las cuatro situaciones en que puede estar un documento. |
| `_CABECERA_INDICE` | El comienzo del README de la carpeta de registros. |

Los cuatro documentos que se reciben del estándar:

| Nombre corto | Molde en el estándar | Dónde va en el proyecto | ¿Se pisa? |
|---|---|---|---|
| `claude-md` | `plantillas/CLAUDE.md.plantilla` | `CLAUDE.md` | No |
| `stack-instalacion` | `plantillas/stack-instalacion.md` | `.agente/stack-instalacion.md` | Sí |
| `historico` | `plantillas/historico-chat.md` | `historico-chat/README.md` | No |
| `recuerdos` | `plantillas/memoria.md` | `historico-chat/memory/memory.md` | No |

### La ficha `Componente`

Un documento que el proyecto recibe del estándar.

**`__init__(id, descripcion, plantilla, destino, se_pisa)`**

- **Recibe:** el nombre corto, la descripción, dónde está el molde en el estándar, dónde va la copia en el proyecto, y si el instalador la pisa o no.
- **Hace:** guarda los cinco valores.

**`ruta_plantilla(estandar=None)`**

- **Retorna:** dónde está exactamente el molde dentro del estándar.

**`ruta_destino(proyecto)`**

- **Retorna:** dónde está exactamente el documento dentro del proyecto.

### La ficha `Estado`

Cómo quedó un documento al compararlo con el estándar.

**`__init__(componente, situacion, sellada, actual)`**

- **Recibe:** el documento, la situación (`al-dia`, `viejo`, `sin-sello` o `falta`), la huella que traía escrita y la huella que tiene hoy el molde.

**`id`**

- **Retorna:** el nombre corto del documento.

**`al_dia`**

- **Retorna:** verdadero solo si la situación es `al-dia`.

**`mensaje()`**

- **Retorna:** el texto que explica el problema, según la situación. Texto vacío si está al día.

### Funciones de huellas y marcas

**`huella_texto(texto)`**

- **Recibe:** un texto.
- **Hace:** le calcula un resumen con SHA-256, que es una cuenta que convierte cualquier texto en un código de largo fijo y da un código distinto en cuanto el texto cambia aunque sea en una letra. Se queda con los primeros 12 caracteres.
- **Retorna:** ese código corto.

**`huella_central(componente, estandar=None)`**

- **Recibe:** un componente.
- **Retorna:** la huella de su plantilla en el estándar, o texto vacío si la plantilla no existe.

**`leer_sello(archivo)`**

- **Recibe:** la ruta de un archivo.
- **Hace:** busca todas las líneas de huella y se queda con la última.
- **Retorna:** un par «huella, versión del estándar». Dos textos vacíos si no hay huella o el archivo no existe.

**`huella_sellada(proyecto, componente)`**

- **Retorna:** solo la huella escrita en el documento del proyecto.

**`texto_sello(huella, version_estandar)`**

- **Retorna:** la línea de huella ya armada, lista para escribir.

**`quitar_sello(texto)`**

- **Recibe:** el contenido de un archivo.
- **Retorna:** el mismo contenido sin la línea de huella. Sirve para agregarle secciones al final y volver a ponerle la huella después, para que quede de última.

**`poner_sello(texto, huella, version_estandar)`**

- **Recibe:** el contenido, la huella y la versión.
- **Hace:** si ya había una huella, la reemplaza en su sitio; si no, agrega una al final.
- **Retorna:** el contenido con su huella al día. Nunca quedan dos.

### Funciones de estado

**`estado(proyecto, estandar=None)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** por cada documento compara la huella que tiene escrita con la de hoy.
- **Retorna:** una lista de fichas `Estado`, en el orden de `COMPONENTES`.

**`viejos(proyecto, estandar=None)`**

- **Retorna:** solo los estados que no están al día.

**`estado_de(proyecto, id, estandar=None)`**

- **Recibe:** la carpeta y el nombre corto de un documento.
- **Retorna:** el estado de ese documento, o nada si no existe.

### Funciones del registro

**`carpeta_registros(proyecto)`**

- **Retorna:** la ruta de `documentacion/versiones/` dentro del proyecto.

**`registros(proyecto)`**

- **Hace:** lee los nombres de archivo de la carpeta y los ordena por fecha, y por el número que llevan al final si hubo varios el mismo día.
- **Retorna:** una lista de tríos «nombre de archivo, fecha, versión», del más viejo al más nuevo.

**`version_registrada(proyecto)`**

- **Retorna:** la versión del último registro, o texto vacío.

**`version_sellada(proyecto)`**

- **Retorna:** la versión que dicen las huellas ya escritas, o texto vacío.

**`_nombre_libre(carpeta, fecha, version)`**

- **Retorna:** un nombre de archivo que no choque con otro que ya exista, agregándole un número si hubo dos el mismo día.

**`escribir_indice(proyecto)`**

- **Hace:** reescribe el `README.md` de la carpeta de registros con la tabla de todos.
- **Retorna:** la ruta del archivo escrito.

**`registrar(proyecto, version_nueva, antes, despues, pasos, pendientes=(), estandar=None, anterior=None)`**

- **Recibe:** la carpeta, la versión que se instala, las huellas de antes y de después, la lista de pasos aplicados, lo que quedó pendiente, la carpeta del estándar y de qué versión venía.
- **Hace:** compara las huellas de antes y de después y arma el documento con lo que cambió, los pasos y lo que quedó pendiente. Después actualiza el índice.
- **Retorna:** la ruta del archivo escrito.

De qué versión venía se lo tienen que decir, no lo calcula: cuando esta función corre, las huellas ya dicen la versión nueva y la anterior se perdió.

**`revisar_registro(proyecto, estandar=None)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** comprueba que la carpeta exista, que tenga al menos un registro y que la versión de las huellas sea la misma del último registro.
- **Retorna:** un par «cumple, detalle», que es lo que espera `checklist.py`.

## Cómo se ejecuta

Al instalar:

```
instalar.py
   ↓ antes de tocar nada: _huellas() → estado() → las huellas de ahora
   ↓ instala y le pone su huella a cada documento con poner_sello()
   ↓ después: _huellas() otra vez
   ↓ ¿cambió alguna? → registrar() escribe documentacion/versiones/<fecha>-<version>.md
```

Al revisar:

```
checklist.py
   ↓ estado_de(proyecto, "claude-md")
   ↓ compara la huella escrita contra la del molde
   ↓ si no son iguales → ese documento reprueba
```

A mano:

```
python validadores/validar.py versiones --raiz "C:/ruta/proyecto"
```

## Ejemplos de lo que retorna

```python
huella_texto('# Título\n\ncontenido\n')
'a3f9c21b04de'          # siempre 12 caracteres

huella_central(POR_ID['claude-md'])
'a3f9c21b04de'          # o '' si la plantilla no existe

texto_sello('a3f9c21b04de', '5.0.0')
'<!-- huella: a3f9c21b04de · estandar 5.0.0 -->'

leer_sello('C:/proyectos/pos/CLAUDE.md')
('a3f9c21b04de', '5.0.0')

leer_sello('C:/proyectos/pos/sin-marca.md')
('', '')

huella_sellada('C:/proyectos/pos', POR_ID['claude-md'])
'a3f9c21b04de'

quitar_sello('# Título\n\ntexto\n\n<!-- huella: a3f9 · estandar 5.0.0 -->\n')
'# Título\n\ntexto\n'

poner_sello('# Título\n\ntexto\n', 'a3f9c21b04de', '5.0.0')
'# Título\n\ntexto\n\n<!-- huella: a3f9c21b04de · estandar 5.0.0 -->\n'

Componente('claude-md', 'El CLAUDE.md del proyecto',
           'plantillas/CLAUDE.md.plantilla', 'CLAUDE.md', se_pisa=False)
   .id                 →  'claude-md'
   .se_pisa            →  False
   .ruta_plantilla()   →  'c:\…\agente\plantillas\CLAUDE.md.plantilla'
   .ruta_destino(p)    →  'C:/proyectos/pos\CLAUDE.md'

Estado(componente, VIEJO, 'a3f9c21b04de', 'ff01ab77cc10')
   .id        →  'claude-md'
   .al_dia    →  False
   .mensaje() →  '`CLAUDE.md` quedó viejo: la plantilla cambió en el estándar
                  (a3f9c21b04de → ff01ab77cc10)'

estado('C:/proyectos/pos')
[Estado(claude-md,         'al-dia'),
 Estado(stack-instalacion, 'viejo',     'a3f9…' → 'ff01…'),
 Estado(historico,         'sin-sello'),
 Estado(recuerdos,         'falta')]

viejos('C:/proyectos/pos')
[Estado(stack-instalacion, ...), Estado(historico, ...), Estado(recuerdos, ...)]

estado_de('C:/proyectos/pos', 'claude-md')
Estado(claude-md, 'al-dia')

estado_de('C:/proyectos/pos', 'no-existe')
None

carpeta_registros('C:/proyectos/pos')
'C:/proyectos/pos\documentacion\versiones'

registros('C:/proyectos/pos')
[('2026-08-01-4.0.0.md',   '2026-08-01', '4.0.0'),
 ('2026-08-09-5.0.0.md',   '2026-08-09', '5.0.0')]
#  └─ archivo               └─ fecha      └─ versión

version_registrada('C:/proyectos/pos')
'5.0.0'          # o '' si no hay ningún registro

version_sellada('C:/proyectos/pos')
'5.0.0'

escribir_indice('C:/proyectos/pos')
'C:/proyectos/pos\documentacion\versiones\README.md'

registrar('C:/proyectos/pos', '5.0.0', antes, despues, pasos)
'C:/proyectos/pos\documentacion\versiones\2026-08-09-5.0.0.md'

revisar_registro('C:/proyectos/pos')
(True, '')

revisar_registro('C:/proyectos/sin-registro')
(False, 'falta `documentacion/versiones/` con el registro de versiones')

revisar_registro('C:/proyectos/desfasado')
(False, 'lo instalado dice `5.0.0` y el último registro dice `4.0.0`:
         falta registrar la actualización')
```
