# -*- coding: utf-8 -*-
"""`manage.py retapar_lineas`: vuelve a pasar el tapado por las líneas ya guardadas.

    python manage.py retapar_lineas

Cuando el tapado aprende una forma de clave nueva, lo guardado antes quedó con
el tapado de entonces (`EP-025·HU-025`, fase B; análisis 1 del pendiente 129,
acuerdo 2). Solo se guarda la línea que cambia, y la huella no se toca: sigue
siendo la de la línea original. No tiene vuelta, a propósito: destapar una clave
es lo que `00·N6` prohíbe.
"""
from django.core.management.base import BaseCommand

from core.comun.consola import preparar_salida
from core.enganches.enmascarar import Enmascarador

from ...formato import miles
from ...models import LineaDeSesion


def retapar(tanda=2000):
    """`(revisadas, cambiadas)`."""
    revisadas = cambiadas = 0
    filas = LineaDeSesion.objects.only("pk", "texto", "tapadas").order_by("pk")
    for linea in filas.iterator(chunk_size=tanda):
        revisadas += 1
        texto, nuevas = Enmascarador.enmascarar(linea.texto)
        if nuevas:
            LineaDeSesion.objects.filter(pk=linea.pk).update(texto=texto, tapadas=linea.tapadas + nuevas)
            cambiadas += 1
    return revisadas, cambiadas


class Command(BaseCommand):
    help = "Vuelve a pasar el tapado de claves por las líneas de sesión ya guardadas."

    def handle(self, *args, **opciones):
        preparar_salida()
        revisadas, cambiadas = retapar()
        self.stdout.write("%s línea(s) revisadas; %s con claves que ahora se tapan."
                          % (miles(revisadas), miles(cambiadas)))
