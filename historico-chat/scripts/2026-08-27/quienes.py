# -*- coding: utf-8 -*-
"""Dice CUALES son, no solo cuantas. El validador da tres numeros."""
import os
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import fases as F

raiz = os.path.join(RAIZ, *F.CARPETA.split("/"))
cumplen, no_cumplen, sin_veredicto = [], [], []

for nombre_epica in F._subcarpetas(raiz):
    ruta_epica = os.path.join(raiz, nombre_epica)
    if not F._EPICA.match(nombre_epica):
        continue
    for nombre_hu in F._subcarpetas(ruta_epica):
        if not F._HU.match(nombre_hu):
            continue
        ruta_hu = os.path.join(ruta_epica, nombre_hu)
        fs = [n for n in F._subcarpetas(ruta_hu) if F._FASE.match(n)]
        if not (fs and all(
                all(os.path.isfile(os.path.join(ruta_hu, f, d))
                    for d in F.DOCUMENTOS)
                for f in fs)):
            continue
        dichos = [(f, F.veredicto_de(os.path.join(ruta_hu, f))) for f in fs]
        etiqueta = "%s / %s" % (nombre_epica.split("-")[0] + "-" + nombre_epica.split("-")[1],
                                nombre_hu)
        if any(v is None for _, v in dichos):
            mudas = [f for f, v in dichos if v is None]
            sin_veredicto.append((etiqueta, mudas))
        elif any(v == "No cumple" for _, v in dichos):
            rojas = [f for f, v in dichos if v == "No cumple"]
            no_cumplen.append((etiqueta, rojas))
        else:
            cumplen.append((etiqueta, []))

print("CUMPLEN: %d" % len(cumplen))
print()
print("NO CUMPLEN (%d) -- con la fase que lo dice:" % len(no_cumplen))
for e, fs in sorted(no_cumplen):
    print("  %s" % e)
    for f in fs:
        print("       %s" % f)
print()
print("NO DICEN (%d) -- con la fase muda:" % len(sin_veredicto))
for e, fs in sorted(sin_veredicto):
    print("  %s" % e)
    for f in fs:
        print("       %s" % f)
