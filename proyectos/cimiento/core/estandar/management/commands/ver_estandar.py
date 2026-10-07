"""`EP-026·HU-005` · Imprime un documento del estándar tal como está en la base.

    manage.py ver_estandar base/reglas-por-tarea/responder.md
    manage.py ver_estandar --lista base/01-conducta
"""
from django.core.management.base import BaseCommand, CommandError

from core.estandar.models import Documento


class Command(BaseCommand):
    help = "Imprime un documento del estándar desde la base, o la lista de los que empiezan por una ruta."

    def add_arguments(self, parser):
        parser.add_argument("ruta")
        parser.add_argument("--lista", action="store_true", help="lista las rutas que empiezan así")

    def handle(self, *args, ruta="", lista=False, **opciones):
        ruta = ruta.replace("\\", "/").strip()
        if lista:
            for r in Documento.objects.filter(ruta__startswith=ruta).values_list("ruta", flat=True):
                self.stdout.write(r)
            return
        documento = Documento.objects.filter(ruta=ruta).first()
        if documento is None:
            raise CommandError("%s no está en el estándar" % ruta)
        self.stdout.write(documento.contenido, ending="")
