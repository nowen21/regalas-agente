#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `SessionStart`: entrega el núcleo al abrir, y vuelve a cero después de un resumen.

    python hook_reglas_sesion.py --raiz "C:/ruta/del/proyecto"

`EP-005·HU-027` · El núcleo manda sobre todas las reglas y no llegaba completo en
ningún momento. Al abrir la sesión llega por `additionalContext`; lo que no cabe,
con los mensajes siguientes (análisis 1 del pendiente 133, acuerdo 4).

Claude Code corre `SessionStart` con origen `compact` justo después de resumir
la conversación, y con `clear` al limpiarla. Ahí lo entregado ya no está a la
vista: la cuenta del agente principal vuelve a cero, y el núcleo, `responder` y
las reglas de cada tarea llegan otra vez (acuerdo 5).

Sale siempre con código 0: entregar una regla no puede costar la sesión.
"""
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "proyectos", "cimiento"))

from core.comun.consola import preparar_salida                    # noqa: E402
from core.herramientas.entrega_de_reglas import EntregaDeReglas    # noqa: E402


def opcion(argv, nombre, por_defecto=""):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return por_defecto


def _entrada():
    """Lo que la herramienta manda por la entrada estándar, o `{}`."""
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return {}


def main():
    from core.enganches.suspendidos import salir_si_esta_suspendido
    salir_si_esta_suspendido(__file__)
    preparar_salida()
    datos = _entrada()
    proyecto = os.path.abspath(opcion(sys.argv[1:], "--raiz") or datos.get("cwd") or os.getcwd())
    try:
        texto = EntregaDeReglas(proyecto, estandar=RAIZ).al_abrir(
            datos.get("session_id") or "", datos.get("source") or "")
    except Exception:                     # noqa: BLE001 — nunca cuesta la sesión
        return 0
    if texto:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                                 "additionalContext": texto}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
