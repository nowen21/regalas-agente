# -*- coding: utf-8 -*-
"""Cuanto ruido daria avisar de los archivos que ninguna sesion registro.

La comprobacion de hoy calla cuando menos de dos sesiones vivas tocaron lo que
entra al commit. Un archivo que NADIE registro no cuenta como de otro: cuenta
como de nadie, y por ahi entraron 712 lineas ajenas el 2026-08-27.

La idea a medir: avisar de los archivos sin registro **solo cuando al menos uno
de los que entran SI tiene registro de una sesion viva**. Eso significa que el
registro esta funcionando ahora mismo, asi que su silencio sobre los demas es
informacion y no ignorancia.

Se mide sobre los commits reales del historial: para cada uno, cuantos de sus
archivos habrian quedado sin registro.
"""
import os
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import sesiones                                          # noqa: E402


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout


registrados = set()
for sesion, archivos in sesiones.registros(RAIZ).items():
    registrados |= archivos

print("Sesiones vivas: %d" % len(sesiones.registros(RAIZ)))
print("Archivos con registro de alguna sesion viva: %d" % len(registrados))
print()

print("Sobre los ultimos commits, cuantos archivos habrian quedado SIN registro:")
print()
print("%-10s %-6s %-8s %-8s %s" % ("COMMIT", "TOTAL", "CON REG", "SIN REG", "AVISARIA"))
for linea in git("log", "--format=%h", "-12").splitlines():
    h = linea.strip()
    if not h:
        continue
    archivos = [l.strip() for l in
                git("show", "--name-only", "--pretty=format:", h).splitlines()
                if l.strip()]
    if not archivos:
        continue
    con = [a for a in archivos if a in registrados]
    sin = [a for a in archivos if a not in registrados]
    # La regla propuesta: solo avisa si HAY registro de algo que entra.
    avisaria = "SI (%d)" % len(sin) if con and sin else "no"
    print("%-10s %-6d %-8d %-8d %s" % (h, len(archivos), len(con), len(sin),
                                       avisaria))

print()
print("NOTA: el registro solo tiene lo que las sesiones VIVAS tocaron hoy, asi")
print("que los commits viejos salen todos sin registro. Lo que importa es el")
print("comportamiento en los commits de esta sesion.")
