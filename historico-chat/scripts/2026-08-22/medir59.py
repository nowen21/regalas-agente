# -*- coding: utf-8 -*-
"""¿Cuáles de las 26 fases detenidas del pendiente 59 siguen sin construirse?"""
import io, os, re, glob
os.chdir(r"c:\Ing. Jose\ia\agente")

filas = []
for est in glob.glob("documentacion/epicas/**/estado-fase.md", recursive=True):
    s = io.open(est, encoding="utf-8").read()
    carpeta = os.path.dirname(est).replace("\\", "/")
    fase = os.path.basename(carpeta)
    m = re.search(r"\*\*Hechas:\*\*\s*(\d+)\s*de\s*(\d+)", s)
    hechas, total = (m.group(1), m.group(2)) if m else ("?", "?")
    detenida = bool(re.search(r"detenid|sin resolver|no arrancó|Nada se ejecutó", s))
    # ¿qué archivos declara tocar el plan?
    plan = os.path.join(carpeta, "plan_trabajo.md")
    tocados = []
    if os.path.isfile(plan):
        p = io.open(plan, encoding="utf-8").read()
        tocados = sorted(set(re.findall(r"`(validadores/[\w/]+\.py|base/[\w\-/]+\.md|plantillas/[\w\-/]+\.md|adaptadores/[\w\-/]+\.py)`", p)))
    existen = [t for t in tocados if os.path.exists(t)]
    if m and hechas == "0" or detenida:
        filas.append((fase, hechas, total, len(existen), len(tocados),
                      "; ".join(t for t in tocados[:4])))

filas.sort()
print("fases con 0 tareas hechas o marcadas detenidas:", len(filas))
for f in filas:
    print("%-58s %s/%s  archivos que ya existen: %d/%d  %s" % (f[0][:58], f[1], f[2], f[3], f[4], f[5][:90]))
