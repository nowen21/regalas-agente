# -*- coding: utf-8 -*-
"""Genera el entregable del expediente de un proyecto."""
from django.core.management.base import BaseCommand

from nucleo.expediente import entregable
from nucleo.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Convierte el expediente en un archivo, desde el texto."

    def add_arguments(self, parser):
        parser.add_argument("proyecto", help="identificador del proyecto")
        parser.add_argument("--hasta", help="nombre de la fase donde cortar")

    def handle(self, *args, **opciones):
        identificador = opciones["proyecto"]
        if not Proyecto.objects.filter(identificador=identificador).exists():
            self.stdout.write("No hay un proyecto con ese identificador.")
            return

        nombre, avisos = entregable.generar(identificador, opciones.get("hasta"))

        # **Los avisos van antes**, aunque el archivo ya esté escrito: quien
        # lea la salida tiene que ver lo que le falta antes que la ruta.
        for aviso in avisos:
            self.stdout.write(aviso)
        if not nombre:
            return
        self.stdout.write("\nEntregable generado: %s" % nombre)
        self.stdout.write(
            "Sale del texto y se rehace cuando se quiera. No se edita: "
            "si hay que corregir algo, se corrige el documento y se genera otra vez.")
