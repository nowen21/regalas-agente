# -*- coding: utf-8 -*-
"""Qué versión del estándar declara un proyecto, y si esa versión existe.

**Nada de esto se reconoce acá: ya lo sabe hacer el estándar.** Es un puente
hacia `validadores/version.py`, igual que [claves.py](claves.py) lo es hacia el
enmascarador.

**Por qué importa comprobar contra el registro de cambios y no contra
`VERSION`.** `VERSION` dice cuál es la última, y la pregunta es otra: si el
número que un proyecto declara **existió alguna vez**. Un número inventado
mayor que el real pasaría la comparación con la vigente y apagaría el aviso de
desfase en vez de dispararlo. Es el pendiente 82, ya resuelto allá.
"""
import io
import os

from django.conf import settings


class NoHayConQueComprobar(Exception):
    """No está el lector de versiones del estándar."""


def _lector():
    import sys
    ruta = str(settings.CARPETA_VALIDADORES)
    if not os.path.isdir(ruta):
        raise NoHayConQueComprobar(
            "No está la carpeta de validadores del estándar: %s" % ruta)
    if ruta not in sys.path:
        sys.path.insert(0, ruta)
    try:
        import version
    except ImportError as falla:
        raise NoHayConQueComprobar(
            "No se pudo cargar el lector de versiones: %s" % falla)
    return version


def declarada_por(ruta_del_proyecto):
    """La versión que el `CLAUDE.md` del proyecto declara, o "" si no declara.

    Vacío no es un error: un proyecto que todavía no instaló el estándar se
    conecta igual, con su aviso. Decidido con el usuario el 2026-08-25.
    """
    archivo = os.path.join(ruta_del_proyecto, "CLAUDE.md")
    if not os.path.isfile(archivo):
        return ""
    with io.open(archivo, encoding="utf-8", errors="replace") as abierto:
        return _lector().extraer_adoptada(abierto.read()) or ""


def existe(version_declarada):
    """Dice si esa versión aparece en el registro de cambios del estándar."""
    if not version_declarada:
        return True          # no declarar nada no es declarar algo falso
    return version_declarada in _lector().versiones_publicadas(
        str(settings.CARPETA_VALIDADORES.parent))


def quedo_atras(version_declarada):
    """El motivo del desfase, o "" si está al día o no declara nada."""
    if not version_declarada:
        return ""
    return _lector().comparar(version_declarada,
                              _lector().version_estandar()) or ""
