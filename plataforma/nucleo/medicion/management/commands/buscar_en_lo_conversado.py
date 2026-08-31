# -*- coding: utf-8 -*-
"""Busca una palabra en lo conversado y dice en qué mensaje se dijo."""
from django.core.management.base import BaseCommand

from nucleo.medicion import core


class Command(BaseCommand):
    help = "Busca en las conversaciones indexadas."

    def add_arguments(self, parser):
        parser.add_argument("texto", help="lo que se busca")
        parser.add_argument("--limite", type=int, default=20)

    def handle(self, *args, **opciones):
        encontrados = core.buscar(opciones["texto"], limite=opciones["limite"])
        if not encontrados:
            # **Dos silencios distintos, y se dicen distinto.** Que no haya
            # nada indexado no es lo mismo que no haber encontrado nada.
            if not core.hay_algo_indexado():
                self.stdout.write(
                    "No hay conversaciones indexadas todavía: "
                    "corre `indexar_conversaciones` primero.")
            else:
                self.stdout.write(
                    "Ninguna conversación dice «%s»." % opciones["texto"])
            return

        for mensaje in encontrados:
            self.stdout.write(
                "%s · %s · %s: %s"
                % (mensaje.sesion.fecha, mensaje.sesion.archivo,
                   mensaje.quien, mensaje.texto[:120].replace("\n", " ")))
        self.stdout.write("%d mensaje(s)." % len(encontrados))
