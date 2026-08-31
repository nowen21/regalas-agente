# -*- coding: utf-8 -*-
"""Dice qué correcciones tuvo que repetir el usuario, y cuántas veces."""
from django.core.management.base import BaseCommand

from nucleo.medicion import repeticion


class Command(BaseCommand):
    help = "Lo que se repitió, de lo más repetido a lo menos."

    def add_arguments(self, parser):
        parser.add_argument("--desde", help="AAAA-MM-DD")
        parser.add_argument("--hasta", help="AAAA-MM-DD")
        parser.add_argument("--limite", type=int, default=15)

    def handle(self, *args, **opciones):
        desde, hasta = opciones.get("desde"), opciones.get("hasta")
        repetidas = repeticion.correcciones(desde, hasta,
                                            limite=opciones["limite"])
        if not repetidas:
            # **Dos silencios distintos, y se dicen distinto.** Que no haya
            # nada repetido no es lo mismo que no haber tenido qué mirar.
            if not repeticion.cuantas_correcciones(desde, hasta):
                self.stdout.write(
                    "No hay correcciones en ese período: puede que no haya "
                    "conversaciones indexadas todavía.")
            else:
                self.stdout.write("Nada se repitió en ese período.")
            return

        for r in repetidas:
            self.stdout.write("%3d  %-34s %d sesión(es)"
                              % (r["veces"], r["frase"], len(r["sesiones"])))
            for archivo in r["sesiones"][:3]:
                self.stdout.write("       %s" % archivo)
            if len(r["sesiones"]) > 3:
                self.stdout.write("       y %d más" % (len(r["sesiones"]) - 3))

        # **El reporte muestra el patrón; la regla la decide el usuario.** Sin
        # esta línea, una lista ordenada se lee como una lista de tareas.
        self.stdout.write(
            "\nEsto es el patrón, no la regla. Lo que amerite regla entra por "
            "la cadena de siempre: pendiente, historia, fase.")
