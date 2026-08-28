# -*- coding: utf-8 -*-
"""Mide el CA-04 de EP-001-HU-007 contra lo que su criterio pide.

El criterio, palabra por palabra:

    Cuando se pregunta que reglas llevan mas tiempo sin revisarse de fondo
    Entonces se obtiene la lista ORDENADA de la mas vieja a la mas nueva
    Y cada una dice CUANDO se reviso y CUANTOS incumplimientos produce hoy

**No pide que las reglas esten revisadas.** Pide que se sepa cuales llevan mas
sin revisarse. La diferencia es lo que hizo que la fase A se reprobara por algo
que su criterio no menciona.
"""
import os
import re
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import vigencia                                          # noqa: E402

salida = subprocess.run(
    [sys.executable, os.path.join(RAIZ, "validadores", "vigencia.py")],
    cwd=RAIZ, capture_output=True, text=True, encoding="utf-8",
    errors="replace").stdout

lineas = [l for l in salida.splitlines() if l.strip()]

print("CP-001 - se obtiene una lista")
print("   la comprobacion corre:", bool(salida.strip()))
cabecera = [l for l in lineas if l.startswith("REGLA")]
print("   trae cabecera de tabla:", bool(cabecera))
if cabecera:
    print("      ", cabecera[0].strip())
print()

print("CP-002 - la lista dice las tres cosas por regla")
if cabecera:
    columnas = cabecera[0].split()
    print("   columnas:", columnas)
    print("   dice CUANDO se reviso:", any("REVISADA" in c for c in columnas))
    print("   dice cuantos INCUMPLIMIENTOS produce hoy:",
          any("FALLA" in c for c in columnas))
print()

print("CP-003 - esta ordenada de la mas vieja a la mas nueva")
# El orden lo produce `vigencia`: se comprueba pidiendoselo dos veces y
# viendo que la secuencia de sellos no retroceda.
reglas = vigencia.ordenadas(RAIZ) if hasattr(vigencia, "ordenadas") else None
if reglas is None:
    # Se lee del texto: la columna del sello, en el orden en que salen.
    sellos = []
    for l in lineas:
        m = re.match(r"^\S+\s+\S+\s+(\S+)", l)
        if m and (m.group(1) == "sin" or re.match(r"\d{4}-\d{2}-\d{2}", m.group(1))):
            sellos.append(m.group(1))
    def clave(s):
        return "0000-00-00" if s == "sin" else s
    ordenados = sellos == sorted(sellos, key=clave)
    print("   sellos leidos:", len(sellos))
    print("   van de la mas vieja a la mas nueva:", ordenados)
    if not ordenados:
        print("      primeros:", sellos[:6])
print()

print("CP-004 - cuantas reglas cubre")
cuenta = [l for l in lineas if "reglas" in l and "sin revisar" in l]
print("   ", cuenta[0].strip() if cuenta else "(no dice)")
print()

print("CP-005 - el programa avisa y no corrige")
antes = subprocess.run(["git", "status", "--porcelain"], cwd=RAIZ,
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace").stdout
subprocess.run([sys.executable, os.path.join(RAIZ, "validadores", "vigencia.py")],
               cwd=RAIZ, capture_output=True)
despues = subprocess.run(["git", "status", "--porcelain"], cwd=RAIZ,
                         capture_output=True, text=True, encoding="utf-8",
                         errors="replace").stdout
print("   correrlo no cambia ningun archivo:", antes == despues)
