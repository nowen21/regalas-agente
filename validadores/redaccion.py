#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lo que se puede medir sobre lo que el agente acaba de escribir — `00·ID10`.

**Por qué existe.** Tres reglas del núcleo hablan de cómo escribe el agente:
[`ID8`](../base/00-identidad-y-rol/reglas/ID8-escribe-sin-las-marcas-que-delatan-generacion-automatica.md)
las marcas de escritura automática, [`ID9`](../base/00-identidad-y-rol/reglas/ID9-di-lo-mismo-en-menos-palabras.md)
cuánto ocupa, e [`ID10`](../base/00-identidad-y-rol/reglas/ID10-escribe-en-el-idioma-del-proyecto-en-tercera-persona-y-en-infinitivo.md)
la persona y la forma verbal. Las tres dependían de que el agente se acordara.

**Lo que este módulo mide, y lo que no.** Lo suyo es el **trato**: «usted»,
«tú» y sus formas, que `ID10` descarta sin discusión. Las otras dos cifras no
se cuentan aquí: las marcas las cuenta `marcas.py` y el largo lo compara con el
umbral de `brevedad.py`, cada uno donde ya vivía. Lo que este módulo agrega es
juntarlas en una línea sobre **un** texto — el que se acaba de escribir.

**Lo que no mide.** Ni la variedad del idioma ni si un imperativo es de verdad un
imperativo: eso pide leer, y prometerlo sería el defecto que esta casa persigue
— un número que el lector completa con lo que quiere creer (`S-091`).

**Mide y no detiene**, que es lo que la historia acepta como forma de hacer
cumplir **si la medición queda a la vista** (`RN-05` de `EP-005·HU-012`). Por eso
el resultado se imprime al cerrar cada turno y no espera a que alguien lo pida.
"""
import re

import brevedad
import comun
import marcas
from comun import RAIZ                                       # noqa: F401

# El trato directo, en las formas que aparecen de verdad al escribir. La lista
# es corta a propósito: cada una se reconoce sin contexto, y una que necesite
# contexto no se cuenta, se lee.
_TRATO = re.compile(
    r"(?i)(?<![\w-])(usted(?:es)?|t[úu]|ti|tuyos?|tuyas?|contigo|"
    r"vosotros|os)(?![\w-])")

# Lo que cita la pantalla o al usuario no es redacción del agente: `ID10` lo
# dice de frente. Se saltan las comillas de cita y los bloques de código.
_CITA = re.compile(r"[«\"'][^«»\"']*[»\"']")


def _sin_citas(linea):
    """La línea sin lo citado ni lo que va en código."""
    return _CITA.sub(" ", comun.sin_codigo_en_linea(linea))


def tratos(texto):
    """`[(línea, palabra)]` de cada trato directo fuera de una cita."""
    salida = []
    cercado = False
    for n, linea in enumerate(texto.split("\n"), 1):
        if linea.lstrip().startswith("```") or linea.lstrip().startswith("~~~"):
            cercado = not cercado
            continue
        if cercado:
            continue
        for m in _TRATO.finditer(_sin_citas(linea)):
            salida.append((n, m.group(1)))
    return salida


def medir(texto):
    """`{"caracteres","tratos","marcas"}` de una respuesta del agente.

    Las tres cifras salen de leer el texto una sola vez, y cada una nombra la
    regla que mide. Ninguna decide nada: el que decide es quien las lee.
    """
    cercado, cuantas = False, 0
    for linea in texto.split("\n"):
        if linea.lstrip().startswith("```") or linea.lstrip().startswith("~~~"):
            cercado = not cercado
            continue
        if cercado:
            continue
        cuantas += len(marcas.marcas_de_linea(marcas.sin_codigo_en_linea(linea)))
    return {"caracteres": len(texto.strip()),
            "tratos": tratos(texto),
            "marcas": cuantas}


def linea_de_cierre(texto, mediana=0):
    """La línea que el enganche imprime, o `""` si no hay nada que decir.

    **Se calla cuando todo está bien.** Un aviso que sale en cada turno deja de
    leerse a la tercera, y entonces tampoco se lee el que sí importaba.
    """
    m = medir(texto)
    partes = []
    if m["marcas"]:
        partes.append("%d marca(s) de `00·ID8`" % m["marcas"])
    if m["tratos"]:
        cuales = sorted({p.lower() for _n, p in m["tratos"]})
        partes.append("trato directo de `00·ID10`: %s" % ", ".join(cuales))
    if m["caracteres"] > brevedad.HOLGADO:
        cuanto = "%d caracteres (holgado: %d)" % (m["caracteres"],
                                                  brevedad.HOLGADO)
        if mediana:
            cuanto += ", mediana de la sesión %d" % mediana
        partes.append("`00·ID9`: " + cuanto)
    if not partes:
        return ""
    return "[redacción] " + " · ".join(partes)


if __name__ == "__main__":
    comun.no_es_punto_de_entrada("redaccion")
