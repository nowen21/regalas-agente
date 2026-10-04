# -*- coding: utf-8 -*-
"""Comprueba en scilit y matematica, sin escribir en ellos, que las tres causas
del análisis 1 del pendiente 110 quedaron corregidas."""
import glob
import os
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import andamio      # noqa: E402
import autorizado   # noqa: E402
import instalar     # noqa: E402

PROYECTOS = [r"C:\DesarrollosClaude\personales\scilit", r"C:\wamp64\www\proyectos\personales\matematica"]
for p in PROYECTOS:
    print("==", os.path.basename(p))
    # Causa 1: el andamio encuentra sus plantillas desde el proyecto (simulado)
    epicas = sorted(glob.glob(os.path.join(p, "documentacion", "epicas", "EP-*")))
    if epicas:
        try:
            andamio.crear_hu(p, os.path.basename(epicas[0]), "prueba-simulada", escribir=False)
            print("  andamio: crea la HU sin error (simulado)")
        except Exception as e:      # noqa: BLE001
            print("  andamio: FALLA", e)
    else:
        print("  andamio: sin épicas para simular")
    # Causa 1: stack.md se repararía
    stack = os.path.join(p, ".agente", "stack.md")
    pasos = instalar._reparar_marcadores(stack, p, False, ".agente/stack.md")
    print("  stack.md:", pasos[0] if pasos else "sin nada que reparar")
    # Causa 2: lo que escribe el instalador queda autorizado
    versiones = glob.glob(os.path.join(p, "documentacion", "versiones", "*.md"))
    rels = [os.path.relpath(v, p).replace("\\", "/") for v in versiones]
    sin = [r for r in rels if not autorizado.quien_autoriza(r, [autorizado.HERRAMIENTAS])]
    print("  documentacion/versiones:", len(rels), "archivos;", "todos autorizados" if not sin else "sin autorizar: %s" % sin)
