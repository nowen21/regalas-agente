# -*- coding: utf-8 -*-
"""De las 15 historias que «no dicen si cumplen», cuantas si lo dicen.

Mide que pasaria si el encabezado aceptado fuera `## N. Veredicto…` en vez de
exigir literalmente «Veredicto de la fase». NO toca nada: solo cuenta.
"""
import os
import re
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import fases as F

# El patron de hoy exige «Veredicto de la fase». Este acepta cualquier
# encabezado cuyo titulo empiece por «Veredicto».
ANCHO = re.compile(
    r"^#{2,3}\s+[\d.]*\s*Veredicto[^\n]*\n+\**(No cumple|Cumple)",
    re.MULTILINE | re.IGNORECASE)


def veredicto_ancho(ruta_fase):
    f = os.path.join(ruta_fase, "resultado_pruebas.md")
    if not os.path.isfile(f):
        return None
    import io
    texto = io.open(f, encoding="utf-8", errors="replace").read()
    dice = F._VEREDICTO.search(texto) or ANCHO.search(texto)
    if not dice:
        return None
    return next(g for g in dice.groups() if g).strip().capitalize()


raiz = os.path.join(RAIZ, *F.CARPETA.split("/"))
antes = {"cumplen": 0, "no": 0, "mudas": 0}
despues = {"cumplen": 0, "no": 0, "mudas": 0}
recuperadas = []

for ep in F._subcarpetas(raiz):
    if not F._EPICA.match(ep):
        continue
    rep = os.path.join(raiz, ep)
    for hu in F._subcarpetas(rep):
        if not F._HU.match(hu):
            continue
        rhu = os.path.join(rep, hu)
        fs = [n for n in F._subcarpetas(rhu) if F._FASE.match(n)]
        if not (fs and all(
                all(os.path.isfile(os.path.join(rhu, f, d))
                    for d in F.DOCUMENTOS) for f in fs)):
            continue

        def reparto(lector, caja):
            dichos = [lector(os.path.join(rhu, f)) for f in fs]
            if any(v is None for v in dichos):
                caja["mudas"] += 1
                return "mudas"
            if any(v == "No cumple" for v in dichos):
                caja["no"] += 1
                return "no"
            caja["cumplen"] += 1
            return "cumplen"

        a = reparto(F.veredicto_de, antes)
        d = reparto(veredicto_ancho, despues)
        if a == "mudas" and d != "mudas":
            recuperadas.append((ep, hu, d))

print("HOY:     %(cumplen)d cumplen, %(no)d no cumplen, %(mudas)d no dicen" % antes)
print("ANCHO:   %(cumplen)d cumplen, %(no)d no cumplen, %(mudas)d no dicen" % despues)
print()
print("SE RECUPERAN %d historias:" % len(recuperadas))
for ep, hu, d in sorted(recuperadas):
    print("   [%s] %s / %s" % (d, ep.split("-")[0] + "-" + ep.split("-")[1], hu))
