# -*- coding: utf-8 -*-
"""EP-027 · Lee cada regla de la base en casillas y la vuelve a armar: dice cuáles
no dan el mismo texto y en qué difieren.

    .venv/Scripts/python.exe manage.py shell -c "exec(open('../../historico-chat/scripts/2026-10-07/ida_y_vuelta.py',encoding='utf-8').read())"
"""
import difflib
import re
from collections import Counter

from core.estandar import molde
from core.estandar.models import Documento


def plano(t):
    return re.sub(r"\n{3,}", "\n\n", t.replace("\r\n", "\n")).strip()


total, iguales, distintas, codigos = 0, 0, [], Counter()
for d in Documento.objects.filter(ruta__startswith="base/").exclude(ruta__startswith="base/reglas-por-tarea/"):
    texto = d.contenido.replace("\r\n", "\n")
    for inicio, fin, codigo in molde.partir(texto):
        total += 1
        codigos[codigo] += 1
        bloque = texto[inicio:fin]
        armado = molde.normalizar(bloque)
        if plano(armado) == plano(bloque):
            iguales += 1
        else:
            distintas.append((codigo, d.ruta, bloque, armado))

print("reglas:", total, "· iguales:", iguales, "· distintas:", len(distintas))
print("códigos repetidos:", [(c, n) for c, n in codigos.items() if n > 1])
sin_blancos = [x for x in distintas if [l for l in plano(x[2]).split("\n") if l.strip()]
               != [l for l in plano(x[3]).split("\n") if l.strip()]]
print("difieren en algo más que renglones en blanco:", [x[0] for x in sin_blancos])
for codigo, ruta, bloque, armado in sin_blancos[:12]:
    print("=====", codigo, ruta)
    for l in difflib.unified_diff(plano(bloque).split("\n"), plano(armado).split("\n"), lineterm="", n=0):
        if not l.startswith(("---", "+++")):
            print("   ", l[:150])
