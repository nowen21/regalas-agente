# -*- coding: utf-8 -*-
"""Separa los cambios sin guardar de la sesión `c3d82767` (EP-025) de los de otras sesiones.

Es de esta sesión lo que escribió con Edit o Write, lo que declaran los planes
de EP-025, y sus documentos. Lo demás es de otra sesión y no se sube con ella.
Se corre desde la raíz del estándar.
"""
import glob
import json
import os
import re
import subprocess
import sys

SESION = "c3d82767-700e-401c-88e8-0dcb67432d0d"
TRANSCRIPCION = os.path.expanduser("~/.claude/projects/c--Ing--Jose-ia-agente/%s.jsonl" % SESION)


def normal(ruta):
    return os.path.normcase(os.path.abspath(ruta))


def escritos():
    rutas = set()
    for linea in open(TRANSCRIPCION, encoding="utf-8"):
        try:
            dato = json.loads(linea)
        except ValueError:
            continue
        if dato.get("type") != "assistant":
            continue
        for bloque in dato["message"].get("content") or []:
            if isinstance(bloque, dict) and bloque.get("type") == "tool_use" and bloque.get("name") in ("Edit", "Write"):
                rutas.add(normal((bloque.get("input") or {}).get("file_path") or ""))
    return rutas


def declarados():
    rutas = set()
    for plan in glob.glob("documentacion/epicas/EP-025-*/HU-*/A-*/plan_trabajo.md"):
        texto = open(plan, encoding="utf-8").read()
        for ruta in re.findall(r"`((?:proyectos|adaptadores|validadores|documentacion|plantillas)/[^`*]+?)`", texto):
            rutas.add(normal(ruta))
    return rutas


def de_la_sesion(ruta, propios):
    return (normal(ruta) in propios or "EP-025" in ruta or "2026-10-04-sesion-3" in ruta
            or "resumenes/2026-10-04/sesion-3" in ruta or "/2026-10-05/cerrar_hu_" in ruta)


def main():
    propios = escritos() | declarados()
    estado = subprocess.run(["git", "-c", "core.quotepath=false", "status", "--porcelain", "-uall"],
                            capture_output=True, text=True, encoding="utf-8").stdout.splitlines()
    mios = [l for l in estado if de_la_sesion(l[3:].strip().strip('"'), propios)]
    ajenos = [l for l in estado if l not in mios]
    sys.stdout.reconfigure(encoding="utf-8")
    print("DE ESTA SESIÓN", len(mios))
    print("\n".join(mios))
    print("DE OTRAS", len(ajenos))
    print("\n".join(ajenos))


if __name__ == "__main__":
    main()
