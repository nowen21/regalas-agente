# -*- coding: utf-8 -*-
"""Reescribe la línea `_CITA_REGLA` de validadores/origen.py: la consola la había
dejado con caracteres de retroceso en lugar de `\\b` (análisis 14 del pendiente 103,
fila 5)."""
import io
import os

p = os.path.join(os.path.dirname(__file__), "..", "..", "..", "validadores", "origen.py")
t = io.open(p, encoding="utf-8").read()
lineas = t.split("\n")
for i, l in enumerate(lineas):
    if l.startswith("_CITA_REGLA"):
        lineas[i] = '_CITA_REGLA = re.compile(r"\\b(\\d{2})·([A-Z]+\\d+)\\b")'
io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lineas))
print([ascii(l) for l in lineas if l.startswith("_CITA_REGLA")])
