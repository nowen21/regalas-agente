"""`EP-026·HU-008` · Un proyecto reporta al estándar lo que encuentra mal en él.

    manage.py reportar --proyecto "C:/ruta" --titulo "…" --texto "…" --regla 02·F8

Queda abierto en Cimiento → Estándar → Reportes. La versión sube cuando se
corrige, y el proyecto se entera al abrir su sesión siguiente.
"""
import os

from django.core.management.base import BaseCommand, CommandError

from core.estandar.models import Reporte
from core.historia.registro import quien_y_por_que
from core.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Deja un reporte de un proyecto al estándar."

    def add_arguments(self, parser):
        parser.add_argument("--proyecto", required=True, help="la carpeta del proyecto que reporta")
        parser.add_argument("--titulo", required=True)
        parser.add_argument("--texto", default="")
        parser.add_argument("--regla", default="")
        parser.add_argument("--quien", default="agente")

    def handle(self, *args, proyecto="", titulo="", texto="", regla="", quien="agente", **opciones):
        registrado = Proyecto.objects.filter(ruta__iexact=os.path.abspath(proyecto), activo=True).first()
        if registrado is None:
            raise CommandError("el proyecto %s no está registrado en Cimiento" % proyecto)
        with quien_y_por_que(quien=quien, motivo="Reporte de %s" % registrado):
            reporte = Reporte.objects.create(proyecto=registrado, titulo=titulo.strip(), texto=texto,
                                             regla=regla.strip(), quien=quien)
        self.stdout.write("Reporte %d abierto. Se ve en Cimiento → Estándar → Reportes." % reporte.pk)
