# -*- coding: utf-8 -*-
"""Llena las partes del análisis 1 del pendiente 124 que no dependen de acuerdos.

Deja intacta la sección «Conversación», que escribe el enganche.
"""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CARPETA = glob.glob(os.path.join(RAIZ, "historico-chat/resumenes/2026-10-05/pendientes/124-*"))[0]
ANALISIS = os.path.join(CARPETA, "analisis-1.md")
R = "../../../../.."

texto = open(ANALISIS, encoding="utf-8").read()
conversacion = texto[texto.index("## Conversación"):texto.index("## Lo acordado")]

pendiente = open(os.path.join(CARPETA, "pendiente.md"), encoding="utf-8").read()
pendiente = pendiente.replace("../../sesion-2.md", R + "/historico-chat/resumenes/2026-10-05/sesion-2.md")
pendiente = pendiente.replace("../../../../../proyectos", R + "/proyectos")
pendiente = "\n".join("#" + l if l.startswith("#") else l for l in pendiente.strip().splitlines())

CABEZA = open(os.path.join(os.path.dirname(__file__), "analisis_124_cabeza.txt"), encoding="utf-8").read()
COLA = open(os.path.join(os.path.dirname(__file__), "analisis_124_cola.txt"), encoding="utf-8").read()

nuevo = CABEZA.replace("{R}", R) + pendiente + "\n\n---\n\n" + conversacion + COLA.replace("{R}", R)
open(ANALISIS, "w", encoding="utf-8").write(nuevo)
print("listo:", os.path.relpath(ANALISIS, RAIZ))
