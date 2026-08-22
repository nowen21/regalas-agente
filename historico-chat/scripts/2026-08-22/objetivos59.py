# -*- coding: utf-8 -*-
"""El objetivo de cada fase detenida, en una línea, para decidir qué falta."""
import io, os, re, glob
os.chdir(r"c:\Ing. Jose\ia\agente")

for est in sorted(glob.glob("documentacion/epicas/**/estado-fase.md", recursive=True)):
    s = io.open(est, encoding="utf-8").read()
    m = re.search(r"\*\*Hechas:\*\*\s*(\d+)\s*de\s*(\d+)", s)
    if not (m and m.group(1) == "0"):
        continue
    carpeta = os.path.dirname(est)
    fase = os.path.basename(carpeta)
    plan = os.path.join(carpeta, "plan_trabajo.md")
    obj = ""
    if os.path.isfile(plan):
        t = io.open(plan, encoding="utf-8").read()
        mo = re.search(r"\*\*Objetivo[.:*]*\*{0,2}\s*(.+?)(?:\n\n|\n\*\*)", t, re.S)
        if not mo:
            mo = re.search(r"##\s*1\.\s*Objetivo[^\n]*\n+(.+?)(?:\n\n)", t, re.S)
        obj = re.sub(r"\s+", " ", mo.group(1)).strip()[:210] if mo else "(sin objetivo escrito)"
    print("### %s\n    %s" % (fase, obj))
