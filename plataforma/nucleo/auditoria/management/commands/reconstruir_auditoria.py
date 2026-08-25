# -*- coding: utf-8 -*-
"""Rehace el índice del registro leyendo `datos/auditoria/`."""
from django.core.management.base import BaseCommand

from nucleo.auditoria import core


class Command(BaseCommand):
    help = "Rehace el índice de auditoría leyendo el texto."

    def handle(self, *args, **opciones):
        cuantas = core.reconstruir_indice()
        self.stdout.write("Índice de auditoría rehecho: %d acción(es)." % cuantas)
