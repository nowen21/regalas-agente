# -*- coding: utf-8 -*-
"""Aprueba un documento, sobre el texto que hay.

    python manage.py aprobar cimiento-el-estandar documentacion/x/spec.md --quien jose

**`--quien` ya no es un nombre cualquiera: es una cuenta de la plataforma**, y
tiene que tener permiso para aprobar. Las cuentas se crean con
`python manage.py crear_cuenta`.
"""
from django.core.management.base import BaseCommand

from nucleo.aprobaciones import core
from nucleo.ciclo_de_vida import core as ciclo
from nucleo.acceso import core as acceso


class Command(BaseCommand):
    help = "Registra que alguien aprobó un documento"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("documento")
        parser.add_argument("--quien", required=True)

    def handle(self, *args, **opciones):
        try:
            aprobacion = core.aprobar(opciones["proyecto"],
                                      opciones["documento"], opciones["quien"])
        except acceso.NoPuede as porque:
            self.stdout.write("No se aprobó: %s"
                              % ciclo.para_la_consola(str(porque)))
            return
        except core.NoSePuedeAprobar as porque:
            self.stdout.write("No se aprobó: %s"
                              % ciclo.para_la_consola(str(porque)))
            return
        self.stdout.write("Aprobado por %s el %s."
                          % (aprobacion.quien, aprobacion.cuando))
        self.stdout.write("Sobre %d caracteres. **Si el documento cambia, la "
                          "aprobación caduca y se dice.**" % aprobacion.tamano)
