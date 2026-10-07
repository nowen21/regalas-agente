"""`EP-026·HU-003` · Pasa el estándar y la memoria de cada proyecto a la base, una sola vez."""
from django.core.management.base import BaseCommand, CommandError

from core.estandar.importar import YaImportado, importar


class Command(BaseCommand):
    help = "Importa base/ y la memoria de cada proyecto registrado a la base de Cimiento."

    def handle(self, *args, **opciones):
        try:
            version, documentos, recuerdos = importar()
        except YaImportado as razon:
            raise CommandError(str(razon))
        self.stdout.write("Estándar %s en la base: %d documentos y %d recuerdos." % (version.numero, documentos,
                                                                                    recuerdos))
