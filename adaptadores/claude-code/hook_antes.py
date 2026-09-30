#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code: ninguna escritura sale de la carpeta del proyecto.

    python hook_antes.py --modo accion --raiz <proyecto>

`EP-005·HU-023·RN-10` · **Por qué existe.** El 2026-09-28 el agente escribió
guiones en la carpeta temporal de la herramienta, en contra de `04·S9` y
`04·S18`, y el usuario pidió que eso no pudiera volver a pasar. Antes de cada
escritura (`PreToolUse`), si el archivo queda fuera del proyecto, detiene la
acción y dice dónde va el guion de apoyo.

**Ya no obliga a leer las reglas.** Hasta el 2026-09-29 este enganche detenía
cada acción y cada respuesta hasta que el agente leyera por comando las reglas
de la tarea, y las olvidaba con cada mensaje. El usuario lo descartó: llenaba
la conversación de lecturas y no hacía cumplir nada. Las reglas llegan con
cada mensaje por `recuperar.py`, según la palabra de `01·C28`.

Nunca rompe el trabajo por un error propio: si algo falla adentro, deja pasar.
"""
import json
import os
import sys

# **Vive en el adaptador, no en `validadores/`.** Por eso tiene que decir
# dónde están los módulos que usa: el trabajo es agnóstico y sigue allá;
# acá sólo está lo que habla con esta herramienta.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

from comun import preparar_salida               # noqa: E402

ESCRITURA = ("Write", "Edit", "MultiEdit", "NotebookEdit")


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


def fuera_del_proyecto(herramienta, entrada, proyecto):
    """La ruta que la acción escribiría fuera del proyecto, o `None`."""
    if herramienta not in ESCRITURA:
        return None
    entrada = entrada or {}
    ruta = entrada.get("file_path") or entrada.get("notebook_path") or ""
    if not ruta:
        return None
    dentro = os.path.normcase(os.path.abspath(proyecto)).rstrip(os.sep)
    destino = os.path.normcase(os.path.abspath(ruta))
    if destino == dentro or destino.startswith(dentro + os.sep):
        return None
    return ruta


def accion(datos, proyecto):
    afuera = fuera_del_proyecto(datos.get("tool_name") or "",
                                datos.get("tool_input"), proyecto)
    if not afuera:
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            f"[NO SE ESCRIBE FUERA DEL PROYECTO: {afuera}]\n"
            "Todo lo del trabajo vive en el repositorio (`04·S9`). El guion de "
            "apoyo va en `historico-chat/scripts/AAAA-MM-DD/`, con su fila en el "
            "README de esa carpeta, y se queda (`04·S18`).")}},
        ensure_ascii=False))
    return 0


def main():
    preparar_salida()
    if opcion(sys.argv[1:], "--modo") != "accion":
        return 0
    proyecto = os.path.abspath(opcion(sys.argv[1:], "--raiz", os.getcwd()))
    try:
        return accion(_entrada(), proyecto)
    except Exception:           # noqa: BLE001 — un error propio no detiene el trabajo
        return 0


if __name__ == "__main__":
    sys.exit(main())
