# -*- coding: utf-8 -*-
"""La pantalla de las aprobaciones: qué está aprobado y qué caducó.

**Los tres estados se dicen con palabras, no con color.** Es el `CA` de `F-016`,
y la razón es sencilla: quien no distingue colores tiene que poder saberlo.

**Solo salen los documentos que tienen alguna aprobación.** Listar todos los del
proyecto es de otro módulo, y esta pantalla lo dice en vez de dar a entender que
esos son todos.
"""
from django.shortcuts import get_object_or_404, render

from nucleo.aprobaciones import core
from nucleo.aprobaciones.models import Aprobacion
from nucleo.proyectos.models import Proyecto


def aprobaciones(peticion, identificador):
    """`P-06`: el estado de cada documento con alguna aprobación."""
    registrado = get_object_or_404(Proyecto, identificador=identificador)
    documentos = sorted(set(
        Aprobacion.objects.filter(proyecto=identificador)
        .values_list("documento", flat=True)))
    estados = core.de_un_proyecto(identificador, documentos)

    cuenta = {}
    for uno in estados:
        cuenta[uno["estado"]] = cuenta.get(uno["estado"], 0) + 1

    return render(peticion, "aprobaciones/aprobaciones.html", {
        "proyecto": registrado,
        "estados": estados,
        "cuantos": len(estados),
        "aprobados": cuenta.get(core.APROBADO, 0),
        "caducadas": cuenta.get(core.CADUCADA, 0),
        "APROBADO": core.APROBADO,
        "CADUCADA": core.CADUCADA,
    })
