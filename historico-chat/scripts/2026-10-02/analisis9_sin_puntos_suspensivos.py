# -*- coding: utf-8 -*-
"""El control previo al commit rechazó cuatro «…» en la conversación del análisis 9 (`00·ID8`).
Salieron de citas cortadas en respuestas del agente; se cambian por el texto completo que citaban."""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*", "analisis-9.md"))[0]

CAMBIOS = [
    ("trabaje siempre igual…»",
     "trabaje siempre igual en cualquier proyecto: con las mismas reglas, la misma memoria y comprobaciones que no dependen de que alguien se acuerde»"),
    ("«… Ese resultado queda en dos sitios",
     "«Un análisis confirma, aclara, amplía, modifica la idea o cambia lo que se construye. Ese resultado queda en dos sitios"),
    ("el planteamiento…», pasaría", "el planteamiento, la épica, la HU o el glosario», pasaría"),
    ("el planteamiento…».", "el planteamiento, la épica, la HU o el glosario»."),
]


def main():
    with open(RUTA, encoding="utf-8") as f:
        t = f.read()
    for viejo, nuevo in CAMBIOS:
        assert t.count(viejo) == 1, viejo
        t = t.replace(viejo, nuevo)
    assert "…" not in t
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


if __name__ == "__main__":
    main()
