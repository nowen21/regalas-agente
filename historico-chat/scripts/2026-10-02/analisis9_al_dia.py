# -*- coding: utf-8 -*-
"""Análisis 9, turno de «revise todo el análisis»: los puntos 3, 4 y 13 de «Lo acordado» y las conclusiones
3, 4 y 11 se ponen al día con lo que se acordó después (puntos 15 y 16). La conversación no se toca:
se devuelven al turno 201 las dos líneas que un primer intento cambió por error. El punto 13 y las
conclusiones 3, 4 y 11 los cambió ese primer intento, un comando suelto, y quedaron bien."""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*"))[0], "analisis-9.md")

NUEVO_3 = ("3. La sección «Lo que aporta al análisis principal» va dentro del análisis y se aprueba con él; qué lleva y "
           "cómo pasa al análisis principal lo dice el punto 15 (turnos 196 a 199 y 222 a 225).")
NUEVO_4 = ("4. Se anotan todos los análisis, del de la forma anterior de `analisis/` al 9, cada uno con su resultado y su "
           "redacción propia; el aviso revisa todos los aprobados (turnos 194 y 222 a 225).")
TURNO_201 = [
    (NUEVO_3, "3. La sección «Lo que aporta al análisis principal» va dentro del análisis. Al aprobar, un programa la copia tal cual, y el validador compara las dos copias."),
    (NUEVO_4, "4. Se anotan los análisis 3, 6, 7 y 8 y el análisis viejo. El aviso revisa todos."),
]


def main():
    with open(RUTA, encoding="utf-8") as f:
        t = f.read()
    for nuevo, original in TURNO_201:
        assert t.count(nuevo) == 1
        t = t.replace(nuevo, original)
    i = t.index("## Lo acordado")
    cab, cuerpo = t[:i], t[i:]
    lineas = cuerpo.split("\n")
    for k, linea in enumerate(lineas):
        if linea.startswith("3. La sección «Lo que aporta al análisis principal» va dentro"):
            lineas[k] = NUEVO_3
        elif linea.startswith("4. Se anotan los análisis 3, 6, 7 y 8"):
            lineas[k] = NUEVO_4
        elif linea.startswith("## Lo que aportó cada parte"):
            break
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(cab + "\n".join(lineas))


if __name__ == "__main__":
    main()
