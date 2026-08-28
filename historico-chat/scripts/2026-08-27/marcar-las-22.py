# -*- coding: utf-8 -*-
"""Pone la marca del commit a las 22 fases que ya estan cerradas de hecho.

**No inventa el hash: lo lee del historial.** Para cada fase se busca el commit
donde entro su documento de cierre, y ese es el que se anota — el que de verdad
la cerro, no el de hoy.

**Usa el mismo codigo que el enganche** (`estacion_commit.marcar`), asi que
hereda sus tres guardias: no toca una fase sin fila, no pisa un hash puesto, y
no escribe si no hay cambio.

Corre en seco por defecto. Con `--aplicar`, escribe.
"""
import io
import os
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import estacion_commit                                   # noqa: E402
import fases as F                                        # noqa: E402

APLICAR = "--aplicar" in sys.argv


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout


raiz = os.path.join(RAIZ, *F.CARPETA.split("/"))
puestas, sin_commit, saltadas = [], [], []

for ep in F._subcarpetas(raiz):
    if not F._EPICA.match(ep):
        continue
    for hu in F._subcarpetas(os.path.join(raiz, ep)):
        if not F._HU.match(hu):
            continue
        rhu = os.path.join(raiz, ep, hu)
        for fase in F._subcarpetas(rhu):
            if not F._FASE.match(fase):
                continue
            carpeta = os.path.join(rhu, fase)
            estado = os.path.join(carpeta, "estado-fase.md")
            cierre = os.path.join(carpeta, "funcionalidad_implementada.md")
            if not os.path.isfile(estado) or not os.path.isfile(cierre):
                continue
            texto = io.open(estado, encoding="utf-8", errors="replace").read()
            if not estacion_commit.tiene_fila_de_estacion(texto):
                continue
            if estacion_commit.ya_esta_marcada(texto):
                continue

            # El commit donde ENTRO el cierre: el primero que lo toco.
            rel = os.path.relpath(cierre, RAIZ).replace("\\", "/")
            linea = git("log", "--reverse", "--format=%h", "--", rel).strip()
            h = linea.splitlines()[0].strip() if linea else ""
            if not h:
                sin_commit.append(fase)
                continue

            nuevo = estacion_commit.marcar(texto, h)
            if nuevo is None:
                saltadas.append(fase)
                continue
            if APLICAR:
                io.open(estado, "w", encoding="utf-8",
                        newline="\n").write(nuevo)
            puestas.append((fase, h))

print("== %s ==" % ("APLICADO" if APLICAR else "EN SECO (usa --aplicar)"))
print()
print("Se marcan %d fases, cada una con el commit que de verdad la cerro:"
      % len(puestas))
for fase, h in sorted(puestas):
    print("   %-64s %s" % (fase[:64], h))
if sin_commit:
    print()
    print("SIN COMMIT en el historial (no se tocan): %d" % len(sin_commit))
    for fase in sorted(sin_commit):
        print("   %s" % fase)
if saltadas:
    print()
    print("SALTADAS por las guardias: %d" % len(saltadas))
