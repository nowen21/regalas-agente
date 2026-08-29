# -*- coding: utf-8 -*-
"""T-04: de donde cuelga la corrida completa sin volverse peaje.

Las 650 pruebas tardan **577 segundos**: 9,6 minutos. El plan estimaba 3, y el
numero real cambia la respuesta ---no la confirma---, asi que se mide antes de
colgar nada.

El criterio de suspension esta escrito: si lo colgado agrega mas de UN MINUTO a
algo que se hace en cada commit, se cuelga en otro sitio. Un peaje de 9,6
minutos por commit no se discute: se desinstala en una tarde, y entonces
quedamos peor que hoy, con un control que figura como puesto.

La pregunta que se mide: en que momentos se podria colgar, y cuanto costaria
cada uno **con el ritmo real de este repositorio**.
"""
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
TARDA = 577.4          # segundos, medido con `validar.py internas`


def git(*args):
    return subprocess.run(["git"] + list(args), cwd=RAIZ, capture_output=True,
                          text=True, encoding="utf-8", errors="replace").stdout


commits = [l for l in git("log", "--format=%h %ad", "--date=short",
                          "--since=14.days").splitlines() if l.strip()]
dias = sorted({l.split()[1] for l in commits})

print("Ritmo real de los ultimos 14 dias:")
print("   commits: %d" % len(commits))
print("   dias con actividad: %d" % len(dias))
print("   commits por dia con actividad: %.1f" % (len(commits) / max(1, len(dias))))
print("")

print("%-28s %-14s %s" % ("SI CUELGA DE...", "VECES/14 DIAS", "COSTO TOTAL"))
opciones = [
    ("cada commit", len(commits)),
    ("cada push (~1 por dia)", len(dias)),
    ("abrir sesion (~1 por dia)", len(dias)),
    ("una vez al dia, al azar", len(dias)),
]
for nombre, veces in opciones:
    total = veces * TARDA / 60.0
    print("%-28s %-14d %.0f min  (%.1f h)" % (nombre, veces, total, total / 60))

print("")
print("Por vez: %.1f minutos." % (TARDA / 60))
print("")
print("El umbral escrito en el plan es UN MINUTO por commit. Ninguna opcion que")
print("CORRA las pruebas lo cumple: la mas barata cuesta 9,6 minutos la vez.")
print("")
print("Asi que la pregunta cambia: no es donde correrlas, es **como enterarse**")
print("de que hace falta correrlas sin pagar 9,6 minutos. Eso ya tiene forma en")
print("esta casa ---el enganche del checkpoint RECLAMA en vez de hacer--- y")
print("cuesta lo que cuesta mirar una fecha.")
