# -*- coding: utf-8 -*-
"""Cuantas fases tienen su estacion 12 sin marcar, y cuantas SI estan en git.

Linea base del pendiente 87, medida antes de crear nada.
"""
import io
import os
import re
import subprocess

RAIZ = r"c:\Ing. Jose\ia\agente"
EPICAS = os.path.join(RAIZ, "documentacion", "epicas")

FILA_12 = re.compile(r"^\|\s*12\s*\|[^|]*\|[^|]*\|\s*([^|]*?)\s*\|", re.M)

sin_marcar, marcadas, sin_fila = [], [], []
for ep in sorted(os.listdir(EPICAS)):
    rep = os.path.join(EPICAS, ep)
    if not os.path.isdir(rep):
        continue
    for hu in sorted(os.listdir(rep)):
        rhu = os.path.join(rep, hu)
        if not os.path.isdir(rhu):
            continue
        for fase in sorted(os.listdir(rhu)):
            f = os.path.join(rhu, fase, "estado-fase.md")
            if not os.path.isfile(f):
                continue
            t = io.open(f, encoding="utf-8", errors="replace").read()
            m = FILA_12.search(t)
            if not m:
                sin_fila.append(fase)
            elif "✅" in m.group(1) or re.search(r"`[0-9a-f]{7,}`", m.group(1)):
                marcadas.append(fase)
            else:
                # ¿su cierre ya esta en git?
                cierre = os.path.join(rhu, fase, "funcionalidad_implementada.md")
                en_git = False
                if os.path.isfile(cierre):
                    r = subprocess.run(
                        ["git", "log", "--oneline", "-1", "--", cierre],
                        cwd=RAIZ, capture_output=True, text=True,
                        encoding="utf-8", errors="replace")
                    en_git = bool((r.stdout or "").strip())
                sin_marcar.append((fase, en_git))

print("Fases con estado-fase.md: %d"
      % (len(sin_marcar) + len(marcadas) + len(sin_fila)))
print()
print("  estacion 12 MARCADA:            %d" % len(marcadas))
print("  estacion 12 SIN marcar:         %d" % len(sin_marcar))
print("     ...y su cierre YA esta en git: %d  <- son marcas, no trabajo"
      % sum(1 for _, g in sin_marcar if g))
print("     ...y su cierre no esta en git: %d  <- trabajo de verdad"
      % sum(1 for _, g in sin_marcar if not g))
print("  sin fila de estacion 12:        %d" % len(sin_fila))
print()
print("LAS QUE SON SOLO UNA MARCA SIN PONER:")
for fase, en_git in sorted(sin_marcar):
    if en_git:
        print("   %s" % fase)
