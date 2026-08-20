#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche de Claude Code que reclama el checkpoint de la fase — `EP-005 · HU-013`.

Se conecta en `.claude/settings.json`:

    PostToolUse (Write|Edit) -> python hook_checkpoint.py --raiz <proyecto>

Lee por la entrada estándar el JSON que envía la herramienta, saca la ruta del
archivo escrito y le pregunta a `validadores/checkpoint.py` si esa escritura
pasó una puerta de la fase sin su `estado-fase.md`. Si sí, imprime el aviso.
Lo que no es de puerta, o no está en una fase, se ignora en silencio.

**No escribe el checkpoint.** Decir en qué estación va la fase es criterio.

Siempre sale con código 0: un enganche que detiene el trabajo es peor que el
problema que resuelve.
"""
import json
import os
import sys

# Vive en el adaptador, no en `validadores/`: por eso dice dónde están los
# módulos agnósticos que usa.
sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "validadores"))
import checkpoint                       # noqa: E402
from comun import preparar_salida       # noqa: E402


def raiz_pedida(argv):
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return os.path.abspath(os.getcwd())


def archivo_editado(datos):
    """La ruta del archivo, mirando primero la entrada y luego la respuesta."""
    entrada = datos.get("tool_input") or {}
    respuesta = datos.get("tool_response") or {}
    return (entrada.get("file_path")
            or respuesta.get("filePath")
            or respuesta.get("file_path")
            or "")


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:])
    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0                        # sin JSON válido no hay nada que mirar
    if not isinstance(datos, dict):
        return 0
    ruta = archivo_editado(datos)
    if not ruta:
        return 0
    try:
        hallazgo = checkpoint.rezago(ruta)
    except Exception as e:                                  # noqa: BLE001
        print(f"[el enganche del checkpoint no pudo correr: {e}]")
        return 0
    if hallazgo:
        print(checkpoint.como_texto(hallazgo, raiz))
    return 0


if __name__ == "__main__":
    sys.exit(main())
