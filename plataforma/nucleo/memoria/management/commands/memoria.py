# -*- coding: utf-8 -*-
"""La memoria de un proyecto: verla, buscarla, corregirla y darla de baja.

    python manage.py memoria cimiento-el-estandar
    python manage.py memoria cimiento-el-estandar --buscar commit
    python manage.py memoria cimiento-el-estandar --dar-de-baja x.md --porque "..."
"""
from django.core.management.base import BaseCommand

from nucleo.auditoria.core import con_constancia
from nucleo.ciclo_de_vida import core as ciclo
from nucleo.memoria import core


class Command(BaseCommand):
    help = "Ver, buscar, corregir y dar de baja la memoria de un proyecto"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--buscar", default="")
        parser.add_argument("--dar-de-baja", default="", dest="baja")
        parser.add_argument("--porque", default="")
        parser.add_argument("--con-el-texto", action="store_true",
                            dest="con_texto")

    def handle(self, *args, **opciones):
        proyecto = opciones["proyecto"]
        try:
            if opciones["baja"]:
                self._baja(proyecto, opciones["baja"], opciones["porque"])
                return
            self._mirar(proyecto, opciones["buscar"], opciones["con_texto"])
        except core.NoHayMemoria as porque:
            self.stdout.write("%s" % ciclo.para_la_consola(str(porque)))

    def _mirar(self, proyecto, palabra, con_texto):
        cuenta = core.resumen(proyecto)
        self.stdout.write("Recuerdos: %d  ·  vigentes: %d  ·  dados de baja: %d"
                          % (cuenta["todos"], cuenta["vigentes"],
                             cuenta["de_baja"]))
        self.stdout.write("")

        encontrados = core.buscar(proyecto, palabra)
        if not encontrados:
            if palabra:
                self.stdout.write("Ningún recuerdo vigente habla de «%s». **No "
                                  "es que no haya memoria:** es que no hay nada "
                                  "guardado de ese tema."
                                  % ciclo.para_la_consola(palabra))
            else:
                self.stdout.write("No hay ningún recuerdo vigente.")
            return

        if palabra:
            self.stdout.write("%d hablan de «%s»:"
                              % (len(encontrados), ciclo.para_la_consola(palabra)))
        for uno in encontrados:
            self.stdout.write("  %-42s %s"
                              % (ciclo.para_la_consola(uno["nombre"]),
                                 ciclo.para_la_consola(uno["titulo"][:70])))
            if con_texto:
                self.stdout.write("")
                self.stdout.write(ciclo.para_la_consola(uno["texto"]))

    def _baja(self, proyecto, nombre, porque):
        if not porque:
            self.stdout.write("Hace falta --porque: dar de baja sin decir por "
                              "qué deja el recuerdo sin explicación.")
            return
        ruta = con_constancia(
            lambda comprobante: core.dar_de_baja(proyecto, nombre, porque),
            que_se_hizo="dar de baja un recuerdo", sobre_que=nombre,
            quien="el usuario", proyecto=proyecto, que_cambio=porque)
        self.stdout.write("Dado de baja: %s" % ciclo.para_la_consola(ruta))
        self.stdout.write("**No se borró.** Deja de entregarse al agente, y "
                          "sigue ahí para entender por qué se creyó.")
