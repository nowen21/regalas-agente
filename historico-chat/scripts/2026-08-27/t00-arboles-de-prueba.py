# -*- coding: utf-8 -*-
"""T-00 de la fase A de la HU-022, ANTES de tocar codigo.

Once pruebas arman arboles con los cinco documentos de mentira. Si el cuerpo
falso de alguno se parece a una plantilla, la comprobacion nueva lo señalaria y
romperian once pruebas por algo que no es un defecto.

Esto busca los cuerpos que `pruebas.py` escribe en documentos de fase y les
cuenta cuantos marcadores de plantilla tienen.
"""
import io
import os
import re
from collections import Counter

RAIZ = r"c:\Ing. Jose\ia\agente"
MOLDES = os.path.join(RAIZ, "plantillas", "ciclo-vida-proyectos")
PRUEBAS = os.path.join(RAIZ, "validadores", "pruebas.py")

MARCADOR = re.compile(u"\u00ab[^\u00bb\n]{0,120}\u00bb|AAAA-MM-DD")

# Todos los marcadores que aparecen en cualquiera de las cinco plantillas.
todos = set()
for nombre in ("07-plan-trabajo.md", "08-plan-pruebas.md",
               "09-resultado-pruebas.md", "10-estado-fase.md",
               "11-funcionalidad-implementada.md"):
    ruta = os.path.join(MOLDES, nombre)
    if os.path.isfile(ruta):
        todos |= set(m.strip() for m in MARCADOR.findall(
            io.open(ruta, encoding="utf-8", errors="replace").read()))
    else:
        print("AVISO: falta la plantilla %s" % nombre)

print("Marcadores distintos en las cinco plantillas: %d" % len(todos))
print()

texto = io.open(PRUEBAS, encoding="utf-8", errors="replace").read()

# Todo lo que en pruebas.py se escribe como cuerpo de un documento: cualquier
# literal de cadena. Se mira el archivo entero, que es lo conservador.
literales = re.findall(r'"""(.*?)"""|"([^"\n]{0,4000})"|\'([^\'\n]{0,4000})\'',
                       texto, re.DOTALL)
planos = [x for tri in literales for x in tri if x]

reparto = Counter()
peores = []
for lit in planos:
    suyos = set(m.strip() for m in MARCADOR.findall(lit))
    n = len(suyos & todos)
    reparto[n] += 1
    if n >= 3:
        peores.append((n, lit[:160].replace("\n", " ")))

print("Literales de pruebas.py mirados: %d" % len(planos))
print()
for n in sorted(reparto):
    print("  con %d marcadores de plantilla: %d" % (n, reparto[n]))
print()
if peores:
    print("!! LITERALES CON TRES O MAS (habria que parar y replantear):")
    for n, muestra in sorted(peores, reverse=True):
        print("  %2d  %s" % (n, muestra))
else:
    print("NINGUN literal de pruebas.py llega a tres marcadores de plantilla.")
    print("La comprobacion nueva no toca los arboles de mentira. Se puede seguir.")
