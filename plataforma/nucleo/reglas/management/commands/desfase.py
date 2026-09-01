# -*- coding: utf-8 -*-
"""Si un proyecto quedó atrás, y qué cambió desde entonces.

    python manage.py desfase cimiento-el-estandar
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import desfase


class Command(BaseCommand):
    help = "Dice si un proyecto quedó atrás, y qué cambió desde entonces"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--cuantas", type=int, default=8)

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        revision = desfase.revisar(proyecto.version_reglas)
        self.stdout.write("Declara: %s  ·  el estándar va en %s"
                          % (proyecto.version_reglas or "nada",
                             desfase.version_del_estandar()))
        self.stdout.write("")
        self.stdout.write(ciclo.para_la_consola(desfase.dicho(revision)))

        if not revision["cambios"]:
            return
        self.stdout.write("")
        self.stdout.write("Versiones que pasaron:")
        for version, tipo, titulo in revision["cambios"][:opciones["cuantas"]]:
            self.stdout.write("  %-9s %-7s %s"
                              % (version, tipo, ciclo.para_la_consola(titulo)))
        if len(revision["cambios"]) > opciones["cuantas"]:
            self.stdout.write("  ... y %d más."
                              % (len(revision["cambios"]) - opciones["cuantas"]))
