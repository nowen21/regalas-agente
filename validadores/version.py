#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desfase de versión del estándar — `pendiente 04`.

Compara la versión de `base/`+`plantillas/` (el archivo `VERSION` del estándar)
con la que **declara** el proyecto en su `CLAUDE.md` (capa 3). Si el proyecto
quedó por detrás, **avisa** — no migra: subir de versión es decisión del usuario,
y las fases ya cerradas quedan selladas con su versión (regla de retroactividad).

Todo **AVISO**: un desfase no es un incumplimiento, es una señal para decidir.
"""
import os
import re

from comun import AVISO, Hallazgo, RAIZ, leer

# Acepta 'X.Y.Z' en la línea "Versión del estándar adoptada: X.Y.Z".
_ADOPTADA = re.compile(
    r"(?i)versi[oó]n\s+del\s+est[aá]ndar\s+adoptada[^\n]*?(\d+\.\d+\.\d+)")


def _tupla(v):
    return tuple(int(x) for x in v.split("."))


def version_estandar():
    """La versión del estándar (primer renglón de `VERSION`), o None."""
    try:
        cabeza = leer(os.path.join(RAIZ, "VERSION")).strip().splitlines()
        return cabeza[0].strip() if cabeza else None
    except OSError:
        return None


def extraer_adoptada(texto):
    """La versión que el `CLAUDE.md` declara adoptada, o None (o sin llenar)."""
    m = _ADOPTADA.search(texto)
    return m.group(1) if m else None


def comparar(adoptada, estandar):
    """Núcleo puro: motivo del desfase, o None si está al día. Aislado de disco."""
    if not estandar:
        return None                             # el estándar sin VERSION: nada que comparar
    if not adoptada:
        return (f"el proyecto no declara qué versión del estándar sigue "
                f"(el estándar va en v{estandar}) — fijarla en su CLAUDE.md")
    if _tupla(adoptada) < _tupla(estandar):
        return (f"el proyecto declara v{adoptada}, el estándar va en v{estandar}: "
                f"subir es decisión del usuario; las fases cerradas quedan selladas")
    return None


def validar(raiz):
    raiz = os.path.abspath(raiz)
    est = version_estandar()
    claude = os.path.join(raiz, "CLAUDE.md")
    if not os.path.isfile(claude):
        return [Hallazgo(AVISO, raiz, 0,
                         "no se encontró CLAUDE.md; no se puede leer la versión adoptada")]
    motivo = comparar(extraer_adoptada(leer(claude)), est)
    return [Hallazgo(AVISO, "CLAUDE.md", 0, motivo)] if motivo else []
