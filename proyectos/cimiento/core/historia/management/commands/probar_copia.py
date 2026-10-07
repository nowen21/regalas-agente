"""`EP-026·HU-010` · Comprueba que una copia se restaura, en una base aparte que después se borra."""
import os

from django.core.management.base import BaseCommand, CommandError

from core.historia import copia


class Command(BaseCommand):
    help = "Carga una copia en una base aparte, cuenta sus tablas y borra la base aparte."

    def add_arguments(self, parser):
        parser.add_argument("archivo", nargs="?", help="la copia; sin esto, la más nueva")

    def handle(self, *args, archivo=None, **opciones):
        destino = copia.carpeta()
        if not archivo:
            nuevas = copia.copias(destino)
            if not nuevas:
                raise CommandError("No hay copias en %s" % destino)
            archivo = os.path.join(destino, nuevas[0])
        cuenta = copia.probar(archivo)
        self.stdout.write("%s se restaura: %d tablas, %d filas." % (os.path.basename(archivo), len(cuenta),
                                                                   sum(cuenta.values())))
