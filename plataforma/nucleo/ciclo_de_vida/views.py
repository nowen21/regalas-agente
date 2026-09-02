# -*- coding: utf-8 -*-
"""La pantalla de las fases: en cuál estación va cada una y qué le falta.

**Es la pantalla que hace útil a `F-012`.** Una fase se mira abriendo su
documento; doscientas no se miran de ninguna forma, y una lista de doscientas
líneas en la consola tampoco se mira.

**Lo que la fase no dice, la pantalla tampoco lo inventa.** Una tabla de otro
modelo no se compara con su frase, una casilla con prosa no es una casilla
pendiente, y una fase sin fecha no lleva cero días quieta: no se sabe.
"""
import datetime

from django.shortcuts import get_object_or_404, render

from nucleo.ciclo_de_vida import estaciones
from nucleo.proyectos.models import Proyecto


def fases(peticion, identificador):
    """`P-04`: todas las fases del proyecto, de la menos avanzada a la más."""
    registrado = get_object_or_404(Proyecto, identificador=identificador)
    hoy = datetime.date.today().isoformat()
    todas = estaciones.de_un_proyecto(registrado.ruta_codigo)

    solo_abiertas = peticion.GET.get("abiertas") == "si"
    if solo_abiertas:
        mostradas = [una for una in todas
                     if una["actual"] != estaciones.TERMINADA]
    else:
        mostradas = todas

    for una in mostradas:
        dias = estaciones.detenida_desde(una, hoy)
        una["dias"] = dias if dias >= 0 else None

    return render(peticion, "ciclo_de_vida/fases.html", {
        "proyecto": registrado,
        "seccion": "fases",
        "fases": mostradas,
        "cuenta": estaciones.resumen(todas),
        "solo_abiertas": solo_abiertas,
        "terminada": estaciones.TERMINADA,
        "trece": estaciones.TRECE,
    })
