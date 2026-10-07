"""`EP-026·HU-005` · Imprime un recuerdo de la memoria de un proyecto, desde la base.

    manage.py ver_recuerdo aprobar-antes-de-commit.md --proyecto "C:/Ing. Jose/ia/agente"
    manage.py ver_recuerdo --lista --proyecto "C:/Ing. Jose/ia/agente"
"""
import os

from django.core.management.base import BaseCommand, CommandError

from core.estandar.models import Recuerdo
from core.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Imprime un recuerdo de un proyecto desde la base, o la lista de sus recuerdos."

    def add_arguments(self, parser):
        parser.add_argument("nombre", nargs="?", default="memory.md")
        parser.add_argument("--proyecto", required=True, help="la carpeta del proyecto")
        parser.add_argument("--lista", action="store_true")

    def handle(self, *args, nombre="memory.md", proyecto="", lista=False, **opciones):
        registrado = Proyecto.objects.filter(ruta__iexact=os.path.abspath(proyecto)).first()
        if registrado is None:
            raise CommandError("el proyecto %s no está registrado en Cimiento" % proyecto)
        if lista:
            for n in Recuerdo.objects.filter(proyecto=registrado).values_list("nombre", flat=True):
                self.stdout.write(n)
            return
        recuerdo = Recuerdo.objects.filter(proyecto=registrado, nombre=nombre).first()
        if recuerdo is None:
            raise CommandError("%s no está en la memoria de %s" % (nombre, registrado))
        self.stdout.write(recuerdo.contenido, ending="")
