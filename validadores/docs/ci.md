# `ci.py`

Revisa que haya algo que, cada vez que llega un cambio, corra solo las pruebas y el revisor de estilo.

## Qué hace

Cuando alguien sube un cambio, no hay que confiar en que se acordó de probarlo: en un servidor de afuera arranca solo un proceso que baja el proyecto, corre las pruebas y pasa el **revisor de estilo**, que es una herramienta que marca el código mal escrito o mal ordenado. Si algo falla, avisa. A eso se le dice **integración continua**, y lo que hay que hacer en cada cambio se escribe en un archivo.

Este validador busca ese archivo entre los que git guarda. Reconoce ocho servicios distintos por dónde ponen el archivo, sin dar por hecho ninguno:

- GitHub Actions (`.github/workflows/*.yml`)
- GitLab (`.gitlab-ci.yml`)
- Azure (`azure-pipelines.yml`)
- Bitbucket (`bitbucket-pipelines.yml`)
- Jenkins (`Jenkinsfile`)
- CircleCI (`.circleci/config.yml`)
- Drone (`.drone.yml`)
- Travis (`.travis.yml`)

Después junta el contenido de todos y comprueba dos cosas: que se nombre en algún lado correr las pruebas, y correr el revisor de estilo.

Todo lo que reporta es **aviso**: el proyecto puede usar un servicio que no está en la lista, o el archivo puede llamar a un programa propio que por dentro sí hace las dos cosas.

## De qué depende y quién lo usa

```
ci.py
   ├── instalar.py ····· repositorios_git()
   ├── versionado.py ··· archivos_versionados()
   └── comun.py ········ AVISO, Hallazgo y leer
```

De Python usa `os` y `re`.

Lo usan:

```
ci.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "ci"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué reconoce |
|---|---|
| `_CI` | Los ocho sitios donde puede estar ese archivo. |
| `_CORRE_PRUEBAS` | Alguna palabra que signifique correr las pruebas: `test`, `tests`, `pruebas`, `phpunit`, `pytest`, `jest`, `vitest`, `artisan test`, `npm test` o `go test`. |
| `_CORRE_LINTER` | Alguna palabra que signifique correr el revisor de estilo: `lint`, `linter`, `pint`, `phpstan`, `psalm`, `eslint`, `prettier`, `ruff`, `flake8`, `rubocop` o `golangci`. |

### Funciones

**`revisar_ci(textos)`**

- **Recibe:** el contenido de todos los archivos encontrados.
- **Hace:**
  - Si no encontró ninguno, dice que no se ve nada que corra solo.
  - Si encontró, los junta todos y busca las dos palabras.
- **Retorna:** la lista de motivos. Vacía si está todo bien.

No toca git, así que se puede probar sin tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso diciéndolo.
  2. Por cada repositorio recorre los archivos que git guarda, se queda con los de la lista y los lee. Si alguno no se puede leer, lo salta.
  3. Le pasa todo a `revisar_ci` y arma un aviso por cada motivo que retorne.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py ci --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git()
   ↓
versionado.archivos_versionados()
   ↓
   ¿el archivo está en alguno de los 8 sitios conocidos?
        sí → se lee
   ↓
revisar_ci([contenido, contenido, ...])
   ↓
   ¿no se encontró ninguno?          → AVISO
   ¿se nombra correr las pruebas?    → si no, AVISO
   ¿se nombra el revisor de estilo?  → si no, AVISO
```

## Ejemplos de lo que retorna

```python
revisar_ci([])
['no se ve un pipeline de CI (G6): pruebas y linter deberían correr solos
  en cada cambio']

revisar_ci(['jobs:\n  test:\n    run: php artisan test\n    run: ./vendor/bin/pint'])
[]               # nombra las pruebas y el revisor de estilo

revisar_ci(['jobs:\n  test:\n    run: php artisan test'])
['el CI no parece correr el linter (G6)']

revisar_ci(['jobs:\n  lint:\n    run: eslint .'])
['el CI no parece correr las pruebas (G6)']

revisar_ci(['jobs:\n  build:\n    run: npm run build'])
['el CI no parece correr las pruebas (G6)',
 'el CI no parece correr el linter (G6)']

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'C:/proyectos/pos', 0,
          'no se ve un pipeline de CI (G6): pruebas y linter deberían correr
           solos en cada cambio')]

# con varios repositorios adentro de proyectos/, cada uno se reporta aparte:
validar('C:/espacio')
[Hallazgo(AVISO, 'proyectos/pos-back/', 0, 'el CI no parece correr el linter (G6)'),
 Hallazgo(AVISO, 'proyectos/pos-front/', 0, 'no se ve un pipeline de CI (G6): …')]

validar('C:/carpeta-sin-git')
[Hallazgo(AVISO, 'C:/carpeta-sin-git', 0, 'no hay repositorios git que revisar')]

validar('C:/proyectos/completo')
[]
```
