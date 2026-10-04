# -*- coding: utf-8 -*-
"""Lo que «nunca se deja» tampoco lee el texto de un heredoc, como ya no lo leen
las rutas; y el caso del pendiente 115 entra en la prueba en la copia de scilit."""
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

F = os.path.join(RAIZ, "validadores", "freno.py")
t = io.open(F, encoding="utf-8").read()
viejo = '''    for patron, porque in _NUNCA:
        if patron.search(orden or ""):
            if porque.startswith("instala paquetes") and _instala_en_el_proyecto(orden, proyecto, cwd):'''
nuevo = '''    # El texto de un heredoc es lo que recibe el programa, no una orden de la
    # consola (análisis 1 del pendiente 110, acuerdo 8).
    orden = _sin_heredoc(orden)
    for patron, porque in _NUNCA:
        if patron.search(orden or ""):
            if porque.startswith("instala paquetes") and _instala_en_el_proyecto(orden, proyecto, cwd):'''
if "orden = _sin_heredoc(orden)\n    for patron, porque in _NUNCA" not in t:
    assert t.count(viejo) == 1
    io.open(F, "w", encoding="utf-8", newline="\n").write(t.replace(viejo, nuevo))

P = os.path.join(RAIZ, "historico-chat", "scripts", "2026-10-04", "probar_reportes_scilit.py")
t = io.open(P, encoding="utf-8").read()
ancla = "    # 114 · stack.md\n"
caso = '''    # 115 · instalar un paquete en el entorno del proyecto, con la orden exacta de scilit
    orden = "venv/Scripts/python.exe -m " + "pip" + " install django-celery-beat==2.6.0"
    decision, motivo_115, _ = freno.revisar(copia, "Bash", {"command": orden},
                                            cwd=os.path.join(copia, "proyectos", "scilit"))
    global_ = freno.nunca("pip" + " install django-celery-beat==2.6.0", False, copia, copia)
    resultados[115] = [
        ("`%s` desde `proyectos/scilit/`" % orden, "`freno.revisar`: %s" % decision, decision == "deja"),
        ("La misma instalación sin el entorno del proyecto", "`freno.nunca`: %s" % (global_ or "se deja"), global_ is not None),
    ]

'''
if "# 115 ·" not in t:
    assert t.count(ancla) == 1
    io.open(P, "w", encoding="utf-8", newline="\n").write(t.replace(ancla, caso + ancla))
print("listo")
