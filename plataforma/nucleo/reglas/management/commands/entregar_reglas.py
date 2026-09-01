# -*- coding: utf-8 -*-
"""Las reglas que rigen en un proyecto, para dárselas al agente.

    python manage.py entregar_reglas cimiento-el-estandar
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import entrega


class Command(BaseCommand):
    help = "Entrega el cuerpo de reglas vigente de un proyecto"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--con-el-texto", action="store_true",
                            dest="con_texto")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        entregada = entrega.entregar(proyecto.ruta_codigo,
                                     proyecto.version_reglas)
        self.stdout.write(ciclo.para_la_consola(entrega.encabezado(entregada)))
        if not entregada["se_pudo"]:
            return

        self.stdout.write("Caracteres: %d" % entregada["caracteres"])
        if opciones["con_texto"]:
            for capitulo in entregada["capitulos"]:
                self.stdout.write("")
                self.stdout.write("<<< %s >>>" % capitulo["ruta"])
                self.stdout.write(ciclo.para_la_consola(capitulo["texto"]))
        else:
            self.stdout.write("")
            self.stdout.write("Con --con-el-texto sale el cuerpo completo.")
