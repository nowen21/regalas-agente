# -*- coding: utf-8 -*-
"""Fase B de la HU-007, T-03: las reglas que mandan escribir la HU, la épica y el pendiente
suman su línea «Autoriza escribir» (análisis 1 del pendiente 103, acuerdo 46), con su sello."""
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SELLO = "contra **v51.0.0**, el **2026-10-03**."
_SELLO = re.compile(r"contra \*\*v[\d.]+\*\*, el \*\*[\d-]+\*\*\.")

REGLAS = [
    ("base/13-documentacion/reglas/DOC15-crea-la-historia-de-usuario-desde-la-plantilla-central.md",
     ["documentacion/epicas/*/HU-*/HU-*.md"]),
    ("base/13-documentacion/reglas/DOC16-crea-la-epica-desde-la-plantilla-central.md",
     ["documentacion/epicas/*/epica.md", "documentacion/epicas/*/EP-*.md"]),
    ("base/02-flujo-de-trabajo/reglas/F23-ejecuta-un-pendiente-como-fase-de-una-historia-de-usuario.md",
     ["**/pendientes/*/pendiente.md"]),
]


def main():
    for archivo, rutas in REGLAS:
        ruta = os.path.join(RAIZ, *archivo.split("/"))
        with open(ruta, encoding="utf-8") as f:
            t = f.read()
        m = re.search(r"^\*\*Aplica a:\*\*.*$", t, re.M)
        assert m and "**Autoriza escribir:**" not in t, archivo
        linea = "**Autoriza escribir:** " + ", ".join("`%s`" % r for r in rutas)
        t = t[:m.end()] + "\n\n" + linea + t[m.end():]
        assert len(_SELLO.findall(t)) == 1, archivo
        t = _SELLO.sub(SELLO, t)
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)


if __name__ == "__main__":
    main()
