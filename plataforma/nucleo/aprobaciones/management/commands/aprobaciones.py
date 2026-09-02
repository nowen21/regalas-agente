# -*- coding: utf-8 -*-
"""El estado de aprobación de los documentos de un proyecto.

    python manage.py aprobaciones cimiento-el-estandar
    python manage.py aprobaciones cimiento-el-estandar --documento documentacion/x/spec.md
"""
from django.core.management.base import BaseCommand

from nucleo.aprobaciones import core
from nucleo.aprobaciones.models import Aprobacion
from nucleo.ciclo_de_vida import core as ciclo


class Command(BaseCommand):
    help = "Qué está aprobado, qué caducó y qué no ha pasado por nadie"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--documento", default="")

    def handle(self, *args, **opciones):
        proyecto = opciones["proyecto"]

        if opciones["documento"]:
            self._uno(proyecto, opciones["documento"])
            return

        documentos = sorted(set(
            Aprobacion.objects.filter(proyecto=proyecto)
            .values_list("documento", flat=True)))
        if not documentos:
            self.stdout.write("Ningún documento de este proyecto tiene "
                              "aprobaciones registradas.")
            return

        self.stdout.write("%d documento(s) con aprobaciones:" % len(documentos))
        self.stdout.write("")
        for uno in core.de_un_proyecto(proyecto, documentos):
            self.stdout.write("  %-11s %s"
                              % (uno["estado"],
                                 ciclo.para_la_consola(uno["documento"])))
        self.stdout.write("")
        self.stdout.write("**Se dice con palabras, no con color:** quien no "
                          "distingue colores tiene que poder saberlo igual.")

    def _uno(self, proyecto, documento):
        estado = core.estado_de(proyecto, documento)
        self.stdout.write(ciclo.para_la_consola(documento))
        self.stdout.write(ciclo.para_la_consola(estado["en_palabras"]))
        if estado["cuantas"]:
            self.stdout.write("Última: %s, el %s."
                              % (ciclo.para_la_consola(estado["quien"]),
                                 estado["desde"]))
            self.stdout.write("Aprobaciones en su historia: %d. **Ninguna se "
                              "borra.**" % estado["cuantas"])
        if estado["estado"] == core.CADUCADA:
            de_mas, de_menos = core.que_cambio(proyecto, documento)
            self.stdout.write("Cambió: %d caracteres de más, %d de menos "
                              "respecto de lo aprobado." % (de_mas, de_menos))
