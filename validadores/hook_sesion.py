#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `SessionStart` de Claude Code — avisa si el estándar se cargó bien.

    python hook_sesion.py --raiz "C:/ruta/del/proyecto"

Devuelve por la salida estándar un JSON con `systemMessage`, que Claude Code
muestra al usuario. Siempre sale con código 0: esto **informa**, no bloquea —
una sesión que no arranca porque falta una sección del `CLAUDE.md` sería peor
que el problema que resuelve.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sesion                                   # noqa: E402
from comun import RAIZ, preparar_salida         # noqa: E402


def raiz_pedida(argv):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(os.getcwd())


def main():
    preparar_salida()
    proyecto = raiz_pedida(sys.argv[1:])

    # El propio estándar no se revisa a sí mismo como si fuera un proyecto.
    if os.path.normcase(proyecto) == os.path.normcase(RAIZ):
        return 0

    try:
        hallazgos = sesion.revisar(proyecto, RAIZ)
    except Exception as e:      # noqa: BLE001 — nunca romper el arranque
        _responder(f"No se pudo revisar el arranque del estándar: {e}", [])
        return 0

    _responder(sesion.resumen(proyecto, hallazgos), hallazgos)
    return 0


def _responder(resumen, hallazgos):
    """Sale por dos canales, a propósito.

    `systemMessage` lo muestra Claude Code al usuario. `additionalContext` se
    lo inyecta al agente. Van los dos porque el primero depende de que la
    interfaz lo dibuje, y si no lo dibuja el aviso se pierde sin dejar rastro
    — que es justo el problema que este enganche vino a resolver. Con el
    segundo, el agente lo sabe y puede decirlo aunque el banner no aparezca.
    """
    detalle = "\n".join(f"  - {h}" for h in hallazgos)
    contexto = resumen if not detalle else f"{resumen}\n{detalle}"

    print(json.dumps({
        "systemMessage": resumen,
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": (
                f"[Revisión de arranque del estándar]\n{contexto}"),
        },
    }, ensure_ascii=False))


if __name__ == "__main__":
    sys.exit(main())
