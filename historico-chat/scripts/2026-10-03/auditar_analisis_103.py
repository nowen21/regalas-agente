# -*- coding: utf-8 -*-
"""Revisa, solo leyendo, cada fila de «Lo que se tiene que hacer» de los análisis del
pendiente 103: si se hizo de una, o si un CA de su HU la cita."""
import glob
import io
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import pendientes  # noqa: E402

P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
E = os.path.dirname(os.path.dirname(P))
HUS = {int(re.search(r"HU-0*(\d+)", os.path.basename(h)).group(1)): io.open(h, encoding="utf-8").read()
       for h in glob.glob(os.path.join(E, "HU-*", "HU-*.md"))}
CITA = re.compile(r"análisis (\d+),? (?:puntos?|acuerdos?|filas?) ([\d ,ya]+)", re.I)


def cubre(texto, n, m):
    for a, ps in CITA.findall(texto):
        if int(a) != n:
            continue
        nums = set(int(x) for x in re.findall(r"\d+", ps))
        for x, y in re.findall(r"(\d+) a (\d+)", ps):
            nums |= set(range(int(x), int(y) + 1))
        if nums & m:
            return True
    return False


total = {"de una": 0, "HU con CA que la cita": 0, "HU sin CA que la cite": 0, "otro destino": 0}
faltas = []
for a in pendientes.analisis_de(P):
    n = int(re.search(r"analisis-(\d+)", a).group(1))
    t = io.open(a, encoding="utf-8").read()
    aprobado = bool(pendientes._APROBADO.search(t))
    m = re.search(r"^## Lo que se tiene que hacer.*$", t, re.M)
    if not m:
        print("análisis %d: sin «Lo que se tiene que hacer» (aprobado: %s)" % (n, aprobado))
        continue
    fin = re.search(r"^## ", t[m.end():], re.M)
    s = t[m.end():m.end() + fin.start()] if fin else t[m.end():]
    marcas = ""
    filas = list(pendientes._FILA.finditer(s))
    for f in filas:
        num = int(re.match(r"^\| *(\d+)", f.group(0)).group(1))
        destino = f.group(0).strip().rstrip("|").split("|")[-1].strip()
        if re.search(r"(?i)este análisis", destino):
            total["de una"] += 1
            marcas += "u"
            continue
        hu = re.search(r"HU[- ]0*(\d+)", destino)
        if hu:
            h = int(hu.group(1))
            celdas = [c.strip() for c in f.group(0).strip().strip("|").split("|")]
            sale = set(int(x) for x in re.findall(r"\d+", celdas[2])) if len(celdas) > 3 else set()
            if cubre(HUS.get(h, ""), n, {num} | sale):
                total["HU con CA que la cita"] += 1
                marcas += "c"
            else:
                total["HU sin CA que la cite"] += 1
                marcas += "X"
                faltas.append("análisis %d, fila %d: la HU-%03d no tiene un CA que cite «análisis %d, punto %d»" % (n, num, h, n, num))
        else:
            total["otro destino"] += 1
            marcas += "?"
            faltas.append("análisis %d, fila %d: destino «%s»" % (n, num, destino[:90]))
    print("análisis %2d: aprobado %s, %2d filas  %s" % (n, "sí" if aprobado else "no", len(filas), marcas))
print(total)
for x in faltas:
    print(" -", x)
