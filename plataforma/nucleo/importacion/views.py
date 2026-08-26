# -*- coding: utf-8 -*-
"""La pantalla de traer: primero se mira, después se confirma, y solo entonces se trae.

Es `P-11` del diseño aprobado. Muestra el **recuento por tipo**, no la lista
entera: un número por tipo se lee, y mil líneas se confirman sin mirar.

Y dice **qué carpetas no se miraron**, con su porqué. Saltarse carpetas sin
decirlo es perder en silencio con otro nombre (`RN-4`).
"""
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from nucleo.proyectos.models import Proyecto
from . import core


def traer(request, identificador):
    proyecto = get_object_or_404(Proyecto, identificador=identificador)
    hallazgo = core.mirar(proyecto)

    if request.method != "POST" or not request.POST.get("confirmado"):
        return render(request, "importacion/traer.html", {
            "proyecto": proyecto,
            "hallazgo": hallazgo,
        })

    try:
        hallazgo, nuevos, ya_estaban = core.traer(
            proyecto, quien="el usuario",
            sesion=(request.POST.get("sesion") or "").strip())
    except core.NoSePudoTraer as falla:
        return render(request, "importacion/traer.html", {
            "proyecto": proyecto,
            "hallazgo": hallazgo,
            "error": str(falla),
        })

    return render(request, "importacion/traer.html", {
        "proyecto": proyecto,
        "hallazgo": hallazgo,
        "nuevos": nuevos,
        "ya_estaban": ya_estaban,
        "hecho": True,
    })


def reportes(request, identificador):
    """Los reportes de lo que no entró, del más nuevo al más viejo.

    **Se pueden mirar sin volver a traer**, que es lo que esta pantalla vino a
    resolver: antes, para saber qué había quedado afuera había que traer el
    proyecto entero otra vez.
    """
    proyecto = get_object_or_404(Proyecto, identificador=identificador)
    return render(request, "importacion/reportes.html", {
        "proyecto": proyecto,
        "reportes": core.reportes_de(proyecto),
    })


def reporte(request, identificador, cuando):
    """Un reporte concreto, tal como quedó escrito."""
    proyecto = get_object_or_404(Proyecto, identificador=identificador)
    for fecha, ruta in core.reportes_de(proyecto):
        if fecha == cuando:
            return render(request, "importacion/reporte.html", {
                "proyecto": proyecto,
                "cuando": fecha,
                "texto": core.leer_reporte(ruta),
            })
    raise Http404("No hay un reporte de esa fecha para este proyecto.")
