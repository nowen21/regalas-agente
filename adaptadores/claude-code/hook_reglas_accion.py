#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche `PreToolUse`: entrega las reglas de la tarea que pide cada acción.

    python hook_reglas_accion.py --raiz "C:/ruta/del/proyecto"

`EP-005·HU-025` · Antes de escribir un archivo, correr un comando o usar una
herramienta de afuera, al agente le llegan las reglas de esa tarea, una sola vez
en la sesión (análisis 1 del pendiente 133, acuerdo 1). Van por
`additionalContext` y sin decisión de permiso: la acción sigue su curso y lo
que la herramienta le pregunte al usuario se le sigue preguntando.

**Va aparte del freno.** Si viviera en `hook_antes.py`, suspender el freno
apagaría también las reglas; cada uno se suspende por su nombre.

Sale siempre con código 0: entregar una regla no puede costar la acción.
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
        texto = EntregaDeReglas(proyecto, estandar=RAIZ).para_la_accion(
            datos.get("session_id") or "", datos.get("agent_id") or "",
            datos.get("tool_name") or "", datos.get("tool_input") or {})
    except Exception:                     # noqa: BLE001 — nunca cuesta la acción
        return 0
    if texto:
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                                 "additionalContext": texto}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
