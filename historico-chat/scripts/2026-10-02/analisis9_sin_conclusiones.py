# -*- coding: utf-8 -*-
"""Análisis 9, turnos 248 a 252: «Lo acordado» reemplaza a «Conclusiones», de una y sin fase.

- Plantilla del análisis: «Lo acordado» va después de la conversación y «Conclusiones» sale.
- `02·F27` y `validadores/reglas-validables.md`: el punto de «Lo acordado» cita su turno.
- Análisis 1 a 8: se quita la tabla de conclusiones; «Lo acordado» ya la tenía, con el mismo número.
- Análisis 9: cada punto acordado lleva su tema, y «Lo que se tiene que hacer» cita el punto acordado.
"""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CARPETA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*"))[0]

NOTA_VIEJA = ("> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este "
              "análisis; no decide nada nuevo.\n\n")
NOTA_ACORDADO = ("> Se agregó en el piloto, por el [análisis 9](analisis-9.md), a partir de las conclusiones de este "
                 "análisis, que después se quitaron para no repetirlas; cada punto conserva el número de su conclusión. "
                 "No decide nada nuevo.\n\n")

# Análisis 9: tema de cada punto acordado.
TEMAS = {1: "Todo análisis se anota", 2: "Lo que hace un análisis", 3: "Lo que aporta al análisis principal",
         4: "Los análisis que faltan", 5: "En qué principal", 6: "Dónde se pide",
         7: "La lista del análisis principal", 8: "Lo acordado", 9: "Todo análisis decide",
         10: "La sección de este análisis", 11: "La marca de aprobado", 12: "La sección en los análisis anteriores",
         13: "Lo que se agrega a los análisis aprobados", 14: "El piloto", 15: "Cómo complementa el hijo al padre",
         16: "Qué abarca el piloto", 17: "Sin información repetida", 18: "Los trabajos del piloto"}
# Análisis 9: fila de «Lo que se tiene que hacer» → puntos acordados que cita.
CITAS = {1: "1, 2, 3, 5", 2: "3, 15", 3: "2, 4, 7, 17", 4: "8", 5: "9", 6: "6", 7: "12, 13", 8: "11, 13",
         9: "18", 10: "16, 18", 11: "17"}


def leer(r):
    with open(r, encoding="utf-8") as f:
        return f.read()


def escribir(r, t):
    with open(r, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def una(t, viejo, nuevo):
    assert t.count(viejo) == 1, viejo[:80]
    return t.replace(viejo, nuevo)


def sin_conclusiones(t):
    """Quita la sección de conclusiones y pasa «Siguen abiertas» al final de «Lo acordado»."""
    m = re.search(r"^## Conclusiones.*\n", t, re.M)
    fin = re.search(r"^## ", t[m.end():], re.M)
    bloque = t[m.start():m.end() + fin.start()]
    abiertas = re.search(r"^Siguen abiertas: .*$", bloque, re.M).group(0)
    antes = t[:m.start()].rstrip("\n")
    if antes.endswith("---"):
        antes = antes[:-3].rstrip("\n")
    t = antes + "\n\n---\n\n" + t[m.end() + fin.start():]
    i = t.index("## Lo acordado")
    j = t.index("\n---\n", i)
    t = t[:j].rstrip("\n") + "\n\n" + abiertas + "\n" + t[j:]
    return t.replace("| Sale de la conclusión |", "| Sale de lo acordado |")


def analisis_1_a_8():
    for n in range(1, 9):
        ruta = os.path.join(CARPETA, "analisis-%d.md" % n)
        t = leer(ruta)
        i = t.index("## Lo acordado")
        t = t[:i] + una(t[i:i + 2000], NOTA_VIEJA, NOTA_ACORDADO) + t[i + 2000:]
        escribir(ruta, sin_conclusiones(t))


def analisis_9():
    ruta = os.path.join(CARPETA, "analisis-9.md")
    t = leer(ruta)
    t = una(t, "> Se escribe en el mismo turno en que el usuario acepta algo. Las conclusiones salen de aquí.",
            "> Se escribe en el mismo turno en que el usuario acepta algo.")
    i = t.index("## Lo acordado")
    j = t.index("\n---\n", i)

    def con_tema(m):
        n, texto = int(m.group(1)), m.group(2)
        return "%d. %s: %s%s" % (n, TEMAS[n], texto[0].lower(), texto[1:])
    t = t[:i] + re.sub(r"^(\d+)\. (.*)$", con_tema, t[i:j], flags=re.M) + t[j:]
    t = una(t, "Mientras `validar.py origen` exija las conclusiones, se quedan; se quitan en la fase `D` (turnos 239 a 250).",
            "Se hace de una y sin fase, con la plantilla, `validar.py origen` y `02·F27` (turnos 239 a 252).")
    t = sin_conclusiones(t)
    k = t.index("## Lo que se tiene que hacer")

    def cita(m):
        celdas = m.group(0).split("|")
        celdas[3] = " %s " % CITAS[int(m.group(1))]
        return "|".join(celdas)
    t = t[:k] + re.sub(r"^\| (\d+) \|.*$", cita, t[k:], flags=re.M)
    t = una(t, "la «Lista de análisis» y las líneas", "la «Lista de análisis», con fecha, resultado y enlace, y las líneas")
    t = re.sub(r"^(\| 4 \| Sumar a la plantilla del análisis la sección «Lo acordado».*\| 8 \|) .*\|$",
               r"\1 Este análisis, de una y sin fase |", t, flags=re.M)
    t = re.sub(r"^\| 11 \| Quitar «Conclusiones».*$",
               "| 11 | Quitar «Conclusiones» de la plantilla del análisis y de los análisis del piloto, y que `validar.py origen` "
               "y `02·F27` citen el punto de «Lo acordado» | 17 | Este análisis, de una y sin fase |", t, flags=re.M)
    escribir(ruta, t)


def plantilla():
    ruta = os.path.join(RAIZ, "plantillas", "analisis.md")
    t = leer(ruta)
    t = una(t, """> acá termina la conversación

---
""", """> acá termina la conversación

---

## Lo acordado

> Se escribe en el mismo turno en que el usuario acepta algo: un punto por cada decisión, con su tema y el turno de la conversación donde se acordó.

1. «tema»: «lo que se decidió» (turno «N»).

Siguen abiertas: «pregunta sin decidir, o "ninguna"».

---
""")
    m = re.search(r"^## Conclusiones\n.*?(?=^## Propuesta final)", t, re.M | re.S)
    t = t[:m.start()] + t[m.end():]
    t = una(t, "y qué conclusión lo recoge»", "y qué punto de «Lo acordado» lo recoge»")
    t = una(t, "«Sale de» cita la conclusión de donde sale; lo que no tenga conclusión no entra.",
            "«Sale de» cita el punto de «Lo acordado» de donde sale; lo que no tenga punto acordado no entra.")
    t = una(t, "| Sale de la conclusión |", "| Sale de lo acordado |")
    escribir(ruta, t)


def regla():
    ruta = os.path.join(RAIZ, "base", "02-flujo-de-trabajo", "reglas", "F27-cada-punto-dice-de-que-punto-del-anterior-sale.md")
    t = leer(ruta)
    t = una(t, "la conclusión del análisis, su turno;", "el punto de «Lo acordado» del análisis, su turno;")
    t = una(t, "contra **v42.0.0**, el **2026-10-02**", "contra **v43.0.0**, el **2026-10-02**")
    escribir(ruta, t)
    ruta = os.path.join(RAIZ, "validadores", "reglas-validables.md")
    t = leer(ruta)
    t = una(t, "conclusión→turno, «Lo que se tiene que hacer»→conclusión", "punto acordado→turno, «Lo que se tiene que hacer»→punto acordado")
    escribir(ruta, t)


if __name__ == "__main__":
    analisis_1_a_8()
    analisis_9()
    plantilla()
    regla()

# Después de correrlo, en la parte «Cimiento» del análisis 9 se cambió a mano «choca con la conclusión 1»
# por «choca con el punto 1 de «Lo acordado»»: era la única cita a una conclusión del mismo análisis.
