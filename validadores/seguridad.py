#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Concatenación, inyección y flags de sesión — `04·S3` y `04·S5`.

S3 prohíbe construir consultas o comandos pegando entrada:
  BD    · consultas parametrizadas / ORM; nunca concatenar en la consulta.
  Shell · no armar comandos con entrada; separar comando y argumentos.
  Masiva· declarar qué campos son asignables; no volcar todo el payload al modelo.

S5 (parte comprobable): las cookies de sesión llevan `HttpOnly` y `Secure`; se
marca cuando alguien los **apaga** (`'http_only' => false`). El resto de S5
(CSRF, HTTPS, hashing) depende del contexto y queda como juicio humano.

Multiproyecto: los patrones son de PHP/JS/Python. Todo **AVISO** y **heurístico**:
una cadena SQL con un nombre de tabla fijo no es inyección; lo confirma un humano.
"""
import re

import codigo
from comun import AVISO, Hallazgo

# SQL de verdad: la cadena **empieza** con un verbo de consulta (no "select"
# suelto dentro de "form-select") y se concatena con una **variable** (no el
# punto de una frase en un comentario).
_SQL_EN_CADENA = re.compile(
    r"(?i)['\"]\s*(SELECT|INSERT\s+INTO|UPDATE|DELETE\s+FROM|REPLACE\s+INTO)\b")
_CONCAT_VAR = re.compile(r"['\"]\s*\.\s*\$\w|\$\w+\s*\.\s*['\"]|['\"]\s*\+\s*\w")

# Llamada a shell, y en la misma línea una concatenación o interpolación.
_SHELL = re.compile(
    r"\b(exec|shell_exec|system|passthru|popen|proc_open)\s*\(|"
    r"\bos\.system\s*\(|\bsubprocess\.\s*(call|run|Popen)\s*\(")
_CONCAT_O_INTERP = re.compile(r"[.+]\s*\$?\w|f['\"]|\$\{")

# Asignación masiva sin freno.
_GUARDED_VACIO = re.compile(r"\$guarded\s*=\s*\[\s*\]")
_TODO_AL_MODELO = re.compile(
    r"(->|::)\s*(create|update|fill|forceCreate|forceFill)\s*\(\s*\$\w+->\s*all\(\)")

# S5 · un flag de cookie de sesión apagado a mano.
_COOKIE_INSEGURA = re.compile(
    r"(?i)['\"]?(http_?only|secure|cookie_httponly|cookie_secure)['\"]?\s*(=>|:|=)\s*(false|0)\b")


def revisar_texto(texto, donde="", hallazgos=None):
    """Núcleo puro: marca concatenación SQL/shell y asignación masiva."""
    if hallazgos is None:
        hallazgos = []

    for n, linea in enumerate(texto.splitlines(), 1):
        if _SQL_EN_CADENA.search(linea) and _CONCAT_VAR.search(linea):
            hallazgos.append(Hallazgo(
                AVISO, donde, n,
                "consulta SQL armada por concatenación — S3: usar parámetros/ORM"))
        if _SHELL.search(linea) and _CONCAT_O_INTERP.search(linea):
            hallazgos.append(Hallazgo(
                AVISO, donde, n,
                "comando de shell armado con entrada — S3: separar comando y argumentos"))

    for patron, motivo in (
        (_GUARDED_VACIO, "asignación masiva sin freno (`$guarded = []`) — S3"),
        (_TODO_AL_MODELO, "todo el payload al modelo (`->…($req->all())`) — S3: declarar asignables"),
        (_COOKIE_INSEGURA, "flag de cookie de sesión apagado (`HttpOnly`/`Secure`) — S5")):
        for m in patron.finditer(texto):
            hallazgos.append(Hallazgo(
                AVISO, donde, codigo.linea_de(texto, m.start()), motivo))
    return hallazgos


def validar(raiz):
    hallazgos = []
    for donde, texto in codigo.archivos(raiz):
        revisar_texto(texto, donde, hallazgos)
    return hallazgos
