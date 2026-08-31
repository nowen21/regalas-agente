# -*- coding: utf-8 -*-
"""Lista las historias sin veredicto y las sin terminar, con lo que les falta.

Se corre antes de tocar nada: es lo que dice si cada una es trabajo, es una
decision del usuario, o solo falta declararla.
"""
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import fases as F                                            # noqa: E402

raiz = os.path.join(RAIZ, *F.CARPETA.split("/"))
marcadores = F.marcadores_de_los_moldes(RAIZ)

sin_veredicto, no_terminadas, cumplen = [], [], 0

for ep in sorted(F._subcarpetas(raiz)):
    if not F._EPICA.match(ep):
        continue
    rep = os.path.join(raiz, ep)
    for hu in sorted(F._subcarpetas(rep)):
        if not F._HU.match(hu):
            continue
        ruta_hu = os.path.join(rep, hu)
        fs = [f for f in sorted(F._subcarpetas(ruta_hu)) if F._FASE.match(f)]
        if not fs:
            no_terminadas.append((ep, hu, "sin ninguna fase"))
            continue
        if not F._historia_terminada(ruta_hu, marcadores):
            no_terminadas.append((ep, hu, "%d fase(s), a medias" % len(fs)))
            continue
        dejados = F.veredictos_reemplazados(ruta_hu, fs)
        dichos = [(f, F.veredicto_de(os.path.join(ruta_hu, f)))
                  for f in fs if f not in dejados]
        mudas = [f for f, v in dichos if v is None]
        if mudas:
            sin_veredicto.append((ep, hu, ", ".join(m[:44] for m in mudas)))
        elif not any(v == "No cumple" for _, v in dichos):
            cumplen += 1

print("HISTORIAS TERMINADAS QUE NO DICEN SI CUMPLEN: %d\n" % len(sin_veredicto))
for ep, hu, detalle in sin_veredicto:
    print("  %s" % hu)
    print("      en %s" % ep)
    print("      fase sin veredicto: %s\n" % detalle)

print("HISTORIAS SIN TERMINAR: %d\n" % len(no_terminadas))
for ep, hu, detalle in no_terminadas:
    print("  %-52s %s" % (hu[:52], detalle[:100]))

print("\ncumplen: %d" % cumplen)
