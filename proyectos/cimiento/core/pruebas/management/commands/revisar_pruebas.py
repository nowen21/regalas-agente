# -*- coding: utf-8 -*-
"""`manage.py revisar_pruebas`: revisa qué parte de un proyecto queda sin pruebas.

    python manage.py revisar_pruebas --proyecto «nombre o número»
    python manage.py revisar_pruebas --todos

`EP-029·HU-002` · Hace lo mismo que el botón «Revisar» (análisis 1 del pendiente
141, acuerdo 11): el botón arranca esta orden aparte, para que la página no
espere. Cada revisión queda guardada con su fecha.
"""
from django.core.management.base import BaseCommand, CommandError

from core.comun.consola import preparar_salida
from core.proyectos.models import Proyecto

from ...revisar import revisar_y_guardar


class Command(BaseCommand):
    help = "Revisa qué parte de un proyecto, o de todos, queda sin pruebas."

    def add_arguments(self, parser):
        grupo = parser.add_mutually_exclusive_group(required=True)
        grupo.add_argument("--proyecto", help="El nombre o el número del proyecto.")
        grupo.add_argument("--todos", action="store_true", help="Todos los proyectos activos.")

    def handle(self, *args, **opciones):
        preparar_salida()
        if opciones["todos"]:
            proyectos = list(Proyecto.objects.filter(activo=True))
        else:
            dato = opciones["proyecto"]
            proyectos = list(Proyecto.objects.filter(pk=int(dato)) if dato.isdigit()
                             else Proyecto.objects.filter(nombre=dato))
            if not proyectos:
                raise CommandError("No hay ningún proyecto registrado con «%s»." % dato)
        for proyecto in proyectos:
            revision = revisar_y_guardar(proyecto)
            porcentaje = "" if revision.porcentaje is None else " · %s%% con pruebas" % revision.porcentaje
            self.stdout.write("%s: %s%s" % (proyecto.nombre, revision.get_resultado_display(), porcentaje))
            if revision.mensaje:
                self.stdout.write("  " + revision.mensaje)
