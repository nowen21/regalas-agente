# -*- coding: utf-8 -*-
"""Borra el índice y lo rehace leyendo `datos/`.

Sirve para comprobar que perder la base no pierde información (`RNF-04`), y
para volver a la vida después de clonar el repositorio en otra máquina.
"""
from django.core.management.base import BaseCommand

from nucleo.almacen import core


class Command(BaseCommand):
    help = "Rehace el índice leyendo la carpeta de datos."

    def handle(self, *args, **opciones):
        cuantos = core.reconstruir_indice()
        self.stdout.write("Índice rehecho: %d archivo(s) leídos." % cuantos)
