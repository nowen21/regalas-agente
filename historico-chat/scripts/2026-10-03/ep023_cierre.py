# -*- coding: utf-8 -*-
"""Deja terminadas las siete HU de EP-023 y la épica (análisis 14 del pendiente 103,
acuerdo 11, fila 13)."""
import glob
import io
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EPICA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*"))[0]
FECHA = "2026-10-03"


def cambiar(ruta, viejo, nuevo, cuenta=1):
    t = io.open(ruta, encoding="utf-8").read()
    n = len(re.findall(viejo, t, re.M))
    assert n == cuenta, (ruta, viejo, n)
    t = re.sub(viejo, nuevo, t, flags=re.M)
    io.open(ruta, "w", encoding="utf-8", newline="\n").write(t)


for hu in sorted(glob.glob(os.path.join(EPICA, "HU-*", "HU-*.md"))):
    cambiar(hu, r"^\| \*\*Estado\*\* \| Lista: aprobada el [0-9-]+ \|$",
            "| **Estado** | Terminada el %s, con sus criterios probados |" % FECHA)

hu7 = glob.glob(os.path.join(EPICA, "HU-007-*", "HU-007-*.md"))[0]
cambiar(hu7, r"^(\| \[`C-EP-023-HU-007-[^\n]*\| Cumple \|)$",
        r"\1\n\nLo que faltaba del CA-02, la revisión en la integración continua y el contrato "
        r"de cada adaptador, se hizo de una en el análisis 14 del pendiente 103 (acuerdo 11, fila 12).")

epica = os.path.join(EPICA, "epica.md")
cambiar(epica, r"^\| \*\*Estado\*\* \| Propuesta \|$",
        "| **Estado** | Terminada el %s: sus siete historias cumplen |" % FECHA)
cambiar(epica, r"\| Lista: aprobada el [0-9-]+ \|$", "| Terminada el %s |" % FECHA, cuenta=7)
cambiar(epica, r"\| Por hacer \|$", "| Hecha |", cuenta=5)
print("listo")
