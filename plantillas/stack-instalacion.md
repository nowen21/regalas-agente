# Stack de instalación del agente

Todo lo que un proyecto debe tener para que el agente funcione completo. Mientras falte un punto, la instalación está **incompleta** y el agente lo dice en cada mensaje.

Este archivo vive en el estándar y se copia a `./.agente/stack-instalacion.md` de cada proyecto. La copia es el retrato de lo que ese proyecto tiene instalado; el original es la verdad. Si el original cambia, la copia queda vieja y eso mismo se reporta como actualización pendiente.

> **No se edita la copia.** La reescribe el instalador. Lo que se ajusta por proyecto va en `CLAUDE.md` o en `.agente/reglas-proyecto.md`.

## Todo se instala con una sola línea

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

**Ningún componente de esta lista se instala a mano.** El instalador lee el estado del proyecto, calcula qué falta y lo deja puesto; después vuelve a comprobar y dice si algo quedó fuera. Es idempotente: lo que ya está al día no se toca, no se duplica y no se pisa.

Lo que **no** decide el instalador —porque no es suyo— es qué código va dentro de `proyectos/` y cuándo el proyecto sube la versión adoptada del estándar. Ni lo pregunta al arrancar: crea la carpeta vacía y deja declarada la versión con la que se instaló.

## Componentes

La columna `id` es la que usa el validador; no se renombra ni se reordena por gusto. Todos se instalan con la línea de arriba: la tercera columna dice qué hace el instalador con cada uno.

| id | Componente | Qué hace el instalador |
|---|---|---|
| `f13` | La carpeta `proyectos/`, donde vive el código (`02·F13`). | La crea vacía. **No** mueve ni reorganiza código: qué va adentro es del usuario. |
| `claude-md` | El `CLAUDE.md` del proyecto: existe, sin marcadores sin reemplazar, y **sincronizado** con la plantilla central. | Si falta, lo genera desde `plantillas/CLAUDE.md.plantilla` con las rutas de esta máquina, el nombre y el slug del proyecto y la versión del estándar. Si ya está, llena los marcadores que queden, agrega al final las secciones que la plantilla sumó —sin pisar lo escrito— y lo vuelve a sellar. |
| `gitignore` | El `.gitignore` con las líneas `CLAUDE.md` y `.agente/`: son configuración local, no del repositorio. | Agrega las líneas que falten. Nunca reescribe ni reordena el resto. |
| `agente-config` | Los 4 archivos de `./.agente/`: `stack.md`, `dominio.md`, `mapeo-nombres.md`, `marco-normativo.md`. | Los pone desde sus plantillas si faltan; si ya están, no los toca. Llenarlos con los datos del proyecto es del agente al abrir sesión (paso 3 del `CLAUDE.md`). |
| `stack-instalacion` | Este mismo archivo, copiado a `./.agente/` y al día con el del estándar. | Lo copia y lo sella. Esta copia sí se reescribe entera: no la llena nadie. |
| `documentacion` | La carpeta `documentacion/`, donde el agente deja especificaciones, planes y trazabilidad (regla `13`). | La crea vacía. |
| `historico` | La carpeta `historico-chat/` con su `README.md`: la transcripción de cada sesión. | La crea con su `README.md` desde la plantilla; si ya está, solo refresca el sello. |
| `recuerdos` | La carpeta `historico-chat/memory/` con su índice: la memoria del agente, versionada. Y la carpeta local de la herramienta (`~/.claude/projects/<proyecto>/memory/`) **vacía**: lo que aparezca ahí se mueve acá. | Crea la carpeta y el índice, y vacía el almacén local moviendo lo que haya. |
| `enganches-git` | Los enganches `commit-msg` y `pre-commit` en cada repositorio, apuntando a este estándar. | Los escribe en `.githooks/` y apunta `core.hooksPath` ahí, en cada repositorio que encuentre. |
| `enganches-claude` | Los enganches de Claude Code en `.claude/settings.json`, apuntando a este estándar. | Los agrega al `settings.json`, respetando lo que ya hubiera. Una versión anterior del mismo enganche se reemplaza, no se duplica. |
| `registro` | El proyecto anotado en `plantillas/proyectos.md` del estándar: la lista única de proyectos que usan el agente. | Agrega la fila con nombre, ruta y scope de memoria. El stack queda «por detectar» hasta que el agente llene `.agente/stack.md`. |
| `version` | Que el proyecto **declare** qué versión del estándar sigue. El número en sí no reprueba: que sea más viejo que el central no obliga a nada por sí solo. | La deja declarada en el `CLAUDE.md` al instalarlo. **Subirla después es decisión del usuario:** un cambio de norma no reabre fases ya cerradas. |
| `versiones` | La carpeta `./documentacion/versiones/`: un registro por actualización, con desde cuándo el proyecto usa cada versión y qué se actualizó. Se versiona. | Escribe un registro cada vez que algo cambia de huella. |

## Cómo se comprueba

```sh
python validadores/validar.py checklist --raiz "<proyecto>"
```

El instalador la corre solo al terminar, así que instalar y comprobar son el mismo paso: no se declara completo lo que no se miró.

Y además: en cada mensaje de la sesión, el enganche `UserPromptSubmit` repite la comprobación. Si falta algo, escribe `./.agente/INSTALACION-INCOMPLETA.md` con la lista y se lo pasa al agente, que debe decirlo. Cuando ya no falta nada, **borra** ese archivo: su ausencia es la señal de instalación completa.

No bloquea el trabajo. Lo que aparezca después de haber instalado es, por definición, algo que exige una decisión del usuario — y entonces se dice cuál es y por qué.

## Nada de lo que el proyecto usa puede quedar viejo

Todo documento que el proyecto **heredó** del estándar lleva al final su **sello**:

```
<!-- huella: a1b2c3d4e5f6 · estandar 1.5.0 -->
```

La huella no es la del documento local: es la de la **plantilla contra la que se sincronizó**. Tiene que ser así porque el `CLAUDE.md` lo llena cada proyecto —su contenido nunca coincide con el original— y aun así hay que poder decir si quedó viejo.

Si la plantilla cambia en el estándar, la huella deja de coincidir y el componente **reprueba**: no es un aviso que se pueda ignorar, es instalación incompleta.

| Documento heredado | Su plantilla |
|---|---|
| `CLAUDE.md` | `plantillas/CLAUDE.md.plantilla` |
| `.agente/stack-instalacion.md` | `plantillas/stack-instalacion.md` |
| `historico-chat/README.md` | `plantillas/historico-chat.md` |
| `historico-chat/memory/memory.md` | `plantillas/memoria.md` |

Del `CLAUDE.md`, del README del histórico y del índice de la memoria **solo se refresca el sello**: el contenido es del proyecto y no se pisa. La copia del stack sí se reescribe entera — no la llena nadie.

## Cómo se detectan las actualizaciones

Cuatro cosas distintas, y se reportan por separado porque se arreglan distinto:

| Qué cambió | Cómo se nota |
|---|---|
| **Un documento heredado** (`CLAUDE.md`, el README del histórico, este archivo) | Su sello no coincide con la huella actual de la plantilla. |
| **Un componente** (un enganche, una carpeta) | Su propia comprobación falla: falta, o apunta a otro estándar. |
| **Una actualización sin registrar** | Lo instalado declara una versión y el último registro de `documentacion/versiones/` dice otra. |

**Al proyecto no le interesan todos los cambios del estándar: solo los que tiene que aplicar.** Por eso el número de versión **no reprueba**. Que el estándar vaya en 2.1.0 y el proyecto declare 1.8.0 no dice nada por sí solo — puede que ninguno de esos cambios lo toque. Lo que sí reprueba es el sello: se queja cuando cambió un documento que **este** proyecto usa. El desfase de número se informa al margen, para que el usuario decida si sube la versión adoptada.

Aplicar la actualización es siempre lo mismo:

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

Es la misma línea que instala desde cero: instalar y actualizar son el mismo proceso, y es idempotente. Lo único que no aplica solo es subir la **versión adoptada** del estándar — esa es decisión del usuario, porque un cambio de norma no reabre fases ya cerradas.

## Dónde queda registrada cada actualización

En `./documentacion/versiones/`, un archivo por actualización — `AAAA-MM-DD-<versión>.md` — que deja escrito **desde cuándo** el proyecto usa esa versión:

- versión anterior y versión instalada, con fecha y hora;
- qué componentes se actualizaron, con la huella antes y después;
- qué pasos aplicó el instalador;
- qué quedó pendiente porque es decisión del usuario.

Los escribe el instalador y no se editan a mano. El `README.md` de esa carpeta es el índice.

**Va en `documentacion/` y no en `.agente/` a propósito:** `.agente/` está en el `.gitignore` y se queda en una sola máquina. Un cambio de norma no reabre fases ya cerradas — quedan selladas con la versión bajo la que cerraron—, y para saber cuál era hay que poder mirarlo desde cualquier copia del repositorio.
