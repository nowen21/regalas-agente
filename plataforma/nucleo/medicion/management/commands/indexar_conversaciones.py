# -*- coding: utf-8 -*-
"""Indexa las conversaciones de un proyecto conectado, o de todos."""
from django.core.management.base import BaseCommand

from nucleo.medicion import core
from nucleo.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Lee historico-chat/ de cada proyecto y lo deja buscable."

    def add_arguments(self, parser):
        parser.add_argument("--proyecto", help="identificador; sin esto, todos")

    def handle(self, *args, **opciones):
        proyectos = Proyecto.objects.all()
        if opciones.get("proyecto"):
            proyectos = proyectos.filter(identificador=opciones["proyecto"])
            if not proyectos:
                self.stdout.write("No hay un proyecto con ese identificador.")
                return

        for proyecto in proyectos:
            try:
                cuenta = core.indexar(proyecto)
            except core.NoSePuedeIndexar as falla:
                self.stdout.write("%s: %s" % (proyecto.nombre, falla))
                continue
            self.stdout.write(
                "%s: %d sesion(es), %d mensaje(s)."
                % (proyecto.nombre, cuenta["sesiones"], cuenta["mensajes"]))
            for nombre, motivo in cuenta["ilegibles"]:
                self.stdout.write("  no se pudo leer %s: %s" % (nombre, motivo))
