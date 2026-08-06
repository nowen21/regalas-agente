#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Errores tragados en silencio — `05·E1`.

E1: un error capturado se maneja **visible y trazable**; nada de `catch` vacío.

La parte comprobable sin criterio es el caso extremo: un bloque de captura
literalmente **vacío**. No se juzga si el manejo es "suficiente" (eso es humano);
solo se marca el silencio total.

Multiproyecto: cubre las dos formas más comunes sin asumir framework —
lenguajes con llaves (`catch (…) {}`) y Python (`except …: pass`). Todo **AVISO**:
puede haber un `catch` vacío deliberado y comentado; lo confirma un humano.
"""
import re

import codigo
from comun import AVISO, Hallazgo

# `catch (...) {}` o `catch {}` (JS) con el cuerpo vacío. \s abarca saltos de
# línea, así que atrapa el vacío repartido en varias líneas.
_CATCH_LLAVES = re.compile(r"catch\s*(?:\([^)]*\))?\s*\{\s*\}")

# Python: `except ...:` cuyo único cuerpo es `pass` (misma línea o la siguiente).
_EXCEPT_PASS = re.compile(r"except\b[^:\n]*:[ \t]*(?:\r?\n[ \t]*)?pass\b")


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: marca cada captura vacía. Aislado de git para probarlo."""
    if hallazgos is None:
        hallazgos = []
    for patron, forma in ((_CATCH_LLAVES, "catch"), (_EXCEPT_PASS, "except: pass")):
        for m in patron.finditer(texto):
            hallazgos.append(Hallazgo(
                AVISO, donde, codigo.linea_de(texto, m.start()),
                f"captura de error vacía (`{forma}`) — E1 pide manejo visible y trazable"))
    return hallazgos


def validar(raiz):
    hallazgos = []
    for donde, texto in codigo.archivos(raiz):
        revisar_texto(texto, donde, hallazgos)
    return hallazgos
