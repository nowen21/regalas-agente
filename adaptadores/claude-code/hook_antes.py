#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code: el freno antes de actuar (capa 1).

    python hook_antes.py --modo accion --raiz <proyecto>

`EP-023·HU-007·CA-02` · Corre antes de **toda** acción (`PreToolUse` sin filtro
de herramienta). Detiene lo que no está en el plan de la fase en curso ni lo
autoriza una regla, por cualquier canal: la herramienta de escritura, la
consola, el segundo plano. Lo que se publica fuera del proyecto se pregunta
cada vez. Al detener, anota el hallazgo en el resumen de la sesión, salvo con
un análisis prendido: ahí se reporta en la conversación. Antes de
cada orden de consola toma la foto que usa `hook_despues.py`.

Nació en `EP-005·HU-023·RN-10` para que ninguna escritura saliera del proyecto
(`04·S9`); eso sigue, ahora dentro del freno. La decisión vive en
`validadores/freno.py`; acá solo está lo que habla con esta herramienta.

Nunca rompe el trabajo por un error propio: si algo falla adentro, deja pasar y
lo avisa.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import freno                                    # noqa: E402
from comun import preparar_salida               # noqa: E402

ACCION = {"Write": "una escritura", "Edit": "una edición", "MultiEdit": "una edición",
          "NotebookEdit": "una edición", "Bash": "una orden de consola",
          "PowerShell": "una orden de consola"}
GUION = ("El guion de apoyo va en `historico-chat/scripts/AAAA-MM-DD/`, con su fila en el "
         "README de esa carpeta, y se queda (`04·S18`).")


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


def _decision(decision, razon):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": razon}}, ensure_ascii=False))


def accion(datos, proyecto):
    herramienta = datos.get("tool_name") or ""
    entrada = datos.get("tool_input") or {}
    cwd = datos.get("cwd") or proyecto
    decision, porque, ruta = freno.revisar(proyecto, herramienta, entrada, cwd)
    if decision == "pregunta":
        _decision("ask", "[EL FRENO PREGUNTA] " + porque[0].upper() + porque[1:] + ".")
    elif decision == "detiene":
        que = ACCION.get(herramienta, "una acción")
        anotado = freno.anotar_hallazgo(proyecto, datos.get("session_id") or "", que, ruta, porque)
        razon = freno.aviso(porque, ruta, bool(anotado), freno.analisis_prendido(proyecto))
        if "04·S9" in porque:
            razon += "\n" + GUION
        _decision("deny", razon)
    elif herramienta in freno.CONSOLA:
        freno.tomar_foto(proyecto)
    return 0


def main():
    preparar_salida()
    if opcion(sys.argv[1:], "--modo") != "accion":
        return 0
    proyecto = os.path.abspath(opcion(sys.argv[1:], "--raiz", os.getcwd()))
    try:
        return accion(_entrada(), proyecto)
    except Exception as error:  # noqa: BLE001 — un error propio no detiene el trabajo
        print(json.dumps({"systemMessage": "[EL FRENO FALLÓ Y DEJÓ PASAR] %s" % error},
                         ensure_ascii=False))
        return 0


if __name__ == "__main__":
    sys.exit(main())
