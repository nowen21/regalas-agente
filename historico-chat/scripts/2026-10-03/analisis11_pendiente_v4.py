# -*- coding: utf-8 -*-
"""Análisis 11, acuerdos 5 y 6: cada análisis mejora al pendiente, y el pendiente 103 pasa a la V4."""
import glob
import io
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
P = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "pendientes", "103-*"))[0]
A = os.path.join(P, "analisis-11.md")
PEND = os.path.join(P, "pendiente.md")
R1001 = "../../../../../historico-chat/resumenes/2026-10-01/sesion.md"
HU003 = "[HU-003](../../HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde/HU-003-el-hallazgo-y-el-pendiente-tienen-solo-lo-que-les-corresponde.md)"

PROBLEMA = ("No hay un documento que fije el alcance antes de la HU. Nada obliga a que cada documento salga del anterior, "
            "ni a que el agente lea lo que el análisis ya decidió. Nada detiene al agente cuando trabaja fuera del plan "
            "aprobado, por ningún canal, y lo que una regla autoriza depende de que esa regla esté vigente. La plantilla "
            "del plan no permite comprobarlo con un programa. Y el análisis no recoge solo lo que pasa: la conversación, "
            "lo que aporta al análisis principal y lo que aprende.")
POR_QUE = "Al ejecutar el plan aparecen hallazgos que se podían evitar, y cada uno se vuelve un pendiente más."
NUEVOS = ["H-1", "H-3", "H-4", "H-5", "H-7", "H-8", "H-11", "H-13", "H-14"]
SALE = ("[H-13 de la sesión del 2026-09-28](../../../../../historico-chat/resumenes/2026-09-28/sesion.md), que reúne H-10, H-11 y H-13; "
        "[H-2 de la sesión del 2026-09-30](../../../../../historico-chat/resumenes/2026-09-30/sesion.md); y de la sesión del 2026-10-01, "
        + ", ".join("[%s](%s)" % (h, R1001) for h in NUEVOS[:-1]) + " y [%s](%s), que abrieron los análisis 3 a 11" % (NUEVOS[-1], R1001))

PENDIENTE = """# Pendiente: lo que se construye se aparta de lo aprobado

Reúne los pendientes 103, 104 y 105. Versión 4, del [análisis 11](analisis-11.md): suma lo que precisaron los análisis 3 a 11.

| | |
|---|---|
| **De dónde sale** | {sale} |

## El problema

{problema}

## Por qué importa

{por_que}
""".format(sale=SALE, problema=PROBLEMA, por_que=POR_QUE)

ACUERDOS = """5. Los hijos mejoran al padre: el análisis 1 originó el pendiente, y cada análisis siguiente lo mejora. Al aprobarse, el pendiente pasa a su versión siguiente: «De dónde sale» suma el hallazgo que abrió ese análisis, y «El problema» y «Por qué importa» recogen lo que precisó. El validador no deja aprobar un análisis cuyo hallazgo falta en el pendiente. Es el acuerdo 10 del análisis 1, que no se estaba cumpliendo (turnos 426 a 429).
6. El pendiente 103 al día: pasa a la V4, con los nueve hallazgos del 2026-10-01 que abrieron los análisis 3 a 11 y su problema reescrito con lo que ellos precisaron. Se hace de una, en este análisis (turnos 428 y 429).

Siguen abiertas: ninguna."""


def cambiar(t, a, b):
    assert t.count(a) == 1, a[:80]
    return t.replace(a, b)


def main():
    io.open(PEND, "w", encoding="utf-8", newline="\n").write(PENDIENTE)
    t = io.open(A, encoding="utf-8").read()
    t = cambiar(t, "\n\nSiguen abiertas: ninguna.", "\n" + ACUERDOS)
    t = cambiar(t, "| Tarea que cambia algo que una prueba o un programa lee |",
                "| Pendiente con varios análisis que no recoge lo que ellos aprendieron | Cualquier pendiente que vuelve al análisis | Se lee un problema viejo y se pierden los hallazgos | Punto 4 |\n"
                "| Tarea que cambia algo que una prueba o un programa lee |")
    t = cambiar(t, "> El H-14 no cambia. El pendiente sigue en la V3. EP-023 no suma HU: lo que se tiene que hacer entra en la fase `B` de la HU-007, que es el plan en curso.",
                "> El H-14 no cambia. El pendiente pasa a la V4. EP-023 no suma HU.\n\n"
                "### Pendiente V4. Lo que se construye se aparta de lo aprobado\n\n"
                "| Campo | Valor |\n|---|---|\n"
                "| De dónde sale | " + SALE.replace(R1001, R1001) + " |\n"
                "| El problema | " + PROBLEMA + " |\n"
                "| Por qué importa | " + POR_QUE + " |")
    t = cambiar(t, "| Es el plan en curso; la ejecución sigue desde la T-04 | 1, 2, 3 |",
                "| Es el plan en curso; la ejecución sigue desde la T-04 | 1, 2, 3 |\n"
                "| 2 | " + HU003 + " | El hallazgo y el pendiente tienen solo lo que les corresponde | El pendiente no recoge lo que aprenden sus análisis | HU-001 | Ya trata la forma del pendiente; no depende del freno | 4 |")
    t = cambiar(t, "| 3 | El estado vive en la regla: entrar o salir no toca el programa | Funcionó | S-276 | complementa R-1 |",
                "| 3 | El estado vive en la regla: entrar o salir no toca el programa | Funcionó | S-276 | complementa R-1 |\n"
                "| 4 | Los análisis no pasaban el pendiente a su versión siguiente, aunque el acuerdo 10 del análisis 1 lo pedía | Falló | S-277 | complementa R-9 |")
    t = cambiar(t, "y seguir desde la T-04 | 1 | EP-023, ",
                "y seguir desde la T-04 | 1 | EP-023, ")
    i = t.index("## Lo que aporta al análisis principal")
    filas = ("| 4 | Que cada análisis aprobado pase el pendiente a su versión siguiente con su hallazgo y lo que precisó, y que el validador no deje aprobarlo si su hallazgo falta en el pendiente | 5 | EP-023, " + HU003 + " |\n"
             "| 5 | Pasar el pendiente 103 a la V4 | 6 | Este análisis, de una y sin fase: `documentacion/epicas/EP-023-lo-que-se-construye-es-lo-que-se-analizo/pendientes/103-cada-documento-de-la-cadena-sale-del-anterior/pendiente.md`, hecho el 2026-10-03 |\n\n")
    antes = t[:i].rstrip("\n") + "\n"
    t = antes + filas + t[i:]
    t = cambiar(t, "y las pruebas no fijan cuáles ni cuántas son.",
                "y las pruebas no fijan cuáles ni cuántas son. Cada análisis mejora a su pendiente: lo deja en su versión siguiente.")
    io.open(A, "w", encoding="utf-8", newline="\n").write(t)


if __name__ == "__main__":
    main()
