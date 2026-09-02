# -*- coding: utf-8 -*-
"""El tablero: cómo va cada proyecto y qué se salió de lo acordado.

**Es la pantalla que la ficha de `F-029` pedía sin nombrarla:** *que enterarse no
dependa de ir a mirar*. Una orden de consola sigue pidiendo ir a mirar; lo que
cambia es dónde.

**Un cero se dice.** Una pantalla en blanco se lee como un error de la
plataforma, y «nada se salió de lo acordado» es una respuesta, no un vacío.
"""
import datetime

from django.shortcuts import render

from nucleo.avisos import core, reporte
from nucleo.proyectos.models import Proyecto


def _hoy():
    return datetime.date.today().isoformat()


def tablero(peticion):
    """`P-03`: los proyectos con su avance, y los avisos de todos juntos."""
    hoy = _hoy()
    filas = reporte.de_todos(hoy)

    de_cada_uno = []
    for registrado in Proyecto.objects.all().order_by("identificador"):
        salida = core.de_un_proyecto(registrado.ruta_codigo, hoy)
        if salida["avisos"]:
            de_cada_uno.append({"proyecto": registrado, "salida": salida})

    return render(peticion, "avisos/tablero.html", {
        "hoy": hoy,
        "filas": filas,
        "que_mide": reporte.QUE_MIDE,
        "de_cada_uno": de_cada_uno,
        "cuantos": sum(uno["salida"]["cuantos"] for uno in de_cada_uno),
        "sin_datos": [una["proyecto"] for una in filas
                      if una["avance"] is None],
        "dias": core.DIAS,
    })
