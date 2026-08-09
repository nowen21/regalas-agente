# `hook_historico.py`

Arranca solo dos veces por cada intercambio y va guardando la conversación en el repositorio.

## Qué hace

Es un mismo archivo enganchado a dos momentos:

| Cuándo arranca | Cómo se lo llama | Qué anota |
|---|---|---|
| El usuario envía un mensaje | `--modo usuario` | El mensaje, tal como lo escribió. |
| El agente termina de responder | `--modo agente` | La respuesta, leída del archivo donde Claude Code va guardando todo. |

Entre los dos, la conversación queda guardada completa sin que nadie tenga que acordarse de copiarla. El chat se borra; el repositorio no.

Un proyecto que no tenga la carpeta `historico-chat/` no se entera de nada: el programa se sale sin hacer nada.

Termina bien siempre. Que no se haya podido guardar la conversación es un problema; que por eso no se pueda trabajar, uno peor.

## De qué depende y quién lo usa

```
hook_historico.py
   ├── historico.py ··· anotar_usuario() y anotar_agente()
   └── comun.py ······· preparar_salida
```

De Python usa `json`, `os` y `sys`.

Ningún archivo lo usa a él. Lo llama Claude Code cuando se envía un mensaje y cuando la respuesta termina.

## Qué tiene adentro

**`opcion(argv, nombre, por_defecto="")`**

- **Recibe:** lo que se escribió en la consola, qué opción se está buscando y qué usar si no está.
- **Hace:** busca esa opción y toma lo que viene después.
- **Retorna:** ese valor, o el de reserva.

**`_entrada()`**

- **Recibe:** nada; lee lo que Claude Code le manda.
- **Hace:** lo lee tal cual llega y lo traduce él mismo a UTF-8, que es la forma de escribir que incluye tildes y eñes, en vez de dejar que Python lo adivine. En Windows, Python adivinaba mal y los mensajes con tildes quedaban guardados con los caracteres rotos.
- **Retorna:** los datos que mandó Claude Code, ya entendibles, o nada si venían mal escritos.

**`main()`**

- **Recibe:** nada.
- **Hace:**
  1. Deja la pantalla lista y mira en qué momento lo llamaron. Si no se lo dicen, supone que fue el usuario quien escribió.
  2. Lee lo que le mandaron. Si no le mandaron nada, termina sin hacer nada.
  3. Averigua la carpeta: primero lo que diga `--raiz`, después lo que diga Claude Code, y si no, la carpeta donde está parado.
  4. Saca el número que identifica la conversación.
  5. Según el momento, llama a `anotar_agente` diciéndole dónde está el archivo de la conversación, o a `anotar_usuario` con el texto del mensaje.
  6. Si algo se rompe, deja escrito el error aparte y sigue.
- **Retorna:** siempre `0`, o sea que terminó bien.

## Cómo se ejecuta

Lo deja puesto `instalar.py` en el archivo de ajustes `.claude/settings.json`, enganchado a dos momentos:

```
UserPromptSubmit → python "<estandar>/validadores/hook_historico.py" --modo usuario --raiz "<proyecto>"
Stop             → python "<estandar>/validadores/hook_historico.py" --modo agente  --raiz "<proyecto>"
```

Por dentro:

```
el usuario envía un mensaje
        ↓
hook_historico.py --modo usuario
        ↓
_entrada()   ← qué conversación es, en qué carpeta y qué se escribió
        ↓
historico.anotar_usuario(carpeta, sesion, mensaje)
        ↓
   escribe el mensaje en historico-chat/<archivo de la conversación>.md


el agente termina de responder
        ↓
hook_historico.py --modo agente
        ↓
_entrada()   ← qué conversación es, en qué carpeta y dónde está guardada
        ↓
historico.anotar_agente(carpeta, sesion, donde_esta_guardada)
        ↓
   lee de ahí la última respuesta y la escribe
```

## Ejemplos de lo que retorna

```python
opcion(['--modo', 'agente', '--raiz', 'C:/proyectos/pos'], '--modo')
'agente'

opcion(['--raiz', 'C:/proyectos/pos'], '--modo', 'usuario')
'usuario'        # no estaba: retorna el de reserva

_entrada()       # cuando el usuario escribió un mensaje
{'session_id': '69ebc47d-a122-4622-b383-3601eca36ee5',
 'cwd': 'C:/proyectos/pos',
 'prompt': 'Documente los validadores.'}

_entrada()       # cuando el agente terminó de responder
{'session_id': '69ebc47d-a122-4622-b383-3601eca36ee5',
 'cwd': 'C:/proyectos/pos',
 'transcript_path': 'C:/Users/user/.claude/projects/…/69ebc47d.jsonl'}

_entrada()       # si no le mandaron nada entendible
None

main()
0                # siempre
```

No imprime nada en pantalla. Lo único que deja es lo escrito en el archivo de la conversación:

```markdown
### 3 · Usuario — 2026-08-09 22:42:46
> Documente los validadores.

**Agente** — 2026-08-09 22:45:10
<!-- agente: 8f21ac30-1b4e-4f77-9c02-5db1e6a44f10 -->

Listo. 40 documentos en validadores/docs/…
```

Si algo se rompe, deja el error aparte y sigue:

```
No se pudo escribir el histórico: [Errno 13] Permission denied: '…'
```
