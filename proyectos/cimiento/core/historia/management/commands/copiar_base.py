"""`EP-026·HU-010` · Copia la base a la carpeta de copias, a mano. Sola, la lanza el inicio de sesión."""
from django.core.management.base import BaseCommand

from core.historia import copia


class Command(BaseCommand):
    help = "Copia la base de Cimiento a cimiento-copias y deja las últimas 7."

    def handle(self, *args, **opciones):
        ruta = copia.copiar(copia.carpeta())
        self.stdout.write("Copia escrita: %s" % ruta)
