# `codigo.py`

Abre los archivos de código del proyecto y los va pasando de a uno, con su nombre y su contenido, a los programas que los revisan.

## Qué hace

Seis revisores necesitan lo mismo: recorrer el código del proyecto y mirar qué dice adentro. En vez de que cada uno lo resuelva por su lado, ese trabajo se hace acá una sola vez.

Se le pasa la carpeta del proyecto y va entregando, de a uno, el nombre del archivo y su contenido. Antes de entregar cada uno decide si vale la pena abrirlo:

1. Solo entrega archivos que **git tiene registrados**. Git es el programa que guarda la historia del proyecto y sabe qué archivos forman parte de él; un archivo suelto en el disco, que git no registró, no cuenta, porque quien se baje una copia del proyecto no lo va a recibir.
2. Solo entrega archivos de código. Los reconoce por la extensión, que son las últimas letras del nombre: `.py`, `.js`, `.php`.
3. Salta lo que no escribió nadie del equipo: lo que viene de afuera y lo que arma sola una herramienta.
4. Si un archivo no se puede leer, lo salta callado.

También ofrece una ayuda pequeña: dado un punto cualquiera dentro del texto, dice en qué línea cae.

## De qué depende y quién lo usa

```
codigo.py
   ├── instalar.py ····· le pide la lista de repositorios del proyecto
   ├── versionado.py ··· le pide la lista de archivos que git tiene registrados
   └── comun.py ········ le pide la función de leer archivos
```

Un **repositorio** es una carpeta cuya historia guarda git. Un proyecto puede tener varios.

Lo usan seis revisores:

```
codigo.py
   ▲
   ├── calidad.py ······ funciones muy largas
   ├── errores.py ······ errores que se atrapan y se tiran a la basura
   ├── rendimiento.py ·· consultas que piden de más y consultas repetidas de a miles
   ├── seguridad.py ···· consultas armadas pegando texto
   ├── aislamiento.py ·· pruebas que dependen del azar
   └── esquema.py ······ solo le pide en qué línea cae un punto del texto
```

De Python usa `os` y `re`.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `EXTENSIONES` | Los finales de nombre que se abren: `.php`, `.py`, `.js`, `.ts`, `.jsx`, `.tsx`, `.mjs`, `.cjs`, `.vue`, `.rb`, `.go`, `.java`, `.kt`, `.cs`, `.rs`, `.swift`, `.scala` y `.sql`. |
| `_SALTAR` | Lo que se descarta sin abrirlo: las carpetas donde vive el código que viene de afuera o lo que arma sola una herramienta (`vendor`, `node_modules`, `dist`, `build`, `.git`, `public`, `static`, `staticfiles`) y los archivos terminados en `.min.js` o `.min.css`. |

`secretos.py` tiene su propia lista, más amplia, porque una contraseña puede estar en un archivo de ajustes y no solo en código.

### Funciones

**`linea_de(texto, pos)`**

- **Recibe:** el texto completo de un archivo y un punto dentro de ese texto (contado por caracteres, desde el comienzo).
- **Hace:** cuenta cuántos saltos de línea hay antes de ese punto.
- **Retorna:** el número de línea, empezando en 1.

Sirve para los revisores que leen el archivo entero de una sola pasada —así encuentran cosas repartidas en varias líneas— y aun así tienen que decir en qué línea está lo que encontraron.

**`archivos(raiz, extensiones=None)`**

- **Recibe:** la carpeta del proyecto y, si se quiere, otra lista de finales de nombre en lugar de la de arriba.
- **Hace:**
  1. Le pregunta a `instalar.py` qué repositorios hay dentro de esa carpeta.
  2. Para cada repositorio decide cómo mostrar los nombres de archivo: si el repositorio es la carpeta misma, se muestran tal cual; si está adentro de `proyectos/`, se les pone adelante el nombre de esa subcarpeta.
  3. Le pregunta a `versionado.py` qué archivos tiene registrados ese repositorio.
  4. Descarta los que caen en `_SALTAR` y los que no terminan como pide la lista.
  5. Lee cada uno; si la lectura falla, lo salta.
- **Retorna:** de a un par por vez: el nombre que se va a mostrar y el contenido del archivo.

## Cómo se ejecuta

Los revisores que lo usan hacen todos lo mismo:

```
errores.validar(carpeta_del_proyecto)
        │
        ▼
for ruta, texto in codigo.archivos(carpeta):
        │
        │   dentro de archivos():
        │      instalar.repositorios_git()  → qué repositorios hay
        │      versionado.archivos_versionados() → qué archivos registra git
        │      se descarta lo que no se va a abrir
        │      comun.leer() → el contenido
        ▼
   revisar_texto(texto, ruta, hallazgos)   ← acá cada revisor aplica su regla
        │
        ▼
   lista de Hallazgo
```

Un **hallazgo** es cada cosa que el revisor encontró mal, con el archivo y la línea donde está.

## Ejemplos de lo que retorna

```python
EXTENSIONES
{'.php', '.py', '.js', '.ts', '.jsx', '.tsx', '.mjs', '.cjs', '.vue',
 '.rb', '.go', '.java', '.kt', '.cs', '.rs', '.swift', '.scala', '.sql'}

linea_de('primera\nsegunda\ntercera', 8)
2        # el carácter 8 cae en la segunda línea

linea_de('primera\nsegunda\ntercera', 0)
1

list(archivos('C:/proyectos/pos'))
[('app/Http/Controllers/PagoController.php', '<?php\n\nnamespace App\Http...'),
 ('app/Models/Factura.php',                  '<?php\n\nnamespace App\Models...'),
 ('resources/js/app.js',                     'import "./bootstrap";\n...')]
#  └─ la ruta a mostrar          └─ el contenido completo del archivo

# con varios repositorios adentro de proyectos/, la ruta lleva el prefijo:
list(archivos('C:/espacio'))
[('proyectos/pos-back/app/Models/Factura.php',  '<?php ...'),
 ('proyectos/pos-front/src/main.ts',            'import { createApp } ...')]

# lo que NO aparece nunca en el resultado:
#   vendor/laravel/framework/src/Foo.php   → carpeta de terceros
#   public/js/app.min.js                   → generado y minificado
#   README.md                              → no es extensión de código
#   notas.php sin agregar a git            → git no lo tiene registrado
```
