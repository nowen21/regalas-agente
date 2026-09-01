# -*- coding: utf-8 -*-
"""El estado de cada funcionalidad, derivado de la prueba corrida.

    python manage.py estado_funcionalidades cimiento-el-estandar
    python manage.py estado_funcionalidades cimiento-el-estandar --solo "sin verificar"
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.comprobaciones import estado
from nucleo.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "El estado de cada funcionalidad, según la fase que la construyó"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--solo", default="",
                            help="mostrar solo las de ese estado")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        estados = estado.estado_de_todas(proyecto.ruta_codigo)
        if not estados:
            self.stdout.write("Ese proyecto no tiene inventario de "
                              "funcionalidades, así que no hay qué medir.")
            return

        cuenta = estado.resumen(estados)
        self.stdout.write(
            "Funcionalidades: %d  ·  verificadas: %d  ·  no cumplen: %d  ·  "
            "sin verificar: %d"
            % (len(estados), cuenta[estado.VERIFICADO], cuenta[estado.NO_CUMPLE],
               cuenta[estado.SIN_VERIFICAR]))
        self.stdout.write("")

        solo = opciones["solo"].strip().lower()
        for uno in estados:
            if solo and uno["estado"] != solo:
                continue
            self.stdout.write("  %-8s %-14s %s"
                              % (uno["funcionalidad"], uno["estado"],
                                 ciclo.para_la_consola(uno["porque"])))

        self.stdout.write("")
        self.stdout.write("**Sin verificar no es lo mismo que no cumple:** una "
                          "es que nadie comprobó, la otra es que se comprobó y "
                          "salió mal. Lo que está sin verificar no se cierra.")
