# -*- coding: utf-8 -*-
"""Parte una transcripción en turnos. **No sabe el formato: lo sabe el estándar.**

Este archivo es un puente hacia `validadores/historico.py`, que es **el módulo
que escribe** las transcripciones y por eso es el que sabe leerlas.

**Por qué un puente y no una copia.** Copiar acá las expresiones que reconocen
un turno dejaría dos verdades que empiezan iguales: el día que el enganche
cambie una marca, la copia vieja indexaría mal **sin decir nada**. Es el mismo
argumento —y el mismo molde— de [`seguridad/claves.py`](../seguridad/claves.py),
que tampoco reconoce las claves: se las pide al estándar.

**Si el estándar no está, revienta.** Devolver cero turnos se leería igual que
«esa sesión no tenía nada», y el índice quedaría vacío pareciendo completo.
"""
import os
import sys

from django.conf import settings


class NoHayConQueLeer(Exception):
    """No se encontró el lector de transcripciones del estándar."""


def _lector():
    ruta = str(settings.CARPETA_VALIDADORES)
    if not os.path.isdir(ruta):
        raise NoHayConQueLeer(
            "No está la carpeta de validadores del estándar: %s" % ruta)
    if ruta not in sys.path:
        sys.path.insert(0, ruta)
    try:
        import historico
    except ImportError as falla:
        raise NoHayConQueLeer(
            "No se pudo cargar el lector del estándar: %s" % falla)
    if not hasattr(historico, "turnos"):
        raise NoHayConQueLeer(
            "El estándar instalado no sabe partir una transcripción en turnos: "
            "le falta `historico.turnos`")
    return historico


def turnos(texto):
    """`[(quién, cuándo, lo dicho)]` de una transcripción, en orden."""
    if not texto:
        return []
    return _lector().turnos(texto)
