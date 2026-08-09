# `versionado.py`

Le pregunta a git qué archivos está guardando y marca los que no deberían estar ahí: contraseñas, claves, programas de afuera y archivos que se arman solos.

## Qué hace

Git es el programa que guarda la historia del proyecto: qué archivo cambió, cuándo y quién lo cambió. Un **repositorio** es la carpeta cuya historia guarda git.

Este validador revisa la regla `G3` del capítulo de git: al repositorio no se suben las contraseñas, ni los datos de gente de verdad, ni lo que se arma solo, ni los ajustes de la máquina de cada quien.

La pregunta no es «¿está el archivo en el disco?» sino «¿git lo está guardando?». Un archivo puede estar en la carpeta y que git lo esté ignorando a propósito; eso no es un problema. El problema es que git lo guarde.

Una contraseña subida a git se reporta como **falla** y no como aviso, porque borrarla después no alcanza: queda en la historia, y esa historia ya la tiene en su computador cada persona que se bajó una copia del proyecto.

Además de revisar, este archivo es el que **le pregunta a git qué archivos hay**, y por eso lo usan otros nueve validadores aunque no les interese la regla `G3`.

## De qué depende y quién lo usa

```
versionado.py
   └── comun.py ··· le pide Hallazgo, FALLA y AVISO
```

De Python usa `os`, `re` y `subprocess` (para llamar a git).

Lo usan diez archivos. Casi todos solo por la función `archivos_versionados`:

```
versionado.py
   ▲
   ├── codigo.py ········ le pide la lista de archivos registrados
   ├── secretos.py ······ ídem
   ├── dependencias.py ·· ídem
   ├── migraciones.py ··· ídem
   ├── esquema.py ······· ídem
   ├── aislamiento.py ··· ídem
   ├── ci.py ············ ídem
   ├── herramientas.py ·· ídem
   ├── validar.py ······· lo llama cuando alguien pide revisar "versionado"
   └── pruebas.py ······· comprueba que clasifique bien
```

Guardar un cambio en git se llama hacer un **commit**. También llama a este archivo el `pre-commit`, un programa que git arranca solo justo antes de guardar —a eso se le dice **enganche**— y que instala `instalar.py`. En ese caso revisa solo lo que entra en ese cambio.

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `EJEMPLOS` | Reconoce los nombres de archivos que son un molde vacío para copiar (`.example`, `.sample`, `.template`, `.dist`, `.ejemplo`, `.plantilla`). Esos sí deben estar guardados: no traen ningún dato secreto, solo muestran qué hay que llenar. |
| `PROHIBIDO` | Pares «cómo se reconoce, por qué está mal» de lo que es **falla**: los archivos `.env`, que son donde se guardan las contraseñas de cada máquina; la carpeta `node_modules/`, donde se instalan los programas de afuera; los archivos de clave (`.pem`, `.key`, `.p12`, `.pfx`, `.jks`, `.keystore`, `.ppk`); las claves privadas con que un computador se identifica ante otro sin contraseña; y los archivos que guardan el usuario y la clave para publicar código (`.npmrc`, `.pypirc`, `.netrc`). |
| `DUDOSO` | Pares «cómo se reconoce, por qué conviene mirarlo» de lo que es **aviso**: los `.log`, que son el diario de lo que fue pasando; bases de datos sueltas; las carpetas `.idea/` y `.vscode/`, que son los ajustes del editor de cada quien; los archivos que Python arma solo; las carpetas `dist/` y `build/`, con el resultado ya armado; y basura del sistema como `.DS_Store`. |
| `MINIMO_INSERTS` | `5`. Cuántas órdenes `INSERT INTO` —cada una mete una fila de datos— hacen pensar que el archivo `.sql` no trae solo la forma de las tablas sino también su contenido. |
| `_INSERT` | La búsqueda de `INSERT INTO`. |

### Funciones

**`_git(repo, *args)`**

- **Recibe:** la carpeta del repositorio y los argumentos del comando git.
- **Hace:** ejecuta git en esa carpeta.
- **Retorna:** la lista de líneas de la salida, sin las vacías. Si git falla, retorna una lista vacía.

**`archivos_versionados(repo)`**

- **Recibe:** la carpeta de un repositorio.
- **Hace:** ejecuta `git ls-files`.
- **Retorna:** la lista de rutas que git tiene registradas.

Es la función más usada del archivo. Nueve validadores empiezan por acá.

**`archivos_preparados(repo)`**

- **Recibe:** la carpeta de un repositorio.
- **Hace:** ejecuta `git diff --cached`, o sea pregunta qué entra en el commit que se está por hacer.
- **Retorna:** la lista de rutas que entran en ese commit.

La usa el enganche de git antes de aceptar un commit, para revisar solo lo que entra ahora.

**`_es_volcado_con_datos(ruta_absoluta)`**

- **Recibe:** la ruta completa de un archivo `.sql`.
- **Hace:** lee hasta 2 MB del archivo y cuenta cuántos `INSERT INTO` tiene.
- **Retorna:** verdadero si hay 5 o más. Si el archivo no se puede leer, retorna falso.

Sirve para separar dos cosas que se parecen: un `.sql` que solo dice **cómo son** las tablas —ese sí se guarda— y uno que además trae adentro las filas, que pueden ser datos de gente de verdad.

**`_es_vendor_de_dependencias(ruta)`**

- **Recibe:** una ruta.
- **Hace:** mira si empieza por `vendor/`.
- **Retorna:** verdadero o falso.

Hay dos carpetas llamadas igual y son cosas distintas. La `vendor/` que está al comienzo del proyecto la llena sola la herramienta que instala los programas de afuera, y no se guarda. Una `static/vendor/` o `assets/vendor/`, más adentro, la copió alguien a propósito, y esa sí.

**`clasificar(repo, archivo)`**

- **Recibe:** la carpeta del repositorio y la ruta de un archivo registrado.
- **Hace:** decide en este orden:
  1. Si el nombre es de un molde vacío → está bien, no dice nada.
  2. Si empieza por `vendor/` → falla: son programas de afuera instalados.
  3. Si se parece a algo de `PROHIBIDO` → falla.
  4. Si tiene `/vendor/` más adentro → está bien, no dice nada.
  5. Si es `.sql` → falla solo si trae datos adentro; si no, está bien.
  6. Si se parece a algo de `DUDOSO` → aviso.
- **Retorna:** un par «gravedad, motivo», o nada si el archivo está bien versionado.

**`validar(repo, ruta_mostrada=None, solo_preparados=False)`**

- **Recibe:** la carpeta del repositorio; opcionalmente cómo mostrar la ruta en los mensajes; y opcionalmente la orden de mirar solo lo que entra en el commit.
- **Hace:**
  1. Pide la lista de archivos (todos, o solo los del commit).
  2. Clasifica cada uno y arma un hallazgo por cada problema.
  3. Si está revisando el repositorio completo y encuentra un `.env` en el disco, comprueba además que esté guardado su molde vacío. Sin ese molde, quien se baje el proyecto no sabe qué datos tiene que poner.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

Desde la consola:

```
python validadores/validar.py versionado --raiz "C:/ruta/proyecto"
```

Desde el enganche de git, antes de cada commit:

```
git commit
   ↓
.githooks/pre-commit
   ↓
validar.py versionado --preparados
   ↓
versionado.validar(repo, solo_preparados=True)
   ↓
git diff --cached  →  clasificar() archivo por archivo
   ↓
si hay una FALLA, el commit se rechaza
```

## Ejemplos de lo que retorna

```python
_git('C:/proyectos/pos', 'ls-files')
['.env.example', 'app/Models/Factura.php', 'composer.json', 'composer.lock']

archivos_versionados('C:/proyectos/pos')
['.env.example', 'app/Models/Factura.php', 'composer.json', 'composer.lock']

archivos_preparados('C:/proyectos/pos')
['app/Models/Factura.php']        # solo lo que entra en este commit

_es_volcado_con_datos('C:/proyectos/pos/db/respaldo.sql')
True          # tiene 5 o más INSERT INTO
_es_volcado_con_datos('C:/proyectos/pos/db/esquema.sql')
False         # solo estructura

_es_vendor_de_dependencias('vendor/laravel/framework/src/Foo.php')
True
_es_vendor_de_dependencias('public/vendor/bootstrap/bootstrap.css')
False

clasificar(repo, '.env')
('FALLA', 'entorno real con valores')

clasificar(repo, 'storage/app.log')
('AVISO', 'registro generado')

clasificar(repo, '.env.example')
None          # es el molde sin valores: así debe estar

clasificar(repo, 'app/Models/Factura.php')
None          # está bien versionado

validar('C:/proyectos/pos', 'pos/')
[Hallazgo(FALLA, 'pos/', 0, 'versionado y no debería (entorno real con valores): .env'),
 Hallazgo(AVISO, 'pos/', 0, '¿debería estar versionado? (registro generado): storage/app.log')]

# impreso, esos dos hallazgos se ven así:
[FALLA] pos/ — versionado y no debería (entorno real con valores): .env
[AVISO] pos/ — ¿debería estar versionado? (registro generado): storage/app.log

validar('C:/proyectos/limpio')
[]            # nada que reportar
```
