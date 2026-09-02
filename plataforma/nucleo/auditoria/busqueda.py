# -*- coding: utf-8 -*-
"""Buscar en la auditoría. **Sin esto, la auditoría existe pero no sirve.**

Lo dice la ficha de `F-019`, y es literal: un registro que solo se puede leer
de corrido, del principio al fin, no responde ninguna pregunta real. Las
preguntas que se hacen son siempre las mismas tres: **de qué proyecto**, **de
cuándo**, y **de qué tipo de acción**.

**Sin coincidencias se dice que no hay.** Una lista vacía y una búsqueda que no
se pudo hacer se ven igual, y la diferencia importa: la primera es una
respuesta, la segunda es un fallo.

**Y responder rápido no es un lujo acá.** Una consulta que tarda se deja de
hacer, y una auditoría que nadie consulta es lo mismo que no tenerla.
"""
import time

from .models import Registro


def buscar(proyecto="", desde="", hasta="", accion="", cuantas=100):
    """Los registros que cumplen lo que se pida, del más nuevo al más viejo.

    Las cuatro condiciones se combinan: lo que se deje vacío no filtra.
    `accion` busca dentro de lo que se hizo, sin distinguir mayúsculas.

    Devuelve `{"hallados", "cuantos", "hubo", "segundos", "se_recorto"}`.
    """
    empezo = time.time()
    consulta = Registro.objects.all()
    if proyecto:
        consulta = consulta.filter(proyecto=proyecto)
    if desde:
        consulta = consulta.filter(cuando__gte=desde)
    if hasta:
        # El día completo: lo que se escribe como fecha incluye toda la jornada.
        consulta = consulta.filter(cuando__lte=hasta + "￿")
    if accion:
        consulta = consulta.filter(que_se_hizo__icontains=accion)

    cuantos = consulta.count()
    hallados = list(consulta.order_by("-cuando", "-id")[:cuantas])
    return {"hallados": hallados, "cuantos": cuantos, "hubo": cuantos > 0,
            "segundos": time.time() - empezo,
            "se_recorto": cuantos > len(hallados)}


def tipos_de_accion(proyecto=""):
    """Qué tipos de acción hay registrados, para saber por cuáles se puede buscar.

    **Se derivan de lo que hay**, no de una lista escrita: una lista escrita a
    mano se queda corta el día que nazca un tipo nuevo, y nadie lo nota.
    """
    consulta = Registro.objects.all()
    if proyecto:
        consulta = consulta.filter(proyecto=proyecto)
    return sorted(set(consulta.values_list("que_se_hizo", flat=True)))


def dicho(resultado):
    """Lo que se le dice a una persona, incluido cuando no hay nada."""
    if not resultado["hubo"]:
        return ("No hay ningún registro que cumpla eso. **No es que la búsqueda "
                "haya fallado:** es que no pasó nada así.")
    partes = ["%d registro(s)" % resultado["cuantos"]]
    if resultado["se_recorto"]:
        partes.append("se muestran los %d más recientes"
                      % len(resultado["hallados"]))
    partes.append("%.3f s" % resultado["segundos"])
    return "  ·  ".join(partes)
