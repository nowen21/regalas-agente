# -*- coding: utf-8 -*-
"""Escribe el acuerdo 3 y las secciones de cierre del análisis 1 del pendiente 129.

Reemplaza desde «Siguen abiertas» hasta el final; la conversación, que escribe el
enganche, queda donde está.
"""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
ANALISIS = glob.glob(os.path.join(RAIZ, "documentacion/epicas/EP-005*/HU-002*/pendientes/129-*/analisis-1.md"))[0]
R = "../../../../../.."

texto = open(ANALISIS, encoding="utf-8").read()
turnos = re.findall(r"^### (\d+) · Usuario", texto, flags=re.M)
cierre = open(os.path.join(os.path.dirname(__file__), "analisis_129_cierre.txt"), encoding="utf-8").read()
cierre = cierre.replace("{R}", R).replace("{T1}", str(int(turnos[-1]) - 1)).replace("{T2}", turnos[-1])
corte = texto.index("\nSiguen abiertas: dónde va la HU.")
open(ANALISIS, "w", encoding="utf-8").write(texto[:corte] + cierre)
print("listo")
