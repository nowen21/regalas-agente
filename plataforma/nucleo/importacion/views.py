# -*- coding: utf-8 -*-
"""La pantalla de traer: primero se mira, después se confirma, y solo entonces se trae.

Es `P-11` del diseño aprobado. Muestra el **recuento por tipo**, no la lista
entera: un número por tipo se lee, y mil líneas se confirman sin mirar.

Y dice **qué carpetas no se miraron**, con su porqué. Saltarse carpetas sin
decirlo es perder en silencio con otro nombre (`RN-4`).
"""
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
