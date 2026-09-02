# -*- coding: utf-8 -*-
"""La pantalla de las funcionalidades: qué está verificado y qué no.

**Los tres estados se dicen con palabras y no con color.** Verificado, no cumple
y sin verificar; y el del medio no se junta con ninguno de los otros dos, porque
*nadie comprobó* y *se comprobó y salió mal* son cosas distintas.

**Y cada uno dice de dónde sale.** Un estado sin su porqué obliga a creerle a la
pantalla, y esta pantalla no quiere que le crean: quiere que la comprueben.
"""
from django.shortcuts import get_object_or_404, render

from nucleo.comprobaciones import estado
from nucleo.proyectos.models import Proyecto


def funcionalidades(peticion, identificador):
    """`P-05`: el estado de cada funcionalidad del inventario."""
    registrado = get_object_or_404(Proyecto, identificador=identificador)
    todas = estado.estado_de_todas(registrado.ruta_codigo)

    por_estado = {}
    for una in todas:
        por_estado[una["estado"]] = por_estado.get(una["estado"], 0) + 1

    return render(peticion, "comprobaciones/funcionalidades.html", {
        "proyecto": registrado,
        "seccion": "funcionalidades",
        "funcionalidades": todas,
        "cuantas": len(todas),
        "verificadas": por_estado.get(estado.VERIFICADO, 0),
        "no_cumplen": por_estado.get(estado.NO_CUMPLE, 0),
        "sin_verificar": por_estado.get(estado.SIN_VERIFICAR, 0),
        "VERIFICADO": estado.VERIFICADO,
        "NO_CUMPLE": estado.NO_CUMPLE,
    })
