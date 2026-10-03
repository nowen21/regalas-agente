# -*- coding: utf-8 -*-
"""HU-003, CA-08: sale el traslado de los pendientes viejos. Lo agregó el agente en el punto 10 del
análisis 8 sin que la conclusión 15 lo dijera; lo acordado es que pasan a la forma nueva cuando se
vayan a trabajar (análisis 1, conclusión 38)."""
import glob
import os

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HU = glob.glob(os.path.join(RAIZ, "documentacion", "epicas", "EP-023-*", "HU-003-*", "HU-003-*.md"))[0]

CAMBIOS = [
    ("Y los pendientes abiertos de la carpeta pendientes/ de la raíz y el 103 se trasladan, con sus enlaces al día\n", ""),
    ("2. Correr el programa del índice.\n3. Buscar los pendientes abiertos y el 103 en su lugar nuevo.\n",
     "2. Correr el programa del índice.\n"),
    ("**Aprobado cuando:** el validador de fases pasa, el índice lista todos y los abiertos están en su lugar con los enlaces sanos.",
     "**Aprobado cuando:** el validador de fases pasa y el índice lista todos."),
    ("| **Estado** | Lista: aprobada el 2026-10-02 |", "| **Estado** | En revisión: cambió el CA-08 |"),
]


def main():
    with open(HU, encoding="utf-8") as f:
        t = f.read()
    for viejo, nuevo in CAMBIOS:
        assert t.count(viejo) == 1, viejo[:60]
        t = t.replace(viejo, nuevo)
    t = t.rstrip("\n") + ("\n| 2026-10-02 | Claude, por pedido de Ing. José Dúmar Jiménez Ruíz | Sale del CA-08 el traslado de "
                          "los pendientes viejos y del 103: lo agregó el agente sin origen en el análisis 8. Lo acordado es que "
                          "pasan a la forma nueva cuando se vayan a trabajar (análisis 1, conclusión 38). La aprobación queda "
                          "sin efecto hasta que se revise |\n")
    with open(HU, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)


if __name__ == "__main__":
    main()
