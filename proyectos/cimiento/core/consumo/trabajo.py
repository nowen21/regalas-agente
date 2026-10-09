# -*- coding: utf-8 -*-
"""`EP-025·HU-010` · De qué trabajo fue un turno: el análisis o la fase que tocó.

Ningún registro dice qué estaba activo. El aviso de acuerdos nombra fases de
otras sesiones, así que no sirve; las rutas que el turno leyó o escribió sí
lo dicen. Gana la que más veces aparece; sin ninguna, el turno queda sin
trabajo. Sin Django.

`EP-025·HU-028` · Tres fuentes, en este orden: el análisis que el aviso de cada
mensaje dice prendido, lo que tocó el turno (rutas y órdenes de consola, con
fases de cualquier letra) y, si nada de eso, el trabajo del mensaje anterior de
la misma conversación (`guardar.py`). Fase B: si ni eso, la conversación misma,
por el título que le pone Claude Code; ningún mensaje queda sin trabajo.
"""
import re
from collections import Counter

_FASE = re.compile(r"(?<![A-Za-z0-9])([A-Z]-EP-\d+-HU-\d+(?:-[A-Za-z0-9-]+)?)")
_ANALISIS = re.compile(r"pendientes[\\/](\d+)-[^\\/]+[\\/]analisis-(\d+)\.md", re.IGNORECASE)
# El aviso de `core/enganches/analisis_en_curso.py`: «La conversación entra al análisis <ruta>.»
_PRENDIDO = re.compile(r"\[ANÁLISIS EN CURSO\] La conversación entra al análisis (.+?\.md)")

# De dónde salió el trabajo de un mensaje (`Pedido.origen`).
DEL_ANALISIS, DE_LO_QUE_TOCO, DE_LA_CONVERSACION = "analisis", "archivos", "sesion"
# `EP-025·HU-028`, fase B · Sin fase ni análisis: la conversación misma, por su título.
DEL_TITULO = "titulo"


def trabajo_de_la_conversacion(sesion, titulo=""):
    """«Conversación «Buenos días»», o con el comienzo del código si Claude Code no le puso título."""
    if titulo and titulo.strip():
        return ("Conversación «%s»" % titulo.strip())[:200]
    return "Conversación %s" % (sesion or "")[:8]


def trabajo_de_la_ruta(ruta):
    """`A-EP-025-HU-010-segunda-tanda`, `análisis 2 del pendiente 119`, o ""."""
    analisis = _ANALISIS.search(ruta or "")
    if analisis:
        return "análisis %s del pendiente %s" % (analisis.group(2), analisis.group(1))
    fase = _FASE.search(ruta or "")
    return fase.group(1).rstrip("-") if fase else ""


def trabajo_de(rutas):
    """El trabajo que más aparece en `rutas`, o ""."""
    cuenta = Counter(t for t in map(trabajo_de_la_ruta, rutas) if t)
    return cuenta.most_common(1)[0][0] if cuenta else ""


def trabajo_del_aviso(texto):
    """El análisis que el aviso de un mensaje dice prendido, o "" (también si está en pausa)."""
    prendido = _PRENDIDO.search(texto or "")
    return trabajo_de_la_ruta(prendido.group(1)) if prendido else ""
