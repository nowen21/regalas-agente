# -*- coding: utf-8 -*-
"""Análisis 9, turnos 232 a 235: el piloto es todo el pendiente 103. Las tablas de HU de los análisis 1 y 2
quedan con su dependencia, su orden y su razón, según el orden que fijó el análisis 8 (conclusión 8),
y el análisis 9 registra lo acordado."""
import glob
import os
import re

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CARPETA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*"))[0]
NOTA = ("> Orden puesto al día en el piloto, por el [análisis 9](analisis-9.md), con el que fijó el "
        "[análisis 8](analisis-8.md), conclusión 8. El número identifica a la HU; el orden sale de sus dependencias.")

TABLA_1 = """| Orden | HU | Título | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|---|
| 1 | 1 | El análisis existe, tiene su forma y revisa las cuatro partes | Ninguna | Las demás se apoyan en el análisis | 1, 2, 3, 15, 16, 23, 29, 30, 32 |
| 2 | 5 | Nada se agrega fuera de lo pedido | 1 | Es pequeña y ataca la causa más directa | 8, 22, 28 |
| 3 | 2 | Cada documento sale del anterior | 1 | Cada documento sale del anterior antes de ordenar el hallazgo y el pendiente | 4, 5 |
| 4 | 3 | El hallazgo y el pendiente tienen solo lo que les corresponde | 1 | Da la forma del hallazgo y del pendiente que usan la 4 y la 7 | 7, 10, 11, 12, 19, 20, 21 |
| 5 | 6 | Lo aprendido incluye las lecciones | 1 | Las lecciones alimentan las recomendaciones del análisis | 9 |
| 6 | 4 | Un hallazgo detiene la ejecución y vuelve al análisis | 3 | Detener la ejecución necesita la forma del hallazgo | 6, 13, 14, 17, 18, 24 |
| 7 | 7 | Nada se escribe fuera del plan aprobado | 3, 4 | El freno anota el hallazgo y vuelve al análisis | 25, 26, 27, 31 |
"""

TABLA_2 = """| Orden | HU | Depende de | Por qué en ese orden | Puntos de lo que se tiene que hacer |
|---|---|---|---|---|
| 1 | HU-001 · El análisis existe, tiene su forma y revisa las cuatro partes | Ninguna | Las demás se apoyan en el análisis | Todos menos el 7 |
| 2 | HU-004 · Un hallazgo detiene la ejecución y vuelve al análisis | HU-003 | Detener la ejecución necesita la forma del hallazgo | 7 |
"""

ACORDADO_16 = ("16. El piloto es todo el pendiente 103: sus análisis, la épica EP-023, sus HU y sus fases. Lo que se "
               "corrige en el piloto se aplica a todos esos documentos, no solo al análisis donde se decidió. Termina "
               "cuando se cumple el plan del pendiente, con EP-023 construida, y entonces se revisan todos sus documentos "
               "contra la base ya construida. Por eso las tablas de HU de los análisis 1 y 2 quedan con su dependencia, su "
               "orden y su razón (turnos 232 a 235).")
CONCLUSION_14 = ("| 14 | Qué abarca el piloto | Todo el pendiente 103: sus análisis, EP-023, sus HU y sus fases. Lo que se corrige "
                 "se aplica a todos; al terminar, todos se revisan contra la base construida | Turnos 232 a 235 |\n")


def leer(ruta):
    with open(ruta, encoding="utf-8") as f:
        return f.read()


def escribir(ruta, texto):
    with open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def main():
    a1 = os.path.join(CARPETA, "analisis-1.md")
    t = leer(a1)
    m = re.search(r"^\| HU \| Título \| Puntos de lo que se tiene que hacer \|\n(?:\|.*\n)+\nOrden: .*\n", t, re.M)
    assert m
    t = t[:m.start()] + NOTA + "\n\n" + TABLA_1 + t[m.end():]
    escribir(a1, t)

    a2 = os.path.join(CARPETA, "analisis-2.md")
    t = leer(a2)
    i = t.index("### HU\n")
    j = t.index("## Lecciones aprendidas", i)
    bloque = t[i:j].rstrip("\n")
    t = t[:i] + bloque + "\n\n" + NOTA + "\n\n" + TABLA_2 + "\n" + t[j:]
    escribir(a2, t)

    a9 = os.path.join(CARPETA, "analisis-9.md")
    t = leer(a9)
    m = re.search(r"^15\. .*$", t, re.M)
    t = t[:m.end()] + "\n" + ACORDADO_16 + t[m.end():]
    t = t.replace("\nSiguen abiertas: ninguna.", CONCLUSION_14 + "\nSiguen abiertas: ninguna.", 1)
    escribir(a9, t)


if __name__ == "__main__":
    main()
