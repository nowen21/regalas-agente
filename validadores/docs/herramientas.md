# `herramientas.py`

Corre las herramientas que el proyecto ya tiene y cuenta qué dijeron.

## Qué hace

Este es distinto de todos los demás. Los otros leen archivos y deciden por su cuenta; este **llama a un programa de afuera**, lo deja trabajar y traduce su respuesta.

Llama a tres cosas:

| Función | Qué corre |
|---|---|
| `linter` | El **revisor de estilo**: marca el código mal escrito o mal ordenado. |
| `suite` | Las **pruebas** del proyecto: los programas chicos que comprueban que todo siga funcionando. |
| `auditoria` | El **buscador de fallas conocidas**: revisa si alguno de los programas de afuera que usa el proyecto tiene un agujero de seguridad ya reportado. |

Cada lenguaje tiene su propia herramienta para cada cosa, así que primero averigua cuál usa este proyecto y después la llama.

Para saberlo busca, entre los archivos que git guarda, la lista de programas de afuera (`composer.json`, `package.json`, `pyproject.toml`…) y corre la herramienta **en la carpeta donde está esa lista**. Un mismo proyecto puede tener varias.

Si no encuentra la herramienta, lo dice; no se inventa nada.

Estas tres no se corren solas cada rato: dependen de qué esté instalado, se demoran, y dejan huella —las pruebas tocan la base de datos, y el buscador de fallas sale a internet—. Se corren cuando alguien las pide.

## De qué depende y quién lo usa

```
herramientas.py
   ├── instalar.py ····· repositorios_git()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO, FALLA y Hallazgo
```

De Python usa `os`, `shutil` y `subprocess`.

Lo usan:

```
herramientas.py
   ▲
   ├── validar.py ··· cuando alguien pide "linter", "suite" o "audit"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `MANIFIESTOS` | Con qué lenguaje está hecho el proyecto, según el archivo que se encuentre: `composer.json` es PHP; `package.json` es Node; `pyproject.toml`, `requirements.txt` y `Pipfile` son Python; `Gemfile` es Ruby; `go.mod` es Go. |
| `_INSTALADO` | Las carpetas donde quedan los programas de afuera ya instalados: `vendor/` y `node_modules/`. |

### Funciones para averiguar con qué está hecho

**`stack_de_manifiesto(nombre)`**

- **Recibe:** el nombre de un archivo.
- **Retorna:** de qué lenguaje es, o nada si no lo reconoce.

**`_es_instalado(ruta)`**

- **Recibe:** la dirección de un archivo.
- **Retorna:** verdadero si está adentro de `vendor/` o `node_modules/`.

**`proyectos(repo)`**

- **Recibe:** la carpeta de un repositorio.
- **Hace:** recorre los archivos que git guarda, salta los de los programas de afuera y anota en qué carpeta encontró cada lista.
- **Retorna:** una lista ordenada de pares «carpeta, con qué lenguaje está hecha».

### Funciones de ejecución

**`_bin_local(carpeta, nombre)`**

- **Recibe:** una carpeta y el nombre de una herramienta.
- **Hace:** la busca en `vendor/bin` y en `node_modules/.bin`, que es donde quedan instaladas. En Windows prueba primero los nombres terminados en `.bat`, `.cmd` y `.exe`, porque el archivo sin nada al final está escrito para otro sistema y en Windows no arranca.
- **Retorna:** dónde está la herramienta, o nada.

**`_correr(carpeta, args, timeout)`**

- **Recibe:** en qué carpeta correr, qué correr, y cuántos segundos esperarla como máximo.
- **Hace:** si lo que hay que correr es un nombre suelto como `composer` o `npm`, lo busca entre los programas que el computador ya conoce. Después lo corre en esa carpeta.
- **Retorna:** un par «cómo terminó, qué escribió en pantalla». Si no se pudo correr, retorna el motivo: puede ser que la herramienta no esté instalada o que se haya demorado más de la cuenta.

**`_resumen(salida, lineas=2, tope=200)`**

- **Recibe:** todo lo que la herramienta escribió, cuántas líneas dejar y el largo máximo.
- **Hace:** se queda con las últimas líneas que dicen algo. Si el texto pasa del largo, lo corta.
- **Retorna:** ese resumen.

### Cómo se elige qué correr

Las tres reciben la carpeta y con qué lenguaje está hecha, y retornan «cómo se llama y qué hay que correr», o nada si no encontraron la herramienta.

**`_cmd_linter(carpeta, stack)`** — en PHP prueba pint, después phpstan, después php-cs-fixer. En Node prueba eslint y después prettier. En Python prueba ruff y después flake8.

**`_cmd_suite(carpeta, stack)`** — en PHP busca phpunit. En Node siempre usa `npm test`. En Python busca pytest.

**`_cmd_audit(carpeta, stack)`** — en PHP siempre usa `composer audit`. En Node siempre `npm audit`. En Python busca pip-audit.

### El motor que comparten

**`_validar(raiz, elegir_cmd, regla, falla_si_rc, timeout)`**

- **Recibe:** la carpeta del proyecto, la función que elige qué correr, qué regla se está comprobando, si un mal resultado cuenta como falla o solo como aviso, y cuánto esperar.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso.
  2. Por cada carpeta con lista de programas de afuera, elige qué correr.
  3. Si no hay herramienta → aviso.
  4. Si la hay, la corre. Si no arrancó → aviso con el motivo. Si terminó mal → falla o aviso, según se haya pedido, con el resumen de lo que dijo.
- **Retorna:** la lista de hallazgos.

### Las tres que se pueden llamar desde afuera

| Función | ¿Falla si la herramienta termina mal? | Cuánto se la espera |
|---|---|---|
| `linter(raiz)` | No, solo avisa | 300 segundos |
| `suite(raiz)` | **Sí** | 600 segundos |
| `auditoria(raiz)` | No, solo avisa | 180 segundos |

Las pruebas son las únicas que reprueban: que una prueba falle es un hecho, no una opinión discutible.

## Cómo se ejecuta

```
python validadores/validar.py linter --raiz "C:/ruta/proyecto"
python validadores/validar.py suite  --raiz "C:/ruta/proyecto"
python validadores/validar.py audit  --raiz "C:/ruta/proyecto"
```

Por dentro:

```
linter(carpeta)
   ↓
_validar(carpeta, _cmd_linter, "Q6", falla_si_rc=False, timeout=300)
   ↓
instalar.repositorios_git()
   ↓
proyectos(repo)   ← busca composer.json, package.json, pyproject.toml...
   ↓
   por cada carpeta encontrada:
        _cmd_linter(carpeta, lenguaje)
             php    → busca pint, phpstan, php-cs-fixer en vendor/bin
             node   → busca eslint, prettier en node_modules/.bin
             python → busca ruff, flake8
        ↓
        ¿no está la herramienta?  → AVISO
        ↓
        _correr(carpeta, que_correr, 300)
             no arrancó           → AVISO con el motivo
             terminó mal          → AVISO con el resumen de lo que dijo
             terminó bien         → no se dice nada
```

## Ejemplos de lo que retorna

```python
stack_de_manifiesto('composer.json')     →  'php'
stack_de_manifiesto('package.json')      →  'node'
stack_de_manifiesto('pyproject.toml')    →  'python'
stack_de_manifiesto('README.md')         →  None

_es_instalado('vendor/laravel/framework/composer.json')  →  True
_es_instalado('composer.json')                           →  False

proyectos('C:/proyectos/pos')
[('C:\proyectos\pos', 'php'),
 ('C:\proyectos\pos\frontend', 'node')]
#  └─ en qué carpeta correr        └─ con qué está hecha

_bin_local('C:/proyectos/pos', 'pint')
'C:/proyectos/pos\vendor\bin\pint.bat'     # en Windows

_bin_local('C:/proyectos/pos', 'no-instalado')
None

_correr('C:/proyectos/pos', ['…/vendor/bin/pint.bat', '--test'], 300)
(1, 'FAIL  app/Models/Factura.php\n  ⨯ no_unused_imports\n2 files, 1 problem')
#  └─ terminó mal   └─ lo que escribió en pantalla

_correr('C:/proyectos/pos', ['…/vendor/bin/pint.bat', '--test'], 300)
(0, 'PASS  ................ 42 files')      # terminó bien

_correr('C:/proyectos/pos', ['pint'], 300)
(None, 'herramienta no encontrada')

_correr('C:/proyectos/pos', ['…/phpunit'], 600)
(None, 'tiempo agotado (600s)')

_resumen('línea uno\nlínea dos\nlínea tres')
'línea dos · línea tres'

_resumen('')
'sin salida'

_cmd_linter('C:/proyectos/pos', 'php')
('pint', ['C:/proyectos/pos\vendor\bin\pint.bat', '--test'])
#  └─ cómo se llama   └─ qué se corre

_cmd_linter('C:/proyectos/pos', 'go')
(None, None)     # no hay herramienta prevista para ese lenguaje

_cmd_suite('C:/proyectos/pos/frontend', 'node')
('npm test', ['npm', 'test', '--silent'])

_cmd_audit('C:/proyectos/pos', 'php')
('composer audit', ['composer', 'audit', '--no-interaction', '--format=plain'])

linter('C:/proyectos/pos')
[Hallazgo(AVISO, '.', 0,
          'pint reporta problemas — FAIL app/Models/Factura.php · 2 files,
           1 problem (Q6)')]

suite('C:/proyectos/pos')
[Hallazgo(FALLA, '.', 0,
          'phpunit reporta problemas — FAILURES! · Tests: 42, Failures: 1 (T5)')]
# esta es la única de las tres que reprueba

auditoria('C:/proyectos/pos')
[Hallazgo(AVISO, '.', 0,
          'composer audit reporta problemas — Found 2 security vulnerability
           advisories affecting 1 package (DEP3)')]

linter('C:/proyectos/limpio')
[]               # la herramienta corrió y no encontró nada

linter('C:/proyectos/sin-herramienta')
[Hallazgo(AVISO, '.', 0, 'php: no se encontró herramienta para Q6')]
```
