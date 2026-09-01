# -*- coding: utf-8 -*-
"""Dice qué le falta por llenar a un documento, o a todo un proyecto.

    python manage.py que_le_falta cimiento-el-estandar
    python manage.py que_le_falta cimiento-el-estandar --documento documentacion/senales.md
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core


class Command(BaseCommand):
    help = "Qué espacios por llenar le quedan a un documento del ciclo"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--documento", default="",
                            help="ruta del documento dentro del proyecto")
        parser.add_argument("--posibles", action="store_true",
                            help="mostrar también los que no son huecos seguros")

    def handle(self, *args, **opciones):
        if opciones["documento"]:
            self._uno(opciones["proyecto"], opciones["documento"],
                      opciones["posibles"])
        else:
            self._todos(opciones["proyecto"])

    def _uno(self, proyecto, documento, con_posibles):
        falta = core.que_le_falta(proyecto, documento)
        if falta is None:
            self.stdout.write("Ese documento no está traído: %s" % documento)
            return

        if falta["sin_tipo"]:
            self.stdout.write("No se le conoce el tipo, así que no se le puede "
                              "atribuir un molde.")
            return
        self.stdout.write("Tipo: %s" % falta["tipo"])
        if falta["sin_molde"]:
            self.stdout.write("Sin molde: %s" % falta["sin_molde"])
        elif falta["molde"]:
            self.stdout.write("Molde: %s" % falta["molde"])

        if falta["completo"]:
            self.stdout.write("Sin espacios por llenar.")
        else:
            self.stdout.write("")
            self.stdout.write("Le faltan %d espacio(s) por llenar:"
                              % falta["cuantos"])
            for uno in falta["ciertos"]:
                self.stdout.write("  linea %d: %s" % (uno["linea"],
                                                      core.para_la_consola(uno["contexto"])))

        if falta["instalacion"]:
            self.stdout.write("")
            self.stdout.write("Y %d marca(s) que llena la instalación, no el "
                              "usuario." % len(falta["instalacion"]))

        if falta["posibles"]:
            self.stdout.write("")
            self.stdout.write("Hay %d marca(s) que también están en el molde. "
                              "No se cuentan: en un documento escrito no se "
                              "distinguen de una cita."
                              % len(falta["posibles"]))
            if con_posibles:
                for uno in falta["posibles"]:
                    self.stdout.write("  linea %d: %s" % (uno["linea"],
                                                          core.para_la_consola(uno["marca"])))

    def _todos(self, proyecto):
        lista = core.de_un_proyecto(proyecto)
        if not lista:
            self.stdout.write("Ningún documento traído tiene espacios por "
                              "llenar. Si esperaba otra cosa, revise que el "
                              "proyecto esté traído.")
            return
        total = sum(uno["cuantos"] for uno in lista)
        self.stdout.write("%d documento(s) con espacios por llenar, %d en total:"
                          % (len(lista), total))
        for uno in lista:
            self.stdout.write("  %4d  %s" % (uno["cuantos"], core.para_la_consola(uno["origen"])))
