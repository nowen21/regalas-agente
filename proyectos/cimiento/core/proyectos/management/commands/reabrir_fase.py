# -*- coding: utf-8 -*-
"""`manage.py reabrir_fase «carpeta» --motivo «…»`: la contraria de `cerrar_fase` (`EP-025·HU-016`).

La fase vuelve a la estación 8, la HU y la épica a «En curso», y el resultado
suma un ciclo por llenar antes de volver a cerrar.
"""
from django.core.management.base import BaseCommand, CommandError

from core.comun import Proyecto
from core.comun.consola import preparar_salida
from core.herramientas.fase import Fase


class Command(BaseCommand):
    help = "Reabre una fase cerrada, con su motivo."
    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument("carpeta", help="la carpeta de la fase")
        parser.add_argument("--motivo", required=True, help="por qué se reabre")
        parser.add_argument("--aplicar", action="store_true", help="escribe de verdad; sin esto solo dice qué haría")

    def handle(self, *args, **o):
        preparar_salida()                   # imprime «·»: sin esto, mojibake
        try:
            accion, tocados = Fase(o["carpeta"]).reabrir(o["motivo"], o["aplicar"])
        except ValueError as e:
            raise CommandError("No se reabre: %s" % e)
        self.stdout.write("%s  (%s)" % (accion, "hecho" if o["aplicar"] else "simulado; agrega --aplicar"))
        for ruta in tocados:
            self.stdout.write("  · %s" % Proyecto(Proyecto.estandar()).mostrar(ruta))
