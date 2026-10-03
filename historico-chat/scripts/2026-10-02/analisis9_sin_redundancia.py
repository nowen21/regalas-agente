# -*- coding: utf-8 -*-
"""Análisis 9, turnos 236 a 250: la información no se repite (`20·M2`).

- En los diez análisis del piloto, «Lo que aporta al análisis principal» queda con dos partes: el
  resultado y lo que el análisis suma al principal. La redacción completa vive solo en el principal.
- El análisis 9 anota lo acordado, su conclusión, sus filas de «Lo que se tiene que hacer» y la lección 4.
- Las conclusiones se quedan mientras `validar.py origen` (`02·F27`) las exija; se quitan en la fase D.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from piloto_aporte_en_cadena import CADENA, NOTA, CARPETA, ruta_de

A9 = os.path.join(CARPETA, "analisis-9.md")
H1 = ("[HU-001](../HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes/"
      "HU-001-el-analisis-existe-tiene-su-forma-y-revisa-las-cuatro-partes.md)")


def leer(r):
    with open(r, encoding="utf-8") as f:
        return f.read()


def escribir(r, t):
    with open(r, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


def una(t, viejo, nuevo):
    assert t.count(viejo) == 1, viejo[:80]
    return t.replace(viejo, nuevo)


def linea(t, prefijo, nueva):
    m = re.search(r"^" + re.escape(prefijo) + r".*$", t, re.M)
    assert m, prefijo
    return t[:m.start()] + nueva + t[m.end():]


def aportes():
    for clave, resultado, _propia, suma in CADENA:
        ruta = ruta_de(clave)
        t = leer(ruta)
        i = t.index("## Lo que aporta al análisis principal")
        a9 = os.path.relpath(A9, os.path.dirname(ruta)).replace(os.sep, "/")
        nota = (NOTA % a9 + "\n\n") if clave != 9 else ""
        t = (t[:i] + "## Lo que aporta al análisis principal\n\n" + nota
             + "**Resultado:** %s.\n\n**Lo que suma al análisis principal:** %s\n"
             % (resultado.lower().capitalize(), suma.strip()))
        escribir(ruta, t)


ACORDADO_2 = ("2. Un análisis confirma, aclara, amplía, modifica la idea o cambia lo que se construye. Ese resultado queda "
              "en la sección «Lo que aporta al análisis principal» del análisis y en la columna «Resultado» de la "
              "«Lista de análisis» del principal (turnos 194, 201 y 239 a 247).")
ACORDADO_15 = ("15. «Lo que aporta al análisis principal» tiene dos partes: el resultado y lo que el análisis suma a la "
               "redacción del principal. El usuario las aprueba con el análisis y el programa pasa lo que suma, tal cual, "
               "al análisis principal. La redacción completa vive solo en el principal (turnos 222 a 225 y 248 a 250).")
ACORDADO_NUEVOS = """17. La información se escribe una sola vez (`20·M2`). «Lo acordado» reemplaza a «Conclusiones»: cada punto lleva su tema y sus turnos, y «Lo que se tiene que hacer» cita el número del punto. La «Lista de análisis» lleva la fecha, el resultado y el enlace al análisis. El análisis principal deja de tener «Lo que está definido» y «Qué se construye hoy»: su contenido es la redacción que forman los aportes de los análisis. Mientras `validar.py origen` exija las conclusiones, se quedan; se quitan en la fase `D` (turnos 239 a 250).
18. Los trabajos que salen del piloto se anotan en «Lo que se tiene que hacer»: las recomendaciones consultadas de los análisis 1 a 9 van a la fase `D` de la HU-001, y la revisión de todos los documentos del piloto, al cierre del pendiente 103 (turnos 236 a 245)."""

CONCLUSION_13 = ("| 13 | Cómo complementa el hijo al padre | El análisis hijo dice solo lo que suma al padre; el usuario lo aprueba "
                 "y el programa lo pasa tal cual. La redacción completa vive solo en el principal | Turnos 222 a 225 y 248 a 250 |")
CONCLUSIONES_NUEVAS = """| 15 | Sin información repetida | Cada cosa se escribe una vez: «Lo acordado» reemplaza a «Conclusiones», la «Lista de análisis» lleva fecha, resultado y enlace, y el principal es la redacción que forman los aportes, sin «Lo que está definido» ni «Qué se construye hoy» | Turnos 239 a 250 |
| 16 | Los trabajos del piloto | Las recomendaciones de los análisis 1 a 9 van a la fase `D` de la HU-001; la revisión de todos los documentos del piloto, al cierre del pendiente 103 | Turnos 236 a 245 |
"""
PUNTO_2 = ("| 2 | Sumar a la plantilla del análisis la sección «Lo que aporta al análisis principal», con el resultado y lo "
           "que suma al principal; que el enganche de aprobar lo pase tal cual al principal y que el validador compare las "
           "copias | 3, 13 | EP-023, %s, fase D |" % H1)
PUNTOS_NUEVOS = """| 9 | Agregar a los análisis 1 a 9 las recomendaciones consultadas, cuando la fase `D` cree su archivo | 16 | EP-023, HU-001, fase D |
| 10 | Al quedar construida EP-023, revisar todos los documentos del piloto contra la base construida | 14, 16 | Cierre del pendiente 103 |
| 11 | Quitar «Conclusiones» de la plantilla del análisis y de los análisis del piloto, y que `validar.py origen` y `02·F27` citen el punto de «Lo acordado»; la «Lista de análisis» con fecha, resultado y enlace | 15 | EP-023, HU-001, fase D |
"""
LECCION_4 = ("| 4 | Se copió en el hijo la redacción del padre; el ejemplo de `Matematicas` aclaró que el hijo dice solo lo que "
             "suma, y la redacción completa queda en el padre | Falló | Por escribir |")


def analisis9():
    t = leer(A9)
    i = t.index("## Lo acordado")
    cab, cuerpo = t[:i], t[i:]
    cuerpo = linea(cuerpo, "2. Un análisis confirma", ACORDADO_2)
    cuerpo = una(cuerpo, "dónde queda escrita: «Lo que está definido», el planteamiento",
                 "dónde queda escrita: la redacción del análisis principal, el planteamiento")
    cuerpo = linea(cuerpo, "15. «Lo que aporta al análisis principal» tiene tres partes", ACORDADO_15)
    m = re.search(r"^16\. .*$", cuerpo, re.M)
    cuerpo = cuerpo[:m.end()] + "\n" + ACORDADO_NUEVOS + cuerpo[m.end():]
    cuerpo = linea(cuerpo, "| 13 | Cómo complementa el hijo al padre |", CONCLUSION_13)
    m = re.search(r"^\| 14 \| Qué abarca el piloto .*\n", cuerpo, re.M)
    cuerpo = cuerpo[:m.end()] + CONCLUSIONES_NUEVAS + cuerpo[m.end():]
    m = re.search(r"^\| 3 \| Se le exigía al piloto .*\n", cuerpo, re.M)
    cuerpo = cuerpo[:m.end()] + LECCION_4 + "\n" + cuerpo[m.end():]
    cuerpo = linea(cuerpo, "| 2 | Sumar a la plantilla del análisis la sección «Lo que aporta", PUNTO_2)
    cuerpo = una(cuerpo, "el análisis principal con la redacción que propone el análisis 9, «Lo que está definido», la «Lista de análisis»",
                 "el análisis principal con la redacción que forman los aportes de los análisis, la «Lista de análisis»")
    m = re.search(r"^\| 8 \| Que el programa de aprobar .*\n", cuerpo, re.M)
    cuerpo = cuerpo[:m.end()] + PUNTOS_NUEVOS + cuerpo[m.end():]
    escribir(A9, cab + cuerpo)


if __name__ == "__main__":
    analisis9()
    aportes()
