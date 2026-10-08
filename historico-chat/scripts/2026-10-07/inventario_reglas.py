# -*- coding: utf-8 -*-
"""EP-027 · Inventario de cómo están escritas las reglas en la base: qué partes
del molde trae cada una y qué texto queda por fuera de las casillas.

Se corre desde proyectos/cimiento:
    .venv/Scripts/python.exe manage.py shell < ../../historico-chat/scripts/2026-10-07/inventario_reglas.py
"""
import re
from collections import Counter

from core.estandar.models import Documento

REGLA = re.compile(r"^## ([A-Z]+\d+(?:\.\d+)?) · (.+)$")
CERCA = re.compile(r"^\s*(```|~~~)")

reglas = []
for d in Documento.objects.filter(ruta__startswith="base/").exclude(ruta__startswith="base/reglas-por-tarea/"):
    lineas = d.contenido.replace("\r\n", "\n").split("\n")
    dentro, inicio = False, None
    cortes = []
    for i, l in enumerate(lineas):
        if CERCA.match(l):
            dentro = not dentro
        if not dentro and REGLA.match(l):
            cortes.append(i)
    for n, c in enumerate(cortes):
        fin = cortes[n + 1] if n + 1 < len(cortes) else len(lineas)
        # Un documento de capítulo cierra la última regla en el siguiente "## " que no es regla.
        for j in range(c + 1, fin):
            if lineas[j].startswith("## ") and not REGLA.match(lineas[j]):
                fin = j
                break
        reglas.append((d.ruta, lineas[c:fin]))

print("reglas:", len(reglas))
partes = Counter()
sobrantes = Counter()
ejemplos_sobra = {}
for ruta, bloque in reglas:
    codigo = REGLA.match(bloque[0]).group(1)
    tipos = []
    dentro = False
    cuerpo_vacio = True
    estado = "cuerpo"
    for l in bloque[1:]:
        if CERCA.match(l):
            dentro = not dentro
            if dentro:
                tipos.append("codigo")
            continue
        if dentro or not l.strip():
            continue
        if l.startswith("### Checklist"):
            estado = "sello"
            tipos.append("sello")
            continue
        if estado == "sello":
            continue
        if l.startswith("**Excepción"):
            tipos.append("excepcion")
        elif l.startswith("**Aplica a:**"):
            tipos.append("aplica")
        elif l.startswith("**Autoriza escribir:**"):
            tipos.append("autoriza")
        elif l.startswith(("**Quién la hace cumplir:**", "**Nadie la hace cumplir:**")):
            tipos.append("cumplir")
        elif l.strip() == "---":
            tipos.append("raya")
        elif l.startswith("> Regla del capítulo"):
            tipos.append("cita_capitulo")
        else:
            tipos.append("texto:" + ("cita" if l.startswith(">") else "tabla" if l.startswith("|")
                                     else "lista" if re.match(r"^\s*([-*]|\d+\.)\s", l)
                                     else "titulo" if l.startswith("#") else "parrafo"))
    # contar los párrafos de texto: el primero es el cuerpo
    textos = [t for t in tipos if t.startswith("texto:")]
    for t in set(tipos):
        partes[t] += 1
    extra = [t for t in tipos if t.startswith("texto:")]
    # el cuerpo son los textos antes del primer elemento no-texto
    primeros = []
    for t in tipos:
        if t.startswith("texto:parrafo") and not any(x for x in primeros if not x.startswith("texto")):
            primeros.append(t)
        else:
            primeros.append(t)
    clave = tuple(t for t in tipos if t not in ("raya",))
    sobrantes[clave] += 1
    ejemplos_sobra.setdefault(clave, codigo)

print("\nPartes, en cuántas reglas aparecen:")
for k, v in partes.most_common():
    print("  %-22s %d" % (k, v))
print("\nFormas distintas (secuencia de partes):", len(sobrantes))
for k, v in sobrantes.most_common(25):
    print("  %3d  %-8s %s" % (v, ejemplos_sobra[k], " ".join(k)))
