# -*- coding: utf-8 -*-
"""Dice si se puede publicar: corre todo lo que ya funcionaba.

    python manage.py puerta_de_publicacion cimiento-el-estandar
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.comprobaciones import puerta


class Command(BaseCommand):
    help = "Corre lo que ya funcionaba y dice si se puede publicar"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")

    def handle(self, *args, **opciones):
        revision = puerta.revisar_antes_de_publicar(opciones["proyecto"])

        if not revision.se_pudo:
            self.stdout.write("No se pudo revisar: %s"
                              % ciclo.para_la_consola(revision.porque))
            self.stdout.write("**Sin revisar no se publica.**")
            return

        veredicto = revision.veredicto
        self.stdout.write("Comprobaciones: %d corridas, %d con fallas"
                          % (veredicto.corridas, veredicto.con_fallas))
        self.stdout.write("Pruebas: %s"
                          % ("en verde" if revision.pruebas["verdes"]
                             else "**con rojas**"))
        self.stdout.write("Tardó %.1f s" % revision.segundos)
        self.stdout.write("")

        if revision.rehacer:
            self.stdout.write("Hay que rehacer %d funcionalidad(es): %s"
                              % (len(revision.rehacer),
                                 ", ".join(revision.rehacer)))
        if revision.sin_verificar:
            self.stdout.write("Sin verificar, y no detienen: %d (%s)"
                              % (len(revision.sin_verificar),
                                 ", ".join(revision.sin_verificar[:8])
                                 + (", ..." if len(revision.sin_verificar) > 8
                                    else "")))
        self.stdout.write("")

        if revision.pasa:
            self.stdout.write("Se puede publicar.")
        else:
            self.stdout.write("**No se publica.** Algo que servía dejó de "
                              "servir, o hay funcionalidades por rehacer.")
