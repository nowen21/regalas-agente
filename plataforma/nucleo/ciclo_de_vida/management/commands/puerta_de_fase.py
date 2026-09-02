# -*- coding: utf-8 -*-
"""Si una fase puede pasar a la estación siguiente, y qué le falta si no.

    python manage.py puerta_de_fase cimiento-el-estandar --fase D-EP-009-HU-001-la-constancia-va-antes-que-el-efecto
"""
import io
import os

from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import apertura, core, estaciones, puertas


class Command(BaseCommand):
    help = "Las tres puertas comprobables de una fase, con su veredicto"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--fase", default="",
                            help="el nombre de la fase; sin esto, todas")

    def handle(self, *args, **opciones):
        raiz = apertura._raiz_del_proyecto(opciones["proyecto"])
        if not raiz:
            self.stdout.write("El proyecto %s no está conectado."
                              % opciones["proyecto"])
            return
        fases = estaciones.de_un_proyecto(raiz)
        if opciones["fase"]:
            fases = [una for una in fases if una["fase"] == opciones["fase"]]
            if not fases:
                self.stdout.write("No se halló la fase %s." % opciones["fase"])
                return
        for una in fases:
            with io.open(una["ruta"], encoding="utf-8",
                         errors="replace") as abierto:
                texto = abierto.read()
            self.stdout.write(core.para_la_consola(una["fase"]))
            self.stdout.write(
                core.para_la_consola(puertas.dicho(puertas.revisar(una, texto))))
            self.stdout.write("")
