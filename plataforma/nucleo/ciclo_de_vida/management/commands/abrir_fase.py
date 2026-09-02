# -*- coding: utf-8 -*-
"""Abre una fase con sus cinco documentos, sin escribir el nombre a mano.

    python manage.py abrir_fase cimiento-el-estandar S EP-019 HU-001 "las puertas se comprueban"
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import apertura, core


class Command(BaseCommand):
    help = "Abre una fase con sus cinco documentos, tomados del molde"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("letra", help="la letra de la fase, una mayúscula")
        parser.add_argument("epica", help="EP-000")
        parser.add_argument("historia", help="HU-000")
        parser.add_argument("titulo", help="de qué trata la fase")
        parser.add_argument("--quien", default="el usuario")
        parser.add_argument("--donde-iria", action="store_true",
                            help="solo decir dónde quedaría, sin crear nada")

    def handle(self, *args, **opciones):
        try:
            if opciones["donde_iria"]:
                carpeta, nombre = apertura.donde_iria(
                    opciones["proyecto"], opciones["letra"], opciones["epica"],
                    opciones["historia"], opciones["titulo"])
                self.stdout.write("Se llamaría: %s" % core.para_la_consola(nombre))
                self.stdout.write("Y quedaría en: %s"
                                  % core.para_la_consola(carpeta))
                return
            abierta = apertura.abrir_fase(
                opciones["proyecto"], opciones["letra"], opciones["epica"],
                opciones["historia"], opciones["titulo"], opciones["quien"])
        except apertura.NoSePuedeAbrir as porque:
            self.stdout.write("No se abrió: %s" % core.para_la_consola(str(porque)))
            return
        self.stdout.write(core.para_la_consola(apertura.dicho(abierta)))
        for uno in abierta["documentos"]:
            self.stdout.write("  %s" % uno)
