# -*- coding: utf-8 -*-
"""Fase D de la HU-001.

- T-10: el análisis principal pasa a ser la redacción que forman los aportes de los diez análisis,
  copiados tal cual de su sección «Lo que aporta al análisis principal», con su «Lista de análisis».
- T-15: los análisis 1 a 9 del pendiente 103 reciben la sección «Recomendaciones», con la nota del piloto.
"""
import glob
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import analisis_en_curso as curso  # noqa: E402
from comun import leer             # noqa: E402

CARPETA = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "103-*"))[0]
VIEJO = os.path.join(RAIZ, "analisis", "base-2026-08-07-cumplimiento-meta-reglas.md")
PRINCIPAL = os.path.join(RAIZ, "analisis", "proyecto-2026-10-02-analisis-principal.md")

INICIO = ("Cimiento es el estándar que hace que una IA que programa trabaje siempre igual en cualquier "
          "proyecto: con las mismas reglas, la misma memoria y comprobaciones que no dependen de que alguien se acuerde.")

CABEZA = """# Análisis principal de Cimiento

> Se forma con lo que aportan los análisis individuales: cada uno que se aprueba suma su frase, tal cual, al final de la redacción, y su fila a la «Lista de análisis» ([`13·DOC25`](../base/13-documentacion/reglas/DOC25-reescribe-el-analisis-principal-con-su-lista-de-cambios.md)). Los análisis individuales viven en la carpeta de su pendiente y, aprobados, no se reescriben ([`13·DOC24`](../base/13-documentacion/reglas/DOC24-cierra-el-analisis-en-su-mismo-archivo.md)). La necesidad, el objetivo y el alcance están en el [planteamiento](../planteamiento.md); las épicas, en su [índice](../documentacion/epicas/README.md).

## Qué es Cimiento

"""

# De sus lecciones salen estas recomendaciones (plantillas/recomendaciones-del-analisis.md).
DE_SUS_LECCIONES = {
    1: "R-2, R-7, R-8, R-9, R-10 y R-11", 2: "R-11, R-12 y R-15", 3: "R-6, R-7 y R-10", 4: "R-13 y R-14",
    5: "R-3 y R-15", 6: "R-2, R-10 y R-15", 7: "R-4", 8: "R-1, R-5, R-16 y R-17",
    9: "ninguna todavía: sus lecciones se suman cuando se revisen contra el archivo",
}


def fecha(ruta):
    m = re.search(r"Aprobado\*\* por el usuario el (\d{4}-\d{2}-\d{2})", leer(ruta))
    return m.group(1) if m else "2026-08-07"


def principal():
    rutas = [VIEJO] + [os.path.join(CARPETA, "analisis-%d.md" % n) for n in range(1, 10)]
    redaccion, filas = INICIO, []
    for ruta in rutas:
        resultado, suma = curso.aporte(leer(ruta))
        redaccion += " " + suma
        enlace = os.path.relpath(ruta, os.path.dirname(PRINCIPAL)).replace(os.sep, "/")
        filas.append("| %s | %s | [%s](%s) |" % (fecha(ruta), resultado.rstrip("."), curso.nombre_del_analisis(ruta), enlace))
    texto = (CABEZA + redaccion + "\n\n" + curso.LISTA + "\n\n| Fecha | Resultado | Análisis |\n|---|---|---|\n"
             + "\n".join(filas) + "\n")
    with open(PRINCIPAL, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


def recomendaciones():
    for n in range(1, 10):
        ruta = os.path.join(CARPETA, "analisis-%d.md" % n)
        t = leer(ruta)
        assert "## Recomendaciones" not in t
        seccion = ("## Recomendaciones\n\n"
                   "> Se agregó en el piloto, por el [análisis 9](analisis-9.md): este análisis no consultó recomendaciones, "
                   "porque el archivo no existía. De sus lecciones salen: %s.\n\n"
                   "| Recomendación | Cómo se aplica en este análisis |\n|---|---|\n"
                   "| Ninguna | El archivo de [recomendaciones del análisis](../../../../plantillas/recomendaciones-del-analisis.md) nació después |\n\n"
                   "---\n\n" % DE_SUS_LECCIONES[n])
        i = t.index("## Hallazgo")
        t = t[:i] + seccion + t[i:]
        with open(ruta, "w", encoding="utf-8", newline="\n") as f:
            f.write(t)


if __name__ == "__main__":
    principal()
    recomendaciones()
