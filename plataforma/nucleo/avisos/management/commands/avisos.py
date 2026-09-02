# -*- coding: utf-8 -*-
"""Lo que se salió de lo acordado en un proyecto.

    python manage.py avisos cimiento-el-estandar --hoy 2026-09-01
    python manage.py avisos cimiento-el-estandar --hoy 2026-09-01 --dias 60
"""
from django.core.management.base import BaseCommand

from nucleo.avisos import core
from nucleo.ciclo_de_vida import core as consola
from nucleo.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Lo que se desvió de lo acordado, de lo que más duele a lo que menos"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--hoy", required=True, help="AAAA-MM-DD")
        parser.add_argument("--dias", type=int, default=core.DIAS,
                            help="cuántos días sin moverse cuentan como vencida")

    def handle(self, *args, **opciones):
        try:
            registrado = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("El proyecto %s no está conectado."
                              % opciones["proyecto"])
            return
        salida = core.de_un_proyecto(registrado.ruta_codigo, opciones["hoy"],
                                     opciones["dias"])
        self.stdout.write(consola.para_la_consola(core.dicho(salida)))
        if not salida["avisos"]:
            return
        self.stdout.write("")
        for uno in salida["avisos"]:
            self.stdout.write("  " + consola.para_la_consola(core.linea(uno)))
