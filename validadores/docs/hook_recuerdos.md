# `hook_recuerdos.py`

Arranca solo al empezar a trabajar y cada vez que se escribe un archivo, y trae los recuerdos del agente al repositorio.

## Qué hace

Corre la mudanza que hace `recuerdos.py`. Está enganchado a dos momentos, por dos razones distintas:

- **Al empezar a trabajar**, para recoger lo que haya quedado de otras veces, antes de que el agente escriba nada.
- **Cada vez que se escribe o se cambia un archivo**, para recoger el recuerdo justo cuando se acaba de escribir. Sin esto, el archivo se pasaría toda la sesión en la carpeta equivocada y el agente creería que ya quedó guardado donde debía.

**Solo mueve. No borra nada, nunca**, y no hace nada si la carpeta de la herramienta y la del proyecto ya son la misma. Un programa que arranca solo, en cada sesión y en cada archivo que se escribe, no puede tener permiso para destruir.

A diferencia de los otros, este **sí corre cuando se trabaja en el estándar mismo**: ahí es justamente donde viven los recuerdos del usuario.

Termina bien siempre.

## De qué depende y quién lo usa

```
hook_recuerdos.py
   ├── recuerdos.py ··· migrar(), pasos(), CARPETA e INDICE
   └── comun.py ······· preparar_salida
```

De Python usa `json`, `os` y `sys`.

Ningún archivo lo usa a él. Lo llama Claude Code al abrir una sesión y después de cada archivo que se escribe.

## Qué tiene adentro

**`opcion(argv, nombre, por_defecto="")`**

- **Recibe:** lo que se escribió en la consola, qué opción se busca y qué usar si no está.
- **Retorna:** lo que viene después de esa opción, o el valor de reserva.

**`_entrada()`**

- **Recibe:** nada; lee lo que Claude Code le manda.
- **Retorna:** esos datos ya entendibles, o nada si venían mal escritos.

**`main()`**

- **Recibe:** nada.
- **Hace:**
  1. Deja la pantalla lista y lee lo que le mandaron.
  2. Averigua la carpeta: primero lo que diga `--raiz`, después lo que diga Claude Code, y si no, la carpeta donde está parado.
  3. Mira en cuál de los dos momentos lo llamaron; si no se lo dicen, supone que la sesión recién empieza.
  4. Llama a `recuerdos.migrar`. Si no puede por falta de permisos o porque un archivo está abierto en otro lado, deja escrito el error y termina.
  5. Si no movió nada, termina callado.
  6. Si movió algo, responde con el resumen para el usuario y, para el agente, el detalle de cada mudanza más tres recordatorios: dónde viven ahora los recuerdos, que hay que agregar su línea al índice, y que si algún nombre terminó con `-local` hay que decidir con el usuario cuál se queda.
- **Retorna:** siempre `0`, o sea que terminó bien.

## Cómo se ejecuta

Lo deja puesto `instalar.py` en el archivo de ajustes `.claude/settings.json`, enganchado a dos momentos:

```
al abrir la sesión     → python "<estandar>/validadores/hook_recuerdos.py" --raiz "<proyecto>"
al escribir un archivo → python "<estandar>/validadores/hook_recuerdos.py" --raiz "<proyecto>"
```

Por dentro:

```
se abre la sesión, o el agente escribe un archivo
        ↓
hook_recuerdos.py --raiz <proyecto>
        ↓
recuerdos.migrar(carpeta, aplicar=True)
        ↓
   ¿la carpeta de la herramienta y la del proyecto son la misma?
        sí → no hay nada que mover
   ¿quedó algún archivo suelto?
        no → termina callado
        sí ↓
   los mueve a historico-chat/memory/
   si el nombre ya estaba ocupado, entra como <nombre>-local.md
        ↓
responde con dos partes:
   para el usuario → "Memoria del agente: 2 archivo(s) movidos a ..."
   para el agente  → el detalle y qué hacer con el índice
```

## Ejemplos de lo que retorna

```python
opcion(['--raiz', 'C:/proyectos/pos'], '--raiz')
'C:/proyectos/pos'

_entrada()
{'session_id': '69ebc47d-…', 'cwd': 'C:/proyectos/pos',
 'hook_event_name': 'PostToolUse'}

_entrada()       # si no le mandaron nada entendible
{}

main()
0                # siempre
```

Cuando **no había nada que mover**, no imprime nada. Cuando movió algo, imprime esto:

```json
{
  "systemMessage": "Memoria del agente: 2 archivo(s) movidos a historico-chat/memory/",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "[Memoria del agente — movida al repositorio]\n  - mover `estilo.md` a `historico-chat/memory/`\n  - mover `MEMORY.md` a `historico-chat/memory/MEMORY-local.md` — el nombre ya estaba ocupado; revisar cuál manda\n\nLa memoria vive en `historico-chat/memory/` del proyecto, versionada, un archivo por recuerdo (`01·C19`). La carpeta local de la herramienta queda vacía: no escribir nada ahí, ni siquiera un puntero. Agregar la línea del recuerdo al índice `historico-chat/memory/memory.md`, y si algún nombre terminó en `-local` decidir con el usuario cuál manda."
  }
}
```

Si no puede mover un archivo, deja el error aparte y termina bien igual:

```
No se pudo mover la memoria del agente: [WinError 32] El archivo está en uso
```
