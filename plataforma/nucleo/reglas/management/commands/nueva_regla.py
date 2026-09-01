# -*- coding: utf-8 -*-
"""Escribe una regla nueva, después de mostrar las que se le parecen.

    python manage.py nueva_regla cimiento-el-estandar --prefijo M --titulo "..." --capitulo base/20-meta-reglas --nombre "20 · Meta-reglas"

Sin `--igual-la-escribo` **no escribe nada**: solo muestra qué identificador le
tocaría y qué reglas vigentes hablan de lo mismo.
"""
from django.core.management.base import BaseCommand

from nucleo.auditoria.core import con_constancia
from nucleo.ciclo_de_vida import core as ciclo
from nucleo.proyectos.models import Proyecto
from nucleo.reglas import numeracion, parecidas, redaccion


class Command(BaseCommand):
    help = "Escribe una regla nueva, con su identificador y su molde"

    def add_arguments(self, parser):
        parser.add_argument("proyecto")
        parser.add_argument("--prefijo", required=True)
        parser.add_argument("--titulo", required=True)
        parser.add_argument("--capitulo", default="",
                            help="carpeta del capítulo, del estilo de base/20-meta-reglas")
        parser.add_argument("--nombre", default="",
                            help="cómo se nombra el capítulo en la primera línea")
        parser.add_argument("--igual-la-escribo", action="store_true",
                            dest="escribir")

    def handle(self, *args, **opciones):
        try:
            proyecto = Proyecto.objects.get(identificador=opciones["proyecto"])
        except Proyecto.DoesNotExist:
            self.stdout.write("No hay un proyecto registrado con ese nombre.")
            return

        raiz = proyecto.ruta_codigo
        titulo = opciones["titulo"]
        prefijo = opciones["prefijo"]

        identificador = numeracion.siguiente_libre(raiz, prefijo)
        self.stdout.write("Identificador que le tocaría: %s" % identificador)
        self.stdout.write("")

        encontradas = parecidas.parecidas_a(raiz, titulo, prefijo)
        self.stdout.write(ciclo.para_la_consola(parecidas.aviso(encontradas)))
        for una, comunes in encontradas:
            self.stdout.write("  %-8s %s"
                              % (una.id, ciclo.para_la_consola(una.titulo)))
            self.stdout.write("           en común: %s"
                              % ciclo.para_la_consola(", ".join(comunes)))

        if not opciones["escribir"]:
            self.stdout.write("")
            self.stdout.write("No se escribió nada. Con --igual-la-escribo se "
                              "escribe.")
            return

        if not opciones["capitulo"] or not opciones["nombre"]:
            self.stdout.write("")
            self.stdout.write("Para escribirla hacen falta --capitulo y "
                              "--nombre.")
            return

        try:
            identificador, ruta = con_constancia(
                lambda comprobante: redaccion.crear(
                    raiz, opciones["capitulo"], prefijo, titulo,
                    opciones["nombre"]),
                que_se_hizo="escribir una regla nueva",
                sobre_que=titulo, quien="el usuario",
                proyecto=opciones["proyecto"])
        except (numeracion.IdentificadorYaUsado,
                redaccion.NoSePuedeTocar) as porque:
            self.stdout.write("")
            self.stdout.write("No se escribió: %s"
                              % ciclo.para_la_consola(str(porque)))
            return

        self.stdout.write("")
        self.stdout.write("Escrita %s en %s"
                          % (identificador, ciclo.para_la_consola(ruta)))
        self.stdout.write("**Nace con sus huecos puestos:** el cuerpo y el "
                          "ejemplo están por llenar, y se ve.")
