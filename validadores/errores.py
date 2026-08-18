#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Errores y logging — `05·E1` y `05·E5`.

E1: un error capturado se maneja **visible y trazable**; nada de `catch` vacío.
La parte comprobable es el caso extremo: un bloque de captura literalmente
**vacío**. No se juzga si el manejo es "suficiente" (eso es humano).

E5: los logs **nunca** llevan secretos ni datos sensibles. La parte comprobable
es una llamada de log que menciona un campo con nombre de secreto
(`password`, `token`, `cvv`…). No se juzga si va enmascarado; se señala para mirar.

Multiproyecto: cubre las formas más comunes sin asumir framework — captura con
llaves (`catch (…) {}`), `except …: pass` (Python), y llamadas de log de PHP/JS/
Python. Todo **AVISO**: puede ser deliberado y estar bien; lo confirma un humano.
"""
import re

import codigo
import comun
from comun import AVISO, Hallazgo

# E1 · `catch (...) {}` o `catch {}` (JS) con el cuerpo vacío. \s abarca saltos
# de línea, así que atrapa el vacío repartido en varias líneas.
_CATCH_LLAVES = re.compile(r"catch\s*(?:\([^)]*\))?\s*\{\s*\}")

# E1 · Python: `except ...:` cuyo único cuerpo es `pass` (misma línea o la siguiente).
_EXCEPT_PASS = re.compile(r"except\b[^:\n]*:[ \t]*(?:\r?\n[ \t]*)?pass\b")

# E5 · una llamada de log y, en la misma línea, un campo con pinta de secreto.
_LOG = re.compile(
    r"(?i)(console\.(log|error|warn|info|debug)|Log::\w+|\blogger\.\w+|"
    r"\blogging\.\w+|\blog\.\w+|\blogger\s*\(|error_log\s*\()")
_SENSIBLE = re.compile(
    r"(?i)\b(pass(?:word|wd)?|contrase\w+|secret|token|api[_-]?key|apikey|"
    r"authorization|cvv|tarjeta|card[_-]?number|numero_tarjeta)\b")


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: marca capturas vacías (E1) y logs de secretos (E5)."""
    if hallazgos is None:
        hallazgos = []
    for patron, forma in ((_CATCH_LLAVES, "catch"), (_EXCEPT_PASS, "except: pass")):
        for m in patron.finditer(texto):
            hallazgos.append(Hallazgo(
                AVISO, donde, codigo.linea_de(texto, m.start()),
                f"captura de error vacía (`{forma}`) — E1 pide manejo visible y trazable"))
    for n, linea in enumerate(texto.splitlines(), 1):
        if _LOG.search(linea) and _SENSIBLE.search(linea):
            hallazgos.append(Hallazgo(
                AVISO, donde, n,
                "posible secreto en un log — E5: los logs no llevan contraseñas/tokens"))
    return hallazgos


def validar(raiz):
    hallazgos = []
    for donde, texto in codigo.archivos(raiz):
        revisar_texto(texto, donde, hallazgos)
    return hallazgos


if __name__ == "__main__":
    # `53` · Un modulo que se ejecuta solo y no imprime nada dice, con su
    # silencio, lo mismo que diria si hubiera comprobado y estuviera todo bien.
    comun.no_es_punto_de_entrada("errores")
