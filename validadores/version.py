#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Desfase de versión del estándar — `pendiente 04`.

Compara la versión de `base/`+`plantillas/` (el archivo `VERSION` del estándar)
con la que **declara** el proyecto en su `CLAUDE.md` (capa 3). Si el proyecto
quedó por detrás, **avisa** — no migra: subir de versión es decisión del usuario,
y las fases ya cerradas quedan selladas con su versión (regla de retroactividad).

El desfase a secas es **AVISO**: no es un incumplimiento, es una señal para
decidir. Con una sola excepción, y es `02·F22`: si en ese desfase hay una regla
**derogada** sin adoptar, el proyecto no abre ni cierra fase, y eso sí es
**FALLA**. Esa parte la comprueba `validar_fase`, que llama `flujo.py` porque es
el que recorre las fases.
"""
import os
import re

from comun import AVISO, FALLA, Hallazgo, RAIZ, leer

# Acepta 'X.Y.Z' en la línea "Versión del estándar adoptada: X.Y.Z".
_ADOPTADA = re.compile(
    r"(?i)versi[oó]n\s+del\s+est[aá]ndar\s+adoptada[^\n]*?(\d+\.\d+\.\d+)")

# El encabezado de una regla derogada: '## F6 · … · `[DEROGADA en 4.0.0 → ver 13·DOC1]`'
# (`20·M11`). Solo se mira la línea del encabezado: las tablas de los índices y
# los ejemplos del molde repiten la marca y no son reglas.
_ENCABEZADO_DEROGADA = re.compile(
    r"^##\s+(\S+)\s*·[^\n]*?\[DEROGADA\s+en\s+(\d+\.\d+\.\d+)\s*(?:→|->)\s*ver\s+([^\]`]+)\]",
    re.M)


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


def derogaciones(base=None):
    """Las reglas derogadas del estándar: `[(versión, regla, reemplazo)]`.

    Se leen de la marca del encabezado de cada regla (`20·M11`), que es dato
    estructurado. El `CHANGELOG.md` es prosa: nombrar la palabra "derogación"
    ahí no significa que se haya derogado nada.
    """
    base = base or os.path.join(RAIZ, "base")
    encontradas = []
    for carpeta, subcarpetas, archivos in os.walk(base):
        subcarpetas[:] = [s for s in subcarpetas if not s.startswith(".")]
        for nombre in archivos:
            if not nombre.endswith(".md"):
                continue
            try:
                texto = leer(os.path.join(carpeta, nombre))
            except OSError:
                continue
            for regla, version, reemplazo in _ENCABEZADO_DEROGADA.findall(texto):
                entrada = (version, regla, reemplazo.strip())
                if entrada not in encontradas:
                    encontradas.append(entrada)
    return sorted(encontradas, key=lambda e: (_tupla(e[0]), e[1]))


def sin_adoptar(adoptada, estandar, derogadas):
    """Núcleo puro: las derogaciones que caen dentro del desfase. Aislado de disco.

    Cuenta la derogación publicada **después** de la versión que el proyecto
    declara y hasta la vigente. Sin versión adoptada no se puede decidir: se
    devuelve vacío y el desfase lo reporta `validar` como aviso.
    """
    if not adoptada or not estandar:
        return []
    desde, hasta = _tupla(adoptada), _tupla(estandar)
    return [d for d in derogadas if desde < _tupla(d[0]) <= hasta]


def validar(raiz):
    raiz = os.path.abspath(raiz)
    est = version_estandar()
    claude = os.path.join(raiz, "CLAUDE.md")
    if not os.path.isfile(claude):
        return [Hallazgo(AVISO, raiz, 0,
                         "no se encontró CLAUDE.md; no se puede leer la versión adoptada")]
    motivo = comparar(extraer_adoptada(leer(claude)), est)
    return [Hallazgo(AVISO, "CLAUDE.md", 0, motivo)] if motivo else []


def validar_fase(raiz):
    """`02·F22` — con una derogación sin adoptar, el proyecto no avanza de fase.

    Lo llama `flujo.py`, que es el que recorre las fases: la comprobación se
    cobra al abrir y al cerrar una fase, no en cualquier momento.
    """
    raiz = os.path.abspath(raiz)
    claude = os.path.join(raiz, "CLAUDE.md")
    if not os.path.isfile(claude):
        return []
    pendientes = sin_adoptar(extraer_adoptada(leer(claude)),
                             version_estandar(), derogaciones())
    if not pendientes:
        return []
    detalle = " · ".join(f"{regla} (derogada en {ver} → {reemplazo})"
                         for ver, regla, reemplazo in pendientes)
    return [Hallazgo(
        FALLA, "CLAUDE.md", 0,
        f"hay derogaciones sin adoptar y ninguna fase se abre ni se cierra hasta "
        f"adoptarlas (F22): {detalle}. Se abre una fase por cada HU que implementaba "
        f"la regla derogada, y al cerrarla se sube la versión declarada")]
