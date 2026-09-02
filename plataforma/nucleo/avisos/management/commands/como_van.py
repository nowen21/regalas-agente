# -*- coding: utf-8 -*-
"""Cómo va cada proyecto conectado, con la misma medida para todos.

    python manage.py como_van --hoy 2026-09-01
"""
from django.core.management.base import BaseCommand

from nucleo.avisos import core, reporte
from nucleo.ciclo_de_vida import core as consola


class Command(BaseCommand):
    help = "El avance, la deuda y lo que lleva quieto, proyecto por proyecto"

    def add_arguments(self, parser):
        parser.add_argument("--hoy", required=True, help="AAAA-MM-DD")
        parser.add_argument("--dias", type=int, default=core.DIAS)

    def handle(self, *args, **opciones):
        filas = reporte.de_todos(opciones["hoy"], opciones["dias"])
        self.stdout.write(consola.para_la_consola(reporte.dicho(filas)))
