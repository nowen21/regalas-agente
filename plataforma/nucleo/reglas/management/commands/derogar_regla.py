# -*- coding: utf-8 -*-
"""Deroga una regla: la marca, **sin borrarla**.

    python manage.py derogar_regla cimiento-el-estandar M20 --en 38.0.0 --ver M5 --porque "Lo que exigía lo exige M5."
"""
from django.core.management.base import BaseCommand

from nucleo.auditoria.core import con_constancia
from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import redaccion


class Command(BaseCommand):
    help = "Deroga una regla, conservando su texto y su identificador"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("identificador")
        parser.add_argument("--en", required=True, dest="version",
                            help="en qué versión deja de regir")
        parser.add_argument("--ver", required=True,
                            help="a qué regla mirar en su lugar")
        parser.add_argument("--porque", required=True,
                            help="por qué deja de regir")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        try:
            ruta = con_constancia(
                lambda comprobante: redaccion.derogar(
                    proyecto.ruta_codigo, opciones["identificador"],
                    opciones["version"], opciones["ver"], opciones["porque"]),
                que_se_hizo="derogar una regla",
                sobre_que=opciones["identificador"], quien="el usuario",
                proyecto=opciones["proyecto"],
                que_cambio="deja de regir en %s, ver %s"
                           % (opciones["version"], opciones["ver"]))
        except redaccion.NoSePuedeTocar as porque:
            self.stdout.write("No se derogó: %s"
                              % ciclo.para_la_consola(str(porque)))
            return

        self.stdout.write("Derogada %s en %s"
                          % (opciones["identificador"],
                             ciclo.para_la_consola(ruta)))
        self.stdout.write("**Su texto se conserva y su identificador queda "
                          "ocupado para siempre.**")
