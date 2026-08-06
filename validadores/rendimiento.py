#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rendimiento — `06·R2` y `06·R1`.

R2: traer **solo las columnas necesarias** (nada de `SELECT *`). La paginación y
el chunking dependen del contexto de cada pantalla y quedan como juicio humano.

R1: no ejecutar **una consulta por cada elemento** de una lista (N+1). Detectable
solo el caso explícito: una llamada de consulta ejecutora (`->get()`, `::find(`,
`.objects.filter(`…) **dentro de un bucle**. El caso clásico —acceder a una
relación lazy en el bucle (`$factura->cliente->nombre`)— no se puede ver
estáticamente (no hay llamada visible), así que ese queda para el ojo humano.

Multiproyecto: `SELECT *` es universal; el N+1 cubre bucles con llaves (PHP/JS/
Java…) y con indentación (Python). Todo **AVISO**: puede ser una sola consulta
construida en partes, o un caso legítimo; lo confirma un humano.
"""
import re

import codigo
from comun import AVISO, Hallazgo

_SELECT_ESTRELLA = re.compile(r"(?i)\bSELECT\s+\*")

# Bucle con llaves (PHP/JS/Java/C#…) e inicio de bucle Python.
_BUCLE_LLAVES = re.compile(r"\b(foreach|for|while)\b\s*\(")
_BUCLE_PYTHON = re.compile(r"^(\s*)(for|while)\b.*:\s*(#.*)?$")

# Consulta que **ejecuta** contra la BD (no solo arma). Dentro de un bucle = N+1.
_CONSULTA = re.compile(
    r"->\s*(get|first|firstOrFail|find|findOrFail|value|pluck|count|exists|sum|avg|max|min|paginate)\s*\(|"
    r"::\s*(find|findOrFail|first|firstWhere|count)\s*\(|"
    r"\bDB::\s*(select|table|statement|insert|update|delete|scalar)\b|"
    r"\.objects\.\s*(get|filter|all|first|count|exists)\b|"
    r"\.(query|execute|fetchall|fetchone)\s*\(")


def _cuerpo_llaves(texto, desde):
    """Cuerpo `{...}` de un bucle: salta el `(...)` de condición y equilibra `{}`.
    Devuelve (cuerpo, fin) o (None, desde) si no hay bloque con llaves."""
    i, prof = desde, 0
    while i < len(texto):                       # salta la condición ( ... )
        if texto[i] == "(":
            prof += 1
        elif texto[i] == ")":
            prof -= 1
            if prof == 0:
                break
        i += 1
    j = i + 1
    while j < len(texto) and texto[j] in " \t\r\n":
        j += 1
    if j >= len(texto) or texto[j] != "{":
        return None, desde
    prof, k = 0, j
    while k < len(texto):
        if texto[k] == "{":
            prof += 1
        elif texto[k] == "}":
            prof -= 1
            if prof == 0:
                break
        k += 1
    return texto[j:k], k


def _cuerpo_python(lineas, desde, sangria):
    """Líneas del bloque indentado bajo un `for/while` de Python (más sangría)."""
    cuerpo = []
    for linea in lineas[desde:]:
        if not linea.strip():
            cuerpo.append(linea)
            continue
        actual = len(linea) - len(linea.lstrip())
        if actual <= sangria:
            break
        cuerpo.append(linea)
    return "\n".join(cuerpo)


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: `SELECT *` (R2) y consultas en bucle (R1)."""
    if hallazgos is None:
        hallazgos = []

    for m in _SELECT_ESTRELLA.finditer(texto):
        hallazgos.append(Hallazgo(
            AVISO, donde, codigo.linea_de(texto, m.start()),
            "`SELECT *` — R2 pide traer solo las columnas necesarias"))

    # R1 · bucles con llaves.
    for m in _BUCLE_LLAVES.finditer(texto):
        cuerpo, _ = _cuerpo_llaves(texto, m.end() - 1)
        if cuerpo and _CONSULTA.search(cuerpo):
            hallazgos.append(Hallazgo(
                AVISO, donde, codigo.linea_de(texto, m.start()),
                "consulta dentro de un bucle — R1: posible N+1 (usar eager loading)"))

    # R1 · bucles Python por indentación.
    lineas = texto.splitlines()
    for i, linea in enumerate(lineas):
        mb = _BUCLE_PYTHON.match(linea)
        if mb and _CONSULTA.search(_cuerpo_python(lineas, i + 1, len(mb.group(1)))):
            hallazgos.append(Hallazgo(
                AVISO, donde, i + 1,
                "consulta dentro de un bucle — R1: posible N+1 (usar eager loading)"))
    return hallazgos


def validar(raiz):
    hallazgos = []
    for donde, texto in codigo.archivos(raiz):
        revisar_texto(texto, donde, hallazgos)
    return hallazgos
