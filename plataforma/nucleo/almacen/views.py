# -*- coding: utf-8 -*-
"""Lo mínimo para saber que la plataforma está viva. Las pantallas llegan después."""
from django.http import HttpResponse

from . import core


def esta_viva(request):
    """Dice que la plataforma responde, y cuántos archivos tiene indexados."""
    from .models import Anotado
    cuantos = Anotado.objects.count()
    return HttpResponse(
        "La plataforma está viva.\n"
        "Carpeta de datos: %s\n"
        "Archivos en el índice: %d\n" % (core.carpeta_datos(), cuantos),
        content_type="text/plain; charset=utf-8")
