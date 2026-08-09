# `dependencias.py`

Revisa que, si el proyecto usa programas de afuera, esté guardado el archivo que dice qué versión exacta usa de cada uno.

## Qué hace

Ningún proyecto se escribe entero desde cero: usa programas hechos por otros. Eso se anota en dos archivos.

- La **lista de pedidos** dice qué programas se usan, en general: «necesito tal cosa, versión 4 o más nueva».
- La **lista de lo que llegó** anota la versión exacta que quedó instalada: «tal cosa, versión 4.2.7».

La segunda es la importante. Si está guardada, todos los computadores —y el servidor donde el sistema corre de verdad— instalan exactamente lo mismo. Si no está, cada uno recibe lo más nuevo que haya ese día, y aparece el clásico «en mi máquina funciona».

Este archivo comprueba una sola cosa: si git guarda una lista de pedidos, tiene que guardar también, al lado, su lista de lo que llegó.

Va de a dos con `versionado.py`, que revisa lo contrario: que **no** se guarden los programas ya instalados, que ocupan muchísimo. Acá se revisa que sí se guarde el papel con el que se vuelven a instalar igualitos.

Se mira lo que git guarda, no lo que hay en el disco: un archivo que está en el disco pero git no guarda no le llega a nadie más.

Todo lo que reporta es **aviso**: puede haber una razón, como un proyecto que todavía no usa nada de afuera.

## De qué depende y quién lo usa

```
dependencias.py
   ├── instalar.py ····· repositorios_git()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO y Hallazgo
```

De Python usa `os`.

Lo usan:

```
dependencias.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "dependencias"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

**`ECOSISTEMAS`** — cada lenguaje nombra estos dos archivos a su manera. Acá está la equivalencia; con que exista uno de los aceptados alcanza:

| Lista de pedidos | Listas de lo que llegó que valen | De qué lenguaje |
|---|---|---|
| `composer.json` | `composer.lock` | Composer / PHP |
| `package.json` | `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml` | npm / Node |
| `Pipfile` | `Pipfile.lock` | Pipenv |
| `pyproject.toml` | `poetry.lock`, `pdm.lock`, `uv.lock` | Python |
| `Gemfile` | `Gemfile.lock` | Bundler / Ruby |
| `go.mod` | `go.sum` | Go |
| `Cargo.toml` | `Cargo.lock` | Cargo / Rust |

**`_INSTALADO`** — las carpetas donde quedan los programas de afuera ya instalados: `vendor/` y `node_modules/`.

### Funciones

**`_es_instalado(ruta)`**

- **Recibe:** la dirección de un archivo.
- **Retorna:** verdadero si está adentro de `vendor/` o `node_modules/`, a cualquier profundidad.

Sirve para no confundirse: cada programa instalado trae su propia lista de pedidos adentro, y esas no son las del proyecto.

**`revisar(versionados, prefijo="")`**

- **Recibe:** la lista de archivos que git guarda y, si hace falta, qué ponerles adelante al nombrarlos.
- **Hace:** recorre la lista en orden; salta lo que está adentro de los programas ya instalados; y por cada archivo que sea una lista de pedidos conocida, comprueba que en la **misma carpeta** haya una de sus listas de lo que llegó.
- **Retorna:** la lista de avisos.

No toca git, así que se puede probar sin tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso diciéndolo.
  2. Por cada repositorio le pasa a `revisar` la lista de archivos que git guarda.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py dependencias --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git()
   ↓
versionado.archivos_versionados()   ← git ls-files
   ↓
revisar(lista, prefijo)
   ↓
   por cada archivo que git guarda:
        ¿está adentro de vendor/ o node_modules/? → se salta
        ¿es una lista de pedidos conocida?
             sí ↓
        ¿git guarda también su lista de lo que
           llegó, en la misma carpeta?
             no → AVISO
```

## Ejemplos de lo que retorna

```python
_es_instalado('vendor/laravel/framework/composer.json')      →  True
_es_instalado('node_modules/axios/package.json')             →  True
_es_instalado('paquetes/mi-libreria/vendor/otro/x.json')     →  True
_es_instalado('composer.json')                               →  False

revisar(['composer.json', 'composer.lock', 'app/Pago.php'])
[]               # la lista de pedidos tiene su lista de lo que llegó

revisar(['composer.json', 'app/Pago.php'])
[Hallazgo(AVISO, 'composer.json', 0,
          'Composer/PHP: hay `composer.json` pero no un lockfile versionado
           (composer.lock) · DEP2')]

revisar(['package.json', 'yarn.lock'])
[]               # cualquiera de los tres aceptados sirve

revisar(['package.json', 'frontend/package-lock.json'])
[Hallazgo(AVISO, 'package.json', 0,
          'npm/Node: hay `package.json` pero no un lockfile versionado
           (package-lock.json o yarn.lock o pnpm-lock.yaml) · DEP2')]
# el archivo tiene que estar en la MISMA carpeta

revisar(['vendor/laravel/framework/composer.json'])
[]               # es de un programa ya instalado, no del proyecto

revisar(['composer.json'], prefijo='pos-back/')
[Hallazgo(AVISO, 'pos-back/composer.json', 0, 'Composer/PHP: hay `composer.json`…')]

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'composer.json', 0, 'Composer/PHP: hay `composer.json` pero
          no un lockfile versionado (composer.lock) · DEP2')]

validar('C:/carpeta-sin-git')
[Hallazgo(AVISO, 'C:/carpeta-sin-git', 0, 'no hay repositorios git que revisar')]
```
