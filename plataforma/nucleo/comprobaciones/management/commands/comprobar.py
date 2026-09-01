# -*- coding: utf-8 -*-
"""Dice si un proyecto cumple lo que las reglas exigen.

    python manage.py comprobar cimiento-el-estandar
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.comprobaciones import core


class Command(BaseCommand):
    help = "Corre las comprobaciones del estándar contra un proyecto"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--cuantas", type=int, default=15,
                            help="cuántas fallas mostrar (0 para todas)")

    def handle(self, *args, **opciones):
        veredicto = core.comprobar(opciones["proyecto"])

        if not veredicto.se_pudo:
            self.stdout.write("No se pudo comprobar: %s"
                              % ciclo.para_la_consola(veredicto.porque))
            return

        self.stdout.write("Comprobaciones corridas: %d  ·  con fallas: %d  ·  "
                          "%.1f s" % (veredicto.corridas, veredicto.con_fallas,
                                      veredicto.segundos))

        if veredicto.corridas == 0:
            self.stdout.write("")
            self.stdout.write("**Cero comprobaciones corridas no es verde:** "
                              "quiere decir que no se comprobó nada.")
            return

        if veredicto.cumple:
            self.stdout.write("")
            self.stdout.write("Cumple.")
            return

        self.stdout.write("")
        self.stdout.write("No cumple. %d falla(s):" % len(veredicto.fallas))
        cuantas = opciones["cuantas"]
        muestra = veredicto.fallas if cuantas <= 0 else veredicto.fallas[:cuantas]
        for una in muestra:
            self.stdout.write("  %s" % ciclo.para_la_consola(una["donde"]))
            self.stdout.write("      %s" % ciclo.para_la_consola(una["que"]))
        if len(muestra) < len(veredicto.fallas):
            self.stdout.write("  ... y %d más. Con --cuantas 0 salen todas."
                              % (len(veredicto.fallas) - len(muestra)))
