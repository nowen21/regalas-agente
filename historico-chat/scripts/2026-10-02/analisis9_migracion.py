# -*- coding: utf-8 -*-
"""Turnos 206 a 212: el análisis 9 suma lo acordado sobre la sección «Lo que aporta al análisis
principal» en los análisis ya aprobados, su propia sección y la puerta de versión, y arregla la tabla de conclusiones."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-9.md")
H1 = ("../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md")

ACORDADO = """10. Este análisis, por ser el piloto, lleva su propia sección «Lo que aporta al análisis principal», y su línea pasa al análisis principal junto con las de los análisis que faltan (turnos 206 y 207).
11. El programa no deja aprobar un análisis sin la sección «Lo que aporta al análisis principal»: si no está, no pone la marca y avisa (turnos 208 a 210).
12. A los análisis 1 a 8 y al análisis con la forma anterior de `analisis/` se les agrega una sola vez la sección «Lo que aporta al análisis principal», sacada de sus conclusiones y sin decisiones nuevas, con la nota de que se agregó en el piloto. Se hace de una, sin abrir fase, porque es la construcción de la base. El usuario aprueba esas secciones antes de que pasen al principal. `13·DOC24` lo admite por esta única vez (turnos 209 a 212).
13. Las demás secciones nuevas («Dónde más puede pasar», las recomendaciones consultadas, «Lo acordado», la tabla de HU con su orden y al menos una fila en «Lo que se tiene que hacer») no se agregan a los análisis ya aprobados: se exigen desde la versión que las trae (turnos 206 y 207).
"""

CONCLUSIONES = """| 10 | La sección en todos los análisis | El programa no deja aprobar un análisis sin «Lo que aporta al análisis principal». A los análisis 1 a 8 y al de la forma anterior se les agrega una sola vez, de una y sin fase, sacada de sus conclusiones y aprobada por el usuario; `13·DOC24` lo admite por esta única vez. Este análisis lleva también la suya | Turnos 206 a 212 |
| 11 | Lo que no se agrega a los análisis aprobados | «Dónde más puede pasar», las recomendaciones consultadas, «Lo acordado», la tabla de HU con su orden y al menos una fila en «Lo que se tiene que hacer» se exigen desde la versión que las trae | Turnos 206 y 207 |
"""

PUNTOS = """| 7 | Agregar a los análisis 1 a 8 y al de la forma anterior la sección «Lo que aporta al análisis principal», sacada de sus conclusiones, con la nota del piloto, y que el usuario la apruebe | 10 | Este análisis, de una y sin fase |
| 8 | Que el programa de aprobar no ponga la marca si falta la sección, y que las demás secciones nuevas se exijan desde la versión que las trae | 10, 11 | EP-023, [HU-001](H1), fase D |
""".replace("(H1)", "(" + H1 + ")")


def una(t, viejo, nuevo):
    assert t.count(viejo) == 1, viejo[:70]
    return t.replace(viejo, nuevo)


def main():
    with open(RUTA, encoding="utf-8") as f:
        t = f.read()
    fin = t.index("\n---\n\n## Lo que aportó cada parte")
    t = t[:fin] + "\n" + ACORDADO.rstrip("\n") + t[fin:]
    t = una(t, "| Turno 194 |\n\n| 7 |", "| Turno 194 |\n| 7 |")
    t = una(t, "\nSiguen abiertas: ninguna.", CONCLUSIONES + "\nSiguen abiertas: ninguna.")
    t = una(t, "| 3 | Pasar el CA-20 de la HU-001 a su versión siguiente: el análisis principal con «Lo que está definido», la «Lista de análisis» y las líneas de los análisis 3, 6, 7 y 8 y del análisis con la forma anterior;",
            "| 3 | Pasar el CA-20 de la HU-001 a su versión siguiente: el análisis principal con «Lo que está definido», la «Lista de análisis» y las líneas de los análisis 1 a 9 y del análisis con la forma anterior;")
    t = t.rstrip("\n") + "\n" + PUNTOS
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


if __name__ == "__main__":
    main()
