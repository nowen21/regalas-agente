# -*- coding: utf-8 -*-
"""Devuelve a su versión de git los renglones donde el reparador de enlaces dejó
un texto terminado en `.md/` (sesión del 2026-10-04, análisis 1 del pendiente 116).

El reparador le pegaba el nombre del archivo a un texto que nombraba una carpeta
y le dejaba la barra: `[base/x/](x/README.md)` pasaba a `[base/x/README.md/](…)`.
El reparador cambia texto, nunca la cantidad de renglones, así que el renglón
dañado se restaura por su posición sin tocar los demás cambios del archivo.

    python restaurar_textos_de_enlace.py
"""
import os
import re
import subprocess

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DANADO = re.compile(r"\[[^\]]*\.md/\]\(")


def cambiados():
    salida = subprocess.run(["git", "-C", RAIZ, "diff", "--name-only"],
                            capture_output=True, text=True, encoding="utf-8").stdout
    return [l.strip() for l in salida.splitlines() if l.strip().endswith(".md")]


def main():
    for relativa in cambiados():
        ruta = os.path.join(RAIZ, *relativa.split("/"))
        with open(ruta, encoding="utf-8", newline="") as f:
            ahora = f.read().split("\n")
        if not any(DANADO.search(l) for l in ahora):
            continue
        antes = subprocess.run(["git", "-C", RAIZ, "show", "HEAD:" + relativa],
                               capture_output=True).stdout.decode("utf-8").split("\n")
        if len(antes) != len(ahora):
            print("se salta, cambió la cantidad de renglones:", relativa)
            continue
        arreglados = 0
        for i, linea in enumerate(ahora):
            if DANADO.search(linea):
                ahora[i] = antes[i].rstrip("\r") + ("\r" if linea.endswith("\r") else "")
                arreglados += 1
        with open(ruta, "w", encoding="utf-8", newline="") as f:
            f.write("\n".join(ahora))
        print(arreglados, relativa)


if __name__ == "__main__":
    main()
