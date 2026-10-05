# -*- coding: utf-8 -*-
"""`EP-025·HU-010` · De qué trabajo fue un turno: el análisis o la fase que tocó.

Ningún registro dice qué estaba activo. El aviso de acuerdos nombra fases de
otras sesiones, así que no sirve; las rutas que el turno leyó o escribió sí
lo dicen. Gana la que más veces aparece; sin ninguna, el turno queda sin
trabajo. Sin Django.
"""
import re
from collections import Counter

_FASE = re.compile(r"(A-EP-\d+-HU-\d+(?:-[A-Za-z0-9-]+)?)")
_ANALISIS = re.compile(r"pendientes[\\/](\d+)-[^\\/]+[\\/]analisis-(\d+)\.md", re.IGNORECASE)


def trabajo_de_la_ruta(ruta):
    """`A-EP-025-HU-010-segunda-tanda`, `análisis 2 del pendiente 119`, o ""."""
    analisis = _ANALISIS.search(ruta or "")
    if analisis:
        return "análisis %s del pendiente %s" % (analisis.group(2), analisis.group(1))
    fase = _FASE.search(ruta or "")
    return fase.group(1) if fase else ""


def trabajo_de(rutas):
    """El trabajo que más aparece en `rutas`, o ""."""
    cuenta = Counter(t for t in map(trabajo_de_la_ruta, rutas) if t)
    return cuenta.most_common(1)[0][0] if cuenta else ""
