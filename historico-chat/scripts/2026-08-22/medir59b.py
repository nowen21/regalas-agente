# -*- coding: utf-8 -*-
"""Para cada fase detenida: qué prueba nombra su plan y si ese archivo existe."""
import io, os, re, glob
os.chdir(r"c:\Ing. Jose\ia\agente")

detenidas = []
for est in sorted(glob.glob("documentacion/epicas/**/estado-fase.md", recursive=True)):
    s = io.open(est, encoding="utf-8").read()
    m = re.search(r"\*\*Hechas:\*\*\s*(\d+)\s*de\s*(\d+)", s)
    if not (m and m.group(1) == "0"):
        continue
    carpeta = os.path.dirname(est).replace("\\", "/")
    fase = os.path.basename(carpeta)
    textos = ""
    for f in ("plan_trabajo.md", "plan_pruebas.md"):
        p = os.path.join(carpeta, f)
        if os.path.isfile(p):
            textos += io.open(p, encoding="utf-8").read()
    tests = sorted(set(re.findall(r"(test_[\w]+\.py)", textos)))
    subs = sorted(set(re.findall(r"validar\.py\s+([a-z_\-]+)", textos)))
    mods = sorted(set(re.findall(r"validadores/([\w]+\.py)", textos)))
    estado = []
    for t in tests:
        estado.append(("OK " if os.path.exists("validadores/tests/" + t) else "NO ") + t)
    print("### %s" % fase)
    print("   pruebas: %s" % ("; ".join(estado) if estado else "(ninguna nombrada)"))
    if subs:
        print("   subcomandos: %s" % ", ".join(subs))
    detenidas.append(fase)
print("\ntotal detenidas:", len(detenidas))
