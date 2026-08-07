# Stack de instalación del agente

Todo lo que un proyecto debe tener para que el agente funcione completo. Mientras falte un punto, la instalación está **incompleta** y el agente lo dice en cada mensaje.

Este archivo vive en el estándar y se copia a `./.agente/stack-instalacion.md` de cada proyecto. La copia es el retrato de lo que ese proyecto tiene instalado; el original es la verdad. Si el original cambia, la copia queda vieja y eso mismo se reporta como actualización pendiente.

> **No se edita la copia.** La reescribe el instalador. Lo que se ajusta por proyecto va en `CLAUDE.md` o en `.agente/reglas-proyecto.md`.

## Componentes

La columna `id` es la que usa el validador; no se renombra ni se reordena por gusto.

| id | Componente | Cómo se instala |
|---|---|---|
| `f13` | La carpeta `proyectos/`, donde vive el código (`02·F13`). Es la precondición de todo lo demás. | La crea el usuario: `proyectos/<su-proyecto>/`. El agente no la inventa. |
| `claude-md` | El `CLAUDE.md` del proyecto: existe, sin `«marcadores»` sin reemplazar, y **sincronizado** con la plantilla central. | Copiar `plantillas/CLAUDE.md.plantilla` a la raíz como `CLAUDE.md` y llenar cada `«…»`. Si la plantilla cambió: aplicar lo nuevo y `python validadores/instalar.py "<proyecto>" --aplicar` para volver a sellarlo. |
| `gitignore` | El `.gitignore` con las líneas `CLAUDE.md` y `.agente/`: son configuración local, no del repositorio. | Agregar las dos líneas al `.gitignore` del proyecto. |
| `agente-config` | Los 4 archivos de `./.agente/`: `stack.md`, `dominio.md`, `mapeo-nombres.md`, `marco-normativo.md`. | Los copia y llena el agente al abrir sesión (paso 3 del `CLAUDE.md`). |
| `stack-instalacion` | Este mismo archivo, copiado a `./.agente/` y al día con el del estándar. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `documentacion` | La carpeta `documentacion/`, donde el agente deja specs, planes y trazabilidad (regla `13`). | La crea el agente al producir el primer documento; también sirve crearla vacía. |
| `historico` | La carpeta `historico-chat/` con su `README.md`: la transcripción de cada sesión. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `recuerdos` | La carpeta `historico-chat/memory/` con su índice: la memoria del agente, versionada. Y la carpeta local de la herramienta (`~/.claude/projects/<proyecto>/memory/`) **vacía**: lo que aparezca ahí se mueve acá. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `enganches-git` | Los enganches `commit-msg` y `pre-commit` en cada repositorio, apuntando a este estándar. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `enganches-claude` | Los enganches de Claude Code en `.claude/settings.json`, apuntando a este estándar. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `registro` | El proyecto anotado en `plantillas/proyectos.md` del estándar: la lista única de proyectos que usan el agente. | Agregar la fila: nombre · ruta · scope de memoria · stack. |
| `version` | Que el proyecto **declare** qué versión del estándar sigue. El número en sí no reprueba: que sea más viejo que el central no obliga a nada por sí solo. | Fijar «Versión del estándar adoptada» en el `CLAUDE.md`. Subir de versión es decisión del usuario. |
| `versiones` | La carpeta `./documentacion/versiones/`: un registro por actualización, con desde cuándo el proyecto usa cada versión y qué se actualizó. Se versiona. | `python validadores/instalar.py "<proyecto>" --aplicar` |

## Cómo se comprueba

```sh
python validadores/validar.py checklist --raiz "<proyecto>"
```

Y solo: en cada mensaje de la sesión, el enganche `UserPromptSubmit` repite la comprobación. Si falta algo, escribe `./.agente/INSTALACION-INCOMPLETA.md` con la lista y se lo pasa al agente, que debe decirlo. Cuando ya no falta nada, **borra** ese archivo: su ausencia es la señal de instalación completa.

No bloquea el trabajo. El único que detiene es el gate `f13`, que ya era así: sin `proyectos/` no hay dónde trabajar.

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

Es idempotente: lo que ya está al día no se toca. Lo único que no aplica solo es subir la **versión adoptada** del estándar — esa es decisión del usuario, porque un cambio de norma no reabre fases ya cerradas.

## Dónde queda registrada cada actualización

En `./documentacion/versiones/`, un archivo por actualización — `AAAA-MM-DD-<versión>.md` — que deja escrito **desde cuándo** el proyecto usa esa versión:

- versión anterior y versión instalada, con fecha y hora;
- qué componentes se actualizaron, con la huella antes y después;
- qué pasos aplicó el instalador;
- qué quedó pendiente porque es decisión del usuario.

Los escribe el instalador y no se editan a mano. El `README.md` de esa carpeta es el índice.

**Va en `documentacion/` y no en `.agente/` a propósito:** `.agente/` está en el `.gitignore` y se queda en una sola máquina. Un cambio de norma no reabre fases ya cerradas — quedan selladas con la versión bajo la que cerraron—, y para saber cuál era hay que poder mirarlo desde cualquier copia del repositorio.
