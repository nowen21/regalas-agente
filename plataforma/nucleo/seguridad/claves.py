# -*- coding: utf-8 -*-
"""Tapa las claves. **No las reconoce: eso ya lo sabe hacer el estándar.**

Este archivo es un puente de tres líneas hacia `validadores/enmascarar.py`, que
lleva ocho formas de secreto de proveedor, la clave entre comillas y la pegada
sin ellas, y sabe **no** tapar los moldes (`tu-clave`, `changeme`) ni la línea
que lee del entorno.

**Por qué un puente y no una copia.** Copiarlo dejaría dos listas de secretos
que se separan, y la que quede vieja va a dejar pasar una clave el día que
aparezca una forma nueva. Lo advierte el propio archivo del estándar.

**Por qué no se movió el archivo a un sitio compartido.** Se evaluó: mover
obliga a tocar `validadores/`, que hoy funciona, y eso es cambio del estándar
con su versión y su registro. No compra nada que este puente no dé ya. Queda
como riesgo aceptado en el plan de la fase: el día que la plataforma y el
estándar vivan en repositorios distintos, esto es lo primero que hay que mover.
"""
import os
import sys

from django.conf import settings


class NoHayConQueTapar(Exception):
    """No se encontró el enmascarador del estándar. Sin él no se escribe nada."""


def _enmascarador():
    ruta = str(settings.CARPETA_VALIDADORES)
    if not os.path.isdir(ruta):
        raise NoHayConQueTapar(
            "No está la carpeta de validadores del estándar: %s" % ruta)
    if ruta not in sys.path:
        sys.path.insert(0, ruta)
    try:
        import enmascarar
    except ImportError as falla:
        raise NoHayConQueTapar(
            "No se pudo cargar el enmascarador del estándar: %s" % falla)
    return enmascarar


def tapar(texto):
    """Devuelve el texto con las claves tapadas, y cuántas se taparon.

    Si el enmascarador no está, **revienta en vez de devolver el texto tal
    cual**: escribir sin tapar es el daño que esto viene a evitar (`00·N6`).
    """
    if not texto:
        return texto, 0
    return _enmascarador().enmascarar(texto)
