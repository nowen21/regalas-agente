# -*- coding: utf-8 -*-
"""Rehace el índice de proyectos leyendo sus fichas en texto."""
from django.core.management.base import BaseCommand

from nucleo.proyectos import core


class Command(BaseCommand):
    help = "Rehace el índice de proyectos leyendo el texto."

    def handle(self, *args, **opciones):
        cuantos = core.reconstruir_indice()
        self.stdout.write("Índice de proyectos rehecho: %d proyecto(s)." % cuantos)
