#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cargas sin límite — `06·R2`.

R2: listas paginadas, procesar por lotes, y traer **solo las columnas
necesarias** (nada de `SELECT *` para tres campos).

De las tres, la única detectable sin criterio es `SELECT *`: la paginación y el
chunking dependen del contexto de cada pantalla y se quedan como juicio humano.
Aquí se marca el `SELECT *` explícito, que es señal de traer de más.

Multiproyecto: es SQL, universal a cualquier stack. **AVISO**: un `SELECT *`
puntual puede ser legítimo (un `EXISTS`, un conteo); lo confirma un humano.
"""
import re

import codigo
from comun import AVISO, Hallazgo

_SELECT_ESTRELLA = re.compile(r"(?i)\bSELECT\s+\*")


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: marca cada `SELECT *`. Aislado de git para probarlo."""
    if hallazgos is None:
        hallazgos = []
    for m in _SELECT_ESTRELLA.finditer(texto):
        hallazgos.append(Hallazgo(
            AVISO, donde, codigo.linea_de(texto, m.start()),
            "`SELECT *` — R2 pide traer solo las columnas necesarias"))
    return hallazgos


def validar(raiz):
    hallazgos = []
    for donde, texto in codigo.archivos(raiz):
        revisar_texto(texto, donde, hallazgos)
    return hallazgos
