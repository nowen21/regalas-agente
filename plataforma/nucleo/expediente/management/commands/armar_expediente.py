# -*- coding: utf-8 -*-
"""Arma el expediente de un proyecto y dice en qué estado está."""
from django.core.management.base import BaseCommand

from nucleo.expediente import core
from nucleo.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Junta la documentación de un proyecto en el orden del ciclo."

    def add_arguments(self, parser):
        parser.add_argument("proyecto", help="identificador del proyecto")
        parser.add_argument("--hasta", help="nombre de la fase donde cortar")
        parser.add_argument("--detalle", action="store_true",
                            help="lista documento por documento")

    def handle(self, *args, **opciones):
        identificador = opciones["proyecto"]
        if not Proyecto.objects.filter(identificador=identificador).exists():
            self.stdout.write("No hay un proyecto con ese identificador.")
            return

        expediente = core.armar(identificador, opciones.get("hasta"))
        if not expediente["grupos"]:
            # **Un proyecto sin documentos lo dice**, en vez de devolver un
            # expediente vacío que se lee como si estuviera todo bien.
            self.stdout.write(
                "Ese proyecto no tiene documentos traídos: no hay qué juntar.")
            return

        for grupo in expediente["grupos"]:
            self.stdout.write("%-32s %d documento(s)"
                              % (grupo["grupo"], len(grupo["documentos"])))
            if opciones["detalle"]:
                for documento in grupo["documentos"]:
                    self.stdout.write("    %-28s %s"
                                      % (documento.tipo, documento.origen))

        self.stdout.write("\n%d documento(s) en el expediente."
                          % core.cuantos_documentos(expediente))

        self._lista("Falta", [u"%s: %s" % (f["donde"], f["que"])
                              for f in expediente["falta"]])
        self._lista("A medio llenar",
                    [u"%s (%d hueco/s)" % (d["origen"], d["huecos"])
                     for d in expediente["incompletos"]])
        self._lista("No encaja en ningún grupo",
                    [u"%s (%s)" % (d["origen"], d["tipo"] or "sin reconocer")
                     for d in expediente["sin_encajar"]])
        self._lista("Fuera del alcance pedido",
                    [u"%s" % d["origen"] for d in expediente["fuera_del_alcance"]])

    def _lista(self, titulo, renglones, cuantos=8):
        """Una de las listas del expediente. **Se dice aunque esté vacía.**

        Un silencio no distingue «no falta nada» de «no se miró».
        """
        self.stdout.write("\n%s: %d" % (titulo, len(renglones)))
        for renglon in renglones[:cuantos]:
            self.stdout.write("    %s" % renglon)
        if len(renglones) > cuantos:
            self.stdout.write("    y %d más" % (len(renglones) - cuantos))
