#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code: el freno después de actuar (capa 2).

    python hook_despues.py --raiz <proyecto>

`EP-023·HU-007·CA-02` · Corre después de cada orden de consola (`PostToolUse`
sobre la consola). Compara lo que cambió en git con la foto que tomó
`hook_antes.py` justo antes de la orden: así ve lo que un programa escribió por
dentro, aunque solo dentro del proyecto. Lo que cambió fuera del plan de la fase
en curso y de lo autorizado es un hallazgo: lo anota en el resumen de la sesión
y se lo devuelve al agente. Lo ya hecho no se deshace: se avisa para volver al
análisis. La decisión vive en `validadores/freno.py`.

Siempre sale con código 0.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))

import freno                                    # noqa: E402
from comun import preparar_salida               # noqa: E402


def _entrada():
    try:
        crudo = sys.stdin.buffer.read()
    except (AttributeError, ValueError):
        crudo = (sys.stdin.read() or "").encode("utf-8", "replace")
    try:
        return json.loads(crudo.decode("utf-8", "replace"))
    except (json.JSONDecodeError, ValueError):
        return {}


def opcion(argv, nombre, por_defecto=""):
    if nombre in argv:
        i = argv.index(nombre)
        if i + 1 < len(argv):
            return argv[i + 1]
    return por_defecto


def main():
    preparar_salida()
    proyecto = os.path.abspath(opcion(sys.argv[1:], "--raiz", os.getcwd()))
    try:
        datos = _entrada()
        if (datos.get("tool_name") or "") not in freno.CONSOLA:
            return 0
        fuera = freno.despues(proyecto)
        if not fuera:
            return 0
        sesion = datos.get("session_id") or ""
        avisos = []
        for ruta, porque in fuera:
            anotado = freno.anotar_hallazgo(proyecto, sesion, "lo que escribió una orden de consola", ruta, porque)
            avisos.append(freno.aviso(porque, ruta, bool(anotado)))
        print(json.dumps({"decision": "block", "reason": "\n\n".join(avisos)}, ensure_ascii=False))
    except Exception as error:  # noqa: BLE001 — un error propio no detiene el trabajo
        print(json.dumps({"systemMessage": "[EL FRENO FALLÓ DESPUÉS DE LA ORDEN] %s" % error},
                         ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
