# `hook_antes.py`

Arranca solo antes de cada escritura de archivo del agente. Si el archivo queda fuera de la carpeta del proyecto, detiene la escritura y dice dónde va el guion de apoyo.

## Qué hace

El 2026-09-28 el agente escribió guiones en la carpeta temporal de la herramienta, en contra de `04·S9` y `04·S18`. Este enganche lo impide: antes de escribir, compara la ruta con la carpeta del proyecto. Una carpeta hermana que empieza igual cuenta como afuera.

Hasta el 2026-09-29 también obligaba al agente a leer por comando las reglas de cada tarea antes de actuar y de responder, y las olvidaba con cada mensaje. El usuario lo descartó: llenaba la conversación de lecturas y no hacía cumplir nada. Las reglas llegan con cada mensaje por [recuperar.md](recuperar.md), según la palabra de `01·C28`.

Si algo falla adentro, deja pasar: un error del enganche no detiene el trabajo.

## De qué depende y quién lo usa

```
hook_antes.py
   └── comun.py ········· preparar_salida
```

Ningún archivo lo usa a él. Lo llama Claude Code, con la orden que `instalar.py` dejó escrita en `.claude/settings.json`.

## Cómo se ejecuta

```
python "<estandar>/adaptadores/claude-code/hook_antes.py" --modo accion --raiz "<proyecto>"
```

Cuando detiene una escritura, responde:

```json
{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
  "permissionDecisionReason": "[NO SE ESCRIBE FUERA DEL PROYECTO: …]\nTodo lo del trabajo vive en el repositorio (`04·S9`). …"}}
```
