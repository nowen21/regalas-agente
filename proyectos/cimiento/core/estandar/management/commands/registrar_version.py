"""`EP-026·HU-006` · Registra una versión del estándar sin cambiar documentos.

Con `base/` congelado, un cambio de `plantillas/` o de las herramientas que
viajan a los proyectos sigue en git, pero su versión se registra en la base
(`20·M10`). El control del commit la pide.

    manage.py registrar_version --obliga no --agrega si --motivo "…"
"""
from django.core.management.base import BaseCommand

from core.historia import versiones
from core.historia.models import ESTANDAR


class Command(BaseCommand):
    help = "Sube la versión del estándar en la base, con el tipo de las dos preguntas y su motivo."

    def add_arguments(self, parser):
        parser.add_argument("--obliga", choices=["si", "no"], required=True,
                            help="¿Un proyecto que hoy cumple deja de cumplir? (MAYOR)")
        parser.add_argument("--agrega", choices=["si", "no"], required=True,
                            help="¿Se agrega algo que nadie está obligado a usar? (MENOR)")
        parser.add_argument("--motivo", required=True)
        parser.add_argument("--quien", default="registrar_version")

    def handle(self, *args, obliga="no", agrega="no", motivo="", quien="registrar_version", **opciones):
        version = versiones.nueva(ESTANDAR, None, versiones.tipo_de(obliga, agrega), motivo, None, quien)
        self.stdout.write("El estándar va en la %s (%s)." % (version.numero, version.get_tipo_display()))
