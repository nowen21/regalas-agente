#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enganche para Claude Code: revisa los enlaces tras editar un `.md`.

Se conecta como hook `PostToolUse` sobre `Write|Edit` en `.claude/settings.json`.
Lee por la entrada estándar el JSON que envía Claude Code y:

  - si el archivo editado NO es un `.md` del proyecto -> no hace nada;
  - si lo es -> comprueba enlaces e índices de ese proyecto.

    python hook_md.py [--raiz <carpeta del proyecto>]

Sin `--raiz` revisa el repositorio del estándar. Con `--raiz` revisa el proyecto
indicado — así el mismo archivo sirve para todos los proyectos sin copiarse.

Sin dependencias externas: en esta máquina no hay `jq`, y de todos modos hacerlo
en Python evita depender de qué trae instalado cada equipo.

Códigos de salida:
  0 — todo bien (o no aplicaba).
  2 — hay fallas; Claude Code se lo devuelve al modelo para que las corrija.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import enlaces                                          # noqa: E402
from comun import FALLA, RAIZ, preparar_salida          # noqa: E402


def raiz_pedida(argv):
    """La carpeta a revisar: `--raiz X`, o el estándar si no se indica."""
    if "--raiz" in argv:
        i = argv.index("--raiz")
        if i + 1 < len(argv):
            return os.path.abspath(argv[i + 1])
    return RAIZ


def archivo_editado(datos):
    """La ruta del archivo, mirando primero la entrada y luego la respuesta."""
    entrada = datos.get("tool_input") or {}
    respuesta = datos.get("tool_response") or {}
    return (entrada.get("file_path")
            or respuesta.get("filePath")
            or respuesta.get("file_path")
            or "")


def es_md_de(ruta, raiz):
    if not ruta.lower().endswith(".md"):
        return False
    try:
        return os.path.commonpath([os.path.abspath(ruta), raiz]) == raiz
    except ValueError:      # otra unidad en Windows
        return False


def main():
    preparar_salida()
    raiz = raiz_pedida(sys.argv[1:])

    try:
        datos = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0            # sin JSON válido no hay nada que revisar

    if not es_md_de(archivo_editado(datos), raiz):
        return 0

    hallazgos = enlaces.validar_enlaces(raiz) + enlaces.validar_indices(raiz)
    fallas = [h for h in hallazgos if h.severidad == FALLA]
    if not fallas:
        return 0

    print("La edición dejó enlaces rotos:", file=sys.stderr)
    for h in fallas:
        print(f"  {h}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
