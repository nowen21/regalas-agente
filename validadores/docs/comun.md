# `comun.py`

Guarda lo que comparten casi todos los demás archivos: cómo se anota un problema encontrado, qué tan grave es, cómo se leen los documentos de texto y cómo se muestra el resultado al final.

## Qué hace

Este archivo no revisa nada. Es la caja de herramientas del resto.

Cuando un validador encuentra algo mal, no lo escribe en pantalla ahí mismo: arma con él un `Hallazgo`, que es la ficha de acá donde queda anotado el problema, en qué archivo y en qué línea.

Los documentos del proyecto están escritos en **markdown**, que es texto normal con unas pocas marcas: `#` para los títulos, `[texto](dirección)` para los enlaces, y tres comillas invertidas seguidas para abrir y cerrar un pedazo de ejemplo. Ese pedazo de ejemplo se llama **bloque de código**, y lo que hay adentro no cuenta: un título de mentira escrito ahí no es un título de verdad. Las funciones de acá saben distinguirlos.

Y cuando hay que mostrar todo en pantalla y decidir si el programa termina bien o mal, también se usa una función de acá.

## De qué depende y quién lo usa

No usa ningún otro archivo de `validadores/`. De Python solo usa `os`, `re` y `sys`.

```
comun.py
   (no depende de nadie)
```

Lo usan **todos los archivos de la carpeta menos dos**: `recuerdos.py` e `historico.py`.

```
                        comun.py
                            ▲
        ┌───────────────────┼───────────────────┐
        │                   │                   │
  los 24 validadores   instalar.py         los 5 hook_*.py
  (piden Hallazgo,     versionado.py       (piden preparar_salida)
   FALLA y AVISO)      versiones.py
                       version.py
                       cargador.py
                       validar.py
                       pruebas.py
```

Qué le pide cada grupo:

| Le pide | Para qué |
|---|---|
| `Hallazgo`, `FALLA`, `AVISO` | Los 24 validadores, para reportar lo que encuentran. |
| `leer` | Todo el que abre un archivo. |
| `RAIZ` | El que necesita saber dónde está la carpeta del estándar. |
| `preparar_salida` | Los programas que imprimen en pantalla. |
| `reportar` | Solo `validar.py`. |
| `lineas_utiles`, `encabezados`, `marcadores`, `enlaces`, `recorrer_md` | Los que leen markdown: `cargador`, `citas`, `enlaces`, `plantillas`, `sesion`, `trazabilidad`. |
| `EXCLUIDAS` | Solo `cargador.py`. |

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `RAIZ` | La carpeta del estándar, o sea la carpeta que contiene a `validadores/`. Casi todos los programas la usan como valor por defecto. |
| `FALLA` | El texto `"FALLA"`. Marca un incumplimiento claro, que hace terminar el programa con error. |
| `AVISO` | El texto `"AVISO"`. Marca algo que hay que mirar, sin detener nada. |
| `EXCLUIDAS` | Los nombres de carpeta que nunca se recorren: `.git`, `__pycache__`, `.venv`, `venv`, `node_modules` y `vendor`. |

### Patrones de búsqueda

Son cuatro búsquedas preparadas de antemano, que usan las funciones de más abajo.

| Nombre | Qué reconoce |
|---|---|
| `_MARCADOR` | Un hueco sin llenar, escrito `[así]`, de los que deja un documento copiado de un molde. Deja fuera los enlaces. |
| `_ENCABEZADO` | Un título, y separa cuántos `#` lleva del texto del título. |
| `_CERCA` | La línea que abre o cierra un bloque de código. |
| `_ENLACE` | Un enlace, y separa el texto que se ve de la dirección a la que lleva. |

### El contrato de la salida

> Escrito el 2026-08-17 en la fase [`A-EP-004-HU-003`](../../documentacion/epicas/EP-004-comprobacion-automatica/HU-003-formato-del-hallazgo/A-EP-004-HU-003-retrodocumentar-el-formato-del-hallazgo/resultado_pruebas.md), que lo probó contra una corrida real de 207 hallazgos. Estaba en el código y no estaba escrito.

**Qué trae todo hallazgo, sin excepción:**

| Parte | Para qué sirve | Cuando falta |
|---|---|---|
| **Archivo** | Dónde está el problema | Nunca falta |
| **Línea** | Dónde exactamente | Vale **0** cuando el problema es del archivo entero. No se inventa un 1 |
| **Regla** | **Por qué** eso está mal | Nunca falta. Va dentro del mensaje, entre paréntesis: `(F18)`, `(F4/F14)` o `(F2: sin especificación acordada no hay código)` |

**Por qué las tres juntas.** Con el archivo y la línea se sabe dónde mirar; sin la regla no se sabe qué se exigía, y hay que abrir el programa que lo reportó. Ese es el criterio con el que se da por bueno un hallazgo: **alcanza para arreglar sin abrir el validador**.

**Qué hace cada severidad:**

| Severidad | Qué significa | Código de salida |
|---|---|---|
| `AVISO` | Algo que una persona debe mirar. Puede ser un falso positivo o algo aceptable | **0** — no detiene |
| `FALLA` | Incumplimiento claro | **1** — detiene |

**La regla del código de salida:** basta **una** falla para que la corrida termine en 1. Cien avisos terminan en 0. Sin hallazgos, 0.

**Lo dudoso sale como aviso, no como falla.** Un validador que reprueba por algo discutible se vuelve ruido, y lo que se termina ignorando no son solo sus avisos: son también sus fallas.

### La ficha `Hallazgo`

Es donde queda anotado un problema encontrado. Todos los validadores retornan una lista de estas fichas.

**`__init__(severidad, archivo, linea, mensaje)`**

- **Recibe:** la etiqueta de gravedad (`FALLA` o `AVISO`), la ruta del archivo, el número de línea y el texto que va a leer la persona.
- **Hace:** guarda los cuatro valores tal cual, sin revisarlos.
- **Retorna:** el objeto.

Los cuatro quedan disponibles como `hallazgo.severidad`, `hallazgo.archivo`, `hallazgo.linea` y `hallazgo.mensaje`.

Sobre `linea`: cuando vale **0** significa que el problema es del archivo entero y no de una línea puntual.

**`__str__()`**

- **Recibe:** nada.
- **Hace:** arma el texto que se imprime.
- **Retorna:** `[FALLA] carpeta/archivo.md:12 — el mensaje`. Si la línea es 0, se omite el número. La ruta se muestra relativa al estándar.

### Funciones

**`preparar_salida()`**

- **Recibe:** nada.
- **Hace:** avisa a la pantalla que el texto viene en UTF-8, que es la forma de escribir que incluye tildes, eñes y símbolos. Sin ese aviso, en Windows una tilde puede cortar el programa.
- **Retorna:** nada.

**`relativo(ruta)`**

- **Recibe:** una ruta de archivo.
- **Hace:** la convierte en una ruta corta, contada desde la carpeta del estándar, con barras `/`.
- **Retorna:** la ruta corta. Si el archivo está fuera del estándar o en otro disco, retorna la ruta completa.

**`leer(ruta)`**

- **Recibe:** una ruta de archivo.
- **Hace:** lo abre como UTF-8. **Nunca revienta**, y lo que no pudo leer bien queda anotado.
- **Retorna:** el contenido como texto.

Tres salidas, y ninguna detiene la corrida:

| Qué pasa con el archivo | Qué retorna | Qué queda anotado |
|---|---|---|
| Se lee bien | su contenido | nada, y se borra la anotación previa si la tenía |
| No está, o no se puede abrir | `""` | la ruta y el motivo del sistema |
| No es UTF-8 | lo que se pudo leer, con lo ilegible reemplazado | la ruta, el byte que falló y el aviso de que lo que se diga de ese archivo puede estar incompleto |

**Por qué anotar y no reventar.** Hasta el 2026-08-22 un `.md` mal codificado tumbaba la corrida entera con un volcado de Python, y se llevaba por delante **todos los hallazgos ya encontrados**. Y la salida contraria —leer reemplazando y callar— es peor: convierte un archivo roto en uno que parece sano. Se hacen las dos: la corrida sigue y el archivo se dice.

**`ilegibles()`**

- **Recibe:** nada.
- **Hace:** recoge lo que `leer` no pudo leer bien en esta corrida.
- **Retorna:** un hallazgo por archivo, siempre **AVISO**: que un archivo no se pueda leer no dice que el proyecto incumpla nada, dice que de ese archivo no se puede opinar.

`reportar` los agrega solo, así que ningún validador tiene que acordarse de llamarla.

**`lineas_utiles(texto)`**

- **Recibe:** el contenido de un archivo markdown.
- **Hace:** lo recorre saltando todo lo que está dentro de un bloque de código.
- **Retorna:** de a un par por vez: el número de línea y el contenido de esa línea.

Es la base de las tres funciones siguientes. Sin ella, un título de ejemplo escrito dentro de un bloque de código contaría como título real.

**`encabezados(texto, desde_nivel=2)`**

- **Recibe:** el contenido y, opcionalmente, el nivel mínimo de título.
- **Hace:** busca los títulos de ese nivel para abajo. Por defecto empieza en `##`, así que el título principal del documento queda fuera.
- **Retorna:** una lista de pares: número de línea y texto del título.

**`marcadores(texto)`**

- **Recibe:** el contenido.
- **Hace:** busca los huecos de plantilla sin llenar. Descarta enlaces y casillas de verificación.
- **Retorna:** una lista de pares: número de línea y el marcador encontrado.

**`enlaces(texto)`**

- **Recibe:** el contenido.
- **Hace:** busca los enlaces de markdown fuera de los bloques de código.
- **Retorna:** una lista de tríos: número de línea, texto visible y dirección.

Tiene el mismo nombre que el archivo `enlaces.py`, pero son cosas distintas: esta es una función, aquel es un archivo. `enlaces.py` la usa.

**`recorrer_md(raiz)`**

- **Recibe:** una carpeta.
- **Hace:** la recorre entera buscando archivos `.md`, sin entrar a las carpetas de `EXCLUIDAS`.
- **Retorna:** de a una por vez, la ruta completa de cada archivo `.md`.

**`reportar(hallazgos, titulo=None)`**

- **Recibe:** la lista de hallazgos y, opcionalmente, un título para encabezar la salida.
- **Hace:** imprime el título, después todas las fallas y después todos los avisos, y al final el conteo.
- **Retorna:** `0` si no hubo ninguna falla, `1` si hubo al menos una. Ese número es el que el programa entrega al sistema operativo.

Si la lista está vacía imprime `OK: sin incumplimientos.` y retorna `0`.

## Cómo se ejecuta

Este archivo no se ejecuta solo. Sus funciones se llaman desde los demás, siempre en el mismo orden:

```
1. validar.py llama a preparar_salida()
       ↓
2. el validador de turno lee archivos con leer() o recorrer_md()
       ↓
3. por cada problema, crea un Hallazgo(...)
       ↓
4. validar.py pasa la lista a reportar()
       ↓
5. reportar() imprime y retorna 0 o 1
```

## Ejemplos de lo que retorna

```python
RAIZ
'c:\Ing. Jose\ia\agente'

FALLA, AVISO
'FALLA'  'AVISO'

EXCLUIDAS
{'.git', '__pycache__', '.venv', 'venv', 'node_modules', 'vendor'}

relativo('c:\Ing. Jose\ia\agente\base\09-git.md')
'base/09-git.md'

leer('base/09-git.md')
'# 09 · Git\n\n## G2 · Mensaje de commit\n\nLa primera línea...'

Hallazgo(FALLA, 'base/09-git.md', 12, 'enlace roto: otro.md')
   .severidad  →  'FALLA'
   .archivo    →  'base/09-git.md'
   .linea      →  12
   .mensaje    →  'enlace roto: otro.md'
   str(...)    →  '[FALLA] base/09-git.md:12 — enlace roto: otro.md'

# el mismo, pero del archivo entero
str(Hallazgo(AVISO, 'base/09-git.md', 0, 'sin índice'))
'[AVISO] base/09-git.md — sin índice'

list(lineas_utiles('## Real\n\n```\n## Falso\n```\n\n## Otro\n'))
[(1, '## Real'), (2, ''), (5, ''), (6, ''), (7, '## Otro')]

encabezados('# Título\n## Uno\n### Dos\n')
[(2, 'Uno'), (3, 'Dos')]          # el H1 no entra

marcadores('- [ ] pendiente\n- [x] hecho\n[Ver](otro.md)\n[Módulo]\n')
[(4, '[Módulo]')]

enlaces('Ver [la regla](../base/09-git.md) y [el plan](plan.md).')
[(1, 'la regla', '../base/09-git.md'), (1, 'el plan', 'plan.md')]

list(recorrer_md('base'))
['c:\...\base\00-nucleo-blindado.md',
 'c:\...\base\01-identidad-y-rol.md',
 'c:\...\base\09-git.md']

reportar([], 'Coherencia del estándar')
0        # y en pantalla:  == Coherencia del estándar ==
         #                 OK: sin incumplimientos.

reportar([Hallazgo(FALLA, 'a.md', 3, 'enlace roto: x.md')], 'Coherencia')
1        # y en pantalla:  [FALLA] a.md:3 — enlace roto: x.md
         #                 1 falla(s), 0 aviso(s).

preparar_salida()
None     # no retorna nada; deja la pantalla en UTF-8
```
