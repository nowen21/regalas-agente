# -*- coding: utf-8 -*-
"""`manage.py cerrar_fase «carpeta»`: cierra una fase con lo que dicen sus planes (`EP-025·HU-016`).

    python manage.py cerrar_fase ../../documentacion/epicas/EP-…/HU-…/A-… --pruebas "python -m unittest …"
    python manage.py cerrar_fase ../../documentacion/epicas/EP-…/HU-…/A-… --aplicar

La primera pasada deja `«…»` en lo que un programa no sabe; la fase se cierra
cuando ya no queda ninguno. Su contraria es `reabrir_fase`.
"""
from django.core.management.base import BaseCommand, CommandError

from core.comun import Proyecto
from core.comun.consola import preparar_salida
from core.herramientas.fase import Fase


class Command(BaseCommand):
    help = "Cierra una fase: escribe sus documentos de cierre y la marca en la HU y en la épica."
    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument("carpeta", help="la carpeta de la fase")
        parser.add_argument("--pruebas", default="", help="la orden que corre las pruebas de la fase; si fallan, no cierra")
        parser.add_argument("--hallazgos", default="ninguno", help="los hallazgos al ejecutar, para el cierre del plan")
        parser.add_argument("--aplicar", action="store_true", help="escribe de verdad; sin esto solo dice qué haría")

    def handle(self, *args, **o):
        preparar_salida()                   # imprime «·»: sin esto, mojibake
        try:
            accion, tocados, faltan = Fase(o["carpeta"]).cerrar(o["aplicar"], o["pruebas"] or None, o["hallazgos"])
        except ValueError as e:
            raise CommandError("No se cierra: %s" % e)
        self.stdout.write("%s  (%s)" % (accion, "hecho" if o["aplicar"] else "simulado; agrega --aplicar"))
        for ruta in tocados:
            self.stdout.write("  · %s" % Proyecto(Proyecto.estandar()).mostrar(ruta))
        for archivo, linea in faltan:
            self.stdout.write("  por llenar: %s:%d" % (archivo, linea))
