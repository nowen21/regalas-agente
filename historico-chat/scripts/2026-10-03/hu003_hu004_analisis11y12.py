# -*- coding: utf-8 -*-
"""Lo que los análisis 11 y 12 del pendiente 103 pasan a las HU: el CA-09 de la HU-003
(análisis 11, punto 4) y el CA-08 de la HU-004 (análisis 12, punto 1)."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
EP = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*"))[0]
HU003 = glob.glob(os.path.join(EP, "HU-003-*", "HU-003-*.md"))[0]
HU004 = glob.glob(os.path.join(EP, "HU-004-*", "HU-004-*.md"))[0]
P = "../pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/"
POR = "Claude, por pedido de Ing. José Dúmar Jiménez Ruíz"

CA09 = """
### CA-09 · Cada análisis deja el pendiente en su versión siguiente

**Sale de:** análisis 11, punto 4.

```gherkin
Dado un análisis que se va a aprobar
Cuando su hallazgo no está en «De dónde sale» de su pendiente
Entonces el análisis no se aprueba, y el aviso dice qué falta
Y al aprobarse, el pendiente queda en su versión siguiente, con el hallazgo sumado y «El problema» y «Por qué importa» con lo que el análisis precisó
```

**Cómo validarlo:**
1. Intentar aprobar un análisis cuyo hallazgo falta en el pendiente.
2. Leer la «Propuesta final» de la plantilla del análisis.

**Aprobado cuando:** la aprobación se niega y dice qué falta, y la plantilla pide el pendiente en su versión siguiente.
"""

CA08 = """
### CA-08 · Solo detiene el hallazgo que obliga a salirse del plan

**Sale de:** análisis 12, punto 1.

```gherkin
Dado un hallazgo al ejecutar una fase
Cuando no es de la épica en curso
Entonces el trabajo sigue y su pendiente nace donde pertenece
Y cuando es de la épica, detiene solo si para cerrar la fase obliga a tocar algo que el plan no declara
```

**Cómo validarlo:**
1. Leer `02·F9`.

**Aprobado cuando:** `02·F9` lo dice.
"""


def cambiar(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)


def agregar_ca(t, ultimo, nuevo):
    i = t.index("### %s ·" % ultimo)
    j = t.index("\n---\n\n## 5.", i)
    return t[:j] + "\n" + nuevo + t[j:]


def agregar_bitacora(t, texto):
    i = t.index("## 13. Bitácora")
    filas = [n for n in range(i, len(t)) if t.startswith("\n| 20", n)]
    fin = t.index("\n", filas[-1] + 1)
    return t[:fin] + "\n" + texto + t[fin:]


def hu003():
    t = io.open(HU003, encoding="utf-8").read()
    t = cambiar(t, "y del [análisis 8](%sanalisis-8.md), punto 10. Los campos" % P,
                "del [análisis 8](%sanalisis-8.md), punto 10, y del [análisis 11](%sanalisis-11.md), punto 4. Los campos" % (P, P))
    i = t.index("| RN-07 |")
    j = t.index("\n", i) + 1
    t = t[:j] + "| RN-08 | Cada análisis aprobado mejora a su pendiente: lo deja en su versión siguiente, con su hallazgo y lo que precisó | Análisis 11, acuerdo 5 |\n" + t[j:]
    t = agregar_ca(t, "CA-08", CA09)
    t = agregar_bitacora(t, "| 2026-10-03 | %s | Nace el CA-09, según el análisis 11. La aprobación queda sin efecto hasta que se revise |" % POR)
    io.open(HU003, "w", encoding="utf-8", newline="\n").write(t)


def hu004():
    t = io.open(HU004, encoding="utf-8").read()
    t = cambiar(t, "y del [análisis 2](%sanalisis-2.md) (punto 7). Los campos" % P,
                "del [análisis 2](%sanalisis-2.md) (punto 7) y del [análisis 12](%sanalisis-12.md) (punto 1). Los campos" % (P, P))
    i = t.index("| RN-08 |")
    j = t.index("\n", i) + 1
    t = t[:j] + ("| RN-09 | El hallazgo que no es de la épica en curso no detiene el trabajo; su pendiente nace donde pertenece. "
                 "El de la épica detiene solo si obliga a tocar algo que el plan no declara | Análisis 12, acuerdo 1 |\n") + t[j:]
    t = agregar_ca(t, "CA-07", CA08)
    t = agregar_bitacora(t, "| 2026-10-03 | %s | Nace el CA-08, según el análisis 12. La aprobación queda sin efecto hasta que se revise |" % POR)
    io.open(HU004, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    hu003()
    hu004()
