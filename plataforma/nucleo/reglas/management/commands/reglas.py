# -*- coding: utf-8 -*-
"""Qué reglas tiene un proyecto, y qué identificador sigue.

    python manage.py reglas cimiento-el-estandar
    python manage.py reglas cimiento-el-estandar --prefijo M
"""
from django.core.management.base import BaseCommand

from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import catalogo, numeracion


class Command(BaseCommand):
    help = "El cuerpo de reglas de un proyecto, y el siguiente identificador"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--prefijo", default="")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        raiz = proyecto.ruta_codigo
        try:
            cuenta = catalogo.resumen(raiz)
        except catalogo.NoHayCuerpoDeReglas as porque:
            self.stdout.write("%s" % ciclo.para_la_consola(str(porque)))
            return

        if not cuenta["todas"]:
            self.stdout.write("Ese proyecto no tiene cuerpo de reglas.")
            return

        self.stdout.write(
            "Reglas: %d  ·  vigentes: %d  ·  derogadas: %d  ·  blindadas: %d  "
            "·  capítulos: %d"
            % (cuenta["todas"], cuenta["vigentes"], cuenta["derogadas"],
               cuenta["blindadas"], cuenta["prefijos"]))
        self.stdout.write("")

        agrupadas = catalogo.por_prefijo(raiz)
        prefijos = ([opciones["prefijo"]] if opciones["prefijo"]
                    else sorted(agrupadas))
        for prefijo in prefijos:
            reglas = agrupadas.get(prefijo, [])
            if not reglas:
                self.stdout.write("  %-5s sin reglas" % prefijo)
                continue
            derogadas = sum(1 for una in reglas if una.derogada)
            self.stdout.write(
                "  %-5s %3d regla(s)%s  ·  el siguiente sería %s"
                % (prefijo, len(reglas),
                   (", %d derogada(s)" % derogadas) if derogadas else "",
                   numeracion.siguiente_libre(raiz, prefijo)))

        self.stdout.write("")
        self.stdout.write("**Ningún identificador se reutiliza**, ni el de una "
                          "derogada: una cita escrita hace un año apuntaría a "
                          "otra cosa sin que nadie lo note.")
