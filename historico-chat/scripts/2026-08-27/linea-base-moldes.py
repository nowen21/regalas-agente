# -*- coding: utf-8 -*-
"""Linea base del pendiente 88, medida ANTES de crear la carpeta de su fase.

Se mide primero porque abrir una fase mueve el numero que la fase va a arreglar:
el andamio crea sus cinco documentos vacios y la historia deja de contar como
terminada. Paso cuatro veces el 2026-08-27.

Cuenta, por documento de fase, cuantos marcadores del molde quedaron sin
reemplazar: `«...»` y `AAAA-MM-DD`. Un documento con treinta no es un documento:
es un formulario.
"""
import io
import os
import re
from collections import Counter

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")
CINCO = ("plan_trabajo.md", "plan_pruebas.md", "resultado_pruebas.md",
         "estado-fase.md", "funcionalidad_implementada.md")

MARCADOR = re.compile(u"\u00ab[^\u00bb\n]{0,120}\u00bb|AAAA-MM-DD")


def fases():
    for ep in sorted(os.listdir(EPICAS)):
        rep = os.path.join(EPICAS, ep)
        if not os.path.isdir(rep):
            continue
        for hu in sorted(os.listdir(rep)):
            rhu = os.path.join(rep, hu)
            if not os.path.isdir(rhu):
                continue
            for fase in sorted(os.listdir(rhu)):
                rf = os.path.join(rhu, fase)
                if os.path.isdir(rf):
                    yield ep, hu, fase, rf


reparto = Counter()
sospechosos = []
total_docs = 0

for ep, hu, fase, rf in fases():
    for doc in CINCO:
        f = os.path.join(rf, doc)
        if not os.path.isfile(f):
            continue
        total_docs += 1
        n = len(MARCADOR.findall(io.open(f, encoding="utf-8",
                                         errors="replace").read()))
        if n == 0:
            reparto["0 (escrito)"] += 1
        elif n <= 4:
            reparto["1 a 4 (prosa con comillas)"] += 1
        elif n <= 9:
            reparto["5 a 9 (a revisar)"] += 1
        else:
            reparto["10 o mas (MOLDE SIN LLENAR)"] += 1
            sospechosos.append((n, ep, hu, fase, doc))

print("Documentos de fase mirados: %d" % total_docs)
print()
for clave in ("0 (escrito)", "1 a 4 (prosa con comillas)",
              "5 a 9 (a revisar)", "10 o mas (MOLDE SIN LLENAR)"):
    print("  %-32s %d" % (clave, reparto[clave]))
print()
print("LOS QUE SIGUEN SIENDO EL MOLDE (%d):" % len(sospechosos))
for n, ep, hu, fase, doc in sorted(sospechosos, reverse=True):
    print("  %3d marcadores  %s / %s" % (n, fase, doc))
