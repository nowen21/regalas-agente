# -*- coding: utf-8 -*-
"""Si un proyecto quedó atrás, y **qué cambió desde entonces**.

**Decir «estás atrasado» no ayuda a decidir.** Lo que decide es si alguna de las
versiones que pasaron obliga a migrar, cuántas van, y de qué se trataban. Con
eso una persona sabe si sube hoy o la semana que viene; sin eso, el aviso se
ignora.

**Y un número inventado no es estar al día.** Una versión mayor que la real
apagaría el aviso en vez de dispararlo: la comparación diría que va adelante. Se
comprueba contra el registro de cambios, que es donde está lo que existió.

**Todo esto lo sabe el estándar.** Acá se le pregunta y se junta la respuesta.
"""
import os
import sys

from django.conf import settings


class NoHayComoComparar(Exception):
    """No se encontró el lector de versiones del estándar."""


def _lector():
    ruta = str(settings.CARPETA_VALIDADORES)
    if not os.path.isdir(ruta):
        raise NoHayComoComparar(
            "No está la carpeta de validadores del estándar: %s" % ruta)
    if ruta not in sys.path:
        sys.path.insert(0, ruta)
    try:
        import version
    except ImportError as falla:
        raise NoHayComoComparar(
            "No se pudo cargar el lector de versiones del estándar: %s" % falla)
    return version


def _raiz_del_estandar():
    return str(settings.CARPETA_VALIDADORES.parent)


def version_del_estandar():
    """La última versión publicada del estándar."""
    return _lector().version_estandar()


def existe(declarada):
    """Si esa versión aparece en el registro de cambios.

    **No declarar nada no es declarar algo falso**, y por eso lo vacío pasa.
    """
    if not declarada:
        return True
    return declarada in _lector().versiones_publicadas(_raiz_del_estandar())


def que_cambio(declarada):
    """Las versiones que separan a esa de la del estándar.

    Devuelve `[(version, tipo, titulo)]`, de la más nueva a la más vieja.
    """
    lector = _lector()
    return lector.tramo(declarada, lector.version_estandar(),
                        _raiz_del_estandar())


def revisar(declarada):
    """Todo lo que hay que decirle a un proyecto sobre su versión.

    Devuelve `{"al_dia", "existe", "motivo", "cambios", "resumen", "obligan"}`.

    **Las tres respuestas son distintas y se dan distinto:** está al día, quedó
    atrás, o declara una versión que nunca existió. La tercera es la peligrosa,
    porque a simple vista se parece a la primera.
    """
    lector = _lector()
    del_estandar = lector.version_estandar()

    if not existe(declarada):
        return {
            "al_dia": False, "existe": False,
            "motivo": ("este proyecto declara la versión %s, que no aparece en "
                       "el registro de cambios del estándar. **No es que vaya "
                       "adelantado: es que ese número no existió nunca**, y "
                       "mientras siga ahí el aviso de desfase no puede servir."
                       % declarada),
            "cambios": [], "resumen": "", "obligan": []}

    motivo = lector.comparar(declarada, del_estandar) or ""
    if not motivo:
        return {"al_dia": True, "existe": True, "motivo": "", "cambios": [],
                "resumen": "", "obligan": []}

    cambios = que_cambio(declarada)
    obligan = [v for v, tipo, _ in cambios if (tipo or "").upper() == "MAYOR"]
    return {
        "al_dia": False, "existe": True, "motivo": motivo, "cambios": cambios,
        "resumen": lector._resumen_del_tramo(cambios), "obligan": obligan}


def dicho(revision):
    """El aviso completo, en una línea, para mostrarlo tal cual."""
    if revision["al_dia"]:
        return "Al día."
    if not revision["existe"]:
        return revision["motivo"]
    return "%s%s" % (revision["motivo"], revision["resumen"])
