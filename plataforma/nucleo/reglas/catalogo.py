# -*- coding: utf-8 -*-
"""Qué reglas tiene un proyecto. **Puente hacia el estándar, no copia.**

El estándar ya sabe leer su propio cuerpo de reglas: las parte por capítulo,
les saca el identificador, y distingue la derogada de la vigente y la blindada
de la común. Copiar eso acá dejaría dos lectores que se separan, y el día que
el formato cambie uno de los dos va a leer mal sin avisar.

**Es el cuarto puente de la plataforma hacia el estándar**, después del que tapa
credenciales, el que parte una conversación en turnos y el que corre las
comprobaciones. Ya no es una excepción: es la forma.
"""
import os
import sys

from django.conf import settings


class NoHayCuerpoDeReglas(Exception):
    """No se encontró el lector de reglas del estándar."""


def _lector():
    ruta = str(settings.CARPETA_VALIDADORES)
    if not os.path.isdir(ruta):
        raise NoHayCuerpoDeReglas(
            "No está la carpeta de validadores del estándar: %s" % ruta)
    if ruta not in sys.path:
        sys.path.insert(0, ruta)
    try:
        import metareglas
    except ImportError as falla:
        raise NoHayCuerpoDeReglas(
            "No se pudo cargar el lector de reglas del estándar: %s" % falla)
    return metareglas


def todas(raiz):
    """Todas las reglas de ese proyecto, vigentes y derogadas.

    **Las derogadas también salen**, y tiene que ser así: su identificador
    sigue ocupado para siempre, y una cita escrita hace un año todavía apunta
    ahí.
    """
    return _lector().reglas(raiz)


def por_prefijo(raiz):
    """`{prefijo: [reglas]}`, con las derogadas adentro."""
    agrupadas = {}
    for una in todas(raiz):
        agrupadas.setdefault(una.prefijo, []).append(una)
    return agrupadas


def vigentes(raiz):
    """Las que todavía rigen."""
    return [una for una in todas(raiz) if not una.derogada]


def resumen(raiz):
    """Cuántas hay, cuántas derogadas y cuántas blindadas."""
    reglas = todas(raiz)
    return {
        "todas": len(reglas),
        "vigentes": sum(1 for una in reglas if not una.derogada),
        "derogadas": sum(1 for una in reglas if una.derogada),
        "blindadas": sum(1 for una in reglas if una.blindada),
        "prefijos": len(set(una.prefijo for una in reglas)),
    }
