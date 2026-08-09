# `rama.py`

Revisa que el trabajo se esté haciendo en una copia aparte, y que esa copia esté al día.

## Qué hace

Git permite trabajar en varias versiones del proyecto a la vez. Cada una es una **rama**. Hay una rama **principal**, que es la buena, la que se publica; y para hacer un cambio se abre una rama aparte, se trabaja ahí, y cuando está listo y probado se junta con la principal. Así, si algo sale mal, lo que está publicado no se rompió nunca.

Este validador señala tres situaciones:

1. **Se está trabajando directo sobre la principal.** Debería ser en una rama aparte.
2. **La rama aparte quedó atrasada.** Mientras se trabajaba, a la principal le entraron cambios que esta rama no tiene. Cuanto más se espere, más difícil es juntarlas.
3. **No se está en ninguna rama.** Git quedó parado sobre un punto suelto de la historia, y lo que se escriba ahí es fácil de perder.

No da por hecho cómo se llama la rama principal. Primero le pregunta al servidor cuál es; si no hay servidor, prueba con los nombres más usados: `main`, `master`, `trunk` y `develop`.

Todo lo que reporta es **aviso**: trabajar sobre la principal puede estar decidido así, y estar un poco atrás es un recordatorio, no algo que deba frenar a nadie.

## De qué depende y quién lo usa

```
rama.py
   ├── instalar.py ··· repositorios_git()
   └── comun.py ······ AVISO y Hallazgo
```

De Python usa `os` y `subprocess` (para llamar a git).

No usa `versionado.py`: no le importan los archivos, solo cómo están las ramas.

Lo usan:

```
rama.py
   ▲
   ├── validar.py ··· cuando alguien pide revisar "rama"
   └── pruebas.py
```

## Qué tiene adentro

### Funciones

**`_git(repo, *args)`**

- **Recibe:** la carpeta del repositorio y qué hay que preguntarle a git.
- **Hace:** corre git ahí.
- **Retorna:** las líneas de la respuesta, sin las vacías. Si git falla, no retorna nada.

**`rama_actual(repo)`**

- **Recibe:** la carpeta del repositorio.
- **Retorna:** en qué rama se está trabajando. Si no se está en ninguna, retorna la palabra `HEAD`.

**`rama_principal(repo)`**

- **Recibe:** la carpeta del repositorio.
- **Hace:** primero le pregunta al servidor cuál es la principal. Si no hay servidor, prueba los nombres más usados, uno por uno, y se queda con el primero que exista.
- **Retorna:** el nombre, o nada si no lo pudo averiguar.

**`commits_detras(repo, principal)`**

- **Recibe:** la carpeta del repositorio y el nombre de la principal.
- **Hace:** cuenta cuántos cambios tiene la principal que esta rama no tiene. Mira primero la copia que hay en este computador; si la principal solo existe en el servidor, mira la del servidor.
- **Retorna:** ese número, o cero si no lo pudo contar.

**`evaluar(actual, principal, detras, donde="")`**

- **Recibe:** en qué rama se está, cuál es la principal, cuántos cambios está atrás y cómo nombrar el repositorio al reportar.
- **Hace:** decide en este orden:
  1. Si la rama actual es `HEAD`, avisa que no se está en ninguna rama.
  2. Si no pudo averiguar alguno de los dos nombres, no dice nada.
  3. Si se está trabajando en la principal, lo avisa.
  4. Si está atrasada, lo avisa diciendo por cuántos cambios.
- **Retorna:** la lista de hallazgos.

No toca git, así que se puede probar sin tener un proyecto de verdad.

**`validar(raiz)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:**
  1. Busca los repositorios. Si no hay ninguno, retorna un aviso diciéndolo.
  2. Por cada uno averigua en qué rama está, cuál es la principal y cuántos cambios está atrás, y se lo pasa a `evaluar`.
- **Retorna:** la lista de hallazgos.

## Cómo se ejecuta

```
python validadores/validar.py rama --raiz "C:/ruta/proyecto"
```

Por dentro:

```
validar(carpeta)
   ↓
instalar.repositorios_git()
   ↓
   por cada repositorio:
        rama_actual()     ¿en qué rama se está?
        rama_principal()  primero el servidor, después main/master/trunk/develop
        commits_detras()  ¿cuántos cambios de la principal le faltan?
        ↓
        evaluar(actual, principal, detras)
             es "HEAD"               → AVISO: no se está en ninguna rama
             es la principal         → AVISO: hay que trabajar en una aparte
             le faltan cambios       → AVISO: está N cambios atrás
```

## Ejemplos de lo que retorna

```python
_git('C:/proyectos/pos', 'rev-parse', '--abbrev-ref', 'HEAD')
['feature/pagos-anulados']

_git('C:/carpeta-sin-git', 'status')
[]               # git falló: lista vacía

rama_actual('C:/proyectos/pos')
'feature/pagos-anulados'

rama_actual('C:/proyectos/desprendido')
'HEAD'           # no está parado en ninguna rama

rama_principal('C:/proyectos/pos')
'main'           # lo dijo el remoto, o se encontró como rama local

rama_principal('C:/proyectos/raro')
None             # no se pudo averiguar

commits_detras('C:/proyectos/pos', 'main')
7                # main tiene 7 commits que esta rama no

evaluar('feature/pagos', 'main', 0, 'pos/')
[]               # rama aparte y al día: nada que decir

evaluar('main', 'main', 0, 'pos/')
[Hallazgo(AVISO, 'pos/', 0,
          'se está trabajando en la rama principal `main`; G4 pide una rama
           dedicada (salvo que la capa 3 lo permita)')]

evaluar('feature/pagos', 'main', 7, 'pos/')
[Hallazgo(AVISO, 'pos/', 0,
          'la rama `feature/pagos` está 7 commit(s) detrás de `main`;
           G4 pide mantenerla al día')]

evaluar('HEAD', 'main', 0, 'pos/')
[Hallazgo(AVISO, 'pos/', 0, 'HEAD desprendido: no se está en una rama (G4)')]

evaluar('cualquiera', None, 0, 'pos/')
[]               # no se sabe cuál es la principal: no se opina

validar('C:/proyectos/pos')
[Hallazgo(AVISO, 'C:/proyectos/pos', 0,
          'se está trabajando en la rama principal `main`; G4 pide una rama
           dedicada (salvo que la capa 3 lo permita)')]

validar('C:/carpeta-sin-git')
[Hallazgo(AVISO, 'C:/carpeta-sin-git', 0, 'no hay repositorios git que revisar')]
```
