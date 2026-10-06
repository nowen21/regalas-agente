from django.http import Http404
from django.shortcuts import render

from .secciones import SECCIONES, TITULOS, seccion_de


def _secciones():
    return [{"slug": s, "titulo": t, "plantilla": "ayuda/secciones/%s.html" % s} for s, t, _ in SECCIONES]


def manual(request):
    """El manual completo, en una página que se puede imprimir."""
    return render(request, "ayuda/manual.html", {"secciones": _secciones()})


def panel(request, seccion):
    """Una sección del manual, para el panel de la derecha, con el índice de las demás."""
    if seccion not in TITULOS:
        raise Http404("Esa sección del manual no existe")
    return render(request, "ayuda/panel.html", {
        "secciones": _secciones(), "actual": seccion, "titulo": TITULOS[seccion],
        "plantilla": "ayuda/secciones/%s.html" % seccion,
    })


def pantalla(request):
    """La sección de la pantalla desde la que se pidió la ayuda (`?vista=app:nombre`)."""
    return panel(request, seccion_de(request.GET.get("vista")))
