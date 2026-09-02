# -*- coding: utf-8 -*-
"""En qué estación va cada fase del proyecto, y qué puerta le falta.

    python manage.py en_que_va cimiento-el-estandar
    python manage.py en_que_va cimiento-el-estandar --sin-terminar
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import apertura, core, estaciones


class Command(BaseCommand):
    help = "La estación actual de cada fase, y la puerta pendiente"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--sin-terminar", action="store_true",
                            help="mostrar solo las que no pasaron las trece")
        parser.add_argument("--hoy", default="",
                            help="fecha contra la cual medir cuánto lleva quieta")

    def handle(self, *args, **opciones):
        raiz = apertura._raiz_del_proyecto(opciones["proyecto"])
        if not raiz:
            self.stdout.write("El proyecto %s no está conectado."
                              % opciones["proyecto"])
            return
        fases = estaciones.de_un_proyecto(raiz)
        if not fases:
            self.stdout.write("No hay ninguna fase con `estado-fase.md` en ese "
                              "proyecto. No es un error: puede que todavía no "
                              "se haya abierto ninguna.")
            return
        cuenta = estaciones.resumen(fases)
        self.stdout.write("%d fase(s) · %d con las trece estaciones pasadas"
                          % (cuenta["cuantas"], cuenta["terminadas"]))
        if cuenta["de_otro_modelo"]:
            self.stdout.write(
                "%d usa(n) una tabla que no es la de trece estaciones: son "
                "fases viejas, no se reescriben, y su estación no se compara "
                "con la de las demás." % cuenta["de_otro_modelo"])
        if cuenta["con_estaciones_sin_marcar"]:
            self.stdout.write(
                "%d tiene(n) alguna estación sin marcar: el documento cuenta "
                "qué pasó con ella en vez de marcarla, y eso no es lo mismo "
                "que estar pendiente." % cuenta["con_estaciones_sin_marcar"])
        if cuenta["sin_coincidir"]:
            self.stdout.write(
                "%d dice(n) ir en una estación distinta de la que marca su "
                "tabla. Manda la tabla." % cuenta["sin_coincidir"])
        self.stdout.write("")
        for una in fases:
            if opciones["sin_terminar"] and una["actual"] == estaciones.TERMINADA:
                continue
            self.stdout.write("  " + core.para_la_consola(estaciones.dicho(una)))
            if opciones["hoy"]:
                dias = estaciones.detenida_desde(una, opciones["hoy"])
                if dias >= 0:
                    self.stdout.write("      sin tocarse hace %d día(s)" % dias)
                else:
                    self.stdout.write("      no dice desde cuándo")
