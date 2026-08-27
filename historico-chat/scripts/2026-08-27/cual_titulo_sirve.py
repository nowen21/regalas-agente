# -*- coding: utf-8 -*-
"""Cual de los titulos que empiezan por «Veredicto» es el de la FASE.

Importa porque «Veredicto por criterio de aceptacion» aparece 70 veces y NO es
el veredicto de la fase: es la tabla criterio por criterio. Aceptar cualquier
titulo que empiece por «Veredicto» seria volver a leer el primer criterio como
si fuera el veredicto de la fase — la mentira optimista que la fase B evito.
"""
import io
import os
import re
from collections import Counter

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")

CABEZA = re.compile(r"^#+\s*[\d.]*\s*(Veredicto[^\n]*)$", re.MULTILINE | re.IGNORECASE)

seguidos_de_palabra = Counter()
seguidos_de_tabla = Counter()

for ep in sorted(os.listdir(EPICAS)):
    rep = os.path.join(EPICAS, ep)
    if not os.path.isdir(rep):
        continue
    for hu in sorted(os.listdir(rep)):
        rhu = os.path.join(rep, hu)
        if not os.path.isdir(rhu):
            continue
        for fase in sorted(os.listdir(rhu)):
            f = os.path.join(rhu, fase, "resultado_pruebas.md")
            if not os.path.isfile(f):
                continue
            texto = io.open(f, encoding="utf-8", errors="replace").read()
            for m in CABEZA.finditer(texto):
                titulo = m.group(1).strip().rstrip(".")
                if titulo.lower().startswith("veredicto de la fase"):
                    continue
                resto = texto[m.end():].lstrip("\n")
                primera = resto.split("\n", 1)[0]
                if re.match(r"\**(No cumple|Cumple)", primera, re.I):
                    seguidos_de_palabra[titulo] += 1
                else:
                    seguidos_de_tabla[titulo] += 1

print("TITULOS SEGUIDOS DE LA PALABRA SUELTA (los que hay que leer):")
for t, n in seguidos_de_palabra.most_common():
    print("  %4d  %s" % (n, t))
print()
print("TITULOS SEGUIDOS DE OTRA COSA (los que NO hay que leer):")
for t, n in seguidos_de_tabla.most_common():
    print("  %4d  %s" % (n, t))
