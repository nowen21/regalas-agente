# -*- coding: utf-8 -*-
"""Cuenta TODAS las formas del encabezado de veredicto, no las tres que se supusieron.

La fase B de la HU-021 declaro tres formas y 39 fases «sin encabezado». Al mirar
una de esas 39 aparecio `## 5. Veredicto` — sin «de la fase», que es lo que el
patron exige. Esto mide cuantas hay de cada variante, antes de tocar nada.
"""
import io
import os
import re

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")

_ENCABEZADO = re.compile(r"^#{2,3}\s*[\d.]*\s*([^\n]*veredicto[^\n]*)$",
                         re.MULTILINE | re.IGNORECASE)


def resultados():
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
                if os.path.isfile(f):
                    yield ep, hu, fase, f


formas = {}
sin_ninguno = []
total = 0
for ep, hu, fase, f in resultados():
    total += 1
    texto = io.open(f, encoding="utf-8", errors="replace").read()
    titulos = _ENCABEZADO.findall(texto)
    if not titulos:
        sin_ninguno.append((ep, hu, fase))
        continue
    for t in titulos:
        clave = t.strip().rstrip(".")
        formas.setdefault(clave, []).append((ep, hu, fase))

print("Resultados mirados: %d" % total)
print()
print("ENCABEZADOS QUE MENCIONAN «veredicto» (%d formas distintas):" % len(formas))
for clave in sorted(formas, key=lambda k: -len(formas[k])):
    print("  %4d  %s" % (len(formas[clave]), clave))
print()
print("SIN NINGUN ENCABEZADO DE VEREDICTO: %d" % len(sin_ninguno))
