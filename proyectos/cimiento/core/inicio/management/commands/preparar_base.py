# -*- coding: utf-8 -*-
"""Deja lista la base de Cimiento: la crea si falta y le aplica las migraciones.

    python manage.py preparar_base

Repetirla no cambia nada: la base ya está y no quedan migraciones. La corre la
instalación del estándar antes de poner los enganches.
"""
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from core.comun.consola import preparar_salida
from core.inicio.base_de_datos import BaseDeDatos, BaseInalcanzable


class Command(BaseCommand):
    help = "Crea la base de Cimiento si falta y le aplica las migraciones."

    def handle(self, *args, **opciones):
        preparar_salida()
        base = BaseDeDatos()
        try:
            creada = base.crear_si_falta()
        except BaseInalcanzable as error:
            # CommandError sale sin traza de Python y con código de error.
            raise CommandError(str(error))

        call_command("migrate", interactive=False, verbosity=0)
        pasadas = base.pasar_a_innodb()
        if pasadas:
            self.stdout.write(f"{len(pasadas)} tabla(s) pasaron de MyISAM a InnoDB.")
        cuando = "se creó ahora y " if creada else ""
        self.stdout.write(f"La base «{base.nombre}» en {base.donde} {cuando}está lista, "
                          f"sin migraciones pendientes.")
