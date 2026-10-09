"""`EP-026·HU-005` · Imprime un documento del estándar tal como está en la base.

    manage.py ver_estandar base/reglas-por-tarea/responder.md
    manage.py ver_estandar --lista base/01-conducta

Lee por el camino único de los documentos (`EP-030·HU-001`).
"""
from django.core.management.base import BaseCommand, CommandError

from core.estandar import documentos
from core.estandar.cambios import CambioInvalido


class Command(BaseCommand):
    help = "Imprime un documento del estándar desde la base, o la lista de los que empiezan por una ruta."

    def add_arguments(self, parser):
        parser.add_argument("ruta")
        parser.add_argument("--lista", action="store_true", help="lista las rutas que empiezan así")

    def handle(self, *args, ruta="", lista=False, **opciones):
        ruta = ruta.replace("\\", "/").strip()
        if lista:
            for r in documentos.listar("estandar", ruta):
                self.stdout.write(r)
            return
        try:
            self.stdout.write(documentos.ver("estandar", ruta), ending="")
        except CambioInvalido:
            raise CommandError("%s no está en el estándar" % ruta)
