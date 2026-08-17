# `instalar.py`

Deja el agente instalado y funcionando en un proyecto con una sola línea, y al terminar comprueba que haya quedado completo.

## Qué hace

Es el archivo más grande de la carpeta y hace dos cosas distintas:

**1. Instala.** Mira cómo está el proyecto, calcula qué le falta y lo deja puesto: las carpetas, el `CLAUDE.md`, el `.gitignore`, los archivos de `.agente/`, la carpeta donde se guardan las conversaciones, la de los recuerdos, los enganches de git, los de Claude Code, la fila en la lista central de proyectos y la anotación de qué versión quedó instalada.

Dos palabras que se repiten abajo:

- **Enganche:** un programa que arranca solo cuando pasa algo —por ejemplo, justo antes de guardar un cambio— sin que nadie tenga que llamarlo.
- **`.gitignore`:** la lista de archivos que git debe ignorar, o sea no guardar.

**2. Responde dónde están los repositorios.** Un **repositorio** es una carpeta cuya historia guarda git, y un proyecto puede tener varios. La función `repositorios_git` la usan once validadores para saber qué carpetas revisar. Por eso `instalar.py` aparece como pieza necesaria de archivos que no instalan nada.

Tres características del instalador:

- **Es repetible.** Lo que ya está al día no se toca ni se duplica. Correrlo dos veces da el mismo resultado que correrlo una.
- **No pregunta.** Lo que ya está decidido por las reglas se aplica solo.
- **Por defecto solo simula.** Sin la opción `--aplicar` no modifica nada.

## De qué depende y quién lo usa

Al comienzo del archivo solo trae `comun.py`. Los otros cuatro los trae **adentro de la función** que los necesita, en el momento justo. Si los trajera al comienzo no arrancaría: tres de ellos lo necesitan a él, y cada uno se quedaría esperando al otro.

```
instalar.py
   ├── comun.py ······ RAIZ, leer, preparar_salida     (al comienzo)
   ├── checklist.py ·· dentro de instalar_stack, comprobar y _pendientes
   ├── versiones.py ·· dentro de las funciones que sellan
   ├── version.py ···· dentro de las funciones que sellan
   └── recuerdos.py ·· dentro de instalar_recuerdos
```

De Python usa `argparse`, `json`, `os`, `re`, `subprocess`, `sys`, `unicodedata` y `datetime`.

Lo usan catorce archivos:

```
instalar.py
   ▲
   ├── por repositorios_git():
   │      codigo.py, sesion.py, rama.py, ci.py, secretos.py,
   │      dependencias.py, migraciones.py, esquema.py,
   │      aislamiento.py, herramientas.py
   ├── por HOOKS, HOOKS_CLAUDE, CONFIG_AGENTE y cumple_f13():
   │      checklist.py, sesion.py, hook_sesion.py
   ├── validar.py ··· para el subcomando "versionado"
   └── pruebas.py
```

## Qué tiene adentro

### Valores fijos

| Nombre | Qué guarda |
|---|---|
| `REGISTRO` | Dónde está `plantillas/proyectos.md`, la única lista de proyectos instalados. |
| `MARCA` | La nota que se escribe adentro de los enganches para reconocer después que los escribió este programa y no una persona. |
| `_PREAMBULO` | El arranque que comparten los dos enganches de git: busca Python, busca el estándar y, si no los encuentra, se detiene diciendo por qué. |
| `PLANTILLA_COMMIT_MSG` | El texto completo del enganche que revisa el mensaje con que se guarda un cambio. |
| `PLANTILLA_PRE_COMMIT` | El texto completo del enganche que revisa qué archivos entran en ese cambio. |
| `HOOKS` | Los dos enganches de git: nombre, texto y descripción. |
| `HOOKS_CLAUDE` | Los siete enganches de Claude Code: evento, filtro, archivo que se ejecuta, mensaje en pantalla y argumentos. |
| `PLANTILLA_HISTORICO` | La ruta de la plantilla del README del histórico. |
| `PLANTILLA_MEMORIA` | La ruta de la plantilla del índice de la memoria. |
| `CARPETAS_BASE` | Las tres carpetas que se crean: `proyectos`, `documentacion` y `prompts`. |
| `CONFIG_AGENTE` | Los cuatro archivos de `.agente/`: `stack.md`, `dominio.md`, `mapeo-nombres.md` y `marco-normativo.md`. |
| `IGNORADOS` | Lo que se agrega al `.gitignore`: `CLAUDE.md` y `.agente/`. |
| `_FILA` | Reconoce una fila de la tabla del registro de proyectos. |
| `_MARCADOR` | Reconoce un hueco sin llenar en el `CLAUDE.md`, escrito entre comillas angulares. |

### Funciones que responden preguntas

**`proyectos_registrados()`**

- **Recibe:** nada.
- **Hace:** lee la tabla de `plantillas/proyectos.md`, salta el encabezado y las líneas que no son filas.
- **Retorna:** una lista de pares «nombre, ruta».

**`cumple_f13(ruta)`**

- **Recibe:** la carpeta de un proyecto.
- **Hace:** mira si existe la subcarpeta `proyectos/`.
- **Retorna:** verdadero o falso.

**`es_el_estandar(ruta)`**

- **Recibe:** una carpeta.
- **Hace:** compara esa carpeta con la del estándar.
- **Retorna:** verdadero si son la misma.

El estándar recibe un trato distinto: no se le crea estructura de proyecto ni se le toca el `.gitignore`.

**`es_repositorio_git(ruta)`**

- **Recibe:** una carpeta.
- **Hace:** mira si tiene una subcarpeta `.git`.
- **Retorna:** verdadero o falso.

**`repositorios_git(ruta)`**

- **Recibe:** la carpeta del proyecto.
- **Hace:** busca repositorios en dos sitios: la carpeta misma, y cada subcarpeta de `proyectos/`.
- **Retorna:** la lista de carpetas que son repositorios, en ese orden.

Es la función más usada del archivo. Existe porque un proyecto puede tener varios repositorios separados dentro de `proyectos/`: por ejemplo, uno con la parte que se ve en pantalla y otro con la parte que trabaja por detrás.

**`_mandar_git(ruta, *args)`**

- **Recibe:** una carpeta y los argumentos de git.
- **Hace:** ejecuta git ahí.
- **Retorna:** el resultado completo del proceso.

### Funciones que instalan

Todas reciben la carpeta del proyecto y un valor `aplicar`; si `aplicar` es falso calculan lo que harían pero no escriben nada. Todas retornan una lista de textos que describen lo que hicieron o harían.

**`instalar_git(ruta, estandar, aplicar)`**

Escribe los dos enganches en `.githooks/` y apunta la configuración de git a esa carpeta. Si la configuración ya apunta a otro lado, no la pisa: avisa y se detiene.

**`instalar_claude(ruta, estandar, aplicar)`**

Agrega los siete enganches al archivo de ajustes `.claude/settings.json`. Respeta lo que ya hubiera puesto otra persona. Reconoce los suyos por el nombre del archivo que ejecutan, así que una versión vieja la reemplaza en vez de dejar dos. Ese archivo está escrito en JSON, que es una forma de anotar datos con llaves y comas; si está mal escrito y no se entiende, no lo toca.

**`instalar_stack(ruta, aplicar)`**

Copia `plantillas/stack-instalacion.md` a `.agente/`, **llena sus huecos** y le pone su **huella**, que es una marca corta que dice de qué versión salió la copia; sirve para saber después si quedó vieja. Esta copia **sí se pisa**, porque nadie escribe nada adentro: es la foto de lo que el estándar exige hoy.

**`instalar_historico(ruta, aplicar)`**

Crea `historico-chat/README.md` desde la plantilla. Si ya existe no lo pisa; solo le actualiza la marca de huella.

**`instalar_recuerdos(ruta, aplicar)`**

Crea `historico-chat/memory/memory.md` desde la plantilla —con sus huecos llenos— y después mueve ahí lo que haya quedado en la memoria de la herramienta. Si la carpeta ya está enlazada y el índice existe, no toca nada.

**`instalar_estructura(ruta, aplicar)`**

Crea las tres carpetas de `CARPETAS_BASE` que falten. Se crean vacías.

**`instalar_gitignore(ruta, aplicar)`**

Agrega al `.gitignore` las líneas de `IGNORADOS` que falten. Solo agrega: nunca reescribe ni reordena.

**`instalar_agente_config(ruta, aplicar)`**

Copia los cuatro archivos de `CONFIG_AGENTE` desde `plantillas/`, solo si faltan, llenando los huecos que el instalador sabe llenar.

**Dos clases de hueco, y solo una la llena el instalador.** Estos cuatro archivos llegan al proyecto **a propósito con huecos**: son las preguntas que nadie puede responder desde afuera —a qué se dedica el negocio, quién usa el sistema— y las contesta el proyecto después. Lo que sí se llena es lo que el instalador sabe: dónde vive el estándar, cómo se llama el proyecto, la fecha. Si uno de esos sobrevive a la copia, la cita a una regla llega muerta.

**`instalar_claude_md(ruta, aplicar)`**

Deja el `CLAUDE.md` puesto, lleno y marcado. Tres casos:

- Si no existe, lo genera desde la plantilla central con los datos de esta máquina.
- Si existe con huecos sin llenar, los llena.
- Si existe y la plantilla ganó secciones nuevas, se las agrega al final sin tocar lo que ya había.

**`instalar_registro(ruta, aplicar)`**

Agrega una fila del proyecto a `plantillas/proyectos.md`, si no estaba.

### Funciones de apoyo

**`_hook_claude(estandar, proyecto, guion, mensaje, argumentos="")`**

- **Recibe:** la ruta del estándar, la del proyecto, el nombre del archivo a ejecutar, el mensaje que se muestra y los argumentos extra.
- **Retorna:** el enganche ya armado como lista de «nombre del dato → valor», lista para escribir en el archivo de ajustes.

**`_escribir_sellado(archivo, texto, componente, proyecto)`**

Escribe el texto en el archivo con la marca de huella al día.

**`_refrescar_sello(archivo, componente, proyecto, aplicar, etiqueta)`**

Actualiza solo la marca de huella de un archivo, sin tocar su contenido.

**`_slug(texto)`**

- **Recibe:** un texto.
- **Retorna:** el mismo texto en minúsculas, sin tildes y con guiones en lugar de espacios.

**`_rellenos(ruta)`**

- **Recibe:** la carpeta del proyecto.
- **Retorna:** la lista de «hueco → con qué se llena» para completar los moldes que se copian al proyecto: el nombre del proyecto, su nombre corto, dónde está el estándar, dónde está el proyecto, qué versión del estándar es y la fecha de hoy. Incluye también los huecos de moldes anteriores, para que un proyecto viejo se ponga al día solo.
- **Es además la lista de lo que el instalador se comprometió a llenar.** La prueba `validadores/tests/test_instalar_marcadores.py` la usa como criterio: ningún archivo copiado puede conservar uno de estos. Al salir de acá, el marcador que se agregue mañana queda cubierto sin tocar la prueba.

**`_rellenar(texto, rellenos)`**

Reemplaza cada hueco por su valor y retorna el texto resultante.

**`_reparar_marcadores(archivo, ruta, aplicar, etiqueta)`**

- **Recibe:** un archivo que **ya existía** en el proyecto, la carpeta del proyecto, si se aplica de verdad y con qué nombre reportarlo.
- **Hace:** rellena en el sitio los huecos que quedaron crudos de una copia anterior, sin reescribir nada más. Si no hay nada que rellenar, no toca el archivo ni reporta paso.
- **Por qué existe:** arreglar el punto de copia solo alcanza a lo que se instale desde ahí en adelante. Un proyecto que ya tenía la copia mala se queda con ella, porque la huella sale del molde central y ese no cambió. Por eso toda copia que ya existe pasa por acá.
- **Qué no toca:** los huecos que llena el proyecto. `_rellenar` solo conoce los de `_rellenos`, así que un hueco como `«motor»` sale intacto.
- **Quién lo usa:** `instalar_stack`, `instalar_agente_config` y `_refrescar_sello` —o sea el histórico y la memoria—. El `CLAUDE.md` ya lo hacía por su cuenta desde antes.

**`_secciones(texto)`**

- **Recibe:** el contenido de un documento de texto.
- **Retorna:** una lista de pares «título, líneas que van debajo de ese título», empezando por los títulos de segundo nivel (los que llevan `##`).

**`_completar_secciones(local, plantilla)`**

- **Recibe:** el contenido local y el de la plantilla.
- **Retorna:** el contenido local con las secciones que le faltaban agregadas al final, y la lista de títulos agregados.

**`_huellas(ruta)`**

- **Retorna:** la lista de «pieza instalada → qué huella tiene marcada» en ese momento.

**`_version_anterior(ruta)`**

- **Retorna:** la versión con la que venía el proyecto, o texto vacío si es la primera instalación.

**`_pendientes(ruta)`**

- **Retorna:** la lista de lo que quedó sin resolver después de instalar todo.

**`registrar_version(ruta, antes, pasos, aplicar, anterior="")`**

Escribe el archivo de registro en `documentacion/versiones/`. Lo escribe por dos motivos, y basta con uno: que alguna huella haya cambiado, o que **haya subido la versión del estándar** aunque al proyecto no le cambie ningún molde. Sin ninguno de los dos no escribe nada, y a la carpeta del propio estándar no le escribe nunca.

El segundo motivo es el que evita que el proyecto se quede atrás para siempre: sin él, el instalador decía «nada que registrar» y la revisión decía «falta el registro», sin más salida que editar a mano un archivo que dice que no se edita a mano.

### Funciones principales

**`instalar(nombre, ruta, aplicar)`**

- **Recibe:** el nombre del proyecto, su carpeta y si se aplica de verdad.
- **Hace:** todo el proceso, en el orden del apartado siguiente.
- **Retorna:** verdadero si se procesó, falso si la carpeta no existe.

**`comprobar(ruta, aplicar, propio=False)`**

- **Recibe:** la carpeta, si se aplicó y si es el propio estándar.
- **Hace:** vuelve a revisar el proyecto con `checklist.py` e imprime qué falta. Si es el propio estándar, no revisa nada.
- **Retorna:** nada; imprime.

**`main()`**

Lee lo que se escribió en la consola, decide sobre qué proyectos hay que trabajar y llama a `instalar` en cada uno.

## Cómo se ejecuta

```
python validadores/instalar.py                    muestra el registro
python validadores/instalar.py C:/ruta            simula, no toca nada
python validadores/instalar.py C:/ruta --aplicar  instala de verdad
python validadores/instalar.py --todos --aplicar  todos los del registro
```

Lo que pasa dentro de `instalar()`, en orden:

```
 1. normaliza la ruta
 2. si la carpeta no existe → se detiene
 3. anota las huellas y la versión ANTES de tocar nada
 4. ¿es el propio estándar?
       sí → salta los pasos 5 y 6
 5. instalar_estructura
 6. instalar_gitignore
 7. por cada repositorio git → instalar_git
 8. instalar_claude          (los enganches de Claude Code)
 9. instalar_historico
10. instalar_recuerdos
11. si no es el estándar → instalar_stack, instalar_agente_config,
                            instalar_claude_md, instalar_registro
12. registrar_version        (si cambió una huella o subió la versión)
13. comprobar                (vuelve a revisar y dice qué falta)
```

## Ejemplos de lo que retorna

```python
proyectos_registrados()
[('agro-system', 'C:/Ing. Jose/ia/agro-system'),
 ('POS',         'C:/Ing. Jose/ia/pos')]

cumple_f13('C:/proyectos/pos')
True             # existe la carpeta proyectos/

es_el_estandar('C:/Ing. Jose/ia/agente')
True

es_repositorio_git('C:/proyectos/pos')
True             # tiene una carpeta .git

repositorios_git('C:/espacio')
['C:/espacio',                    # la raíz, si es repositorio
 'C:/espacio\proyectos\pos-back',
 'C:/espacio\proyectos\pos-front']

repositorios_git('C:/carpeta-sin-git')
[]

_slug('Proyecto de Grado')
'proyecto-de-grado'

_rellenos('C:/proyectos/pos')
{'«NOMBRE-PROYECTO»':  'pos',
 '«SLUG-PROYECTO»':    'pos',
 '«RUTA-ESTANDAR»':    'c:/Ing. Jose/ia/agente',
 '«RUTA-PROYECTO»':    'C:/proyectos/pos',
 '«VERSION-ESTANDAR»': '5.0.0',
 '«FECHA»':            '2026-08-09',
 ...}

_hook_claude('c:/…/agente', 'C:/proyectos/pos', 'hook_md.py', 'Revisando…')
{'type': 'command',
 'command': 'python "c:/…/agente/validadores/hook_md.py" --raiz "C:/proyectos/pos"',
 'statusMessage': 'Revisando…'}

_secciones('# Título\n## Uno\ntexto\n## Dos\n')
[('Uno', ['## Uno', 'texto']), ('Dos', ['## Dos'])]

_completar_secciones(local, plantilla)
('# Proyecto\n## Uno\n…\n\n## Nueva\ntexto de la plantilla\n', ['Nueva'])
#  └─ el texto ya completo                                     └─ qué se agregó

_huellas('C:/proyectos/pos')
{'claude-md': 'a3f9c21b04de', 'stack-instalacion': '7b12ee90aa31',
 'historico': '55c0d1f8b2a7', 'recuerdos': ''}

_version_anterior('C:/proyectos/pos')
'4.0.0'          # o '' si es la primera instalación

_pendientes('C:/proyectos/pos')
['**version** — el proyecto no declara qué versión del estándar sigue']
```

Las funciones que instalan retornan **la lista de lo que hicieron o harían**, una línea por paso:

```python
instalar_estructura('C:/proyectos/nuevo', aplicar=True)
['crear proyectos/', 'crear documentacion/', 'crear prompts/']

instalar_estructura('C:/proyectos/ya-listo', aplicar=True)
['la estructura base ya estaba']

instalar_gitignore('C:/proyectos/pos', aplicar=True)
['agregar al .gitignore: CLAUDE.md, .agente/']

instalar_git('C:/proyectos/pos', 'c:/…/agente', aplicar=True)
['escribir .githooks\commit-msg',
 'escribir .githooks\pre-commit',
 'git config core.hooksPath .githooks']

instalar_git(...)     # la segunda vez, sin cambios
['commit-msg ya estaba al día', 'pre-commit ya estaba al día',
 'core.hooksPath ya estaba puesto']

instalar_claude('C:/proyectos/pos', 'c:/…/agente', aplicar=True)
['agregar enganche PostToolUse a .claude\settings.json',
 'reemplazar el enganche SessionStart en .claude\settings.json',
 'enganche Stop ya estaba puesto']

instalar_claude_md('C:/proyectos/nuevo', aplicar=True)
['crear CLAUDE.md desde la plantilla, con las rutas y la versión de esta máquina']

instalar_recuerdos('C:/proyectos/pos', aplicar=True)
['historico-chat/memory/memory.md ya estaba sellado al día',
 'mover `aprobar-antes-de-commit.md` a `historico-chat/memory/`']

instalar_registro('C:/proyectos/pos', aplicar=True)
['anotar «pos» en plantillas/proyectos.md']

registrar_version('C:/proyectos/pos', antes, pasos, aplicar=True)
['registrar documentacion\versiones\2026-08-09-5.0.0.md']

registrar_version(...)   # subió la versión, ningún molde cambió
['registrar documentacion\versiones\2026-08-16-21.2.0.md']

registrar_version(...)   # ni los moldes ni la versión cambiaron
['versiones: ni las plantillas ni la versión cambiaron, no hay actualización que registrar']

_reparar_marcadores('C:/proyectos/pos/.agente/stack-instalacion.md', ...)
['rellenar los marcadores que quedaron crudos en .agente/stack-instalacion.md']

_reparar_marcadores(...)   # cuando no quedaba ninguno
[]

instalar('POS', 'C:/proyectos/pos', aplicar=True)
True             # False solo si la carpeta no existe

comprobar('C:/proyectos/pos', aplicar=True)
None             # no retorna nada; imprime el resultado

main()
0
```
