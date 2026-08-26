# -*- coding: utf-8 -*-
"""Rehace el índice de lo traído leyendo los archivos copiados."""
from django.core.management.base import BaseCommand

from nucleo.importacion import core


class Command(BaseCommand):
    help = "Rehace el índice de lo traído leyendo el texto."

    def handle(self, *args, **opciones):
        cuantos = core.reconstruir_indice()
        self.stdout.write("Índice de lo traído rehecho: %d documento(s)." % cuantos)
