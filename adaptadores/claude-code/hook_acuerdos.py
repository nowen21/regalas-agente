#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `UserPromptSubmit`: entrega con cada mensaje los acuerdos de lo que se trabaja.

    python hook_acuerdos.py --raiz "C:/ruta/del/proyecto"

`EP-023 · HU-002 · CA-04` · El agente escribía planes sin seguir el «Sale de» de
cada criterio hasta los acuerdos del análisis, y preguntaba lo que ya estaba
decidido (H-13 del 2026-10-01). Igual que las reglas, los acuerdos le llegan con
cada mensaje y no dependen de que se acuerde de buscarlos. El trabajo lo hace
`validadores/acuerdos.py`; acá solo está lo que habla con la herramienta.

Va en un enganche propio porque la herramienta acepta un máximo por enganche, y
el de las reglas ya va casi lleno.

Siempre sale con código 0: un error propio no detiene el trabajo.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import acuerdos                                     # noqa: E402
from comun import preparar_salida                   # noqa: E402


def _entrada():
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return {}


def opcion(argv, nombre):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return ""


def main():
    preparar_salida()
    try:
        entrada = _entrada()
        raiz = os.path.abspath(opcion(sys.argv[1:], "--raiz") or entrada.get("cwd") or os.getcwd())
        bloque = acuerdos.texto(raiz)
    except Exception:           # noqa: BLE001 — un error propio no detiene el trabajo
        return 0
    if bloque:
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": bloque}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
