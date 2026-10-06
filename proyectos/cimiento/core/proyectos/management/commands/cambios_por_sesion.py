# -*- coding: utf-8 -*-
"""`manage.py cambios_por_sesion`: lo que cambió cada sesión, y prepararlo para el commit (`EP-025·HU-016`).

    python manage.py cambios_por_sesion
    python manage.py cambios_por_sesion c3d82767 --preparar --aplicar
    python manage.py cambios_por_sesion c3d82767 --soltar --aplicar

Lo que tocaron dos sesiones se nombra y no se prepara.
"""
from django.core.management.base import BaseCommand, CommandError

from core.comun import Proyecto
from core.comun.consola import preparar_salida
from core.herramientas.cambios import CambiosPorSesion


class Command(BaseCommand):
    help = "Lista lo que cambió cada sesión; prepara o suelta lo de una sola."
    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument("sesion", nargs="?", default="", help="el comienzo del identificador de la sesión")
        parser.add_argument("--raiz", default=Proyecto.estandar(), help="la carpeta del repositorio")
        accion = parser.add_mutually_exclusive_group()
        accion.add_argument("--preparar", action="store_true", help="prepara para el commit lo de la sesión")
        accion.add_argument("--soltar", action="store_true", help="la contraria: saca lo de la sesión de lo preparado")
        parser.add_argument("--aplicar", action="store_true", help="lo hace de verdad; sin esto solo dice qué haría")

    def handle(self, *args, **o):
        preparar_salida()                   # imprime «·»: sin esto, mojibake
        cambios = CambiosPorSesion(o["raiz"])
        marca = "hecho" if o["aplicar"] else "simulado; agrega --aplicar"
        try:
            if o["preparar"] or o["soltar"]:
                if not o["sesion"]:
                    raise ValueError("preparar o soltar piden la sesión")
                if o["preparar"]:
                    sesion, archivos, compartidos = cambios.preparar(o["sesion"], o["aplicar"])
                    self.stdout.write("preparar lo de %s: %d archivos  (%s)" % (sesion[:8], len(archivos), marca))
                    self._lista(archivos)
                    if compartidos:
                        self.stdout.write("no se preparan, los tocaron dos sesiones: %d" % len(compartidos))
                        self._lista(compartidos)
                else:
                    sesion, archivos = cambios.soltar(o["sesion"], o["aplicar"])
                    self.stdout.write("soltar lo de %s: %d archivos  (%s)" % (sesion[:8], len(archivos), marca))
                    self._lista(archivos)
                return
            propios, compartidos, sin_sesion = cambios.repartir()
        except ValueError as e:
            raise CommandError(str(e))
        for sesion, archivos in sorted(propios.items()):
            self.stdout.write("%s: %d" % (sesion[:8], len(archivos)))
            self._lista(archivos)
        for titulo, archivos in (("de dos sesiones", compartidos), ("sin sesión", sin_sesion)):
            if archivos:
                self.stdout.write("%s: %d" % (titulo, len(archivos)))
                self._lista(archivos)

    def _lista(self, archivos):
        for a in archivos:
            self.stdout.write("  · %s" % a)
