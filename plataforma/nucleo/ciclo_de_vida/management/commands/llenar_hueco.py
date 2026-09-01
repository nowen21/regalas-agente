# -*- coding: utf-8 -*-
"""Llena un espacio por llenar de un documento del ciclo.

    python manage.py llenar_hueco <proyecto> <documento>
    python manage.py llenar_hueco <proyecto> <documento> --numero 1 --texto "lo que va"

Sin `--texto` solo muestra qué huecos tiene y en qué línea está cada uno, para
poder elegir cuál. **Escribe en el archivo del proyecto**, no en la copia.
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core, escritura


class Command(BaseCommand):
    help = "Llena un espacio por llenar de un documento del ciclo"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("documento")
        parser.add_argument("--numero", type=int, default=0,
                            help="cuál de los espacios, contando desde uno")
        parser.add_argument("--texto", default="",
                            help="lo que va en ese espacio")

    def handle(self, *args, **opciones):
        proyecto = opciones["proyecto"]
        documento = opciones["documento"]

        ruta, _, falta = core.huecos_del_original(proyecto, documento)
        if falta is None:
            if ruta:
                self.stdout.write("No se encontró el archivo del proyecto: %s"
                                  % ruta)
            else:
                self.stdout.write("Ese documento no está traído: %s" % documento)
            return

        if not opciones["texto"]:
            self._mostrar(ruta, falta)
            return

        try:
            quedan = core.llenar(proyecto, documento, opciones["numero"],
                                 opciones["texto"])
        except escritura.CambioAjeno as porque:
            self.stdout.write("No se escribió nada. %s"
                              % core.para_la_consola(str(porque)))
            return
        except escritura.SeMovio as porque:
            self.stdout.write("No se escribió nada. %s"
                              % core.para_la_consola(str(porque)))
            return
        except ValueError as porque:
            self.stdout.write("%s" % core.para_la_consola(str(porque)))
            return

        self.stdout.write("Escrito en %s" % core.para_la_consola(ruta))
        self.stdout.write("Le quedan %d espacio(s) por llenar."
                          % quedan["cuantos"])

    def _mostrar(self, ruta, falta):
        self.stdout.write("Archivo: %s" % core.para_la_consola(ruta))
        if falta["completo"]:
            self.stdout.write("Sin espacios por llenar.")
            return
        self.stdout.write("Le faltan %d espacio(s):" % falta["cuantos"])
        for numero, uno in enumerate(falta["ciertos"], 1):
            self.stdout.write("  %d)  linea %d: %s"
                              % (numero, uno["linea"], core.para_la_consola(uno["contexto"])))
        self.stdout.write("")
        self.stdout.write("Para llenar uno: --numero N --texto \"lo que va\"")
