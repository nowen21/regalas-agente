"""`EP-026·HU-005` · Imprime un recuerdo de la memoria de un proyecto, desde la base.

    manage.py ver_recuerdo aprobar-antes-de-commit.md --proyecto "C:/Ing. Jose/ia/agente"
    manage.py ver_recuerdo --lista --proyecto "C:/Ing. Jose/ia/agente"

Lee por el camino único de los documentos (`EP-030·HU-001`).
"""
from django.core.management.base import BaseCommand, CommandError

from core.estandar import documentos
from core.estandar.cambios import CambioInvalido


class Command(BaseCommand):
    help = "Imprime un recuerdo de un proyecto desde la base, o la lista de sus recuerdos."

    def add_arguments(self, parser):
        parser.add_argument("nombre", nargs="?", default="memory.md")
        parser.add_argument("--proyecto", required=True, help="la carpeta del proyecto")
        parser.add_argument("--lista", action="store_true")

    def handle(self, *args, nombre="memory.md", proyecto="", lista=False, **opciones):
        try:
            registrado = documentos.proyecto_de(proyecto)
            if lista:
                for n in documentos.listar("recuerdo", "", registrado):
                    self.stdout.write(n)
                return
            texto = documentos.ver("recuerdo", nombre, registrado)
        except CambioInvalido as razon:
            raise CommandError(str(razon))
        self.stdout.write(texto, ending="")
