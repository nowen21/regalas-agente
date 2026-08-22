# -*- coding: utf-8 -*-
"""De las fases detenidas: ¿cuáles ya tienen resultado y cierre escritos?"""
import io, os, re, glob
os.chdir(r"c:\Ing. Jose\ia\agente")

MARCA = "\u00ab\u2026\u00bb"
filas = []
for est in sorted(glob.glob("documentacion/epicas/**/estado-fase.md", recursive=True)):
    s = io.open(est, encoding="utf-8").read()
    m = re.search(r"\*\*Hechas:\*\*\s*(\d+)\s*de\s*(\d+)", s)
    if not (m and m.group(1) == "0"):
        continue
    c = os.path.dirname(est)
    fase = os.path.basename(c)

    def estado(nombre):
        p = os.path.join(c, nombre)
        if not os.path.isfile(p):
            return "falta"
        t = io.open(p, encoding="utf-8").read()
        if MARCA in t:
            return "con huecos (%d)" % t.count(MARCA)
        return "escrito"

    res, fun = estado("resultado_pruebas.md"), estado("funcionalidad_implementada.md")
    veredicto = ""
    p = os.path.join(c, "resultado_pruebas.md")
    if os.path.isfile(p):
        t = io.open(p, encoding="utf-8").read()
        mv = re.search(r"(No cumple|Cumple con reservas|Cumple)", t)
        veredicto = mv.group(1) if mv else "sin veredicto"
    filas.append((fase, res, fun, veredicto))

print("fase | resultado_pruebas | funcionalidad | veredicto")
for f in filas:
    print("%-56s %-18s %-18s %s" % (f[0][:56], f[1], f[2], f[3]))
print("\ntotal:", len(filas))
listas = [f for f in filas if f[1] == "escrito" and f[2] == "escrito"]
print("con los dos escritos:", len(listas))
