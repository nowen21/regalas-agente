# -*- coding: utf-8 -*-
"""Las reglas que pueden cambiar de nivel: todas las de `base/`, menos las del
núcleo, que siempre frenan, y las derogadas, que ya no rigen.

Se leen una vez por proceso: son 268 reglas repartidas en decenas de archivos.
"""
from collections import namedtuple
from functools import lru_cache

ReglaConfigurable = namedtuple("ReglaConfigurable", "id capitulo titulo")


def es_del_nucleo(id_completo):
    capitulo, _, regla = id_completo.partition("·")
    return capitulo == "00" and regla.startswith("N")


@lru_cache(maxsize=1)
def reglas_configurables():
    """`[ReglaConfigurable]` en el orden de `base/`."""
    # `core.validadores` primero: importar `metareglas` de entrada cae en el
    # ciclo de importación del pendiente 121.
    import core.validadores  # noqa: F401
    from core.validadores.metareglas import CuerpoDeReglas

    salida = []
    for regla in CuerpoDeReglas.leer():
        id_completo = f"{regla.capitulo}·{regla.id}"
        if regla.derogada or es_del_nucleo(id_completo):
            continue
        salida.append(ReglaConfigurable(id_completo, regla.capitulo, regla.titulo))
    return salida


def ids_configurables():
    return {regla.id for regla in reglas_configurables()}
