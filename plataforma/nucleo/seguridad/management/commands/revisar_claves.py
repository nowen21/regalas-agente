# -*- coding: utf-8 -*-
"""Dice qué documentos traídos parecen traer credenciales. No toca ninguno.

    python manage.py revisar_claves cimiento-el-estandar
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.importacion.models import Traido
from nucleo.seguridad import revision


class Command(BaseCommand):
    help = "Qué documentos traídos parecen traer credenciales"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")

    def handle(self, *args, **opciones):
        traidos = list(Traido.objects.filter(proyecto=opciones["proyecto"]))
        if not traidos:
            self.stdout.write("Ese proyecto no tiene documentos traídos.")
            return

        textos = [(uno.origen, ciclo._texto_de(uno)) for uno in traidos]
        encontrados = revision.parecen_traer_claves(textos)

        self.stdout.write("Documentos revisados: %d" % len(traidos))
        if not encontrados:
            self.stdout.write("Ninguno parece traer credenciales.")
            return

        total = sum(cuantas for _, cuantas in encontrados)
        self.stdout.write("Parecen traer credenciales: %d documento(s), "
                          "%d fragmento(s)." % (len(encontrados), total))
        self.stdout.write("")
        for nombre, cuantas in encontrados:
            self.stdout.write("  %3d  %s"
                              % (cuantas, ciclo.para_la_consola(nombre)))
        self.stdout.write("")
        self.stdout.write("**No se tocó ninguno.** Lo traído es texto que ya "
                          "existía, y taparlo no se deshace. Revíselos: puede "
                          "que sean ejemplos escritos y no claves de verdad.")
