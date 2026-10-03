# -*- coding: utf-8 -*-
"""Turnos 201 a 205: el análisis 9 suma «Lo acordado» y pone al día conclusiones y puntos."""
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RUTA = os.path.join(RAIZ, "documentacion", "epicas", "EP-023-lo-que-se-construye-es-lo-que-se-analizo",
                    "103-cada-documento-de-la-cadena-sale-del-anterior", "analisis-9.md")
H1 = ("../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md")

ACORDADO = """## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo. Las conclusiones salen de aquí.

1. Todo análisis se anota en el análisis principal, aunque no cambie el sistema (turnos 193 y 194).
2. Un análisis confirma, aclara, amplía, modifica la idea o cambia lo que se construye. Ese resultado queda en tres sitios: en la sección «Lo que aporta al análisis principal» del análisis, en la columna «Resultado» de la «Lista de análisis» del principal y, si toca una idea, en «Lo que está definido» del principal (turnos 194 y 201).
3. La sección «Lo que aporta al análisis principal» va dentro del análisis y se aprueba con él. Al aprobar, un programa la copia tal cual, y el validador falla si las dos copias no son idénticas (turnos 196 a 199).
4. Se anotan los análisis 3, 6, 7 y 8 y el análisis con la forma anterior de `analisis/`; el aviso revisa todos los aprobados (turno 194).
5. Cada análisis se anota en el análisis principal de su alcance, el del módulo o el del proyecto (turno 194).
6. Todo entra a la fase `D` de la HU-001 (turno 194).
7. La «Lista de cambios» del análisis principal pasa a ser «Lista de análisis», con fecha, resultado, qué y análisis (turno 201).
8. La plantilla del análisis lleva la sección «Lo acordado», que el agente escribe en el mismo turno en que el usuario acepta algo (turnos 201 y 202).
9. Todo análisis termina en una decisión que afecta al proyecto, y «Lo que se tiene que hacer» tiene siempre al menos una fila. Si la decisión es conceptual, la fila dice dónde queda escrita: «Lo que está definido», el planteamiento, la épica, la HU o el glosario. El validador no deja aprobar un análisis sin filas (turnos 202 a 204).

---

"""

CONCLUSIONES_NUEVAS = """| 7 | La lista del análisis principal | La «Lista de cambios» pasa a ser «Lista de análisis», con fecha, resultado, qué y análisis | Turno 201 |
| 8 | Lo acordado | La plantilla del análisis lleva la sección «Lo acordado», que el agente escribe en el mismo turno en que el usuario acepta algo; las conclusiones salen de ella | Turnos 201 y 202 |
| 9 | Todo análisis decide | Todo análisis termina en una decisión que afecta al proyecto, y «Lo que se tiene que hacer» tiene siempre al menos una fila. Si la decisión es conceptual, la fila dice dónde queda escrita. El validador no deja aprobar un análisis sin filas | Turnos 202 a 204 |

Siguen abiertas: ninguna."""

PUNTOS_NUEVOS = """| 5 | Sumar a la plantilla del análisis la sección «Lo acordado», después de la conversación | 8 | EP-023, [HU-001](H1), fase D |
| 6 | Que el validador no deje aprobar un análisis sin filas en «Lo que se tiene que hacer» | 9 | EP-023, [HU-001](H1), fase D |
""".replace("(H1)", "(" + H1 + ")")


def una(texto, viejo, nuevo):
    assert texto.count(viejo) == 1, viejo[:70]
    return texto.replace(viejo, nuevo)


def main():
    with open(RUTA, encoding="utf-8") as f:
        t = f.read()
    t = una(t, "## Lo que aportó cada parte", ACORDADO + "## Lo que aportó cada parte")
    t = una(t, "y qué cambia en «Lo que está definido» o en «Qué se construye hoy». El usuario la aprueba",
            "y qué cambia en «Lo que está definido» o en «Qué se construye hoy». El resultado queda también en la columna «Resultado» de la «Lista de análisis» y, si toca una idea, en «Lo que está definido». El usuario la aprueba")
    i = t.index("Siguen abiertas:")
    j = t.index("## Propuesta final")
    t = t[:i] + CONCLUSIONES_NUEVAS + "\n\n" + t[j:]
    t = una(t, "el análisis principal con «Lo que está definido» y las líneas",
            "el análisis principal con «Lo que está definido», la «Lista de análisis» y las líneas")
    t = una(t, "| 2, 4 | EP-023,", "| 2, 4, 7 | EP-023,")
    fila = [l for l in t.split("\n") if l.startswith("| 4 | Pasar el plan de la fase")][0]
    t = una(t, fila + "\n", PUNTOS_NUEVOS + fila.replace("| 4 |", "| 7 |", 1) + "\n")
    with open(RUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


if __name__ == "__main__":
    main()
