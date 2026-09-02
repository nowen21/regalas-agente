# -*- coding: utf-8 -*-
"""Busca en la auditoría por proyecto, por fecha y por tipo de acción.

    python manage.py buscar_en_la_auditoria --proyecto cimiento-el-estandar
    python manage.py buscar_en_la_auditoria --desde 2026-09-01 --accion aprobar
    python manage.py buscar_en_la_auditoria --que-tipos-hay
"""
from django.core.management.base import BaseCommand

from nucleo.auditoria import busqueda
from nucleo.ciclo_de_vida import core as ciclo


class Command(BaseCommand):
    help = "Busca en la auditoría por proyecto, fecha y tipo de acción"

    def add_arguments(self, parser):
        parser.add_argument("--proyecto", default="")
        parser.add_argument("--desde", default="")
        parser.add_argument("--hasta", default="")
        parser.add_argument("--accion", default="")
        parser.add_argument("--cuantas", type=int, default=30)
        parser.add_argument("--que-tipos-hay", action="store_true",
                            dest="tipos")

    def handle(self, *args, **opciones):
        if opciones["tipos"]:
            tipos = busqueda.tipos_de_accion(opciones["proyecto"])
            if not tipos:
                self.stdout.write("No hay ningún registro todavía.")
                return
            self.stdout.write("Tipos de acción registrados: %d" % len(tipos))
            for uno in tipos:
                self.stdout.write("  %s" % ciclo.para_la_consola(uno))
            return

        resultado = busqueda.buscar(opciones["proyecto"], opciones["desde"],
                                    opciones["hasta"], opciones["accion"],
                                    opciones["cuantas"])
        self.stdout.write(ciclo.para_la_consola(busqueda.dicho(resultado)))
        if not resultado["hubo"]:
            return
        self.stdout.write("")
        for uno in resultado["hallados"]:
            self.stdout.write("  %s  %-22s %s"
                              % (uno.cuando[:19],
                                 ciclo.para_la_consola(uno.que_se_hizo[:22]),
                                 ciclo.para_la_consola(uno.sobre_que[:60])))
