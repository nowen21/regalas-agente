"""`EP-026·HU-004` · Pone la base al día con lo que dice git de base/, en una versión del estándar."""
from django.core.management.base import BaseCommand

from core.estandar.importar import sincronizar
from core.historia.versiones import tipo_de


class Command(BaseCommand):
    help = "Trae a la base lo guardado en git de base/ que no esté en ella."

    def add_arguments(self, parser):
        parser.add_argument("--obliga", choices=["si", "no"], default="no",
                            help="¿Un proyecto que hoy cumple deja de cumplir? (MAYOR)")
        parser.add_argument("--agrega", choices=["si", "no"], default="no",
                            help="¿Se agrega algo que nadie está obligado a usar? (MENOR)")
        parser.add_argument("--motivo", default="")

    def handle(self, *args, obliga="no", agrega="no", motivo="", **opciones):
        creados, cambiados, quitados = sincronizar(tipo=tipo_de(obliga, agrega), motivo=motivo)
        if not (creados or cambiados or quitados):
            self.stdout.write("La base ya está al día con git: no sube versión.")
            return
        self.stdout.write("Base al día con git: %d nuevos, %d cambiados, %d quitados." % (creados, cambiados, quitados))
