# Stack de instalación del agente

Todo lo que un proyecto debe tener para que el agente funcione completo. Mientras falte un punto, la instalación está **incompleta** y el agente lo dice en cada mensaje.

Este archivo vive en el estándar y se copia a `./.agente/stack-instalacion.md` de cada proyecto. La copia es el retrato de lo que ese proyecto tiene instalado; el original es la verdad. Si el original cambia, la copia queda vieja y eso mismo se reporta como actualización pendiente.

> **No se edita la copia.** La reescribe el instalador. Lo que se ajusta por proyecto va en `CLAUDE.md` o en `.agente/reglas-proyecto.md`.

## Componentes

La columna `id` es la que usa el validador; no se renombra ni se reordena por gusto.

| id | Componente | Cómo se instala |
|---|---|---|
| `f13` | La carpeta `proyectos/`, donde vive el código (`02·F13`). Es la precondición de todo lo demás. | La crea el usuario: `proyectos/<su-proyecto>/`. El agente no la inventa. |
| `claude-md` | El `CLAUDE.md` del proyecto, sin `«marcadores»` sin reemplazar. | Copiar `plantillas/CLAUDE.md.plantilla` a la raíz como `CLAUDE.md` y llenar cada `«…»`. |
| `gitignore` | El `.gitignore` con las líneas `CLAUDE.md` y `.agente/`: son configuración local, no del repositorio. | Agregar las dos líneas al `.gitignore` del proyecto. |
| `agente-config` | Los 4 archivos de `./.agente/`: `stack.md`, `dominio.md`, `mapeo-nombres.md`, `marco-normativo.md`. | Los copia y llena el agente al abrir sesión (paso 3 del `CLAUDE.md`). |
| `stack-instalacion` | Este mismo archivo, copiado a `./.agente/` y al día con el del estándar. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `documentacion` | La carpeta `documentacion/`, donde el agente deja specs, planes y trazabilidad (regla `13`). | La crea el agente al producir el primer documento; también sirve crearla vacía. |
| `historico` | La carpeta `historico-chat/` con su `README.md`: la transcripción de cada sesión. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `enganches-git` | Los enganches `commit-msg` y `pre-commit` en cada repositorio, apuntando a este estándar. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `enganches-claude` | Los enganches de Claude Code en `.claude/settings.json`, apuntando a este estándar. | `python validadores/instalar.py "<proyecto>" --aplicar` |
| `registro` | El proyecto anotado en `plantillas/proyectos.md` del estándar: la lista única de proyectos que usan el agente. | Agregar la fila: nombre · ruta · scope de memoria · stack. |
| `version` | La versión del estándar que el proyecto declara seguir, sin desfase con la central. | Fijar «Versión del estándar adoptada» en el `CLAUDE.md`. Subir de versión es decisión del usuario. |

## Cómo se comprueba

```sh
python validadores/validar.py checklist --raiz "<proyecto>"
```

Y solo: en cada mensaje de la sesión, el enganche `UserPromptSubmit` repite la comprobación. Si falta algo, escribe `./.agente/INSTALACION-INCOMPLETA.md` con la lista y se lo pasa al agente, que debe decirlo. Cuando ya no falta nada, **borra** ese archivo: su ausencia es la señal de instalación completa.

No bloquea el trabajo. El único que detiene es el gate `f13`, que ya era así: sin `proyectos/` no hay dónde trabajar.

## Cómo se detectan las actualizaciones

Tres cosas distintas, y se reportan por separado:

| Qué cambió | Cómo se nota |
|---|---|
| **El stack de instalación** (este archivo) | La copia en `.agente/` lleva la huella del original. Si no coinciden, hay componentes nuevos que instalar. |
| **Un componente** (un enganche, una carpeta) | Su propia comprobación falla: falta, o apunta a otro estándar. |
| **El estándar** (reglas y plantillas) | `VERSION` del estándar contra la versión que declara el `CLAUDE.md` del proyecto. |

Aplicar la actualización es siempre lo mismo:

```sh
python validadores/instalar.py "<proyecto>" --aplicar
```

Es idempotente: lo que ya está al día no se toca. Lo único que no aplica solo es subir la **versión adoptada** del estándar — esa es decisión del usuario, porque un cambio de norma no reabre fases ya cerradas.
