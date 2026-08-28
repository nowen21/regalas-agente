# -*- coding: utf-8 -*-
"""Segundo intento: contar marcadores NO sirve. Se compara contra el molde.

El primer intento conto los `«...»` y `AAAA-MM-DD` de cada documento y llamo
«molde sin llenar» a los que pasaran de diez. **Da falsos positivos**: tres
documentos de la fase C de la HU-021 —escritos, cerrados y publicados el mismo
dia— salieron con 11, 12 y 13, porque este repositorio usa comillas angulares
en prosa todo el tiempo: «Cumple», «No cumple», «por criterio de aceptacion».

La medida buena no es cuantos marcadores hay, sino **cuantos de ellos siguen
siendo los del molde**. `«Cumple»` es prosa; `«2-4 lineas en lenguaje claro»`
es el formulario sin llenar. La diferencia se sabe leyendo la plantilla.
"""
import io
import os
import re
from collections import Counter

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")
MOLDES = os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos")

# Que plantilla corresponde a cada documento de fase.
DE_QUE_MOLDE = {
    "plan_trabajo.md": "07-plan-trabajo.md",
    "plan_pruebas.md": "08-plan-pruebas.md",
    "resultado_pruebas.md": "09-resultado-pruebas.md",
    "funcionalidad_implementada.md": "11-funcionalidad-implementada.md",
    "estado-fase.md": "10-estado-fase.md",
}

MARCADOR = re.compile(u"\u00ab[^\u00bb\n]{0,120}\u00bb|AAAA-MM-DD")


def marcadores(texto):
    return set(m.strip() for m in MARCADOR.findall(texto))


del_molde = {}
for doc, molde in DE_QUE_MOLDE.items():
    if True:
        ruta = os.path.join(MOLDES, molde)
        if os.path.isfile(ruta):
            del_molde[doc] = marcadores(
                io.open(ruta, encoding="utf-8", errors="replace").read())
        else:
            print("AVISO: no existe la plantilla %s" % molde)
            del_molde[doc] = set()

reparto = Counter()
sospechosos = []
total = 0

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
            if not os.path.isdir(rf):
                continue
            for doc, propios in del_molde.items():
                f = os.path.join(rf, doc)
                if not os.path.isfile(f):
                    continue
                total += 1
                suyos = marcadores(io.open(f, encoding="utf-8",
                                           errors="replace").read())
                quedan = suyos & propios
                if not quedan:
                    reparto["ninguno del molde"] += 1
                elif len(quedan) <= 2:
                    reparto["1 o 2 del molde"] += 1
                else:
                    reparto["3 o mas del molde"] += 1
                    sospechosos.append((len(quedan), fase, doc,
                                        sorted(quedan)[:3]))

print("Documentos comparables mirados: %d" % total)
print()
for clave in ("ninguno del molde", "1 o 2 del molde", "3 o mas del molde"):
    print("  %-24s %d" % (clave, reparto[clave]))
print()
print("SIGUEN SIENDO EL MOLDE (%d):" % len(sospechosos))
for n, fase, doc, ejemplos in sorted(sospechosos, reverse=True):
    print("  %3d  %s / %s" % (n, fase, doc))
    print("       ej: %s" % " | ".join(ejemplos))
