# -*- coding: utf-8 -*-
"""Lo mismo que `cuantas_se_recuperan.py`, con el patron AJUSTADO.

El primero acepto cualquier titulo que empezara por «Veredicto», y eso incluye
«Veredicto por criterio de aceptacion», que aparece 70 veces y NO es el
veredicto de la fase. No fallo por casualidad —esas 70 van seguidas de tabla, no
de la palabra suelta— pero el patron era mas ancho que el hecho.

Ajustado: el titulo tiene que ser exactamente «Veredicto». Medido: de los seis
titulos distintos, ese es el UNICO seguido de la palabra suelta, 15 veces.
"""
import io
import os
import re
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import fases as F

AJUSTADO = re.compile(
    r"^##\s+\d+\.?\s*Veredicto\s*\n+\**(No cumple|Cumple)",
    re.MULTILINE | re.IGNORECASE)


def veredicto_ajustado(ruta_fase):
    f = os.path.join(ruta_fase, "resultado_pruebas.md")
    if not os.path.isfile(f):
        return None
    texto = io.open(f, encoding="utf-8", errors="replace").read()
    dice = (F._VEREDICTO.search(texto)
            or F._VEREDICTO_BAJO_TITULO.search(texto)
            or AJUSTADO.search(texto))
    if not dice:
        return None
    return next(g for g in dice.groups() if g).strip().capitalize()


raiz = os.path.join(RAIZ, *F.CARPETA.split("/"))
antes = {"cumplen": 0, "no": 0, "mudas": 0}
despues = {"cumplen": 0, "no": 0, "mudas": 0}
recuperadas, siguen_mudas = [], []

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
        d = reparto(veredicto_ajustado, despues)
        if a == "mudas" and d != "mudas":
            recuperadas.append((ep, hu, d))
        elif a == "mudas":
            siguen_mudas.append((ep, hu))
        if a != "mudas" and a != d:
            print("  !! CAMBIO UNA QUE NO ERA MUDA: %s / %s  %s -> %s" % (ep, hu, a, d))

print("HOY:       %(cumplen)d cumplen, %(no)d no cumplen, %(mudas)d no dicen" % antes)
print("AJUSTADO:  %(cumplen)d cumplen, %(no)d no cumplen, %(mudas)d no dicen" % despues)
print()
print("SE RECUPERAN %d:" % len(recuperadas))
for ep, hu, d in sorted(recuperadas):
    print("   [%-8s] %s" % (d, hu))
print()
print("SIGUEN MUDAS %d:" % len(siguen_mudas))
for ep, hu in sorted(siguen_mudas):
    print("   %s" % hu)
