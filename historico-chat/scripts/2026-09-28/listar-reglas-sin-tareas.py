# -*- coding: utf-8 -*-
"""Lista las reglas vigentes que todavía no dicen a qué tareas aplican.

Fase `B` de `EP-005·HU-023`, tarea T-05. Escribe `reglas-sin-tareas.md` al lado
de este guion: una fila por regla, con su título y su cuerpo, para leerlas y
decidir sus tareas. No se vuelve a correr: las reglas ya quedaron anotadas.
"""
import io
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, os.path.join(RAIZ, "validadores"))

import mapa_tareas   # noqa: E402
import metareglas    # noqa: E402


def main():
    filas = ["| Regla | Título | Cuerpo |", "|---|---|---|"]
    n = 0
    for r in metareglas.reglas(RAIZ):
        if r.derogada or mapa_tareas.declaradas(r):
            continue
        # Sin el destino de los enlaces: son relativos a `base/`, y copiados
        # acá quedarían rotos. Se deja el texto, que es lo que se lee.
        cuerpo = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1",
                        " ".join(t for _, t in r.cuerpo)).replace("|", "/")
        filas.append("| %s·%s | %s | %s |" % (r.capitulo, r.id,
                                             r.titulo.replace("|", "/"),
                                             cuerpo[:260]))
        n += 1
    with io.open(os.path.join(AQUI, "reglas-sin-tareas.md"), "w",
                 encoding="utf-8", newline="\n") as f:
        f.write("# Reglas sin tareas\n\n%d reglas.\n\n" % n + "\n".join(filas) + "\n")
    print(n)


if __name__ == "__main__":
    main()
