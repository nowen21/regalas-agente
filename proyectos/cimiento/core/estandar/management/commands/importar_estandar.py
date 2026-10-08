"""`EP-026·HU-003` · Pasa el estándar y la memoria de cada proyecto a la base, una sola vez.

`EP-027·HU-003` · Después, las reglas pasan a sus tablas y el texto se arma desde ellas.
"""
import os

from django.core.management.base import BaseCommand, CommandError

from core.comun import Proyecto as Carpeta
from core.estandar.importar import YaImportado, importar
from core.estandar.reglas import pasar_todo
from core.historia.registro import en_version, quien_y_por_que


class Command(BaseCommand):
    help = "Importa base/ y la memoria de cada proyecto registrado a la base de Cimiento."

    def handle(self, *args, **opciones):
        try:
            version, documentos, recuerdos = importar()
        except YaImportado as razon:
            raise CommandError(str(razon))
        with quien_y_por_que(quien="importar_estandar", motivo=version.resumen), en_version(version):
            reglas, _ = pasar_todo(os.path.abspath(Carpeta.estandar()))
        self.stdout.write("Estándar %s en la base: %d documentos, %d reglas y %d recuerdos."
                          % (version.numero, documentos, reglas, recuerdos))
