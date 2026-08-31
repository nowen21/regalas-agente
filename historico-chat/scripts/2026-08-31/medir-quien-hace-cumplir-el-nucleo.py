# -*- coding: utf-8 -*-
"""Que regla del capitulo 00 tiene hoy quien la haga cumplir, y cual no.

Es la linea base de `EP-005·HU-012`. **No decide nada**: busca el identificador
de cada regla dentro de los programas de comprobacion y de los enganches, y dice
donde aparece. Que una regla se nombre en un programa no prueba que ese programa
la haga cumplir; prueba que hay por donde empezar a mirar.

Lo que el guion **no** puede contestar es lo que la historia pide de verdad: si
esa pieza la ejecuta o solo la menciona. Eso se lee.
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import metareglas                                            # noqa: E402

# Donde vive lo que ejecuta: los programas de comprobacion y los enganches.
CARPETAS = (("validadores", ".py"), ("adaptadores", ".py"), (".githooks", ""))

# Un identificador suelto aparece en cualquier prosa. Se busca citado como lo
# cita esta casa: `N1`, `00·N1`, o dentro de un mensaje de hallazgo.
def _citas(rid):
    return re.compile(r"(?<![A-Za-z0-9])(?:00·)?%s(?![A-Za-z0-9])" % rid)


def _archivos():
    for carpeta, ext in CARPETAS:
        base = os.path.join(RAIZ, carpeta)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirs, nombres in os.walk(base):
            if "__pycache__" in dirpath or "tests" in dirpath:
                continue
            for n in nombres:
                if ext and not n.endswith(ext):
                    continue
                ruta = os.path.join(dirpath, n)
                try:
                    with io.open(ruta, encoding="utf-8", errors="replace") as f:
                        yield os.path.relpath(ruta, RAIZ).replace("\\", "/"), f.read()
                except OSError:
                    continue


def main():
    reglas = [r for r in metareglas.reglas(RAIZ)
              if r.capitulo == "00" and not r.derogada]
    fuentes = list(_archivos())

    con, sin = [], []
    for r in reglas:
        patron = _citas(r.id)
        donde = sorted({ruta for ruta, texto in fuentes if patron.search(texto)})
        (con if donde else sin).append((r, donde))

    print("REGLAS DEL CAPITULO 00 VIGENTES: %d\n" % len(reglas))

    print("SE NOMBRAN EN ALGUN PROGRAMA O ENGANCHE: %d" % len(con))
    print("(nombrarse no es hacerse cumplir: hay que leer cada una)\n")
    for r, donde in con:
        print("  %-6s %s" % (r.id, r.titulo[:58]))
        for d in donde[:4]:
            print("           %s" % d)
        if len(donde) > 4:
            print("           y %d mas" % (len(donde) - 4))
        print("")

    print("NO SE NOMBRAN EN NINGUNO: %d" % len(sin))
    print("(estas dependen hoy de que el agente se acuerde)\n")
    for r, _ in sin:
        print("  %-6s %s" % (r.id, r.titulo[:58]))

    print("\n" + "-" * 72)
    print("Con alguna pieza que mirar: %d de %d" % (len(con), len(reglas)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
