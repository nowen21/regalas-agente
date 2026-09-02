# -*- coding: utf-8 -*-
"""Cuánto tiempo se gasta revisando, mes a mes, y contra la línea base.

    python manage.py cuanto_se_revisa
    python manage.py cuanto_se_revisa --proyecto cimiento-el-estandar --por-mes
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as consola
from nucleo.medicion import revision


class Command(BaseCommand):
    help = "El tiempo de revisión, medido de las horas que ya están escritas"

    def add_arguments(self, parser):
        parser.add_argument("--proyecto", default="")
        parser.add_argument("--por-mes", action="store_true",
                            help="mostrar el detalle mes a mes")

    def handle(self, *args, **opciones):
        proyecto = opciones["proyecto"] or None
        if opciones["por_mes"]:
            meses = revision.por_mes(proyecto)
            if not meses:
                self.stdout.write("No hay ninguna sesión indexada con hora de "
                                  "reloj. No es cero: es que no se sabe.")
                return
            self.stdout.write("%-9s %8s %12s %10s %10s" % (
                "mes", "cuantas", "total (min)", "mediana", "sin hora"))
            for uno in meses:
                self.stdout.write("%-9s %8d %12.1f %9.0fs %10d" % (
                    uno["mes"], uno["cuantos"], uno["total_minutos"],
                    uno["mediana_segundos"], uno["descartados_sin_hora"]))
            self.stdout.write("")
        self.stdout.write(
            consola.para_la_consola(revision.dicho(revision.comparar(proyecto))))
