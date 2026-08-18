#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Funciones pequeñas — `07·Q3`.

Q3: cada función hace **una cosa**. La parte comprobable sin criterio es la
**longitud**: una función muy larga casi siempre hace varias cosas. No mide
"responsabilidad única" (eso es juicio); mide líneas, como señal para revisar.

El umbral (`TOPE`) no es sagrado: marca lo que conviene mirar, no un incumplimiento.
Por eso es **AVISO**.

Multiproyecto: cubre funciones con llaves y palabra `function` (PHP/JS) y `def`
de Python. Los métodos de lenguajes sin `function` (Java/C#) quedan fuera por ahora.
"""
import re

import codigo
import comun
from comun import AVISO, Hallazgo

TOPE = 60       # líneas de cuerpo; por encima, se señala para revisar

_FUNC_LLAVES = re.compile(r"\bfunction\b[^\n;(]*\([^;{]*\)\s*(?::\s*[\w\\|?]+\s*)?\{")
_DEF_PYTHON = re.compile(r"^(\s*)def\s+\w+\s*\(")


def _cuerpo_llaves(texto, abre):
    """Del `{` en `abre` a su `}` pareja; devuelve el texto del cuerpo."""
    prof, k = 0, abre
    while k < len(texto):
        if texto[k] == "{":
            prof += 1
        elif texto[k] == "}":
            prof -= 1
            if prof == 0:
                return texto[abre:k + 1]
        k += 1
    return texto[abre:]


def _largo_cuerpo_python(lineas, desde, sangria):
    n = 0
    for linea in lineas[desde:]:
        if not linea.strip():
            continue
        if len(linea) - len(linea.lstrip()) <= sangria:
            break
        n += 1
    return n


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: marca funciones cuyo cuerpo pasa de `TOPE` líneas."""
    if hallazgos is None:
        hallazgos = []

    for m in _FUNC_LLAVES.finditer(texto):
        abre = texto.find("{", m.start())
        largo = _cuerpo_llaves(texto, abre).count("\n") - 1     # sin la línea del `}`
        if largo > TOPE:
            hallazgos.append(Hallazgo(
                AVISO, donde, codigo.linea_de(texto, m.start()),
                f"función de ~{largo} líneas (tope {TOPE}) — Q3: una función, una cosa"))

    lineas = texto.splitlines()
    for i, linea in enumerate(lineas):
        md = _DEF_PYTHON.match(linea)
        if md:
            largo = _largo_cuerpo_python(lineas, i + 1, len(md.group(1)))
            if largo > TOPE:
                hallazgos.append(Hallazgo(
                    AVISO, donde, i + 1,
                    f"función de ~{largo} líneas (tope {TOPE}) — Q3: una función, una cosa"))
    return hallazgos


def validar(raiz):
    hallazgos = []
    for donde, texto in codigo.archivos(raiz):
        revisar_texto(texto, donde, hallazgos)
    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("calidad")
