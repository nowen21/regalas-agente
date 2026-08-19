# -*- coding: utf-8 -*-
"""`09·14` · Escribe la línea del índice que falta, en vez de solo reportarla.

**El validador la detecta después; nadie la evita antes.** Cada archivo nuevo
obliga a agregar su línea al índice a mano, y olvidarlo es trabajo mecánico que
se descubre corriendo `validar.py estandar` — a veces varios commits después.

**No reescribe el índice entero, y es a propósito.** Las líneas que ya están
llevan una descripción escrita por alguien —*«por qué se confunde de quién es el
dato con quién lo tocó»*— que el encabezado del archivo no tiene. Regenerar el
bloque cambiaría eso por el título y perdería lo único que hacía útil el índice.

**Lo que hace es agregar lo que falta**, con el título del archivo como
descripción provisional, y **dejar dicho que hay que afinarla**. Lo que sobra lo
reporta y no lo borra: quitar una línea del índice puede ser el error, no el
archivo que ya no está.
"""
import os
import re

import comun
from comun import AVISO, Hallazgo, leer, relativo

# Las mismas carpetas que `enlaces.validar_indices` comprueba.
_TITULO = re.compile(r"(?m)^#\s+(.+?)\s*$")

# Se pone al final de la descripción provisional. Quien la afine, la borra.
POR_AFINAR = "— (por describir)"


def titulo_de(ruta):
    """El primer encabezado `#` del archivo, o su nombre si no tiene."""
    try:
        m = _TITULO.search(leer(ruta))
    except OSError:
        return os.path.basename(ruta)[:-3]
    return m.group(1).strip() if m else os.path.basename(ruta)[:-3]


def faltantes(carpeta):
    """Los `.md` de la carpeta que su `README.md` no menciona."""
    indice = os.path.join(carpeta, "README.md")
    if not os.path.isfile(indice):
        return []
    texto = leer(indice)
    salida = []
    for nombre in sorted(os.listdir(carpeta)):
        if not nombre.lower().endswith(".md") or nombre == "README.md":
            continue
        if "(%s)" % nombre in texto or "/%s)" % nombre in texto:
            continue
        salida.append(nombre)
    return salida


def _linea(carpeta_rel, nombre, ruta):
    """La línea del índice, con el texto que pide `13·DOC14`."""
    return "- [%s/%s](%s) %s %s\n" % (carpeta_rel, nombre, nombre,
                                      POR_AFINAR, titulo_de(ruta))


def completar(raiz=None, carpetas=None, escribir=False):
    """Agrega la línea que falte en cada índice. `[(indice, cuántas)]`.

    Sin `escribir` solo simula, como el resto de los reparadores de esta casa.
    """
    raiz = raiz or comun.RAIZ
    import enlaces
    tocados = []

    for rel in (carpetas or enlaces.CON_INDICE):
        carpeta = os.path.join(raiz, rel)
        faltan = faltantes(carpeta)
        if not faltan:
            continue
        indice = os.path.join(carpeta, "README.md")
        texto = leer(indice)
        nuevas = "".join(_linea(rel, n, os.path.join(carpeta, n)) for n in faltan)
        if escribir:
            with open(indice, "w", encoding="utf-8", newline="\n") as f:
                f.write(texto.rstrip() + "\n" + nuevas)
        tocados.append((indice, len(faltan)))
    return tocados


def validar(raiz=None, carpetas=None):
    """Avisa de las líneas por afinar. **No repite lo que ya dice `enlaces`.**

    Que falte una línea lo reporta `validar.py estandar` como falla. Lo que se
    avisa acá es lo contrario: la línea que **este programa escribió** y nadie
    terminó de redactar. Sin esto, la descripción provisional se queda para
    siempre y el índice deja de decir algo.
    """
    raiz = raiz or comun.RAIZ
    import enlaces
    hallazgos = []
    for rel in (carpetas or enlaces.CON_INDICE):
        indice = os.path.join(raiz, rel, "README.md")
        if not os.path.isfile(indice):
            continue
        cuantas = leer(indice).count(POR_AFINAR)
        if cuantas:
            hallazgos.append(Hallazgo(
                AVISO, indice, 0,
                f"{cuantas} línea(s) con la descripción provisional «{POR_AFINAR}» "
                f"— la puso el generador y hay que reemplazarla por qué es y "
                f"para qué sirve"))
    return hallazgos


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("indices")
