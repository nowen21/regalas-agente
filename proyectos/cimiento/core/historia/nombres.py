# -*- coding: utf-8 -*-
"""`EP-027·HU-005` · La historia nombra la tabla por lo que guarda y la fila por su nombre.

La tabla dice su `verbose_name` («Documento del estándar»), no `estandar.documento`.
La fila dice el `nombre_legible()` del modelo, o su `str`; lo que ya se borró se
nombra desde la fila que el cambio guardó. Las filas de una página se traen en una
consulta por tabla, no una por fila.
"""
from collections import defaultdict

from django.apps import apps


def _modelo(tabla):
    try:
        return apps.get_model(tabla)
    except (LookupError, ValueError):
        return None


def nombre_de_tabla(tabla):
    modelo = _modelo(tabla)
    if modelo is None:
        return tabla
    nombre = str(modelo._meta.verbose_name)
    return nombre[:1].upper() + nombre[1:]


def _nombre(instancia):
    legible = getattr(instancia, "nombre_legible", None)
    try:
        return legible() if callable(legible) else str(instancia)
    except Exception:  # una fila a medias, rearmada desde la historia
        return ""


def _desde_lo_guardado(modelo, datos):
    """Una instancia sin guardar, armada con la fila que guardó el cambio."""
    campos = {f.attname for f in modelo._meta.concrete_fields}
    return modelo(**{k: v for k, v in (datos or {}).items() if k in campos})


def nombrar(cambios):
    """Pone `tabla_legible` y `fila_legible` a cada cambio."""
    cambios = list(cambios)
    por_tabla = defaultdict(set)
    for cambio in cambios:
        por_tabla[cambio.tabla].add(cambio.fila)
    vivas = {}
    for tabla, filas in por_tabla.items():
        modelo = _modelo(tabla)
        if modelo is None:
            continue
        claves = [f for f in filas if str(f).isdigit()]
        for instancia in modelo._default_manager.filter(pk__in=claves):
            vivas[(tabla, str(instancia.pk))] = instancia
    for cambio in cambios:
        cambio.tabla_legible = nombre_de_tabla(cambio.tabla)
        instancia = vivas.get((cambio.tabla, str(cambio.fila)))
        modelo = _modelo(cambio.tabla)
        if instancia is None and modelo is not None:
            instancia = _desde_lo_guardado(modelo, cambio.antes or cambio.despues)
        cambio.fila_legible = (_nombre(instancia) if instancia is not None else "") or cambio.fila
    return cambios
