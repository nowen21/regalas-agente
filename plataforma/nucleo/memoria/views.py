# -*- coding: utf-8 -*-
"""La pantalla de la memoria: qué recuerda el agente sobre este proyecto.

**Es un problema de confianza antes que de comodidad**, y así está escrito en la
ficha de `F-024`: *hoy solo el agente ve lo que recuerda*. Esta pantalla es la
mitad que faltaba — la de mirar.

**Lo dado de baja también sale.** Esconderlo dejaría al usuario sin saber que
existió, y lo que ya no vale sigue siendo la respuesta a por qué algo se hizo
como se hizo.
"""
from django.shortcuts import get_object_or_404, render

from nucleo.memoria import core
from nucleo.proyectos.models import Proyecto


def memoria(peticion, identificador):
    """`P-07`: los recuerdos del proyecto, vigentes y dados de baja."""
    registrado = get_object_or_404(Proyecto, identificador=identificador)
    palabra = peticion.GET.get("buscar", "").strip()

    error = ""
    recuerdos = []
    cuenta = {"todos": 0, "vigentes": 0, "de_baja": 0}
    try:
        recuerdos = core.todos(identificador)
        cuenta = core.resumen(identificador)
    except core.NoHayMemoria as porque:
        error = str(porque)

    if palabra and not error:
        pedazo = palabra.lower()
        recuerdos = [uno for uno in recuerdos
                     if pedazo in uno["titulo"].lower()
                     or pedazo in uno["texto"].lower()]

    return render(peticion, "memoria/memoria.html", {
        "proyecto": registrado,
        "recuerdos": recuerdos,
        "cuenta": cuenta,
        "palabra": palabra,
        "error": error,
    })
