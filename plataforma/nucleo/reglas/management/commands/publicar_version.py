# -*- coding: utf-8 -*-
"""Publica una versión del cuerpo de reglas, después de revisarlo todo.

    python manage.py publicar_version cimiento-el-estandar 37.3.0
    python manage.py publicar_version cimiento-el-estandar 37.3.0 --igual-la-publico
"""
from django.core.management.base import BaseCommand

from nucleo.auditoria.core import con_constancia
from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import publicacion


class Command(BaseCommand):
    help = "Publica una versión del cuerpo de reglas"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("version")
        parser.add_argument("--igual-la-publico", action="store_true",
                            dest="publicar")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        revision = publicacion.revisar(opciones["proyecto"],
                                       proyecto.ruta_codigo,
                                       opciones["version"])
        if revision["entrada"]:
            self.stdout.write("Entrada del registro: sí, tipo %s"
                              % (revision["tipo"] or "sin declarar"))
        if revision["puerta"] is not None:
            self.stdout.write("Puerta de publicación: %s"
                              % ("pasa" if revision["puerta"].pasa
                                 else "**no pasa**"))
        self.stdout.write("")

        for problema in revision["problemas"]:
            self.stdout.write("  - %s" % ciclo.para_la_consola(problema))

        if not revision["se_puede"]:
            self.stdout.write("")
            self.stdout.write("**No se publica.**")
            return

        self.stdout.write("Todo listo para publicar %s." % opciones["version"])
        if not opciones["publicar"]:
            self.stdout.write("No se publicó. Con --igual-la-publico se "
                              "publica.")
            return

        con_constancia(
            lambda comprobante: publicacion.publicar(
                opciones["proyecto"], proyecto.ruta_codigo,
                opciones["version"]),
            que_se_hizo="publicar una versión del cuerpo de reglas",
            sobre_que=opciones["version"], quien="el usuario",
            proyecto=opciones["proyecto"],
            que_cambio="tipo %s" % (revision["tipo"] or "sin declarar"))
        self.stdout.write("Publicada %s." % opciones["version"])
