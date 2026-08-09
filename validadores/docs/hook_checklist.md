# `hook_checklist.py`

Arranca solo con cada mensaje del usuario y revisa qué le falta al proyecto para quedar bien instalado.

## Qué hace

Corre la revisión de `checklist.py`. Mientras falte alguna pieza, en **cada** mensaje:

- escribe `.agente/INSTALACION-INCOMPLETA.md` con la lista de lo que falta y cómo se arregla;
- se lo muestra al usuario;
- se lo pasa al agente, con la orden de decírselo al usuario en esa misma respuesta.

Cuando ya no falta nada, borra ese archivo y se calla. Un aviso que sale siempre, aunque todo esté bien, a los dos días nadie lo lee.

No traba nada: un proyecto a medio instalar igual puede tener trabajo urgente.

Si la carpeta es la del estándar mismo, no hace nada: el estándar no se instala a sí mismo.

Termina bien siempre.

## De qué depende y quién lo usa

```
hook_checklist.py
   ├── checklist.py ··· revisar(), escribir_marca(), pendientes(),
   │                    resumen(), detalle() y MARCA
   └── comun.py ······· RAIZ y preparar_salida
```

De Python usa `json`, `os` y `sys`.

Ningún archivo lo usa a él. Lo llama Claude Code cada vez que el usuario envía un mensaje.

## Qué tiene adentro

**`opcion(argv, nombre, por_defecto="")`**

- **Recibe:** lo que se escribió en la consola, qué opción se busca y qué usar si no está.
- **Retorna:** lo que viene después de esa opción, o el valor de reserva.

**`_entrada()`**

- **Recibe:** nada; lee lo que Claude Code le manda.
- **Hace:** lo lee tal cual llega y lo traduce a UTF-8, la forma de escribir que incluye tildes y eñes.
- **Retorna:** esos datos ya entendibles, o nada si venían mal escritos.

**`main()`**

- **Recibe:** nada.
- **Hace:**
  1. Deja la pantalla lista y lee lo que le mandaron.
  2. Averigua la carpeta: primero lo que diga `--raiz`, después lo que diga Claude Code, y si no, la carpeta donde está parado.
  3. Si esa carpeta es la del estándar mismo, termina.
  4. Corre `checklist.revisar` y `checklist.escribir_marca`. Si algo se rompe, deja escrito el error aparte y termina; nunca tumba la sesión.
  5. Si no falta nada, termina callado.
  6. Si falta algo, responde con el resumen para el usuario y el detalle para el agente.
- **Retorna:** siempre `0`, o sea que terminó bien.

## Cómo se ejecuta

Lo deja puesto `instalar.py` en el archivo de ajustes `.claude/settings.json`, para que arranque con cada mensaje:

```
python "<estandar>/validadores/hook_checklist.py" --raiz "<proyecto>"
```

Por dentro:

```
el usuario envía un mensaje
        ↓
hook_checklist.py --raiz <proyecto>
        ↓
¿la carpeta es la del estándar mismo?
     sí → termina sin hacer nada
     no ↓
checklist.revisar(carpeta)
     lee plantillas/stack-instalacion.md y comprueba cada pieza
        ↓
checklist.escribir_marca(carpeta, puntos)
     si falta algo → escribe .agente/INSTALACION-INCOMPLETA.md
     si no falta   → borra ese archivo
        ↓
¿falta algo?
     no → termina callado
     sí ↓
responde con dos partes:
     para el usuario → "INSTALACIÓN INCOMPLETA · proyecto · 9 de 13 · falta: ..."
     para el agente  → el detalle y la orden de decírselo al usuario
```

## Ejemplos de lo que retorna

```python
opcion(['--raiz', 'C:/proyectos/pos'], '--raiz')
'C:/proyectos/pos'

opcion([], '--raiz')
''               # no estaba y no se dio valor de reserva

_entrada()
{'session_id': '69ebc47d-…', 'cwd': 'C:/proyectos/pos',
 'prompt': 'Documente los validadores.'}

_entrada()       # si no le mandaron nada entendible
{}

main()
0                # siempre
```

Cuando **no falta nada**, no imprime nada. Cuando falta algo, imprime esto:

```json
{
  "systemMessage": "INSTALACIÓN INCOMPLETA · pos · 11 de 13 · falta: gitignore, version",
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "[Instalación del agente incompleta]\nINSTALACIÓN INCOMPLETA · pos · 11 de 13 · falta: gitignore, version\n\n- **gitignore** — al .gitignore le faltan: CLAUDE.md, .agente/\n  Se arregla así: correr validadores/instalar.py --aplicar\n- **version** — el proyecto no declara qué versión del estándar sigue\n  Se arregla así: fijarla en su CLAUDE.md\n\nDecíselo al usuario en esta respuesta: qué falta y cómo se arregla. El detalle también quedó en `.agente/INSTALACION-INCOMPLETA.md`."
  }
}
```

Y deja escrito el archivo `.agente/INSTALACION-INCOMPLETA.md`:

```markdown
# Instalación del agente incompleta

Comprobado: 2026-08-09 22:42:46 · faltan 2 de 13 componentes.

## Qué falta

- **gitignore** — al .gitignore le faltan: CLAUDE.md, .agente/
  Se arregla así: correr validadores/instalar.py --aplicar

## Se resuelve con una línea

python "c:/Ing. Jose/ia/agente/validadores/instalar.py" "C:/proyectos/pos" --aplicar
```

Si algo se rompe, deja el error aparte y termina bien igual:

```
No se pudo revisar la instalación: [Errno 2] No such file or directory: '…'
```
