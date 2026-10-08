"""`EP-027·HU-006` · Las reglas propias de un proyecto, desde la base.

    manage.py ver_regla --proyecto "C:/DesarrollosClaude/dp"          el índice
    manage.py ver_regla P3 --proyecto "C:/DesarrollosClaude/dp"       una regla entera
    manage.py ver_regla --todas --proyecto "C:/DesarrollosClaude/dp"  todas, enteras
"""
import os

from django.core.management.base import BaseCommand, CommandError

from core.estandar import molde
from core.estandar.models import Regla
from core.estandar.reglas import casillas_de, texto_del_proyecto
from core.proyectos.models import Proyecto


def registrado(ruta):
    proyecto = Proyecto.objects.filter(ruta__iexact=os.path.abspath(ruta)).first()
    if proyecto is None:
        raise CommandError("el proyecto %s no está registrado en Cimiento" % ruta)
    return proyecto


class Command(BaseCommand):
    help = "Imprime el índice de las reglas propias de un proyecto, una regla o todas, desde la base."

    def add_arguments(self, parser):
        parser.add_argument("codigo", nargs="?", default="")
        parser.add_argument("--proyecto", required=True, help="la carpeta del proyecto")
        parser.add_argument("--todas", action="store_true")

    def handle(self, *args, codigo="", proyecto="", todas=False, **opciones):
        proyecto = registrado(proyecto)
        if todas:
            self.stdout.write(texto_del_proyecto(proyecto), ending="")
            return
        reglas = Regla.objects.filter(proyecto=proyecto, apartada=False).order_by("orden", "pk")
        if codigo:
            regla = reglas.filter(codigo=codigo).first()
            if regla is None:
                raise CommandError("%s no es una regla de %s" % (codigo, proyecto))
            self.stdout.write(molde.armar(casillas_de(regla)) + "\n", ending="")
            return
        for regla in reglas:
            self.stdout.write("%s · %s%s" % (regla.codigo, regla.titulo, " (%s)" % regla.grupo if regla.grupo else ""))
