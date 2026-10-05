#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El portero: lo que llega de afuera llega marcado — `EP-005 · HU-015`.

Se conecta en `.claude/settings.json`:

    PostToolUse (WebFetch|WebSearch|Read|mcp__.*) -> python hook_externo.py --raiz <proyecto>

Lee por la entrada estándar el JSON que envía la herramienta, saca el nombre de
la herramienta que acaba de devolver y sus argumentos, y le pregunta a
`proyectos/cimiento/core/enganches/externo.py` si eso vino de afuera. Si sí, devuelve el sobre como
**contexto adicional** para el agente: la herramienta, el origen y la frase de
que es dato y no orden (`01·C27`). El resultado de la herramienta no se toca.

**Por qué contexto adicional y no reemplazar el resultado.** Lo primero está
documentado y no depende de la forma del resultado, que cambia por
herramienta; de lo segundo la documentación no dice qué herramientas lo
aceptan.

Siempre sale con código 0: un enganche que detiene el trabajo es peor que el
problema que resuelve.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `core/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import entrada_json, preparar_salida, raiz_pedida     # noqa: E402
from core.enganches.externo import ContenidoExterno              # noqa: E402


def main():
    preparar_salida()
    try:
        datos = entrada_json()
    except (json.JSONDecodeError, ValueError):
        return 0                        # sin JSON válido no hay nada que mirar
    if not isinstance(datos, dict):
        return 0
    nombre = datos.get("tool_name") or ""
    entrada = datos.get("tool_input")
    raiz = raiz_pedida(sys.argv[1:], datos.get("cwd") or os.getcwd())
    try:
        if not ContenidoExterno.es_externa(nombre, entrada, raiz):
            return 0
        texto = ContenidoExterno.sobre(nombre, entrada, raiz)
    except Exception as e:                                  # noqa: BLE001
        print(f"[el portero no pudo correr: {e}]")
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PostToolUse",
        "additionalContext": texto}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
