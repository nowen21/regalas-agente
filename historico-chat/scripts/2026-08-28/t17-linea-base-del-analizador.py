# -*- coding: utf-8 -*-
"""`02.F17`: la linea base del plan tiene once dias. Se vuelve a medir.

El plan de `B-EP-004-HU-002` se escribio el 2026-08-17 y dice tres cosas que
hay que comprobar hoy antes de construir nada:

  1. «200 reglas reconocidas»            -> ?cuantas ve hoy el analizador?
  2. «no existe un subcomando que lo corra» -> ?sigue sin existir?
  3. «4 reglas con ### en el cap 16, y 5 sub-reglas de F12 en vinneta»

Es la leccion que dejo `A-EP-003-HU-006` (`D-02`): declarar la entrada de un
procedimiento no obliga a comprobar que lo declarado siga siendo cierto, y once
fases arrancaron ese dia con una linea base de cinco dias atras.
"""
import io
import os
import re
import subprocess
import sys

RAIZ = r"c:\Ing. Jose\ia\agente"
sys.path.insert(0, os.path.join(RAIZ, "validadores"))
import metareglas                                           # noqa: E402
import comun                                                # noqa: E402

print("=== 1 - Cuantas reglas ve el analizador hoy ===")
reglas = metareglas.reglas(comun.RAIZ)
print("   El plan decia 200. Hoy ve: %d" % len(reglas))
print("")

print("=== 2 - El subcomando que 'no existe' ===")
r = subprocess.run([sys.executable, os.path.join(RAIZ, "validadores", "validar.py"),
                    "metareglas"], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
existe = "invalid choice" not in (r.stdout + r.stderr)
print("   `validar.py metareglas` %s" % ("EXISTE y corre" if existe else "sigue sin existir"))
if existe:
    ultima = [l.strip() for l in (r.stdout or "").splitlines() if l.strip()][-1:]
    print("   Su ultima linea: %s" % (ultima[0] if ultima else "(sin salida)"))
print("")

print("=== 3 - Las formas de escribir una regla que el analizador NO ve ===")
base = os.path.join(RAIZ, "base")
con_tres = []
for carpeta, _, archivos in os.walk(base):
    for n in archivos:
        if not n.endswith(".md"):
            continue
        ruta = os.path.join(carpeta, n)
        texto = io.open(ruta, encoding="utf-8", errors="replace").read()
        for linea in texto.splitlines():
            if re.match(r"^###\s+[A-Z]+\d+\s*[\u00b7.-]", linea):
                con_tres.append((os.path.relpath(ruta, RAIZ), linea.strip()[:60]))
vistas = {r.id for r in reglas}
print("   Encabezados con ### que parecen regla: %d" % len(con_tres))
for ruta, linea in con_tres[:12]:
    ident = linea.split()[1] if len(linea.split()) > 1 else "?"
    print("      %-46s %-22s %s" % (ruta.replace(os.sep, "/")[:44], linea[:20],
                                    "LA VE" if ident in vistas else "no la ve"))
print("")

print("=== 4 - El capitulo 16, que salio con cero en las 21 fases ===")
del_16 = [r for r in reglas if r.capitulo == "16"]
print("   Reglas del capitulo 16 que ve el analizador: %d" % len(del_16))
print("")

print("=== 5 - Las pruebas en rojo esperado que el plan nombra ===")
pruebas = io.open(os.path.join(RAIZ, "validadores", "pruebas.py"),
                  encoding="utf-8").read()
for nombre in ("test_el_analizador_ve_todas_las_reglas",
               "test_la_regla_sin_clasificar_es_falla"):
    if nombre in pruebas:
        i = pruebas.index(nombre)
        contexto = pruebas[max(0, i - 400):i]
        tapada = "expectedFailure" in contexto.split("def ")[-2] if "def " in contexto else False
        print("   %-46s existe %s" % (nombre, "(tapada)" if tapada else ""))
    else:
        print("   %-46s NO EXISTE" % nombre)
