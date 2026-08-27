# -*- coding: utf-8 -*-
"""Como esta escrita EXACTAMENTE la linea del encabezado y la que le sigue.

Para no volver a inventar el patron: se mira el texto crudo de los encabezados
que empiezan por «Veredicto» y no son «Veredicto de la fase».
"""
import io
import os
import re
from collections import Counter

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")

CABEZA = re.compile(r"^(#+)(\s*)([\d.]*)(\s*)(Veredicto[^\n]*)$",
                    re.MULTILINE | re.IGNORECASE)

niveles, numeros, siguientes, titulos = Counter(), Counter(), Counter(), Counter()

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
                almohadillas, _, numero, _, titulo = m.groups()
                if titulo.lower().startswith("veredicto de la fase"):
                    continue
                niveles[almohadillas] += 1
                numeros["con numero" if numero else "SIN numero"] += 1
                titulos[titulo.strip()] += 1
                resto = texto[m.end():m.end() + 300].lstrip("\n")
                primera = resto.split("\n", 1)[0][:60]
                clase = ("**Cumple / **No cumple" if re.match(r"\**(No cumple|Cumple)", primera, re.I)
                         else "tabla" if primera.startswith("|")
                         else "otra cosa")
                siguientes[clase] += 1
                if clase == "otra cosa":
                    print("   OTRA: %-28s %s" % (fase[:28], primera))

print()
print("NIVEL:     ", dict(niveles))
print("NUMERO:    ", dict(numeros))
print("QUE SIGUE: ", dict(siguientes))
print()
print("TITULOS:")
for t, n in titulos.most_common():
    print("  %4d  %s" % (n, t))
