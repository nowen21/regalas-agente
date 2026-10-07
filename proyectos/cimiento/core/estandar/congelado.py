# -*- coding: utf-8 -*-
"""`EP-026·HU-006` · El estándar congelado: `base/`, `VERSION` y `CHANGELOG.md` no se tocan.

**La marca es un ajuste común**, `base_congelada = si`, en la capa de la base:
queda en la historia y sube la versión del estándar como cualquier cambio.

**Sin Django** para leerla: la leen el freno en cada acción y el control del
commit. Sin base no se sabe, y se toma como congelado: es el lado seguro, y el
freno ya no deja modificar sin base (análisis 1 del pendiente 132, acuerdo 9).

**Solo vale en la carpeta del estándar.** La `base/` de otro proyecto, si la
tiene, no es el estándar.
"""
import datetime
import os

from ..enganches.niveles import BaseSinRespuesta, NivelesDelProyecto

CLAVE = "base_congelada"
SI = "si"
QUIETOS = ("VERSION", "CHANGELOG.md")
PREFIJO = "base/"
_CACHE = {}


def es_el_estandar(raiz):
    from ..comun import Proyecto

    estandar = Proyecto.estandar()
    return bool(estandar) and os.path.normcase(os.path.abspath(raiz)) == os.path.normcase(os.path.abspath(estandar))


def congelada(raiz, ajustes=None):
    """¿El estándar en `raiz` está congelado? Fuera del estándar, nunca."""
    if not es_el_estandar(raiz):
        return False
    clave = os.path.normcase(os.path.abspath(raiz))
    if clave not in _CACHE:
        try:
            filas = NivelesDelProyecto(raiz, estandar=raiz, ajustes=ajustes).consultar(
                "SELECT valor FROM proyectos_ajustebase WHERE clave = %s", [CLAVE])
            _CACHE[clave] = bool(filas) and filas[0][0] == SI
        except BaseSinRespuesta:
            _CACHE[clave] = True
    return _CACHE[clave]


def quieto(relativa):
    """¿La ruta, desde la raíz del estándar, es de lo que queda quieto?"""
    rel = (relativa or "").replace("\\", "/").lstrip("./")
    return rel.startswith(PREFIJO) or rel in QUIETOS


def ultima_version_del_estandar(raiz, ajustes=None):
    """La fecha, en UTC, de la última versión del estándar registrada en la base, o None."""
    filas = NivelesDelProyecto(raiz, estandar=raiz, ajustes=ajustes).consultar(
        "SELECT MAX(fecha) FROM historia_version WHERE ambito = 'estandar'", [])
    fecha = filas[0][0] if filas else None
    if fecha is not None and fecha.tzinfo is None:
        fecha = fecha.replace(tzinfo=datetime.timezone.utc)
    return fecha


def versiones_en_la_base(raiz, ajustes=None):
    """`EP-026·HU-008` · `["X.Y.Z", ...]` de las versiones del estándar en la base, de
    la más nueva a la más vieja. Sin base, `BaseSinRespuesta`."""
    filas = NivelesDelProyecto(raiz, estandar=raiz, ajustes=ajustes).consultar(
        "SELECT mayor, menor, parche FROM historia_version WHERE ambito = 'estandar' "
        "ORDER BY mayor DESC, menor DESC, parche DESC", [])
    return ["%d.%d.%d" % f for f in filas]


def olvidar():
    _CACHE.clear()


MOTIVO = ("el estándar vive en la base de Cimiento: `base/`, `VERSION` y `CHANGELOG.md` quedaron quietos. "
          "Se cambia en Cimiento → Estándar, o se propone con `manage.py proponer` (20·M10)")
