# -*- coding: utf-8 -*-
"""Qué reglas opcionales rigen en un proyecto, y encender o apagar una.

    python manage.py que_rige cimiento-el-estandar
    python manage.py que_rige cimiento-el-estandar --encender DOC5 --cuando 2026-09-01
    python manage.py que_rige cimiento-el-estandar --apagar DOC5 --cuando 2026-09-01
"""
import os

from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core
from nucleo.proyectos import configuracion
from nucleo.proyectos.models import Proyecto


class Command(BaseCommand):
    help = "Qué reglas opcionales rigen en un proyecto"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--encender", default="", help="identificador de regla")
        parser.add_argument("--apagar", default="", help="identificador de regla")
        parser.add_argument("--cuando", default="",
                            help="la fecha que queda escrita, AAAA-MM-DD")
        parser.add_argument("--quien", default="el usuario")

    def handle(self, *args, **opciones):
        try:
            registrado = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("El proyecto %s no está conectado."
                              % opciones["proyecto"])
            return
        raiz_proyecto = registrado.ruta_codigo
        # La raíz del estándar es la carpeta que contiene `plantillas/`; se
        # deriva de ahí para no tener dos formas de decir dónde está.
        raiz_estandar = os.path.dirname(core._carpeta_de_plantillas())

        if opciones["encender"] or opciones["apagar"]:
            self._poner(raiz_proyecto, raiz_estandar, opciones)
            return

        entregado = configuracion.para_el_agente(raiz_proyecto, raiz_estandar)
        self.stdout.write(core.para_la_consola(configuracion.dicho(entregado)))
        if entregado["encendidas"]:
            self.stdout.write("")
            self.stdout.write("Encendidas: %s"
                              % ", ".join(entregado["encendidas"]))
        self.stdout.write("")
        self.stdout.write("Apagadas (%d): %s" % (
            len(entregado["apagadas"]), ", ".join(entregado["apagadas"])))

    def _poner(self, raiz_proyecto, raiz_estandar, opciones):
        cual = opciones["encender"] or opciones["apagar"]
        estado = (configuracion.ENCENDIDA if opciones["encender"]
                  else configuracion.APAGADA)
        if not opciones["cuando"]:
            self.stdout.write("Falta --cuando: la fecha queda escrita en el "
                              "archivo, y no se inventa.")
            return
        try:
            puesta = configuracion.poner(
                raiz_proyecto, cual, estado, raiz_estandar,
                opciones["cuando"], opciones["quien"],
                proyecto=opciones["proyecto"])
        except configuracion.NoSePuedeApagar as porque:
            self.stdout.write("No se hizo: %s"
                              % core.para_la_consola(str(porque)))
            return
        self.stdout.write("%s quedó %s el %s, por %s." % (
            puesta["regla"], puesta["estado"], puesta["desde"], puesta["quien"]))
        self.stdout.write("Escrito en %s" % core.para_la_consola(puesta["ruta"]))
